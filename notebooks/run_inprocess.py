"""Execute notebooks in-process with IPython and save their outputs, without a Jupyter kernel.

Use this only where `jupyter nbconvert --execute` cannot start a kernel (e.g. a broken libzmq install, as on the machine
these results were produced on). On a healthy setup prefer:  jupyter nbconvert --to notebook --execute --inplace notebooks/0*.ipynb

    python notebooks/run_inprocess.py notebooks/00_setup_and_overview.ipynb [more.ipynb ...]
"""
import glob
import os
import sys
from pathlib import Path

import nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
from nbformat.v4 import new_output


def execute(path):
    path, cwd = Path(path).resolve(), os.getcwd()
    nb = nbformat.read(path, as_version=4)
    InteractiveShell.clear_instance()
    shell = InteractiveShell.instance()
    os.chdir(path.parent)
    try:
        return _run(shell, nb, path)
    finally:
        os.chdir(cwd)


def _run(shell, nb, path):
    count, failed = 0, False
    for cell in (c for c in nb.cells if c.cell_type == "code"):
        if failed:
            cell.outputs, cell.execution_count = [], None
            continue
        count += 1
        with capture_output() as cap:
            res = shell.run_cell(cell.source, store_history=True)
        outs = [new_output("stream", name=n, text=t) for n, t in (("stdout", cap.stdout), ("stderr", cap.stderr)) if t]
        outs += [new_output("display_data", data=o.data, metadata=o.metadata) for o in cap.outputs]
        if res.result is not None:
            data, meta = shell.display_formatter.format(res.result)
            outs.append(new_output("execute_result", data=data, metadata=meta, execution_count=count))
        if not res.success:
            e = res.error_in_exec or res.error_before_exec
            outs.append(new_output("error", ename=type(e).__name__, evalue=str(e), traceback=[]))
            failed = True
        cell.outputs, cell.execution_count = outs, count
    nbformat.write(nb, path)
    return not failed


if __name__ == "__main__":
    ok = True
    for p in [q for a in sys.argv[1:] for q in (sorted(glob.glob(a)) or [a])]:  # PowerShell/cmd pass wildcards unexpanded
        good = execute(p)
        ok &= good
        print(f"{'OK  ' if good else 'FAIL'} {p}")
    sys.exit(0 if ok else 1)
