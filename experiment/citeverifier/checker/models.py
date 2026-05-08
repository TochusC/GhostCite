"""
数据结构定义模块
"""

import re
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class VerificationStatus(str, Enum):
    """验证状态枚举"""
    VALID = "valid"                 # 验证通过
    INVALID = "invalid"             # 验证失败（伪造/错误）
    SUSPICIOUS = "suspicious"       # 可疑（部分信息错误）
    UNVERIFIED = "unverified"       # 无法验证（信息不足）
    ERROR = "error"                 # 验证过程出错
    TIMEOUT = "timeout"             # 验证超时


class ReferenceType(str, Enum):
    """文献类型枚举"""
    JOURNAL_ARTICLE = "journal_article"     # 期刊论文
    CONFERENCE_PAPER = "conference_paper"   # 会议论文
    BOOK = "book"                          # 书籍
    BOOK_CHAPTER = "book_chapter"          # 书籍章节
    PATENT = "patent"                      # 专利
    TECHNICAL_REPORT = "technical_report"   # 技术报告
    THESIS = "thesis"                      # 学位论文
    PREPRINT = "preprint"                  # 预印本
    WEBSITE = "website"                    # 网站
    OTHER = "other"                        # 其他


class Reference(BaseModel):
    """输入的参考文献数据结构"""
    id: int = Field(..., description="文献ID")
    title: str = Field(..., description="文献标题")
    authors: List[str] = Field(..., description="作者列表")
    year: Optional[int] = Field(None, description="发表年份")
    venue: Optional[str] = Field(None, description="发表期刊/会议/出版社")
    volume: Optional[str] = Field(None, description="卷号")
    issue: Optional[str] = Field(None, description="期号")
    pages: Optional[str] = Field(None, description="页码")
    doi: Optional[str] = Field(None, description="DOI标识符")
    pmid: Optional[str] = Field(None, description="PubMed ID")
    isbn: Optional[str] = Field(None, description="ISBN（书籍）")
    patent_number: Optional[str] = Field(None, description="专利号")
    arxiv_id: Optional[str] = Field(None, description="arXiv ID")
    url: Optional[str] = Field(None, description="URL链接")
    reference_type: Optional[str] = Field(None, description="文献类型")
    raw: Optional[str]  = Field(..., description="原始参考文献字符串")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Deep Learning",
                "authors": ["Yann LeCun", "Yoshua Bengio", "Geoffrey Hinton"],
                "year": 2015,
                "venue": "Nature",
                "volume": "521",
                "issue": "7553",
                "pages": "436-444",
                "doi": "10.1038/nature14539",
                "raw": "[1] Y. LeCun, Y. Bengio, and G. Hinton, \"Deep learning,\" Nature, vol. 521, no. 7553, pp. 436–444, 2015."
            }
        }


class ExternalReference(BaseModel):
    """外部数据源返回的文献信息"""
    title: Optional[str] = None
    authors: Optional[List[str]] = None
    year: Optional[int] = None
    venue: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    abstract: Optional[str] = None
    source: str = Field(..., description="数据源标识 (crossref, pubmed, arxiv)")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="额外的元数据")


class FieldMatchResult(BaseModel):
    """单个字段的匹配结果"""
    field_name: str = Field(..., description="字段名称")
    input_value: Optional[str] = Field(None, description="输入值")
    external_value: Optional[str] = Field(None, description="外部源值")
    similarity_score: float = Field(..., ge=0.0, le=1.0, description="相似度分数 (0-1)")
    is_match: bool = Field(..., description="是否匹配")


class ApiResult(BaseModel):
    """单个API客户端的验证结果"""
    source: str = Field(..., description="API数据源名称")
    status: VerificationStatus = Field(..., description="验证状态")
    external_ref: Optional[ExternalReference] = Field(None, description="找到的外部文献信息")
    field_matches: List[FieldMatchResult] = Field(default_factory=list, description="字段匹配详情")
    overall_similarity: float = Field(0.0, ge=0.0, le=1.0, description="整体相似度分数")
    error_message: Optional[str] = Field(None, description="错误信息")
    response_time: float = Field(0.0, description="API响应时间(秒)")
    timestamp: datetime = Field(default_factory=datetime.now, description="验证时间戳")


class VerificationResult(BaseModel):
    """最终的验证结果"""
    reference_id: int = Field(..., description="参考文献ID")
    final_status: VerificationStatus = Field(..., description="最终验证状态")
    overall_similarity: float = Field(0.0, ge=0.0, le=1.0, description="整体相似度分数")
    
    # 诊断信息
    diagnosis: str = Field(..., description="详细诊断信息")
    problematic_fields: List[str] = Field(default_factory=list, description="有问题的字段")
    
    # 各API的详细结果
    api_results: List[ApiResult] = Field(default_factory=list, description="各API的验证结果")
    
    # 汇总信息
    best_match: Optional[ExternalReference] = Field(None, description="最佳匹配的外部文献")
    sources_checked: List[str] = Field(default_factory=list, description="已检查的数据源")
    sources_failed: List[str] = Field(default_factory=list, description="失败的数据源")
    
    # 性能统计
    total_time: float = Field(0.0, description="总验证时间(秒)")
    fastest_source: Optional[str] = Field(None, description="最快响应的数据源")
    
    # 详细说明
    verification_notes: List[str] = Field(default_factory=list, description="验证说明")
    recommendations: List[str] = Field(default_factory=list, description="建议")
    
    timestamp: datetime = Field(default_factory=datetime.now, description="验证完成时间")

    class Config:
        json_schema_extra = {
            "example": {
                "reference_id": 1,
                "final_status": "valid",
                "overall_similarity": 0.95,
                "diagnosis": "通过DOI验证",
                "sources_checked": ["crossref", "pubmed"],
                "total_time": 2.5,
                "verification_notes": ["Title and authors match exactly", "DOI confirmed"],
                "recommendations": ["Reference appears to be accurate"]
            }
        }

