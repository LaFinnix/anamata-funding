"""Rebuild the submission PDFs from the source markdown, reproducibly.

1. Application: Sections 1 to 5 only, internal notes stripped.
2. Accessibility programme evidence: assessor-facing section only.

Both render through /opt/data/anamata/funding/_tools/md2pdf.py so they share the design system.
"""
import os, re, subprocess, sys

D = "/opt/data/anamata/funding/applications/2026-CNZ-CreativeFellowshipFund-R2"
BUILD = f"{D}/build"
TOOL = "/opt/data/anamata/funding/_tools/md2pdf.py"
PY = "/opt/data/.playwright-venv/bin/python"
os.makedirs(BUILD, exist_ok=True)


def strip_internal(md: str) -> str:
    for marker in ["# CORRECT THESE BEFORE SUBMITTING", "# INTERNAL NOTES, NOT FOR THE ASSESSOR"]:
        if marker in md:
            md = md.split(marker)[0].rstrip()
    return re.sub(r"\n-{3,}\s*$", "", md)


def application_source() -> str:
    src = open(f"{D}/APPLICATION.md", encoding="utf-8").read()
    body = strip_internal(src.split("\n---\n", 1)[1])
    title = ("Ngā Tono o te Tinana: Somatosensory Composition, Vibrotactile Waiata, and the "
             "Decoupling of Sound from Hearing")
    parts = {}
    for p in re.split(r"\n(?=#{1,2} )", body):
        head, _, rest = p.partition("\n")
        parts[head.strip()] = rest.strip()
    out = [f"# {title}", "",
           "## Application to Creative New Zealand, Creative Fellowship Fund 2026, Round 2", "",
           "## At a glance", "",
           "| | |", "|---|---|",
           "| Applicant | Ngaika Smith, applying as an individual |",
           "| Practice | Composer and producer, trading as Anamata Records, a trading brand of Anamata Kāhui Limited |",
           "| Whakapapa | Ngāi Tahu, Ngāti Kahungunu, Ngāti Awa |",
           "| Ask | $50,000, twelve month tenure |",
           "| Pool | Ngā Toi Māori, with a multidisciplinary panel fit |",
           "| Activity window | 2 December 2026 to 31 December 2027 |",
           "| Results due | 2 December 2026 |", ""]
    out += ["## Executive summary", "", parts["## Executive summary"], ""]
    for i in range(1, 6):
        h = next(k for k in parts if k.startswith(f"## Question {i}"))
        out += [f"## {h.lstrip('# ').strip()}", "", parts[h], ""]
    for sec in ["SECTION 3", "SECTION 4", "SECTION 5"]:
        for k in parts:
            if k.startswith(f"# {sec}"):
                clean = re.sub(r"^#\s*SECTION \d+:\s*", "", k).strip()
                clean = {"Twelve Month Research Timeline And Milestones": "Twelve month research timeline and milestones",
                         "Budget Allocation": "Budget allocation",
                         "Collaborators And Support Network": "Collaborators and support network"}.get(clean, clean)
                out += [f"## {clean}", "", parts[k], ""]
    return "\n".join(out)


def evidence_source() -> str:
    src = open(f"{D}/ACCESSIBILITY-PROGRAMME-EVIDENCE.md", encoding="utf-8").read()
    body = strip_internal(src)
    assert body.startswith("# Accessibility programme evidence")
    body = body.replace(
        "# Accessibility programme evidence\n",
        "# Accessibility programme evidence\n\n"
        "## Supplementary evidence for the Creative Fellowship Fund 2026, Round 2 application\n", 1)
    return body


def render(name: str, md: str, kicker: str, subtitle: str) -> tuple[str, str]:
    src = f"{BUILD}/{name}-source.md"
    pdf = f"{D}/{name}.pdf"
    open(src, "w", encoding="utf-8").write(md)
    env = dict(os.environ, PLAYWRIGHT_BROWSERS_PATH="/opt/hermes/.playwright")
    r = subprocess.run([PY, TOOL, src, "--pdf-out", pdf, "--title", kicker, "--kicker", kicker,
                        "--subtitle", subtitle], capture_output=True, text=True, env=env)
    print(r.stdout.strip() or r.stderr.strip()[-400:])
    return src, pdf


render("CNZ-CreativeFellowship-R2-Somatosensory", application_source(),
       "Creative Fellowship Fund 2026 · Round 2",
       "Application by Ngaika Smith · Ngā Toi Māori pool · September 2026")
render("CNZ-CreativeFellowship-R2-Accessibility-Evidence", evidence_source(),
       "Creative Fellowship Fund 2026 · Round 2",
       "Supplementary evidence · accessibility programme · 21 September 2026")
