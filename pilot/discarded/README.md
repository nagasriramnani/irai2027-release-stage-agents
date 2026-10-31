# Discarded pilot runs

The 34 runs here were made on 2026-10-30 before a harness bias was fixed: search-result ties (two versions of one
source share a title) were broken by source-id order, so the superseded version was always listed first. The fix (seeded
per-run tie-break, harness/env.py) was made before any analysis of these runs. They are kept for transparency and are
not used anywhere.

## Second discard (69 runs, 2026-10-30): `runs_dev_qwen3-8b_textual_toolcall_bug.jsonl`
Two harness bugs found by inspecting interim pilot output (not by looking at outcome rates):
1. Qwen3 sometimes writes a tool call as plain text (`submit_answer {"answer": ..., "refused": true}`) instead of a
   structured call (27 assistant turns in 69 runs). The loop treated it as a free-text answer and lost `refused: true`,
   so correct refusals were scored as missed refusals. Fix: `textual_calls()` in harness/run.py parses and executes such
   calls; transcripts now flag them (`textual_call: true`) so their frequency can be reported.
2. One run crashed when the model passed a JSON object as the search query. Fix: `Env.call` coerces arguments to text.
The scorer's abstention patterns were also widened ("could not be found", "not accessible", ...); because every run is
re-scored from its trace (notebook 03), this change applies uniformly to all kept runs.

## Third discard (160 runs, 2026-10-30): `runs_dev_qwen3-8b_pre_design_review.jsonl`
Stopped after an adversarial design review (5 reviewer lenses, each finding checked by a skeptic: 56 confirmed, 4 refuted).
The benchmark itself changed, so these runs no longer match the frozen data:
* source condition was confounded with format and calculation type (all authoritative/stale data items CSV, all
  prohibited/distractor JSON) -> counterbalanced;
* post-release permission drift was invisible to any agent -> announced in the stated policy (tool labels still lag);
* stage-injected wrong versions often left comparison answers unchanged -> every confounder and fault now provably changes
  the answer (asserted at generation);
* the ABCR scorer counted wrong comparison answers as leaks -> ABCR = forbidden content reached the agent;
* added the observable-ideal reference agent so stage effects are reported as agent-attributable differences.
Full list: protocol/PROTOCOL.md §10.

## Fourth discard (1,080 scripted reference runs, 2026-10-30): `ideal_v1.1_tiebreak/`
The observable-ideal agent's runs (`runs_dev_ideal.jsonl`, `runs_dev_ablation_ideal.jsonl`) made with an inverted
tie-break: when a package hides the metadata that tells two versions apart, the agent should take the version the search
lists first (the same seeded coin the LLM sees) but took the last-listed one. Its guesses were therefore anti-correlated
with the LLM's and the agent-minus-ideal contrasts were inflated (H1 SAR DiD +0.15 -> +0.06 after the fix). Found by
checking why the LLM appeared to beat the reference agent. These are scripted, deterministic runs; no LLM run was
discarded. A self-check now asserts the shared coin.

## Fifth discard (whole v1.1 pilot, 2026-10-30): `v1.1_pilot/`
600 Qwen3 runs, 480 Qwen3 ablation runs, 180 Llama-3.1 runs, the reference-agent runs and the v1.1 analysis. A six-lens
adversarial audit (49 findings; serious ones checked by two skeptics, 28 upheld) found benchmark artifacts that change agent
behaviour, so the benchmark was regenerated (v1.2) and these runs no longer match its hashes:
* the catalog `owner` field showed the asking role as owner of every forbidden record (drove most prompt-mode breaches);
* post-release freshness gold could equal a confounder's answer; dev-split factors were not balanced; evidence rows were
  always first; prohibited policy documents carried draft markers; connector faults hit confounders;
* Llama-3.1 sent `refused` as the string "false", which the harness coerced to true (Llama numbers were not interpretable).
Scoring and analysis fixes (tolerance, stated-policy credit, exposure, H2c, estimand, power) are listed in protocol §10.
The full audit is reproducible from the repository state; these runs are kept for transparency and are not analysed.

## Sixth discard (124 Qwen3 runs, 2026-10-30): `v1.2a_partial/`
The first v1.2 pilot was stopped after 124 runs when an adversarial check of the v1.2 fixes found that the new dev parities
aliased format with distractor type, restriction cue and gold position, and that perturbed versions could carry rates above
100% (one post-release gold). Both change what the agent sees, so the benchmark was regenerated (v1.2b) and the pilot
restarted. Protocol §10 lists all v1.2b changes.

## Seventh discard (170 Qwen3 runs, 2026-10-30): `v1.2b_partial/`
Stopped when a second check of the fixes found remaining defects that change what the agent sees: the Brazil-addendum
distractor documents claimed group-wide scope in their body (gold arguable); only cued prohibited titles said "adjusted";
JSON bodies alone carried scope/period and a fixed "/v2/" endpoint; connector faults fell only on confounded items. All were
rated minor by skeptics but would have made the pilot run on an instrument the confirmatory study will not use, so the
benchmark was regenerated (v1.3). From v1.3 on, a stopping rule applies (protocol §10): only critical or major
behaviour-affecting findings that survive a skeptic stop a run.

## Eighth discard (180 Llama-3.1 runs, 2026-10-31): `llama_v1.3_default_template/`
The v1.3 Llama replication ran with Ollama's default `llama3.1` chat template, which renders the tool definitions only
when the last message is a user message. After the first tool result the model therefore saw no tools, except those named
in its system prompt; the development prompt (`dev-0.3`) names only `submit_answer`, so no development run that searched
ever read a source (SAR 0/24), and some production reads used guessed argument names (`id`, `src_id`) that return 404.
This made "which tools the prompt names" a hidden, stage-dependent factor for Llama only (Qwen3's template keeps the tools
in the system block on every turn; its runs are unaffected). Found by the post-pilot artifact audit and confirmed with
`ollama show llama3.1:8b --template`. The replication was re-run with `harness/llama3.1-tools.Modelfile`
(`llama3.1-tools:8b`: same weights, tools rendered in the latest user message). Protocol §10 v1.3a.
