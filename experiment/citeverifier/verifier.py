#!/usr/bin/env python3

import asyncio
import logging
from math import log
import time
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import sys
import os
import sqlite3
import pandas as pd
from tqdm import tqdm
from grobid_client.grobid_client import GrobidClient

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parser.llm_parser import llm_str2ref
from checker.models import Reference, ExternalReference, convert_parsed_reference, convert_parsed_references, VerificationResult, VerificationStatus
from checker.clients.scrapingdog_client import ScrapingDogClient
from checker.clients.google_search_client import GoogleSearchClient
from checker.utils import StringUtils, AuthorUtils
from unified_database import (
    UnifiedDatabase, 
    ScholarRecord, 
    create_scholar_record_from_external_reference
)
from reference_storage_service import ReferenceStorageService, StorageIntegratedFileProcessor
import csv

from checker.logger_config import setup_logging

# Set up logging
log_filename = setup_logging(log_to_file=True, log_level="DEBUG")
if log_filename:
    print(f"Logs will be saved to: {log_filename}")

logger = logging.getLogger(__name__)


@dataclass
class VerificationStats:
    """Verification statistics"""
    total_searches: int = 0
    successful_searches: int = 0
    failed_searches: int = 0
    cache_hits: int = 0
    api_calls: int = 0
    total_results_found: int = 0
    verified_valid: int = 0
    verified_invalid: int = 0
    verified_suspicious: int = 0
    verified_unverified: int = 0
    verified_error: int = 0
    google_fallback_used: int = 0
    google_fallback_successful: int = 0
    llm_reparse_used: int = 0
    llm_reparse_successful: int = 0
    total_time: float = 0.0
    start_time: Optional[float] = None
    end_time: Optional[float] = None

    def update_verification_status(self, status: VerificationStatus):
        """Update verification status statistics"""
        if status == VerificationStatus.VALID:
            self.verified_valid += 1
        elif status == VerificationStatus.INVALID:
            self.verified_invalid += 1
        elif status == VerificationStatus.SUSPICIOUS:
            self.verified_suspicious += 1
        elif status == VerificationStatus.UNVERIFIED:
            self.verified_unverified += 1
        elif status == VerificationStatus.ERROR:
            self.verified_error += 1

    def print_statistics(self):
        """Print statistics"""
        print("\n" + "="*60)
        print("Verification Statistics")
        print("="*60)
        print(f"Total verifications: {self.total_searches}")
        print(f"Successful searches: {self.successful_searches}")
        print(f"Failed searches: {self.failed_searches}")
        print(f"Cache hits: {self.cache_hits}")
        print(f"API calls: {self.api_calls}")
        print(f"Total results found: {self.total_results_found}")
        print()
        print("Verification result distribution:")
        print(f"  Valid (VALID): {self.verified_valid}")
        print(f"  Invalid (INVALID): {self.verified_invalid}")
        print(f"  Suspicious (SUSPICIOUS): {self.verified_suspicious}")
        print(f"  Unverified (UNVERIFIED): {self.verified_unverified}")
        print(f"  Error (ERROR): {self.verified_error}")
        print()
        print("Google search fallback statistics:")
        print(f"  Used count: {self.google_fallback_used}")
        print(f"  Successful count: {self.google_fallback_successful}")
        print()
        print("LLM reparse statistics:")
        print(f"  Used count: {self.llm_reparse_used}")
        print(f"  Successful count: {self.llm_reparse_successful}")
        print(f"Total time: {self.total_time:.2f} seconds")
        
        if self.total_searches > 0:
            success_rate = (self.successful_searches / self.total_searches) * 100
            cache_rate = (self.cache_hits / self.total_searches) * 100
            valid_rate = (self.verified_valid / self.total_searches) * 100
            avg_time = self.total_time / self.total_searches
            print(f"Search success rate: {success_rate:.1f}%")
            print(f"Cache hit rate: {cache_rate:.1f}%")
            print(f"Verification valid rate: {valid_rate:.1f}%")
            if self.google_fallback_used > 0:
                google_success_rate = (self.google_fallback_successful / self.google_fallback_used) * 100
                print(f"Google fallback success rate: {google_success_rate:.1f}%")
            if self.llm_reparse_used > 0:
                llm_success_rate = (self.llm_reparse_successful / self.llm_reparse_used) * 100
                print(f"LLM reparse success rate: {llm_success_rate:.1f}%")
            print(f"Average time: {avg_time:.2f} seconds/item")
        
        print("="*60)


class VerificationStrategy:
    """验证策略基类"""
    
    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        """执行验证"""
        raise NotImplementedError


