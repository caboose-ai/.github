# Caboose AI Organization

This repository powers the public Caboose AI GitHub organization profile.

GitHub renders organization profile content from:

```text
profile/README.md
```

The rendered organization profile is visible at:

- [caboose-ai](https://github.com/caboose-ai)

The `repo-status` block in the profile README is rendered by
`scripts/update_profile_readme.py`, with a byte-identical Go port in
[`caboose-ai/caboose`](https://github.com/caboose-ai/caboose) (`caboose board`)
ready to take over — see that repo's `docs/pending/` for the workflow switch.
