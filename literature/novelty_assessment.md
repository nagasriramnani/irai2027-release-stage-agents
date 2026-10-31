# Novelty assessment

Paper: *Release-Stage Effects on AI Agent Answer Reliability Across Business Simulation Profiles: Source Appropriateness, Answer Support, and Access-Boundary Compliance* (IRAI 2027 target).
Date: 2026-10-30. Inputs: three independent novelty-challenge reports, nine topic literature sweeps, and my own verification of the novelty-report candidates on arXiv, ACL Anthology and ICML pages. All keys refer to `references.bib`.

## Verdict

**Not pre-empted. The novelty margin is narrow, though, and it sits in the combination, not in any single component.** All three reviewers reached the same conclusion on their own.

Every ingredient exists somewhere:

| Our ingredient | Already shown by |
|---|---|
| Synthetic enterprise roles + RBAC + multi-source data | EnterpriseBench, OrgAccess, ACCESS DENIED INC, CRMArena-Pro |
| Stale / denied-permission / conflicting evidence with evidence-gated success | LayerRAG-Bench, EnterpriseRAG-Bench, HoH, GaRAGe |
| Prompt-only policy is unreliable; enforcement outside the model works better | OrgAccess, Control Illusion, CRMArena-Pro, PCAS (48% to 93%), Prompts Don't Protect, Arceo & Narsing |
| Compliance-conditioned success < raw success; groundedness differs from correctness | ST-WebAgentBench (CuP), LayerRAG-Bench, Trust-Score, Liu et al. 2023 |
| Lifecycle / release-gated evaluation of LLM apps | EDDOps (process model), Maiorano 2026a/b (single-system case study, CI gates) |
| "Access-boundary" as a risk construct | Baek et al. 2026 ("access-boundary awareness") |

What no verified paper does: a **controlled factorial** that crosses (i) five release-stage configuration packages, including a post-release package with injected document **and** permission drift, with (ii) prompt-only vs retrieval/tool-level permission enforcement, on one tool-using agent across six business role profiles. Our design also uses controlled source conditions (authoritative-permitted, relevant-but-prohibited, stale, distractor, no-permitted-source) and reports **Source Appropriateness, Supported Answer Rate and Access-Boundary Compliance as separate outcomes** next to accuracy and refusal correctness vs over-restriction. The analysis uses mixed-effects models and double-coded human labels.

## Closest works, ranked

| # | Key | Work (venue) | Overlap | What it already covers | What it lacks relative to us |
|---|---|---|---|---|---|
| 1 | `shams2026layerrag` | LayerRAG-Bench (arXiv, single author, Jul 2026) | **High** | 8 enterprise domains incl. finance/HR; 240 tasks; 9 faults incl. stale index, permission denied, conflicting evidence, schema drift; 2 contract modes (a crossed config factor); strict success requires retrieving required evidence and citing only retrieved evidence; shows groundedness-only scoring gives false positives | No role profiles; permission is a "denied" fault, not a relevant-but-prohibited record that can leak; no prompt-vs-tool enforcement; no release stages or post-release drift; no over-restriction metric; no human coding or mixed models; not peer-reviewed |
| 2 | `vishwakarma2025enterprisebench` | EnterpriseBench (EMNLP 2025) | **High** | Synthetic enterprise sandbox, departmental personas, fragmented sources, access-control hierarchies, tool-using agents | Single configuration; task completion only; no source-appropriateness, claim support or separate boundary metric; no stale/distractor conditions; no stages, drift or enforcement ablation |
| 3 | `fazlija2025accessdenied` | ACCESS DENIED INC (Findings ACL 2025) | **High** on the boundary/refusal outcomes | Clearance-based access over corporate data; refusing unauthorized vs answering legitimate requests (our ABCR + over-restriction pair); coins "sensitivity awareness" | Model-level, no tool-using agent; no source appropriateness or support; no stale sources; no enforcement arm, stages or drift |
| 4 | `palumbo2026policy` | PCAS / Formal Policy Enforcement (arXiv) | Medium-high on H3 | Deterministic reference monitor raises policy compliance from 48% to 93% (v2 abstract) | Customer-service action policies, not data-access permissions; no RAG source metrics; no roles, stages or drift |
| 5 | `uppala2026promptsdontprotect` | Prompts Don't Protect (EMNLP 2026 Industry, accepted) | Medium on H3 | Head-to-head prompt allowlists vs ABAC MCP proxy: 4-68% unauthorized invocations under prompts, 0% by design under proxy | Tool access, not record retrieval and disclosure; no accuracy, support or source metrics; no stages |
| 6 | `huang2026crmarenapro` | CRMArena-Pro (TMLR 2026) | Medium | Business personas; confidentiality awareness near zero, prompting helps at task-success cost (motivates our over-restriction split) | CRM-only; no tool-level arm; no source or support metrics; no stages or drift |
| 7 | `sanyal2026orgaccess` | OrgAccess (EMNLP 2026) | Medium | Prompt-stated RBAC fails as permissions compose; over-cautious "False Partial" answers | No retrieval or tools; no enforcement arm; no source/support metrics |
| 8 | `baek2026leakage` | Singapore/Korea AISI leakage study (REALM 2026) | Medium | Non-adversarial leakage in tool-using agents; "access-boundary awareness" risk type; capability and data-handling safety scored separately | 12 tasks, 3 agents, LLM-judge rubrics; no source conditions, enforcement ablation, stages |
| 9 | `levy2026stwebagentbench` | ST-WebAgentBench (ICLR 2026) | Medium | Completion under Policy well below nominal completion | Web action policies; no permissions over records; no stages |
| 10 | `maiorano2026qualitygate`, `maiorano2026readiness` | Release gate / readiness harness (arXiv, single author) | Medium on the stage axis | PROMOTE/HOLD/ROLLBACK release gate over 20+ releases with evidence coverage; CI gates with policy compliance and groundedness | Longitudinal case study of one proprietary system / model-k matrix; no controlled stage packages, permissions, prohibited sources or enforcement arm |
| 11 | `fu2026ciwork`, `klisura2025rolecond`, `liang2026worksurfacebench`, `arceo2026securing` | CI-Work; Role-Conditioned Refusals; WorkSurface-Bench; Securing the Agent | Medium / low-medium | Enterprise leakage trade-off; prompting vs verifier for SQL RBAC; routing scored separately from answers; retrieval-time ABAC gating | Each covers one or two of our dimensions only |

