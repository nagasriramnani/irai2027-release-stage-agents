"""Word version of the paper, built on the official IRAI A4 Word template.

    python paper/make_docx.py          -> paper/build/main.docx

Text, tables, figure, citation numbers and the reference list come from main.tex, the generated macro files and an
IEEEtran.bst run (Tectonic, intermediates kept in a temporary folder), so every number is the one in the PDF. Styles, page
setup, columns and the numbering of headings, table and figure captions and references come from the template:
docs/templates/conference-template-a4.docx, re-saved by Word as transitional OOXML in paper/template-a4.docx because
python-docx cannot open the Strict original. Inline math is written as Unicode text.
"""
import copy
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from datetime import datetime, timezone

import fitz  # PyMuPDF
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.packuri import PackURI
from docx.opc.part import Part
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, Twips

HERE = Path(__file__).resolve().parent
TEMPLATE, OUT = HERE / "template-a4.docx", HERE / "build/main.docx"


# --- LaTeX source -----------------------------------------------------------------------------------------------------
def group(s, i):
    """Content of the brace group starting at s[i] == '{', and the index after it."""
    assert s[i] == "{", s[i:i + 40]
    depth, j = 0, i
    while j < len(s):
        if s[j] == "\\":
            j += 2  # an escaped character (\{, \}, \\) never opens or closes a group
            continue
        depth += {"{": 1, "}": -1}.get(s[j], 0)
        if depth == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces")


def macros():
    m = {}
    for f in [*sorted((HERE / "generated").glob("*.tex")), HERE / "main.tex"]:
        t = f.read_text(encoding="utf-8")
        for x in re.finditer(r"\\newcommand\{\\(\w+)\}(?!\[)", t):
            m[x.group(1)] = group(t, x.end())[0]
    return m


def expand(t, m):
    out, i = [], 0
    for x in re.finditer(r"\\vs\{", t):  # table marks: * significant with the pre-specified sign, dagger: compatible with SESOI
        a, j = group(t, x.end() - 1)
        b, _ = group(t, j)
        v, s = m[a.strip("\\")], m[b.strip("\\")]
        out += [t[i:x.start()], ("$^{*}$" if v in ("supported", "difference") else "") + ("$^{\\dagger}$" if "compatible" in s else "")]
        i = _
    t = "".join(out) + t[i:]
    for _ in range(4):
        t = re.sub(r"\\([A-Za-z]+)(?:\{\})?", lambda x: m[x.group(1)] if x.group(1) in m else x.group(0), t)
    return t


