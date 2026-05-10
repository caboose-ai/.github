# Caboose AI Organization Status

> Last updated: 2026-05-10
>
> This is a manual snapshot of the public `caboose-ai` organization. The intended next step is a generated/live status board that refreshes from the GitHub API.

## Repository Status Overview

| Repo | Focus | Language | Open PRs | Last Build | Status |
|------|-------|----------|----------|------------|--------|
| [caboose-ai.io](https://github.com/caboose-ai/caboose-ai.io) | Homelab infrastructure stack and CLI tooling | Go | None | CI ✅ (2026-05-10) | 🟢 Active |
| [ai-skills](https://github.com/caboose-ai/ai-skills) | Reusable Claude/Codex skills | Python | None | No runs | 🟢 Active |
| [homebrew-tap](https://github.com/caboose-ai/homebrew-tap) | Homebrew tap for Caboose AI tools | Ruby | None | No runs | 🟢 Active |
| [mcp-server](https://github.com/caboose-ai/mcp-server) | Go MCP server and REST API | Go | 1 | Addressing comment on PR #8 ✅ (2026-05-08) | 🟢 Active |
| [waldo](https://github.com/caboose-ai/waldo) | Persistent persona system for AI tools | Go | None | Pages build/deploy ✅ (2026-04-18) | 🟢 Active |
| [meml](https://github.com/caboose-ai/meml) | Emoji-first configuration language | Go | None | No runs | ⚪ Needs CI |
| [.github](https://github.com/caboose-ai/.github) | Organization profile and documentation | Markdown | None | Copilot code review ✅ (2026-03-24) | 🟢 Active |

---

## Detailed Repository Notes

### caboose-ai.io
- **Purpose**: Go monorepo for a self-hosted homelab infrastructure stack with SSO via Authentik.
- **Notable services**: Forgejo, Woodpecker CI, Portainer, Grafana, Open WebUI, SonarQube, Mattermost, Ghost, Paperclip, and Homarr.
- **Open PRs**: None
- **Last Build**: CI ✅ (2026-05-10)

### ai-skills
- **Purpose**: Reusable Claude/Codex skills published by Caboose AI.
- **Current highlight**: Maximum Effort Status Line skill for agent status displays.
- **Open PRs**: None
- **Last Build**: No workflow runs found

### homebrew-tap
- **Purpose**: Homebrew tap for Caboose AI command-line tools.
- **Current formulae**: `caboose-homelab` and `caboose-homelab-mcp` from `caboose-ai/caboose-ai.io` tagged releases.
- **Open PRs**: None
- **Last Build**: No workflow runs found

### mcp-server
- **Purpose**: Model Context Protocol server written in Go, plus a PostgreSQL-backed REST API.
- **Current tools**: `calculate` and `dad_joke` over MCP stdio and companion HTTP surfaces.
- **Open PRs**: 1
- **Last Build**: Addressing comment on PR #8 ✅ (2026-05-08)

### waldo
- **Purpose**: Persistent persona system for AI tools.
- **Supported workflows**: Define and reuse voice, tone, and style across Claude Code, Cursor, ChatGPT, Gemini, Codeium, and other tools.
- **Open PRs**: None
- **Last Build**: Pages build/deploy ✅ (2026-04-18)

### meml
- **Purpose**: MEML/EML parser and toolchain for an emoji-first configuration language.
- **Language idea**: Emoji can serve as section decorators, key annotations, pure keys, and value atoms.
- **Open PRs**: None
- **Last Build**: No workflow runs found

### .github
- **Purpose**: Organization-level profile, documentation, and status snapshots.
- **Future role**: Host or feed the generated live organization status board.
- **Open PRs**: None
- **Last Build**: Copilot code review ✅ (2026-03-24)

---

## Action Items

- [ ] **meml**: Set up CI workflows.
- [ ] **ai-skills**: Decide whether skills need CI, validation, or release checks.
- [ ] **homebrew-tap**: Consider formula validation workflows.
- [ ] **.github**: Add a generator for this status snapshot using the GitHub API.
- [ ] **.github**: Publish a live or scheduled status board for organization health.
