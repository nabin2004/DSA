# Data Model: GenAI System Design Skeleton Pages

**Phase**: Phase 1 (Design & Contracts)  
**Status**: COMPLETED  
**Date**: 2026-05-12  

This document defines the core entities and their relationships for the GenAI skeleton page system.

---

## Core Entities

### 1. GenAISystem

Represents a single GenAI interview topic from the 22-system curriculum.

**Attributes**:
- `id` (string): System identifier in format `NNN_system_name_lowercase` (e.g., `002_gmail_smart_compose`, `004_chatgpt_assistant`)
- `number` (integer): Sequential number from 2-22 (01 is intro, not included)
- `title` (string): Display name (e.g., "Gmail Smart Compose", "ChatGPT: Personal Assistant Chatbot")
- `category` (enum): One of {Foundations, Language & Dialogue, Multimodal Image, Multimodal Video & Audio, Infrastructure}
- `objective` (string): 1-2 sentence summary of system purpose and relevance
- `key_components` (list): [component names], e.g., ["Encoder", "Decoder", "Attention", "Training Pipeline"]
- `complexity_metrics` (dict):
  - `model_size`: string (e.g., "7B-70B parameters")
  - `time_complexity`: string (e.g., "O(seq_len)")
  - `space_complexity`: string (e.g., "~2x model size")
  - `latency_target`: string (e.g., "p95 <500ms")
  - `throughput_target`: string (e.g., "100 req/s per GPU")
- `created_date` (ISO 8601): When skeleton page was generated
- `last_updated` (ISO 8601): When content was last modified
- `completion_status` (enum): {not_started, in_progress, ready_for_review, completed}

**Relationships**:
- 1 GenAISystem → Many CitationEntry (3-5 citations per system)
- 1 GenAISystem → Many DiagramBlock (2-3 diagrams per system: architecture, data flow, optional: failure modes)

---

### 2. CitationEntry

Represents a single reference source with reproducibility metadata.

**Attributes**:
- `id` (string): Unique identifier within a system (e.g., `004_cite_001`, `004_cite_002`)
- `system_id` (string): Reference to parent GenAISystem
- `title` (string): Citation title (e.g., "Attention Is All You Need")
- `source_url` (string): URL to paper, blog post, or reference
- `source_type` (enum): {arxiv_paper, github_repo, blog_post, documentation, textbook_chapter, video, whitepaper, other}
- `publication_date` (ISO 8601 or "unknown"): When source was published
- `access_date` (ISO 8601): When this citation was verified and added to skeleton page
- `relevance_summary` (string): 1-2 sentences explaining why this source supports the topic
- `reproducibility_artifact` (string): Specific artifact used (e.g., "GitHub repo: meta-llama/llama2, commit abc123")
- `reproducibility_claim` (string): Specific claim supported by artifact (e.g., "Token embeddings are 4096-dimensional for Llama 2 70B")
- `reproducibility_verified` (boolean): Whether claim was independently verified
- `reproducibility_verification_note` (string): How verification was performed (e.g., "Checked model config, ran inference, confirmed in output tensor")

**Constraints**:
- `access_date` must not be in the future
- `publication_date` must be ≤ `access_date` (if both are present)
- `source_url` must be a valid, accessible URL (validated during generation)
- `reproducibility_verified` must be true for all citations (part of Constitution Principle V: Reproducibility)

**Relationships**:
- Many CitationEntry → 1 GenAISystem

---

### 3. DiagramBlock

Represents a reusable diagram template for system architecture, data flow, or failure modes.

**Attributes**:
- `id` (string): Unique identifier within a system (e.g., `004_diagram_architecture`, `004_diagram_dataflow`)
- `system_id` (string): Reference to parent GenAISystem
- `type` (enum): {architecture, data_flow, failure_recovery, scaling_strategy, training_pipeline}
- `title` (string): Display name (e.g., "ChatGPT Architecture", "LLM Inference Pipeline")
- `description` (string): 1-2 sentences explaining what the diagram shows
- `mermaid_code` (string): Raw Mermaid diagram code (flowchart, sequence, state diagram)
- `annotations` (list): Key annotations on the diagram explaining latency, throughput, bottlenecks
  - Each annotation: {element, latency_ms, throughput_rps, constraint}
- `complexity_notes` (string): Key performance or architectural insights shown in diagram
- `created_date` (ISO 8601): When diagram was generated

**Constraints**:
- `mermaid_code` must be valid Mermaid syntax (validated by rendering parser)
- `type` must match diagram purpose (e.g., "architecture" for component boxes and connections)
- All diagrams must render in <500ms in GitHub Markdown renderer

**Relationships**:
- Many DiagramBlock → 1 GenAISystem

---

### 4. SkeletonPage

Represents the generated markdown page for a single GenAI system.

**Attributes**:
- `id` (string): Same as GenAISystem id (e.g., `004_chatgpt_assistant`)
- `system_id` (string): Reference to parent GenAISystem
- `file_path` (string): Relative path to markdown file (e.g., `genai_systems/002_language_dialogue/004_chatgpt_assistant.md`)
- `content_sections` (dict):
  - `objective`: Populated from GenAISystem.objective
  - `architecture_diagram`: Embedded DiagramBlock (type=architecture)
  - `technical_approach`: Populated from GenAISystem.key_components and complexity_metrics
  - `complexity_analysis`: Auto-generated table from GenAISystem.complexity_metrics
  - `pros_cons`: Placeholder fields for manual content fill
  - `real_world_applications`: Placeholder fields for manual content fill
  - `citations`: All CitationEntry objects embedded in order
  - `reproducibility_checklist`: Standardized checkbox list
