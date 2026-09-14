# Contributing

Thank you for helping improve **Awesome Coding Agents for Robot Learning**. Contributions may add a work, correct an existing record, supply missing resources, or challenge a classification.

## Before adding a work

Use these editorial questions to check fit. They are review principles, not a point system or paper-quality score.

1. **Agentic role** — What does the LLM-based agent generate, modify, operate, or adapt?
2. **Executable layer** — Through what code, structured artifact, tool, skill, policy, or stateful harness does it act?
3. **Embodied connection** — How is that layer used in robot learning, evaluation, deployment, or physical execution?
4. **Topic fit** — What is the work's main research object, and which topic best matches it?

A work normally enters through executable artifact authoring, robot operation, or both. The work should substantively study or develop the agent's role in robot learning or robot operation. A language-only plan, ordinary middleware, or a fixed automated pipeline is not sufficient by itself.

## Adding or updating an entry

1. Edit the appropriate table in `README.md` directly.
2. Prefer authoritative primary sources: the official paper when one exists, the canonical code repository, and the official project page.
3. Follow the existing `Date / Org / Links / Stars / Title or Notes` row format. Use only the first listed affiliation in `Org` without `et al.`.
4. Label the primary source accurately: `[Paper]`, `[Post]`, or `[Docs]`. Keep official implementation and project links as `[Code]` and `[Website]`.
5. Keep the note to one compact, factual sentence that states what the system contributes and where it was evaluated, executed, or released. Do not copy the abstract or add unsupported comparative judgments.
6. Place a work first in the topic that matches its main research object. Add another topic only when the source explicitly frames and independently evaluates a distinct topic-specific claim—not merely because the component exists somewhere in the system.
7. Update the affected topic count, summary badges, and `Last updated` date.
8. Preview the rendered Markdown and verify every new link before opening a pull request.

## Curation guidelines

- Keep **topic fit**, **evidence type**, **evidence rigor**, and **source genre** separate. A product research post may be highly topical without offering the protocol disclosure of a paper; describe that difference rather than treating it as a different topic.
- When a source reports empirical results without a fully disclosed benchmark, use careful verbs such as *reports* and state the setting that is actually documented.
- Use 🤖 only when a physical robot is part of the reported evaluation.
- Add `[Code]` and a GitHub stars badge only for an official public implementation. The code link already communicates open-source availability; no separate row icon is needed.

## Quality standard

Whenever possible, verify the date, organization, links, contribution, evaluation setting, and physical-robot claim against primary sources such as the paper, official repository, project documentation, and released evaluation artifacts. If a claim cannot be verified, omit it or state the uncertainty explicitly.

Promotional submissions, duplicate project pages, generic agentic-robotics systems without the coding-agent executable layer, and entries without a substantive robot-learning or robot-operation contribution may be declined.
