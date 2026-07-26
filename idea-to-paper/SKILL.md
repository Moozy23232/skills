---
name: idea-to-paper
description: Turn an empirical research question or tentative idea into an evidence-backed paper through literature discovery, novelty and feasibility checks, adversarial clarification, persistent project state, staged experiments, claim-evidence mapping, drafting, and review. Use when the user asks to discover or validate a research idea, convert a vague hypothesis into an executable plan, initialize or resume a long-running research repository, design smoke/pilot/formal experiments, decide go/no-go, or write and improve a paper from research artifacts. Do not use for generic essay editing, an isolated paper summary, or ordinary coding that is not part of a research lifecycle.
---

# Idea to Paper

## Objective

Move a research project from uncertainty to defensible evidence without pretending that later stages are complete. Resume at the earliest unsupported gate, keep claims traceable to sources or experiments, and preserve enough state for a new session to continue reliably.

## Keep Work Inside the Research Scope

- Treat the explicitly selected research project and user-provided artifacts as the only writable scope.
- Treat installed skills, runtime configuration, shell profiles, global environments, sibling repositories, and unrelated project files as external read-only state.
- Keep generated downloads, caches, logs, and outputs inside the selected project or an explicitly approved temporary location.
- Never update, patch, rename, delete, repair, reinstall, or overwrite an existing skill or dependency.
- Use a companion skill only when the user explicitly invokes it or the runtime permits a user-approved handoff. Respect its invocation policy; never bypass its entry point to reach internal skills.
- Treat an explicit “yes” to a narrowly scoped companion-install prompt as authorization only to install the named missing components from their official source through the approved skill installer. Make no other external change.

## Route the Request

Inspect the user's materials and repository before choosing a phase. Start at the narrowest phase that matches the evidence already present.

| Current state | Start here | Required result |
|---|---|---|
| Broad area, no concrete question | Idea discovery | Candidate ideas grounded in a literature map |
| Candidate idea, novelty uncertain | Collision and feasibility review | `GO`, `PIVOT`, `HOLD`, or `NO-GO` recommendation |
| Plausible idea, execution unclear | Adversarial specification | Falsifiable research spec and staged plan |
| Existing project across sessions | Project-state recovery | Verified status, active gate, and next action |
| Implementation exists, evidence weak | Experiment ladder | Smoke, pilot, then frozen-protocol formal evidence |
| Stable results and target venue | Paper construction | Claim-evidence matrix, draft, and review backlog |
| Draft exists, contribution feels thin | Theory and reviewer pass | Stronger valid framing without invented claims |

Do not repeat completed work merely to follow the phase order. If artifacts conflict, treat the conflict as the current task.

## Establish the Evidence Base

Before making a research recommendation:

1. Inspect local papers, notes, code, data, configs, run outputs, and Git state.
2. Distinguish `reported fact`, `local observation`, `inference`, and `proposal`.
3. Use current scholarly search when novelty, related work, datasets, benchmarks, or venue rules may have changed. Prefer original papers, official repositories, and official benchmark or venue pages.
4. Read full text for the closest collisions when available; do not infer novelty from titles, abstracts, or absence in one search engine.
5. Cite external sources and link local claims to concrete files or artifacts.
6. When the current phase materially benefits from a companion skill, check only whether the runtime reports it as installed or callable. If the runtime inventory is inconclusive, check only whether its exact standard install destination exists; do not open it. This is an availability check: do not validate, fingerprint, hash, or inspect file contents.

Read [references/literature-protocol.md](references/literature-protocol.md) for idea discovery, survey, novelty, or feasibility work.

## Phase 1: Discover and Test the Idea

Build a vocabulary map before searching: problem, mechanism, task, data, evaluation, failure mode, synonyms, and adjacent fields. Search broadly for clusters, then deeply inspect the nearest work.

For each candidate idea, write an idea brief containing:

- problem and affected setting;
- gap supported by evidence;
- proposed mechanism;
- expected observable signal;
- strongest baseline or competing explanation;
- smallest experiment that could falsify it;
- likely contribution and explicit non-goals;
- required data, compute, access, and expertise.

