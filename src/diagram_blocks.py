"""Diagram block management for skeleton pages."""

import re
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class DiagramBlock:
    """Represents a Mermaid diagram block."""
    diagram_id: str
    diagram_type: str  # architecture, data_flow, failure_recovery, scaling_strategy
    title: str
    description: str
    mermaid_code: str
    annotations: List[Dict[str, str]] = None
    complexity_notes: str = ""


class MermaidValidator:
    """Validates Mermaid diagram syntax and completeness."""
    
    @staticmethod
    def validate_syntax(mermaid_code: str) -> bool:
        """Check Mermaid code for valid syntax."""
        # Basic checks for flowchart structure
        if not mermaid_code.strip():
            return False
        
        # Check for unclosed quotes
        if mermaid_code.count('"') % 2 != 0:
            return False
        
        # Must contain flowchart or sequence or state keyword
        valid_keywords = ['flowchart', 'sequenceDiagram', 'stateDiagram', 'graph']
        return any(keyword in mermaid_code for keyword in valid_keywords)
    
    @staticmethod
    def validate_annotations(annotations: List[Dict[str, str]]) -> bool:
        """Verify critical paths have latency/throughput annotations."""
        if not annotations:
            return False
        
        # Should have at least 2 annotations
        if len(annotations) < 2:
            return False
        
        # Check that annotations have required fields
        required_fields = {'element', 'latency_ms', 'throughput_rps'}
        for annotation in annotations:
            if not all(field in annotation for field in required_fields):
                return False
        
        return True
    
    @staticmethod
    def validate_line_count(mermaid_code: str) -> bool:
        """Verify diagram code is not excessively long (readability check)."""
        lines = mermaid_code.split('\n')
        return len(lines) < 500


class DiagramBlockFormatter:
    """Formats diagram blocks for markdown."""
    
    @staticmethod
    def diagram_to_markdown(diagram: DiagramBlock) -> str:
        """Convert DiagramBlock to markdown format."""
        markdown = f"""### {diagram.title}

{diagram.description}

```mermaid
{diagram.mermaid_code}
```

"""
        if diagram.annotations:
            markdown += "**Annotations**:\n"
            for ann in diagram.annotations:
                markdown += f"- {ann.get('element', '')}: {ann.get('latency_ms', 'N/A')}ms latency, {ann.get('throughput_rps', 'N/A')} req/s\n"
            markdown += "\n"
        
        if diagram.complexity_notes:
            markdown += f"**Complexity Notes**: {diagram.complexity_notes}\n\n"
        
        return markdown


def get_sample_diagrams(system_category: str) -> List[DiagramBlock]:
    """Get sample diagram templates for a category."""
    # Returns a basic template diagram
    return [
        DiagramBlock(
            diagram_id="llm_architecture",
            diagram_type="architecture",
            title="LLM Inference Pipeline",
            description="High-level architecture showing LLM inference flow with caching.",
            mermaid_code="""flowchart LR
    A["Input Tokens"] -->|Embedding Layer| B["Token Embeddings"]
    B -->|Attention Layers| C["Hidden States"]
    C -->|Output Layer| D["Logits"]
    D -->|Sampling| E["Output Tokens"]
    C -->|KV Cache| F["GPU Memory"]
    F -->|Retrieve| C""",
            annotations=[
                {
                    'element': 'Attention Layers to KV Cache',
                    'latency_ms': '50-100',
                    'throughput_rps': '100-500',
                    'constraint': 'Memory bandwidth bottleneck'
                },
                {
                    'element': 'Input to Output',
                    'latency_ms': '200-500',
                    'throughput_rps': '20-100',
                    'constraint': 'Full sequence dependent'
                }
            ],
            complexity_notes="KV cache significantly reduces latency from O(n²) to O(n) per token"
        )
    ]
