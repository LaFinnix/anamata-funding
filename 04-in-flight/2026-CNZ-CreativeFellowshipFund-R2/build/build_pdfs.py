"""Rebuild the submission PDFs from the source markdown, reproducibly.

Renders, all through /opt/data/anamata/funding/_tools/md2pdf.py so they share one design system:

1. Application: Sections 1 to 5 only, internal notes stripped.
2. Portal answers: reference copy of the paste-ready text, with counts per field.
3. Accessibility programme evidence: assessor-facing section only.
4. Method annex: the practice brief and the tactile notation, in one document.
"""
import os, re, subprocess, sys

D = "/opt/data/anamata/funding/applications/2026-CNZ-CreativeFellowshipFund-R2"
BUILD = f"{D}/build"
TOOL = "/opt/data/anamata/funding/_tools/md2pdf.py"
SOMA = "/opt/data/anamata/somatosensory"
PY = "/opt/data/.playwright-venv/bin/python"
os.makedirs(BUILD, exist_ok=True)

KICKER = "Creative Fellowship Fund 2026 · Round 2"


def strip_internal(md: str) -> str:
    for marker in ["# CORRECT THESE BEFORE SUBMITTING", "# INTERNAL NOTES, NOT FOR THE ASSESSOR"]:
        if marker in md:
            md = md.split(marker)[0].rstrip()
    return re.sub(r"\n-{3,}\s*$", "", md)


def answer_sections() -> dict:
    """Executive summary plus the five answers, keyed by their heading."""
    src = open(f"{D}/APPLICATION.md", encoding="utf-8").read()
    body = strip_internal(src.split("\n---\n", 1)[1])
    parts = {}
    for p in re.split(r"\n(?=#{1,2} )", body):
        head, _, rest = p.partition("\n")
        parts[head.strip()] = rest.strip()
    return parts


def application_source() -> str:
    parts = answer_sections()
    title = ("Ngā Tono o te Tinana: Somatosensory Composition, Vibrotactile Waiata, and the "
             "Decoupling of Sound from Hearing")
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
                clean = {"TWELVE MONTH RESEARCH TIMELINE AND MILESTONES": "Twelve month research timeline and milestones",
                         "BUDGET ALLOCATION": "Budget allocation",
                         "COLLABORATORS AND SUPPORT NETWORK": "Collaborators and support network"}.get(clean.upper(), clean)
                out += [f"## {clean}", "", parts[k], ""]
    return "\n".join(out)


def portal_answers_source() -> str:
    """Mirror of PORTAL-ANSWERS.txt as a readable document, counts included."""
    txt = open(f"{D}/PORTAL-ANSWERS.txt", encoding="utf-8").read()
    blocks = re.split(r"={70,}\n(.+?)\n={70,}\n", txt)
    fields = []
    i = 1
    while i < len(blocks) - 1:
        head = blocks[i].strip()
        raw = blocks[i + 1]
        # counts are computed from the text that is actually pasted, not read from a caption
        body = re.split(r"\n---\n", raw)[0].strip()
        chars, words = f"{len(body):,}", f"{len(body.split()):,}"
        head = re.sub(r"\s*\(paste first.*?\)$", "", head).strip()
        if head.upper() == "EXECUTIVE SUMMARY":
            head = "Executive summary"
        fields.append((head, body, chars, words))
        i += 2
    out = ["# Portal answers", "",
           "## Reference copy of the paste-ready text, Creative Fellowship Fund 2026, Round 2", "",
           "Paste from this document into the portal fields. The portal sets no published character limit;",
           "the counts below are given so any field that caps can be trimmed deliberately rather than by guess.",
           "", "| Field | Characters | Words |", "|---|---|---|"]
    for head, _body, chars, words in fields:
        out.append(f"| {head} | {chars} | {words} |")
    out.append("")
    for head, body, _chars, _words in fields:
        out += [f"## {head}", "", body, ""]
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


def method_annex_source() -> str:
    def demote(md: str) -> str:
        out, dropped = [], False
        for ln in md.split("\n"):
            if not dropped and ln.startswith("# "):
                dropped = True
                continue
            out.append("#" + ln if ln.startswith("#") else ln)
        return "\n".join(out).strip()

    def audience_ready(md: str) -> str:
        # internal plumbing does not belong in an assessor-facing annex
        md = re.sub(r"/opt/data/\S*/APPLICATION\.md", "the application document", md)
        md = re.sub(r"\n\n(?=\d+\. )", "\n", md)          # keep a numbered list numbered
        return md

    brief = audience_ready(demote(open(f"{SOMA}/PRACTICE-BRIEF.md", encoding="utf-8").read()))
    notation = audience_ready(demote(open(f"{SOMA}/TACTILE-NOTATION.md", encoding="utf-8").read()))
    return "\n".join([
        "# Method annex", "",
        "## Supporting method documentation for the Creative Fellowship Fund 2026, Round 2 application", "",
        "## Practice brief", "", brief, "",
        "## Tactile notation", "", notation, ""])


def render(name: str, md: str, subtitle: str) -> tuple[str, str]:
    src = f"{BUILD}/{name}-source.md"
    pdf = f"{D}/{name}.pdf"
    open(src, "w", encoding="utf-8").write(md)
    env = dict(os.environ, PLAYWRIGHT_BROWSERS_PATH="/opt/hermes/.playwright")
    r = subprocess.run([PY, TOOL, src, "--pdf-out", pdf, "--title", KICKER, "--kicker", KICKER,
                        "--subtitle", subtitle], capture_output=True, text=True, env=env)
    print(r.stdout.strip() or r.stderr.strip()[-400:])
    return src, pdf


if __name__ == "__main__":
    render("CNZ-CreativeFellowship-R2-Somatosensory", application_source(),
           "Application by Ngaika Smith · Ngā Toi Māori pool · September 2026")
    render("CNZ-CreativeFellowship-R2-Portal-Answers", portal_answers_source(),
           "Reference copy of the paste-ready answers · September 2026")
    render("CNZ-CreativeFellowship-R2-Accessibility-Evidence", evidence_source(),
           "Supplementary evidence · accessibility programme · ongoing")
    render("CNZ-CreativeFellowship-R2-Method-Annex", method_annex_source(),
           "Practice brief and tactile notation · supporting method · September 2026")