Construct a collision matrix against the nearest work. Classify differences as problem, assumptions, mechanism, data, evaluation, or evidence strength. Do not count cosmetic implementation changes as novelty.

End with one recommendation:

- `GO`: enough novelty and feasibility evidence to specify experiments;
- `PIVOT`: valuable core, but the claim or mechanism must change;
- `HOLD`: a named evidence, access, or resource gap blocks a sound decision;
- `NO-GO`: prior work, invalid assumptions, or infeasibility defeats the core claim.

State confidence and unresolved search gaps. Ask the user before a `PIVOT` or `NO-GO` decision changes the research direction.

## Phase 2: Convert the Idea into an Executable Spec

The protocol below is complete on its own. When material ambiguities make a deeper interview useful:

1. Check whether the current runtime reports `grill-me` as installed or callable. If that inventory is inconclusive, check only whether the exact standard `grill-me` install destination exists; do not open its files.
2. If callable or installed, use the original `grill-me` entry point with the bounded handoff below. If it is installed but not exposed for model invocation, give the user the ready-to-run explicit invocation instead of offering to reinstall it. Do not copy its workflow or depend directly on its internal skills.
3. If absent, say that Grill is optional and the built-in questions can continue, then ask once whether to install the official original.
4. If the user declines, continue locally and do not ask again during the current phase.
5. If the user agrees, hand installation to the approved `skill-installer`. Check only exact destination existence and install only absent components from `mattpocock/skills`: `skills/productivity/grill-me` and its required `skills/productivity/grilling` component. Abort on any occupied destination, preserve every downloaded file unchanged, and do not validate or repair either skill.
6. Tell the user when the runtime will expose the new skill, normally on the next turn. Continue with the built-in questions now unless the user prefers to resume after refresh.

Give `grill-me` only the current proposal, fixed constraints, resolved decisions, open decisions, and exit criteria. Instruct it to ask one question at a time and only clarify decisions—do not edit files, install anything, implement, run experiments, evaluate evidence, or advance the research phase. After the interview, verify its compact decision handoff against project evidence and persist accepted decisions in this project's canonical research context.

When the runtime requires direct user invocation, provide a ready-to-run handoff instead of bypassing that policy:

```text
Use $grill-me only to resolve these open research decisions: <open decisions>.
Treat <verified evidence> and <fixed constraints> as fixed context. Ask one
question at a time. Do not edit files, install, implement, run experiments,
review evidence, or advance the research phase. Return confirmed decisions,
assumptions, rejected options, and unresolved blockers to $idea-to-paper.
```

Interrogate one material ambiguity at a time:

- What exact construct or phenomenon is being studied?
- What causal or predictive mechanism is claimed?
- What observation would falsify it?
- Which baseline, confound, or simpler explanation is strongest?
- What data unit, split, metric, evaluator, and statistical test answer the question?
- What resource, ethics, privacy, licensing, or access constraint can invalidate the plan?

Persist user decisions instead of asking them again. After three to five clarification rounds, summarize remaining unknowns. Continue with explicit, reversible assumptions when safe; stop for a decision that materially changes the claim, cost, or risk.

Produce a research spec with:

1. research question and falsifiable hypothesis;
2. independent variables, outcomes, controls, and confounds;
3. baselines, datasets, metrics, and go/no-go thresholds;
4. dependency-ordered spike, smoke, pilot, and formal experiments;
5. compute/time budget, risks, fallbacks, and stop conditions;
6. artifacts expected from every stage.

Do not enter the pilot stage until the predicted observation and the interpretation of failure are both explicit.

## Phase 3: Persist and Resume the Project

For work spanning sessions, read [references/research-state-protocol.md](references/research-state-protocol.md). Reuse an equivalent project structure if one already exists; do not create a parallel documentation system.

If persistent state is requested and no equivalent exists, run:

```bash
python3 "<skill-directory>/scripts/init_research_workspace.py" <project-root> --title "<project title>" --dry-run
python3 "<skill-directory>/scripts/init_research_workspace.py" <project-root> --title "<project title>"
```

