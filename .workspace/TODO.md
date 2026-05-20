# TODO — fidakarWebsite

## Pending

- [ ] **Photo likes + view counter** — added 2026-05-20
  - Users can like individual photos; Mohammad can see total likes and view counts
  - Via Firebase Realtime Database (already discussed; Firebase project creation is Step 1)

- [ ] **Photo purchase / download — $2 per photo, proceeds to Afghan children's education** — added 2026-05-20
  - Add a buy/download button on each photo (in lightbox or on hover)
  - $2 per photo via Stripe or PayPal
  - Proceeds go to children's education in Afghanistan
  - Decide: link out to a charity or collect via payment processor and donate manually
  - Add a short note on the photography page explaining the mission

- [ ] **Blog: "Stories of Displacement" section** — added 2026-05-20
  - New section on blog.html for first-person or curated displacement stories
  - Decide format: submitted stories (contact form), curated external links, or Mohammad's own writing
  - Add submission prompt so visitors can contribute their own story

- [ ] **Blog: placeholder for future categories** — added 2026-05-20
  - "Add here for more..." — revisit once Stories of Displacement is live

- [ ] **Deploy to mfidakar.com** — added 2026-05-20
  - Push all files to hosting (GitHub Pages, Netlify, or existing host)
  - Confirm domain DNS is pointed at host

- [ ] **Add more photos to photography page** — added 2026-05-20
  - Drop photos into the correct year folder (images/photography/2024/, 2025/, 2026/, etc.)
  - Then run: python3 build_photos.py — HTML updates automatically

- [ ] **Update bio text on home page** — added 2026-05-20
  - Located in index.html, the About section (3 paragraphs)

- [ ] **Update CV** — added 2026-05-20
  - Replace files/cv.pdf with updated version when ready

- [ ] **Missing abstracts for 2 working papers on research page** — added 2026-05-20

- [x] **Farsi article link on blog page** — added 2026-05-20, done 2026-05-20

- [ ] **Add syllabus for ECON 220 Lab on teaching page** — added 2026-05-20
  - Add a syllabus link/download button under the ECON 220 Lab — Data Science for Economists entry
  - Drop the syllabus PDF into files/ and link it, similar to how CV is handled

- [ ] **ECON 220 Lab dedicated course page** — added 2026-05-20
  - Clicking "ECON 220 Lab — Data Science for Economists" on the teaching page opens a new page (econ220.html)
  - Page should have sections for: slides (by chapter/week), readings, and any other course materials
  - Need content: slide files or links, chapter titles, reading lists

## Completed

- [x] Build complete website from scratch (all 6 pages) — done 2026-05-18
- [x] Photography grid with lightbox — done 2026-05-18
- [x] Social media icons, profile photos, cover hero layout — done 2026-05-18
- [x] CV page with embedded PDF — done 2026-05-18
- [x] Research, Teaching, Blog pages with content — done 2026-05-18
- [x] Organize photos into year subfolders + build_photos.py auto-update script — done 2026-05-20
