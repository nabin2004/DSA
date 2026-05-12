# GenAI System Design Interview - Skeleton Page Generator

## Overview

A Python-based skeleton page generator for 22 GenAI interview systems. This project generates comprehensive skeleton pages for interview preparation on GenAI system design, covering foundational models, language systems, multimodal approaches, and infrastructure.

### 22 Systems Covered

**Foundations (2)**
- Gmail Smart Compose (2)
- Google Translate (3)

**Language & Dialogue (5)**
- ChatGPT: Personal Assistant Chatbot (4)
- Retrieval Augmented Generation (5)
- Code Generation Assistant (6)
- Document Q&A over PDF/Enterprise Corpus (7)
- Real-Time Meeting Summariser (8)

**Multimodal Image (7)**
- Image Captioning (9)
- Realistic Face Generation (GAN) (10)
- High-Resolution Image Synthesis (11)
- Text-to-Image Generation (12)
- Personalized Headshot Generation (13)
- Visual Question Answering (14)
- Product Photo Background Removal and Staging (15)

**Multimodal Video & Audio (3)**
- Text-to-Video Generation (16)
- AI Video Subtitle and Dubbing System (17)
- Music Generation from Text Prompt (18)

**Infrastructure (5)**
- LLM Serving Infrastructure (19)
- Online Fine-Tuning and RLHF Pipeline (20)
- ML Feature Store for GenAI (21)
- Evaluation and Red-Teaming Platform (22)

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── template_generator.py      # Core skeleton generation logic
│   ├── systems_data.py             # All 22 system definitions
│   ├── citations.py                # Citation management
│   └── main.py                     # CLI entry point
├── tests/
│   ├── test_template_generator.py  # Unit tests for generation
│   └── test_systems_data.py        # Systems data validation
├── genai_systems/                  # Output directory (created on generate)
│   ├── INDEX.md                    # Master index
│   ├── 02_gmail_smart_compose.md
│   ├── 03_google_translate.md
│   └── ...                         # One file per system
├── README.md                       # This file
├── requirements.txt                # Python dependencies
└── pyproject.toml                  # Project configuration
```

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. Clone or navigate to the project:
```bash
cd /path/to/DSA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python -m pytest tests/ -v
```

## Usage

### Generate All Skeleton Pages

```bash
python -m src.main --generate-all
```

This will:
1. Validate the systems data (all 22 systems)
2. Generate skeleton pages for each system in `genai_systems/`
3. Create a master index file `genai_systems/INDEX.md`

Expected output:
```
======================================================================
GenAI System Design Interview - Skeleton Page Generator
======================================================================

[Phase 3] Generating skeleton pages for all 22 systems...

✓ Systems data validation passed

Generating 22 skeleton pages in genai_systems/...
✓ Generated 22/22 skeleton pages in 0.45s

Generating master index...
✓ Created genai_systems/INDEX.md

Total generation time: 0.45s
Average time per system: 0.02s
```

### Generate with Validation

```bash
python -m src.main --generate-all --validate
```

This will run additional validation tests after generation.

### Custom Output Directory

```bash
python -m src.main --generate-all --output-dir my_output
```

### Help

```bash
python -m src.main --help
```

## Skeleton Page Structure

Each generated skeleton page includes:

1. **Title & Metadata**
   - System number and name
   - Problem statement and motivation

2. **Complexity Analysis**
   - Model size
   - Time complexity
   - Space complexity
   - Latency target
   - Throughput target

3. **Architecture Design**
   - High-level data flow diagram
   - Key components breakdown

4. **Core Algorithm/Model**
   - Model architecture explanation
   - Key innovations
   - Training approach

5. **Evaluation & Metrics**
   - Evaluation methodology
   - Key metrics
   - Benchmarks

6. **References & Citations**
   - Academic papers
   - Blog posts and articles
   - Documentation links

## Running Tests

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Suite

```bash
# Test template generation
pytest tests/test_template_generator.py -v

# Test systems data
pytest tests/test_systems_data.py -v
```

### Test Coverage

```bash
pytest tests/ --cov=src --cov-report=html
```

## Key Features

### 1. **Template Generator**
- Generates consistent skeleton pages from system definitions
- Includes complexity metrics, architecture diagrams, and references
- Validates output for completeness

### 2. **Systems Data**
- Centralized definitions for all 22 systems
- Metadata: objectives, key components, complexity metrics
- Easy to extend and maintain

### 3. **Citation Management**
- Sample citations for each system
- Citation formatting (APA, IEEE, HTML)
- References to papers, blogs, and docs

### 4. **Validation Framework**
- Data integrity checks
- Generated page validation
- Category distribution verification

## API Reference

### Template Generator

```python
from src.template_generator import TemplateGenerator, GenAISystem

# Generate a single skeleton page
page = TemplateGenerator.generate_skeleton_page(system)

# Generate all skeleton pages
results = TemplateGenerator.generate_all_skeletons(systems, output_dir)

# Generate master index
TemplateGenerator.generate_index(systems, index_file_path)
```

### Systems Data

```python
from src.systems_data import get_all_systems, get_systems_by_category

# Get all 22 systems
systems = get_all_systems()

# Filter by category
image_systems = get_systems_by_category("Multimodal Image")

# Validate data integrity
validate_systems_data()
```

### Citation Management

```python
from src.citations import get_sample_citations, CitationFormatter

# Get citations for a system
citations = get_sample_citations(system_number=4)

# Format citations
formatter = CitationFormatter()
apa_format = formatter.to_apa(citation)
```

## Example Output

### Master Index
```markdown
# GenAI System Design Interview - Master Index

## Quick Navigation

- **Foundations (2 systems)**
  - [Gmail Smart Compose](#2-gmail-smart-compose)
  - [Google Translate](#3-google-translate)

- **Language & Dialogue (5 systems)**
  - [ChatGPT: Personal Assistant Chatbot](#4-chatgpt-personal-assistant-chatbot)
  - ...
```

### System Skeleton
```markdown
# Gmail Smart Compose

## Problem Statement

Predicts and suggests the next words in email drafts using an on-device ML model, demonstrating real-time language prediction at scale for billions of users.

## Complexity Analysis

| Metric | Value |
|--------|-------|
| Model Size | 10-100M parameters (on-device) |
| Time Complexity | O(seq_len) per token |
| Space Complexity | ~50-200MB on device |
| Latency Target | p95 <50ms |
| Throughput Target | 1000s of requests/s |

...
```

## Performance

- **Generation Speed**: ~0.02s per system, 0.45s for all 22 systems
- **Memory Usage**: <100MB during generation
- **Output Size**: ~10KB per skeleton page, ~220KB total

## Contributing

To add or modify systems:

1. Edit `src/systems_data.py`
2. Add system to `ALL_SYSTEMS` list
3. Run validation: `python -m pytest tests/test_systems_data.py`
4. Regenerate pages: `python -m src.main --generate-all`

## License

This project is provided as-is for educational purposes.

## Author

GenAI Interview Preparation Tool
