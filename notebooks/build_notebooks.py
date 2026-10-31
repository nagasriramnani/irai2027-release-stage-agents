"""Build the reproducibility notebooks (run from the repository root):  python notebooks/build_notebooks.py
Then execute them in order:  jupyter nbconvert --to notebook --execute --inplace notebooks/0*.ipynb
"""
from pathlib import Path

import nbformat as nbf

HERE = Path(__file__).parent
SETUP = '''import sys, json, subprocess
from pathlib import Path
ROOT = Path.cwd().resolve().parent if Path.cwd().name == "notebooks" else Path.cwd().resolve()
sys.path[:0] = [str(ROOT / "harness"), str(ROOT / "benchmark")]
import pandas as pd
from IPython.display import Markdown, Image, display
pd.set_option("display.max_colwidth", 120)
print("repository root:", ROOT)'''


def nb(cells):
    book = nbf.v4.new_notebook()
    book.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    book.cells = [nbf.v4.new_markdown_cell(c[3:]) if c.startswith("md:") else nbf.v4.new_code_cell(c) for c in cells]
    return book


NOTEBOOKS = {
"00_setup_and_overview.ipynb": [
"""md:# 00 · Setup and overview
**Paper:** *Release-Stage Effects on AI Agent Answer Reliability Across Business Simulation Profiles* (target: IEEE IRAI 2027).

This notebook checks the environment. Run the notebooks in order; each one states what it verifies.

| Notebook | What it does | Needs Ollama? | Runtime |
|---|---|---|---|
| 01 | Regenerates the synthetic benchmark and checks it reproduces the frozen SHA-256 content hashes | no | < 1 min |
| 02 | Validates the scorer with scripted agents and worked examples (assertions) | no | ~1 min |
| 03 | Runs or loads the pilot; **re-scores every logged run from its trace** and checks it matches | only if `RUN_AGENT=True` | 1 min (load) / ≈ 9 h (run) |
| 04 | Pilot analysis: rates, contrasts, models, ablation, figure, paper macros | no | ~2 min |
| 05 | Simulation-based power analysis for the confirmatory design | no | ~10-20 min |
| 06 | Literature review: bibliography integrity, comparison matrix, novelty assessment | no | < 1 min |
| 07 | Paper consistency checks: citations resolve, numbers come from the analysis, banned phrases absent | no | < 1 min |
""",
SETUP,
'''import platform, importlib
print("python", platform.python_version())
for pkg in ["numpy", "pandas", "scipy", "statsmodels", "matplotlib", "tabulate", "nbformat"]:
    print(f"{pkg:12s}", importlib.import_module(pkg).__version__)
print()
print(open(ROOT / "requirements.txt").read())''',
'''# Optional: the local model server is only needed to RE-RUN the agent (notebook 03 with RUN_AGENT=True).
import urllib.request
try:
    tags = json.loads(urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3).read())
    models = [m["name"] for m in tags["models"]]
    print("Ollama is running. Models:", models)
    print("qwen3:8b available:", any(m.startswith("qwen3:8b") for m in models))
except Exception as e:
    print("Ollama not reachable (fine unless you want to re-run agents):", e)''',
'''import shutil
# list what the repository holds: skip files git ignores (local notes, build output, caches)
ignored = set(subprocess.run(["git", "ls-files", "-oi", "--exclude-standard", "--directory"], cwd=ROOT, capture_output=True,
                             text=True).stdout.splitlines()) if shutil.which("git") else set()
def tree(p, depth=0, max_depth=2):
    for c in sorted(p.iterdir(), key=lambda c: c.name.lower()):
        if c.name.startswith((".", "__")) or c.relative_to(ROOT).as_posix() + ("/" if c.is_dir() else "") in ignored:
            continue
        print("    " * depth + ("📁 " if c.is_dir() else "   ") + c.name)
        if c.is_dir() and depth < max_depth - 1 and c.name not in ("data",):
            tree(c, depth + 1, max_depth)
tree(ROOT)''',
],
"01_benchmark_generation.ipynb": [
"""md:# 01 · Benchmark generation and integrity
The benchmark is **fully synthetic and deterministic**. `benchmark/generate.py` builds two self-contained splits from fixed seeds:

* `dev` (seed 1027, 30 items) — harness/prompt tuning and the pilot;
* `confirmatory` (seed 2027, 120 items) — frozen; never used for tuning.

Each split has `sources.json`, `items.jsonl` (the query registry with gold answers), `stages/*.json` (the five release-stage
configuration packages), `fault_map.json`, and `MANIFEST.json` with SHA-256 hashes.
**Check 1:** regenerating from the seeds reproduces the frozen hashes exactly.""",
SETUP,
'''import generate
frozen = {s: json.loads((ROOT / "benchmark/data" / s / "MANIFEST.json").read_text()) for s in ("dev", "confirmatory")}
for split, seed, per_cell in [("dev", 1027, 0), ("confirmatory", 2027, 1)]:
    generate.write_split(split, seed, per_cell)
    now = json.loads((ROOT / "benchmark/data" / split / "MANIFEST.json").read_text())
    assert now == frozen[split], f"{split}: regenerated benchmark differs from the frozen manifest"
    print(f"{split:13s} items {now['items_sha256'][:16]}…  sources {now['sources_sha256'][:16]}…  -> identical to frozen ✔")''',
'''items = pd.DataFrame([json.loads(l) for l in (ROOT / "benchmark/data/confirmatory/items.jsonl").read_text().splitlines()])
print("confirmatory items:", len(items))
display(pd.crosstab(items.profile, items.task_class, margins=True))
display(pd.crosstab(items.task_class, items.condition, margins=True))
display(pd.crosstab(items.condition, items.format).rename_axis("condition x format (counterbalanced)"))
display(items.groupby("condition")[["prohibited_cue", "distractor_type"]].agg(lambda s: s.dropna().value_counts().to_dict()))''',
'''# v1.2 design checks: no cue outside the design
src = pd.DataFrame(json.loads((ROOT / "benchmark/data/confirmatory/sources.json").read_text())).set_index("id")
forb = [(r.profile, s) for r in items.itertuples() for s in r.confounders.get("prohibited", [])]
print("forbidden records whose catalog owner is the asking role:", sum(src.loc[s, "domain"] == p for p, s in forb), "of", len(forb))
pairs = src[src.status.isin(["current", "superseded"])].groupby("title").filter(lambda g: set(g.status) >= {"current", "superseded"})
lower = pairs.groupby("title").apply(lambda g: g[g.status == "current"].index.min() < g[g.status == "superseded"].index.min())
print("version pairs where the current version has the lower id:", int(lower.sum()), "of", len(lower), "(random permutation)")
pos = [list(src.loc[r.authoritative_sources[0], "values"]).index(r.evidence_keys[0]) for r in items.itertuples() if r.task_class == "lookup"]
print("row position of the looked-up entity:", pd.Series(pos).value_counts().sort_index().to_dict())''',
"""md:## Example items (one per task class)
`gold_value` is computed from the synthetic source, so gold labels need no manual annotation. Restricted items have no
permitted source and the correct action is to refuse.""",
'''cols = ["item_id", "profile", "condition", "question", "gold_value", "unit", "authoritative_sources", "confounders"]
display(items.groupby("task_class").head(1)[["task_class"] + cols])''',
'''sources = {s["id"]: s for s in json.loads((ROOT / "benchmark/data/confirmatory/sources.json").read_text())}
it = items[(items.condition == "stale") & (items.task_class == "lookup")].iloc[0]
for sid in it.authoritative_sources + it.confounders["stale"]:
    s = sources[sid]
    print(f"--- {sid} [{s['kind']}] {s['title']}  (version {s['version']}, as_of {s['as_of']}, {s['status']}, {s['classification']})")
    print(s["content"][:400], "\\n")''',
"""md:## The five release-stage configuration packages
Stage comparisons estimate the effect of the **whole package**. The table lists what each package changes; the
leave-one-component-out ablation (notebook 04) decomposes the development–production gap.""",
'''rows = []
for st in ["development", "integration", "preproduction", "production", "postrelease"]:
    c = json.loads((ROOT / f"benchmark/data/confirmatory/stages/{st}.json").read_text())
    rows.append(dict(stage=st, prompt=c["prompt_version"], metadata=", ".join(c["metadata_fields"][3:]) or "id/title/class only",
                     missing_sources=len(c["index_exclude"]), added_sources=len(c["index_add"]), old_version_served=len(c["read_redirect"]),
                     json_connector_faults=len(c["transient_faults"]), policy_classes=len(c["policy"]["class_rules"]),
                     wrong_denies=len(c["policy"]["source_overrides"]), reclassified=len(c["reclassified"]),
                     gold_changed=len(c["gold_overrides"])))
display(pd.DataFrame(rows).set_index("stage"))
print("fault map:", {k: len(v) for k, v in json.loads((ROOT / "benchmark/data/confirmatory/fault_map.json").read_text()).items()})''',
'''from env import Env
for st in ["development", "production"]:
    print(f"===== system prompt, finance role, {st} =====")
    print(Env(ROOT / "benchmark/data/confirmatory", st, "prompt", "finance").system_prompt(), "\\n")''',
],
"02_scorer_validation.ipynb": [
"""md:# 02 · Scorer validation
All outcomes are scored **deterministically from tool traces** by `harness/score.py`. Definitions are frozen in
`protocol/PROTOCOL.md` §5. This notebook (a) prints the definitions, (b) runs scripted reference agents whose correct scores
are known, and (c) walks through three hand-built cases, including the rule that a *blocked attempt is not a breach*.""",
SETUP,
'''import score, run
print(score.__doc__)''',
"""md:## Scripted reference agents
* `oracle` knows the gold answer and reads only the authoritative source → must score perfectly in production, track
  post-release drift, and never breach the boundary.
* `naive` reads the top two search hits whatever their classification → must breach in prompt-only mode and must be fully
  blocked by complete tool-level enforcement.""",
'''run.selfcheck()''',
"""md:## Worked examples""",
'''from env import Env
from score import score_run
split = ROOT / "benchmark/data/dev"
items = [json.loads(l) for l in (split / "items.jsonl").read_text().splitlines()]
restricted = next(i for i in items if i["task_class"] == "restricted")
forbidden = restricted["confounders"]["prohibited"][0]

# (a) tool-level enforcement: the agent TRIES to read the forbidden source -> ACCESS_DENIED -> blocked attempt, ABCR holds
env = Env(split, "production", "tool", restricted["profile"])
print(env.read_source(forbidden))
a = score_run(restricted, env, {"answer": "I am not permitted to access that information.", "citations": [], "refused": True})
print({k: a[k] for k in ("abcr", "blocked_attempts", "refusal_correct", "label")})
assert a["abcr"] and a["blocked_attempts"] == 1 and a["label"] == "ok_refusal"

# (b) prompt-only: the same read SUCCEEDS -> the forbidden record reached the agent -> ABCR fails even if it then refuses
env = Env(split, "production", "prompt", restricted["profile"])
env.read_source(forbidden)
b = score_run(restricted, env, {"answer": "I cannot share this.", "citations": [], "refused": True})
print({k: b[k] for k in ("abcr", "forbidden_read", "label")})
assert not b["abcr"] and b["label"] == "policy_violation"''',
'''# (c) a correct number with no citation is correct but NOT supported (the gap behind H5)
look = next(i for i in items if i["task_class"] == "lookup")
env = Env(split, "production", "tool", look["profile"])
env.read_source(look["authoritative_sources"][0])
c = score_run(look, env, {"answer": f"{look['gold_value']}", "citations": [], "refused": False})
print({k: c[k] for k in ("correct", "supported", "sar", "label")})
assert c["correct"] and not c["supported"] and c["label"] == "unsupported_correct"
print("all worked examples behave as specified ✔")''',
],
"03_pilot_experiment.ipynb": [
"""md:# 03 · Pilot experiment (development split)
**Design (benchmark v1.3):** 30 dev items × 5 stage packages × 2 enforcement modes × 2 repetitions = 600 runs, plus a
leave-one-component-out ablation (production with one component — prompt, metadata, snapshot or policy from development;
the same four plus connectors from integration) × 2 modes × 1 repetition = 540 runs, plus the secondary model
(`llama3.1-tools:8b` = Llama-3.1-8B with a chat template that keeps the tool definitions visible, built locally by
`ollama create llama3.1-tools:8b -f harness/llama3.1-tools.Modelfile`; production, development, post-release × 2 modes ×
1 repetition = 180 runs). Model `qwen3:8b` (local Ollama),
temperature 0.7, top-p 0.8, thinking off, ≤ 10 steps; decoding seed = SHA-256(item, repetition), shared by paired cells. Runs
are resumable; infrastructure errors are retried (≤ 3 attempts).

The **observable-ideal** reference agent (scripted; protocol §4.3) is re-run here every time, on the dev split and on the
confirmatory split (3 repetitions; this fixes the confirmatory fault-free stratum used by the power analysis — no LLM touches
the confirmatory split). By default the LLM runs are **loaded**; set `RUN_AGENT = True` to run them (≈ 9 h on an 8 GB GPU: 3.4 h main, 4.7 h ablation, 0.5 h Llama, from the logged run
times). The runner resumes, skipping every run already in a log, so move the three LLM logs aside first to re-run from scratch.""",
SETUP,
'''import run
RUN_AGENT = False
MAIN, ABL = ROOT / "pilot/runs_dev_qwen3-8b.jsonl", ROOT / "pilot/runs_dev_ablation_qwen3-8b.jsonl"
LLAMA = ROOT / "pilot/runs_dev_llama3.1-8b.jsonl"
IDEAL, ABL_IDEAL = ROOT / "pilot/runs_dev_ideal.jsonl", ROOT / "pilot/runs_dev_ablation_ideal.jsonl"
CONF_IDEAL = ROOT / "pilot/runs_confirmatory_ideal.jsonl"
SWAPS = ([f"production~{c}@development" for c in ("prompt", "metadata", "snapshot", "policy")]
         + [f"production~{c}@integration" for c in ("prompt", "metadata", "snapshot", "connectors", "policy")])
# The observable-ideal reference agent is scripted (seconds, no GPU): always (re)run it so it matches the frozen data.
for p in (IDEAL, ABL_IDEAL, CONF_IDEAL):
    p.unlink(missing_ok=True)
run.run("dev", "ideal", 2, IDEAL)
run.run("dev", "ideal", 1, ABL_IDEAL, stages=SWAPS)
run.run("confirmatory", "ideal", 3, CONF_IDEAL)
if RUN_AGENT:
    run.run("dev", "ollama", 2, MAIN)
    run.run("dev", "ollama", 1, ABL, stages=SWAPS)
    run.run("dev", "ollama", 1, LLAMA, stages=["production", "development", "postrelease"], model="llama3.1-tools:8b")''',
'''logs = {p.name: [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        for p in (MAIN, ABL, LLAMA, IDEAL, ABL_IDEAL, CONF_IDEAL) if p.exists()}
for name, rows in logs.items():
    df = pd.DataFrame(rows)
    print(f"{name}: {len(df)} runs, {df.item_id.nunique()} items, duplicates: {df.run_id.duplicated().sum()}, "
          f"infrastructure errors: {sum('error' in r['result'] for r in rows)}, unsubmitted: {sum(bool(r['result'].get('unsubmitted')) for r in rows)}")
    display(df.groupby(["stage", "mode"]).size().unstack().rename_axis(None))''',
"""md:## Independent re-scoring
Every run log stores the full tool trace. Here each run is **re-scored from scratch** with the current scorer and compared
field by field with the logged scores. Zero mismatches means the reported numbers follow from the raw traces.""",
'''from env import Env
from score import score_run
splits = {s: ROOT / "benchmark/data" / s for s in ("dev", "confirmatory")}
items_of = {s: {i["item_id"]: i for i in map(json.loads, (d / "items.jsonl").read_text().splitlines())} for s, d in splits.items()}
item_by_id = items_of["dev"]
fields = ["gold_action", "reachable", "unreachable_reason", "refused", "substantive", "correct", "hedged", "sar", "supported",
          "supported_cond", "abcr", "exposed", "abcr_exposed", "blocked_attempts", "forbidden_read", "forbidden_cited", "disclosed",
          "deployed_violation", "refusal_correct", "over_restriction", "drift_exposed", "label"]
mismatch = 0
for name, rows in logs.items():
    s = "confirmatory" if "confirmatory" in name else "dev"
    for r in rows:
        env = Env(splits[s], r["stage"], r["mode"], r["profile"], r["seed"])
        env.trace = r["trace"]
        new = score_run(items_of[s][r["item_id"]], env, r["result"])
        mismatch += any(new[f] != r[f] for f in fields)
print(f"re-scored {sum(map(len, logs.values()))} runs; mismatches: {mismatch}")
assert mismatch == 0''',
"""md:## Example transcripts
One run per failure type, to show what the labels mean in practice.""",
'''df = pd.DataFrame(logs.get(MAIN.name, []))
for label in ["stale_source", "policy_violation", "unwarranted_refusal", "unsupported_correct", "ok"]:
    ex = df[df.label == label].head(1)
    if ex.empty:
        continue
    r = ex.iloc[0]
    print(f"===== {label}: {r.run_id} =====\\nQ: {item_by_id[r.item_id]['question']}")
    for t in r.trace:
        print("  ", t["tool"], t.get("query") or t.get("id"), t.get("outcome", ""))
    print("  answer:", str(r.result.get("answer"))[:200], "| cites:", r.result.get("citations"), "| refused:", r.result.get("refused"), "\\n")''',
],
"04_pilot_analysis.ipynb": [
"""md:# 04 · Pilot analysis
Runs `harness/analyze.py` on the pilot logs: item-cluster bootstrap 95% CIs, the preregistered contrasts (fault-free
stratum for H1/H2a/b, every exposed scenario for H2c, Holm, directional verdicts), the v1.1 DiD and GEE / mixed logit as
secondary, run-to-run consistency (pass^k), failure taxonomy, the H5 gate test, the leave-one-component-out ablation, the
paper figure, and `results_macros.tex` (every number quoted in the paper). The secondary model (Llama-3.1-8B) is analysed
the same way into `pilot/analysis_llama/`.

*These are pilot results on the development split; they inform the power analysis and harness fixes. Confirmatory claims
will come only from the frozen 120-item split.*""",
SETUP,
'''import analyze, shutil
OUT = ROOT / "pilot/analysis"
P = ROOT / "pilot"
sys.argv = ["analyze.py", str(P / "runs_dev_qwen3-8b.jsonl"), "--ideal", str(P / "runs_dev_ideal.jsonl"), "--outdir", str(OUT),
            "--ablation", str(P / "runs_dev_ablation_qwen3-8b.jsonl"), "--ablation-ideal", str(P / "runs_dev_ablation_ideal.jsonl"),
            "--confirm-ideal", str(P / "runs_confirmatory_ideal.jsonl"), "--power"]
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    analyze.main()
display(Markdown((OUT / "REPORT.md").read_text(encoding="utf-8")))''',
'''# secondary model: same analysis (contrasts involving integration/pre-production are absent by design)
if (P / "runs_dev_llama3.1-8b.jsonl").exists():
    sys.argv = ["analyze.py", str(P / "runs_dev_llama3.1-8b.jsonl"), "--ideal", str(P / "runs_dev_ideal.jsonl"),
                "--outdir", str(P / "analysis_llama"), "--prefix", "Llama"]   # macros \\LlamaCon..., beside Qwen3's
    with contextlib.redirect_stdout(io.StringIO()):
        analyze.main()
    display(pd.read_csv(P / "analysis_llama/contrasts.csv"))''',
'''display(Image(str(OUT / "fig_stage_mode.png")))
for src, f in [(OUT, "fig_stage_mode.pdf"), (OUT, "results_macros.tex")]:      # hand the paper exactly these generated files
    shutil.copy(src / f, ROOT / "paper/generated" / f)
if (P / "analysis_llama/results_macros.tex").exists():
    shutil.copy(P / "analysis_llama/results_macros.tex", ROOT / "paper/generated/results_macros_llama.tex")
print("copied figure and macros to paper/generated/")''',
],
"05_power_analysis.ipynb": [
"""md:# 05 · Directional resampling power
Protocol §9: power on the **binary run scale** for each of the 9 preregistered contrasts. Each simulated study draws the number
of eligible confirmatory scenarios (counted on the frozen reference-agent runs of the confirmatory split: fault-free stratum for
H1/H2a/b, drift-exposed scenarios for H2c) from the pilot's eligible scenarios with their agent rate in the reference package,
moves each rate toward the boundary so that the mean shift equals a preregistered smallest effect of interest (5 or 10 points)
**in the expected direction**, draws 3 repetitions x 2 modes (or x packages) of binary runs, and tests at the strictest Holm
threshold (alpha = .05/9); only rejections with the expected sign count (H3b: either sign). NaN = not estimable from the pilot
(too few scenarios, or a pilot rate that leaves no room for the effect).
Decision rule: if power at 10 points is < .80 for any H1 contrast or for H3a, add scenarios before confirmatory runs.

**Sensitivity (v1.3a).** The simulation spreads the effect evenly over scenarios. The pilot's stage effects sat in a few
scenarios, so `power_*_pilotsd` recomputes power with a noncentral t using the pilot's own SD of the item differences. If the
two disagree, the decision is the authors' (protocol §9): add scenarios, or keep 120 and treat null H1/H2 verdicts as
inconclusive.""",
SETUP,
'''import analyze
df = analyze.load(ROOT / "pilot/runs_dev_qwen3-8b.jsonl")
ideal = analyze.load(ROOT / "pilot/runs_dev_ideal.jsonl")
conf = analyze.load(ROOT / "pilot/runs_confirmatory_ideal.jsonl")
power = analyze.power(df, ideal, conf)
power.to_csv(ROOT / "pilot/analysis/power.csv", index=False)
display(power)
rule = power[((power.hyp == "H1") | ((power.hyp == "H3") & (power.outcome == "ABCR"))) & ~(power.power_10pt >= 0.8)]
print("Decision rule (protocol §9): H1/H3a contrasts below .80 power at 10 points:",
      rule[["hyp", "outcome", "contrast", "power_10pt"]].values.tolist() or "none")
sens = power[((power.hyp == "H1") | ((power.hyp == "H3") & (power.outcome == "ABCR"))) & ~(power.power_10pt_pilotsd >= 0.8)]
print("Same rule with the pilot's item SD (sensitivity):",
      sens[["hyp", "outcome", "contrast", "power_10pt_pilotsd"]].round(2).values.tolist() or "none")''',
],
"06_literature_review.ipynb": [
"""md:# 06 · Literature review
Built by a documented search (`literature/search_log.md`): nine topic sweeps, an adversarial citation audit of every entry
against its source page, and three independent novelty challenges. This notebook checks bibliography integrity and shows the
comparison matrix and novelty verdict.""",
SETUP,
'''import re
bib = (ROOT / "literature/references.bib").read_text(encoding="utf-8")
entries = re.findall(r"@(\\w+)\\s*\\{\\s*([^,\\s]+)\\s*,(.*?)(?=\\n@|\\Z)", bib, re.S)
keys = [k for _, k, _ in entries]
titles = [re.sub(r"\\W+", " ", (re.search(r"title\\s*=\\s*[{\\"](.+?)[}\\"],?\\s*\\n", b, re.S) or [None, ""])[1]).lower().strip()
          for _, _, b in entries]
print("entries:", len(entries), "| types:", pd.Series([t.lower() for t, _, _ in entries]).value_counts().to_dict())
dups = pd.Series(keys)[pd.Series(keys).duplicated()].tolist()
dup_titles = pd.Series(titles)[pd.Series(titles).duplicated() & (pd.Series(titles) != "")].tolist()
print("duplicate keys:", dups, "| duplicate titles:", dup_titles)
no_url = [k for (_, k, b) in entries if not re.search(r"(url|doi|howpublished|eprint)\\s*=", b, re.I)]
print("entries without url/doi:", len(no_url), no_url[:10])
assert not dups''',
'''display(pd.read_csv(ROOT / "literature/related_work_matrix.csv"))''',
'''display(Markdown((ROOT / "literature/novelty_assessment.md").read_text(encoding="utf-8")))''',
],
"07_paper_consistency_checks.ipynb": [
"""md:# 07 · Paper consistency checks
Pre-submission checks on `paper/`: every `\\cite` key resolves in the bibliography, every result macro used in the text is
generated by the analysis, the figure exists, and phrases flagged by the novelty review (e.g. unsupported "first" claims) are
absent.""",
SETUP,
'''import re, hashlib
tex ="\\n".join(p.read_text(encoding="utf-8") for p in sorted((ROOT / "paper").glob("*.tex")))
body = re.sub(r"(?<!\\\\)%.*", "", tex)
bibkeys = set(re.findall(r"@\\w+\\s*\\{\\s*([^,\\s]+)\\s*,", (ROOT / "paper/references.bib").read_text(encoding="utf-8")))
cited = {k.strip() for g in re.findall(r"\\\\cite\\w*\\{([^}]*)\\}", body) for k in g.split(",")}
missing = sorted(cited - bibkeys)
print(f"cited keys: {len(cited)}; missing from references.bib: {missing}")
# the paper's macro files must be byte-identical to the analysis output, and name the intended runs and model
gen = {"results_macros.tex": (ROOT / "pilot/analysis/results_macros.tex", "qwen3:8b"),
       "results_macros_llama.tex": (ROOT / "pilot/analysis_llama/results_macros.tex", "llama3.1-tools:8b")}
defined = set()
for name, (src, model) in gen.items():
    f = ROOT / "paper/generated" / name
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    assert text == src.read_text(encoding="utf-8"), f"paper/generated/{name} is stale: re-run notebook 04"
    assert model in text.splitlines()[0], f"{name} was generated from another model: {text.splitlines()[0]}"
    m = re.search(r"from (\\S+) \\(sha256 ([0-9a-f]{64})\\)", text.splitlines()[0])   # provenance: the run log's raw bytes
    assert m and hashlib.sha256((ROOT / "pilot" / m[1]).read_bytes()).hexdigest() == m[2], f"{name}: its run log changed after the macros were generated"
    print(text.splitlines()[0])
    defined |= set(re.findall(r"\\\\newcommand\\{\\\\(\\w+)\\}", text))
used = set(re.findall(r"\\\\((?:Res|Con|Ideal|HFive|Gate|Abl|Pow|Uat|Post|Llama|N)[A-Z]\\w*)", body))
print(f"result macros used: {len(used)}; undefined: {sorted(used - defined)}")
banned = [r"\\bthe first\\b", r"\\bfirst (?:study|benchmark|work)\\b", r"to the best of our knowledge", r"\\bguarantee", r"\\bunprecedented\\b",
          r"\\bproduction-grade\\b", r"\\bhallucination-free\\b", r"\\bholistic\\b"]
hits = {b: len(re.findall(b, body, re.I)) for b in banned if re.search(b, body, re.I)}
print("banned phrases found:", hits or "none")
labels = set(re.findall(r"\\\\label\\{((?:fig|tab):[^}]*)\\}", body))
unref = labels - set(re.findall(r"\\\\ref\\{([^}]*)\\}", body))
print("figure/table labels never referenced:", sorted(unref) or "none")
left = re.findall(r"\\\\pilot\\{|\\[(?:RESULT|Interpretation|Restate|Dominant|Department|City|email|First name|repository URL)", body)
print(f"draft markers still present (must be 0 before submission): {len(left)}")
assert not missing and not (used - defined) and not hits and not unref''',
'''import shutil, subprocess
tectonic = shutil.which("tectonic") or next((str(p) for p in (Path.home() / "tools/tectonic" / n for n in ("tectonic.exe", "tectonic"))
                                             if p.exists()), None)
if tectonic:  # builds with the conference's IEEEtran.cls / IEEEtran.bst copied into paper/
    r = subprocess.run([tectonic, "-X", "compile", "main.tex", "--outdir", "build"], cwd=ROOT / "paper", capture_output=True, text=True)
    print("tectonic:", "ok" if r.returncode == 0 else r.stderr[-800:])
else:
    print("Tectonic not found: checking the committed PDF, not a fresh build")
pdf = next((p for p in (ROOT / "paper/build/main.pdf", ROOT / "paper/main.pdf") if p.exists()), None)
if pdf:
    from pypdf import PdfReader          # counts pages correctly even with compressed object streams
    rd = PdfReader(pdf)
    fonts = {str(v.get_object().get("/Subtype")) for p in rd.pages for v in ((p.get("/Resources") or {}).get("/Font") or {}).values()}
    box = rd.pages[0].mediabox
    print(f"{pdf.relative_to(ROOT)}: {len(rd.pages)} pages, {pdf.stat().st_size / 1e6:.2f} MB, page {float(box.width) / 72:.1f} x "
          f"{float(box.height) / 72:.1f} in, font types {sorted(fonts)} (limits: 6 pages, 2 MB, no Type 3)")
    assert len(rd.pages) <= 6 and pdf.stat().st_size < 2e6 and "/Type3" not in fonts
else:
    print("PDF not built: install Tectonic or compile paper/main.tex on Overleaf (see paper/README.md)")''',
],
}

if __name__ == "__main__":
    for name, cells in NOTEBOOKS.items():
        nbf.write(nb(cells), HERE / name)
        print("wrote", name)
