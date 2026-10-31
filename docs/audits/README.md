# Audit and review records

Reports from the adversarial checks run on this project, kept so that every change to the instrument, analysis or paper can
be traced to the finding that caused it (protocol §10 logs the resulting deviations).

| Date | Report | Outcome |
|---|---|---|
| 2026-10-31 | [Pilot artifact audit](2026-10-31_pilot_artifact_audit.md) | No scorer/data defect; Llama chat template hid the tools (re-run); ablation repetition mismatch fixed; results reworded by mechanism (v1.3a) |
| 2026-10-31 | [Analysis changes review](2026-10-31_analysis_changes_review.md) | 0 numeric mismatches; reference agent seed-matched for 1-rep models; chance-correct relevance filter; raw-p macros |
| 2026-10-31 | [Paper review](2026-10-31_paper_review.md) | Abstract re-centred on the measured behaviour; pre-specified (not preregistered) wording; sign-flip robustness check; Methods define the three policies and the ablation |

Earlier design and pilot audits (v1.1-v1.3) are summarised in protocol §10 and `pilot/discarded/README.md`.

## Open items for the authors
* Register the protocol (e.g. OSF) before any confirmatory run, then cite it in the paper.
* Decide on the §9 power question: add scenarios, or keep 120 and treat null stage verdicts as inconclusive.
* Fill in affiliations, e-mails and the repository URL; confirm the AI-use acknowledgment.
