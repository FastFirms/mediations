#!/usr/bin/env python3
"""Build the downloadable parenting plan worksheet (brief §4.1).

Source:  build/assets_src/parenting-plan-template.html  (single source of truth)
Outputs: downloads/parenting-plan-template.pdf   (Chrome headless, tagged PDF)
         downloads/parenting-plan-template.docx  (pandoc, editable, no macros)

Run manually after editing the source:  python3 build/gen_parenting_plan_assets.py
"""
import os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "build", "assets_src", "parenting-plan-template.html")
OUT = os.path.join(ROOT, "downloads")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(OUT, exist_ok=True)
pdf = os.path.join(OUT, "parenting-plan-template.pdf")
docx = os.path.join(OUT, "parenting-plan-template.docx")

subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--generate-pdf-document-outline", f"--print-to-pdf={pdf}",
                "file://" + SRC], check=True, capture_output=True)
subprocess.run(["pandoc", SRC, "-f", "html", "-t", "docx", "-o", docx,
                "--metadata", "title=Parenting Plan Template (Discussion Worksheet)"],
               check=True)

for f in (pdf, docx):
    print(f"{os.path.relpath(f, ROOT)}  {os.path.getsize(f) // 1024} KB")
