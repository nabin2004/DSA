"""Template generator for GenAI system skeleton pages."""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
import os
from src.utils import (
    write_file, read_file, file_exists, sanitize_filename, 
    get_date_string, count_words, validate_markdown_syntax,
    progress_bar
)


@dataclass
class ComplexityMetrics:
    """Complexity metrics for a GenAI system."""
    model_size: str
    time_complexity: str
    space_complexity: str
    latency_target: str
    throughput_target: str


@dataclass
class GenAISystem:
    """Represents a single GenAI system."""
    number: int
    title: str
    category: str
    objective: str
    key_components: List[str] = field(default_factory=list)
    complexity_metrics: ComplexityMetrics = field(default_factory=lambda: ComplexityMetrics(
        model_size="", time_complexity="", space_complexity="",
        latency_target="", throughput_target=""
    ))
    
    @property
    def id(self) -> str:
        """Generate system ID."""
        slug = sanitize_filename(self.title)
        return f"{self.number:02d}_{slug}"
    
    @property
    def filename(self) -> str:
        """Generate markdown filename."""
        slug = sanitize_filename(self.title)
        return f"{self.number:02d}_{slug}.md"
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        d = asdict(self)
        d['complexity_metrics'] = asdict(self.complexity_metrics)
        return d


class SkeletonPageValidator:
    """Validates skeleton page structure and content."""
    
    REQUIRED_SECTIONS = [
        "# ",  # Title (H1)
        "## Objective",
        "## System Architecture",
        "## Technical Approach",
        "## Complexity Analysis",
        "## Pros & Cons",
        "## Real-World Applications",
        "## References & Citations",
        "### Reproducibility Checklist"
    ]
    
    @staticmethod
    def validate_all_sections(content: str) -> bool:
        """Check if all required sections are present."""
        for section in SkeletonPageValidator.REQUIRED_SECTIONS:
            if section not in content:
                return False
        return True
    
    @staticmethod
    def validate_heading_hierarchy(content: str) -> bool:
        """Verify H1 title, H2 sections, consistent hierarchy."""
        lines = content.split('\n')
        
        # First heading should be H1
        first_heading = None
        for line in lines:
            if line.startswith('#'):
                first_heading = line
                break
        
        if not first_heading or not first_heading.startswith('# '):
            return False
        
        # All section headings should be H2
        section_count = sum(1 for line in lines if line.startswith('## '))
        if section_count < 7:  # At least 7 H2 sections
            return False
        
        return True
    
    @staticmethod
    def validate_complexity_table(content: str) -> bool:
        """Verify complexity analysis table has 5 rows with non-empty cells."""
        # Look for complexity table
        if "| Model size |" not in content:
            return False
        
        # Check that table has all 5 metrics
        required_metrics = [
            "| Model size |",
            "| Time complexity |",
            "| Space complexity |",
            "| Latency target |",
            "| Throughput target |"
        ]
        
        for metric in required_metrics:
            if metric not in content:
                return False
        
        return True
    
    @staticmethod
    def validate_markdown_syntax(content: str) -> bool:
        """Check for markdown syntax errors."""
        # Check for unclosed code blocks
        if content.count('```') % 2 != 0:
            return False
        
        # Check for unclosed emphasis
        if content.count('**') % 2 != 0:
            return False
        
        return True
    
    @staticmethod
    def validate_citations_present(content: str, min_citations: int = 3) -> bool:
        """Verify minimum citation blocks present."""
        citation_count = content.count('### Citation ')
        return citation_count >= min_citations
    
    @staticmethod
    def validate_all(content: str) -> Dict[str, bool]:
        """Run all validation checks."""
        return {
            'all_sections': SkeletonPageValidator.validate_all_sections(content),
            'heading_hierarchy': SkeletonPageValidator.validate_heading_hierarchy(content),
            'complexity_table': SkeletonPageValidator.validate_complexity_table(content),
            'markdown_syntax': SkeletonPageValidator.validate_markdown_syntax(content),
            'citations_present': SkeletonPageValidator.validate_citations_present(content),
        }
    
    @staticmethod
    def is_valid(content: str) -> bool:
        """Return True if all validation checks pass."""
        results = SkeletonPageValidator.validate_all(content)
        return all(results.values())


