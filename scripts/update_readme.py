#!/usr/bin/env python3
"""Validate paper metadata and regenerate machine-maintained README regions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA = ROOT / "data" / "papers.json"

TOPICS = {
    "code-as-policy": ("Code as Policy", "3867D6"),
    "simulation-task-generation": ("Simulation and Task Generation", "20BF6B"),
    "reward-design": ("Automated Reward Design", "F7B731"),
    "robot-evaluation": ("Automated Robot Evaluation", "EB3B5A"),
    "synthetic-data": ("Synthetic Data Generation for Policy Learning", "8854D0"),
    "agentic-policy-training": ("Agentic Policy Training and Robot Autoresearch", "0FB9B1"),
}

BADGE_LABELS = {
    "code-as-policy": "Code_as_Policy",
    "simulation-task-generation": "Simulation_%26_Tasks",
    "reward-design": "Reward_Design",
    "robot-evaluation": "Robot_Evaluation",
    "synthetic-data": "Synthetic_Data",
    "agentic-policy-training": "Agentic_Training",
}

REQUIRED = {
    "id",
    "title",
    "date",
    "topics",
    "classification",
    "agent_writes",
    "feedback",
    "final_artifact",
    "evaluation",
    "summary",
    "links",
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_and_validate() -> list[dict[str, Any]]:
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        fail("data/papers.json must contain a JSON array")

    seen: set[str] = set()
    for index, entry in enumerate(raw):
        label = f"entry #{index + 1}"
        if not isinstance(entry, dict):
            fail(f"{label} must be an object")
        missing = REQUIRED - entry.keys()
        if missing:
            fail(f"{label} is missing: {', '.join(sorted(missing))}")

        work_id = entry["id"]
        if not isinstance(work_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", work_id):
            fail(f"{label} has an invalid id: {work_id!r}")
        if work_id in seen:
            fail(f"duplicate id: {work_id}")
        seen.add(work_id)

        if entry["classification"] not in {"core", "related"}:
            fail(f"{work_id}: classification must be core or related")
        topics = entry["topics"]
        if not isinstance(topics, list) or not topics:
            fail(f"{work_id}: topics must be a non-empty list")
        unknown = set(topics) - TOPICS.keys()
        if unknown:
            fail(f"{work_id}: unknown topics: {', '.join(sorted(unknown))}")
        if len(topics) != len(set(topics)):
            fail(f"{work_id}: topics contains duplicates")
        if not re.fullmatch(r"\d{4}(-\d{2})?", str(entry["date"])):
            fail(f"{work_id}: date must be YYYY or YYYY-MM")
        if entry["classification"] == "related" and not entry.get("strictness_note"):
            fail(f"{work_id}: related entries require strictness_note")
        if not isinstance(entry["feedback"], list):
            fail(f"{work_id}: feedback must be a list")
        if not isinstance(entry["links"], dict) or not entry["links"]:
            fail(f"{work_id}: links must be a non-empty object")
        if entry.get("open_source") and not entry["links"].get("code"):
            fail(f"{work_id}: open_source=true requires links.code")

    return raw


def replace_region(text: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"(<!-- {re.escape(name)}:start -->).*?(<!-- {re.escape(name)}:end -->)",
        re.DOTALL,
    )
    replacement = rf"\1\n{content.rstrip()}\n\2"
    updated, count = pattern.subn(replacement, text)
    if count != 1:
        fail(f"expected exactly one README region named {name!r}, found {count}")
    return updated


def badge(label: str, value: int, color: str, alt: str | None = None) -> str:
    alt_text = alt or label.replace("_", " ").replace("%26", "&")
    return f"![{alt_text}](https://img.shields.io/badge/{label}-{value}-{color}?style=flat-square)"


def render_badges(entries: list[dict[str, Any]]) -> str:
    core = [entry for entry in entries if entry["classification"] == "core"]
    related = [entry for entry in entries if entry["classification"] == "related"]
    topic_counts = Counter(topic for entry in core for topic in entry["topics"])
    lines = [
        "[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)",
        badge("Papers", len(core), "2F80ED"),
        badge("Topics", len(TOPICS), "6C5CE7"),
        badge("Open_source", sum(bool(entry.get("open_source")) for entry in core), "00A86B"),
        badge("Real_robot", sum(bool(entry.get("real_robot")) for entry in core), "E17055"),
        badge("Related_systems", len(related), "7F8C8D"),
        "<br>",
    ]
    lines.extend(
        badge(BADGE_LABELS[key], topic_counts[key], color, title)
        for key, (title, color) in TOPICS.items()
    )
    return "\n".join(lines)


def render_stats(entries: list[dict[str, Any]]) -> str:
    lines = ["| Topic | Core | Related | Total |", "|---|---:|---:|---:|"]
    for key, (title, _) in TOPICS.items():
        core = sum(entry["classification"] == "core" and key in entry["topics"] for entry in entries)
        related = sum(entry["classification"] == "related" and key in entry["topics"] for entry in entries)
        lines.append(f"| {title} | {core} | {related} | {core + related} |")
    unique_core = sum(entry["classification"] == "core" for entry in entries)
    unique_related = sum(entry["classification"] == "related" for entry in entries)
    lines.append(f"| **Unique works** | **{unique_core}** | **{unique_related}** | **{len(entries)}** |")
    return "\n".join(lines)


def escape_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def resource_links(entry: dict[str, Any]) -> str:
    labels = {"paper": "Paper", "code": "Code", "project": "Project", "dataset": "Data", "video": "Video"}
    return " · ".join(f"[{labels[key]}]({url})" for key, url in entry["links"].items() if key in labels)


def work_cell(entry: dict[str, Any]) -> str:
    primary = entry["links"].get("paper") or entry["links"].get("project") or next(iter(entry["links"].values()))
    labels = ["Core" if entry["classification"] == "core" else "Related"]
    if entry.get("curator_pick"):
        labels.append("Pick")
    if entry.get("open_source"):
        labels.append("Code")
    if entry.get("real_robot"):
        labels.append("Real")
    suffix = " ".join(f"`{label}`" for label in labels)
    venue = f" — {escape_cell(entry['venue'])}" if entry.get("venue") else ""
    return f"**[{escape_cell(entry['title'])}]({primary})**{venue}<br>{suffix}"


def render_topic(entries: list[dict[str, Any]], topic: str) -> str:
    selected = [entry for entry in entries if topic in entry["topics"]]
    selected.sort(key=lambda entry: (entry["date"], entry["title"].lower()), reverse=True)
    if not selected:
        return "_No entries curated yet._"

    lines = [
        "| Date | Work | Agent writes / changes | Feedback loop | Final artifact | Evaluation | Resources |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in selected:
        feedback = "<br>".join(f"• {escape_cell(item)}" for item in entry["feedback"]) or "—"
        evaluation = escape_cell(entry["evaluation"])
        if entry["classification"] == "related":
            evaluation += f"<br>**Strictness:** {escape_cell(entry['strictness_note'])}"
        lines.append(
            "| {date} | {work} | {writes} | {feedback} | {artifact} | {evaluation} | {resources} |".format(
                date=escape_cell(entry["date"]),
                work=work_cell(entry),
                writes=escape_cell(entry["agent_writes"]),
                feedback=feedback,
                artifact=escape_cell(entry["final_artifact"]),
                evaluation=evaluation,
                resources=resource_links(entry),
            )
        )
    return "\n".join(lines)


def render_picks(entries: list[dict[str, Any]]) -> str:
    picks = [entry for entry in entries if entry.get("curator_pick")]
    picks.sort(key=lambda entry: (entry["date"], entry["title"].lower()), reverse=True)
    if not picks:
        return "_Curator's Picks will be added after the first topic-level audit._"
    lines = []
    for entry in picks:
        primary = entry["links"].get("paper") or entry["links"].get("project") or next(iter(entry["links"].values()))
        topic_names = ", ".join(TOPICS[key][0] for key in entry["topics"])
        lines.append(f"- **[{entry['title']}]({primary})** — {entry['summary']} _{topic_names}._")
    return "\n".join(lines)


def generate(readme: str, entries: list[dict[str, Any]]) -> str:
    readme = replace_region(readme, "stats-badges", render_badges(entries))
    readme = replace_region(readme, "stats-table", render_stats(entries))
    readme = replace_region(readme, "curator-picks", render_picks(entries))
    for topic in TOPICS:
        readme = replace_region(readme, f"topic:{topic}", render_topic(entries, topic))
    readme = replace_region(readme, "last-updated", date.today().isoformat())
    return readme


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README is not up to date")
    args = parser.parse_args()

    try:
        entries = load_and_validate()
        original = README.read_text(encoding="utf-8")
        updated = generate(original, entries)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if updated != original:
            print("README.md is stale; run: python scripts/update_readme.py", file=sys.stderr)
            return 1
        print(f"README.md is up to date ({len(entries)} unique works).")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"Updated README.md from {len(entries)} unique works.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