Resolve `<skill-directory>` from the location of this `SKILL.md`; do not assume the target repository contains the script. Pass an explicit `<project-root>`, inspect the dry-run, and write only when the resolved target is the selected research project. The script rejects paths that escape that root and creates files exclusively, so existing content is never overwritten. Review its output, then link the research status from the root README only when that README belongs to the selected project.

At every resumed session:

1. Read the authoritative map, overview, decisions, live plan, experiment index, and recent run manifests.
2. Inspect recent commits and actual artifacts rather than trusting status prose alone.
3. Report the stable question, active gate, strongest evidence, blockers, and next decision.
4. Reconcile contradictions before implementation or experimentation.
5. Update only the document that owns each fact; archive superseded plans and keep raw run records append-only.

## Phase 4: Run an Experiment Ladder

Read [references/experiment-protocol.md](references/experiment-protocol.md) before designing or executing experiments.

Advance in dependency order:

1. `spike`: prove the riskiest component can work;
2. `smoke`: prove the complete pipeline runs and artifacts are readable;
3. `pilot`: test whether the hypothesized signal plausibly exists;
4. `formal`: test paper claims under a frozen protocol;
5. `ablation/robustness`: locate the mechanism and its limits.

Freeze data splits, model and dependency versions, baselines, metrics, training budget, checkpoint selection, evaluator, seeds, and stop rules before formal comparisons. Apply the same protocol to comparable methods. Record deviations as new protocol versions rather than silently editing history.

If a formal protocol still contains material unresolved decisions, optionally hand only those decisions to an explicitly accepted `grill-me` session under the same no-write, no-implementation limits. Otherwise use the built-in question loop. Do not re-grill settled fields or use Grill to reinterpret observed results.

For every run, record commit, environment, configuration, inputs, outputs, logs, artifact paths, result, and interpretation boundary. Preserve failed runs and negative results. Request confirmation before a materially expensive run and include a cost/time estimate.

Do not promote a single successful run into a paper claim. Use replication, uncertainty, and statistical analysis appropriate to the field.

For theory-first work, replace experiment gates with explicit definition, lemma, proof, counterexample, and independent-verification gates; do not force an empirical ladder onto the project.

## Phase 5: Build the Paper from Claims and Evidence

Read [references/paper-protocol.md](references/paper-protocol.md) before drafting or reviewing a paper.

1. Freeze the target venue, format, page limit, audience, and intended core claim.
2. Build the claim-evidence matrix before polishing prose.
3. Draft methods and results from frozen protocols and actual artifacts.
4. Draft limitations, introduction, related work, conclusion, title, and abstract after the argument is stable.
5. Mark unsupported claims and missing evidence explicitly; do not fill gaps with plausible prose.
6. Bind tables and plots to reproducible scripts and raw artifacts. Prefer editable conceptual diagrams when practical.
7. Run separate consistency, citation, statistical, presentation, and adversarial-review passes.

Triage feedback as:

- `P0`: invalid claim, missing decisive evidence, leakage, unfair comparison, or irreproducibility;
- `P1`: incomplete method, analysis, baseline, limitation, or claim-to-result link;
- `P2`: clarity, organization, notation, figure, style, or formatting issue.

Repair higher priorities first. After three full author-review cycles, summarize persistent disagreements and ask the user to decide rather than looping indefinitely.

## Phase 6: Strengthen Theory Without Manufacturing It

Add theory only when it clarifies an observed method or result. State assumptions, definitions, proof obligations, applicability bounds, and empirical consequences. Label conjectures and heuristic interpretations honestly.

Require every equation, theorem, bound, or formal claim to be derivable from the method or explicitly introduced assumptions. Check edge cases and counterexamples. Remove formalism that is decorative, unverified, or contradicted by experiments.

Use separate author and reviewer perspectives. A reviewer must try to break the claim, not merely rewrite it.

## Output Contract

For any substantial response, report:

1. current phase and gate;
2. evidence inspected and its limitations;
3. decision or recommendation;
4. artifacts created or updated;
5. exact next gate and what would pass it.

Never describe a search as exhaustive, an idea as novel, an experiment as conclusive, or a paper as submission-ready without stating the supporting scope and remaining uncertainty.
