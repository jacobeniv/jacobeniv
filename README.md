# jacobeniv

Claude Code configuration for this account, including a vendored copy of
Google's [Agent Skills](https://github.com/google/skills) catalog.

## Skills

`.claude/skills/` contains all 131 skills from
[google/skills](https://github.com/google/skills), pinned at commit
[`1776276`](https://github.com/google/skills/commit/1776276d672b41e12aba7ead134d473af001d147),
flattened into one directory (the upstream `skills/<category>/<name>/`
layout is collapsed to `.claude/skills/<name>/` since skill names are
unique across categories). These cover Google Cloud, GKE, BigQuery,
Agent Platform, Genkit, Google Ads, Analytics, and Identity products.

They are Google's content, licensed under Apache 2.0 (see `LICENSE`),
not authored in this repo. To refresh them, re-sync from upstream at a
newer commit and re-copy `skills/*/*/` into `.claude/skills/`.

Google's plugin catalog (`.claude-plugin/marketplace.json` upstream) was
not vendored here, since those are separate git-submodule repositories
rather than skills.
