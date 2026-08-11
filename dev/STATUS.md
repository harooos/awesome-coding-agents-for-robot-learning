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
| Code as Policy | First audit complete: 22 Core + 3 Related | Review the draft PR, then audit deferred boundary cases and newly released code |
| Simulation and Task Generation | Not started | Build the seed corpus and identify recurring generation/evaluation settings |
| Automated Reward Design | Not started | Audit the reward-generation lineage and its downstream RL protocols |
| Automated Robot Evaluation | Not started | Separate coding-agent evaluators from learned evaluator baselines and infrastructure systems |
| Synthetic Data Generation | Not started | Require downstream policy evidence and record sim-to-real claims carefully |
| Agentic Policy Training | Not started | Distinguish substantive agent decisions from fixed automated training recipes |

## Immediate next step

Review and merge the Code as Policy draft PR. Then choose the next topic for a full audit and follow dev/TOPIC_WORKFLOW.md.

## Known blockers

- The full Code as Policy Feishu page is still unavailable, but the user-provided condensed note was sufficient for the first audit.
- Other five topic counts remain intentionally zero until they receive topic-level source verification.
