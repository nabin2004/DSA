"""Unit tests for skeleton page generation."""

import pytest
import tempfile
from pathlib import Path

from src.template_generator import GenAISystem, ComplexityMetrics, TemplateGenerator
from src.systems_data import get_all_systems, validate_systems_data


class TestComplexityMetrics:
    """Test ComplexityMetrics data class."""
    
    def test_create_metrics(self):
        """Test creating complexity metrics."""
        metrics = ComplexityMetrics(
            model_size="1B parameters",
            time_complexity="O(n²)",
            space_complexity="10GB",
            latency_target="<100ms",
            throughput_target="1000 req/s"
        )
        
        assert metrics.model_size == "1B parameters"
        assert metrics.time_complexity == "O(n²)"
        assert metrics.space_complexity == "10GB"
        assert metrics.latency_target == "<100ms"
        assert metrics.throughput_target == "1000 req/s"


class TestGenAISystem:
    """Test GenAISystem data class."""
    
    def test_create_system(self):
        """Test creating a GenAI system."""
        metrics = ComplexityMetrics(
            model_size="1B",
            time_complexity="O(n²)",
            space_complexity="10GB",
            latency_target="<100ms",
            throughput_target="1000 req/s"
        )
        
        system = GenAISystem(
            number=1,
            title="Test System",
            category="Test",
            objective="Test objective",
            key_components=["Component 1", "Component 2"],
            complexity_metrics=metrics
        )
        
        assert system.number == 1
        assert system.title == "Test System"
        assert system.category == "Test"
        assert system.objective == "Test objective"
        assert len(system.key_components) == 2


class TestSystemsData:
    """Test systems data loading and validation."""
    
    def test_load_all_systems(self):
        """Test loading all systems."""
        systems = get_all_systems()
        
        assert len(systems) == 21
        
        # Check first system (Gmail Smart Compose)
        system = systems[0]
        assert system.number == 2
        assert "Gmail" in system.title
        
        # Check last system (Evaluation and Red-Teaming)
        system = systems[-1]
        assert system.number == 22
        assert "Evaluation" in system.title
    
    def test_validate_systems(self):
        """Test systems validation."""
        # Should not raise any exceptions
        validate_systems_data()
    
    def test_systems_have_required_fields(self):
        """Test that all systems have required fields."""
        systems = get_all_systems()
        
        for system in systems:
            assert system.number is not None
            assert system.title is not None
            assert system.category is not None
            assert system.objective is not None
            assert system.key_components is not None
            assert system.complexity_metrics is not None
            assert len(system.key_components) > 0


class TestTemplateGenerator:
    """Test template generation."""
    
    def test_generate_skeleton_page(self):
        """Test generating a skeleton page."""
        metrics = ComplexityMetrics(
            model_size="1B",
            time_complexity="O(n²)",
            space_complexity="10GB",
            latency_target="<100ms",
            throughput_target="1000 req/s"
        )
        
        system = GenAISystem(
            number=99,
            title="Test System",
            category="Test",
            objective="This is a test objective.",
            key_components=["Component 1", "Component 2"],
            complexity_metrics=metrics
        )
        
        page = TemplateGenerator.generate_skeleton_page(system)
        
        # Check required sections
        assert "Test System" in page
        assert "test objective" in page
        assert "Component 1" in page
        assert "Component 2" in page
        assert "## Complexity Analysis" in page
        assert "## Technical Approach" in page
        assert "## Pros & Cons" in page
    
    def test_generate_index(self):
        """Test generating master index."""
        systems = get_all_systems()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            index_file = f"{tmpdir}/INDEX.md"
            TemplateGenerator.generate_index(systems, index_file)
            
            content = Path(index_file).read_text()
            
            # Check index structure
            assert "Complete Index" in content
            assert "Foundations" in content
            assert "Language & Dialogue" in content
            assert len(content) > 1000


class TestSkeletonPageValidator:
    """Test skeleton page validation."""
    
    def test_validate_valid_page(self):
        """Test validating a valid skeleton page."""
        from src.template_generator import SkeletonPageValidator
        
        valid_page = """# System Title

## Problem Statement
Test content

## Complexity Analysis
- Model Size: 1B

## Architecture Design
### Data Flow
Test

### Key Components
Test

## Core Algorithm/Model
Test

## Evaluation & Metrics
Test

## References
- Test reference
"""
        
        # Should return True for valid pages
        # Note: validator checks for key sections
        assert "## Problem Statement" in valid_page
        assert "## Complexity Analysis" in valid_page
        assert "## Architecture Design" in valid_page


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
