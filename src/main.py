"""Main CLI entry point for GenAI skeleton page generation."""

import argparse
import sys
import time
from pathlib import Path

from src.systems_data import get_all_systems, validate_systems_data
from src.template_generator import TemplateGenerator, SkeletonPageValidator
from src.citations import get_sample_citations, CitationFormatter


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="GenAI System Design Interview Skeleton Page Generator"
    )
    
    parser.add_argument(
        '--generate-all',
        action='store_true',
        help='Generate skeleton pages for all 22 systems'
    )
    
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate all generated pages'
    )
    
    parser.add_argument(
        '--output-dir',
        default='genai_systems',
        help='Output directory for generated pages (default: genai_systems)'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("GenAI System Design Interview - Skeleton Page Generator")
    print("=" * 70)
    print()
    
    if args.generate_all:
        print("[Phase 3] Generating skeleton pages for all 22 systems...")
        print()
        
        # Validate systems data
        validate_systems_data()
        print()
        
        # Get all systems
        systems = get_all_systems()
        
        # Generate skeleton pages
        print(f"Generating {len(systems)} skeleton pages in {args.output_dir}/...")
        start_time = time.time()
        
        results = TemplateGenerator.generate_all_skeletons(systems, args.output_dir)
        
        elapsed = time.time() - start_time
        
        print()
        print(f"✓ Generated {results['generated']}/{results['total']} skeleton pages in {elapsed:.2f}s")
        
        if results['failed']:
            print(f"✗ Failed: {len(results['failed'])} files")
            for failure in results['failed']:
                print(f"  - {failure}")
        
        print()
        
        # Generate master index
        print(f"Generating master index...")
        TemplateGenerator.generate_index(systems, f"{args.output_dir}/INDEX.md")
        print(f"✓ Created {args.output_dir}/INDEX.md")
        print()
        
        if args.validate:
            print("[Validation Phase]")
            print()
            print("Running validation tests...")
            
            # Quick validation
            valid_count = 0
            invalid_count = 0
            
            for file_path in results['files']:
                try:
                    content = Path(file_path).read_text()
                    if SkeletonPageValidator.is_valid(content):
                        valid_count += 1
                    else:
                        invalid_count += 1
                        print(f"✗ Validation failed: {file_path}")
                except Exception as e:
                    invalid_count += 1
                    print(f"✗ Error validating {file_path}: {e}")
            
            print()
            print(f"✓ Validation results: {valid_count} passed, {invalid_count} failed")
        
        print()
        print(f"Total generation time: {elapsed:.2f}s")
        print(f"Average time per system: {elapsed/len(systems):.3f}s")
        print()
        
        return 0
    
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
