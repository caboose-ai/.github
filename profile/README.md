<p align="center">
  <img src="logo.png" alt="Caboose AI logo" width="180" />
</p>

<h1 align="center">🚂 Caboose AI</h1>

<p align="center">
  Open-source AI tooling, homelab infrastructure, and developer-experience experiments.
</p>

---

## 📊 Organization Snapshot

> Manually refreshed on 2026-05-10. This is a lightweight snapshot while we work toward a live status board.

| Repository | Focus | Language | Open PRs | Last Build | Status | Notes |
|-----------|-------|----------|----------|------------|--------|-------|
| [**caboose-ai.io**](https://github.com/caboose-ai/caboose-ai.io) | Self-hosted homelab infrastructure stack and CLI tooling | Go | None | CI ✅ | 🟢 Active | - |
| [**ai-skills**](https://github.com/caboose-ai/ai-skills) | Reusable Claude/Codex skills published by Caboose AI | Python | None | No runs | 🟢 Active | - |
| [**homebrew-tap**](https://github.com/caboose-ai/homebrew-tap) | Homebrew formulae for Caboose AI CLI tools | Ruby | None | No runs | 🟢 Active | - |
| [**mcp-server**](https://github.com/caboose-ai/mcp-server) | Go MCP server and companion REST API | Go | 1 | No runs | 🟢 Active | PR #8 addressing review comments |
| [**waldo**](https://github.com/caboose-ai/waldo) | Persistent persona system for AI tools | Go | None | Pages build/deploy ✅ | 🟢 Active | - |
| [**meml**](https://github.com/caboose-ai/meml) | Emoji-first configuration language parser/toolchain | Go | None | No runs | ⚪ Needs CI | CI setup needed |
| [**.github**](https://github.com/caboose-ai/.github) | Organization profile, docs, and status snapshots | Markdown | None | No runs | 🟢 Active | PR #12 in review |

### 🔗 Quick Links

- 🏠 [Organization repositories](https://github.com/orgs/caboose-ai/repositories)
- 📋 [Open issues](https://github.com/search?q=org%3Acaboose-ai+is%3Aissue+is%3Aopen&type=issues)
- 🔀 [Open pull requests](https://github.com/search?q=org%3Acaboose-ai+is%3Apr+is%3Aopen&type=pullrequests)

---

## 📦 Repository Map

### [🌐 caboose-ai.io](https://github.com/caboose-ai/caboose-ai.io)
Go monorepo for the Caboose AI self-hosted homelab stack, including SSO with Authentik and services such as Forgejo, Woodpecker CI, Grafana, Open WebUI, SonarQube, Mattermost, Ghost, and related operational tooling.

### [🧰 ai-skills](https://github.com/caboose-ai/ai-skills)
A collection of reusable Claude/Codex skills. The current published skill set includes a maximum-effort status line with dynamic segments and install instructions for agent environments.

### [🍺 homebrew-tap](https://github.com/caboose-ai/homebrew-tap)
Homebrew tap for distributing Caboose AI command-line tools from tagged releases, including the homelab CLI and MCP-related utilities.

### [🔌 mcp-server](https://github.com/caboose-ai/mcp-server)
Model Context Protocol server written in Go, paired with a PostgreSQL-backed REST API. It exposes sample tools such as `calculate` and `dad_joke` over MCP stdio and HTTP interfaces.

### [🎭 waldo](https://github.com/caboose-ai/waldo)
Persistent persona system for AI tools. Define a voice, tone, and style once, then reuse it across Claude Code, Cursor, ChatGPT, Gemini, Codeium, and other agent workflows.

### [😄 meml](https://github.com/caboose-ai/meml)
MEML/EML explores emoji-first configuration syntax: emoji section decorators, key annotations, emoji keys, and emoji value atoms in a Go parser/toolchain.

### [🏢 .github](https://github.com/caboose-ai/.github)
Organization-level profile and documentation repository. For now, it keeps a manually refreshed snapshot; eventually it should become or feed a live status board.

---

## 🧭 Status Board Roadmap

- [ ] Replace the manual snapshot with generated data from the GitHub API.
- [ ] Track open PRs, issues, latest workflow conclusions, default branches, and release tags per repository.
- [ ] Publish the generated dashboard to the organization profile or a dedicated page.
- [ ] Add scheduled refreshes so the board reflects live organization health.
