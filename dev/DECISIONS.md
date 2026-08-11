# Decisions

This file records durable project decisions. New entries should state the date, decision, and reason.

## 2026-08-11 — One long README

**Decision:** Keep the complete public taxonomy, paper list, annotations, and navigation in one long `README.md`.

**Reason:** This matches established awesome-list browsing conventions and keeps the collection searchable and skimmable from the repository landing page.

## 2026-08-11 — Use `dev/` for shared internal context

**Decision:** Store cross-window project context in `dev/`, not `internal/`.

**Reason:** The directory is a temporary development workspace rather than a permanent hidden subsystem. It can be cleaned or selectively retained before launch.

## 2026-08-11 — Derive topics from actual research clusters

**Decision:** Topic boundaries follow recurring research questions, controlled variables, baselines, and evaluation protocols in the literature. They need not form a mutually exclusive system decomposition.

**Reason:** The collection should represent what researchers actually study, even when system papers span several topics.

## 2026-08-11 — Preserve Code as Policy as an independent topic

**Decision:** CaP is a full section rather than a subcase of agentic training.

**Reason:** In CaP, generated code is the deployed policy; in agentic policy training, generated code usually changes the outer research loop and leaves behind a learned policy.

## 2026-08-11 — Separate reward design and evaluation when research questions justify it

**Decision:** Reward design and robot evaluation each receive a section, while generic “training infrastructure” does not.

**Reason:** Reward design and evaluation have recognizable independent objectives and protocols. Environment/task generation already tends to bundle reward, reset, and termination, making a broad infrastructure split redundant.

## 2026-08-11 — Data-driven generated regions

**Decision:** Use `data/papers.json` as the source of truth and generate paper tables, Curator's Picks, statistics, badges, and update date in README.

**Reason:** This preserves a single long public README while preventing duplicated records and stale counts across overlapping topics.

## 2026-08-11 — Start verified counts at zero

**Decision:** Do not seed unverified records merely to make the initial page look populated.

**Reason:** The project values traceable, topic-level source audits. Existing discussion notes are leads, not automatically verified entries.
