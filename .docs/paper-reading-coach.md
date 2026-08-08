# Paper Reading Coach

[简体中文](paper-reading-coach_zh.md)

`paper-reading-coach` helps you turn one academic paper or technical report into source-grounded, testable understanding.

It can start with a quick map, teach the paper in a functional order, unpack a difficult formula or figure, check a claim with code or a toy example, quiz you, and keep compact reading state across sessions.

## What It Can Help With

- summarize a known paper without losing the connection to exact sections and evidence;
- build a reading route around your background and goal;
- repair prerequisites only where they block the paper;
- explain equations with symbols, shapes, assumptions, derivations, and examples;
- read figures and tables as evidence rather than decoration;
- separate the authors' claims from derivations, checks, outside context, and unknowns;
- test an identity, reported number, implementation detail, or hidden assumption;
- diagnose a confusing passage from the smallest useful context;
- create questions with progressive hints, meaningful variants, and misconception feedback;
- resume from existing notes without rereading mastered sections.

It focuses on understanding one selected paper. Use `idea-to-paper` instead when the main goal is novelty search, research planning, experiments for a new claim, or writing a new paper.

## Try These Prompts

Map a paper:

```text
Use $paper-reading-coach to map this paper. I know basic Transformers but not
state-space models. Give me a functional reading order, the prerequisites I
actually need, and the three claims I should verify most carefully.
```

Deep-read a formula:

```text
Use $paper-reading-coach to explain Equation 7. Define every symbol and tensor
shape, derive each step the paper skips, work a tiny numerical example, and
show one boundary case where the intuition stops working.
```

Check a claim:

```text
Use $paper-reading-coach to check whether the blockwise and recurrent forms in
this paper are really equivalent. Design the smallest deterministic test,
include one switch that breaks a required assumption, and state exactly what
the result cannot prove.
```

Review interactively:

```text
Use $paper-reading-coach to quiz me on Sections 2 and 3. Ask one question at a
time, do not show the answer before I try, and give hints progressively.
```

Useful context includes the paper or stable link, the exact version, your goal, current background, desired depth, and available time. Missing context is fine; the skill begins with conservative assumptions and asks only for decisions that materially change the route.

## How It Reads a Paper

1. **Orient.** Identify the problem, central claims, mechanism, evidence, and limitations.
2. **Route.** Choose a functional order and insert prerequisites immediately before they are needed.
3. **Explain.** Move from motivation and intuition to precise notation, derivation, and a concrete example.
4. **Verify.** Use arithmetic, shapes, limiting cases, code, or a small reproducible experiment to expose misunderstandings.
5. **Challenge.** State assumptions, missing evidence, alternative explanations, and what each result cannot establish.
6. **Retrieve.** Use questions, progressive hints, variants, and later review to test actual recall.

For important claims, it keeps five kinds of evidence distinct: what the paper states, what can be derived from it, what was directly checked, what came from external sources, and what remains unknown.

## Typical Outputs

| Request | Typical output |
|---|---|
| Quick orientation | Paper map, contribution summary, reading route, and caution points |
| Guided deep reading | Learning units, prerequisite bridges, exact source locators, and retrieval checks |
| Equation walkthrough | Symbol and shape table, derivation, toy example, assumptions, and edge cases |
| Figure or table walkthrough | Axes and comparison map, supported claim, confounds, and interpretation limits |
| Claim verification | Reproducible check, observed result, supported interpretation, and non-claims |
| Review session | One-at-a-time questions, hint usage, misconception feedback, and transfer variants |
| Multi-session study | Compact reading state, evidence-backed takeaways, open questions, and next unit |

## What It Will Not Pretend

- A fluent summary does not prove understanding.
- A paper's self-reported result is not independent validation.
- A missing derivation will not be attributed to the authors.
- Outside knowledge will not be presented as paper content.
- A toy experiment will not be stretched into a full-scale empirical claim.
- One inspected version will not silently stand in for every revision.
- A paper will not be called correct, fully reproduced, or exhaustively reviewed without matching evidence.

## Design Inspiration

The workflow was synthesized from the evidence-bound explanations, runnable numerical checks, deliberate “break it” controls, progressive hints, active recall, and scoped question packets demonstrated by [kimi-k3-learn](https://github.com/ViffyGwaanl/kimi-k3-learn) and its [live learning system](https://kimi.papertok.ai/#s0-1). The skill generalizes those principles into a tool-agnostic paper-reading process; it does not copy the project’s website implementation or learning content.