Not cited: GuardianAgentBench (Naik et al.). A novelty report listed it as an ICML 2026 main-conference paper showing guardrail > system-prompt defenses. The ICML page shows it is a **workshop poster** ("Failure Modes in Agentic AI"), and its author list renders incompletely. I left it out of `references.bib`. If you want it, confirm authors on OpenReview first.

## Hypothesis-level novelty

- **H1 (production > dev/integration on SAR and SuAR): risk of being true by construction.** Stage packages are author-built bundles. If "production" simply adds guardrails, a fresher index and stricter permission sync, H1 is a configuration effect, not a stage effect. **Reposition:** treat each stage as a documented vector of factor settings (prompt version, tool schema, index freshness, permission-sync lag, guardrail layer, logging). Report the per-package deltas in a table, and if budget allows run a leave-one-component-out ablation on a scenario subset so each effect can be attributed to a component.
- **H2 (drift lowers reliability): expected, but the specific form is new.** Injected document and permission drift as a post-release condition, crossed with enforcement mode, has not been studied. LayerRAG-Bench has static stale-index faults, and ReliabilityBench has schema-drift faults; cite both.
- **H3 (tool-level > prompt-only on boundary compliance): confirmatory.** Frame it as quantification and extension: data-record retrieval and disclosure rather than tool invocation, measured jointly with accuracy, support and over-restriction, and checked for persistence across stages and drift. The interesting result is **what remains** under tool-level enforcement (stale-source selection, unsupported claims, over-restriction), and whether enforcement costs answer accuracy.
- **H4 (SuAR < raw accuracy): expected measurement, not a finding.** Prior attribution work (Liu et al. 2023; Trust-Score; Wallat et al. 2025; LayerRAG-Bench) predicts it. The new part is the size of the gap per stage and enforcement mode, and that a relevant-but-prohibited record can make an answer "supported" under standard attribution metrics yet non-compliant under ours.

## Recommended contribution statement (safe wording)

