# Day 1 - Foundations, GitHub, Governance, Project Kickoff

## Definition Of Done

- Fork and clone this repo.
- Run the mini economics tests.
- Choose a tool lane.
- Create or refine `docs/project_brief.md`.
- Create at least one issue and one branch.
- Record your tool-lane notes.

## Flow

| Time | Activity |
| --- | --- |
| 09:30-09:45 | Kickoff and repository orientation |
| 09:45-10:15 | Demo: app-first agent tour and GitHub workflow |
| 10:15-11:30 | Sprint: fork, clone, setup, guided test |
| 11:45-12:30 | Sprint: `AGENTS.md`, privacy, first issue/branch |
| 13:30-14:30 | Lab: project brief and backlog seed |
| 14:30-15:15 | Review: first PR path and context notes |
| 15:15-15:30 | Wrap-up |

## Read

- [`topics/01-foundations/reading.md`](../topics/01-foundations/reading.md)
- [`tool-lanes/codex-app.md`](../tool-lanes/codex-app.md), [`claude-app.md`](../tool-lanes/claude-app.md), or [`cursor.md`](../tool-lanes/cursor.md)

## Do

1. Run:

   ```bash
   python3 -m pytest examples/mini-economics/tests
   ```

2. Fill:
   - `docs/project_brief.md`
   - `notes/context_patterns.md`

3. Ask your agent:

   ```text
   Read AGENTS.md, days/day1.md, and topics/01-foundations/checklist.md.
   Do not edit files. Tell me the Day 1 definition of done and the safest first issue.
   ```
