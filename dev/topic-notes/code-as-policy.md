# Code as Policy audit

Audit date: 2026-08-11

## Public framing

The section is organized around a stable artifact-level idea:

> A foundation model uses its coding prior to synthesize an external, executable robot policy. The model need not itself be the fast control policy.

The public README compresses the evolution into five readable stages:

1. a function or program generated once;
2. a program revised from rollout feedback;
3. programs plus persistent skill memory;
4. structured graphs or multi-file repositories;
5. agent harnesses that orchestrate frozen neural and classical controllers.

This is a reading aid, not a claim that every work falls into one mutually exclusive generation.

## Inputs

- The user's condensed CaP research note supplied in chat.
- The user's reference repository: https://github.com/lysandre001/awesome-code-as-policy-Robot-learning
- Original papers, official project pages, and official code repositories for every public record.

## First-pass result

- 22 Core works.
- 3 Related systems.
- 10 official code releases.
- 16 Core works with physical-robot evidence under the current annotation rules.

The curated records span:

- foundations and deployable code generation: Code as Policies, PromptBook, RoboScript, RoboCodeX, GenCHiP, RoboPro;
- closed-loop diagnosis and rewriting: RoboCoder, DAHLIA, HyCodePolicy, neuro-symbolic CaP, AOR, and CaP-X;
- persistent skill memory: Growing with Your Embodied Agent, RATs, ASPIRE, and ARCHITECT;
- structured and hybrid policies: GenSwarm, RHO, GaP, Harness VLA, and MEMENTO;
- broad interface/benchmark work: ALRM and Claude Plays Robotics;
- productized systems retained as Related: Waddle and Telekinesis.

## Boundary decisions

### Included as Core

- One-shot systems are valid CaP when generated code is actually executed as the policy.
- Programs may call learned primitives, VLAs, motion planners, or classical controllers.
- Simulation, verification, search, and persistent memory do not move a work out of CaP when the final deployed artifact remains executable policy structure.

### Included as Related

- **Claude Plays Robotics:** evaluates a programmatic-control condition but is primarily a cross-interface capability study.
- **Waddle:** presents a deployed CaP and skill-memory product with real-hardware evidence, but no paper-level benchmark protocol or reproducible release.
- **Telekinesis:** documents reviewable Python policy generation over a typed skill library, but no controlled robot-learning evaluation.

### Excluded or routed elsewhere

- **SayCan:** selects skills rather than generating an executed policy program.
- **Chain of Code:** general language-model code execution, not a robot-learning contribution.
- **NLaP:** focuses on non-code low-level planning outputs rather than executed robot policy code.
- **ENPIRE:** edits the outer policy-development and training loop; route to Agentic Policy Training / Robot Autoresearch.
- **LabVLA / RoboGenesis:** generates demonstrations to train a separate VLA; route to Synthetic Data.
- **Maestro:** conceptually relevant, but the arXiv preprint is withdrawn and currently has no active paper version.

### Deferred pending a deeper artifact audit

- GRAPPA: clarify whether its deployed artifact is generated policy code or online action guidance.
- GROOT and Ca2P: verify execution path, feedback loop, and empirical evidence.
- RoboClaw: distinguish a general coding-agent robotics framework from a CaP research contribution.
- VIA and newer VLA orchestration systems: determine whether they generate executable policy structure or only select actions/tools.

## Verification conventions

- Dates use the first public version, not the latest revision date.
- open_source: true requires an official code link, not a promise that code will be released.
- Quantitative claims are included only when recoverable from the paper or official project page.
- Related product entries use conservative evidence language and explicit strictness notes.
- Cross-topic tags are not added before the destination topic receives its own audit; for example, RoboPro's Video2Code pipeline will be reconsidered during Synthetic Data curation.

## Follow-up

1. Recheck deferred candidates and official code releases.
2. Compare the full Feishu export if it becomes available.
3. Consider adding a structured field for policy carrier or agent role only if the same axes prove useful across several topics; for now the public stage table is enough.
