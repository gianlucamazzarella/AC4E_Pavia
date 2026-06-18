# Topic 2 Reading - Research Pipeline and Spec-Driven Development

Spec-driven development helps keep research coding grounded in the research
question. It separates intent, requirements, design, and tasks so the agent does
not jump from a vague idea to a sprawling code edit.

## SDD For Research

| Stage | Research artifact |
| --- | --- |
| Intent | research question, contribution, audience, success criteria |
| Requirements | data contracts, output formats, numerical tolerances, replication needs |
| Design | data flow, estimator/model, robustness plan, folder map |
| Tasks | issues with acceptance criteria and verification |

## EARS Acceptance Criteria

Use concrete forms:

- WHEN a clean run starts, the pipeline SHALL exit 0.
- GIVEN fixed inputs, the script SHALL produce the same table values.
- IF a data source is unavailable, the repo SHALL document the blocker.

## Artifact Checklist

- `docs/research_design_memo.md`
- `docs/data_source_map.md`
- `references/bibliography.bib`
- backlog issues with acceptance criteria
- `notes/context_patterns.md`
