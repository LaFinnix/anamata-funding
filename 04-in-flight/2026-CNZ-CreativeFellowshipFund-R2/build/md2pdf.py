"""Convert a markdown document to a styled HTML file and a print-ready A4 PDF.

Usage:
    /opt/data/.playwright-venv/bin/python md2pdf.py <input.md> [--pdf-out PATH]
                                                     [--title "Letterhead title"]
                                                     [--kicker "Right-hand kicker"]
                                                     [--subtitle "Italic line under the title"]

Design system: shares the Anamata funding document styling (Liberation Serif body,
kōkōwai #9E2A2B accents, booktabs tables, page numbers in the footer).

Covers the markdown subset used in this workspace: ATX headings, paragraphs,
pipe tables, blockquotes, ordered and unordered lists, horizontal rules,
**bold**, *italic*, `code`.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import os
import re
from pathlib import Path

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/hermes/.playwright")

CSS = """
  @page { size: A4; }
  * { box-sizing: border-box; }
  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body {
    font-family: "Liberation Serif", "Times New Roman", serif;
    font-size: 10.6pt; line-height: 1.48; color: #1a1a1a; margin: 0;
    -webkit-font-smoothing: antialiased;
  }
  .jp { font-family: "IPAGothic", "IPAPGothic", sans-serif; font-size: 0.96em; }
  .letterhead {
    display: flex; align-items: flex-end; justify-content: space-between;
    gap: 14px; padding-bottom: 9px; border-bottom: 1.1px solid #1a1a1a;
  }
  .brand { display: flex; align-items: center; gap: 9px; }
  .brand img { height: 30px; width: auto; display: block; }
  .brand-text .name { font-size: 13.5pt; line-height: 1.1; color: #9E2A2B; }
  .brand-text .entity { font-size: 8.4pt; font-style: italic; color: #6f6f6f; line-height: 1.35; margin-top: 1px; }
  .letterhead .right { text-align: right; font-size: 8.4pt; font-style: italic; color: #6f6f6f; line-height: 1.4; }
  .kicker { font-size: 9.4pt; color: #9E2A2B; margin: 20px 0 5px 0; }
  h1 { font-size: 20pt; line-height: 1.14; font-weight: normal; margin: 0 0 7px 0; color: #111; max-width: 92%; }
  .deck { font-size: 10.4pt; font-style: italic; color: #5c5c5c; margin: 0 0 4px 0; }
  h2 {
    font-size: 11.6pt; font-weight: bold; color: #111;
    margin: 20px 0 8px 0; padding-top: 8px;
    border-top: 1px solid #dcdcdc; page-break-after: avoid;
  }
  h3 { font-size: 10.6pt; font-weight: bold; color: #2b2b2b; margin: 11px 0 5px 0; page-break-after: avoid; }
  p { margin: 0 0 6px 0; }
  strong { font-weight: bold; }
  ul, ol { margin: 4px 0 8px 0; padding-left: 18px; }
  li { margin: 0 0 3px 0; page-break-inside: avoid; }
  table { width: 100%; border-collapse: collapse; margin: 6px 0 9px 0; font-size: 9.3pt; border-top: 1.1px solid #1a1a1a; }
  thead { display: table-header-group; }
  thead th {
    text-align: left; vertical-align: bottom; padding: 0 12px 4px 0;
    font-weight: bold; font-style: italic; color: #4a4a4a; font-size: 9.4pt;
    border-bottom: 1px solid #1a1a1a;
  }
  tbody td { padding: 2.2px 12px 2.2px 0; vertical-align: top; border: 0; }
  tbody tr:last-child td { border-bottom: 1.1px solid #1a1a1a; padding-bottom: 3px; }
  tr { page-break-inside: avoid; }
  blockquote {
    margin: 10px 0 8px 0; padding: 2px 0 2px 15px; border-left: 2px solid #9E2A2B;
    font-style: italic; color: #444; page-break-inside: avoid;
  }
"""


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    return text


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md: str, title: str, kicker: str, subtitle: str, logo_uri: str, entity_line: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    first_h1_used = False
    deck_used = False
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("---") and set(stripped) <= {"-"}:
            i += 1
            continue

        # tables
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            header = split_row(stripped)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in header) + "</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1 and not first_h1_used:
                out.append(f'<h1>{inline(text)}</h1>')
                first_h1_used = True
            elif level <= 2:
                # only the FIRST h2 under the h1 becomes the deck line; the rest are real headings
                if first_h1_used and level == 2 and not deck_used:
                    out.append(f'<p class="deck">{inline(text)}</p>')
                    deck_used = True
                else:
                    out.append(f"<h2>{inline(text)}</h2>")
            else:
                out.append(f"<h3>{inline(text)}</h3>")
            i += 1
            continue

        if stripped.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + "".join(f"<p>{inline(b)}</p>" for b in buf if b) + "</blockquote>")
            continue

        if re.match(r"^[-*]\s+", stripped):
            buf = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                buf.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ul>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            buf = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                buf.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ol>")
            continue

        # paragraph (merge consecutive plain lines)
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{1,4}\s|\||>|[-*]\s|\d+\.\s|---$)", lines[i].strip()
        ):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{CSS}</style></head><body>
<div class="letterhead">
  <div class="brand">
    <img src="{logo_uri}" alt="Anamata">
    <div class="brand-text"><div class="name">Anamata Records</div>
    <div class="entity">{html.escape(entity_line)}</div></div>
  </div>
  <div class="right">{kicker}</div>
</div>
<p class="kicker">{html.escape(subtitle)}</p>
{chr(10).join(out)}
</body></html>
"""


async def render(html_path: Path, pdf_path: Path) -> None:
    from playwright.async_api import async_playwright

    footer = (
        '<div style="width:100%; font-family:\'Liberation Serif\',serif; font-size:7.8pt;'
        ' color:#8a8a8a; padding:0 24mm; display:flex; justify-content:space-between;">'
        '<span>Anamata K&#257;hui Limited &#183; Te K&#257;hui Anamata</span>'
        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
    )
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = await browser.new_context(viewport={"width": 900, "height": 1200}, device_scale_factor=2)
        page = await ctx.new_page()
        await page.goto(f"file://{html_path}")
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(900)
        await page.pdf(path=str(pdf_path), format="A4", print_background=True,
                       display_header_footer=True, header_template="<div></div>",
                       footer_template=footer,
                       margin={"top": "19mm", "bottom": "18mm", "left": "24mm", "right": "24mm"})
        await browser.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--pdf-out", default=None)
    ap.add_argument("--title", default="Anamata Records")
    ap.add_argument("--kicker", default="")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--entity-line", default="Anamata Kāhui Limited · NZBN 9429052960734 · Aotearoa New Zealand")
    args = ap.parse_args()

    src = Path(args.input).resolve()
    pdf = Path(args.pdf_out).resolve() if args.pdf_out else src.with_suffix(".pdf")
    html_path = src.with_suffix(".print.html")
    logo = Path("/opt/data/anamata-kahui/public/brand/flame-256.png")
    import base64

    logo_uri = "data:image/png;base64," + base64.b64encode(logo.read_bytes()).decode()

    md = src.read_text(encoding="utf-8")
    html_path.write_text(convert(md, args.title, args.kicker, args.subtitle, logo_uri, args.entity_line), encoding="utf-8")
    asyncio.run(render(html_path, pdf))
    print(f"html: {html_path}")
    print(f"pdf:  {pdf}  ({pdf.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
