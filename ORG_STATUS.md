# caboose-mcp Organization Status

> Last updated: 2026-03-24

## Repository Status Overview

| Repo | PRs | Last Build | Last Deploy | Status |
|------|-----|-----------|------------|--------|
| [fafb](https://github.com/caboose-mcp/fafb) | None | Docker (in progress) | Deploy Bots ✅ | 🟡 In Progress |
| [ui](https://github.com/caboose-mcp/ui) | 1 open | CI ✅ | N/A | 🟢 Ready |
| [meml](https://github.com/caboose-mcp/meml) | None | No runs | N/A | ⚪ Idle |
| [extensions](https://github.com/caboose-mcp/extensions) | 2 open | Code review ✅ | N/A | 🟡 Active |
| [app](https://github.com/caboose-mcp/app) (private) | None | Build failed ❌ | N/A | 🔴 Blocked |
| [WIP] [extensions](https://github.com/caboose-mcp/extensions) | 2 open | Code review ✅ | N/A | 🟡 Testing |
| [WIP] [app](https://github.com/caboose-mcp/app) (private) | None | Build failed ❌ | N/A | 🔴 Testing |

---

## Detailed PR Status

### fafb
- **Open PRs**: None
- **Last Build**: Docker (in progress)
- **Last Deploy**: Deploy Bots ✅

### ui
- **Open PRs**: 1
  - [fix: remove all Auth Portal and Changelog references](https://github.com/caboose-mcp/ui/pull/29) - OPEN
- **Last Build**: CI ✅ (2026-03-24 03:54:26Z)
- **Last Deploy**: N/A

### meml
- **Open PRs**: None
- **Last Build**: No workflow runs
- **Last Deploy**: N/A

### extensions
- **Open PRs**: 2
  - [fix(vscode-fafb): address PR review — race condition, SSE state, UX, type safety, lint, docs](https://github.com/caboose-mcp/extensions/pull/2) - OPEN
  - [feat: add vscode-fafb VS Code extension](https://github.com/caboose-mcp/extensions/pull/1) - OPEN
- **Last Build**: Copilot code review ✅ (2026-03-22 02:34:59Z)
- **Last Deploy**: N/A

### [WIP] app (private)
- **Open PRs**: None
- **Last Build**: Build APK on Main Merge ❌ (2026-03-24 04:50:06Z)
- **Last Deploy**: N/A
- **Status**: Build failures need investigation

### [WIP] extensions
- **Status**: Not fully tested yet

---

## Action Items

- [ ] **fafb**: Monitor Docker build completion
- [ ] **ui**: Review and merge PR #29
- [ ] **extensions**: Review and test both open PRs (not fully tested yet)
- [ ] **app**: Fix APK build failures (private repo)
- [ ] **meml**: Set up CI workflows