> We present a controlled, fully synthetic study of a single tool-using LLM agent answering business questions for six role profiles (finance, operations, HR, sales, compliance, executive) over CSV tables, JSON API responses and policy documents. In a factorial design, five stage-modelled configuration packages (development, integration, pre-production/UAT, production, and post-release monitoring with injected document and permission drift) are crossed with two permission-enforcement modes (prompt-only policy instructions vs retrieval/tool-level enforcement), for 3,600 runs over 120 scenarios. Prior enterprise benchmarks evaluate role-based access or reliability under stale and denied evidence within a single configuration. We instead score source appropriateness, claim-level evidence support and access-boundary compliance as separate outcomes alongside answer accuracy and refusal correctness, under controlled source conditions that include relevant-but-prohibited records. Mixed-effects models with scenario random effects and double-coded human annotation estimate how configuration package and enforcement mode jointly affect each outcome. Our results quantify, for record retrieval and disclosure, the advantage of enforcement outside the prompt that earlier work reports for tool access and multitenant retrieval, and show which failures remain under it. They also show by how much accuracy-only evaluation overstates reliability when answers must rest on permitted, current evidence. All configurations are simulated; no production system is evaluated.

## Phrases to avoid

- "first benchmark" / "first study" / "to the best of our knowledge, the first" (EnterpriseBench, ACCESS DENIED INC, OrgAccess, LayerRAG-Bench exist). If any priority claim is made, limit it to the exact combination and hedge it.
- "first to evaluate LLM agents across release/deployment stages" (Maiorano 2026a, EDDOps)
- "we show for the first time that tool-level enforcement beats prompt-only" (PCAS, Prompts Don't Protect, Arceo & Narsing, CRMArena-Pro)
- "release stage causes / production improves reliability" (use "stage-modelled configuration packages" and attribute effects to documented package differences)
- "production deployment", "real-world enterprise", "production-grade", "real Copilot" (fully synthetic, simulated packages)
- "novel metric" / "we introduce the access-boundary concept" (say "operationalize"; cite Baek et al. 2026 and attribution work)
- "sensitivity awareness" without citing ACCESS DENIED INC
- "first to show grounded answers differ from correct answers" / "first to model stale or denied-permission sources" (LayerRAG-Bench, Trust-Score, HoH)
- "novel LLMOps/AgentOps lifecycle framework" (EDDOps, AgentOps, readiness harness)
- "guarantees compliance" / "eliminates leakage" (enforcement covers only the record classes it filters)
- "generalizes across LLMs or enterprises" (single agent, synthetic data)
- "comprehensive", "holistic", "unprecedented", "trustworthy agent", "hallucination-free"
- Microsoft 365 Copilot oversharing statistics (only vendor/consultancy figures were found, no peer-reviewed source)

## Design changes suggested by the literature

1. **Unbundle the stage factor.** Publish a per-package delta table and, on a subset, ablate components so H1 is not true by construction (all three novelty reports; harness-variance argument).
2. **Add a second agent model** if budget allows (reviewers will flag single-model generality).
3. **Score boundary violations on retrieval and tool-argument channels, not only the final answer.** AgentLeak shows output-only audits miss 41.7% of violations.
4. **Score access compliance and source choice deterministically from tool logs**; reserve human double-coding (Cohen's kappa, plus per-category kappa or Krippendorff's alpha for the rare-class failure taxonomy) for claim support. If an LLM judge pre-scores support, validate it against the human subset (Bavaresco et al. 2025; Thakur et al. 2025).
5. **Use AIS-style claim decomposition** (Rashkin et al.; FActScore) in the SuAR coding manual, and report RAGAS-style faithfulness only as a secondary automated check, since it would count prohibited-source claims as faithful.
6. **Never score empty answers or refusals as success** unless refusal is correct (ABC checklist, Zhu et al. 2025); report correct refusal and over-restriction as separate rates (XSTest/OR-Bench paired design).
7. **Randomise or log tool-result order**, and make distractor and stale records topically similar to the authoritative one (Lost in the Middle; Power of Noise).
8. **Report pass^k-style or TAR@N run-to-run consistency** per stage alongside means (tau-bench; Atil et al. 2025; Rabanser et al. 2026). Use Wilson or Bayesian intervals for per-cell rates (Bowyer et al. 2025) and clustered or mixed-model inference (Miller 2024).
9. **Balance prohibited-source items across roles** so per-role ABCR estimates are not too noisy (novelty report 2).
10. **Preregister** the four hypotheses, model formula and exclusions before the 3,600 runs (van Miltenburg et al. 2021).
11. **State the synthetic-data limitation explicitly**: absolute rates may not transfer; relative stage and enforcement contrasts are the inferential target (Gill et al. 2025).
12. **Venue fit:** target IRAI track TT04 (AI Safety and Security) with TT01 as fallback, and watch for a successor to the 2026 ReDAS agentic special session (proposals close 31 Mar 2027).
