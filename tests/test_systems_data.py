"""Test for systems data integrity."""

import pytest
from dsapython.systems_data import (
    ALL_SYSTEMS,
    get_all_systems,
    get_systems_by_category,
    validate_systems_data
)


class TestSystemsDataIntegrity:
    """Test the integrity of systems data."""
    
    def test_all_systems_exist(self):
        """Test that all 21 systems are defined."""
        systems = get_all_systems()
        assert len(systems) == 21
    
    def test_systems_numbered_correctly(self):
        """Test that systems are numbered 2-22."""
        systems = get_all_systems()
        numbers = sorted([s.number for s in systems])
        
        # Should be numbered 2-22 (skipping 1)
        assert numbers == list(range(2, 23))
    
    def test_unique_titles(self):
        """Test that all systems have unique titles."""
        systems = get_all_systems()
        titles = [s.title for s in systems]
        
        assert len(titles) == len(set(titles))
    
    def test_category_distribution(self):
        """Test correct distribution across categories."""
        systems = get_all_systems()
        
        categories = {}
        for system in systems:
            if system.category not in categories:
                categories[system.category] = 0
            categories[system.category] += 1
        
        # Check expected counts
        assert categories['Foundations'] == 2
        assert categories['Language & Dialogue'] == 5
        assert categories['Multimodal Image'] == 7
        assert categories['Multimodal Video & Audio'] == 3
        assert categories['Infrastructure'] == 4
    
    def test_get_systems_by_category(self):
        """Test filtering systems by category."""
        foundations = get_systems_by_category('Foundations')
        assert len(foundations) == 2
        
        image = get_systems_by_category('Multimodal Image')
        assert len(image) == 7
        
        # All should have matching category
        for system in image:
            assert system.category == 'Multimodal Image'
    
    def test_systems_have_complexity_metrics(self):
        """Test that all systems have complexity metrics."""
        systems = get_all_systems()
        
        for system in systems:
            assert system.complexity_metrics is not None
            assert system.complexity_metrics.model_size is not None
            assert system.complexity_metrics.time_complexity is not None
            assert system.complexity_metrics.space_complexity is not None
            assert system.complexity_metrics.latency_target is not None
            assert system.complexity_metrics.throughput_target is not None
    
    def test_systems_have_components(self):
        """Test that all systems have key components."""
        systems = get_all_systems()
        
        for system in systems:
            assert len(system.key_components) >= 2
            assert all(isinstance(comp, str) for comp in system.key_components)
    
    def test_validate_function(self):
        """Test the validation function."""
        # Should not raise any exceptions
        validate_systems_data()
    
    def test_sample_systems_content(self):
        """Test specific systems for expected content."""
        systems = {s.number: s for s in get_all_systems()}
        
        # Check Gmail Smart Compose (2)
        system2 = systems[2]
        assert system2.title == "Gmail Smart Compose"
        assert "email" in system2.objective.lower()
        assert "on-device" in system2.objective.lower()
        
        # Check ChatGPT (4)
        system4 = systems[4]
        assert "ChatGPT" in system4.title
        assert "RLHF" in system4.objective
        
        # Check Text-to-Image (12)
        system12 = systems[12]
        assert "Text-to-Image" in system12.title
        assert "CLIP" in " ".join(system12.key_components)
        
        # Check LLM Serving Infrastructure (19)
        system19 = systems[19]
        assert "Serving" in system19.title
        assert "KV Cache" in " ".join(system19.key_components)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
