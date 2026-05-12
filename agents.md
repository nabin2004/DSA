
# Agents and Workspace Agent Modes

This document defines how automated agents (Copilot / workspace assistants) and contributors should behave when authoring, editing, or generating content in this repository.

Purpose

- Make agent behaviour explicit and auditable.
- Reduce accidental edits to code and tests.
- Ensure generated content is traceable and reviewable.

Quick start

- For content generation use the `GenAI Skeleton Agent` (see below) with `.prompt.md` variables.
- For editing lessons, use the `DSA Content Agent` rules: keep changes small, preserve lesson order, and include author metadata.

Agent Modes

1) DSA Content Agent

- Scope: `001_intro/`, `002_arrays/`, `genai_systems/` and other top-level lesson files.
- Purpose: draft and refine lesson content, exercises, and notebooks.
- Rules:
  - Preserve lesson order listed in `README.md` and the syllabus tracker.
  - Avoid direct edits to `src/` unless accompanied by tests and a PR with human approval.
  - Do not perform large automated refactors; open an issue first.

2) GenAI Skeleton Agent

- Scope: `specs/001-genai-system-skeleton/` and `genai_systems/` outputs.
- Purpose: produce spec-compliant skeleton pages and draft content for review.
- Rules:
  - Follow `specs/001-genai-system-skeleton/contracts/skeleton_page_contract.md` for structure and required headings.
  - Validate citations using `specs/001-genai-system-skeleton/contracts/citation_block_contract.md`.
  - Output files must include frontmatter with `id`, `title`, `author`, `status: draft`, and `source`.
  - Place generated drafts in `genai_systems/` and open a PR referencing the generating prompt.

Common Guidance

- Tests: any change touching `src/` or `tests/` must include or update tests in `tests/`.
- Review: all agent-generated content requires a human reviewer before merging.
- Provenance: include a `generated_with` field in frontmatter describing the agent and prompt used.
- Naming: prefer `YYYY-MM-DD-<slug>.md` or `<spec-id>-<short-slug>.md` for generated pages.

Templates and examples

Example frontmatter for generated pages:

---
id: g001
title: "Example System"
author: "AutoGen"
status: draft
source: specs/001-genai-system-skeleton/spec.md
generated_with: GenAI Skeleton Agent
---

Minimal generation prompt (use `.prompt.md` variables):

"Generate a skeleton page for 'Gmail Smart Compose' following `specs/001-genai-system-skeleton/spec.md`. Include required headings and a citation block per contract. Mark as `status: draft` and add provenance metadata."

Validation checklist for agents

- All required headings from `skeleton_page_contract.md` present.
- Frontmatter includes `id`, `title`, `author`, `status`, `source`.
- Citation blocks validate against `citation_block_contract.md`.
- File saved under `genai_systems/` and a PR opened for review.

See also

- `specs/001-genai-system-skeleton/.agent.md` — specialized instructions for skeleton generation.
- `.instructions.md` — workspace-level agent rules and escalation.
- `.prompt.md` — shared prompt variables and templates.

