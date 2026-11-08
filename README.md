# Release-Stage Effects on AI Agent Answer Reliability

**Working title:** *Release-Stage Effects on AI Agent Answer Reliability Across Business Simulation Profiles: Source
Appropriateness, Answer Support, and Access-Boundary Compliance*
**Authors:** Ram Kochetti, Prof. Hussain Tazar · **Target:** IEEE IRAI 2027 (6 pages, deadline 30 Jun 2027; see
[docs/CONFERENCE_REQUIREMENTS.md](docs/CONFERENCE_REQUIREMENTS.md))

We study how a tool-using LLM agent's answers change across five release-stage configuration packages (development,
integration, pre-production, production, post-release with drift) and two permission-enforcement modes (prompt-only vs
tool-level), on a fully synthetic enterprise benchmark with six business roles. Outcomes: **SAR** (source appropriateness),
**SuAR** (supported-answer rate), **ABCR** (access-boundary compliance), accuracy, and refusal behaviour.

> Everything here is synthetic and local: fictional company, people, and values; local models via Ollama (`qwen3:8b`, plus
> `llama3.1-tools:8b` for the replication); no employer systems, no real data, and no cloud resources.

## Status 
| Milestone | Status |
|---|---|
| Protocol / pre-registration | v1.3a signed by both authors (31 Oct 2026); **v1.4** adopted the same day before any confirmatory LLM run (six blocks, H6, SESOI classes; frozen as tag `prereg-v1.4`) → [protocol/PROTOCOL.md](protocol/PROTOCOL.md) |
| Literature search and novelty check | Done: 136 verified references, novelty **not pre-empted** (narrow) → [literature/](literature/) |
| Adversarial design review (v1.1) | Done: 5 lenses, 56 confirmed findings, all critical/major ones fixed (protocol §10) |
| Adversarial pilot-artifact audit (v1.2-v1.3) | Done: 6 lenses, 49 findings (28 upheld), then two checks of the fixes (19 and 10 findings); all fixed or logged (protocol §10). Stopping rule adopted |
| Benchmark (dev 30 + confirmatory 120 items) | v1.3: counterbalanced (pairwise-balance asserted), no cues outside the design, hash-frozen → [benchmark/](benchmark/) |
| Harness, scorer, analysis | Built and self-checked (incl. observable-ideal reference agent) → [harness/](harness/) |
| Pilot (dev split; Qwen3 600 + 540 ablation, Llama-3.1 180) | Done (v1.3 data, v1.3a analysis); all runs re-score identically → [pilot/analysis/REPORT.md](pilot/analysis/REPORT.md), `pilot/analysis_llama/` |
| Adversarial audit of the pilot results (v1.3a) | Done: 8 agents (one setup defect: Llama's chat template hid the tools, re-run), then a 3-lens check of the analysis changes (0 numeric mismatches) |
| Paper draft (IEEEtran, conference template 6/27/2024) | Compiles locally with Tectonic; results filled from macros → [paper/](paper/) |
| Confirmatory blocks (v1.4) | Six frozen blocks of the 120-cell design (720 scenarios; seed rule in `benchmark/data/GENERATION_LOG.md`); reference agent run on every block before any LLM run → `runs/confirmatory/ideal_*.jsonl` |
| Confirmatory campaign (14,400 + 144 H6 + 2,160 ablation + 4,320 Llama + 72 Llama H6) | Done 8 Nov 2026 (21,096 runs; 1 excluded under §6); analysed in notebook 08, post hoc in notebook 09 → `runs/confirmatory/analysis*/` |
| Human audit of the scorer (§8) | Sample drawn 8 Nov 2026 before any coding (720 runs + 72 re-codes). Not completed: the author hand-coded 15 runs (spot check, reported in the paper); the other rows were tool-filled and are not used (protocol §10) → [human_audit/README.md](human_audit/README.md) |

## Reproduce and verify, in order
```bash
pip install -r requirements.txt          # Python 3.13; Ollama + `ollama pull qwen3:8b` only needed to re-run agents
ollama pull llama3.1:8b                  # optional: secondary-model replication, then:
ollama create llama3.1-tools:8b -f harness/llama3.1-tools.Modelfile   # same weights; keeps tool definitions visible
python notebooks/build_notebooks.py      # (re)creates the notebooks from one script
jupyter nbconvert --to notebook --execute --inplace notebooks/0*.ipynb
```
If Jupyter kernels cannot start on your machine (broken `libzmq`, the case on the machine that produced these results), run
`python notebooks/run_inprocess.py notebooks/0*.ipynb` instead. It executes the same cells in-process and saves the outputs.

Models as used (`ollama list` IDs, both Q4_K_M): `qwen3:8b` 500a1f067a9f, `llama3.1:8b` 46e0c10c039e, from which
`llama3.1-tools:8b` 528696a4274c is built. A different ID after pulling means different weights.

**What a re-run changes.** The check is `git diff --exit-code --ignore-cr-at-eol paper/generated/*.tex pilot/analysis*/*.csv`:
every number in the paper must come out unchanged. `git status` will still list the re-executed notebooks (outputs), the
recompiled `paper/build/main.pdf` (date), and the reference-agent logs `pilot/runs_*_ideal.jsonl` (wall-clock `seconds` only).
Files are stored byte for byte (`.gitattributes`); on Linux or macOS the regenerated files differ only in line endings (and the
figure's font, if Times New Roman is not installed).

| Notebook | Verifies |
|---|---|
| [00_setup_and_overview](notebooks/00_setup_and_overview.ipynb) | environment, package versions, optional Ollama check |
| [01_benchmark_generation](notebooks/01_benchmark_generation.ipynb) | regenerating from seeds reproduces the frozen SHA-256 manifest exactly; design balance; stage packages |
| [02_scorer_validation](notebooks/02_scorer_validation.ipynb) | scorer behaves as specified (oracle/naive agents + worked cases; assertions) |
| [03_pilot_experiment](notebooks/03_pilot_experiment.ipynb) | run counts and integrity; **every run re-scored from its raw trace = logged scores** |
| [04_pilot_analysis](notebooks/04_pilot_analysis.ipynb) | all tables, contrasts, models, ablation, figure, and the paper's numeric macros |
| [05_power_analysis](notebooks/05_power_analysis.ipynb) | simulation-based power for the confirmatory design |
| [06_literature_review](notebooks/06_literature_review.ipynb) | bibliography integrity, comparison matrix, novelty verdict |
| [07_paper_consistency_checks](notebooks/07_paper_consistency_checks.ipynb) | citations resolve, paper numbers come from the analysis, no over-claiming phrases, page/size limits |
| [08_confirmatory_analysis](notebooks/08_confirmatory_analysis.ipynb) | campaign counts; once complete, re-scores every confirmatory run and runs the pooled, Llama and block-1 analyses |

**Confirmatory campaign (protocol v1.4).** `python harness/campaign.py --reference` (scripted, seconds; already done and
frozen), then `python harness/campaign.py` (Ollama with `qwen3:8b` and `llama3.1-tools:8b`; ~5 days on an 8 GB laptop GPU).
After any interruption run the same command again: finished runs are skipped, and the script waits while the model server is
down. Keep the laptop on mains power; Windows Update and Ollama auto-updates should be paused for the duration.

Command-line equivalents (notebooks 03 and 04 hold the exact calls, including the reference agent and the Llama analysis;
an existing `--out` log is resumed, so runs already in it are skipped): `python harness/run.py --selfcheck`
· `python harness/run.py --split dev --agent ollama --reps 2 --out pilot/runs_dev_qwen3-8b.jsonl`
· ablation: `python harness/run.py --split dev --agent ollama --reps 1 --out pilot/runs_dev_ablation_qwen3-8b.jsonl --stages
production~prompt@development,production~metadata@development,production~snapshot@development,production~policy@development,production~prompt@integration,production~metadata@integration,production~snapshot@integration,production~connectors@integration,production~policy@integration`
· `python harness/run.py --split dev --agent ollama --model llama3.1-tools:8b --stages production,development,postrelease --out pilot/runs_dev_llama3.1-8b.jsonl`
· `python harness/analyze.py pilot/runs_dev_qwen3-8b.jsonl --ideal pilot/runs_dev_ideal.jsonl --ablation pilot/runs_dev_ablation_qwen3-8b.jsonl --ablation-ideal pilot/runs_dev_ablation_ideal.jsonl --confirm-ideal runs/confirmatory/ideal_confirmatory*.jsonl --power --outdir pilot/analysis`
  (power for the v1.4 design: the frozen reference runs of all six blocks, 2 repetitions; on PowerShell list the six files)
· paper: `tectonic -X compile paper/main.tex --outdir paper/build` (see [paper/README.md](paper/README.md))

## Repository layout
```
docs/                  conference requirements, templates/ (official IEEE conference LaTeX + Word
                       templates and IEEEtran BibTeX style as supplied for IRAI 2027), audits/ (adversarial audit and
                       review reports, with the open author items)
protocol/PROTOCOL.md   pre-registration: RQs, hypotheses, measures, exclusions, analysis plan, deviations log
literature/            search_log.md · references.bib (136, audited) · related_work_matrix.csv · novelty_assessment.md
                       related_work.tex / related_work_table.tex (draft section and comparison table)
benchmark/
  generate.py          deterministic generator (all synthetic); data/<split>/{items.jsonl, sources.json, stages/*.json,
                       fault_map.json, intended_policy.json, MANIFEST.json}; splits: dev, confirmatory (block 1),
                       confirmatory_b2..b6 (v1.4 blocks), GENERATION_LOG.md (block seed rule)
harness/
  env.py               tools (search_sources, read_source, submit_answer), access policy, stage prompts, component swaps
  score.py             frozen outcome definitions (SAR, SuAR, ABCR, accuracy, refusal, failure taxonomy)
  run.py               agents (Ollama; scripted oracle, naive, observable-ideal), resumable runner with retries, self-check
  campaign.py          the confirmatory campaign (v1.4): every phase in order, resumable, counts only until complete
  analyze.py           cluster-bootstrap rates, agent-attributable contrasts + Holm, gate decisions (H5), GEE + mixed logit,
                       pass^k, ablation, resampling power, figure, LaTeX macros
  posthoc.py           post-hoc analyses of the confirmatory results (labelled post hoc; macros prefix Ph; notebook 09)
  audit.py             human audit (§8): seeded sample and blinded coding sheets (draw), kappa vs the scorer (compare)
human_audit/           coding guide (README.md), case booklets and code sheets for rounds 1 and 2, key/ (not opened while coding)
pilot/                 runs_*.jsonl (full traces + transcripts), runs_confirmatory_ideal.jsonl (scripted reference agent on the
                       confirmatory split; fixes the fault-free stratum), analysis/ and analysis_llama/ (REPORT.md, CSVs, figure,
                       macros), discarded/ (every superseded run set with the reason, kept for transparency)
runs/confirmatory/     confirmatory run logs (one per model, block and arm), frozen reference-agent logs, campaign.log;
                       analysis*/ written by notebook 08 once the campaign is complete
notebooks/             00-08 re-runnable notebooks, build_notebooks.py, run_inprocess.py
paper/                 main.tex (IEEEtran conference), IEEEtran.cls + IEEEtran.bst (conference-supplied versions),
                       references.bib, generated/ (figure + results_macros.tex from 04), build/ (local PDF)
```

## Key design decisions (and why)
* **Gold answers are computed, not annotated.** Values are drawn from seeds, so every gold answer, stage-specific gold
  (drift), and confounder answer is exact. Human coding is reserved for claim support (protocol §8).
* **Blocked attempt ≠ breach.** ABCR fails only if forbidden content reaches the agent, is cited, or is disclosed;
  `ACCESS_DENIED` attempts are counted separately.
* **Stage = package, and faults are separated from behaviour.** Packages inject faults by design, so even a perfect agent
  shows stage gaps (the scripted observable-ideal agent reaches only .72 accuracy in development vs 1.00 in production).
  H1/H2 therefore test the *agent-attributable* effect: the agent's package difference on the scenarios the scripted
  reference agent solves in both packages (frozen on the confirmatory split before any LLM run). The v1.1 difference-in-
  differences is kept as a secondary estimate (it is attenuated when a fault and an agent error hit the same scenario). A
  leave-one-component-out ablation (production with one component from development or integration) locates each gap.
* **Only cues the design intends.** Audits found and removed cues outside the design: ID order, list order, the catalog
  owner showing the asker's own role, evidence always in the first rows, draft markers. The self-check asserts the fixes.
* **Separation-safe, item-clustered inference.** Tool-level ABCR sits at 100% in complete-policy packages (a design invariant,
  not a hypothesis), which breaks logistic models; the 9 preregistered contrasts use scenario-cluster bootstrap CIs with Holm
  correction; GEE and mixed logit are secondary. Every interval is clustered on scenarios.
* **Counterbalanced benchmark.** Format, calculation type, distractor type, gold position, prohibited class and a restriction
  cue (title vs label only) are balanced against source condition, so condition effects are not format effects.
* **Search ties are randomized per run.** Two versions of a source share a title; ties are broken by a seeded hash, never by
  id order (a bias found and fixed during the pilot; see `pilot/discarded/README.md`).

## AI-assistance disclosure
Benchmark code, harness, analysis, literature search, and draft text were produced with an AI assistant co-pilot under the
authors' direction and must be reviewed by both authors. IEEE requires disclosing this in the paper's Acknowledgments.
