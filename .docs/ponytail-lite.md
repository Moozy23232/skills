# Ponytail Lite

[简体中文](ponytail-lite_zh.md)

`ponytail-lite` is an opt-in coding mode for building the smallest solution that fully handles the real requirement.

It behaves like a deliberately lazy senior developer: understand the affected flow first, then avoid speculative features, unnecessary abstractions, new dependencies, and code the platform already provides. “Lazy” means efficient, not careless.

## Activation

This skill never activates automatically. Invoke it explicitly:

```text
Use $ponytail-lite to implement this change.
```

The default intensity is `full`. Once activated, it remains active for coding requests in the current session. Say `stop ponytail-lite` or `normal mode` to turn it off.

You can also choose an intensity:

```text
Use $ponytail-lite lite to add this endpoint.
Use $ponytail-lite ultra to simplify this implementation.
```

## What It Can Help With

- question work that does not need to exist yet;
- find and reuse helpers, types, and patterns already in the codebase;
- prefer the standard library, native platform features, and installed dependencies;
- solve a requirement with the fewest necessary files and lines;
- trace callers and fix a bug once at its shared root cause;
- keep one small runnable check for non-trivial logic;
- mark intentional shortcuts with their limits and upgrade path;
- review a diff only for avoidable complexity and over-engineering.

The skill reduces the solution only after understanding the task and the real code path. A small change in the wrong place is still a bad change.

## The Decision Ladder

It stops at the first option that fully handles the requirement:

1. Does this need to exist at all?
2. Does the codebase already contain it?
3. Does the standard library provide it?
4. Does the platform have a native feature for it?
5. Can an already-installed dependency do it?
6. Can the solution be one line?
7. If none of those hold, what is the minimum new code that works?

If two options work, the skill takes the earlier and simpler one. It does not turn this check into a research project.

## Intensity Levels

| Level | Behavior |
|---|---|
| `lite` | Builds what you asked for and briefly names a simpler alternative. |
| `full` | Enforces the decision ladder and ships the shortest complete diff. This is the default. |
| `ultra` | Applies strict YAGNI, prefers deletion, and challenges requirements that can safely wait. |

Explicit requirements still win. If you confirm that the full version is necessary, the skill implements it without repeatedly arguing for a smaller scope.

## Try These Prompts

Build a lean feature:

```text
Use $ponytail-lite to add caching to this fetch path. Trace the real callers,
reuse anything already present, and leave the smallest runnable check.
```

Fix a root cause:

```text
Use $ponytail-lite full to fix this validation bug. Inspect every caller of
the function you change and fix the shared cause instead of patching one path.
```

Push back on speculative work:

```text
Use $ponytail-lite ultra for this proposal. Implement only what is required
now and state in one line what should wait for measured demand.
```

Return to ordinary behavior:

```text
Stop ponytail-lite and return to normal mode.
```

## Review Mode

Invoke the one-shot review mode when you want findings but no edits:

```text
Use $ponytail-lite review on this diff.
```

The review looks only for code that can be deleted, replaced by the standard library or a native feature, or expressed more directly. Each finding identifies the file and line, labels the type of simplification, and names the replacement. It ends with an estimated number of removable lines or `Lean already. Ship.`

Correctness, security, and performance review are intentionally outside this mode. Request those separately when needed.

## What It Will Not Simplify Away

- validation at trust boundaries;
- error handling that prevents data loss;
- security measures;
- accessibility basics;
- calibration controls required by real hardware;
- anything you explicitly require.

Non-trivial branches, loops, parsers, and money or security paths keep one minimal runnable check. Trivial one-liners do not gain tests merely for ceremony.

## Typical Output

After making the change, the skill keeps the handoff short: what it implemented, what it deliberately skipped, and when the skipped complexity would become justified. Explanations, reports, and walkthroughs remain detailed when you explicitly ask for them.