class TemplateGenerator:
    """Main template generator for skeleton pages."""
    
    @staticmethod
    def generate_skeleton_page(system: GenAISystem) -> str:
        """Generate markdown skeleton page for a single system."""
        
        components_list = '\n'.join(
            f"- **{comp}**: [description]"
            for comp in system.key_components
        ) if system.key_components else "- **[Component 1]**: [description]"
        
        metrics = system.complexity_metrics
        
        template = f"""# {system.number:02d}. {system.title}

## Objective

{system.objective}

## System Architecture

[Mermaid diagram - flowchart showing core components and data flow]

[3-5 sentence description of architecture]

## Technical Approach

### Key Components

{components_list}

### Pipeline / Data Flow

[Detailed description of request → processing → response flow]

## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| Model size | {metrics.model_size} | [implications] |
| Time complexity | {metrics.time_complexity} | [notes] |
| Space complexity | {metrics.space_complexity} | [notes] |
| Latency target | {metrics.latency_target} | [real-time vs. batch] |
| Throughput target | {metrics.throughput_target} | [per GPU/instance] |

## Pros & Cons

### Pros

- **[Pro 1]**: [1-2 sentence explanation]
- **[Pro 2]**: [1-2 sentence explanation]

### Cons

- **[Con 1]**: [1-2 sentence explanation]
- **[Con 2]**: [1-2 sentence explanation]

### Trade-offs

[1-2 paragraphs discussing key technical trade-offs]

## Real-World Applications

### Where This Pattern Appears

- **[Company/Product 1]**: [Use case]
- **[Company/Product 2]**: [Use case]

### Production Considerations

[2-3 paragraphs on scaling, failure modes, monitoring, cost]

## References & Citations

### Citation 1: Architecture & Design

**Title**: [Paper/Blog Title on {system.title} Architecture]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper1]
- **Summary**: [1-2 sentences on key technical contribution]

### Citation 2: Performance & Benchmarks

**Title**: [Performance Benchmarks for {system.title}]
- **Author(s)**: [Author names]  
- **Published**: [Date]
- **Link**: [https://example.com/paper2]
- **Summary**: [1-2 sentences on performance characteristics]

### Citation 3: Implementation Details

**Title**: [Implementation Details and Trade-offs]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper3]
- **Summary**: [1-2 sentences on practical implementation insights]

### Citation 4: Real-World Deployment

**Title**: [Production Deployment Insights]
- **Author(s)**: [Author names]
- **Published**: [Date]
- **Link**: [https://example.com/paper4]
- **Summary**: [1-2 sentences on deployment considerations]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
"""
        return template.strip() + "\n"
    
    @staticmethod
    def generate_all_skeletons(systems: List[GenAISystem], output_dir: str = "genai_systems") -> Dict[str, str]:
        """Generate skeleton pages for all systems."""
        results = {
            'total': len(systems),
            'generated': 0,
            'failed': [],
            'files': []
        }
        
        for idx, system in enumerate(systems, 1):
            try:
                # Generate content
                content = TemplateGenerator.generate_skeleton_page(system)
                
                # Validate
                if not SkeletonPageValidator.is_valid(content):
                    results['failed'].append(f"{system.filename}: validation failed")
                    continue
                
                # Determine file path
                category_map = {
                    'Foundations': '001_foundations',
                    'Language & Dialogue': '002_language_dialogue',
                    'Multimodal Image': '003_multimodal_image',
                    'Multimodal Video & Audio': '004_multimodal_video_audio',
                    'Infrastructure': '005_infrastructure'
                }
                
                category_dir = category_map.get(system.category, 'unknown')
                file_path = os.path.join(output_dir, category_dir, system.filename)
                
                # Write file
                write_file(file_path, content)
                
                results['generated'] += 1
                results['files'].append(file_path)
                
                # Print progress
                print(progress_bar(idx, len(systems), f"Generating: {system.title}"))
                
            except Exception as e:
                results['failed'].append(f"{system.filename}: {str(e)}")
        
        return results
    
    @staticmethod
    def generate_index(systems: List[GenAISystem], output_file: str = "genai_systems/INDEX.md") -> None:
        """Generate master index of all systems."""
        
        # Group by category
        categories = {}
        for system in systems:
            if system.category not in categories:
                categories[system.category] = []
            categories[system.category].append(system)
        
        # Generate markdown index
        index_content = """# GenAI System Design Interview: Complete Index

Master index of all 22 GenAI systems organized by category.

**Status**: 0/22 completed

"""
        
        for category_name in ['Foundations', 'Language & Dialogue', 'Multimodal Image', 
                               'Multimodal Video & Audio', 'Infrastructure']:
            if category_name in categories:
                systems_in_cat = categories[category_name]
                index_content += f"## {category_name}\n\n"
                index_content += "| # | System | Status | Link |\n"
                index_content += "|---|--------|--------|------|\n"
                
                for system in systems_in_cat:
                    # Determine category dir
                    category_map = {
                        'Foundations': '001_foundations',
                        'Language & Dialogue': '002_language_dialogue',
                        'Multimodal Image': '003_multimodal_image',
                        'Multimodal Video & Audio': '004_multimodal_video_audio',
                        'Infrastructure': '005_infrastructure'
                    }
                    category_dir = category_map[system.category]
                    link = f"{category_dir}/{system.filename}"
                    
                    index_content += f"| {system.number:02d} | {system.title} | ⬜ Not started | [{system.filename}]({link}) |\n"
                
                index_content += "\n"
        
        write_file(output_file, index_content)


def main():
    """Main entry point for template generation."""
    print("GenAI System Skeleton Page Generator")
    print("=" * 50)
