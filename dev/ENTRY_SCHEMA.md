# Entry schema

The machine-readable schema is `data/paper.schema.json`. This note explains the research meaning of each field.

| Field | Required | Meaning |
|---|---:|---|
| `id` | yes | Stable kebab-case identifier; used to deduplicate cross-topic works |
| `title` | yes | Official work or system title |
| `date` | yes | `YYYY` or `YYYY-MM`, preferably first public paper date |
| `venue` | no | Verified venue; use `arXiv` only when helpful |
| `organization` | no | Verified affiliation or organization, not inferred from a username |
| `topics` | yes | One or more topic IDs for independently supported claims |
| `classification` | yes | `core` or `related` |
| `strictness_note` | for related | Exact core criterion that is unclear or missing |
| `agent_writes` | yes | Concrete code or executable artifact generated/changed by the agent |
| `feedback` | yes | Signals returned to the agent after execution or training |
| `final_artifact` | yes | What remains after the system finishes |
| `evaluation` | yes | Compact evidence: setup, scale, baselines, and useful headline result |
| `summary` | yes | One-sentence contribution summary in the curator's own words |
| `curator_pick` | no | Sparse “start here” designation after a topic audit |
| `open_source` | no | True only with an official code link |
| `real_robot` | no | True only with physical-robot evaluation |
| `links` | yes | Official paper/code/project/data/video URLs |

## Topic IDs

- `code-as-policy`
- `simulation-task-generation`
- `reward-design`
- `robot-evaluation`
- `synthetic-data`
- `agentic-policy-training`

## Evidence checklist

Before marking an entry Core, record:

- the exact generated or modified artifact;
- at least one execution or learning feedback signal;
- where the artifact is executed;
- the downstream final artifact;
- simulation and/or real-robot evidence;
- human intervention that materially limits claims of autonomy;
- any ambiguity between marketing language and the evaluated system.

## Example

```json
{
  "id": "example-work",
  "title": "Example Work",
  "date": "2026-08",
  "venue": "arXiv",
  "topics": ["simulation-task-generation", "synthetic-data"],
  "classification": "core",
  "agent_writes": "Executable simulator task code and success predicates",
  "feedback": ["Simulator exceptions", "Policy success rate"],
  "final_artifact": "Generated tasks and successful trajectories",
  "evaluation": "Reports task validity and trains a separate policy on generated data.",
  "summary": "Generates executable tasks and tests their value through downstream learning.",
  "curator_pick": false,
  "open_source": true,
  "real_robot": false,
  "links": {
    "paper": "https://example.org/paper",
    "code": "https://github.com/example/repository"
  }
}
```
