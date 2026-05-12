# Contract: Citation Block Format

**Version**: 1.0  
**Type**: Markdown Content Contract  
**Purpose**: Define mandatory structure for all citations in GenAI skeleton pages  
**Enforcement**: Validated via regex and pytest during `test_citations.py`  

---

## Canonical Format

Every citation in a skeleton page MUST follow this exact structure:

```markdown
### Citation [N]: [Title]

- **Source**: [URL or Reference ID]
- **Publication Date**: [YYYY-MM-DD or "N/A"]
- **Access Date**: [YYYY-MM-DD when verified]
- **Relevance**: [1-2 sentence summary]
- **Reproducibility**: [artifact used + specific claim supported + verification note]
```

---

## Field Definitions & Constraints

| Field | Type | Required | Pattern | Constraint |
|-------|------|----------|---------|-----------|
| **Citation [N]** | Header | Yes | `### Citation \d+: .{3,100}` | Sequential numbering within page; 3-100 char title |
| **Source** | URL/ID | Yes | `https?://\S+` or `[A-Z0-9_\-]{5,}` | Valid HTTP(S) URL or reference code |
| **Publication Date** | ISO 8601 | Yes | `\d{4}-\d{2}-\d{2}` or `N/A` | Must be ≤ Access Date (if both present) |
| **Access Date** | ISO 8601 | Yes | `\d{4}-\d{2}-\d{2}` | Must be present; no future dates |
| **Relevance** | Text | Yes | `.{20,200}` | 20-200 characters; explains why this source matters |
| **Reproducibility** | Text | Yes | `.{50,500}` | 50-500 characters; artifact + claim + verification |

---

## Validation Rules

### Parse Validation

```python
# Pattern for detecting and validating citation blocks
citation_block_pattern = r"^### Citation (\d+): (.+?)$\n- \*\*Source\*\*: (.+?)$\n- \*\*Publication Date\*\*: (.+?)$\n- \*\*Access Date\*\*: (\d{4}-\d{2}-\d{2})$\n- \*\*Relevance\*\*: (.+?)$\n- \*\*Reproducibility\*\*: (.+?)$"

# Validation checks:
# 1. All citation blocks match regex pattern exactly
# 2. Citation numbers are sequential (1, 2, 3, ...)
# 3. Source URL is accessible (HTTP 200-399 status code)
# 4. Access date is today or earlier
# 5. Relevance is 20-200 characters
# 6. Reproducibility is 50-500 characters
```

### Examples

**✅ VALID**:

```markdown
### Citation 1: Attention Is All You Need

- **Source**: https://arxiv.org/abs/1706.03762
- **Publication Date**: 2017-06-12
- **Access Date**: 2026-05-12
- **Relevance**: Foundational transformer architecture paper, essential for understanding modern GenAI systems
- **Reproducibility**: Paper PDF section 3.2 (Attention mechanism). Verified: math derivation matches implementation in llama.cpp
```

**✅ VALID (no publication date)**:

```markdown
### Citation 2: Llama 2 Blog Post

- **Source**: https://www.meta.com/research/llama-2/
- **Publication Date**: N/A
- **Access Date**: 2026-05-10
- **Relevance**: Meta's official description of Llama 2 training, scaling, and safety approach
- **Reproducibility**: Blog post + linked paper. Verified: 70B model config matches published numbers
```

**❌ INVALID (missing fields)**:

```markdown
### Citation 1: Something

- **Source**: https://example.com
- **Access Date**: 2026-05-12
# Missing: Publication Date, Relevance, Reproducibility
```

**❌ INVALID (wrong date format)**:

```markdown
### Citation 1: Paper Title

- **Source**: https://arxiv.org/abs/1234.56789
- **Publication Date**: May 12, 2017
# WRONG: Should be YYYY-MM-DD format (2017-05-12)
```

---

## Integration with SkeletonPage

### Minimum Citation Requirement

- Every skeleton page MUST include at least 3 citations
- Every skeleton page MUST include at most 5 citations (conciseness for interview prep)
- Citations MUST appear in the "References & Citations" section (after Real-World Applications)

### Citation Placement

```markdown
# [System Number]. [System Name]

## [Other sections...]

## References & Citations

[3-5 citation blocks here, numbered sequentially starting from 1]

### Reproducibility Checklist

- [ ] All claims verified against source material
- [ ] Diagram generated and renders correctly in Markdown
- [ ] Complexity figures match cited papers or benchmarks
- [ ] Real-world examples are current (within 1 year)
- [ ] Page reviewed for consistency with other skeleton pages
```

---

## Reproducibility Field Guidance

The **Reproducibility** field MUST answer three questions:

1. **Artifact Used**: What specific material did you consult?
   - Examples: "GitHub repo meta-llama/llama2", "Paper PDF section 4.1", "Blog post dated 2024-01-15"

2. **Specific Claim Supported**: What exact claim does this artifact support?
   - Examples: "70B model has 4096-dimensional embeddings", "ChatGPT uses RLHF with human feedback dataset", "Latency p95 target is <500ms"

3. **Verification Note**: How did you verify the claim?
   - Examples: "Checked model config.json", "Ran inference and confirmed output shape", "Compared against benchmark results in paper Table 3"

### Full Example

```markdown
- **Reproducibility**: GitHub repo meta-llama/llama2 (commit 8b3191f). Verified: 70B model has 4096-dimensional token embeddings by reading config.json and confirmed via torch.Size of embedding layer during inference run on H100 GPU.
```

---

## Import/Export Contract

### Markdown → JSON (for tooling)

```json
{
  "number": 1,
  "title": "Attention Is All You Need",
  "source": "https://arxiv.org/abs/1706.03762",
  "source_type": "arxiv_paper",
  "publication_date": "2017-06-12",
  "access_date": "2026-05-12",
  "relevance": "Foundational transformer architecture paper, essential for understanding modern GenAI systems",
  "reproducibility_artifact": "Paper PDF section 3.2 (Attention mechanism)",
  "reproducibility_claim": "Multi-head attention computation formula",
  "reproducibility_verification": "Math derivation matches implementation in llama.cpp"
}
```

### JSON → Markdown (for skeleton page generation)

```python
def citation_to_markdown(citation_json):
    return f"""### Citation {citation_json['number']}: {citation_json['title']}

- **Source**: {citation_json['source']}
- **Publication Date**: {citation_json['publication_date']}
- **Access Date**: {citation_json['access_date']}
- **Relevance**: {citation_json['relevance']}
- **Reproducibility**: {citation_json['reproducibility_artifact']}. Verified: {citation_json['reproducibility_verification']}
"""
```

---

## Validation Checklist (for Contributors)

Before submitting a skeleton page with citations:

- [ ] All citation blocks follow canonical format (3 citation fields required)
- [ ] Citation numbers are sequential (1, 2, 3, ...)
- [ ] All source URLs are accessible (test with `curl -I` or browser)
- [ ] All access dates are ≤ today
- [ ] All publication dates are ≤ access dates (if applicable)
- [ ] Relevance field is 20-200 characters and explains why this source matters
- [ ] Reproducibility field is 50-500 characters and includes artifact + claim + verification
- [ ] Total citations per page: 3-5 (not more, not fewer)
- [ ] Citations are placed in "References & Citations" section

---

## Related Documents

- **Data Model** (`data-model.md`): CitationEntry entity definition
- **Research** (`research.md`): Decision rationale for citation format
- **Skeleton Page Contract** (`skeleton_page_contract.md`): Integration with full page structure
