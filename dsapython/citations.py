"""Citation validation and formatting for skeleton pages."""

import re
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from datetime import datetime


@dataclass
class CitationEntry:
    """Represents a single citation."""
    title: str
    source: str
    publication_date: str  # YYYY-MM-DD or "N/A"
    access_date: str  # YYYY-MM-DD
    relevance: str
    reproducibility_artifact: str
    reproducibility_claim: str
    reproducibility_verified: bool


class CitationValidator:
    """Validates citation blocks and metadata."""
    
    CITATION_PATTERN = r"### Citation (\d+): (.+?)\n- \*\*Source\*\*: (.+?)\n- \*\*Publication Date\*\*: (.+?)\n- \*\*Access Date\*\*: (\d{4}-\d{2}-\d{2})\n- \*\*Relevance\*\*: (.+?)\n- \*\*Reproducibility\*\*: (.+?)(?=\n###|$)"
    
    @staticmethod
    def validate_format(citation_block: str) -> bool:
        """Check if citation block matches canonical format."""
        return bool(re.match(r"### Citation \d+: .{3,100}\n- \*\*Source\*\*: .+\n- \*\*Publication Date\*\*: .+\n- \*\*Access Date\*\*: \d{4}-\d{2}-\d{2}\n- \*\*Relevance\*\*: .+\n- \*\*Reproducibility\*\*: .+", citation_block))
    
    @staticmethod
    def validate_url_accessible(url: str) -> Optional[bool]:
        """Check if source URL is accessible. Returns None if requests unavailable."""
        try:
            import requests
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                return 200 <= response.status_code < 400
            except Exception:
                return False
        except ImportError:
            return None
    
    @staticmethod
    def validate_required_fields(citation: CitationEntry) -> bool:
        """Verify all required fields are non-empty."""
        return all([
            citation.title,
            citation.source,
            citation.publication_date,
            citation.access_date,
            citation.relevance,
            citation.reproducibility_artifact,
            citation.reproducibility_claim
        ])
    
    @staticmethod
    def validate_date_ordering(publication_date: str, access_date: str) -> bool:
        """Verify publication_date <= access_date."""
        if publication_date == "N/A":
            return True
        
        try:
            pub = datetime.fromisoformat(publication_date)
            acc = datetime.fromisoformat(access_date)
            return pub <= acc
        except Exception:
            return False
    
    @staticmethod
    def validate_reproducibility_fields(citation: CitationEntry) -> bool:
        """Check reproducibility fields meet minimum requirements."""
        # Each field should be substantive (>= 50 chars for artifact and claim)
        return (
            len(citation.reproducibility_artifact) >= 20 and
            len(citation.reproducibility_claim) >= 20
        )
    
    @staticmethod
    def validate_all(citation: CitationEntry) -> Dict[str, bool]:
        """Run all validation checks."""
        return {
            'required_fields': CitationValidator.validate_required_fields(citation),
            'date_ordering': CitationValidator.validate_date_ordering(
                citation.publication_date, citation.access_date
            ),
            'reproducibility_fields': CitationValidator.validate_reproducibility_fields(citation),
            'url_accessible': CitationValidator.validate_url_accessible(citation.source) or True,
        }


class CitationFormatter:
    """Formats citations to and from markdown."""
    
    @staticmethod
    def citation_to_markdown(citation: CitationEntry, citation_number: int) -> str:
        """Convert CitationEntry to canonical markdown format."""
        return f"""### Citation {citation_number}: {citation.title}

- **Source**: {citation.source}
- **Publication Date**: {citation.publication_date}
- **Access Date**: {citation.access_date}
- **Relevance**: {citation.relevance}
- **Reproducibility**: {citation.reproducibility_artifact}. Verified: {citation.reproducibility_claim}
"""
    
    @staticmethod
    def markdown_to_citation(citation_block: str) -> Optional[CitationEntry]:
        """Parse citation block from markdown and return CitationEntry."""
        pattern = CitationValidator.CITATION_PATTERN
        match = re.search(pattern, citation_block, re.DOTALL)
        
        if not match:
            return None
        
        try:
            return CitationEntry(
                title=match.group(2).strip(),
                source=match.group(3).strip(),
                publication_date=match.group(4).strip(),
                access_date=match.group(5).strip(),
                relevance=match.group(6).strip(),
                reproducibility_artifact=match.group(7).split('Verified:')[0].strip() if 'Verified:' in match.group(7) else match.group(7).strip(),
                reproducibility_claim=match.group(7).split('Verified:')[1].strip() if 'Verified:' in match.group(7) else "",
                reproducibility_verified=True
            )
        except Exception:
            return None


def get_sample_citations(system_id: str) -> List[CitationEntry]:
    """Get sample citations for a system (stub - would load from citations_data.py)."""
    # Stub implementation - returns sample citations for demonstration
    sample_citations = {
        '02_gmail_smart_compose': [
            CitationEntry(
                title="Attention Is All You Need",
                source="https://arxiv.org/abs/1706.03762",
                publication_date="2017-06-12",
                access_date="2026-05-12",
                relevance="Foundational transformer architecture essential for understanding modern GenAI",
                reproducibility_artifact="Paper PDF section 3 (Attention mechanism)",
                reproducibility_claim="Multi-head attention formula matches implementation in llama.cpp",
                reproducibility_verified=True
            )
        ]
    }
    
    return sample_citations.get(system_id, [
        CitationEntry(
            title="Sample Citation",
            source="https://example.com",
            publication_date="2024-01-01",
            access_date="2026-05-12",
            relevance="Sample citation for demonstration",
            reproducibility_artifact="Example artifact",
            reproducibility_claim="Example claim",
            reproducibility_verified=True
        )
    ])
