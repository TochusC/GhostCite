"""
参考文献存储服务
负责管理解析后参考文献的存储和LLM重解析结果的更新
"""
import logging
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path

from parsed_references_database import (
    ParsedReferencesDatabase, 
    ParsedReferenceRecord,
    create_parsed_reference_record_from_dict,
    create_parsed_reference_record_from_reference
)
from unified_database import (
    UnifiedDatabase,
    SearchResultRecord,
    create_search_result_record_from_external_reference
)

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from checker.models import Reference, ExternalReference

logger = logging.getLogger(__name__)


class ReferenceStorageService:
    """参考文献存储服务（包含解析结果和搜索结果）"""
    
    def __init__(self, db_path: str = "parsed_references.db", unified_db_path: str = "scholar_results.db"):
        """
        初始化存储服务
        
        Args:
            db_path: 解析后参考文献数据库文件路径
            unified_db_path: 统一数据库文件路径（包含scholar_results和search_results）
        """
        self.parsed_refs_db = ParsedReferencesDatabase(db_path)
        self.unified_db = UnifiedDatabase(unified_db_path)
        
        self.stats = {
            # 解析结果统计
            'total_processed': 0,
            'inserted': 0,
            'duplicates': 0,
            'llm_reparsed': 0,
            'errors': 0,
            
            # 搜索结果统计
            'search_results_stored': 0,
            'search_results_duplicates': 0,
            'search_results_errors': 0
        }
    
    # 保持向后兼容的属性
    @property
    def db(self):
        """向后兼容：返回解析后参考文献数据库"""
        return self.parsed_refs_db
    
    def store_parsed_references_from_dict(self, references: List[dict], source_file: str = None) -> Dict[str, int]:
        """
        存储从字典格式的解析结果
        
        Args:
            references: grobid解析结果字典列表
            source_file: 来源文件名
            
        Returns:
            存储统计信息
        """
        logger.info(f"开始存储 {len(references)} 个解析后的参考文献，来源文件: {source_file}")
        
        records = []
        for ref_dict in references:
            try:
                record = create_parsed_reference_record_from_dict(ref_dict, source_file)
                # 只存储有标题的记录
                if record.title and record.title.strip():
                    records.append(record)
                else:
                    logger.debug(f"跳过无标题的参考文献: {ref_dict.get('id', 'unknown')}")
            except Exception as e:
                logger.error(f"创建记录失败: {ref_dict.get('id', 'unknown')}, 错误: {e}")
                self.stats['errors'] += 1
        
        if not records:
            logger.warning("没有有效的记录可存储")
            return {'inserted': 0, 'duplicates': 0, 'errors': self.stats['errors']}
        
        # 批量插入
        batch_stats = self.db.insert_batch(records, ignore_duplicates=True)
        
        # 更新统计
        self.stats['total_processed'] += len(references)
        self.stats['inserted'] += batch_stats['inserted']
        self.stats['duplicates'] += batch_stats['duplicates']
        self.stats['errors'] += batch_stats['errors']
        
        logger.info(f"存储完成: {batch_stats}")
        return batch_stats
    
    def store_parsed_references_from_references(self, references: List[Reference], source_file: str = None) -> Dict[str, int]:
        """
        存储从Reference对象列表
        
        Args:
            references: Reference对象列表
            source_file: 来源文件名
            
        Returns:
            存储统计信息
        """
        logger.info(f"开始存储 {len(references)} 个Reference对象，来源文件: {source_file}")
        
        records = []
        for ref in references:
            try:
                record = create_parsed_reference_record_from_reference(ref, source_file)
                # 只存储有标题的记录
                if record.title and record.title.strip():
                    records.append(record)
                else:
                    logger.debug(f"跳过无标题的参考文献: {ref.id if hasattr(ref, 'id') else 'unknown'}")
            except Exception as e:
                logger.error(f"创建记录失败: {ref.id if hasattr(ref, 'id') else 'unknown'}, 错误: {e}")
                self.stats['errors'] += 1
        
        if not records:
            logger.warning("没有有效的记录可存储")
            return {'inserted': 0, 'duplicates': 0, 'errors': self.stats['errors']}
        
        # 批量插入
        batch_stats = self.db.insert_batch(records, ignore_duplicates=True)
        
        # 更新统计
        self.stats['total_processed'] += len(references)
        self.stats['inserted'] += batch_stats['inserted']
        self.stats['duplicates'] += batch_stats['duplicates']
        self.stats['errors'] += batch_stats['errors']
        
        logger.info(f"存储完成: {batch_stats}")
        return batch_stats
    
    def update_with_llm_reparse(self, original_ref: Reference, llm_reparsed_dict: dict) -> bool:
        """
        更新记录为LLM重解析结果
        
        Args:
            original_ref: 原始Reference对象
            llm_reparsed_dict: LLM重解析结果字典
            
        Returns:
            是否更新成功
        """
        if not original_ref.title or not llm_reparsed_dict.get('title'):
            logger.warning("原始或LLM解析结果缺少标题，无法更新")
            return False
        
        # 查找原始记录
        original_authors = ', '.join(original_ref.authors) if original_ref.authors else None
        existing_record = self.db.check_duplicate(original_ref.title, original_authors, original_ref.venue)
        
        if not existing_record:
            logger.warning(f"未找到原始记录: {original_ref.title[:50]}...")
            return False
        
        # 准备LLM解析结果
        llm_authors = ', '.join(llm_reparsed_dict.get('authors', [])) if llm_reparsed_dict.get('authors') else None
        llm_year = int(llm_reparsed_dict.get('year')) if llm_reparsed_dict.get('year') and str(llm_reparsed_dict.get('year')).isdigit() else None
        
        # 更新记录
        success = self.db.update_with_llm_reparse(
            existing_record.id,
            llm_reparsed_dict.get('title'),
            llm_authors,
            llm_reparsed_dict.get('venue'),
            llm_year
        )
        
        if success:
            self.stats['llm_reparsed'] += 1
            logger.info(f"LLM重解析更新成功: {existing_record.id} -> {llm_reparsed_dict.get('title')[:50]}...")
        
        return success
    
    def find_and_update_with_llm_reparse(self, llm_reparsed_dict: dict, source_file: str = None) -> bool:
        """
        根据LLM重解析结果查找并更新记录
        
        Args:
            llm_reparsed_dict: LLM重解析结果字典（包含id字段用于匹配）
            source_file: 来源文件名
            
        Returns:
            是否更新成功
        """
        ref_id = llm_reparsed_dict.get('id')
        if not ref_id:
            logger.warning("LLM重解析结果缺少ID，无法匹配原始记录")
            return False
        
        # 根据来源文件和ID查找记录
        if source_file:
            records = self.db.search_by_source_file(source_file)
            # 这里需要根据实际的ID匹配逻辑来查找
            # 由于数据库中没有存储原始的参考文献ID，我们需要其他方式匹配
            logger.warning("暂时无法根据ID匹配记录，需要改进匹配逻辑")
            return False
        
        return False
    
    def store_search_result(self, external_ref: ExternalReference, search_query: str = None, 
                           result_position: int = None) -> bool:
        """
        存储单个搜索结果
        
        Args:
            external_ref: 外部引用对象
            search_query: 搜索查询
            result_position: 搜索结果位置
            
        Returns:
            是否成功存储
        """
        try:
            record = create_search_result_record_from_external_reference(
                external_ref, search_query, result_position
            )
            
            record_id = self.unified_db.insert_search_result(record, ignore_duplicates=True)
            
            if record_id:
                self.stats['search_results_stored'] += 1
                logger.debug(f"存储搜索结果成功: {external_ref.title[:50] if external_ref.title else 'No title'}...")
                return True
            else:
                self.stats['search_results_duplicates'] += 1
                logger.debug(f"搜索结果重复，跳过: {external_ref.title[:50] if external_ref.title else 'No title'}...")
                return False
                
        except Exception as e:
            self.stats['search_results_errors'] += 1
            logger.error(f"存储搜索结果失败: {external_ref.title if external_ref.title else 'No title'}, 错误: {e}")
            return False
    
    def store_search_results_batch(self, external_refs: List[ExternalReference], 
                                  search_query: str = None) -> Dict[str, int]:
        """
        批量存储搜索结果
        
        Args:
            external_refs: 外部引用对象列表
            search_query: 搜索查询
            
        Returns:
            存储统计信息
        """
        logger.info(f"开始批量存储 {len(external_refs)} 个搜索结果")
        
        records = []
        for i, external_ref in enumerate(external_refs):
            try:
                record = create_search_result_record_from_external_reference(
                    external_ref, search_query, i + 1
                )
                records.append(record)
            except Exception as e:
                logger.error(f"创建搜索结果记录失败: {external_ref.title if external_ref.title else 'No title'}, 错误: {e}")
                self.stats['search_results_errors'] += 1
        
        if not records:
            logger.warning("没有有效的搜索结果记录可存储")
            return {'inserted': 0, 'duplicates': 0, 'errors': self.stats['search_results_errors']}
        
        # 批量插入
        batch_stats = self.unified_db.insert_search_results_batch(records, ignore_duplicates=True)
        
        # 更新统计
        self.stats['search_results_stored'] += batch_stats['inserted']
        self.stats['search_results_duplicates'] += batch_stats['duplicates']
        self.stats['search_results_errors'] += batch_stats['errors']
        
        logger.info(f"搜索结果存储完成: {batch_stats}")
        return batch_stats
    
    def get_storage_statistics(self) -> Dict[str, Any]:
        """获取存储统计信息"""
        parsed_refs_stats = self.parsed_refs_db.get_statistics()
        search_results_stats = self.unified_db.get_search_results_statistics()
        
        return {
            **self.stats,
            'parsed_refs': parsed_refs_stats,
            'search_results': search_results_stats
        }
    
    def print_storage_statistics(self):
        """打印存储统计信息"""
        stats = self.get_storage_statistics()
        
        print("\n" + "="*60)
        print("参考文献存储统计信息")
        print("="*60)
        
        # 解析结果统计
        print("解析结果存储:")
        print(f"  总处理数: {stats['total_processed']}")
        print(f"  成功插入: {stats['inserted']}")
        print(f"  重复跳过: {stats['duplicates']}")
        print(f"  LLM重解析: {stats['llm_reparsed']}")
        print(f"  错误数: {stats['errors']}")
        
        # 搜索结果统计
        print("\n搜索结果存储:")
        print(f"  已存储: {stats['search_results_stored']}")
        print(f"  重复跳过: {stats['search_results_duplicates']}")
        print(f"  错误数: {stats['search_results_errors']}")
        
        # 解析结果数据库统计
        parsed_refs_stats = stats.get('parsed_refs', {})
        print("\n解析结果数据库统计:")
        print(f"  总记录数: {parsed_refs_stats.get('total_records', 0)}")
        print(f"  LLM重解析记录数: {parsed_refs_stats.get('llm_reparsed_count', 0)}")
        print(f"  LLM重解析比例: {parsed_refs_stats.get('llm_reparsed_percentage', 0):.1f}%")
        
        # 搜索结果数据库统计
        search_results_stats = stats.get('search_results', {})
        print("\n搜索结果数据库统计:")
        print(f"  总记录数: {search_results_stats.get('total_records', 0)}")
        print(f"  有URL记录数: {search_results_stats.get('records_with_url', 0)}")
        
        # 搜索来源分布
        if search_results_stats.get('source_distribution'):
            print("\n搜索来源分布:")
            for source, count in search_results_stats['source_distribution'].items():
                print(f"  {source}: {count}")
        
        # 搜索引擎分布
        if search_results_stats.get('search_engine_distribution'):
            print("\n搜索引擎分布:")
            for engine, count in search_results_stats['search_engine_distribution'].items():
                print(f"  {engine}: {count}")
        
        # 引用类型分布
        if parsed_refs_stats.get('type_distribution'):
            print("\n引用类型分布:")
            for ref_type, count in list(parsed_refs_stats['type_distribution'].items())[:5]:
                print(f"  {ref_type}: {count}")
        
        # 年份分布
        if parsed_refs_stats.get('year_distribution'):
            print("\n年份分布 (前5年):")
            for year, count in list(parsed_refs_stats['year_distribution'].items())[:5]:
                print(f"  {year}: {count}")
        
        print("="*60)
    
    def export_to_csv(self, output_path: str, include_llm_only: bool = False) -> int:
        """
        导出解析结果到CSV文件
        
        Args:
            output_path: 输出文件路径
            include_llm_only: 是否只包含LLM重解析的记录
            
        Returns:
            导出的记录数
        """
        return self.parsed_refs_db.export_to_csv(output_path, include_llm_only)
    
    def export_search_results_to_csv(self, output_path: str, source_filter: str = None) -> int:
        """
        导出搜索结果到CSV文件
        
        Args:
            output_path: 输出文件路径
            source_filter: 来源过滤器（如'google_search'或'scrapingdog'）
            
        Returns:
            导出的记录数
        """
        return self.unified_db.export_search_results_to_csv(output_path, source_filter)
    
    def get_llm_reparsed_records(self) -> List[ParsedReferenceRecord]:
        """获取所有LLM重解析的记录"""
        return self.db.get_llm_reparsed_records()
    
    def search_by_title(self, title: str) -> List[ParsedReferenceRecord]:
        """根据标题搜索记录"""
        return self.db.search_by_title(title)
    
    def search_by_source_file(self, source_file: str) -> List[ParsedReferenceRecord]:
        """根据来源文件搜索记录"""
        return self.db.search_by_source_file(source_file)
    
    def close(self):
        """关闭数据库连接"""
        self.parsed_refs_db.close()
        self.unified_db.close()


