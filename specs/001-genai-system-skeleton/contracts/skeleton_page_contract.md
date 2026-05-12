# Contract: Skeleton Page Format

**Version**: 1.0  
**Type**: Markdown Content Contract  
**Purpose**: Define mandatory structure for all 22 GenAI skeleton pages  
**Enforcement**: Validated via pytest in `test_template_generator.py::test_skeleton_sections_complete`  
**Applies To**: All generated skeleton pages in `genai_systems/` directory  

---

## Canonical Structure

Every GenAI skeleton page MUST follow this exact section hierarchy and format:

```markdown
# [System Number]. [System Name]

## Objective

[1-2 sentence summary of what this system does and why it matters in GenAI]

## System Architecture

[Mermaid flowchart diagram showing core components and data flow]

[3-5 sentence description of architecture in plain text]

## Technical Approach

### Key Components

- **[Component 1]**: [1-2 sentence description of role and responsibility]
- **[Component 2]**: [1-2 sentence description]
- ... (3-6 components typical)

### Pipeline / Data Flow

[Detailed description of request → processing → response flow, or embed Mermaid sequence diagram]

## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| Model size | [e.g., 7B-70B parameters] | [Implications: latency, cost, hardware] |
| Time complexity | [e.g., O(seq_len), O(n²) attention] | [Memory-bound vs. compute-bound] |
| Space complexity | [e.g., ~2x model size for activations] | [Peak during training vs. inference] |
| Latency target | [e.g., p95 <500ms] | [Real-time vs. batch constraint] |
| Throughput target | [e.g., 100 req/s per GPU] | [Determined by model, batch size, quantization] |

## Pros & Cons

### Pros

- **[Pro 1 Title]**: [1-2 sentence explanation]
- **[Pro 2 Title]**: [1-2 sentence explanation]
- ... (typically 3-5 pros)

### Cons

- **[Con 1 Title]**: [1-2 sentence explanation]
- **[Con 2 Title]**: [1-2 sentence explanation]
- ... (typically 3-5 cons)

### Trade-offs

[1-2 paragraphs discussing key technical trade-offs:
- Model size vs. latency
- Batch size vs. cost
- Fine-tuning vs. zero-shot
- Compute budget vs. quality
- Other domain-specific trade-offs]

## Real-World Applications

### Where This Pattern Appears

- **[Company/Product 1]**: [1-2 sentence description of use case and lessons learned]
- **[Company/Product 2]**: [1-2 sentence description of use case and lessons learned]
- ... (typically 3-5 real-world examples)

### Production Considerations

[2-3 paragraphs covering:
- Scaling challenges (horizontal vs. vertical)
- Failure modes and recovery strategies
- Monitoring and observability requirements
- Cost drivers and optimization strategies
- Team structure and operational overhead]

## References & Citations

[3-5 structured citation blocks following citation_block_contract.md]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
```

---

## Section Specifications

### 1. Title/Heading

```markdown
# [System Number]. [System Name]
```

**Constraints**:
- System number: 2-22 (integer, left-zero-padded to 2 digits, e.g., "02", "04", "22")
- System name: Must match GenAISystem.title from data-model.md
- File name: `[number]_[slug_from_title].md` (e.g., `02_gmail_smart_compose.md`)
- Path: `genai_systems/[category]/[filename]` where category matches CategoryIndex

---

### 2. Objective Section

```markdown
## Objective

[1-2 sentence summary]
```

**Constraints**:
- Exactly one paragraph (1-2 sentences)
- Max 200 characters total
- Must answer: "What does this system do?" and "Why is it important for GenAI?"
- No citations in this section
- Plain English, readable for first-time learner

**Example**:

```markdown
## Objective

Gmail Smart Compose predicts and suggests the next words in email drafts using an on-device ML model. This system demonstrates how real-time language prediction is deployed at scale for billions of users while maintaining low latency and privacy.
```

---

### 3. System Architecture Section

```markdown
## System Architecture

[Mermaid diagram]

[3-5 sentence description]
```

**Diagram Constraints** (Mermaid):
- Type: flowchart LR (left-to-right) or flowchart TD (top-down)
- Nodes: core components (LLM, encoder, decoder, storage, inference engine, etc.)
- Edges: labeled with data flow type (embeddings, tokens, vectors, etc.)
- Complexity: 5-10 nodes typical; <15 nodes maximum
- Syntax: Must render in <500ms in GitHub Markdown viewer

