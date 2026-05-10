# Deep Reading Checklist

Use this checklist for nontrivial AI source-code reading tasks. It is a guardrail against shallow explanations and missed conditions.

## 1. Scope And Evidence

- Identify the exact target: file, class, function, CLI, config key, training step, inference path, kernel, or algorithm.
- Capture repository clues that affect behavior: branch/version, package layout, optional backends, examples, tests, and default configs.
- Prefer local evidence in this order: executable entry points, implementation files, tests, examples, docs, then external background knowledge.
- Quote or cite file paths and line numbers for key claims.

## 2. Call-Path Coverage

Verify these layers when they exist:

- User entry: CLI/script/notebook/example/config.
- Object construction: registry, factory, dataclass, model/trainer/engine builder.
- Core execution: forward pass, generate loop, train step, rollout, scheduler, worker, executor, or kernel wrapper.
- Helpers: masking, batching, padding, sampling, reward/loss calculation, logging, metrics, checkpointing.
- Lower-level implementation: CUDA/Triton/custom op, collective communication, cache/block manager, fused op, or distributed wrapper.
- Tests/examples: at least one nearby test or config that shows intended usage.

## 3. Conditional Branches

Look for branches controlled by:

- Model architecture: decoder-only, encoder-decoder, MoE, multimodal, LoRA/adapter, reward model, policy/ref/value model.
- Runtime mode: train/eval/inference, eager/graph, prefill/decode, rollout/update, streaming/non-streaming.
- Distributed setup: DP, TP, PP, EP, FSDP, ZeRO, sequence parallel, worker placement, rank/world size.
- Precision/performance: fp32/fp16/bf16/fp8, quantization, flash attention, paged attention, CUDA graphs, Triton/CUDA fallback.
- Data shape: packed vs padded, variable sequence length, micro-batch, gradient accumulation, beam/sample count, prompt/generated split.
- Config flags: defaults, overrides, environment variables, optional dependencies.

When a branch matters, explain the condition and the behavior for each relevant case.

## 4. Tensor Shape Protocol

For each key tensor, fill in as much as the code supports:

- Name in code.
- Semantic meaning.
- Shape with symbols defined.
- Dtype and device if they affect behavior.
- Layout/order, such as `[B, S, H]`, `[S, B, H]`, sharded `[B, S, H/TP]`, packed tokens `[T]`, cache blocks, or flattened samples.
- Producer and consumer.
- Transformations: view/reshape, transpose, split/chunk, gather/scatter, pad/unpad, mask, indexing, concat, reduce, all-reduce/all-gather.
- Edge cases: empty sequences, EOS truncation, left/right padding, uneven shard, last micro-batch, max length, cache eviction.

Use a table when more than three tensors are involved.

## 5. Math Protocol

Use LaTeX for formulas and connect each symbol to code variables:

- Attention: $QK^\top / \sqrt{d}$, masks, softmax, value projection, cache update.
- Losses: cross entropy, masked loss, mean/reduction, label shift.
- RL/RLHF: reward, advantage, returns, KL penalty, PPO/GRPO objective, clipping, entropy.
- Distributed partitioning: shard size, gather/reduce semantics, rank-local vs global shape.
- Sampling: temperature, top-k/top-p filtering, logprobs, beam or best-of semantics.

State whether the formula is directly implemented in the code block or is the mathematical interpretation of several operations.

## 6. Example Quality Bar

An example is acceptable only if it satisfies all of these:

- It uses the same function/path currently being explained.
- Its dimensions satisfy code asserts and config assumptions.
- It exercises the branch under discussion.
- It shows at least one intermediate shape or value that helps interpret the code.
- It does not contradict repo defaults, tests, comments, or naming.

If a fully verified example is unavailable, say which assumption is hypothetical.

## 7. Final Answer Checks

Before finalizing, verify:

- The explanation follows execution order, not just file order.
- Every important conditional branch is either covered or explicitly out of scope.
- Shape symbols are defined before use.
- Tensor shape changes are not skipped at reshape, transpose, split, gather, reduce, mask, concat, and cache boundaries.
- Examples are local to the current code path.
- The summary is simple but does not erase important conditions.
