# Issue Count Model

## Goal

Open issue counts should make workflow pressure visible without requiring the user to leave the board.

## Current Prototype Data

Each task stores issue counts by severity:

```js
issues: {
  critical: 1,
  high: 2,
  medium: 3
}
```

The task-level open issue count is the sum of those values.

The column-level count is the sum of all task issue counts inside the column.

The inspector-level count is the sum of all active board task issues.

## Suggested GitHub Mapping

If this board reads from GitHub, use labels or fields to classify severity:

| GitHub Signal | Board Field |
| --- | --- |
| `severity:critical` label | Critical |
| `severity:high` label | High |
| `severity:medium` label | Medium |
| `state:open` | Counted as open |
| `state:closed` | Excluded from open counts |

## Suggested Workflow Health Rules

Health can be computed from issue pressure and stale work:

| Rule | Health |
| --- | --- |
| Any critical issue is open | At risk |
| Multiple high issues are open | Watch |
| No open issues and recent activity | Healthy |
| No activity for more than 24 hours in an active lane | Watch |
| No activity for more than 48 hours in an active lane | At risk |

## Notes

The current app keeps these rules simple and local. A future GitHub-backed version should make the mapping configurable because teams often use different labels, milestones, projects, and status fields.
