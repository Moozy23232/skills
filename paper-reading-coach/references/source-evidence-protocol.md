# Source and Evidence Protocol

Use this protocol when the reading requires precise citations, disputed claims, outside context, or a reusable evidence map.

## Contents

- Prefer Sources in This Order
- Create a Source Map
- Label Evidence
- Maintain a Claim Ledger
- Audit Coverage
- Build a Confusion Packet
- Cite Without Flooding

## Prefer Sources in This Order

1. The exact paper version selected by the learner.
2. Its official appendix, supplement, data, model card, or errata.
3. The authors’ official implementation and released artifacts.
4. The archival venue version or an explicitly compared revision.
5. Other primary papers needed for background or comparison.
6. Secondary explanations only when they add teaching context unavailable from primary sources.

Do not silently merge versions. Record version identifiers and material differences when an arXiv revision, proceedings paper, and project page disagree.

## Create a Source Map

Record:

- title, authors, date, venue, and stable URL or local path;
- version, revision date, and supplement;
- printed page number versus PDF file page number;
- section, equation, figure, table, theorem, algorithm, and appendix identifiers;
- official repository commit or release when code is inspected;
- inaccessible, unreadable, or missing artifacts.

Use the paper’s printed locator when available. If it differs from the PDF page index, state both once, for example: `paper p. 7 (PDF page 9)`.

## Label Evidence

Use these labels internally and expose them whenever provenance could be confused:

| Label | Meaning |
|---|---|
| `paper` | Explicitly stated or displayed in the selected paper |
| `derived` | Logically or mathematically derived from paper material |
| `verified` | Recalculated, executed, or checked against an artifact |
| `external` | Added from another cited source |
| `unknown` | Not established by available material |

Never present `derived`, `verified`, or `external` material as though the paper said it.

## Maintain a Claim Ledger

For a detailed reading, track:

| Field | Content |
|---|---|
| Claim | One specific proposition |
| Importance | Core, supporting, or contextual |
| Evidence label | `paper`, `derived`, `verified`, `external`, or `unknown` |
| Locator | Exact page and structural identifier |
| Support | Experiment, proof, table, implementation, or argument |
| Scope | Dataset, model size, assumptions, metric, or theorem conditions |
| Status | Supported, partial, contradicted, or unresolved |
| Check | Recalculation, code trace, reproduction, or counterexample |

Split compound claims. A method can be faster, more accurate, and more memory-efficient for different reasons and with different evidence.

## Audit Coverage

For each core claim, check:

1. Does the abstract or introduction overstate what later evidence measures?
2. Is the comparison controlled and is the strongest relevant baseline present?
3. Are uncertainty, seeds, sample size, and selection rules reported?
4. Does the appendix add assumptions or exclusions missing from the main text?
5. Does the released implementation match the described algorithm?
6. Are negative results, failure modes, or resource costs omitted?
7. Does a result show association, mechanism, causality, or only feasibility?

Describe search and inspection coverage precisely. “No contradiction found in Sections 2–4 and Appendix B” is defensible; “the paper is correct” is not.

## Build a Confusion Packet

Use this shape when asking or answering a bounded question:

```text
Paper and version:
Location:
Quoted or paraphrased passage:
My current interpretation:
My exact question:
Context included:
Answer constraints:
- Answer from the included paper material first.
- Say when the material does not contain the answer.
- Label derivations and external context.
- Point out contradictions or skipped steps.
```

Keep the context centered on one confusion. Add the containing subsection or prerequisite only when the smaller excerpt is insufficient.

## Cite Without Flooding

- Attach citations to claims, not whole pages of prose.
- Prefer section, equation, figure, or table identifiers over vague page-only citations.
- Paraphrase by default; quote only language whose exact wording matters.
- Cite the original source for numerical results and method details.
- When using an official implementation, cite the file, symbol, commit, and relevant configuration.
- State when a source was unavailable or only an abstract was inspected.
