# Setup

Documentation checked: **June 18, 2026**. Vendor UI labels and install commands
change quickly. Use official docs as the source of truth and verify in your
installed version before the workshop.

## Required

- GitHub account
- Git
- Python 3.10 or newer
- One main coding agent: Codex app, Claude Code app, Cursor, CLI agent, or other compatible agent
- A terminal

## Recommended

- Python 3.12+
- `uv` or Conda for environment management
- VS Code if you are not using Cursor
- GitHub CLI (`gh`)

## Install Python Dependencies

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pytest examples/mini-economics/tests
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
py -3 -m pip install --upgrade pip
py -3 -m pip install -r requirements.txt
py -3 -m pytest examples/mini-economics/tests
```

## Choose A Tool Lane

| Tool | Lane |
| --- | --- |
| Codex desktop/app-first workflow | [`tool-lanes/codex-app.md`](tool-lanes/codex-app.md) |
| Claude Code desktop/app-first workflow | [`tool-lanes/claude-app.md`](tool-lanes/claude-app.md) |
| Cursor IDE workflow | [`tool-lanes/cursor.md`](tool-lanes/cursor.md) |
| Terminal-first agents | [`tool-lanes/cli-agents.md`](tool-lanes/cli-agents.md) |
| Antigravity, OpenClaw, Hermes, Eve, or other agents | [`tool-lanes/other-agents.md`](tool-lanes/other-agents.md) |

## Official Docs

- Codex: <https://developers.openai.com/codex>
- Claude Code: <https://code.claude.com/docs/en/overview>
- Cursor: <https://cursor.com/docs>
- OpenClaw: <https://github.com/openclaw/openclaw>
- Hermes Agent: <https://hermes-agent.nousresearch.com/>
- Eve by Vercel: <https://vercel.com/eve>

## Privacy

Do not put restricted data, secrets, passwords, API keys, or unpublished third
party material into prompts. Keep raw or restricted data outside AI context unless
you have explicit permission and understand the tool's data boundary.
