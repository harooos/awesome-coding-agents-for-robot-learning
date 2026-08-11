# Research backlog

These are working questions, not claims for the public README.

## Cross-cutting

- What minimum behavior distinguishes a coding agent from an LLM code generator?
- How often does execution feedback change semantics rather than only repair syntax/API errors?
- What evidence supports “autonomous,” “self-improving,” or “closed-loop” claims?
- Which systems improve an independently evaluated policy rather than their own internal success metric?
- How should human-written skill libraries, templates, and privileged simulator APIs be disclosed?
- Which evaluation protocols make results comparable across systems?

## Code as Policy

- First source audit completed on 2026-08-11; see dev/topic-notes/code-as-policy.md.
- Re-audit deferred boundary cases: GRAPPA, GROOT, Ca2P, RoboClaw, VIA, and other VLA orchestration systems.
- Recheck official code releases for ASPIRE, RHO, and other entries currently marked closed-source.
- Continue recording runtime safety boundaries, recovery mechanisms, scaffold dependence, and cross-embodiment evidence.
- If the full Feishu export becomes available, compare it against the condensed note without flattening its internal taxonomy.

## Simulation and Task Generation

- Distinguish visual/world asset generation from executable task generation.
- Track compilation/runtime validity and downstream learnability separately.
- Identify true learner-conditioned curricula versus static diversity generation.

## Reward Design

- Compare open-loop generation, evolutionary revision, and training-feedback loops.
- Record reward hacking checks and sim-to-real evidence.
- Clarify overlap with success-verifier generation.

## Robot Evaluation

- Determine whether there is a coherent coding-agent core literature or mainly adjacent VLM evaluators.
- Separate success judging, progress estimation, failure diagnosis, test generation, reset, and long-running evaluation.
- Track human-label agreement and real-world reliability.

## Synthetic Data

- Require downstream policy training evidence.
- Compare synthetic-only, synthetic-plus-real, and targeted failure-driven data generation.
- Record filtering, deduplication, and data-quality mechanisms.

## Agentic Policy Training

- Distinguish fixed automation from agents that change algorithms or experiments.
- Record the number of agent-driven iterations and intervention count.
- Separate one-time automatic training from genuine data-training-policy feedback loops.