class DblpVerificationStrategy(VerificationStrategy):
    """Local DBLP matching strategy (runs before online matching)."""

    def __init__(
        self,
        validator: 'ReferenceValidator',
        dblp_db_path: Optional[str],
        dblp_match_threshold: float = 0.9,
        max_candidates: int = 100000,
    ):
        self.validator = validator
        self.dblp_db_path = Path(dblp_db_path) if dblp_db_path else None
        self.dblp_match_threshold = dblp_match_threshold
        self.max_candidates = max_candidates
        self._use_index: Optional[bool] = None
        self._conn: Optional[sqlite3.Connection] = None
        self._all_titles: Optional[List[Any]] = None

    def _ensure_ready(self) -> bool:
        if not self.dblp_db_path or not self.dblp_db_path.exists():
            return False

        if self._use_index is None:
            # Decide the fastest strategy once: indexed search or full DB load.
            from dblp_match import _db_has_word_index, load_all_titles_from_db

            conn = sqlite3.connect(str(self.dblp_db_path))
            self._use_index = _db_has_word_index(conn)
            conn.close()

            if not self._use_index:
                self._all_titles = load_all_titles_from_db(self.dblp_db_path)

        if self._use_index and self._conn is None:
            # Keep a read-only connection for low-memory indexed search.
            from dblp_match import _sqlite_readonly_fast

            self._conn = sqlite3.connect(str(self.dblp_db_path))
            _sqlite_readonly_fast(self._conn)

        return True

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        if not reference.title:
            return None
        if not self._ensure_ready():
            return None

        from dblp_match import search_dblp_by_index, search_dblp_brute_force

        if self._use_index:
            assert self._conn is not None
            # Indexed search: fast candidate selection + ratio matching.
            match = search_dblp_by_index(self._conn, reference.title, self.max_candidates)
        else:
            assert self._all_titles is not None
            # Brute force: ratio matching over all titles (memory-heavy fallback).
            match = search_dblp_brute_force(self._all_titles, reference.title)

        if not match:
            return None

        external_ref = ExternalReference(
            title=match.get("dblp_title"),
            authors=None,
            year=None,
            venue=None,
            url=None,
            source="dblp",
            metadata={
                "dblp_id": match.get("dblp_id"),
                "dblp_title_similarity": match.get("dblp_title_similarity"),
            },
        )

        result = self.validator.validate_external_reference(reference, external_ref, "DBLP match")
        if match.get("dblp_title_similarity", 0.0) < self.dblp_match_threshold:
            result.verification_notes.append(
                f"DBLP title similarity below threshold: {match.get('dblp_title_similarity', 0.0):.2f} < {self.dblp_match_threshold:.2f}"
            )
        return result


class CacheVerificationStrategy(VerificationStrategy):
    """缓存验证策略"""
    
    def __init__(self, db: UnifiedDatabase, validator: 'ReferenceValidator'):
        self.db = db
        self.validator = validator
    
    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        """Cache verification"""
        cached_result = self.db.search_scholar_by_title(reference.title)
        if cached_result:
            logger.info(f"Reference {reference.id} found in cache, performing verification...")
            external_ref = self._create_external_ref_from_record(cached_result)
            return self.validator.validate_external_reference(reference, external_ref, "缓存验证")
        return None
    
    def _create_external_ref_from_record(self, record: ScholarRecord):
        """Create ExternalReference from database record"""
        from checker.models import ExternalReference
        
        return ExternalReference(
            title=record.title,
            authors=record.authors.split(', ') if record.authors else [],
            year=record.year,
            venue=record.venue,
            url=record.url,
            source="scrapingdog"
        )


class APIVerificationStrategy(VerificationStrategy):
    """API验证策略"""
    
    def __init__(self, validator: 'ReferenceValidator', storage_service: 'ReferenceStorageService' = None):
        self.validator = validator
        self.storage_service = storage_service
    
    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        """通过API验证"""
        scrapingdog_client = clients.get('scrapingdog')
        if scrapingdog_client:
            try:
                external_ref = await scrapingdog_client.search_reference(reference)
                if external_ref:
                    # Store search results
                    if self.storage_service:
                        search_query = reference.title if reference.title else ""
                        self.storage_service.store_search_result(external_ref, search_query, 1)
                    
                    return self.validator.validate_external_reference(reference, external_ref, "ScrapingDog验证")
            except Exception as e:
                logger.warning(f"ScrapingDog搜索失败: {reference.id}, 错误: {e}")
        return None


