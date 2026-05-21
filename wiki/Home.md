# Workflow Health Board

The Workflow Health Board extends a standard delivery board with health signals, open issue counts, and clear timestamp handling.

## What It Shows

- Workflow columns for Backlog, In progress, Review, and Done.
- Open issue counts at the column and task level.
- Workflow health at the column and task level.
- A right-side inspector with total open issues, critical issues, stuck work, healthy work, and severity breakdowns.
- Discord-style relative timestamps with a static EDT fallback.

## Local Preview

Open `index.html` in a browser from the project folder.

## Pages

- [Workflow Health Board](Workflow-Health-Board.md)
- [Time Formatting](Time-Formatting.md)
- [Issue Count Model](Issue-Count-Model.md)

## Publishing To GitHub Wiki

GitHub Wikis are backed by a separate repository named `OWNER/REPO.wiki.git`.

From this project folder, publish these pages with:

```powershell
.\scripts\publish-github-wiki.ps1 -Repository OWNER/REPO
```
