# Claim-Evidence Paper Protocol

Use this protocol when evidence is mature enough to draft, review, or strengthen a paper.

## 1. Freeze the Writing Contract

Record target venue, submission date, format, page and appendix limits, audience, artifact policy, anonymity rules, and the one-sentence core claim. Verify current venue rules from official sources.

## 2. Build the Claim-Evidence Matrix

Use one row per externally visible claim:

| Claim ID | Exact claim | Scope and assumptions | Supporting protocol/runs | Figure/table | Related work | Counterevidence | Status |
|---|---|---|---|---|---|---|---|

Use statuses `supported`, `qualified`, `missing`, `contradicted`, or `out-of-scope`. Drafting must not silently promote a missing or qualified claim.

## 3. Draft in Evidence Order

1. Methods from frozen protocol files.
2. Results from manifests and reproducible analyses.
3. Limitations and failure cases from negative evidence.
4. Related work from the collision matrix.
5. Introduction and contribution list from the supported claims.
6. Conclusion, title, and abstract after scope is stable.

Keep observed results separate from interpretation. State the evaluation population, uncertainty, and boundary conditions near each result.

## 4. Make Figures Reproducible

- Generate quantitative plots from versioned raw artifacts and scripts.
- Preserve data transformations, filters, aggregation, and uncertainty computation.
- Use editable conceptual diagrams when practical.
- Keep labels, legends, units, colors, terminology, and numbers consistent with the text and tables.
- Do not use illustrative numbers in a result figure.

## 5. Review in Independent Passes

Run separate passes:

1. **Validity**: leakage, confounds, protocol deviations, unfair baselines, statistics, unsupported causality.
2. **Claim coverage**: every contribution maps to evidence; every decisive result supports a named claim.
3. **Reproducibility**: data, code, versions, seeds, evaluator, and artifacts are recoverable.
4. **Literature and citations**: nearest work is represented accurately and every citation supports the attached statement.
5. **Consistency**: abstract, body, tables, figures, appendix, notation, and reported numbers agree.
6. **Presentation**: argument order, concision, definitions, captions, accessibility, and venue compliance.

Triage findings as `P0`, `P1`, or `P2`. Fix validity before rhetoric.

## 6. Add Theory Carefully

For each proposed theorem, equation, or bound, record:

- definition and assumptions;
- exact statement and quantifiers;
- derivation or proof;
- edge cases and counterexamples;
- empirical prediction;
- where the assumptions hold in the implemented method.

Call an unproved statement a conjecture. Remove decorative mathematics and any formal claim that cannot survive an independent derivation.

## 7. Declare Readiness Honestly

Call a paper submission-ready only when:

- no open `P0` issue remains;
- core claims are supported or explicitly qualified;
- figures and tables are reproducible;
- citations and venue constraints are verified;
- limitations and negative evidence are disclosed;
- an adversarial reviewer pass has been answered.

List residual `P1` and `P2` issues rather than hiding them.