class GoogleFallbackStrategy(VerificationStrategy):
    """Google搜索fallback策略"""
    
    def __init__(self, validator: 'ReferenceValidator', storage_service: 'ReferenceStorageService' = None):
        self.validator = validator
        self.storage_service = storage_service
    
    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        """Google搜索fallback验证"""
        google_client = clients.get('google')
        if google_client:
            try:
                external_ref = await google_client.search_reference(reference)
                if external_ref:
                    # 存储搜索结果
                    if self.storage_service:
                        search_query = reference.title if reference.title else ""
                        self.storage_service.store_search_result(external_ref, search_query, 1)
                    
                    return self.validator.validate_external_reference(reference, external_ref, "Google搜索验证")
            except Exception as e:
                logger.warning(f"Google搜索失败: {reference.id}, 错误: {e}")
        return None


class LLMReparseStrategy(VerificationStrategy):
    """LLM重解析策略"""
    
    def __init__(self, validator: 'ReferenceValidator', llm_reparser: 'LLMReparser', 
                 storage_service: 'ReferenceStorageService' = None):
        self.validator = validator
        self.llm_reparser = llm_reparser
        self.storage_service = storage_service
    
    async def verify(self, reference: Reference, clients: Dict[str, Any]) -> Optional[VerificationResult]:
        """LLM重解析后验证"""
        reparsed_dict = await self.llm_reparser.reparse_with_llm(reference)
        if reparsed_dict:
            reparsed_reference = convert_parsed_reference(reparsed_dict, reparsed_dict['id'])
            if self.storage_service:
                self._store_llm_reparsed_result(reference, reparsed_dict)
            if reparsed_reference:
                # 先尝试ScrapingDog，再尝试Google
                for client_name, method_suffix in [('scrapingdog', 'ScrapingDog'), ('google', 'Google搜索')]:
                    client = clients.get(client_name)
                    if client:
                        try:
                            external_ref = await client.search_reference(reparsed_reference)
                            if external_ref:
                                # 存储搜索结果
                                if self.storage_service:
                                    search_query = reparsed_reference.title if reparsed_reference.title else ""
                                    self.storage_service.store_search_result(external_ref, search_query, 1)
                                
                                result = self.validator.validate_external_reference(
                                    reparsed_reference, external_ref, f"{method_suffix}LLM重解析+验证"
                                )

                                if result.final_status == VerificationStatus.VALID:
                                    result.sources_checked = [client_name, "llm_reparse"]
                                    result.verification_notes.append("LLM重解析后验证成功")
                                    
                        
                                    
                                    return result
                                else:
                                    result.sources_checked = [client_name, "llm_reparse"]
                                    result.verification_notes.append("LLM重解析后验证失败")
                                    return result
                        except Exception as e:
                            logger.warning(f"{method_suffix}搜索失败: {reference.id}, 错误: {e}")
        return None
    
    def _store_llm_reparsed_result(self, original_reference: Reference, reparsed_dict: dict):
        """
        存储LLM重解析后的结果
        
        Args:
            original_reference: 原始参考文献
            reparsed_dict: LLM重解析后的字典结果
        """
        try:
            from parsed_references_database import ParsedReferenceRecord
            
            # 创建LLM重解析后的记录
            record = ParsedReferenceRecord(
                # 使用重解析后的信息作为主要信息
                title=reparsed_dict.get('title'),
                authors=', '.join(reparsed_dict.get('authors', [])) if reparsed_dict.get('authors') else None,
                venue=reparsed_dict.get('venue'),
                year=reparsed_dict.get('year'),
                reference_type=reparsed_dict.get('reference_type', 'unknown'),
                raw_text=reparsed_dict.get('raw'),
                
                # LLM重解析标识
                is_llm_reparsed=True,
                
                # 保存原始解析信息
                original_title=original_reference.title,
                original_authors=', '.join(original_reference.authors) if original_reference.authors else None,
                original_venue=original_reference.venue,
                original_year=original_reference.year,
                
                # 元数据
                source_file=f"llm_reparse_{original_reference.id}",
                parser_version="llm_reparse"
            )
            
            # 存储记录
            record_id = self.storage_service.parsed_refs_db.insert_parsed_reference(record, ignore_duplicates=True)
            
            if record_id:
                self.storage_service.stats['llm_reparsed'] += 1
                logger.info(f"已存储LLM重解析结果: {original_reference.id} -> {reparsed_dict.get('title', '')[:50]}...")
            else:
                logger.debug(f"LLM重解析结果重复，跳过存储: {original_reference.id}")
                
        except Exception as e:
            logger.error(f"存储LLM重解析结果失败: {original_reference.id}, 错误: {e}")
            self.storage_service.stats['errors'] += 1