def latex_run():
    """Citation numbers, labels and the IEEEtran-formatted bibliography from a fresh build."""
    exe = shutil.which("tectonic") or str(Path.home() / "tools/tectonic/tectonic.exe")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([exe, "-X", "compile", "main.tex", "--outdir", tmp, "--keep-intermediates"], cwd=HERE, check=True,
                       capture_output=True)
        aux, bbl = ((Path(tmp) / f"main.{e}").read_text(encoding="utf-8") for e in ("aux", "bbl"))
    cites = {k: int(n) for k, n in re.findall(r"\\bibcite\{([^}]*)\}\{(\d+)\}", aux)}
    labels = dict(re.findall(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", aux))
    items = re.split(r"\\bibitem\{[^}]*\}", bbl.split("\\BIBdecl", 1)[1])[1:]
    refs = []
    for it in items:
        it = it.split("\\end{thebibliography}")[0]
        it = re.sub(r"\\BIBentry(?:ALT|STD)interwordspacing|\\newblock", " ", it)
        it = re.sub(r"\\hskip[^\\]*\\relax", " ", it)
        refs.append(" ".join(it.split()))
    assert len(refs) == len(cites), (len(refs), len(cites))
    return cites, labels, refs


def cite_text(keys, cites):
    """The cite package's output: sorted, runs of three or more compressed to a range."""
    ns, out, i = sorted(cites[k.strip()] for k in keys.split(",")), [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        out += [f"[{ns[i]}]--[{ns[j]}]"] if j - i >= 2 else [f"[{n}]" for n in ns[i:j + 1]]
        i = j + 1
    return ", ".join(out)


def blocks(body):
    """Block list from the document body: (kind, payload)."""
    out = []
    pat = re.compile(r"\\(section\*?|subsection)\{|\\begin\{(table\*?|figure\*?|enumerate|itemize)\}|\\label\{[^}]*\}"
                     r"|\\bibliographystyle\{[^}]*\}|\\bibliography\{[^}]*\}|\n\s*\n")
    i, buf = 0, []

    def flush():
        txt = " ".join("".join(buf).split())
        if txt:
            out.append(("para", txt))
        buf.clear()
    for x in pat.finditer(body):
        if x.start() < i:
            continue
        buf.append(body[i:x.start()])
        i = x.end()
        if x.group(1):
            flush()
            title, i = group(body, x.end() - 1)
            out.append(({"section": "h1", "section*": "h5", "subsection": "h2"}[x.group(1)], title))
        elif x.group(2):
            flush()
            env = x.group(2)
            end = body.index(f"\\end{{{env}}}", i)
            out.append((env.rstrip("*"), (body[i:end], env.endswith("*"))))
            i = end + len(f"\\end{{{env}}}")
        elif x.group(0).strip() == "" or x.group(0).startswith("\\bib"):
            flush()
    buf.append(body[i:])
    flush()
    return out


def table_parts(src):
    cap = group(src, src.index("\\caption{") + 8)[0]
    tab = re.search(r"\\begin\{(tabularx?)\}(?:\{[^}]*\})?\{((?:[^{}]|\{[^{}]*\})*)\}(.*?)\\end\{tabularx?\}", src, re.S)
    note = re.search(r"\\parbox\{\\(?:column|text)width\}\{\\(?:scriptsize|footnotesize)\s*(.*)\}\s*$", src.strip(), re.S)
    rows = []
    for row in re.split(r"\\\\", tab.group(3)):
        row = re.sub(r"\\(?:toprule|midrule|bottomrule)", "", row).strip()
        if row:
            rows.append([c.strip() for c in re.split(r"(?<!\\)&", row)])
    spec = re.sub(r"@\{[^}]*\}|>\{[^}]*\}", "", tab.group(2))  # column alignment as in the LaTeX table
    aligns = [{"c": WD_ALIGN_PARAGRAPH.CENTER, "r": WD_ALIGN_PARAGRAPH.RIGHT}.get(a, WD_ALIGN_PARAGRAPH.LEFT)
              for a in re.findall(r"[lcrX]", spec)]
    assert len(aligns) == len(rows[0]), (spec, rows[0])
    return cap, rows, note.group(1) if note else None, aligns


FONTS = {False: fitz.Font(fontfile=r"C:\Windows\Fonts\times.ttf"), True: fitz.Font(fontfile=r"C:\Windows\Fonts\timesbd.ttf")}


def col_widths(cells, size_pt, avail, pad):
    """Auto table layout: each column's natural width (widest cell on one line, measured in Times New Roman) if they fit;
    otherwise every column keeps its longest word and the remaining space goes to the columns that can wrap."""
    def width(text, bold):
        return FONTS[bold].text_length(text, fontsize=size_pt) * 12700 + pad  # points -> EMU
    nat, word = [], []
    for j in range(len(cells[0])):
        col = [("".join(x for x, _ in c[j]), i == 0) for i, c in enumerate(cells)]
        nat.append(max(width(t, b) for t, b in col))
        word.append(max(width(w, b) for t, b in col for w in (t.split() or [""])))
    if sum(nat) <= avail:
        return [int(n + (avail - sum(nat)) * n / sum(nat)) for n in nat]
    spare, flex = avail - sum(word), [n - w for n, w in zip(nat, word)]
    return [int(w + max(spare, 0) * f / (sum(flex) or 1)) for w, f in zip(word, flex)]


# --- inline conversion (one pandoc call for every snippet) -------------------------------------------------------------
def pandoc_inlines(snippets):
    doc = "\n\n".join(f"{s}" for s in snippets)
    r = subprocess.run(["pandoc", "-f", "latex", "-t", "json"], input=doc.encode("utf-8"), capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode("utf-8", "replace"))
    paras = [b["c"] for b in json.loads(r.stdout.decode("utf-8"))["blocks"]]
    assert len(paras) == len(snippets), (len(paras), len(snippets))
    return paras


# \circ as U+25CB: at table size its ring matches LaTeX's \circ (U+25E6 reads as a dot next to the check marks).
# TeX math spaces are kerns that never break a line, so they become no-break spaces (U+202F narrow, U+00A0).
SYM = {"geq": "≥", "leq": "≤", "subseteq": "⊆", "cap": "∩", "cup": "∪", "emptyset": "∅", "checkmark": "✓", "circ": "○",
       "dagger": "†", "kappa": "κ", "times": "×", "pm": "±", "in": "∈", "ldots": "…", "cdot": "·", "%": "%",
       ",": "\u202f", ":": "\u202f", ";": "\u00a0", "!": "", "quad": "\u00a0\u00a0"}
GREEK = "αβγδελμπρστφχωκ"
SYM.update(dict(zip("alpha beta gamma delta epsilon lambda mu pi rho sigma tau phi chi omega".split(), GREEK)))
REL = set("<>=") | {"≥", "≤", "⊆", "∈"}
BIN = set("−+×±·") | {"∩", "∪"}


def math_runs(tex, fmt):
    """Inline TeX math as runs: italic Latin letters, upright digits, Unicode symbols, super/subscripts."""
    runs, i, toks = [], 0, []
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:])
            toks.append(("sym", SYM.get(m.group(1), m.group(1))))
            i += len(m.group(0))
        elif c in "^_":
            if tex[i + 1] == "{":
                inner, i = group(tex, i + 1)
            else:
                inner, i = tex[i + 1], i + 2
            toks.append(("sup" if c == "^" else "sub", inner))
        elif c in "{} ":
            i += 1
        else:
            toks.append(("chr", "−" if c == "-" else c))
            i += 1
    for k, (kind, v) in enumerate(toks):
        if kind in ("sup", "sub"):
            runs += [(t, {**f, kind: True}) for t, f in math_runs(v, fmt)]
            continue
        italic = (kind == "chr" and v.isalpha() and v.isascii()) or (kind == "sym" and v in GREEK)
        prev = toks[k - 1] if k else None  # a binary operator follows an operand; a sign (unary minus) does not
        after_operand = prev is not None and (prev[0] in ("sup", "sub") or prev[1].isalnum() or prev[1] in ")]")
        spaced = k < len(toks) - 1 and ((v in REL and k > 0) or (v in BIN and after_operand))
        runs.append((f" {v} " if spaced else v, {**fmt, "italic": fmt.get("italic") or italic, "math": True}))
    return runs


def runs_of(inlines, fmt=None):
    fmt, out = fmt or {}, []
    for x in inlines:
        t, c = x["t"], x.get("c")
        if t == "Str":  # pandoc's thin spaces (\, in page numbers and text) are kerns in TeX: keep them unbreakable;
            # Word's no-width non-break (U+200D) after the dash keeps hypothesis ranges (H1--H3, H2a--c) on one line, as \mbox does in LaTeX
            c = re.sub(r"(\bH\d[a-d]?)\u2013(?=[a-dH])", "\\1\u2013\u200d", c.replace("\u2006", "\u202f").replace("\u2009", "\u202f"))
            out.append((c, fmt))
        elif t in ("Space", "SoftBreak"):
            out.append((" ", fmt))
        elif t == "LineBreak":
            out.append(("\n", fmt))
        elif t in ("Emph", "Strong", "Superscript", "Subscript", "SmallCaps"):
            key = {"Emph": "italic", "Strong": "bold", "Superscript": "sup", "Subscript": "sub", "SmallCaps": "smallcaps"}[t]
            out += runs_of(c, {**fmt, key: True})
        elif t == "Code":
            out.append((c[1], {**fmt, "mono": True}))
        elif t == "Quoted":
            q = ("“", "”") if c[0]["t"] == "DoubleQuote" else ("‘", "’")
            out += [(q[0], fmt), *runs_of(c[1], fmt), (q[1], fmt)]
        elif t == "Math":
            out += math_runs(c[1], fmt)
        elif t == "Span":
            out += runs_of(c[1], fmt)
        elif t == "Link":  # a zero-width space after each slash lets Word break long URLs instead of stretching the line
            out += [(re.sub(r"/(?!/)", "/​", x), f) for x, f in runs_of(c[1], fmt)]  # never inside "//"
        elif t == "RawInline":
            raise ValueError(f"unconverted LaTeX: {c}")
        else:
            raise ValueError(f"unhandled inline {t}")
    return out


MATH_FONT = set("∅∪⊆∩")  # not in Times New Roman; Cambria Math ships with Office on every platform


def add_runs(p, runs, size=None):
    for text, f in runs:
        for k, line in enumerate(text.split("\n")):
            if k:
                p.add_run().add_break(WD_BREAK.LINE)
            for part in re.split(r"([✓∅∪⊆∩])", line):
                if part:
                    add_run(p, part, f, size)
    return p


def add_run(p, part, f, size):
    r = p.add_run("" if part == "✓" else part)
    r.italic, r.bold = f.get("italic") or None, f.get("bold") or None
    if f.get("sup"):  # set only when on: assigning None to either clears the run's vertical alignment
        r.font.superscript = True
    if f.get("sub"):
        r.font.subscript = True
    r.font.small_caps = False if f.get("math") else (f.get("smallcaps") or None)  # math keeps its case in small-caps captions
    if size:
        r.font.size = size
    if f.get("mono"):  # same size as the surrounding text, as \texttt in the PDF
        r.font.name = "Courier New"
    if part == "✓":  # Word's own check-mark symbol (Insert > Symbol, Wingdings 252): Times has no check mark
        r._r.append(r._r.makeelement(qn("w:sym"), {qn("w:font"): "Wingdings", qn("w:char"): "F0FC"}))
    elif part in MATH_FONT:
        r.font.name = "Cambria Math"
    return r


# --- document ---------------------------------------------------------------------------------------------------------
def sect(src, cols):
    s = copy.deepcopy(src)
    for e in s.findall(qn("w:footerReference")) + s.findall(qn("w:titlePg")):
        s.remove(e)  # the template's copyright-line placeholder is for the camera-ready version
    c = s.find(qn("w:cols"))
    c.set(qn("w:num"), str(cols))
    if s.find(qn("w:type")) is None:
        t = s.makeelement(qn("w:type"), {qn("w:val"): "continuous"})
        s.insert(0, t)
    return s


def end_section(doc, sectpr):
    p = doc.add_paragraph(style="Normal")
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r = p.add_run()
    r.font.size = Pt(1)
    p._p.get_or_add_pPr().append(sectpr)
    return p


def add_svg(doc, p, svg):
    """Attach a vector (SVG) copy of the picture in paragraph p; Word 2016+ draws and exports it, older readers use the PNG."""
    part = Part(PackURI("/word/media/fig_stage_mode.svg"), "image/svg+xml", svg, doc.part.package)
    rid = doc.part.relate_to(part, RT.IMAGE)
    p._p.xpath(".//a:blip")[0].append(parse_xml(
        '<a:extLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:ext uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}">'
        '<asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" '
        f'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid}"/></a:ext></a:extLst>'))


def clean_package(doc, title, authors):
    """Document properties of this paper, not of the template (its page/word counts, company, edit lock and dates)."""
    cp = doc.core_properties
    cp.title, cp.author, cp.last_modified_by, cp.revision = title, authors, authors, 1
    cp.created = cp.modified = datetime.now(timezone.utc).replace(microsecond=0)
    for rid, rel in list(doc.part.rels.items()):  # the template's copyright footer and sample hyperlinks are not used
        if rel.reltype in (RT.FOOTER, RT.HYPERLINK) and f'"{rid}"' not in doc.element.xml:
            doc.part.drop_rel(rid)
    pkg_rels = doc.part.package.rels
    for rid, rel in list(pkg_rels.items()):  # Word rebuilds app.xml (pages, words) on its next save
        if rel.reltype == RT.EXTENDED_PROPERTIES:
            pkg_rels.pop(rid)


def build():
    m = macros()
    cites, labels, refs = latex_run()
    src = (HERE / "main.tex").read_text(encoding="utf-8")
    pre, body = src.split("\\begin{document}", 1)
    body = body.split("\\end{document}")[0]
    body = re.sub(r"(?<!\\)%.*", "", body)
    body = re.sub(r"\\cite\{([^}]*)\}", lambda x: cite_text(x.group(1), cites), body)
    body = re.sub(r"\\ref\{([^}]*)\}", lambda x: labels[x.group(1)], body)
    body = expand(body, m)

    title = group(body, body.index("\\title{") + 6)[0]
    authors = []
    for x in re.finditer(r"\\IEEEauthorblockN\{", body):
        name, j = group(body, x.end() - 1)
        aff, _ = group(body, body.index("\\IEEEauthorblockA{", j) + 17)
        authors.append((name, [l.strip() for l in re.split(r"\\\\\{\}|\\\\", aff) if l.strip()]))
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S).group(1)
    keywords = re.search(r"\\begin\{IEEEkeywords\}(.*?)\\end\{IEEEkeywords\}", body, re.S).group(1)
    main = body[body.index("\\end{IEEEkeywords}") + len("\\end{IEEEkeywords}"):]
    bl = blocks(main)
    # Word cannot float a table to the top of a column as LaTeX's [t] does, so Table I follows the paragraph that ends near
    # the top of page 2 (the template asks for tables at the top or bottom of columns). Re-check after large text changes.
    for label, anchor in {"tab:related": r"\textbf{Enterprise agent benchmarks.}"}.items():
        blk = bl.pop(next(k for k, (kind, pay) in enumerate(bl) if kind == "table" and f"\\label{{{label}}}" in pay[0]))
        bl.insert(1 + next(k for k, (kind, pay) in enumerate(bl) if kind == "para" and pay.startswith(anchor)), blk)

    # every inline snippet, converted in one pandoc call
    snippets = [title, *(l for name, ls in authors for l in [name, *ls]), abstract.strip(), keywords.strip(), *refs]
    for kind, pay in bl:
        if kind in ("para", "h1", "h2", "h5"):
            snippets.append(pay)
        elif kind in ("enumerate", "itemize"):
            snippets += [" ".join(s.split()) for s in pay[0].split("\\item")[1:]]
        elif kind == "table":
            cap, rows, note, _ = table_parts(pay[0])
            snippets += [cap, *(c or "~" for r in rows for c in r)] + ([note] if note else [])
        elif kind == "figure":
            snippets.append(group(pay[0], pay[0].index("\\caption{") + 8)[0])
    conv = iter(pandoc_inlines([" ".join(s.split()) for s in snippets]))
    nxt = lambda: runs_of(next(conv))  # noqa: E731

    doc = Document(TEMPLATE)
    tb = doc.element.body
    sps = tb.xpath(".//w:sectPr")
    s_title, s_two = sps[0], sps[3]
    for el in list(tb):
        if el.tag != qn("w:sectPr"):
            tb.remove(el)
    tb.replace(tb.find(qn("w:sectPr")), sect(s_two, 2))
    text_w = doc.sections[-1].page_width - doc.sections[-1].left_margin - doc.sections[-1].right_margin

    add_runs(doc.add_paragraph(style="paper title"), nxt())
    # author blocks side by side in a borderless one-row table: unlike balanced columns, the blocks stay level everywhere
    ta = doc.add_table(rows=1, cols=len(authors))
    ta.alignment, ta.autofit = 1, False
    nil = ta._tbl.tblPr.makeelement(qn("w:tblBorders"), {})
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        nil.append(nil.makeelement(qn(f"w:{side}"), {qn("w:val"): "nil"}))
    ta._tbl.tblPr.append(nil)
    for cell, (name, lines) in zip(ta.rows[0].cells, authors):
        cell.width = text_w // len(authors)
        p = cell.paragraphs[0]
        p.style = doc.styles["Author"]
        p.paragraph_format.space_after = Pt(18)  # gap before the abstract, as in the LaTeX title block
        add_runs(p, nxt())
        for _ in lines:
            p.add_run().add_break(WD_BREAK.LINE)
            add_runs(p, nxt())
    first = sect(s_title, 1)
    first.remove(first.find(qn("w:type")))  # the first section starts the document
    end_section(doc, first)

    p = doc.add_paragraph(style="Abstract")
    p.add_run("Abstract").italic = True
    p.add_run("—")
    add_runs(p, nxt())
    p = doc.add_paragraph(style="Keywords")
    p.add_run("Keywords—")
    add_runs(p, nxt())

    ref_runs = [nxt() for _ in refs]
    for kind, pay in bl:
        if kind in ("h1", "h2", "h5"):
            add_runs(doc.add_paragraph(style={"h1": "Heading 1", "h2": "Heading 2", "h5": "Heading 5"}[kind]), nxt())
        elif kind == "para":
            add_runs(doc.add_paragraph(style="Body Text"), nxt())
        elif kind == "itemize":
            for _ in pay[0].split("\\item")[1:]:
                add_runs(doc.add_paragraph(style="bullet list"), nxt())
        elif kind == "enumerate":
            for k, _ in enumerate(pay[0].split("\\item")[1:], start=1):  # hanging indent: wrapped lines align with the text
                p = add_runs(doc.add_paragraph(style="Body Text"), [(f"{k})\t", {})] + nxt())
                p.paragraph_format.left_indent, p.paragraph_format.first_line_indent = Twips(288), -Twips(288)  # = Body Text's tab stop
        elif kind == "table":
            cap, rows, note, aligns = table_parts(pay[0])
            wide = pay[1]
            if wide:
                end_section(doc, sect(s_two, 2))
            add_runs(doc.add_paragraph(style="table head"), nxt()).paragraph_format.keep_with_next = True
            cells = [[nxt() for _ in r] for r in rows]
            size = Pt(7) if "\\scriptsize" in pay[0].split("\\begin{tabular")[0] else Pt(8)  # as in the LaTeX table
            t = doc.add_table(rows=len(rows), cols=len(rows[0]))
            t.autofit = False
            tpr = t._tbl.tblPr
            borders = tpr.makeelement(qn("w:tblBorders"), {})
            for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
                borders.append(borders.makeelement(qn(f"w:{side}"), {qn("w:val"): "single", qn("w:sz"): "2", qn("w:space"): "0",
                                                                     qn("w:color"): "auto"}))
            tpr.append(borders)
            mar = tpr.makeelement(qn("w:tblCellMar"), {})
            for side in ("left", "right"):
                mar.append(mar.makeelement(qn(f"w:{side}"), {qn("w:w"): "45", qn("w:type"): "dxa"}))
            tpr.append(mar)
            t.alignment = 1
            avail = text_w if wide else (text_w - Cm(0.635)) // 2
            widths = col_widths(cells, size.pt, avail, pad=2 * 45 * 635 + Pt(2))  # cell margins (45 twips a side) + slack
            for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
                gc.set(qn("w:w"), str(w // 635))  # EMU -> twips
            for i, row in enumerate(cells):
                for j, rr in enumerate(row):
                    cell = t.cell(i, j)
                    cell.width = widths[j]
                    para = cell.paragraphs[0]
                    para.style = doc.styles["table col head" if i == 0 else "table copy"]
                    para.alignment = aligns[j]
                    para.paragraph_format.keep_with_next = i < len(cells) - 1 or bool(note)  # the table stays in one piece
                    add_runs(para, [(x, f) for x, f in rr if x != "\u00a0" or len(rr) > 1], size)
                tr = t.rows[i]._tr.get_or_add_trPr()
                tr.append(tr.makeelement(qn("w:cantSplit"), {}))
            if note:  # the style's automatic footnote letter is switched off: the notes carry their own marks
                fp = add_runs(doc.add_paragraph(style="table footnote"), nxt(), size)  # the note's size equals the table's
                num = fp._p.get_or_add_pPr().makeelement(qn("w:numPr"), {})
                for tag in ("w:ilvl", "w:numId"):
                    num.append(num.makeelement(qn(tag), {qn("w:val"): "0"}))
                fp._p.get_or_add_pPr().insert(1, num)
                fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            if wide:
                end_section(doc, sect(s_two, 1))
        elif kind == "figure":
            src_fig = re.search(r"\\includegraphics\[width=([\d.]+)\\textwidth\]\{([^}]*)\}", pay[0])
            png = Path(tempfile.gettempdir()) / "irai_fig.png"
            fitz.open(HERE / src_fig.group(2))[0].get_pixmap(dpi=600).save(png)
            end_section(doc, sect(s_two, 2))
            p = doc.add_paragraph(style="Normal")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = True  # the caption never leaves the figure
            p.add_run().add_picture(str(png), width=int(text_w * float(src_fig.group(1))))
            add_svg(doc, p, fitz.open(HERE / src_fig.group(2))[0].get_svg_image(text_as_path=True).encode("utf-8"))
            add_runs(doc.add_paragraph(style="figure caption"), nxt())
            end_section(doc, sect(s_two, 1))
    add_runs(doc.add_paragraph(style="Heading 5"), [("References", {})])
    for rr in ref_runs:
        add_runs(doc.add_paragraph(style="references"), rr)
    end_section(doc, sect(s_two, 2))  # a continuous break after the last reference balances the last page's columns
    end_para = doc.add_paragraph(style="Normal")
    end_para.paragraph_format.space_before = end_para.paragraph_format.space_after = Pt(0)
    end_para.add_run().font.size = Pt(1)
    assert next(conv, None) is None, "unused converted snippets"
    OUT.parent.mkdir(exist_ok=True)
    clean_package(doc, "".join(x for x, _ in runs_of(pandoc_inlines([title])[0])), ", ".join(n for n, _ in authors))
    doc.save(OUT)
    print(f"wrote {OUT.relative_to(HERE.parent)}: {len(bl)} blocks, {len(refs)} references, {len(doc.tables)} tables")


if __name__ == "__main__":
    build()
