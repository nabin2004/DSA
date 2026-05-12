"""dsapython package - re-export key symbols for ease of use."""

from .template_generator import (
    TemplateGenerator,
    GenAISystem,
    ComplexityMetrics,
    SkeletonPageValidator,
)

from .systems_data import (
    ALL_SYSTEMS,
    get_all_systems,
    get_systems_by_category,
    validate_systems_data,
)

from .utils import (
    write_file,
    read_file,
    file_exists,
    sanitize_filename,
    get_date_string,
    count_words,
    progress_bar,
)

from .citations import (
    CitationEntry,
    CitationFormatter,
    CitationValidator,
)

from .diagram_blocks import (
    DiagramBlock,
    MermaidValidator,
    DiagramBlockFormatter,
)

__all__ = [
    'TemplateGenerator', 'GenAISystem', 'ComplexityMetrics', 'SkeletonPageValidator',
    'ALL_SYSTEMS', 'get_all_systems', 'get_systems_by_category', 'validate_systems_data',
    'write_file', 'read_file', 'file_exists', 'sanitize_filename',
    'CitationEntry', 'CitationFormatter',
    'DiagramBlock'
]
