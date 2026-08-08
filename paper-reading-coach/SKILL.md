---
name: paper-reading-coach
description: Teach, explain, and verify a specific academic paper or technical report through source-grounded structural mapping, prerequisite repair, equation and figure walkthroughs, small reproducible checks, misconception diagnosis, active recall, and resumable reading notes. Use when the user asks to summarize, read, learn, deeply understand, annotate, question, reproduce, or review one known paper or one of its sections, formulas, figures, tables, appendices, or companion implementations. Do not use for broad literature surveys, novelty searches, turning a research idea into a new paper, generic prose editing, or codebase learning where the paper is not the primary source.
---

# Paper Reading Coach

## Objective

Turn a paper from something the learner recognizes into something they can explain, calculate with, challenge, and verify. Anchor every substantive claim to the paper or a clearly labeled external source, repair missing prerequisites only when they block progress, and test understanding through retrieval rather than familiarity.

## Keep the Scope Clear

- Treat the selected paper, its supplement, and explicitly linked official artifacts as the primary reading scope.
- Distinguish what the paper reports from derivations, local checks, external context, and unresolved questions.
- Do not turn a single-paper reading request into a literature survey or research project unless the user asks to expand the scope.
- Do not create a website, notebook tree, question bank, or persistent progress files unless the user asks for those artifacts.
- Keep any requested writes inside the user-selected project or notes location. Reuse an existing documentation structure instead of creating a parallel one.
- Use concise paraphrases. Quote only the minimum text needed to locate or disambiguate a claim.

## Route the Request

Inspect the available source and start with the narrowest route that answers the request.

| Request or current state | Route | Main result |
|---|---|---|
| “What is this paper about?” | Orientation | Problem, contribution, method map, evidence, and limitations |
| “Teach me this paper” | Guided reading | Functional reading order, prerequisite bridge, and section-by-section learning |
| “Explain this formula/figure/table” | Focused deep dive | Symbols or axes, derivation or reading logic, assumptions, and boundary cases |
| “Does this claim really follow?” | Verification | Arithmetic, shape, code, or toy-experiment check with interpretation limits |
| “I do not understand this passage” | Confusion diagnosis | Exact sticking point, repaired prerequisite, and corrected mental model |
| “Quiz/review me” | Active recall | Questions, progressive hints, feedback, variants, and a review queue |
| Existing notes from an earlier session | Resume | Verified reading state, unresolved questions, and the next learning unit |

For a broad request, use this default sequence:

1. orient to the paper;
2. identify blocking prerequisites;
3. trace the core mechanism;
4. inspect the main evidence;
5. test the strongest claim and its limits;
6. use active recall to expose gaps.

Prefer a functional order over reading every page linearly. State the proposed order before a long walkthrough.

## Establish the Source and Learning Contract

1. Identify the exact paper version, title, authors, venue or repository, publication date, and available supplement.
2. Record whether locators refer to printed page numbers or PDF file pages.
3. Ask only for choices that materially change the result: learning goal, current background, desired depth, time budget, language, and preferred artifacts.
4. When these choices are absent, make a conservative assumption, state it, and begin with an orientation pass.
5. Inspect the table of contents, abstract, introduction, conclusion, figures, tables, appendices, and official companion repository before promising a reading plan.

Read [references/source-evidence-protocol.md](references/source-evidence-protocol.md) before building a detailed source map, answering a disputed claim, or mixing the paper with outside material.

## Build a Functional Paper Map

Summarize the paper in five connected layers:

1. **Problem:** What fails or costs too much without this work?
2. **Claim:** What does the paper say is new, better, or newly explained?
3. **Mechanism:** What components or reasoning are supposed to produce that result?
4. **Evidence:** Which experiments, proofs, tables, or analyses support each important claim?
5. **Boundary:** Which assumptions, missing comparisons, failure modes, or unreported details limit the conclusion?

Produce a reading route that names the relevant sections, equations, figures, tables, and appendices. Add prerequisites immediately before the first place they are needed; do not front-load a generic textbook.

## Teach One Learning Unit at a Time

