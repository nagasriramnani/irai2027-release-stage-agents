# Paper (IEEEtran, conference mode)

* `main.tex`: the manuscript. Result numbers are **macros** (`\ResSarProdTool`, `\ConHThreeAbcrToolProduction`, ...) defined in
  `generated/results_macros.tex`, which `harness/analyze.py` writes (notebook 04 copies it here with the figure).
  Never type a result number by hand. To switch from pilot to confirmatory results, re-run the analysis on the confirmatory
  logs and copy the two generated files again.
* Red `\pilot{...}` text marks content that depends on pilot data. Before submission, rewrite it and set
  `\renewcommand{\pilot}[1]{#1}`; notebook 07 checks citations, macros, banned over-claiming phrases, and the 6-page / 2 MB limits.
* `references.bib`: the audited literature bibliography plus two verified additions (Qwen3 report, Holm 1979). Only cited
  entries appear in the PDF.

## Build
`IEEEtran.cls` (V1.8b) and `IEEEtran.bst` (v1.12) in this folder are the versions supplied with the IRAI 2027 templates
(`docs/templates/`); local files take precedence over any TeX distribution's copies, so every build uses them.
* Locally (used for the page check): [Tectonic](https://tectonic-typesetting.github.io) 0.17.0, a single self-contained
  executable that fetches the needed packages on first use: `tectonic -X compile main.tex --outdir build` → `build/main.pdf`.
  Notebook 07 runs this automatically when Tectonic is on the PATH or in `~/tools/tectonic/`.
* Overleaf: upload this folder and compile `main.tex` with pdfLaTeX (`\usepackage[T1]{fontenc}` gives the same Type 1 Times
  fonts under both engines).
* Paper size is US Letter (the LaTeX template's default); add the `a4paper` class option if IRAI asks for A4 (the Word template
  it supplies is A4).

## Before submission (docs/CONFERENCE_REQUIREMENTS.md)
6 pages including references · single-blind (author names stay) · PDF ≤ 2 MB · IEEE PDF eXpress check · AI-use disclosure in
the Acknowledgment · fill author affiliations and the repository URL.
