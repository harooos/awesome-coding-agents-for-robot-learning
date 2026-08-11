# Status

Last updated: 2026-08-11

## Bootstrap

- [x] Confirm one long public README as the primary artifact.
- [x] Rename the internal context directory to `dev/`.
- [x] Establish the six-topic working map.
- [x] Add core/related scope rules.
- [x] Add a banner and badge system.
- [x] Add canonical paper data, README generation, validation, and GitHub Actions automation.
- [x] Add contribution templates, license, and citation metadata.

## Topic curation

| Topic | Status | Immediate next step |
|---|---|---|
| Code as Policy | Existing external notes | Import the Feishu export, then audit every source and map it to the shared schema |
| Simulation and Task Generation | Not started | Build the seed corpus and identify recurring generation/evaluation settings |
| Automated Reward Design | Not started | Audit the reward-generation lineage and its downstream RL protocols |
| Automated Robot Evaluation | Not started | Separate coding-agent evaluators from learned evaluator baselines and infrastructure systems |
| Synthetic Data Generation | Not started | Require downstream policy evidence and record sim-to-real claims carefully |
| Agentic Policy Training | Not started | Distinguish substantive agent decisions from fixed automated training recipes |

## Immediate next step

Choose one topic for a full audit. For that topic, create a working note in `dev/topic-notes/`, follow `dev/TOPIC_WORKFLOW.md`, and add only source-verified records to `data/papers.json`.

## Known blockers

- The existing Code as Policy Feishu page needs to be exported or attached before it can be imported reliably.
- Counts are intentionally zero until entries receive topic-level source verification.
