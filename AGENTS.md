# Repository instructions for coding agents

This repository maintains one public-facing, long-form `README.md`. Do not split the public paper list into per-topic Markdown files unless `dev/DECISIONS.md` records a later decision to do so.

## Read first

Before research or edits, read these files in order:

1. `dev/CONTEXT.md`
2. `dev/STATUS.md`
3. `dev/DECISIONS.md`
4. `dev/ENTRY_SCHEMA.md`
5. `dev/TOPIC_WORKFLOW.md` for topic-level work

## Source of truth

- `data/papers.json` is the source of truth for paper records.
- `README.md` is the user-facing artifact.
- Regions wrapped in `<!-- ...:start -->` and `<!-- ...:end -->` are generated. Do not edit their contents by hand.
- Regenerate with `python scripts/update_readme.py` and verify with `python scripts/update_readme.py --check`.

## Research rules

- Start from the paper's actual research question, baselines, and evaluation—not from a desire for a perfectly mutually exclusive taxonomy.
- State exactly what code or executable artifact the agent writes or changes.
- Verify quantitative claims against the paper PDF or official source.
- Treat cross-topic classification as normal when multiple claims are independently evaluated.
- Use `related` plus a precise `strictness_note` when a work is valuable but the coding-agent component is unclear.
- Code as Policy is a full independent topic. Do not subsume it under automated training.
- Keep public prose in English. Development notes may be bilingual.

## Finishing a research session

- Update `dev/STATUS.md` with completed work and the next concrete step.
- Add durable taxonomy or scope decisions to `dev/DECISIONS.md`.
- Put unresolved source notes under `dev/topic-notes/`; do not paste full chat transcripts.
- Ensure the README generator is idempotent and all checks pass.
