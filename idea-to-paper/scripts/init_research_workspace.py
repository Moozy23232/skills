#!/usr/bin/env python3
"""Initialize non-destructive, persistent research state in an existing project."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path


DIRECTORIES = (
    "plans",
    "literature",
    "notes",
    "experiments/protocols",
    "experiments/runs",
    "paper",
    "archive",
)

TEMPLATES = {
    "README.md": """# {{TITLE}} Research Status

Status: `draft`
Last verified: {{DATE}}

## Five-Minute Status

- Current phase and gate:
- Stable research question:
- Strongest positive evidence:
- Strongest negative evidence:
- Current blocker:
- Next smallest action:

## Authoritative Map

- [Overview](overview.md)
- [Decisions and constraints](CONTEXT.md)
- [Live plan](plans/live-plan.md)
- [Literature evidence ledger](literature/evidence-ledger.md)
- [Experiment index](experiments/index.md)
- [Claim-evidence matrix](paper/claim-evidence.md)
- [Observation log](notes/log.md)
- [Archive](archive/)
""",
    "overview.md": """# Research Overview

Status: `draft`
Updated: {{DATE}}

## Research Question

## Motivation and Gap

## Proposed Mechanism

## Falsifiable Hypothesis

## Intended Contribution

## Scope and Non-Goals

## Strongest Baseline or Competing Explanation

## Evaluation Roadmap

## Known Limitations
""",
    "CONTEXT.md": """# Decisions and Constraints

Updated: {{DATE}}

## Fixed Constraints

| Constraint | Value | Source or owner |
|---|---|---|

## Resolved Decisions

| Date | Decision | Rationale and evidence | Supersedes |
|---|---|---|---|

## Open Decisions

| ID | Question | Why it matters | Needed evidence | Owner |
|---|---|---|---|---|
""",
    "plans/live-plan.md": """# Live Research Plan

Status: `active`
Updated: {{DATE}}

## Current Gate

## Exit Criteria

- [ ]

## Dependency-Ordered Actions

1.

## Risks and Fallbacks

## Expected Artifacts

## Next Decision
""",
    "literature/evidence-ledger.md": """# Literature Evidence Ledger

Search coverage last updated: {{DATE}}

| ID | Source | Question and method | Data/evaluation | Finding | Relation to idea | Limitation | Verification |
|---|---|---|---|---|---|---|---|

## Query Coverage

| Date | Query family or citation trail | Source index | New cluster found? | Notes |
|---|---|---|---|---|

## Closest-Collision Summary

| Work | Same problem? | Same mechanism? | Same data/assumptions? | Same evaluation? | Material difference |
|---|---:|---:|---:|---:|---|
""",
    "notes/log.md": """# Append-Only Research Log

Do not rewrite earlier entries. Add corrections as new dated entries.

## {{DATE}}

- Observation:
- Evidence:
- Interpretation:
- Uncertainty:
- Next action:
""",
    "experiments/index.md": """# Experiment Index

Updated: {{DATE}}

| Run ID | Stage | Protocol | Commit | Status | Primary result | Manifest |
|---|---|---|---|---|---|---|

## Stage Gate

- Current stage:
- Exit criterion:
- Decision: `ADVANCE | REPEAT | REVISE | STOP`
- Evidence:
""",
    "paper/claim-evidence.md": """# Claim-Evidence Matrix

Updated: {{DATE}}

| Claim ID | Exact claim | Scope/assumptions | Protocol and runs | Figure/table | Counterevidence | Status |
|---|---|---|---|---|---|---|

Allowed statuses: `supported`, `qualified`, `missing`, `contradicted`, `out-of-scope`.

## Venue Contract

- Venue:
- Submission date:
- Page and appendix limits:
- Audience:
- Core one-sentence claim:
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create missing research-state files without overwriting existing content."
        )
    )
    parser.add_argument(
        "project_root",
        help="Explicit path to the existing project root",
    )
    parser.add_argument(
        "--state-dir",
        default="docs/research",
        help="Relative state directory inside the project (default: docs/research)",
    )
    parser.add_argument(
        "--title",
        help="Human-readable project title (default: project directory name)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show intended changes without writing files",
    )
    return parser.parse_args()


def resolve_target(project_root: str, state_dir: str) -> tuple[Path, Path]:
    root = Path(project_root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"project root is not an existing directory: {root}")

    relative = Path(state_dir)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("--state-dir must be a safe relative path without '..'")

    target = (root / relative).resolve()
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError("state directory resolves outside the project root") from exc
    return root, target


def require_path_in_project(root: Path, path: Path) -> None:
    """Reject managed paths whose existing symlinks resolve outside the project."""
    try:
        path.resolve(strict=False).relative_to(root)
    except ValueError as exc:
        raise ValueError(f"managed path resolves outside the project root: {path}") from exc


def render(template: str, title: str, today: str) -> str:
    return template.replace("{{TITLE}}", title).replace("{{DATE}}", today)


def main() -> int:
    args = parse_args()
    try:
        root, target = resolve_target(args.project_root, args.state_dir)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    title = args.title.strip() if args.title and args.title.strip() else root.name
    today = date.today().isoformat()

    ancestor = target
    while ancestor != root:
        ancestor = ancestor.parent
        if ancestor == root:
            break
        if ancestor.exists() and not ancestor.is_dir():
            print(
                f"ERROR: state path parent exists but is not a directory: {ancestor}",
                file=sys.stderr,
            )
            return 2

    required_directories = (target, *(target / item for item in DIRECTORIES))
    destinations = tuple(target / relative for relative in TEMPLATES)
    try:
        for path in (*required_directories, *destinations):
            require_path_in_project(root, path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    for directory in required_directories:
        if directory.exists() and not directory.is_dir():
            print(
                f"ERROR: required directory path exists but is not a directory: "
                f"{directory}",
                file=sys.stderr,
            )
            return 2

    for destination in destinations:
        if destination.exists() and destination.is_dir():
            print(
                f"ERROR: required file path exists as a directory: {destination}",
                file=sys.stderr,
            )
            return 2

    planned = [target / directory for directory in DIRECTORIES]
    planned.extend(destinations)

    if args.dry_run:
        print(f"Research state root: {target}")
        for path in planned:
            status = "SKIP existing" if path.exists() else "CREATE"
            print(f"{status}: {path}")
        return 0

    created_dirs = 0
    for directory in required_directories:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

    created_files = 0
    skipped_files = 0
    for relative, template in TEMPLATES.items():
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open("x", encoding="utf-8") as output:
                output.write(render(template, title, today))
        except FileExistsError:
            if destination.is_dir():
                print(
                    f"ERROR: required file path exists as a directory: {destination}",
                    file=sys.stderr,
                )
                return 2
            print(f"SKIP existing: {destination}")
            skipped_files += 1
            continue
        print(f"CREATE: {destination}")
        created_files += 1

    print(
        f"Done: {created_files} file(s) and {created_dirs} directories created; "
        f"{skipped_files} existing file(s) preserved."
    )
    state_readme = (target / "README.md").relative_to(root)
    print(f"Next: inspect {state_readme} and link it from the project README.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
