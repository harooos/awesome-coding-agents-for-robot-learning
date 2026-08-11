# Contributing

Thank you for helping improve **Awesome Coding Agents for Robot Learning**. Contributions may add a work, correct an existing record, supply missing resources, or challenge a classification.

## Before adding a work

Check that the contribution can answer these questions:

1. What executable artifact does the LLM or coding agent generate, edit, select, or debug?
2. Where does that artifact sit in the robot-learning system?
3. What feedback is returned after execution, simulation, training, or deployment?
4. What empirical robot-learning evidence is reported?

Works that are highly relevant but fail one core criterion can be marked `related` with a precise `strictness_note`.

## Adding or updating an entry

1. Edit `data/papers.json` using the fields documented in `dev/ENTRY_SCHEMA.md` and `data/paper.schema.json`.
2. Use a stable kebab-case ID. One work has one ID even when it appears in several topics.
3. Prefer the paper's official URL, canonical code repository, and official project page.
4. Keep claims compact and evidence-based. Do not copy an abstract into `summary`.
5. Run:

   ```bash
   python scripts/update_readme.py
   python scripts/update_readme.py --check
   ```

6. Commit both `data/papers.json` and the generated `README.md`.

## Classification guidelines

- Use multiple `topics` when the paper makes a substantive, evaluated claim in each topic—not merely because components coexist in the system.
- Use `core` only when executable code or a comparably structured executable artifact is generated or modified by an LLM/coding agent and evaluated in a robot-learning setting.
- Use `related` for important neighboring systems and explain the exact missing criterion.
- Set `real_robot` only when a physical robot is part of the reported evaluation.
- Set `open_source` only when an official public code implementation is linked.
- Set `curator_pick` sparingly, after a topic-level audit.

## Quality standard

Whenever possible, verify claims against the paper PDF and official repository rather than secondary summaries. Numbers should include enough context to avoid misleading comparisons. If a claim cannot be verified, omit it or state the uncertainty explicitly.

Promotional submissions, duplicate project pages, and entries without a clear connection to the scope may be declined.
