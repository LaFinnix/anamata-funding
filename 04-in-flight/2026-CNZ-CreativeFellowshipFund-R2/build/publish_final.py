"""Copy the built PDFs to their final, upload-ready filenames.

The build writes internal names (CNZ-CreativeFellowship-R2-<document>.pdf) because the zip, the archive and
the manifest all reference them. This script publishes byte-identical copies under the names that go into the
Creative New Zealand portal, so a rename never breaks a rebuild.

Run:  python3 build/publish_final.py
"""
import hashlib
import io
import os
import shutil

D = "/opt/data/anamata/funding/applications/2026-CNZ-CreativeFellowshipFund-R2"
STEM = "Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2"

MAP = {
    "CNZ-CreativeFellowship-R2-Somatosensory.pdf": f"{STEM}-Application.pdf",
    "CNZ-CreativeFellowship-R2-Method-Annex.pdf": f"{STEM}-Method-Annex.pdf",
    "CNZ-CreativeFellowship-R2-Accessibility-Evidence.pdf": f"{STEM}-Accessibility-Evidence.pdf",
    "CNZ-CreativeFellowship-R2-CV-Ngaika-Smith.pdf": f"{STEM}-Arts-CV.pdf",
    "CNZ-CreativeFellowship-R2-Portal-Answers.pdf": f"{STEM}-Portal-Answers.pdf",
    "CNZ-CreativeFellowship-R2-People-and-Organisations.pdf": f"{STEM}-Participation-Records.pdf",
}


def md5(path: str) -> str:
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def main() -> int:
    out = f"{D}/final"
    os.makedirs(out, exist_ok=True)
    # clear stale final copies so a removed document cannot linger
    for name in os.listdir(out):
        os.remove(os.path.join(out, name))

    rows = []
    for src_name, dst_name in MAP.items():
        src = f"{D}/{src_name}"
        if not os.path.exists(src):
            print(f"  MISSING SOURCE  {src_name}")
            continue
        dst = os.path.join(out, dst_name)
        shutil.copyfile(src, dst)
        same = md5(src) == md5(dst)
        size = os.path.getsize(dst)
        rows.append((dst_name, size, same))
        print(f"  {dst_name}  {size:,} bytes  {'identical' if same else 'COPY MISMATCH'}")

    index = [f"# Final upload set, {STEM}", "",
             "Byte-identical copies of the built PDFs, named for upload. Rebuild with",
             "`build/build_pdfs.py`, then re-publish with `build/publish_final.py`.", "",
             "| File | Bytes | Internal source |", "|---|---|---|"]
    for src_name, dst_name in MAP.items():
        if os.path.exists(f"{D}/{src_name}"):
            index.append(f"| `{dst_name}` | {os.path.getsize(os.path.join(out, dst_name)):,} | `{src_name}` |")
    io.open(os.path.join(out, "00-FINAL-SET.md"), "w", encoding="utf-8").write("\n".join(index) + "\n")
    print(f"\n  {len(rows)} documents published to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
