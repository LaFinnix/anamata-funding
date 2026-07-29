# Funding Landscape — live snapshot

These two files are **the source of truth** for what Anamata Kāhui is eligible to apply for right now.

## What's in this folder

- `TRACKER.md` — every funding round for Anamata Records, with eligibility status, deadlines, and notes. Living register; rows are added/updated by the funding cron.
- `ELIGIBILITY-RADAR.md` — auto-evaluated snapshot of which rounds Anamata is eligible for, with the eligibility gates (NZBN, cultural reviewer, co-funding capability, etc.) listed at the top.

## How this gets updated

The funding cron (in the main Hermes workspace) reads `TRACKER.md` weekly and refreshes the radar's "Active rounds" section. Manual edits to TRACKER.md propagate on the next cron run.

The `ELIGIBILITY-RADAR.md` is *additive* — never edit by hand, edit `TRACKER.md`.

## How to read this for a new application

1. Check `ELIGIBILITY-RADAR.md` for currently-open rounds (has deadline countdown).
2. Cross-reference against `TRACKER.md` for the round's eligibility notes (e.g., "requires matched funding", "specific genre").
3. Check the round's typical $ award + frequency to prioritise.
4. Read the relevant template at `01-templates/` for the round's question shape.
5. Draft + archive in `02-past-applications/`.

## What this is NOT

These files don't tell you **how to apply** — that's what the round-specific README at `02-past-applications/<round>/` covers (after submission). They tell you **what to apply for** and **what fits Anamata**.

## When this goes stale

If TRACKER.md is more than 30 days old without a refresh, the active-rounds table is unreliable. Run `hermes cron run <funding-cron-job-id>` to refresh.