- `word_count` (integer): Total words in page (target: 500-800 words)
- `line_count` (integer): Total lines of markdown
- `citations_count` (integer): Number of citations embedded
- `diagrams_count` (integer): Number of diagrams embedded
- `completion_percentage` (integer): % of placeholder fields filled (0% = skeleton only, 100% = ready for review)
- `generated_date` (ISO 8601): When page was generated
- `last_verified` (ISO 8601): When all citations were last verified as accessible

**Validation Rules**:
- All required sections must be present (non-empty)
- All citations must have `reproducibility_verified` = true
- All diagrams must render correctly in Markdown
- Page must respect 244-byte filename limit (GitHub constraint)
- Page must remain editable in standard Markdown editors

**Relationships**:
- 1 SkeletonPage ← 1 GenAISystem
- 1 SkeletonPage contains Many CitationEntry
- 1 SkeletonPage contains Many DiagramBlock

---

### 5. CategoryIndex

Represents grouping of systems by interview category.

**Attributes**:
- `id` (string): Category identifier (e.g., `foundations`, `language_dialogue`, `multimodal_image`, `multimodal_video_audio`, `infrastructure`)
- `name` (string): Display name (e.g., "Foundations", "Language and Dialogue")
- `description` (string): 1-2 sentences describing category focus
- `systems` (list): Ordered list of GenAISystem objects in this category
- `system_count` (integer): Number of systems (auto-calculated)
- `completion_status` (dict):
  - `total_systems`: Integer count
  - `completed_systems`: Integer count
  - `completion_percentage`: Integer (0-100)
- `learning_prerequisites` (list): Category names that should be studied first (e.g., Foundations required before Language & Dialogue)

**Relationships**:
- 1 CategoryIndex contains Many GenAISystem
- CategoryIndex objects form a DAG (directed acyclic graph) via learning_prerequisites

---

### 6. TopicIndex (Master Index)

Represents the master index of all 22 systems organized by category.

**Attributes**:
- `id` (string): Always "master_index"
- `title` (string): "GenAI System Design Interview: Complete Index"
- `version` (string): Semantic version (e.g., "1.0.0")
- `categories` (list): All CategoryIndex objects in order
- `total_systems` (integer): 22 (fixed)
- `total_completion_percentage` (integer): Aggregate % across all systems
- `generated_date` (ISO 8601): When index was generated
- `file_path` (string): Always `genai_systems/INDEX.md`

**Relationships**:
- 1 TopicIndex contains Many CategoryIndex
- 1 TopicIndex → All 22 GenAISystem objects (transitive via CategoryIndex)

---

## Validation Rules & Constraints

### Constitution Principles Enforcement

1. **Code Quality (Principle I)**:
   - All CitationEntry records must have non-empty `reproducibility_claim` (no vague citations)
   - All DiagramBlock `mermaid_code` must be syntactically valid and properly formatted

2. **Testing (Principle II)**:
   - Every SkeletonPage must pass validation: all sections present, all citations accessible, all diagrams render
   - CitationEntry records must be tested for URL accessibility (404 detection)

3. **Learning UX Consistency (Principle III)**:
   - All SkeletonPages must follow identical section order and heading hierarchy
   - All CitationEntry records use identical template format
   - All DiagramBlock objects use identical Mermaid syntax style

4. **Performance Explicitness (Principle IV)**:
   - All GenAISystem.complexity_metrics must be populated (no null values)
   - All DiagramBlock annotations must include latency and throughput where applicable
   - Page render time <500ms per skeleton page (validated during generation)

5. **Reproducibility (Principle V)**:
   - All CitationEntry.reproducibility_verified must be true
   - All CitationEntry.reproducibility_artifact must be non-empty and specific
   - All SkeletonPage must be regenerable from source (no manual-only content in required sections)

---

## Relationships Diagram

```
TopicIndex (1)
    ↓
    ├── CategoryIndex (5)
    │       ↓
    │       └── GenAISystem (22)
    │           ├── CitationEntry (3-5 per system)
    │           │   ├── source_url → accessible URL
    │           │   ├── reproducibility_artifact → verified
    │           │   └── reproducibility_verified → true
    │           │
    │           ├── DiagramBlock (2-3 per system)
    │           │   ├── mermaid_code → valid syntax
    │           │   ├── type → {architecture, data_flow, etc}
    │           │   └── annotations → latency, throughput
    │           │
    │           └── SkeletonPage (1 per system)
    │               ├── content_sections → all required
    │               ├── completion_percentage → 0-100
    │               └── word_count → 500-800 target
```

---

## Storage & Serialization

### File Formats

- **SkeletonPage**: Markdown (.md) — human-readable, version-controllable, editable
- **Metadata**: JSON or YAML frontmatter in each .md file (optional)
- **Index**: Markdown with embedded tables and links
- **Master Index** (`INDEX.md`): Markdown with category sections and completion progress

### Versioning Strategy

- Store GenAISystem definitions in version control (git)
- CitationEntry records versioned per SkeletonPage (accessed_date updated on re-verification)
- DiagramBlock code versioned with SkeletonPage (regeneration only if template changes)
- Use git commit messages to track major structure changes

---

## Future Extensions

- **AI-assisted citation search**: Automatically find and validate citations for new systems
- **Diagram rendering service**: Pre-render all Mermaid diagrams to PNG/SVG for faster page loads
- **Citation freshness checker**: Periodically verify all URLs are still accessible
- **Completion analytics**: Track which systems are in progress, ready for review, or completed
- **Community contributions**: Allow external PRs to fill in pro/cons and real-world applications
