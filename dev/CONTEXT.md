# Project context

## Objective

Maintain a useful, evidence-oriented awesome list for **Coding Agents for Robot Learning**. The main artifact is one long, unified `README.md`, consistent with the normal awesome-list browsing experience.

The repository is currently private and in development. It will be cleaned before public release.

## Stable framing

The unifying question is:

> What executable code or structured artifact does the coding agent generate or change, where does it sit in the robot-learning system, and what evidence is produced when it runs?

The project should not overclaim that the field already forms one unified end-to-end autonomous robot-learning loop. The umbrella title organizes the collection; each section should remain a concrete research topic observed in existing work.

## Working topic map

1. **Code as Policy** — generated code is itself the robot policy.
2. **Simulation and Task Generation** — generated code defines an executable world, task, or curriculum.
3. **Automated Reward Design** — generated reward code is optimized while the task/simulator is largely fixed.
4. **Automated Robot Evaluation** — generated or agentic evaluation measures success, progress, failure, or safety.
5. **Synthetic Data Generation for Policy Learning** — generated tasks and rollouts are evaluated through downstream policy learning.
6. **Agentic Policy Training / Robot Autoresearch** — a coding agent runs and modifies the outer training/research loop.

These topics are not required to be mutually exclusive. The map should follow actual research clusters, baselines, and benchmarks rather than a conceptually perfect software architecture.

## Important boundaries

- **Code as Policy remains a large independent section.** It is not merely a subset of automated policy training.
- A generated simulation task normally includes reward, success, termination, and reset. We do not create a generic “training infrastructure” topic just to separate those components.
- Reward design remains separate because there is a recognizable literature that fixes tasks/simulators and evaluates reward-generation quality through downstream RL.
- Robot evaluation deserves a dedicated topic because measurement reliability, failure diagnosis, reset, and unattended testing have distinct goals and protocols.
- Systems with unclear or absent coding-agent behavior may be useful Related systems, but should not silently inflate the core list.

## Language and presentation

- Public-facing content: English.
- Development notes: English or Chinese, whichever preserves the research reasoning most clearly.
- README style: long-form awesome list with banner, badges, scope, taxonomy, annotated paper tables, updates, contribution instructions, and citation.

## Existing source material

- Prior Code as Policy research exists in Feishu: https://my.feishu.cn/wiki/C4lowqZnhiD7qSkqe6ycvNhined
- It was not directly readable during repository bootstrap. Import it only after the user provides an accessible export or attachment; preserve its existing structure before normalizing entries.
- Inspiration repository: https://github.com/thinkwee/AwesomeOPD
