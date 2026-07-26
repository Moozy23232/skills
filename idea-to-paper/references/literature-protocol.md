# Literature, Collision, and Feasibility Protocol

Use this protocol for idea discovery, related-work mapping, novelty checks, and pre-experiment feasibility decisions.

## 1. Frame the Search

Write the candidate claim in one sentence, then expand a query map across:

- problem and target population or environment;
- proposed mechanism and neighboring mechanisms;
- task, dataset, benchmark, and metric;
- known failure modes and negative terminology;
- synonyms, older terminology, and adjacent fields;
- likely author groups, repositories, and citation trails.

Record the search date and coverage. Treat recent literature as time-sensitive.

## 2. Search Breadth Before Depth

Declare a search budget before starting. Unless the user requests a systematic review, begin with three to five query families, screen roughly 20 to 40 plausible sources, and deep-read three to eight closest collisions. Return a provisional map with coverage gaps instead of silently expanding into an unbounded review. Increase the budget only when a named gate depends on it.

1. Use multiple query families rather than one long query.
2. Cluster results by research question and mechanism.
3. Identify surveys only as maps; verify important claims in original papers.
4. Follow backward citations, forward citations, author pages, and linked repositories for the closest work.
5. Read the full text of the closest collisions when accessible.
6. Stop at practical saturation: two successive query families add no new relevant cluster. Call this scoped saturation, not exhaustiveness.

Prefer primary papers, official datasets, official benchmarks, and official code. Mark secondary summaries as such.

## 3. Maintain an Evidence Ledger

Use one row per source:

| Field | Record |
|---|---|
| ID and citation | Stable identifier, title, authors, year, URL or local path |
| Source quality | Peer reviewed, preprint, official artifact, replication, or secondary |
| Exact question | What the source actually studies |
| Method and assumptions | Mechanism and boundary conditions |
| Data and evaluation | Dataset, split, baselines, metrics, evaluator |
| Main finding | Reported result, with location in the source |
| Limitations | Author-stated and independently observed |
| Relation | Supports, collides, narrows, contradicts, or enables |
| Confidence | Full text checked, artifact checked, or abstract only |

Keep quotations short and distinguish source statements from your inference.

## 4. Build a Collision Matrix

Compare the candidate idea with the nearest work:

| Work | Same problem? | Same mechanism? | Same assumptions/data? | Same evaluation? | Remaining difference | Material? |
|---|---:|---:|---:|---:|---|---:|

Test at least these collision types:

- exact claim already evaluated;
- same method under a different name;
- stronger general method subsumes the idea;
- benchmark or dataset invalidates the intended evaluation;
- negative result undermines the mechanism;
- concurrent or very recent work narrows the contribution.

Do not call a difference material unless it changes the scientific question, mechanism, evidence, applicability, or practical outcome.

## 5. Assess Feasibility

Check:

- data availability, licensing, privacy, and contamination risk;
- compute, time, hardware, API, and human-evaluation cost;
- baseline and evaluator reproducibility;
- signal-to-noise ratio and required replication;
- implementation dependency chain;
- ethics, safety, and access constraints;
- smallest falsifying experiment and likely failure causes.

Separate `unknown but testable` from `unavailable or unaffordable`.

## 6. Produce the Gate Decision

Return:

1. candidate claim;
2. closest collisions;
3. strongest supporting and contradicting evidence;
4. feasibility bottlenecks;
5. novelty scope and confidence;
6. `GO`, `PIVOT`, `HOLD`, or `NO-GO`;
7. the next evidence that could change the decision.

Never infer novelty solely from not finding a paper. Say which databases, query families, dates, languages, and full texts were covered.
