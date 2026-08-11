# Topic research workflow

Use this workflow for each topic. The aim is a reliable awesome-list section, not a full survey paper.

## 1. Define the observed research question

- Write the question the papers actually optimize.
- Identify what is normally held fixed and what is generated or improved.
- List the common baselines and evaluation metrics.
- Keep adjacent systems visible without weakening the Core boundary.

## 2. Build a candidate corpus

- Start from known seed papers, their references, and later citing work.
- Search project pages, lab pages, code repositories, and relevant benchmarks.
- Record candidates in `dev/topic-notes/<topic>.md` before inclusion.
- Include negative decisions; they prevent the same out-of-scope work from being reconsidered repeatedly.

## 3. Audit each candidate

Read the official paper and answer:

1. What does the agent write or modify?
2. Is that artifact executable?
3. What feedback is available to the agent?
4. Is there iteration, or only one-shot generation?
5. What is the final artifact?
6. How is it evaluated?
7. Is a real robot used?
8. What human templates, demonstrations, or interventions remain?
9. Does the paper make a substantive claim in more than one topic?
10. Is it Core or Related, and why?

## 4. Enter verified records

- Add records to `data/papers.json`.
- Keep `summary` analytic and compact.
- Put claims in `evaluation` only when the source and setting are clear.
- Use `curator_pick` only after comparing the topic's main approaches.
- Regenerate and check README.

## 5. Synthesize the topic

Update the hand-written introduction and “Questions to track” in README only when the audited corpus changes the framing. Add durable decisions to `dev/DECISIONS.md`.

## 6. Close the session

- Update `dev/STATUS.md`.
- Leave the next search query or candidate set in the topic note.
- Run `python scripts/update_readme.py --check`.