class ReferenceValidator:
    """参考文献验证器"""
    
    def validate_external_reference(self, input_ref: Reference, external_ref, method: str = "API搜索") -> VerificationResult:
        """验证外部文献信息"""
        start_time = time.time()
        
        # 1. 标题匹配检查
        title_similarity = 0.0
        problematic_fields = []
        
        if input_ref.title and external_ref.title:
            # 使用增强的标题相似度计算
            title_similarity = StringUtils.enhanced_title_similarity(input_ref.title, external_ref.title)
            
            if title_similarity <= 0.9:  # 标题相似度阈值
                return VerificationResult(
                    reference_id=input_ref.id,
                    final_status=VerificationStatus.INVALID,
                    diagnosis="标题严重错误",
                    problematic_fields=["title"],
                    best_match=external_ref,
                    sources_checked=[external_ref.source] if external_ref.source else ["unknown"],
                    total_time=time.time() - start_time,
                    verification_notes=[f"标题相似度: {title_similarity:.2f}"],
                    recommendations=["检查标题是否正确"]
                )
        
        # 综合判断（简化版本）
        diagnosis = "验证通过"
        status = VerificationStatus.VALID
        
        return VerificationResult(
            reference_id=input_ref.id,
            final_status=status,
            diagnosis=diagnosis,
            problematic_fields=problematic_fields,
            best_match=external_ref,
            sources_checked=[external_ref.source] if external_ref.source else ["unknown"],
            total_time=time.time() - start_time,
            verification_notes=[f"标题相似度: {title_similarity:.2f}"],
            recommendations=self._generate_recommendations(status, problematic_fields)
        )
    
    def _generate_recommendations(self, status: VerificationStatus, problematic_fields: list) -> list:
        """生成建议"""
        recommendations = []
        
        if status == VerificationStatus.VALID:
            recommendations.append("文献验证通过")
        elif status == VerificationStatus.SUSPICIOUS:
            if "title" in problematic_fields:
                recommendations.append("检查标题是否正确")
            if "authors" in problematic_fields:
                recommendations.append("检查作者信息")
            if "year" in problematic_fields:
                recommendations.append("检查发表年份")
        elif status == VerificationStatus.INVALID:
            recommendations.append("文献信息错误，需要修正")
        else:
            recommendations.append("无法验证文献")
        
        return recommendations


class LLMReparser:
    """LLM重解析器"""
    
    async def reparse_with_llm(self, reference) -> Optional[dict]:
        """
        使用LLM重新解析参考文献的原始文本
        
        Args:
            reference: 原始参考文献对象，可以是Reference类型或字典类型
            
        Returns:
            重新解析后的参考文献字典，如果解析失败返回None
        """
        # 处理不同的输入类型
        if isinstance(reference, dict):
            ref_id = reference.get('id')
            raw_text = reference.get('raw')
            ref_type = reference.get('reference_type', 'unknown')
        else:
            ref_id = reference.id
            raw_text = reference.raw
            ref_type = reference.reference_type if hasattr(reference, 'reference_type') else 'unknown'
        
        if not raw_text:
            logger.warning(f"参考文献 {ref_id} 没有原始文本，无法进行LLM重解析")
            return None
        
        try:
            logger.info(f"使用LLM重新解析参考文献 {ref_id}: {raw_text[:50]}...")
            
            # 使用异步信号量来限制并发
            semaphore = asyncio.Semaphore(1)  # 限制LLM调用并发数
            
            # 调用LLM解析
            parsed_data = await llm_str2ref(raw_text, semaphore)
            
            if not parsed_data or not parsed_data.get('title'):
                logger.warning(f"LLM解析结果为空或缺少标题: {ref_id}")
                return None
            
            # 保留原始信息
            parsed_data['id'] = ref_id
            parsed_data['raw'] = raw_text
            parsed_data['reference_type'] = ref_type
            
            logger.info(f"LLM重解析成功: {ref_id} -> {parsed_data['title'][:50]}...")
            return parsed_data
            
        except Exception as e:
            logger.error(f"LLM重解析失败: {ref_id}, 错误: {e}")
            return None