class StorageIntegratedFileProcessor:
    """集成存储功能的文件处理器"""
    
    def __init__(self, verifier, storage_service: ReferenceStorageService):
        self.verifier = verifier
        self.storage_service = storage_service
    
    async def process_directory_with_storage(self, dir_path: str, args) -> Dict[str, List[Reference]]:
        """处理目录中的文件并存储解析结果"""
        import grobid_parser_to_xml
        from tqdm import tqdm
        from checker.models import convert_parsed_references
        
        references = {}
       
        output_dir = dir_path.strip('/').split('/')[-1] + '_ref_xml'
        print(f"文件路径 {dir_path}, xml输出路径{output_dir}")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        files = os.listdir(output_dir)
        exist_files = [f for f in files if f.endswith('.xml')]
        exist_files_str = ','.join(exist_files)

        files = os.listdir(dir_path)
        
        for file in tqdm(files):
            if file.endswith('.pdf') and file not in exist_files_str:
                print(f"正在处理 {file}")
                try:
                    # 解析PDF
                    parsed_refs = grobid_parser_to_xml.grobid_parse(os.path.join(dir_path, file), output_dir)
                    
                    # 存储解析结果
                    storage_stats = self.storage_service.store_parsed_references_from_dict(parsed_refs, file)
                    logger.info(f"文件 {file} 存储统计: {storage_stats}")
                    
                    # 转换为Reference对象用于后续验证
                    references[file] = convert_parsed_references(parsed_refs)
                    
                except Exception as e:
                    print(f"处理 {file} 失败: {e}")
                    logger.error(f"处理文件 {file} 失败: {e}")
                    continue
        
        total = len(references)
        print(f"加载了 {total} 个参考文件")
        references = self._exclude_reference_type(references)
        
        return references
    
    async def process_single_file_with_storage(self, file_path: str) -> List[Reference]:
        """处理单个文件并存储解析结果"""
        from parser.grobid_parser import parse_xml
        from checker.models import convert_parsed_references
        
        file_name = Path(file_path).name
        
        # 解析文件
        parsed_refs = await self._exclude_no_venue(parse_xml(file_path))
        
        # 存储解析结果
        storage_stats = self.storage_service.store_parsed_references_from_dict(parsed_refs, file_name)
        logger.info(f"文件 {file_name} 存储统计: {storage_stats}")
        
        return convert_parsed_references(parsed_refs)
    
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
                    # 更新存储的记录
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
