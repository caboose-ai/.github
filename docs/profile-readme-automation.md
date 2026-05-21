# Profile README automation

This repository can refresh `profile/README.md` when another repo in the org updates its default branch.

## Receiver setup in this repo

1. Optionally add an org or repository variable named `PROFILE_SOURCE_REPOS`.
   - Value: a comma-separated list of source repos, for example:
     `caboose-ai/api,caboose-ai/web,caboose-ai/docs`
   - If this is not set, the workflow uses the current public Caboose AI repos from the profile README.
   - The repository that triggered the dispatch is included automatically even if it is not listed yet.

2. Add an optional secret named `PROFILE_README_TOKEN`.
   - Use a fine-grained PAT or GitHub App token with read access to the source repos and write access to this `.github` repo.
   - If all source repos are public and this workflow only needs to write this repo, the default `GITHUB_TOKEN` may be enough.

3. Keep `.github/workflows/update-profile-readme.yml` enabled.

## Sender setup in each source repo

Copy this workflow into each source repository as `.github/workflows/notify-profile-readme.yml`.

```yaml
name: Notify profile README

on:
  push:
    branches:
      - main

jobs:
  notify-profile:
    if: github.repository != 'caboose-ai/.github'
    runs-on: ubuntu-latest
    steps:
      - name: Dispatch profile README refresh
        env:
          GH_TOKEN: ${{ secrets.PROFILE_README_DISPATCH_TOKEN }}
          TARGET_REPOSITORY: caboose-ai/.github
        run: |
          gh api \
            --method POST \
            "/repos/$TARGET_REPOSITORY/dispatches" \
            -f event_type=repo-main-updated \
            -f client_payload[repository][full_name]="${{ github.repository }}" \
            -f client_payload[repository][default_branch]="${{ github.event.repository.default_branch }}" \
            -f client_payload[after]="${{ github.sha }}" \
            -f client_payload[pusher]="${{ github.actor }}"
```

Add a source-repo secret named `PROFILE_README_DISPATCH_TOKEN`.

The token must be allowed to call `repository_dispatch` on `caboose-ai/.github`. For a fine-grained PAT, grant access to the `.github` repo with repository `Contents: Read and write` permission.

## Manual refresh

Run the `Update profile README` workflow manually in this repo. Optionally pass a single `owner/repo` value to include that repo in the generated block for the run.