class VerificationChain:
    """验证链 - 按顺序执行不同的验证策略"""
    
    def __init__(self, strategies: List[VerificationStrategy]):
        self.strategies = strategies
    
    async def execute(self, reference: Reference, clients: Dict[str, Any], stats: VerificationStats) -> VerificationResult:
        """执行验证链"""
        start_time = time.time()
        sources_attempted = []
        verification_notes = []
        last_external_ref = None  # 保存最后一次的external_ref

        for strategy in self.strategies:
            try:
                result = await strategy.verify(reference, clients)
                if result:
                    # 保存最后一次的external_ref（即使验证失败）
                    if result.best_match:
                        last_external_ref = result.best_match

                    if result.final_status == VerificationStatus.VALID:
                        # 更新统计信息
                        if isinstance(strategy, CacheVerificationStrategy):
                            stats.cache_hits += 1
                        elif isinstance(strategy, APIVerificationStrategy):
                            stats.api_calls += 1
                            stats.successful_searches += 1
                            stats.total_results_found += 1
                        elif isinstance(strategy, GoogleFallbackStrategy):
                            stats.google_fallback_used += 1
                            stats.google_fallback_successful += 1
                        elif isinstance(strategy, LLMReparseStrategy):
                            stats.llm_reparse_used += 1
                            stats.llm_reparse_successful += 1

                        stats.update_verification_status(result.final_status)
                        return result
                    else:
                        # 记录尝试的策略
                        if isinstance(strategy, GoogleFallbackStrategy):
                            stats.google_fallback_used += 1
                            sources_attempted.append("google_search")
                        elif isinstance(strategy, LLMReparseStrategy):
                            stats.llm_reparse_used += 1
                            sources_attempted.append("llm_reparse")

                        verification_notes.extend(result.verification_notes or [])
            except Exception as e:
                logger.error(f"验证策略执行失败: {type(strategy).__name__}, 错误: {e}")
                verification_notes.append(f"{type(strategy).__name__}错误: {str(e)}")

        # 所有策略都失败，返回最后一次的external_ref而不是None
        stats.failed_searches += 1
        result = VerificationResult(
            reference_id=reference.id,
            final_status=VerificationStatus.INVALID,
            diagnosis="所有验证方法都未能验证文献",
            problematic_fields=[],
            best_match=last_external_ref,  # 使用最后一次的external_ref
            sources_checked=sources_attempted or ["scrapingdog"],
            total_time=time.time() - start_time,
            verification_notes=verification_notes,
            recommendations=["检查文献信息是否正确，可能需要手动验证"]
        )
        stats.update_verification_status(result.final_status)
        return result


