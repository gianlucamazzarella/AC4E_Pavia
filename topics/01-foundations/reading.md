# Topic 1 Reading - Foundations, GitHub, and Governance

Agentic coding is a workflow: the agent reads context, proposes a plan, edits or
runs tools when allowed, and verifies outputs. You remain responsible for scope,
privacy, interpretation, and acceptance.

## Core Ideas

- **Read-only mode:** ask for explanation, file maps, or risks before edits.
- **Plan mode:** ask for a concrete implementation plan and acceptance criteria.
- **Implementation mode:** allow edits only after scope is clear.
- **Debug mode:** reproduce the symptom, inspect evidence, change one thing, rerun.
- **Governance:** put stable instructions in `AGENTS.md`; use tool adapters only when useful.
- **GitHub control plane:** issue -> branch -> pull request -> review -> merge.

## Official Links

- Codex `AGENTS.md`: <https://developers.openai.com/codex/guides/agents-md>
- Cursor rules/context: <https://cursor.com/docs/context/rules>
- Claude Code memory: <https://code.claude.com/docs/en/memory>
- GitHub pull requests: <https://docs.github.com/en/pull-requests>

## Artifact Checklist

- `docs/project_brief.md`
- `AGENTS.md`
- optional `CLAUDE.md` or `.cursor/rules/`
- `notes/context_patterns.md`
- first issue and branch
