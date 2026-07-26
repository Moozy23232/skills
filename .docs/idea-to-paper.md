# Idea to Paper

[简体中文](idea-to-paper_zh.md)

`idea-to-paper` helps you turn a research direction, tentative idea, or existing project into a paper whose claims are traceable to literature and experiments.

It is not a one-click paper generator. Think of it as a research partner that helps you decide what is worth testing, what the evidence actually supports, and what to do next.

## What It Can Help With

You can use it when:

- you have a broad topic but not yet a research question;
- you have an idea and want to know whether nearby work already covers it;
- you need to turn a hypothesis into a concrete, falsifiable experiment plan;
- you want to resume a research repository after days or weeks away;
- you have results and need to decide whether to continue, pivot, or stop;
- you want to draft or review a paper without losing the link between claims and evidence.

You do not need to start from the beginning. Give it whatever already exists: a sentence, papers, notes, code, a repository, experiment logs, figures, a draft, or some combination of them.

## Try These Prompts

Starting from a broad direction:

```text
Use $idea-to-paper. I am interested in reducing KV-cache memory for
long-context inference. Help me map the nearby research and identify a few
questions that could be tested with two GPUs.
```

Stress-testing an idea:

```text
Use $idea-to-paper to examine this idea: <idea>. Find the closest prior work,
the strongest competing explanation, and the smallest experiment that could
show the idea is wrong.
```

Resuming an existing project:

```text
Use $idea-to-paper with this repository. Read the existing notes, code, and
experiment artifacts, summarize what has actually been established, and tell
me the next decision I need to make.
```

Moving from results to a paper:

```text
Use $idea-to-paper to review these experiment results and this draft. Show
which claims are supported, which need more evidence, and which should be
weakened or removed.
```

Useful context to include, when available:

- the problem or phenomenon you care about;
- papers, methods, or baselines you already know;
- available data, compute, time, and expertise;
- a target venue or deadline;
- constraints that must not change.

It is fine if some of these are unknown. The skill will ask about decisions that materially affect the research instead of requiring a complete brief up front.

## What Working Together Looks Like

The skill first works out where the project really is. It does not force an existing project back through completed steps.

1. **Frame the question.** Clarify the setting, proposed contribution, assumptions, and what result would disprove the idea.
2. **Check the neighborhood.** Search for closely related work and separate genuine differences from renamed or cosmetic ones.
3. **Make a scoped decision.** Recommend `GO`, `PIVOT`, `HOLD`, or `NO-GO`, with reasons and remaining uncertainty.
4. **Test the cheapest risk first.** Design small checks before committing to expensive experiments.
5. **Build reliable evidence.** Record protocols, runs, failures, and interpretation limits so results can be reproduced and compared fairly.
6. **Write from evidence.** Connect each important paper claim to literature or experiment artifacts before polishing the prose.

At every point, you should be able to see what evidence was inspected, what remains uncertain, and what would justify moving forward.

The four recommendations have specific meanings:

- `GO`: the idea has enough support to justify the next test;
- `PIVOT`: part of the idea is promising, but the claim or mechanism needs to change;
- `HOLD`: a specific evidence, access, or resource gap must be resolved first;
- `NO-GO`: prior work, invalid assumptions, or infeasibility defeats the core idea.

## Typical Outputs

| What you ask for | What you can expect |
|---|---|
| Explore a direction | A terminology map, literature clusters, and candidate research questions |
| Check an idea | A comparison with the closest work, feasibility risks, and a `GO`/`PIVOT`/`HOLD`/`NO-GO` recommendation |
| Plan the research | A falsifiable hypothesis, baselines, metrics, thresholds, staged experiments, risks, and stop conditions |
| Resume a project | A verified project status, contradictions or missing artifacts, the current evidence checkpoint, and the next action |
| Evaluate experiments | A protocol-aware interpretation, failed assumptions, follow-up experiments, and a decision about the claim |
| Build a paper | A claim-to-evidence table, drafting plan, unsupported-claim list, and prioritized review findings |

Recommendations are always scoped to the sources and artifacts that were actually inspected. `GO` means the idea is ready for the next test, not that novelty or publication is guaranteed.

## Experiment Stages in Plain Language

The skill uses progressively stronger tests so that weak evidence is not mistaken for a scientific result.

| Stage | Question it answers |
|---|---|
| Spike | Can the riskiest technical piece work at all? |
| Smoke test | Does the full pipeline run and produce readable artifacts? |
| Pilot | Is there enough signal to justify a proper study? |
| Formal experiment | Does the claim hold under a fixed, fair, reproducible protocol? |
| Ablation or robustness test | Why does it work, and where does it stop working? |

You can stop, revise the idea, or return to an earlier stage whenever the evidence calls for it.

## Keeping a Long-Running Project Organized

For a short investigation, no special project structure is required. For work that will span multiple sessions, ask:

```text
Use $idea-to-paper to set up persistent research tracking in this repository.
Show me what would be created before writing anything.
```

With your approval, the skill can create a `docs/research/` area containing:

- a research map and project overview;
- decisions, open questions, and the current plan;
- experiment protocols, run records, and an experiment index;
- a table linking paper claims to evidence.

The setup is optional. It creates missing files only, stays inside the project you selected, and reuses an equivalent structure if one already exists.

### Why Is There an Initializer Script?

The included script creates the same research folders and starter documents reliably instead of rebuilding them by hand in every session. You normally do not need to run it yourself—the skill can preview and run it when you request persistent tracking. It does not conduct research, run experiments, or write a paper.

## Optional Deeper Questioning with `grill-me`

`idea-to-paper` works on its own. If the proposal still contains important unresolved choices, it may suggest a focused interview with the original `grill-me`.

- You decide whether to use it.
- If it is not installed, you can decline installation and continue with the built-in questions.
- An existing installation is not modified or reinstalled.
- The interview is limited to clarifying decisions; it does not edit files, run experiments, or take over the research workflow.

This option is most useful before committing to an experiment plan. It does not replace literature review, evidence evaluation, or paper review.

## What It Will Not Pretend

- One search with no match does not prove that an idea is novel.
- A working pipeline does not prove a scientific claim.
- A successful run is not automatically a reliable result.
- Missing citations, experiments, or numbers will not be filled with plausible inventions.
- Failed and negative experiments remain part of the research record.
- Expensive experiments require your confirmation after cost and scope are clear.
- Project writes stay inside the research repository you explicitly selected.

For generic prose polishing, a single-paper summary, or ordinary coding unrelated to a research project, use a more focused tool instead.
