"""Rasterise the rendered PDF so the pages can actually be looked at before delivery."""
import os, sys

PDF = sys.argv[1]
OUT = os.path.join(os.path.dirname(PDF), "build", "pages")
os.makedirs(OUT, exist_ok=True)

import fitz  # pymupdf

doc = fitz.open(PDF)
print("pages:", doc.page_count)
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=110)
    p = f"{OUT}/page-{i+1}.png"
    pix.save(p)
    print(f"  page {i+1}: {pix.width}x{pix.height}  {p}")
# text sanity: catch a heading stranded at the foot of a page
for i, page in enumerate(doc):
    txt = page.get_text().strip().splitlines()
    if txt:
        print(f"  page {i+1} last line: {txt[-1][:80]!r}")