**Text Description Constraints**:
- 3-5 sentences describing the diagram
- Explain data flow and component responsibilities
- Highlight key architectural decisions (e.g., client-side vs. server-side, batch vs. streaming)
- Mention performance implications (latency, throughput)

**Example Diagram**:

```markdown
## System Architecture

graph LR
    A["User Input"] -->|embeddings| B["Encoder<br/>(Transformer)"]
    B -->|attention features| C["LLM<br/>(7B-70B params)"]
    C -->|logits| D["Decoder<br/>(Softmax)"]
    D -->|token| E["Token Selection"]
    E -->|top-k sampling| F["Output"]
    C -->|KV cache| G["Storage<br/>(GPU memory)"]
    G -->|retrieve| C

The architecture consists of an encoder-decoder transformer stack with efficient attention mechanisms. The encoder processes input embeddings and produces contextual representations. The LLM core performs autoregressive decoding, generating one token at a time. A KV cache layer stores attention key-value pairs to avoid recomputation, reducing latency from O(n²) to O(n). Token selection uses top-k sampling to balance diversity and coherence.
```

---

### 4. Technical Approach Section

```markdown
## Technical Approach

### Key Components

- **[Component]**: [description]
- ...

### Pipeline / Data Flow

[description or diagram]
```

**Key Components Constraints**:
- 3-6 components typical
- Format: `**[Name]**: [1-2 sentence description]`
- Include: input processor, model, cache/storage, output formatter, safety filter (if applicable)

**Pipeline Constraints**:
- Can be prose or Mermaid sequence diagram
- Must explain: request entry → processing stages → response format
- Must identify: bottlenecks, parallelizable stages, serial dependencies

---

### 5. Complexity Analysis Section

```markdown
## Complexity Analysis

| Metric | Complexity | Notes |
|--------|-----------|-------|
| Model size | ... | ... |
| Time complexity | ... | ... |
| Space complexity | ... | ... |
| Latency target | ... | ... |
| Throughput target | ... | ... |
```

**Constraints**:
- Exactly 5 rows (one per metric)
- All cells must be non-empty (no null/N/A values)
- Complexity values must be specific and measurable (e.g., "7B parameters" not just "large")
- Notes must include operational implications
- Must match GenAISystem.complexity_metrics from data-model.md

**Examples**:

```markdown
| Model size | 70B parameters | Requires 140GB GPU memory (FP16); cost ≈ $2-5 per million tokens |
| Time complexity | O(seq_len × hidden²) attention | Quadratic in sequence length; KV cache mitigates linear complexity |
| Space complexity | ~2x model size for activations | 140GB for storage + 280GB for training gradients peak |
| Latency target | p95 <500ms | Single request; batch inference enables higher throughput |
| Throughput target | 20-50 req/s per GPU | Depends on model, batch size, quantization (int8, int4) |
```

---

### 6. Pros & Cons Section

```markdown
## Pros & Cons

### Pros
- **[Title]**: [description]
- ...

### Cons
- **[Title]**: [description]
- ...

### Trade-offs

[paragraphs]
```

**Constraints**:
- 3-5 pros typical
- 3-5 cons typical
- Each pro/con: title + 1-2 sentence explanation
- Trade-offs: 1-2 paragraphs (150-300 words) explaining key decisions and compromises
- Compare against alternative approaches (if applicable)

---

### 7. Real-World Applications Section

```markdown
## Real-World Applications

### Where This Pattern Appears

- **[Company/Product]**: [description]
- ...

### Production Considerations

[paragraphs]
```

**Where This Pattern Appears Constraints**:
- 3-5 real-world examples typical
- Format: `**[Company/Product]**: [1-2 sentence use case]`
- Examples must be current (published within last 2 years)
- Include a mix: large tech companies, startups, research labs

**Production Considerations Constraints**:
- 2-3 paragraphs (300-500 words)
- Cover: scaling challenges, failure modes, monitoring, cost optimization, team structure
- Based on public documentation or research papers
- Realistic constraints (not idealized scenarios)

**Example**:

```markdown
### Production Considerations

ChatGPT-style systems require sophisticated infrastructure for scaling. Latency requirements (p95 <1s for chat interactions) demand careful resource allocation: GPU utilization must be balanced against context switching overhead. Cache coherency across multiple GPUs becomes a bottleneck; solutions include: sequence pipelining, disaggregated inference, and speculative decoding. Cost is the primary constraint: a 70B model generating 1M tokens/day at $0.002/1K tokens costs ~$2K/day in inference alone. Teams must implement sophisticated monitoring (token latency, queue depth, cost per request) to stay within budgets.
```

