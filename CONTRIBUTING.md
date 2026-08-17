# Contributing

Thank you for helping improve **Awesome Coding Agents for Robot Learning**. Contributions may add a work, correct an existing record, supply missing resources, or challenge a classification.

## Before adding a work

Check that the contribution can answer the four core criteria from the README:

1. **C1 Generation** — What executable artifact does the LLM or coding agent generate, edit, select, or debug?
2. **C2 Placement** — Where does that artifact sit in the robot-learning system?
3. **C3 Execution** — Is the generated artifact executed, simulated, trained, or deployed?
4. **C4 Evidence** — What empirical robot-learning evidence is reported?

Works that are highly relevant but fail one criterion can be marked `Related`, with the missing criterion explained in that section's **Scope notes**, for example: *"fails C4: product post without a controlled benchmark."*

## Adding or updating an entry

1. Edit the appropriate table in `README.md` directly.
2. Prefer authoritative primary sources: the official paper when one exists, the canonical code repository, and the official project page.
3. Follow the existing `Date / Org / Links / Stars / Title or Notes` row format.
4. Keep the note to one compact, factual sentence. Do not copy the abstract or add unsupported comparative judgments.
5. Add a work to multiple topic tables only when each placement has an independently evaluated claim.
6. Update the affected topic count, summary badges, and `Last updated` date.
7. Preview the rendered Markdown and verify every new link before opening a pull request.

## Classification guidelines

- Use multiple topic placements when the work makes a substantive, evaluated claim in each topic—not merely because components coexist in the system.
- Use Core only when executable code or a comparably structured executable artifact is generated or modified by an LLM/coding agent and evaluated in a robot-learning setting.
- Use `Related` for important neighboring systems and explain the exact missing criterion in the section's Scope notes.
- Show E0–E4 markers in order and include only evidence verified from an official source. Core entries require E0.
- Use 🤖 only when a physical robot is part of the reported evaluation.
- Use 💻 and a GitHub stars badge only when an official public code implementation is linked.

## Quality standard

Whenever possible, verify the date, organization, links, and note against primary sources such as the paper PDF, official repository, project documentation, and released evaluation artifacts. If a claim cannot be verified, omit it or state the uncertainty explicitly.

Promotional submissions, duplicate project pages, and entries without a clear connection to the scope may be declined.