class ScrapingDogVerifier:
    """ScrapingDog批量验证器"""
    
    def __init__(
        self,
        db_path: str = "scholar_results.db",
        max_concurrent: int = 3,
        parsed_refs_db_path: str = "parsed_references.db",
        dblp_db_path: Optional[str] = "dblp_titles.db",
        dblp_match_threshold: float = 0.9,
        dblp_max_candidates: int = 100000,
        enable_dblp: bool = True,
    ):
        """
        初始化验证器
        
        Args:
            db_path: 统一数据库文件路径（包含scholar_results和search_results表）
            max_concurrent: 最大并发数
            parsed_refs_db_path: 解析后参考文献数据库文件路径
        """
        self.db = UnifiedDatabase(db_path)
        self.max_concurrent = max_concurrent
        self.client: Optional[ScrapingDogClient] = None
        self.google_client: Optional[GoogleSearchClient] = None
        self.stats = VerificationStats()
        
        # 初始化组件
        self.validator = ReferenceValidator()
        self.llm_reparser = LLMReparser()
        
        # 初始化存储服务
        self.storage_service = ReferenceStorageService(parsed_refs_db_path, db_path)

        # DBLP matching configuration
        self.dblp_db_path = dblp_db_path
        self.dblp_match_threshold = dblp_match_threshold
        self.dblp_max_candidates = dblp_max_candidates
        self.enable_dblp = enable_dblp
        self.dblp_strategy: Optional[DblpVerificationStrategy] = None
        
        # 构建验证策略链
        self._build_verification_chain()
    
    def _build_verification_chain(self):
        """构建验证策略链"""
        strategies: List[VerificationStrategy] = []

        # DBLP match first (local, ratio-based)
        if self.enable_dblp:
            self.dblp_strategy = DblpVerificationStrategy(
                self.validator,
                self.dblp_db_path,
                self.dblp_match_threshold,
                self.dblp_max_candidates,
            )
            strategies.append(self.dblp_strategy)

        strategies.extend([
            CacheVerificationStrategy(self.db, self.validator),
            APIVerificationStrategy(self.validator, self.storage_service),
            GoogleFallbackStrategy(self.validator, self.storage_service),
            LLMReparseStrategy(self.validator, self.llm_reparser, self.storage_service),
        ])

        self.verification_chain = VerificationChain(strategies)
    
    async def __aenter__(self):
        """异步上下文管理器入口"""
        self.client = ScrapingDogClient()
        await self.client.initialize()
        
        self.google_client = GoogleSearchClient()
        await self.google_client.initialize()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        if self.client:
            await self.client.close()
        if self.google_client:
            await self.google_client.close()
        if self.storage_service:
            self.storage_service.close()
        if self.dblp_strategy:
            self.dblp_strategy.close()
    
    async def verify_single_reference(self, reference: Reference) -> VerificationResult:
        """
        验证单个参考文献
        
        Args:
            reference: 待验证的参考文献
            
        Returns:
            验证结果
        """
        logger.info(f"验证参考文献 {reference.id}: {reference.title[:50]}...")
        
        clients = {
            'scrapingdog': self.client,
            'google': self.google_client
        }
        
        result = await self.verification_chain.execute(reference, clients, self.stats)
        
        # 如果验证通过，存储到数据库缓存
        if result.final_status == VerificationStatus.VALID and result.best_match:
            record = create_scholar_record_from_external_reference(result.best_match)
            self.db.insert_scholar_result(record)
        
        return result
    
    async def verify_batch(self, references: List[Reference]) -> List[VerificationResult]:
        """
        批量验证参考文献
        
        Args:
            references: 待验证的参考文献列表
            
        Returns:
            验证结果列表
        """
        self.stats.start_time = time.time()
        self.stats.total_searches = len(references)
        
        logger.info(f"开始批量验证 {len(references)} 个参考文献，最大并发数: {self.max_concurrent}")
        
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async def verify_with_semaphore(ref: Reference) -> VerificationResult:
            async with semaphore:
                return await self.verify_single_reference(ref)
        
        # 创建所有验证任务
        tasks = [verify_with_semaphore(ref) for ref in references]
        
        # 执行任务并显示进度
        results = []
        completed = 0
        
        for task in asyncio.as_completed(tasks):
            try:
                result = await task
                results.append(result)
                completed += 1
                
                # 显示进度
                if completed % 10 == 0 or completed == len(references):
                    progress = (completed / len(references)) * 100
                    logger.info(f"进度: {completed}/{len(references)} ({progress:.1f}%)")
                    
            except Exception as e:
                logger.error(f"验证任务失败: {e}")
                completed += 1
        
        self.stats.end_time = time.time()
        self.stats.total_time = self.stats.end_time - self.stats.start_time
        
        logger.info(f"批量验证完成，耗时: {self.stats.total_time:.2f}秒")
        self.stats.print_statistics()
        
        return results
    
    def export_verification_results_to_csv_with_original(self, verification_results: List[VerificationResult], 
                                                        original_references: List[Reference], 
                                                        output_path: str) -> int:
        """
        导出验证结果到CSV文件（包含原始引用信息）
        """
        if not verification_results:
            logger.warning("没有验证结果可导出")
            return 0
        
        # 创建引用ID到引用的映射
        ref_map = {ref.id: ref for ref in original_references}
        
        # CSV字段定义
        fieldnames = [
            'reference_id', 'final_status', 'diagnosis', 'problematic_fields',
            'original_title', 'found_title', 'original_authors', 'found_authors',
            'original_year', 'found_year', 'found_venue', 'found_url',
            'title_similarity', 'author_similarity', 'verification_time',
            'sources_checked', 'llm_reparsed', 'verification_notes', 'recommendations'
        ]
        
        rows = []
        for result in verification_results:
            # 获取原始引用
            original_ref = ref_map.get(result.reference_id)
            
            # 提取相似度信息和LLM重解析标识
            title_similarity = 0.0
            author_similarity = 0.0
            llm_reparsed = False
            if result.verification_notes:
                for note in result.verification_notes:
                    if "标题相似度:" in note:
                        title_similarity = float(note.split(":")[1].strip())
                    elif "作者相似度:" in note:
                        author_similarity = float(note.split(":")[1].strip())
                    elif "LLM重解析后验证成功" in note:
                        llm_reparsed = True
            
            # 也检查sources_checked是否包含llm_reparse
            if result.sources_checked and "llm_reparse" in result.sources_checked:
                llm_reparsed = True
            
            # 准备行数据
            row_data = {
                'reference_id': result.reference_id,
                'final_status': result.final_status.value,
                'diagnosis': result.diagnosis,
                'problematic_fields': ';'.join(result.problematic_fields) if result.problematic_fields else '',
                'original_title': original_ref.title if original_ref else '',
                'found_title': result.best_match.title if result.best_match else '',
                'original_authors': ';'.join(original_ref.authors) if original_ref and original_ref.authors else '',
                'found_authors': ';'.join(result.best_match.authors) if result.best_match and result.best_match.authors else '',
                'original_year': original_ref.year if original_ref else '',
                'found_year': result.best_match.year if result.best_match else '',
                'original_venue': original_ref.venue if original_ref else '',
                'found_venue': result.best_match.venue if result.best_match else '',
                'found_url': result.best_match.url if result.best_match else '',
                'title_similarity': title_similarity,
                'author_similarity': author_similarity,
                'verification_time': f"{result.total_time:.3f}",
                'sources_checked': ';'.join(result.sources_checked) if result.sources_checked else '',
                'llm_reparsed': 'Yes' if llm_reparsed else 'No',
                'verification_notes': ';'.join(result.verification_notes) if result.verification_notes else '',
                'recommendations': ';'.join(result.recommendations) if result.recommendations else ''
            }
            rows.append(row_data)
        
        pd.DataFrame(rows).sort_values(by='reference_id', ascending=True).to_csv(output_path, index=False)
        logger.info(f"已导出 {len(verification_results)} 条验证结果到 {output_path}")
        return len(verification_results)
    
    def get_database_statistics(self) -> Dict[str, Any]:
        """获取数据库统计信息"""
        return self.db.get_scholar_statistics()
    
    def print_database_statistics(self):
        """打印数据库统计信息"""
        stats = self.get_database_statistics()
        
        print("\n" + "="*60)
        print("验证结果数据库统计信息")
        print(f"总记录数: {stats['total_records']}")
        print("="*60)
    
    def print_storage_statistics(self):
        """打印存储统计信息"""
        self.storage_service.print_storage_statistics()


