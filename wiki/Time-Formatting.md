# Time Formatting

## Goal

The board should feel familiar to users of chat and collaboration tools. Primary timestamps use relative time where possible, similar to Discord, while still exposing a static EDT timestamp for auditability.

## Current Behavior

By default, each task displays:

```text
12 minutes ago
May 21, 1:03 AM EDT
```

The top toolbar includes a toggle that swaps the priority:

```text
May 21, 1:03 AM EDT
12 minutes ago
```

## Relative Time

Relative labels are generated with `Intl.RelativeTimeFormat`, using the user's browser locale.

Examples:

- `this minute`
- `12 minutes ago`
- `3 hours ago`
- `yesterday`
- `2 days ago`

## Static EDT Fallback

Static timestamps use `Intl.DateTimeFormat` with:

```js
timeZone: "America/New_York"
```

This keeps the fallback pinned to Eastern time and lets the browser render `EST` or `EDT` depending on daylight saving time.

## Future GitHub Integration

If this is connected to GitHub issues, timestamps can be taken from:

- Issue `updated_at`.
- Pull request `updated_at`.
- Workflow run `updated_at`.
- Review or check-run completion timestamps.