Treat a section, mechanism, derivation, experiment, or figure as one learning unit. Use this order:

1. State the question the unit answers and why it exists.
2. State what the paper actually claims, with an exact locator.
3. Give an intuitive model in plain language.
4. Give the precise formulation.
5. Work a small concrete example.
6. Name the assumptions and where the intuition stops working.
7. Ask the learner to retrieve or apply the idea before moving on.

When using an analogy, always state where the analogy fails. When the paper omits a step, say so before supplying a derivation or external explanation.

### Explain Equations

For each important equation:

1. define every symbol at first use;
2. give tensor shapes, units, domains, indices, and dependency direction when applicable;
3. state the assumptions and the quantity the equation computes;
4. derive the equation in small justified steps instead of restating it;
5. work a minimal numeric or symbolic example;
6. check dimensions, limiting cases, invariances, signs, and edge conditions;
7. connect the result back to the algorithm, figure, or claim it supports.

Label a reconstruction that is not shown in the paper as a derivation, not as the authors’ explanation.

### Explain Figures and Tables

For each important visual:

1. identify its source and the claim it is meant to support;
2. decode axes, units, legends, aggregation, uncertainty, and comparison groups;
3. describe the strongest visible pattern without overstating causality;
4. check whether the caption, surrounding prose, and numbers agree;
5. state what the visual cannot establish;
6. use 3D or an interactive view only when the extra dimension carries real information.

## Verify Instead of Merely Rephrasing

Choose the cheapest check that could reveal a misunderstanding:

- recalculate a reported number;
- trace tensor shapes or units;
- test an identity on a small deterministic example;
- compare two claimed-equivalent computation paths;
- inspect the official implementation;
- remove one required assumption and observe the failure;
- test a limiting case or construct a counterexample.

Read [references/verification-lab-protocol.md](references/verification-lab-protocol.md) before writing or running a verification script, reproducing a result, or designing an interactive demonstration.

Never promote a toy check into proof of full-model quality, scalability, causality, or reproducibility. Report what the check supports and what it cannot support.

## Diagnose Confusion with a Bounded Question Packet

When the learner is stuck, collect:

- paper title and exact location;
- the smallest confusing excerpt or equation;
- the learner’s current interpretation;
- the specific question;
- the smallest surrounding context needed to answer it.

Answer from that packet first. If the answer requires information absent from the packet or paper, say so and label any added context as external. Point out contradictions or skipped reasoning rather than silently repairing the authors’ argument.

## Turn Understanding into Retrieval

Read [references/teaching-recall-protocol.md](references/teaching-recall-protocol.md) before designing a substantial quiz, review session, question bank, or spaced-review artifact.

For a normal guided session:

1. define observable learning objectives;
2. ask at least one question after each major unit;
3. vary questions across explanation, calculation, transfer, counterexample, and reviewer challenge;
4. reveal hints progressively: direction, key idea, first step, then full solution;
5. include a genuine variant with changed conditions;
6. use wrong answers to diagnose a specific misconception;
7. revisit weak items later instead of trusting self-reported familiarity.

In an interactive conversation, ask one question at a time and let the learner attempt it before showing the solution.

## Persist Reading State Only When Requested

Reuse the learner’s existing notes system when present. Otherwise, for multi-session work, keep a compact record containing:

- paper identity and version;
- reading goal and current route;
- completed learning units;
- evidence-backed takeaways with locators;
- glossary and prerequisites;
- unresolved questions and contradictions;
- verification checks and their limits;
- recall items with observed difficulty;
- exact next unit.

Verify resume notes against the paper and actual artifacts. Treat stale confidence scores or prose summaries as hints, not proof that a unit was mastered.

## Output Contract

For a substantial response, report:

1. current paper location and learning goal;
2. source material inspected and locator convention;
3. explanation or result, with evidence labels where needed;
4. assumptions, uncertainties, and what the paper does not establish;
5. a retrieval check or concrete next reading unit;
6. artifacts created or updated, if any.

Never claim that a paper has been fully understood, reproduced, proved correct, or exhaustively reviewed merely because its prose was summarized.