---

### 8. References & Citations Section

```markdown
## References & Citations

[3-5 citation blocks]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
```

**Constraints**:
- 3-5 citations (enforced minimum/maximum)
- Each citation follows `citation_block_contract.md` format exactly
- All source URLs must be accessible (HTTP 200-399)
- Checklist: exactly as shown above (5 items, all present at page generation)

---

## Validation Rules

### Structural Validation

```python
# Pseudo-code for validation
def validate_skeleton_page(file_path):
    content = read_file(file_path)
    
    # Check: all required sections present
    required_sections = [
        "# ",           # Title
        "## Objective",
        "## System Architecture",
        "## Technical Approach",
        "## Complexity Analysis",
        "## Pros & Cons",
        "## Real-World Applications",
        "## References & Citations",
        "### Reproducibility Checklist"
    ]
    for section in required_sections:
        assert section in content, f"Missing section: {section}"
    
    # Check: correct section order (regex-based line matching)
    section_order_regex = r"# .+\n## Objective\n## System Architecture\n..."
    assert re.search(section_order_regex, content)
    
    # Check: complexity table well-formed
    table_regex = r"\| Model size \| .+ \| .+ \|"
    assert re.search(table_regex, content)
    
    # Check: citation blocks (3-5)
    citations = re.findall(r"### Citation \d+:", content)
    assert 3 <= len(citations) <= 5, f"Expected 3-5 citations, found {len(citations)}"
    
    # Check: word count (target 500-800 words)
    word_count = len(content.split())
    assert 400 <= word_count <= 1000, f"Word count {word_count} outside typical range"
    
    return True
```

### Content Validation

- ✅ All section headings use H2 (`##`) except title (H1, `#`)
- ✅ Complexity table has exactly 5 rows
- ✅ Citation numbering is sequential (1, 2, 3, ...)
- ✅ Citation source URLs are accessible
- ✅ Mermaid diagram syntax is valid
- ✅ No broken internal links
- ✅ File name matches system number and title slug
- ✅ No TODOs or placeholder text (except in Pros/Cons/Real-World, which are placeholders for learners to fill)

---

## File Naming Convention

```
genai_systems/
├── 001_foundations/
│   ├── 02_gmail_smart_compose.md
│   └── 03_google_translate.md
├── 002_language_dialogue/
│   ├── 04_chatgpt_assistant.md
│   ├── 05_rag_system.md
│   ├── 06_code_generation.md
│   ├── 07_document_qa.md
│   └── 08_meeting_summarizer.md
├── 003_multimodal_image/
├── 004_multimodal_video_audio/
└── 005_infrastructure/
```

**Naming Rules**:
- System number: 2-22 (leading zero for single digits: 02, 03, ..., 09, 10, ...)
- Slug: derived from system name (lowercase, hyphens between words, max 50 characters)
- File extension: `.md` (mandatory)
- Max path length: 244 bytes (GitHub filename limit) ✓ All paths comply

---

## Integration with Master Index

The master index (`genai_systems/INDEX.md`) includes:

```markdown
## Category: [Name]

| # | System | Status | Sections | Citations | Diagrams | Edited |
|-|--------|--------|----------|-----------|----------|---------|
| 02 | Gmail Smart Compose | ⬜ Not started | ✓ 8/8 | ✓ 3/3 | ✓ 1/1 | N/A |
| 03 | Google Translate | ⬜ Not started | ✓ 8/8 | ✓ 4/3 | ✓ 1/1 | N/A |
```

Each skeleton page is tracked for:
- **Status**: Not started (⬜) → In progress (🟨) → Ready for review (🟦) → Completed (✅)
- **Sections**: Count of populated sections / 8 required
- **Citations**: Count of citations / minimum 3
- **Diagrams**: Count of diagrams / target 1-2
- **Edited**: Date last modified by human (learner)

---

## Related Documents

- **Citation Block Contract** (`citation_block_contract.md`): Defines citation format
- **Data Model** (`data-model.md`): GenAISystem, SkeletonPage, CitationEntry entities
- **Research** (`research.md`): Design decisions and rationale
- **Quick Start** (`quickstart.md`): Generation and editing instructions
