# Verification Lab Protocol

Use this protocol when a paper claim can be checked through arithmetic, shapes, code, a toy example, or a small reproducible experiment.

## Choose the Cheapest Revealing Check

Prefer, in order:

1. arithmetic and unit checks;
2. tensor-shape and index checks;
3. limiting cases, invariances, and counterexamples;
4. a hand-worked toy example;
5. two independently implemented equivalent paths;
6. inspection of the official implementation;
7. a small executable reproduction;
8. a larger experiment only when the smaller checks cannot answer the question.

Do not build an interactive laboratory for a claim that a few lines of calculation can settle.

## Specify the Check Before Running It

Record:

- paper claim and exact locator;
- suspected ambiguity or failure mode;
- expected observable if the interpretation is correct;
- inputs taken from the paper;
- inputs invented for the toy setting;
- baseline or independent path;
- metric and tolerance;
- deliberate break or counterexample;
- what a pass and failure would mean.

Freeze these choices before looking at the output when confirmation bias matters.

## Build a Trustworthy Micro-Experiment

1. Use the smallest dimensions that retain the claimed mechanism.
2. Use deterministic inputs and record seeds.
3. Implement the comparison path independently when practical.
4. Print or save intermediate values that can reveal the first divergence.
5. Compare with an explicit error metric and tolerance.
6. Add a deliberate break that removes one assumption, normalization, mask, rescaling, or update term.
7. Verify that the break causes the predicted failure rather than an unrelated error.
8. Test edge cases, including zero, one element, maximum range, or degenerate shapes as relevant.

A “break it” control is useful only when it corresponds to a real dependency in the paper.

## Separate Parameters by Provenance

Label:

- values reported by the paper;
- values taken from official code or configuration;
- values chosen only to make the toy example readable;
- values tuned after observing results.

Never let a visualization simplification masquerade as a reported architecture or dataset value.

## Inspect Companion Code Carefully

When official code exists:

1. record repository, commit or release, file, symbol, and active configuration;
2. trace the actual caller and data path instead of reading an isolated helper;
3. compare equation terms with implementation operations;
4. check defaults, masks, normalization, data types, and numerical-stability branches;
5. identify differences between paper pseudocode and executable behavior;
6. run a minimal reference test when the environment permits.

Treat third-party reimplementations as external evidence and state that provenance.

## Interpret the Result

Report four separate statements:

1. **Observed:** exact output, error, trace, or artifact.
2. **Supports:** the narrow interpretation consistent with the observation.
3. **Does not support:** quality, scale, speed, causal, or generalization claims not tested.
4. **Next check:** the smallest remaining test if the paper’s central claim is still unresolved.

Examples:

- Numerical agreement between recurrent and blockwise forms supports implementation equivalence on the tested inputs; it does not prove production speed or stability.
- Recomputing a table entry supports arithmetic consistency; it does not validate the dataset or evaluator.
- Matching official code supports a description of that release; it does not prove the paper’s empirical conclusion.

## Validate the Artifact

- Run the code rather than only reading it.
- Check syntax and dependencies.
- Compare against a simple reference implementation.
- Inspect representative outputs or plots visually.
- Preserve commands, versions, inputs, and raw results.
- Keep failed checks and discrepancies.
- State when environment limits prevented execution.

Request confirmation before any materially expensive run and provide a time, compute, and storage estimate.