class FileProcessor:
    """文件处理器"""
    
    def __init__(self, verifier: ScrapingDogVerifier):
        self.verifier = verifier
        self.storage_processor = StorageIntegratedFileProcessor(verifier, verifier.storage_service)
    
    async def process_directory(self, dir_path: str, args: argparse.Namespace) -> Dict[str, List[Reference]]:
        """处理目录中的文件（带存储功能）"""
        return await self.storage_processor.process_directory_with_storage(dir_path, args)
    
    async def process_single_file(self, file_path: str) -> List[Reference]:
        """处理单个文件（带存储功能）"""
        return await self.storage_processor.process_single_file_with_storage(file_path)
    
    async def process_llm_file(self,file_path:str) -> List[Reference]:
        jsons = os.listdir(file_path)
        
        references = {}
        for name in jsons:
            file = os.path.join(file_path,name)
            try:
                with open(file,'r') as jsonfile:
                    data = json.load(jsonfile)
                    if type(data['response'])==type('xx') and data['response']!='':
                        data['response'] = data['response'].replace('null',"''")
                        data['response'] = data['response'].replace(".\n ","")
                        data['response'] = data['response'].replace("```","")
                        data['response'] = data['response'].replace("json\n","")
                        data['response'] = data['response'].replace(".]","]")
                        data = eval(data['response'])
                        print(data)
                        break
                    else: 
                        data = data['response']
                    reflist = data
                references[file] = convert_parsed_references(reflist)
                
            except Exception as e:
                logger.error('读取llm文献失败',file,e)
                continue
        return references
    
    async def _exclude_no_venue(self, references: List[dict]) -> List[dict]:
        """过滤掉不符合条件的参考文献，并对标题为空的文献进行LLM重解析"""
        references_ = []
        for ref in references:
            if ref['venue'] != 'monograph' and ref['venue'] != 'unknown':
                references_.append(ref)
        
        # 对标题为空的文献进行LLM重解析
        for i in range(len(references_)):
            if references_[i]['title'] is None or references_[i]['title'].strip() == '':
                logger.info(f"发现标题为空的参考文献，尝试LLM重解析: {references_[i]['id']}")
                reparsed_dict = await self.verifier.llm_reparser.reparse_with_llm(references_[i])
                if reparsed_dict and reparsed_dict.get('title'):
                    references_[i] = reparsed_dict
                    logger.info(f"LLM重解析成功: {reparsed_dict['title'][:50]}...")
                else:
                    logger.warning(f"LLM重解析失败: {references_[i]['id']}")
        
        return references_
    
    def _exclude_reference_type(self, references: Dict[str, List[Reference]]) -> Dict[str, List[Reference]]:
        """过滤掉不符合条件的参考文献"""
        references_ = {}
        for name, ref in references.items():
            refs = []
            for r in ref:
                if r.reference_type != 'unknown' and r.reference_type != 'monograph':
                    refs.append(r)
            references_[name] = refs
        return references_


async def start_verify(verifier: ScrapingDogVerifier, references: List[Reference], args: argparse.Namespace) -> List[VerificationResult]:
    """启动验证流程"""
    async with verifier:
        verification_results = await verifier.verify_batch(references)
    
    # 导出验证结果到CSV
    if args.input:
        input_name = Path(args.input).stem
        csv_output = f"{input_name}_verified.csv"
    else:
        csv_output = args.output.replace('.json', '.csv')
    
    dir_main = '/'.join(args.dir.split('/')[:-1])+'/validation_results/'+args.dir.split('/')[-1]
    print(dir_main)
    if args.dir:
        if not os.path.exists(dir_main):
            os.makedirs(dir_main)
        csv_output = os.path.join(dir_main, csv_output)
    
    exported_count = verifier.export_verification_results_to_csv_with_original(
        verification_results, references, csv_output
    )
    print(f"\n已导出 {exported_count} 条验证结果到 {csv_output}")
    print(f"验证结果文件: {csv_output}")


