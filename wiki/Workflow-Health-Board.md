# Workflow Health Board

## Purpose

The board is designed for engineering and product operations teams that need to scan delivery status quickly. It keeps the kanban layout familiar while adding workflow health, issue pressure, and stale-work signals directly where work is happening.

## Board Areas

### Sidebar

The sidebar provides board navigation and a global open issue count across active workflow lanes.

### Top Bar

The top bar shows the board title, last sync time, a refresh action, and a time display toggle.

### Columns

Each column includes:

- Work item count.
- Total open issues in that column.
- Computed workflow health based on the tasks inside the column.

### Task Cards

Each task card includes:

- Task title.
- Owner initials.
- Task health.
- Open issue count.
- Last updated time.
- Static EDT timestamp fallback.

### Workflow Inspector

The inspector summarizes:

- Overall workflow health.
- Total open issues.
- Critical issue count.
- Stuck or watched work.
- Healthy work count.
- Severity breakdown.
- Items needing attention.

## Health States

| State | Meaning |
| --- | --- |
| Healthy | Work is moving normally. |
| Watch | Work has notable issue pressure or age. |
| At risk | Work has critical issues or is stale enough to require intervention. |
| Paused | Work is not actively moving but is not currently at risk. |

## Implementation Notes

The current prototype is static and self-contained:

- `index.html` defines the app shell and board regions.
- `styles.css` defines responsive layout and visual states.
- `app.js` defines sample board data, health aggregation, issue totals, and time formatting.
