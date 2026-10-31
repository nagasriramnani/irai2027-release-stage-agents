"""Confirmatory campaign (protocol v1.4 §4 and §6): every phase in order, resumable. After any interruption, run the same
command again; finished runs are skipped. It prints run counts and infrastructure errors only: no outcome is shown, computed
or summarized before the whole campaign is complete (interim-look rule).

  python harness/campaign.py --reference   # scripted reference agent on every block (before any LLM run; seconds)
  python harness/campaign.py               # the LLM phases (~5 days on an 8 GB laptop GPU)
  python harness/campaign.py --status      # counts per log, no outcomes
  python harness/campaign.py --dry-run     # every LLM phase with the scripted naive agent, into pilot/_selfcheck/dry/
"""
import argparse
import ctypes
import json
import sys
import time
import urllib.request
from datetime import datetime

from run import OLLAMA, ROOT, confirmatory_splits, run

OUT = ROOT / "runs" / "confirmatory"
SWAPS = ([f"production~{c}@development" for c in ("prompt", "metadata", "snapshot", "policy")]
         + [f"production~{c}@integration" for c in ("prompt", "metadata", "snapshot", "connectors", "policy")])
QWEN, LLAMA = "qwen3:8b", "llama3.1-tools:8b"
H6 = dict(stages=["postrelease~labels"], modes=["prompt"], only="drift_perm")  # the labels-synced arm


def llm_phases():
    """Qwen3: per block the main design (2 reps), then its H6 arm; the block-1 ablation; Llama on every block, then its H6 arm."""
    blocks = confirmatory_splits()
    for s in blocks:
        yield f"qwen3-8b_{s}", dict(split=s, reps=2, model=QWEN)
        yield f"qwen3-8b_h6_{s}", dict(split=s, reps=2, model=QWEN, **H6)
    yield "qwen3-8b_ablation_confirmatory", dict(split="confirmatory", reps=1, stages=SWAPS, model=QWEN)
    for s in blocks:
        yield f"llama3.1-8b_{s}", dict(split=s, reps=1, stages=["production", "development", "postrelease"], model=LLAMA)
        yield f"llama3.1-8b_h6_{s}", dict(split=s, reps=1, model=LLAMA, **H6)


def reference_phases():
    for s in confirmatory_splits():
        yield f"ideal_{s}", dict(split=s, reps=2)
    yield "ideal_ablation_confirmatory", dict(split="confirmatory", reps=1, stages=SWAPS)


def expected(kw):
    d = ROOT / "benchmark" / "data" / kw["split"]
    items = [json.loads(l)["item_id"] for l in (d / "items.jsonl").read_text().splitlines() if l.strip()]
    if kw.get("only"):
        items = json.loads((d / "fault_map.json").read_text())[kw["only"]]
    return len(items) * len(kw.get("stages", ["development", "integration", "preproduction", "production", "postrelease"])) \
        * len(kw.get("modes", ["prompt", "tool"])) * kw["reps"]


def counts(path):
    """Distinct runs logged, runs finished (no error, or 3 attempts used), and runs whose last attempt failed."""
    last, tries = {}, {}
    for l in (path.read_text().splitlines() if path.exists() else []):
        try:
            r = json.loads(l)
        except json.JSONDecodeError:
            continue
        last[r["run_id"]], tries[r["run_id"]] = r, tries.get(r["run_id"], 0) + 1
    err = {k for k, r in last.items() if "error" in r["result"]}
    return len(last), sum(1 for k in last if k not in err or tries[k] >= 3), len(err)


def log(msg, out=OUT):
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
    print(line, flush=True)
    with (out / "campaign.log").open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def server_up():
    try:
        urllib.request.urlopen(OLLAMA.replace("/api/chat", "/api/version"), timeout=10)
        return True
    except Exception:
        return False


def unload(model):  # one model on the 8 GB GPU at a time
    req = urllib.request.Request(OLLAMA.replace("/api/chat", "/api/generate"), method="POST",
                                 data=json.dumps({"model": model, "keep_alive": 0}).encode())
    try:
        urllib.request.urlopen(req, timeout=60).read()
    except Exception:
        pass


def execute(phases, agent, out):
    out.mkdir(parents=True, exist_ok=True)
    loaded = None
    for name, kw in phases:
        path, want = out / f"{name}.jsonl", expected(kw)
        strikes = 0
        while counts(path)[1] < want:
            if agent == "ollama":
                if not server_up():  # never spend attempts while the server is down
                    log(f"{name}: Ollama not reachable, waiting 5 min", out)
                    time.sleep(300)
                    continue
                if loaded and loaded != kw["model"]:
                    unload(loaded)
                loaded = kw["model"]
            log(f"{name}: {counts(path)[1]}/{want} runs done, starting", out)
            n0, _, e0 = counts(path)
            try:
                run(kw["split"], agent, kw["reps"], path, **{k: v for k, v in kw.items() if k not in ("split", "reps")})
            except (SystemExit, Exception) as e:  # circuit breaker or connection loss: wait, then resume
                n1, _, e1 = counts(path)
                strikes = strikes + 1 if n1 - e1 == n0 - e0 else 0  # no new successful run since the last stop
                if agent == "ollama" and strikes >= 2:  # the server answers but inference fails: stop before runs use attempt 3
                    log(f"{name}: two stops in a row with no successful run while the server answers ({str(e)[:200]}); "
                        "campaign halted for inspection; re-run this command once inference works", out)
                    sys.exit(1)
                log(f"{name}: stopped ({str(e)[:200]}); retrying in 5 min", out)
                time.sleep(300)
        n, done, err = counts(path)
        log(f"{name}: complete, {done}/{want} runs ({err} with an unresolved infrastructure error)", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--reference", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.status:
        for name, kw in [*reference_phases(), *llm_phases()]:
            n, done, err = counts(OUT / f"{name}.jsonl")
            print(f"{name:38s} {done:5d}/{expected(kw):5d} done, {err} unresolved errors")
        sys.exit()
    if sys.platform == "win32":  # keep the PC awake while this process runs (released when it exits)
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
        import msvcrt  # one campaign process at a time: a second one would append to the same logs
        OUT.mkdir(parents=True, exist_ok=True)
        LOCK = open(OUT / "campaign.lock", "w")
        try:
            msvcrt.locking(LOCK.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            sys.exit("another campaign process is running")
    if a.reference:
        execute(reference_phases(), "ideal", OUT)
    elif a.dry_run:
        execute([(n, {**kw, "model": None}) for n, kw in llm_phases()], "naive", ROOT / "pilot" / "_selfcheck" / "dry")
    else:
        execute(llm_phases(), "ollama", OUT)