def create_sample_references() -> List[Reference]:
    """创建示例参考文献"""
    sample_data = [
        {
            "title": "Attention Is All You Need",
            "authors": ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar"],
            "year": 2017,
            "venue": "NeurIPS",
            "doi": None,
            "pmid": None,
            "isbn": None,
            "patent_number": None,
            "arxiv_id": None,
            "url": None,
            "raw": "[1] A. Vaswani et al., \"Attention Is All You Need,\" NeurIPS, 2017."
        },
    ]
    
    return convert_parsed_references(sample_data)


async def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="ScrapingDog批量搜索程序")
    parser.add_argument("--dir", "-d", type=str, help="输入目录路径", default=None)
    parser.add_argument("--input", "-i", type=str, help="输入JSON文件路径")
    parser.add_argument("--inllm", "-l", type=str, help="输入LLM JSON文件路径")
    parser.add_argument("--output", "-o", type=str, default="scholar_results.json", help="输出JSON文件路径")
    parser.add_argument("--database", "-db", type=str, default="scholar_results.db", help="数据库文件路径")
    parser.add_argument("--concurrent", "-c", type=int, default=10, help="最大并发数")
    parser.add_argument("--sample", action="store_true", help="使用示例数据")
    parser.add_argument("--stats-only", action="store_true", help="只显示数据库统计信息")
    parser.add_argument("--clear-db", action="store_true", help="清空数据库")
    parser.add_argument("--cleanup-duplicates", action="store_true", help="清理重复数据（保留最早的记录）")
    parser.add_argument("--year-filter", type=int, help="按年份过滤导出")
    parser.add_argument("--dblp-db", type=str, default="dblp_titles.db", help="DBLP SQLite database path")
    parser.add_argument("--dblp-threshold", type=float, default=0.9, help="DBLP title match threshold (ratio)")
    parser.add_argument("--dblp-max-candidates", type=int, default=100000, help="Max DBLP candidates per query")
    parser.add_argument("--disable-dblp", action="store_true", help="Skip DBLP pre-match step")
    
    args = parser.parse_args()
    
    # 创建验证器和文件处理器
    verifier = ScrapingDogVerifier(
        db_path=args.database,
        max_concurrent=args.concurrent,
        dblp_db_path=args.dblp_db,
        dblp_match_threshold=args.dblp_threshold,
        dblp_max_candidates=args.dblp_max_candidates,
        enable_dblp=not args.disable_dblp,
    )
    file_processor = FileProcessor(verifier)
    
    try:
        # 处理特殊命令
        if args.clear_db:
            verifier.db.clear_all_data()
            print("数据库已清空")
            return
        
        if args.cleanup_duplicates:
            print("正在清理重复数据...")
            deleted_count = verifier.db.cleanup_duplicates()
            print(f"清理完成，删除了 {deleted_count} 条重复记录")
            verifier.print_database_statistics()
            return
        
        if args.stats_only:
            verifier.print_database_statistics()
            return
        
        
        # 加载参考文献
        if args.sample:
            print("使用示例参考文献数据")
            references = create_sample_references()
            await start_verify(verifier, references, args)
        elif args.dir:
            print(f"从文件目录加载参考文献: {args.dir}")
            references = await file_processor.process_directory(args.dir, args)
            
            for file, ref in tqdm(references.items()):
                args.input = file
                await start_verify(verifier, ref, args)
                print("\n" + "="*60)
        elif args.input:
            print(f"从文件加载参考文献: {args.input}")
            references = await file_processor.process_single_file(args.input)
            print(f"加载了 {len(references)} 个参考文献")
            await start_verify(verifier, references, args)
        elif args.inllm:
            print(f"从文件加载LLM文献: {args.inllm}")
            args.dir = args.inllm
            references = await file_processor.process_llm_file(args.inllm)
            print(f"加载了 {len(references)} 个参考json文件")
            for file, ref in tqdm(references.items()):
                print('处理',file)
                args.input = file
                await start_verify(verifier, ref, args)
                print("\n" + "="*60)

        else:
            print("请指定输入文件目录进行批量处理(--dir)或输入文件路径(--input) 或使用示例数据 (--sample)")
            return
        
        # 显示数据库统计信息
        verifier.print_database_statistics()
        
        print(f"\n数据库文件: {args.database}")
        print("\n验证完成！")
        
    except KeyboardInterrupt:
        print("\n\n用户中断程序")
    except Exception as e:
        logger.error(f"程序执行失败: {e}", exc_info=True)
        print(f"程序执行失败: {e}")


if __name__ == "__main__":
    asyncio.run(main())