def clean_title(title: str) -> str:
        """清理标题字符串，移除多层花括号和其他格式字符"""
        if not title:
            return ""
        
        title = title.strip()
        
        # 递归移除花括号，处理多层嵌套的情况
        # 例如: {A Formal Analysis of SCTP: Attack Synthesis and Patch Verification}
        # 或者: {{Title}} -> {Title} -> Title
        prev_title = ""
        while prev_title != title:
            prev_title = title
            # 移除最外层的花括号
            if title.startswith('{') and title.endswith('}'):
                # 检查是否是完整的花括号对
                brace_count = 0
                for i, char in enumerate(title):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                    # 如果在中间位置花括号计数为0，说明不是完整的外层包装
                    if brace_count == 0 and i < len(title) - 1:
                        break
                else:
                    # 如果循环正常结束，说明是完整的外层包装，可以移除
                    if brace_count == 0:
                        title = title[1:-1].strip()
        
        # 移除其他常见的格式字符
        # 移除方括号内容 [1], [Online], etc.
        title = re.sub(r'\s*\[.*?\]\s*', ' ', title)
        
        # 移除开头的编号 "1. ", "1) ", etc.
        title = re.sub(r'^\s*[\d\.\-\)\]]+\s*', '', title)
        
        # 移除引号
        title = title.strip('"\'""''')

        # 移除因换行产生-
        title = title.replace('-', '')
        
        # 标准化空格
        title = re.sub(r'\s+', ' ', title).strip()
        
        return title

def convert_parsed_reference(parsed_ref_dict: Dict[str, Any], ref_id: int) -> Reference:
    """
    将parser返回的单个字典转换为Reference对象
    
    Args:
        parsed_ref_dict: parser解析出的参考文献字典
        ref_id: 参考文献ID
        
    Returns:
        Reference对象
    """
    # 处理年份字段
    year = parsed_ref_dict.get('year')
    if year is not None:
        if isinstance(year, str):
            # 提取字符串中的数字
            import re
            year_match = re.search(r'\d{4}', str(year))
            if year_match:
                try:
                    year = int(year_match.group())
                except (ValueError, TypeError):
                    year = None
            else:
                year = None
        elif not isinstance(year, int):
            year = None
    
    # title、authors、raw 三个字段需有默认值
    title = parsed_ref_dict.get('title', '')
    if not title or title.strip() == '':
        title = 'Untitled'
    #title = clean_title(title)
    


    if parsed_ref_dict.get('doi') is not None:
        if "\\" in parsed_ref_dict.get('doi'):
            parsed_ref_dict['doi'] = parsed_ref_dict['doi'].replace('\\', '')
    
    authors = parsed_ref_dict.get('authors', [])
    if not isinstance(authors, list):
        if isinstance(authors, str) and authors.strip():
            authors = [authors.strip()]
        else:
            authors = []
    
    raw = parsed_ref_dict.get('raw', '')
    if not raw or raw.strip() == '':
        raw = f"Reference {ref_id}"
    
    return Reference(
        id=ref_id,
        title=title,
        authors=authors,
        year=year,
        venue=parsed_ref_dict.get('venue'),
        volume=parsed_ref_dict.get('volume'),
        issue=parsed_ref_dict.get('issue'),
        pages=parsed_ref_dict.get('pages'),
        doi=parsed_ref_dict.get('doi'),
        pmid=parsed_ref_dict.get('pmid'),
        isbn=parsed_ref_dict.get('isbn'),
        patent_number=parsed_ref_dict.get('patent_number'),
        arxiv_id=parsed_ref_dict.get('arxiv_id'),
        url=parsed_ref_dict.get('url'),
        reference_type=parsed_ref_dict.get('reference_type'),
        raw=raw
    )


def convert_parsed_references(parsed_references: List[Dict[str, Any]]) -> List[Reference]:
    """
    将parser返回的字典列表转换为Reference对象列表
    
    Args:
        parsed_references: parser解析出的参考文献字典列表
        
    Returns:
        Reference对象列表
    """
    #print(parsed_references)
    references = []
    for i, parsed_ref in enumerate(parsed_references):
        # 如果字典中已有id，使用它；否则使用索引+1
        ref_id = parsed_ref.get('id', i + 1)
        
        # 处理None值和字符串转换
        if ref_id is None:
            ref_id = i + 1
        elif isinstance(ref_id, str):
            try:
                ref_id = int(ref_id)
            except ValueError:
                ref_id = i + 1
        elif not isinstance(ref_id, int):
            ref_id = i + 1
        
        ref_obj = convert_parsed_reference(parsed_ref, ref_id)
        references.append(ref_obj)
    
    return references


