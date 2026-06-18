# Tool Lane - CLI Agents

Use this lane for terminal-first workflows such as Codex CLI, Claude Code CLI,
Cursor CLI, or another command-line coding agent.

## Setup

From the repo root, verify Python first:

```bash
python3 -m pytest examples/mini-economics/tests
```

Then launch your agent from the same directory.

## Workflow

Use explicit prompts:

```text
Read AGENTS.md and days/day1.md. Do not edit files. Summarize the active task,
allowed files, and verification command.
```

```text
Plan the implementation for issue #N. Do not edit files yet. Include files,
steps, risks, and verification.
```

```text
Implement issue #N only. Stay within the allowed files. Run the verification
command and report the output.
```

## CLI Discipline

- Keep one terminal session per branch.
- Prefer small commits.
- Paste exact command output into review notes when useful.
- Do not give the agent broad write access to confidential folders.
