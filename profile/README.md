<p align="center">
  <img src="logo.png" alt="caboose-mcp logo" width="180" />
</p>

<h1 align="center">⚙️ caboose-mcp</h1>

<p align="center">
  Open-source tools for AI-assisted development — MCP servers, language tooling, and more.
</p>

---

## 📊 Status Dashboard

| Repository | PRs | Last Build | Last Deploy | Status |
|-----------|-----|-----------|------------|--------|
| [**fafb**](https://github.com/caboose-mcp/fafb) | None | Docker (in progress) | Deploy Bots ✅ | 🟡 In Progress |
| [**ui**](https://github.com/caboose-mcp/ui) | [1 open](https://github.com/caboose-mcp/ui/pulls) | CI ✅ | N/A | 🟢 Ready |
| [**meml**](https://github.com/caboose-mcp/meml) | None | No runs | N/A | ⚪ Idle |
| [**extensions**](https://github.com/caboose-mcp/extensions) | [2 open](https://github.com/caboose-mcp/extensions/pulls) | Code review ✅ | N/A | 🟡 WIP Testing |
| [**app**](https://github.com/caboose-mcp/app) (private) | None | Build failed ❌ | N/A | 🔴 WIP Testing |

### 📋 Open PRs

- **ui**: [fix: remove all Auth Portal and Changelog references](https://github.com/caboose-mcp/ui/pull/29)
- **extensions**: [fix(vscode-fafb): address PR review — race condition, SSE state, UX, type safety, lint, docs](https://github.com/caboose-mcp/extensions/pull/2)
- **extensions**: [feat: add vscode-fafb VS Code extension](https://github.com/caboose-mcp/extensions/pull/1)

### 🔗 Quick Links

- 🚀 [View All Workflows](https://github.com/orgs/caboose-mcp/actions)
- 📋 [Open Issues](https://github.com/orgs/caboose-mcp/repositories?q=is%3Aopen+is%3Aissue)
- 🔀 [Open PRs](https://github.com/orgs/caboose-mcp/repositories?q=is%3Aopen+is%3Apr)

---

## 📦 Projects

### [🔧 fafb](https://github.com/caboose-mcp/fafb)
The caboose-mcp monorepo. Contains the core MCP server (Go 1.24) and accompanying tools. Node packages include n8n workflows.

### [🎨 ui](https://github.com/caboose-mcp/ui)
React/Vite/Tailwind frontend for caboose-mcp — browse tools, view changelogs, and try the sandbox. Deployed to [ui.mcp.chrismarasco.io](https://ui.mcp.chrismarasco.io).

### [🔌 extensions](https://github.com/caboose-mcp/extensions)
VS Code extensions and language tooling integrations. Current: `vscode-fafb` for MCP server integration.

### [🎭 meml](https://github.com/caboose-mcp/meml)
**Emoji Markup Language (EML)** — a config language with first-class emoji support. A Go-based parser and toolchain for a human-friendly configuration format.
