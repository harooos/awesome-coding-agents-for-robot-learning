<div align="center">
  <img src="assets/banner.svg" alt="Awesome Coding Agents for Robot Learning" width="100%">
</div>

<div align="center">

<!-- stats-badges:start -->
[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/Papers-22-2F80ED?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-6-6C5CE7?style=flat-square)
![Open source](https://img.shields.io/badge/Open_source-10-00A86B?style=flat-square)
![Real robot](https://img.shields.io/badge/Real_robot-16-E17055?style=flat-square)
![Related systems](https://img.shields.io/badge/Related_systems-3-7F8C8D?style=flat-square)
<br>
![Code as Policy](https://img.shields.io/badge/Code_as_Policy-22-3867D6?style=flat-square)
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

In this list, a **coding agent** is an LLM-based system that generates or modifies executable artifacts in a robot-learning workflow. The simplest systems synthesize once; agentic systems additionally inspect tool or execution feedback and revise their artifacts. The artifact may be a robot policy, a simulator task, a reward function, an evaluator, a data-generation program, or training code.

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
| Code as Policy | 22 | 3 | 25 |
| Simulation and Task Generation | 0 | 0 | 0 |
| Automated Reward Design | 0 | 0 | 0 |
| Automated Robot Evaluation | 0 | 0 | 0 |
| Synthetic Data Generation for Policy Learning | 0 | 0 | 0 |
| Agentic Policy Training and Robot Autoresearch | 0 | 0 | 0 |
| **Unique works** | **22** | **3** | **25** |
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
- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** — A clean division of labor: the coding agent handles semantics, long-horizon recovery, and memory while the frozen VLA handles local contact-rich motion. _Code as Policy._
- **[GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness for Variational Automation Tasks](https://arxiv.org/abs/2607.05369)** — Replaces a monolithic policy script with an editable computation graph and uses generated simulations to rehearse candidate structures. _Code as Policy._
- **[RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458)** — Expands the policy artifact from one program to a repository, shifting expensive search before deployment while retaining fixed execution. _Code as Policy._
- **[ASPIRE: Agentic Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** — Treats external code memory as continual learning: verified repairs are abstracted into reusable skills rather than folded into model weights. _Code as Policy._
- **[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435)** — Turns CaP into a controlled agent benchmark and shows how abstraction quality and test-time computation jointly determine reliability. _Code as Policy._
- **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)** — The foundational CaP formulation: repurpose a language model's code prior to synthesize inspectable robot policies over a curated API. _Code as Policy._
<!-- curator-picks:end -->

## Paper List

### 1. Code as Policy

**Research question.** Can a coding agent synthesize, compose, debug, or optimize code that directly constitutes the robot's policy?

The defining property is that the generated program is on the robot's execution path. This includes direct API calls, hierarchical skill programs, behavior trees, computation graphs, and other executable policy representations. A work does not leave this topic merely because it also uses simulation, verification, or search to improve the program.

The key idea is **policy synthesis, not necessarily direct model control**: the foundation model's coding prior is used to construct an external policy that can be executed, inspected, tested, and deployed. Across the literature, both the policy carrier and the coding agent's role have expanded:

| Stage | Policy carrier | Coding agent role |
| --- | --- | --- |
| Program synthesis | A Python function or script | Generate a policy from an instruction |
| Agentic repair | A repeatedly revised program | Execute, inspect failures, and rewrite |
| Persistent learning | Programs plus a skill library | Validate fixes and distill reusable skills |
| Structured policy | A computation graph or multi-file repository | Edit nodes, routes, tools, prompts, and control logic |
| Agent–VLA harness | A program around frozen neural and classical controllers | Plan, bind, retry, recover, and manage memory above fast control |

This boundary is about the final deployed artifact. Systems that mainly edit rewards, data, training code, or algorithms and ultimately produce a learned policy belong under [Agentic Policy Training and Robot Autoresearch](#6-agentic-policy-training-and-robot-autoresearch), even when they use similar coding-agent machinery.

**Typical evaluation:** task success, generalization to new instructions/objects/scenes, runtime failures, recovery, execution efficiency, and real-robot transfer.

<!-- topic:code-as-policy:start -->
| Date | Work | Agent writes / changes | Feedback loop | Final artifact | Evaluation | Resources |
|---|---|---|---|---|---|---|
| 2026-07 | **[MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/abs/2607.22832)** — arXiv<br>`Core` `Code` `Real` | Executable policies and rollout evaluators evolved through mutation, crossover, and memory. | • Rollout scores<br>• Failure memories<br>• Evaluator-guided evolutionary selection | An evolved executable policy and its learned evaluator. | Robosuite Tower of Hanoi, AI2-THOR tasks, held-out variants, and sim-to-real transfer to a Franka robot. | [Paper](https://arxiv.org/abs/2607.22832) · [Code](https://github.com/sygkounas/MEMENTO) |
| 2026-07 | **[Introducing Waddle: Agents that Control Robots](https://www.waddlelabs.ai/research/introducing-waddle)** — Waddle Labs Blog<br>`Related` `Real` | Task programs and parameterized skills that compose fixed perception and control primitives or call action models. | • Camera observations<br>• Intermediate outcome verification<br>• Failure-triggered replanning | A runnable task program plus skills shared across deployed agents. | Real-hardware demonstrations, an internal model comparison, and a reported overnight run of roughly 1,000 LEGO operations used to train ACT.<br>**Strictness:** A product research post with real-hardware demonstrations and internal evaluations, but without a paper-level benchmark protocol or reproducible release. | [Project](https://www.waddlelabs.ai/research/introducing-waddle) |
| 2026-07 | **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** — arXiv<br>`Core` `Pick` `Code` | Task programs, primitive bindings, retry logic, and memories around a frozen VLA. | • Task-specific execution traces<br>• Global success rules<br>• Primitive failure models | An agent harness that composes analytic primitives with a retryable VLA primitive. | Perturbed LIBERO-Pro, RoboCasa365, and RoboTwin C2R simulation benchmarks. | [Paper](https://arxiv.org/abs/2607.08448) · [Code](https://github.com/RLinf/RPent) |
| 2026-07 | **[GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness for Variational Automation Tasks](https://arxiv.org/abs/2607.05369)** — arXiv<br>`Core` `Pick` `Code` `Real` | Directed computation graphs whose nodes are modular perception, planning, and control skills. | • Parallel simulation rehearsal<br>• Task success and throughput<br>• Graph-structure and parameter search | A rehearsed computation graph deployed as the robot policy. | Eight new variational-automation benchmarks: four simulated and four physical. | [Paper](https://arxiv.org/abs/2607.05369) · [Code](https://github.com/graph-robots/graph-as-policy) · [Project](https://graph-robots.github.io/gap/) |
| 2026-07 | **[Claude Plays Robotics](https://www.anthropic.com/research/claude-plays-robotics)** — Anthropic Research<br>`Related` | Python controllers in the programmatic-control condition; other conditions use direct, learned-policy, or high-level interfaces. | • Simulator state and rendered observations<br>• Execution outcomes<br>• Interface-specific observations | Controller code in one evaluation condition. | A cross-interface capability study spanning classical control, legged robots, and manipulation in simulation, with separate physical-robot demonstrations.<br>**Strictness:** A capability and interface study rather than a standalone CaP method; included because one evaluated interface asks the model to write robot controllers. | [Paper](https://www.anthropic.com/research/claude-plays-robotics) |
| 2026-07 | **[A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784)** — arXiv<br>`Core` `Code` `Real` | Modular robot programs and persistent skills grounded from localized language corrections. | • Human natural-language corrections<br>• Program execution traces<br>• Skill-library retrieval | An executable policy program plus a reusable skill library. | Physical Franka tasks spanning long horizons, articulated-object manipulation, and cloth folding. | [Paper](https://arxiv.org/abs/2607.23784) · [Code](https://github.com/robo-architect/architect-franka) · [Project](https://robo-architect.github.io/) |
| 2026-06 | **[RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458)** — arXiv<br>`Core` `Pick` | Interpretable multi-file repositories containing prompts, tools, wrappers, routing, and control code. | • Environment reward<br>• Program execution traces<br>• Reflective repository-level search | A pre-deployment-optimized neurosymbolic policy repository. | LIBERO-Pro, robosuite, and held-out O3DE tasks, including single-turn deployment and harness-efficiency measures. | [Paper](https://arxiv.org/abs/2606.16458) · [Project](https://rho-robotics.github.io/) |
| 2026-06 | **[Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419)** — arXiv<br>`Core` `Code` `Real` | Self-proposed task programs and persistent skills distilled from verified retries during play. | • Execution outcomes<br>• Failure diagnosis<br>• Verifier results | A frozen reusable code-skill library plus task programs. | LIBERO-Pro, MolmoSpaces, cross-environment robosuite transfer, and zero-shot physical-robot transfer. | [Paper](https://arxiv.org/abs/2606.19419) · [Code](https://github.com/Playful-RATs/RATs) · [Project](https://playful-rats.github.io/) |
| 2026-06 | **[ASPIRE: Agentic Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** — arXiv<br>`Core` `Pick` `Real` | Robot programs, validated repairs, and parameterized skills that persist across tasks. | • Fine-grained multimodal execution traces<br>• Automatic failure diagnosis and revalidation<br>• Evolutionary task and program search | A continually expanding library of verified program skills. | LIBERO-Pro, robosuite, BEHAVIOR-1K, unseen long-horizon tasks, and cross-embodiment real-robot transfer. | [Paper](https://arxiv.org/abs/2607.00272) · [Project](https://research.nvidia.com/labs/gear/aspire/) |
| 2026-03 | **[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435)** — arXiv<br>`Core` `Pick` `Code` `Real` | Robot programs and automatically synthesized skills over perception and control primitives. | • Structured execution feedback<br>• Visual differencing<br>• Multi-turn rollout history | An iteratively repaired policy program and optional skill library. | CaP-Gym with 187 tasks; CaP-Bench across 12 models; simulation, real embodiments, and sim-to-real experiments. | [Paper](https://arxiv.org/abs/2603.22435) · [Code](https://github.com/capgym/cap-x) · [Project](https://capgym.github.io/) |
| 2026-03 | **[Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation](https://arxiv.org/abs/2603.04466)** — arXiv<br>`Core` | An entire low-level Python controller class rewritten between robot episodes. | • RGB-D keyframes<br>• Reward and phase logs<br>• Structured failure diagnostics | A revised low-level controller implementation. | Three robosuite UR5e manipulation tasks with sandboxing, action clamps, and rollback. | [Paper](https://arxiv.org/abs/2603.04466) |
| 2026-01 | **[ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510)** — arXiv<br>`Core` | Executable Code-as-Policy controllers or ReAct-style tool calls under a shared benchmark. | • Environment observations<br>• Tool results<br>• ReAct reasoning traces in the tool-policy setting | An executable control program or online tool-use policy. | Fifty-six manipulation tasks across multiple simulated environments, model families, and language variants. | [Paper](https://arxiv.org/abs/2601.19510) |
| 2026 | **[Telekinesis Physical AI Agents](https://docs.telekinesis.ai/agents/introduction.html)** — Product Documentation<br>`Related` | Readable Python programs that compose existing robot skills and generate new skills when needed. | • Optional robot-view images<br>• Typed skill inputs and outputs<br>• Human code review before execution | A reviewable Python robot program. | Product examples and application demos; no controlled empirical benchmark is documented.<br>**Strictness:** The documentation describes executable, reviewable CaP over a large skill library, but does not provide a controlled robot-learning evaluation. | [Project](https://docs.telekinesis.ai/agents/introduction.html) |
| 2025-10 | **[Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://arxiv.org/abs/2510.21302)** — NeurIPS 2025<br>`Core` `Real` | Task code plus exploratory programs that acquire missing observations. | • Symbolic verification<br>• Interactive environment observations<br>• Execution validation | A symbolically checked, environment-grounded task program. | Dynamic and partially observable RLBench tasks plus real-world experiments. | [Paper](https://arxiv.org/abs/2510.21302) |
| 2025-09 | **[Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills](https://arxiv.org/abs/2509.18597)** — arXiv<br>`Core` `Real` | Long-horizon manipulation code and reusable skills distilled from human corrections. | • Human natural-language corrections<br>• Execution outcomes<br>• Retrieval from an external skill memory | Executable task code plus a persistent reusable skill library. | Ravens, Franka Kitchen, MetaWorld, and real-world long-horizon tasks, including programs spanning more than 20 primitives. | [Paper](https://arxiv.org/abs/2509.18597) |
| 2025-08 | **[HyCodePolicy: Hybrid Language Controllers for Multimodal Monitoring and Decision in Embodied Agents](https://arxiv.org/abs/2508.02629)** — arXiv<br>`Core` | Checkpointed manipulation programs that can be revised after execution failures. | • Program execution traces<br>• Checkpoint images<br>• VLM-generated failure analysis | A repaired executable manipulation program. | RoboTwin 1.0 and Bi2Code comparisons against one-shot CaP and CodeAct-style baselines. | [Paper](https://arxiv.org/abs/2508.02629) |
| 2025-03 | **[GenSwarm: Scalable Multi-Robot Code-Policy Generation and Deployment via Language Models](https://arxiv.org/abs/2503.23875)** — npj Robotics<br>`Core` `Code` `Real` | Python skill libraries, skill graphs, and deployable code policies for multi-robot systems. | • Static code checks<br>• Simulation and video feedback<br>• Optional human feedback | A verified multi-robot code policy and reusable skill graph. | Simulated and physical multi-robot tasks, including altered and unseen instructions, against agent and CaP baselines. | [Paper](https://arxiv.org/abs/2503.23875) · [Code](https://github.com/WindyLab/GenSwarm) |
| 2025-03 | **[Embodied Long Horizon Manipulation with Closed-loop Code Generation and Incremental Few-shot Adaptation](https://arxiv.org/abs/2503.21969)** — arXiv<br>`Core` `Code` `Real` | Executable long-horizon code plans rather than natural-language subtask lists. | • RGB-D outcome reports<br>• Structured plan-execution misalignment feedback<br>• Incrementally added successful examples | A replanned executable manipulation program. | More than 30 seen and unseen tasks across LoHoRavens, CALVIN, Franka Kitchen, and cluttered real settings. | [Paper](https://arxiv.org/abs/2503.21969) · [Code](https://github.com/Ghiara/DAHLIA) · [Project](https://ghiara.github.io/DAHLIA/) |
| 2025-01 | **[Robotic Programmer: Video Instructed Policy Code Generation for Robotic Manipulation](https://arxiv.org/abs/2501.04268)** — arXiv<br>`Core` `Real` | Executable robot policy code that invokes an embodiment-specific skill API. | • Visual observations and free-form instructions<br>• Video2Code-generated training supervision<br>• No test-time repair loop | A policy program for zero-shot manipulation. | Zero-shot manipulation on RLBench and LIBERO plus real-world experiments and API-variation tests. | [Paper](https://arxiv.org/abs/2501.04268) · [Project](https://video2code.github.io/RoboPro-website/) |
| 2024-06 | **[RoboCoder: Robotic Learning from Basic Skills to General Tasks with Large Language Models](https://arxiv.org/abs/2406.03757)** — arXiv<br>`Core` | Action code that composes basic skills for progressively harder simulated tasks. | • Real-time environment observations<br>• Task pass or failure<br>• Dynamic action-code refinement | Refined executable action code. | Eighty manually designed tasks across seven simulated entities, including a humanoid setting. | [Paper](https://arxiv.org/abs/2406.03757) |
| 2024-04 | **[GenCHiP: Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2404.06645)** — IROS 2024<br>`Core` `Real` | Policy code over compliant motion primitives with force, stiffness, and pose constraints. | • Estimated object poses<br>• Force-aware compliant control<br>• No autonomous code-repair loop | Executable policy code for precision and contact-rich manipulation. | Subtasks derived from the Functional Manipulation Benchmark and NIST task boards under perception and grasp noise. | [Paper](https://arxiv.org/abs/2404.06645) · [Project](https://dex-code-gen.github.io/dex-code-gen/) |
| 2024-02 | **[RoboScript: Code Generation for Free-Form Manipulation Tasks across Real and Simulation](https://arxiv.org/abs/2402.14623)** — arXiv<br>`Core` `Real` | Deployable manipulation code against a unified ROS and Gazebo interface. | • Syntax validation<br>• Gazebo simulation validation<br>• Perception and motion-planning outputs | Robot-executable manipulation code. | A free-form manipulation benchmark plus end-to-end evaluations on Franka and UR5 embodiments in simulation and reality. | [Paper](https://arxiv.org/abs/2402.14623) |
| 2024-02 | **[RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis](https://arxiv.org/abs/2402.16117)** — ICML 2024<br>`Core` `Code` `Real` | Tree-structured robot code built from object-centric manipulation units with affordance and safety constraints. | • Multimodal scene inputs<br>• Object affordances and physical constraints<br>• Iterative self-updating during supervised fine-tuning | Executable object-centric robot behavior code. | Four manipulation categories and one navigation task in simulators and on real robots. | [Paper](https://arxiv.org/abs/2402.16117) · [Code](https://github.com/RoboCodeX-source/RoboCodeX_code) |
| 2023-10 | **[How to Prompt Your Robot: A PromptBook for Manipulation Skills with Code as Policies](https://doi.org/10.1109/ICRA57147.2024.10610784)** — ICRA 2024<br>`Core` `Real` | Robot policy code and new low-level manipulation skills under alternative prompt designs. | • State-estimation outputs supplied in the prompt<br>• Prompt examples and instructions<br>• No autonomous post-rollout repair loop | Executable manipulation-skill code. | Prompt-component ablations and new-skill execution on a mobile manipulator. | [Paper](https://doi.org/10.1109/ICRA57147.2024.10610784) |
| 2022-09 | **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)** — ICRA 2023<br>`Core` `Pick` `Code` `Real` | Hierarchical Python policies that compose perception, planning, and control APIs. | • Runtime perception consumed by the generated program<br>• No post-rollout code-repair loop in the original system | An executable Python policy program. | Tabletop manipulation, whiteboard drawing, and mobile manipulation across physical robot platforms. | [Paper](https://arxiv.org/abs/2209.07753) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) · [Project](https://code-as-policies.github.io/) |
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
