# Research & Design Decisions

**Phase**: Phase 0 (Research)  
**Status**: COMPLETED  
**Date**: 2026-05-12  

This document captures key design decisions for the GenAI skeleton page system. All NEEDS CLARIFICATION items from the spec have been resolved below.

---

## 1. Diagram Format Decision

**Research Question**: What diagramming format best serves GenAI system design content?

**Candidates Evaluated**:
- **Mermaid**: Markdown-native, version-controllable, renders in GitHub/Jupyter, extensive diagram types (flowchart, sequence, class, state)
- **PlantUML**: Flexible but requires external rendering; slower integration into markdown workflows
- **SVG/Graphviz**: High-quality output but difficult to maintain and version-control as source code
- **ASCII diagrams**: Simple and portable but low visual clarity for complex architectures

**Decision**: **Mermaid (flowchart + sequence diagrams)**

**Rationale**:
- Native markdown support: no external processing pipeline needed
- First-class support in GitHub, Jupyter Book (MyST), and standard markdown editors
- Version-control friendly: diffs are readable and merge conflicts resolvable
- Fast rendering: enables rapid iteration during interview prep sessions
- Learner-friendly: students can copy-paste Mermaid blocks into their own notes
- Ecosystem: rich library of diagram types (flowchart for architecture, sequence for data flow, state for system transitions)

**Alternatives Rejected**:
- PlantUML requires external compilation; adds dependency complexity
- SVG/Graphviz not editable in standard markdown tools
- ASCII diagrams lack visual impact for system design interviews

**Reference Implementation**: Mermaid flowchart block for each GenAI system showing:
- Core components (LLM, embeddings, storage, inference)
- Request → Processing → Response flow
- Latency/throughput annotations
- Scaling strategy (horizontal vs. vertical)
- Failure recovery paths

---

## 2. Citation Template Format Decision

**Research Question**: What citation format ensures reproducibility while remaining lightweight for interview prep?

**Candidates Evaluated**:
- **BibTeX**: Standard academic format but verbose; not readable in plain markdown
- **APA/IEEE**: Standardized but rigid; designed for formal papers, not learning notes
- **Custom Markdown**: Simple key-value format, readable in plain text, flexible for reproducibility metadata
- **JSON frontmatter**: Structured but harder to read without tooling

**Decision**: **Custom Markdown citation blocks (with structured key-value fields)**

**Rationale**:
- Remains readable in any text editor (consistent with Constitution Principle III: UX Consistency)
- Lightweight syntax enables rapid entry during timed interview prep
- Extensible: can add new fields (e.g., "reproducibility_verified_date") without breaking existing citations
- Supports automatic extraction via regex or simple parsing
- Shareable: readers can easily copy, modify, and contribute back to community

**Citation Block Template**:

```markdown
### Citation [N]: [Title]

- **Source**: [URL or reference ID]
- **Publication Date**: [YYYY-MM-DD or "N/A"]
- **Access Date**: [YYYY-MM-DD when verified]
- **Relevance**: [1-2 sentence summary of why this source supports the topic]
- **Reproducibility**: [artifact used (e.g., GitHub repo, whitepaper, blog post) + specific claim supported + verification note]
```

**Example**:

```markdown
### Citation 1: "Attention Is All You Need"

- **Source**: https://arxiv.org/abs/1706.03762
- **Publication Date**: 2017-06-12
- **Access Date**: 2026-05-12
- **Relevance**: Foundational paper on transformer architecture, essential for understanding modern GenAI systems
- **Reproducibility**: Paper PDF + Section 3.2 (Attention mechanism) + Verified: math derivation matches implementation in llama.cpp
```

**Alternatives Rejected**:
- BibTeX incompatible with Markdown-first workflows
- APA/IEEE formats too formal; overkill for learning notes
- JSON frontmatter requires external parsing tools

---

## 3. Template Hierarchy & Skeleton Page Structure

**Research Question**: What consistent structure best serves all 22 GenAI interview topics?

**Analysis of Topics**:
- **Foundations** (2 systems): Gmail Smart Compose, Google Translate — focus on end-to-end pipeline
- **Language & Dialogue** (5 systems): ChatGPT, RAG, Code Gen, Doc Q&A, Meeting Summarizer — varies from single-LLM to multi-stage
- **Multimodal Image** (7 systems): Image captioning to headshots — shared tokenization/encoding but different objectives
- **Multimodal Video & Audio** (3 systems): Video generation, dubbing, music generation — real-time or batch constraints
- **Infrastructure** (5 systems): LLM serving, fine-tuning, feature store, evaluation platform — heavy ops focus

