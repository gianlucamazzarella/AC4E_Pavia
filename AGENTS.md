# Agent Instructions - AC4E Pavia Participant Repo

## Project

This is the participant repository for the Agentic Coding for Economists Pavia
workshop. It contains public instructional materials, examples, templates, and
participant work products.

## Workflow

- Use issue -> branch -> pull request for non-trivial changes.
- Plan before editing multiple files.
- Keep edits scoped to the active day/topic.
- Run the documented verification command before claiming work is complete.
- Treat agent output as a proposal until a human reviews the diff and evidence.

## Economics Standards

- Document data sources, transformations, units, and sample restrictions.
- Use relative paths.
- Do not modify raw data.
- Separate research claims from code mechanics.
- Do not let agents certify identification, causality, or interpretation.

## Privacy

- Do not commit secrets, API keys, private data, or confidential manuscripts.
- Do not ask agents to read `data/raw/`, `data/private/`, or `.env`.
- If using a cloud or autonomous agent, complete the risk card before connecting it to research work.

## Verification

Run:

```bash
python3 -m pytest examples/mini-economics/tests
```

For final packaging, also follow `replication/README.md`.
