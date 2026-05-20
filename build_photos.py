#!/usr/bin/env python3
"""
Scans images/photography/<year>/ folders and updates photography.html.

Usage:
    python3 build_photos.py

Drop photos into images/photography/2024/ (or any year folder), then run
this script. It rewrites the <div class="photo-grid"> block for each year.
"""

import os
import re

PHOTO_DIR = "images/photography"
HTML_FILE = "photography.html"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def build_grid(year):
    folder = os.path.join(PHOTO_DIR, str(year))
    if not os.path.isdir(folder):
        return f'          <!-- drop photos into {folder}/ and run build_photos.py -->'
    files = sorted(
        f for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in EXTENSIONS
    )
    if not files:
        return f'          <!-- no photos yet in {folder}/ -->'
    lines = []
    for f in files:
        src = f"{PHOTO_DIR}/{year}/{f}"
        lines.append(f'          <img src="{src}" alt="">')
    return "\n".join(lines)


with open(HTML_FILE, "r") as fh:
    html = fh.read()

# Find all year sections by id="year-YYYY"
years = re.findall(r'id="year-(\d{4})"', html)

for year in years:
    grid_content = build_grid(year)
    # Replace content between <div class="photo-grid"> and </div> for this year's section
    pattern = (
        r'(id="year-' + year + r'"[\s\S]*?<div class="photo-grid">)'
        r'[\s\S]*?'
        r'(</div>)'
    )
    replacement = r'\1\n' + grid_content + r'\n        \2'
    html, n = re.subn(pattern, replacement, html, count=1)
    if n:
        print(f"  {year}: updated")
    else:
        print(f"  {year}: section not found — skipped")

with open(HTML_FILE, "w") as fh:
    fh.write(html)

print(f"\nDone. Open {HTML_FILE} in your browser to preview.")
