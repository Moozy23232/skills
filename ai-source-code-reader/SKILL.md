---
name: ai-source-code-reader
description: Deeply read AI/ML source code by tracing call paths, configs, branches, tensor shapes, formulas, and grounded examples. Use for Megatron, vLLM, VeRL, Ms-Swift, TinyZero, Search-R1, or similar repos.
---

# AI Source Code Reader

## Overview

Use this skill to read AI source code deeply instead of answering from memory or from surface-level files. Prefer concrete repository evidence, precise call paths, tensor shape tracking, and validated examples over broad conceptual summaries.

For nontrivial requests, read `references/deep-reading-checklist.md` before producing the final explanation.

## Working Rules

- Inspect the current repository before explaining. Do not rely on general knowledge when code is available.
- Prefer `rg`, `rg --files`, language-aware symbols, tests, examples, configs, and docs to build the call graph.
- Cite local files and line numbers for important claims.
- Track both caller and callee sides: entry points, wrappers, config plumbing, class construction, dispatch, hooks, kernels, and post-processing.
- State uncertainty explicitly when a branch cannot be verified from the available code.
- Keep the final answer in the user's language unless asked otherwise.
- Do not modify source files unless the user explicitly asks for code changes.

## Reading Workflow

1. Define the reading target.
   - Restate the feature, function, class, CLI command, config option, or training/inference path being explained.
   - If the request is broad, propose a functional reading order and then dive into the most likely core path. Ask one concise question only when multiple incompatible targets cannot be resolved from context.

2. Build a code map before explaining.
   - Locate entry points such as CLI commands, scripts, registry decorators, model builders, trainer loops, inference engines, schedulers, kernels, or config files.
   - Identify core modules, adjacent helper modules, tests/examples, and important external dependencies.
   - Record the exact path order to explain, from user-facing entry point to lower-level implementation.

3. Trace the real execution path.
   - Follow imports, aliases, registries, inheritance, callbacks, decorators, dataclasses, config defaults, feature flags, and runtime dispatch.
   - For AI systems, always check distributed and performance branches: tensor/pipeline/data parallelism, CUDA/Triton kernels, KV cache, micro-batching, gradient accumulation, mixed precision, offload, checkpointing, LoRA/PEFT, rollout workers, reward functions, and generation sampling.
   - Verify branch conditions from code rather than assuming the common case.

4. Explain in a planned order.
   - Start with a concise functional map: what each relevant file/module contributes.
   - Explain key code blocks in execution order.
   - Use line-by-line explanation for critical logic, state transitions, tensor transforms, scheduling decisions, loss/reward computation, communication primitives, and kernel launch arguments.
   - For less important glue code, summarize and say why it is not central.

5. Track tensors and data structures.
   - Define symbols before using them, such as `B` batch size, `S` sequence length, `H` hidden size, `V` vocab size, `TP` tensor-parallel size, `N` number of samples, `G` generated tokens, or `K/V` cache blocks.
   - For each key tensor, explain semantic meaning, shape before and after the operation, dtype/device if relevant, and layout changes such as transpose, reshape, shard, gather, pad, flatten, pack, or cache append.
   - If shape depends on a config or runtime condition, show the condition and provide separate cases.

6. Include math and examples.
   - Write formulas in LaTeX for losses, rewards, attention, normalization, sampling, policy gradients, KL terms, or communication partitioning.
   - Provide examples that match the exact code path being explained. Use small concrete shapes or values and validate them against the local code, tests, configs, or documented assumptions.
   - Mark an example as hypothetical only when it cannot be directly verified, and keep it consistent with the code.

7. Close with verification and summary.
   - Summarize what was verified from source files, what remains conditional, and which files are the best next places to read.
   - End with a plain-language explanation of the whole mechanism, connecting the low-level details back to the user-visible behavior.

## Output Shape

Use this structure for substantial explanations:

1. **阅读范围**: target, assumptions, repo/version clues, and what is out of scope.
2. **讲解顺序**: ordered file/function path with one-line role per item.
3. **整体流程**: compact end-to-end control/data flow.
4. **逐段讲解**: critical code blocks with line references, conditions, and side effects.
5. **张量与 shape**: table or bullets covering semantic meaning and transformations.
6. **公式**: LaTeX formulas tied directly to the code.
7. **例子**: validated small example for the current path.
8. **通俗总结**: short explanation that preserves the important caveats.

For small questions, use a shorter version but keep source evidence, shape tracking, and caveats.

## Depth Guardrails

- Do not stop after reading only the most obvious file. Check at least the definition, caller, callee, config source, and one test/example when available.
- Do not present a branch as universal when it depends on flags, backend, model type, parallelism, dtype, or runtime environment.
- Do not invent shapes. Derive them from code, function signatures, asserts, comments, tests, or standard tensor conventions used by the same repo.
- Do not use examples that are only thematically related. Tie each example to the exact function or code block being explained.
- Do not skip "boring" plumbing when it changes behavior, shape, scheduling, randomness, loss scaling, masking, or distributed communication.
