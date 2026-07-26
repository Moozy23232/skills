# Experiment Ladder and Protocol

Use this protocol to move from an executable idea to paper-grade evidence.

## Ladder and Exit Criteria

| Stage | Question | Minimum exit evidence |
|---|---|---|
| Spike | Can the riskiest component work at all? | A focused artifact or failure diagnosis |
| Smoke | Does the complete pipeline execute correctly? | End-to-end output plus sanity checks |
| Pilot | Does the predicted signal plausibly exist? | Predeclared go/no-go metric and uncertainty |
| Formal | Does the paper claim survive a fair frozen comparison? | Replicated results under a frozen protocol |
| Ablation/robustness | Why, when, and where does it work? | Mechanism and boundary evidence |

Do not interpret a smoke pass as scientific support or a pilot as a final result.

## Freeze a Formal Protocol

Assign a protocol ID and record:

- research question, hypothesis, and predicted direction;
- experimental unit and sample inclusion/exclusion;
- dataset version, checksums, splits, and contamination controls;
- code commit, environment, dependencies, model, and checkpoint;
- all baselines and fairness constraints;
- training budget, hyperparameter search budget, and seed policy;
- checkpoint selection, early stopping, and failure recovery;
- evaluator version, prompts or rubrics, blinding, and human-review procedure;
- primary and secondary metrics with aggregation and statistical analysis;
- go/no-go thresholds and stop conditions;
- known confounds, exclusions, and planned ablations.

Freeze before observing formal outcomes. Any material change creates a new protocol version and links to the old one.

## Record Every Run

Create one immutable manifest containing:

```yaml
run_id:
stage: spike | smoke | pilot | formal | ablation | robustness
protocol_id:
status: running | pass | fail | invalid | stopped
started_at:
ended_at:
git_commit:
environment:
data_version:
model_version:
config_paths: []
command:
seeds: []
inputs: []
logs: []
artifacts: []
metrics: {}
resource_usage:
deviations: []
failure_class:
interpretation:
claim_boundary:
next_action:
```

Use exact artifact paths. Preserve stdout/stderr and intermediate diagnostics when they explain failure.

## Compare Fairly

- Hold protocol, data, evaluator, and budget constant for methods being compared unless the difference is the declared independent variable.
- Include strong and relevant baselines, not only convenient ones.
- Separate model-selection data from final evaluation data.
- Report uncertainty, variance, and failed seeds when appropriate.
- Prevent manual cherry-picking of checkpoints, examples, or metrics.
- Distinguish engineering failure, invalid run, null result, and evidence against the hypothesis.

## Decide After Each Stage

Record one action:

- `ADVANCE`: exit criteria met;
- `REPEAT`: uncertainty is reducible under the same protocol;
- `REVISE`: mechanism or protocol needs a documented new version;
- `STOP`: evidence or cost defeats the current path.

Estimate time, compute, and external cost before a materially expensive run. Obtain user confirmation for the expense, then persist the decision.
