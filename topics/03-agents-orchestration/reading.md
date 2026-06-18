# Topic 3 Reading - Agents, Skills, Subagents, Orchestration

Advanced agent work is not about letting the model run wild. It is about using
the right harness piece for the job.

## Harness Pieces

| Need | Use |
| --- | --- |
| Persistent rules | `AGENTS.md`, `CLAUDE.md`, Cursor rules |
| Repeated procedure | skill (`SKILL.md`) |
| Independent review | subagent/custom agent |
| Long isolated work | branch agent, cloud agent, or worktree |
| Many workstreams | GitHub issues and labels |
| New autonomous systems | risk card before execution |

## Tool Updates Checked June 18, 2026

- Codex: app, CLI, web, IDE, GitHub workflows, `AGENTS.md`, skills, subagents, hooks, goals.
- Claude Code: app, CLI, web, IDE, skills, subagents, hooks, goals/checkpoints, GitHub workflows.
- Cursor: Cloud Agents, subagents, Agent Skills, CLI, MCP, hooks, review surfaces.
- Other agents: use the same review discipline even when UI and terminology differ.

## Autonomous Agents

Read these as examples of where the field is moving:

- OpenClaw: <https://github.com/openclaw/openclaw>
- OpenClaw skills: <https://docs.openclaw.ai/tools/skills>
- Hermes Agent by Nous Research: <https://hermes-agent.nousresearch.com/>
- Eve by Vercel: <https://vercel.com/eve>

Eve is especially new in the public Vercel surface. Verify its current docs before
teaching from screenshots or live commands.
