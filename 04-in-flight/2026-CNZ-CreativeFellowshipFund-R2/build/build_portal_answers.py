"""Regenerate PORTAL-ANSWERS.txt from APPLICATION.md.

The answers are authored once in APPLICATION.md. This script extracts the executive summary and the five
answers, writes the paste-ready text file with the count caption per field, and prints the counts so the
tables in APPLICATION.md, SUBMIT-CHECKLIST.md and the manifest can be kept honest.

Run:  python3 build/build_portal_answers.py
"""
import io
import re
import sys
import textwrap

D = "/opt/data/anamata/funding/applications/2026-CNZ-CreativeFellowshipFund-R2"
SEP = "=" * 78
TITLE = ("Ngā Tono o te Tinana: Somatosensory Composition, Vibrotactile Waiata, and the\n"
         "Decoupling of Sound from Hearing")
HEADER = """CREATIVE NEW ZEALAND: CREATIVE FELLOWSHIP FUND 2026, ROUND 2
Paste-ready answers, plain text, no formatting marks.
Applicant: Ngaika Smith, as an individual. Closes 1:00 PM NZ time, Thursday 24 September 2026.
Funding pool: Ngā Toi Māori. Ask: $50,000, the tier with five questions.

PROJECT TITLE FIELD: {title}
Confirm the reo before typing it in.
"""


def answer_sections() -> dict:
    src = io.open(f"{D}/APPLICATION.md", encoding="utf-8").read()
    body = src.split("\n---\n", 1)[1]
    for marker in ["# CORRECT THESE BEFORE SUBMITTING", "# INTERNAL NOTES"]:
        if marker in body:
            body = body.split(marker)[0]
    parts = {}
    for p in re.split(r"\n(?=#{1,2} )", body):
        head, _, rest = p.partition("\n")
        parts[head.strip()] = rest.strip()
    return parts


def main() -> int:
    parts = answer_sections()
    fields = [("EXECUTIVE SUMMARY (paste first if the form has an intro field)",
               parts["## Executive summary"])]
    for i in range(1, 6):
        h = next(k for k in parts if k.startswith(f"## Question {i}"))
        fields.append((h.lstrip("# ").strip(), parts[h]))

    def rewrap(text: str, width: int = 100) -> str:
        # answers are authored hard wrapped; unwrap then rewrap so edits do not leave ragged short lines
        paras = []
        for para in re.split(r"\n\s*\n", text):
            joined = re.sub(r"\s+", " ", para).strip()
            paras.append(textwrap.fill(joined, width=width) if joined else "")
        return "\n\n".join(paras)

    out = [HEADER.format(title=TITLE), ""]
    counts = []
    for head, raw in fields:
        body = rewrap(raw)
        counts_placeholder = None
        counts.append((len(body), len(body.split())))
        out += [SEP, head, SEP, "", body, "", "---", "",
                f"[{len(body)} characters, {len(body.split())} words]", "", ""]
    io.open(f"{D}/PORTAL-ANSWERS.txt", "w", encoding="utf-8").write("\n".join(out))

    print("PORTAL-ANSWERS.txt written")
    for (head, _b), (c, w) in zip(fields, counts):
        print(f"   {head[:44]:46s} {c:5d} chars  {w:4d} words")
    over = [h for (h, _b), (c, _w) in zip(fields, counts) if c > 2500]
    if over:
        print("OVER 2,500:", over)
    return 0


if __name__ == "__main__":
    sys.exit(main())
