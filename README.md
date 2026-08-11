<div align="center">
  <img src="assets/banner.svg" alt="Awesome Coding Agents for Robot Learning" width="100%">
</div>

<div align="center">

<!-- stats-badges:start -->
[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/Papers-0-2F80ED?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-6-6C5CE7?style=flat-square)
![Open source](https://img.shields.io/badge/Open_source-0-00A86B?style=flat-square)
![Real robot](https://img.shields.io/badge/Real_robot-0-E17055?style=flat-square)
![Related systems](https://img.shields.io/badge/Related_systems-0-7F8C8D?style=flat-square)
<br>
![Code as Policy](https://img.shields.io/badge/Code_as_Policy-0-3867D6?style=flat-square)
![Simulation and Task Generation](https://img.shields.io/badge/Simulation_%26_Tasks-0-20BF6B?style=flat-square)
![Automated Reward Design](https://img.shields.io/badge/Reward_Design-0-F7B731?style=flat-square)
![Automated Robot Evaluation](https://img.shields.io/badge/Robot_Evaluation-0-EB3B5A?style=flat-square)
![Synthetic Data Generation for Policy Learning](https://img.shields.io/badge/Synthetic_Data-0-8854D0?style=flat-square)
![Agentic Policy Training and Robot Autoresearch](https://img.shields.io/badge/Agentic_Training-0-0FB9B1?style=flat-square)
<!-- stats-badges:end -->

[![Update README](https://github.com/harooos/awesome-coding-agents-for-robot-learning/actions/workflows/update-readme.yml/badge.svg)](https://github.com/harooos/awesome-coding-agents-for-robot-learning/actions/workflows/update-readme.yml)
[![Last commit](https://img.shields.io/github/last-commit/harooos/awesome-coding-agents-for-robot-learning?style=flat-square)](https://github.com/harooos/awesome-coding-agents-for-robot-learning/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

**A curated research map of coding agents that create, execute, evaluate, and improve robot-learning systems.**

[Scope](#scope) · [Taxonomy](#taxonomy) · [Paper List](#paper-list) · [Contributing](#contributing) · [Citation](#citation)

</div>

> [!NOTE]
> This repository is in an early curation stage. The taxonomy is intentionally treated as a working map of research topics observed in the literature—not as a claim that the topics are mutually exclusive.

## Contents

- [What is a Coding Agent for Robot Learning?](#what-is-a-coding-agent-for-robot-learning)
- [Scope](#scope)
- [Taxonomy](#taxonomy)
- [At a Glance](#at-a-glance)
- [Legend and Annotation Axes](#legend-and-annotation-axes)
- [Curator's Picks](#curators-picks)
- [Paper List](#paper-list)
  - [Code as Policy](#1-code-as-policy)
  - [Simulation and Task Generation](#2-simulation-and-task-generation)
  - [Automated Reward Design](#3-automated-reward-design)
  - [Automated Robot Evaluation](#4-automated-robot-evaluation)
  - [Synthetic Data Generation for Policy Learning](#5-synthetic-data-generation-for-policy-learning)
  - [Agentic Policy Training and Robot Autoresearch](#6-agentic-policy-training-and-robot-autoresearch)
- [How to Read Cross-topic Systems](#how-to-read-cross-topic-systems)
- [Updates](#updates)
- [Contributing](#contributing)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)

## What is a Coding Agent for Robot Learning?

In this list, a **coding agent** is an LLM-based system that generates or modifies executable artifacts in a robot-learning workflow and uses tool or execution feedback to make progress. The artifact may be a robot policy, a simulator task, a reward function, an evaluator, a data-generation program, or training code.

The list asks a concrete question for every entry:

> **What code does the agent write or change, and what happens when that code is executed?**

This framing is broader than **Code as Policy (CaP)**, where generated code is itself the policy executed by the robot. CaP remains a full, independent topic here; the other sections focus on coding agents elsewhere in robot learning.

## Scope

### Core inclusion criteria

A work belongs in the **core list** when it satisfies all of the following:

1. It uses an LLM or coding agent to generate, edit, select, or debug executable code or a comparably structured executable artifact.
2. The artifact is part of a robot-learning system: policy, task/environment, reward, evaluator/verifier, data pipeline, or policy-training loop.
3. The generated artifact is actually executed, compiled, trained, simulated, or deployed—not only shown as text.
4. The work reports empirical evidence in simulation, on a real robot, or both.

### Related systems

Relevant systems that do not cleanly satisfy the core definition may still appear as **Related** when they are important for understanding the research topic. Common cases include:

- synthetic-data systems whose coding-agent component is unclear;
- VLM evaluators that predict success but do not generate executable evaluation logic;
- automated robot-learning pipelines whose experiment controller is not an LLM agent;
- environment generators that create assets or videos but not executable simulation tasks.

Related entries are labeled explicitly and are excluded from the core-paper badge count.

### Generally out of scope

- LLM planners that output only natural-language plans or low-level actions;
- general-purpose robotics foundation models without code generation or editing;
- ordinary simulator procedural generation without an LLM/coding agent;
- papers that propose code generation but never execute or evaluate the generated artifact;
- generic software-engineering agents applied to a robotics repository without a robot-learning research question.

## Taxonomy

The taxonomy is induced from recurring research questions, baselines, and evaluation protocols in the literature. Topics may overlap; a system can appear in more than one section.

| Topic | Community research question | Primary artifact |
|---|---|---|
| **Code as Policy** | Can an agent generate or debug a program that directly controls a robot? | Executable policy, skill, or policy graph |
| **Simulation and Task Generation** | Can an agent create valid, diverse, and learnable robot tasks or curricula in a simulator? | Environment/task code and assets |
| **Automated Reward Design** | With the task and simulator largely fixed, can an agent design a reward that produces a stronger learned policy? | Reward function and reward parameters |
| **Automated Robot Evaluation** | Can success, progress, safety, and failure modes be judged automatically and reproducibly? | Evaluator, verifier, test scenario, or reset logic |
| **Synthetic Data Generation** | Can agent-generated tasks and rollouts produce data that improves an independent learned policy? | Trajectories, annotations, and datasets |
| **Agentic Policy Training** | Can an agent act as a robot-learning researcher by running experiments, changing code, and iterating on policies? | Training pipeline and trained policy |

## At a Glance

<!-- stats-table:start -->
| Topic | Core | Related | Total |
|---|---:|---:|---:|
| Code as Policy | 0 | 0 | 0 |
| Simulation and Task Generation | 0 | 0 | 0 |
| Automated Reward Design | 0 | 0 | 0 |
| Automated Robot Evaluation | 0 | 0 | 0 |
| Synthetic Data Generation for Policy Learning | 0 | 0 | 0 |
| Agentic Policy Training and Robot Autoresearch | 0 | 0 | 0 |
| **Unique works** | **0** | **0** | **0** |
<!-- stats-table:end -->

Last curated update: <!-- last-updated:start -->
2026-08-11
<!-- last-updated:end -->

## Legend and Annotation Axes

Each work is summarized using the same evidence-oriented fields:

| Field | What it tells you |
|---|---|
| **Agent writes / changes** | The concrete executable artifact produced by the coding agent |
| **Feedback loop** | Compiler errors, simulator traces, reward, training curves, human feedback, or real-robot outcomes available to the agent |
| **Final artifact** | What the system ultimately leaves behind: policy, environment, reward, evaluator, dataset, or training system |
| **Evaluation** | Simulator/robot setup, scale, baselines, and headline evidence |
| **Resources** | Paper, code, project page, dataset, and video links |

Entry labels:

- `Core` — satisfies the core inclusion criteria.
- `Related` — important adjacent system; the strictness note explains why it is not core.
- `Real` — includes real-robot evaluation.
- `Code` — has a public implementation or official code release.
- `Pick` — selected as a particularly useful starting point, not necessarily “best paper.”

## Curator's Picks

<!-- curator-picks:start -->
_Curator's Picks will be added after the first topic-level audit._
<!-- curator-picks:end -->

## Paper List

### 1. Code as Policy

**Research question.** Can a coding agent synthesize, compose, debug, or optimize code that directly constitutes the robot's policy?

The defining property is that the generated program is on the robot's execution path. This includes direct API calls, hierarchical skill programs, behavior trees, computation graphs, and other executable policy representations. A work does not leave this topic merely because it also uses simulation, verification, or search to improve the program.

**Typical evaluation:** task success, generalization to new instructions/objects/scenes, runtime failures, recovery, execution efficiency, and real-robot transfer.

<!-- topic:code-as-policy:start -->
_No entries curated yet._
<!-- topic:code-as-policy:end -->

**Questions to track**

- How much improvement comes from code representation versus stronger perception or skill libraries?
- Does execution feedback improve the policy, or only repair syntax and API errors?
- Can generated policies generalize across embodiments and long-horizon tasks?
- What safety boundary exists between agent-written code and robot actuation?

### 2. Simulation and Task Generation

**Research question.** Can a coding agent turn a task description, asset set, video, or learning signal into an executable robot simulation task or curriculum?

In practice, a usable task often bundles scene construction, assets, initial-state sampling, observations, success conditions, rewards, termination, and reset. We therefore treat **task generation as a system-level topic**, rather than trying to separate every simulator component into a different chapter.

Reward-generation papers may still form their own topic when they hold the environment largely fixed and make reward quality the controlled research variable.

**Typical evaluation:** task validity, code pass rate, task diversity, learnability, policy transfer across generated tasks, curriculum quality, and human effort saved.

<!-- topic:simulation-task-generation:start -->
_No entries curated yet._
<!-- topic:simulation-task-generation:end -->

**Questions to track**

- Is the output merely visually plausible, or executable and physically valid?
- Are generated tasks novel, solvable, and useful for learning?
- Does the generator respond to learner performance when constructing a curriculum?
- Which parts still require human-authored templates, assets, or privileged simulator state?

### 3. Automated Reward Design

**Research question.** Given a task and simulator, can a coding agent generate and iteratively improve a reward function that trains a better policy?

Reward is part of an environment implementation, but automated reward design is a recognizable research line because papers often fix the simulator and task, compare reward-generation methods, and evaluate the resulting policy. The object of study is not whether a whole world can be generated; it is whether the **training signal** is effective, robust, and transferable.

**Typical evaluation:** downstream RL performance, sample efficiency, reward hacking, robustness, transfer, human reward-engineering effort, and agreement with task success.

<!-- topic:reward-design:start -->
_No entries curated yet._
<!-- topic:reward-design:end -->

**Questions to track**

- What feedback does the agent receive when revising a reward?
- Does the learned policy optimize the intended task or exploit simulator artifacts?
- Are dense rewards necessary, or can verifiers and sparse success signals suffice?
- Does an automatically designed reward survive sim-to-real transfer?

### 4. Automated Robot Evaluation

**Research question.** Can an automated system determine whether a robot succeeded, how far it progressed, why it failed, and whether it remained safe?

Evaluation is kept as a dedicated topic because it has its own target: **measurement reliability**, not primarily policy learning. Relevant work includes generated success predicates, visual-language evaluators, failure diagnosis, automated test-scenario construction, reset systems, and infrastructure for repeated or long-running evaluation.

Core entries must contain a coding-agent or executable-artifact component. Purely learned visual evaluators can be retained as Related systems when they define important baselines or protocols.

**Typical evaluation:** agreement with human labels, false-positive/false-negative rates, calibration, robustness to viewpoint and scene changes, coverage of failure modes, reset reliability, and unattended runtime.

<!-- topic:robot-evaluation:start -->
_No entries curated yet._
<!-- topic:robot-evaluation:end -->

**Questions to track**

- Can a verifier detect partial success and safety violations, not only terminal success?
- What evidence is used: privileged simulator state, video, robot telemetry, or generated tests?
- Does evaluator error corrupt data collection or policy optimization downstream?
- Can evaluation run repeatedly on real robots without hidden human intervention?

### 5. Synthetic Data Generation for Policy Learning

**Research question.** Can coding agents generate executable tasks and successful trajectories that train or improve a separate robot policy?

This section requires evidence beyond “we generated scenes” or “we collected trajectories.” The central result should connect the generated data to downstream policy learning. Systems may overlap heavily with simulation/task generation; they appear here when **data utility** is a principal claim.

**Typical evaluation:** dataset scale and diversity, success filtering, downstream BC/RL/VLA performance, comparison with human or procedural data, out-of-distribution generalization, and sim-to-real transfer.

<!-- topic:synthetic-data:start -->
_No entries curated yet._
<!-- topic:synthetic-data:end -->

**Questions to track**

- Is data utility established by training an independent policy?
- How are failed, low-quality, or duplicated trajectories filtered?
- What is synthetic versus manually specified in the generation pipeline?
- Does the system close the loop by generating new data from policy failures?

### 6. Agentic Policy Training and Robot Autoresearch

**Research question.** Can a coding agent operate as a robot-learning engineer or researcher by running experiments, modifying training code, diagnosing failures, and iterating on a learned policy?

The generated code is usually **not** the deployed policy. Instead, the coding agent lives in an outer research loop and may change algorithms, hyperparameters, data collection, reward, reset, verifier, or policy composition. This distinguishes the topic from Code as Policy.

**Typical evaluation:** number and quality of autonomous iterations, policy improvement over time, intervention count, breadth of algorithms/tasks, reproducibility, real-robot uptime, and comparison with human-designed training.

<!-- topic:agentic-policy-training:start -->
_No entries curated yet._
<!-- topic:agentic-policy-training:end -->

**Questions to track**

- Does the agent make substantive research decisions or only launch a fixed recipe?
- Can it diagnose whether failures come from data, environment, reward, or optimization?
- Does the loop improve an independently evaluated policy across multiple iterations?
- What human intervention, safety supervision, and infrastructure are still required?

## How to Read Cross-topic Systems

The same work may be listed in several sections when it makes substantial claims in each. This is intentional. Examples of legitimate overlap include:

- task generation **and** synthetic-data generation when generated simulations produce training trajectories;
- reward design **and** agentic policy training when an agent revises rewards inside a broader experiment loop;
- evaluation **and** autoresearch when verifiers drive real-robot policy iteration;
- Code as Policy **and** simulation search when simulation feedback optimizes an executable policy program.

The per-topic badge counts count appearances in that topic. The overall paper count is deduplicated by work ID.

## Updates

<details open>
<summary><strong>Development log</strong></summary>

- **2026-08-11** — repository bootstrap: long-form README, working six-topic taxonomy, evidence-oriented entry schema, automatic statistics, contribution workflow, banner, and citation metadata.

</details>

## Contributing

Paper suggestions, corrections, missing code links, and classification challenges are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

The fastest contribution path is:

1. open a paper-suggestion issue with the paper and code links;
2. state exactly what executable artifact the agent generates or changes;
3. identify the feedback loop and empirical robot-learning evidence;
4. note whether the work is best treated as Core or Related.

The generated parts of this README should not be edited manually. Add or update records in `data/papers.json`, then run:

```bash
python scripts/update_readme.py
python scripts/update_readme.py --check
```

## Citation

If this collection is useful in your research, please cite it using GitHub's **Cite this repository** button or the metadata in [CITATION.cff](CITATION.cff).

```bibtex
@misc{awesome-coding-agents-robot-learning,
  title        = {Awesome Coding Agents for Robot Learning},
  author       = {harooos and contributors},
  year         = {2026},
  howpublished = {\url{https://github.com/harooos/awesome-coding-agents-for-robot-learning}},
  note         = {A curated research map of coding agents for robot learning}
}
```

## Acknowledgements

The presentation and curation discipline are inspired in part by [AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) and the broader [awesome list](https://awesome.re) community.

This list is built by reading papers, project pages, and source repositories with assistance from coding agents, followed by human review. Errors are possible; corrections are encouraged.

## License

Distributed under the [MIT License](LICENSE).
