# Tool Lane - Other Agents

Use this lane for Antigravity, OpenClaw, Hermes, Eve, Windsurf, Cline, or another
compatible coding or autonomous agent.

## Portable Mapping

| Course need | Look for this in your tool |
| --- | --- |
| Project instructions | `AGENTS.md`, rules, memories, instruction files |
| Reusable workflow | skills, commands, routines, playbooks |
| Role isolation | subagents, custom agents, workers, roles |
| Tool access | MCP, plugins, tools, connections, gateways |
| Long-running work | goals, schedules, tasks, background agents |
| Review | diffs, logs, PRs, transcripts, run evidence |

## Required Before Autonomous Use

Before connecting an autonomous agent to research files, fill:

```text
agent-harness/autonomous_agent_risk_card.md
```

## Reading Links

- OpenClaw: <https://github.com/openclaw/openclaw>
- OpenClaw skills: <https://docs.openclaw.ai/tools/skills>
- Hermes Agent by Nous Research: <https://hermes-agent.nousresearch.com/>
- Eve by Vercel: <https://vercel.com/eve>

## Rule

If the tool can act without you watching, require stronger logging, narrower
permissions, and a human approval gate before outputs enter the repo.