**Common Elements Across All 22**:
1. Core objective (1-2 sentences)
2. System approach (high-level architecture)
3. Technical complexity (time, space, GPU/compute requirements)
4. Pros and cons (vs. alternatives)
5. Real-world usage (where this design appears in production)
6. Diagrams (architecture, data flow, failure modes)
7. Citations (sources and reproducibility metadata)
8. Complexity checklist (completeness validation)

**Decision**: **8-section skeleton page structure (identical for all 22 systems)**

**Rationale**:
- Consistent section order reduces cognitive load for interview prep (learner can quickly locate complexity tradeoffs, architecture decisions)
- Supports rapid fill-in-the-blank content creation (P1 feature on spec: <10 min per page)
- Enables automated validation: every section present, citations in correct format, diagrams referenced
- Shareable: community contributors know exact structure when adding new systems

**Skeleton Page Sections**:

```markdown
# [SYSTEM_NUMBER]. [System Name]

## Objective

[1-2 sentence summary of what this system does and why it matters in GenAI]

## System Architecture

[High-level diagram (Mermaid flowchart) + 3-5 sentence description]

## Technical Approach

### Key Components
- [Component 1]: [brief role]
- [Component 2]: [brief role]
- ...

### Pipeline / Data Flow
[Sequence diagram or detailed description of request → processing → response]

## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| Model size | [e.g., 7B-70B parameters] | [e.g., affects latency, cost, hardware requirements] |
| Time complexity | [e.g., O(seq_len) inference] | [memory-bound on GPUs] |
| Space complexity | [e.g., ~2x model size for activations] | [peak during training] |
| Latency target | [e.g., p95 <500ms] | [real-time vs. batch constraint] |
| Throughput target | [e.g., 100 req/s per GPU] | [determined by model, batch size, quantization] |

## Pros & Cons

### Pros
- [Pro 1]: [brief explanation]
- [Pro 2]
- ...

### Cons
- [Con 1]: [brief explanation]
- [Con 2]
- ...

### Trade-offs
[Discuss key technical trade-offs: model size vs. latency, batch size vs. cost, fine-tuning vs. zero-shot, etc.]

## Real-World Applications

### Where This Pattern Appears
- **[Company/Product 1]**: [Use case and lessons learned]
- **[Company/Product 2]**: [Use case and lessons learned]
- ...

### Production Considerations
[1-2 paragraphs on scaling, failure modes, monitoring, operational complexity]

## References & Citations

[3-5 structured citation blocks using the Citation Template format above]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
```

**Alternatives Rejected**:
- Heterogeneous structures (different sections per system): increases cognitive load during interview prep
- Minimal structure (only objective + diagram): insufficient complexity reasoning for interview readiness
- Paper-journal structure (introduction, related work, methodology): overkill for rapid prep notes; not suitable for community sharing

---

## 4. Template Generation Implementation Strategy

**Rationale for Programmatic Generation**:
- Ensures consistency: same structure, no manual drift
- Reproducibility: new contributors can regenerate all 22 pages from source in <30s
- Maintainability: updates to template structure propagate to all pages automatically
- Testability: pytest validates all 22 pages have required sections and correct format

**Python Script Responsibilities**:
1. **Template generation**: Create markdown skeleton for each system
2. **Citation validation**: Verify citation blocks match template format and URLs are accessible
3. **Diagram inclusion**: Embed Mermaid code blocks in correct section
4. **Complexity metrics**: Pre-populate complexity table with research-backed numbers
5. **Index generation**: Create INDEX.md linking all 22 systems with completion status

**Data Source**:
- System definitions from README.md GenAI Interview section (22 systems across 5 categories)
- Category groupings: Foundations, Language & Dialogue, Multimodal Image, Multimodal Video/Audio, Infrastructure

---

## Summary of Decisions

| Aspect | Decision | Key Benefit |
|--------|----------|------------|
| **Diagram Format** | Mermaid (flowchart + sequence) | Native markdown, version-controllable, learner-friendly |
| **Citation Format** | Custom markdown key-value blocks | Readable, lightweight, extensible, shareable |
| **Page Structure** | 8-section skeleton (identical for all 22) | Consistent UX, rapid content creation, community-friendly |
| **Generation Method** | Python script with pytest validation | Reproducible, maintainable, testable |

---

## Next Steps

→ **Phase 1**: Use these decisions to design data model (`data-model.md`) and create contracts for skeleton page structure and citation blocks (`contracts/`).

→ **Phase 2** (`/speckit.tasks`): Generate task breakdown for implementing template generation script, validating all 22 skeleton pages, and preparing community release.
