# Me Gusta Redesign — Session Review
**Date:** 31 March 2026

---

## What Was Done

### 1. cafe.html — Built from scratch
Created the full Café page for Me Gusta Spanish, covering:
- **Hero** — dark coffee-brown background with two floating polaroid photos and an animated SVG steam effect. Terra-coloured ticker strip with scrolling copy.
- **The Space** — atmospheric section with an overlapping dual-polaroid layout (main interior shot + smaller courtyard photo overlapping bottom-right), and clean left-rule feature items (Colonial Architecture, Free WiFi, Open-Air Courtyard) using `border-left: 2px solid var(--terra)` — no box backgrounds or icons.
- **Menu** — four categories (Coffee, Food, Cold Drinks, Special Drinks) with hover left-bar effect and ghost `"café"` background text.
- **Coffee Origins** — dark section highlighting three Bolivian single-origin coffees (Caranavi, Yungas, Lavazza blend) with gold-accent hover cards.
- **Reviews** — three customer testimonials in polaroid-style cards.
- **Visit Info** — address (Bolivar #603), opening hours, and study space callout.
- Full EN/ES language toggle support (`data-en` / `data-es` attributes).
- Scroll reveal via IntersectionObserver.
- Matches the font stack and CSS variables used across the rest of the redesign (Cormorant, Caveat, Lora).

### 2. Café nav link — size bump across all pages
Increased the Café link font-size in the nav from `1.55rem` (previously bumped from `1.25rem`) across all 10 HTML files:
`index.html`, `classes.html`, `methodology.html`, `teachers.html`, `cafe.html`, `about.html`, `accommodation.html`, `faqs.html`, `blog.html`, `contact.html`

### 3. cafe.html — Design iteration
Applied the frontend-design skill to produce a heavily redesigned version of cafe.html with a more editorial aesthetic. After review, reverted to the original version as the base, keeping two specific elements from the redesign:
- **Overlapping dual-polaroid** in the atmosphere section (replacing the original three-photo grid)
- **Left-rule feature items** (replacing rounded card components that felt too generic)

### 4. Folder structure
Moved all 10 HTML files from `megusta-redesign/` into a clean project folder at:
```
/Users/ash/Projects/migusta/
```
No code changes required — all inter-page links use relative filenames and continue to work correctly.

---

## Current File Structure

```
migusta/
├── index.html
├── classes.html
├── kids.html
├── methodology.html
├── teachers.html
├── activities.html
├── cafe.html
├── about.html
├── accommodation.html
├── faqs.html
├── blog.html
├── contact.html
├── docs/
├── images/
└── review.md
```

---

## Design System (shared across all pages)

| Token | Value |
|---|---|
| `--bg` | `#FAFAF7` |
| `--terra` | `#C8572D` (primary accent) |
| `--gold` | `#C4913A` |
| `--coffee` | `#3D2314` (dark sections) |
| `--ink` | `#1C1410` |
| Display font | Cormorant (italic headings) |
| Accent font | Caveat (handwritten labels, prices) |
| Body font | Lora (serif body copy) |

---

## Session — 31 March 2026 (continued)

### 5. cafe.html — Coffee Origins section redesign
Replaced the three equal rounded cards (AI-looking) with an editorial **archive/logbook** layout:
- Three horizontal rows separated by thin gold ruled lines (`1px solid rgba(196,145,58,0.18)`)
- Large faded index numbers (`01`, `02`, `03`) in ghosted Cormorant (4.5rem, opacity ~13%) as left column
- Origin name in large Cormorant (left-aligned), location label in Caveat above
- Description text in Lora italic, left-aligned, not boxed
- Taste notes stacked on the right as italic Cormorant text with thin underline strokes
- Removed: flag emojis, rounded cards, gold top borders, pill taste tags
- Fully bilingual (`data-en`/`data-es`) preserved throughout
- CSS classes renamed: `origins-grid` → `origins-list`, `origin-card` → `origin-entry`, `taste-tag` → `taste-note`

### 6. Git setup & GitHub push
- Initialised git repo in `/Users/ash/Projects/migusta/`
- Created and pushed to `github.com/Ashdabash2926/migusta` (public)
- Initial commit included all 10 HTML files
- **Repo later renamed to `migustaschoolprivate` and set to private** (April 2026)
- Remote URL updated to: `https://github.com/Ashdabash2926/migustaschoolprivate.git`

### 7. Added migusta to Studio North portfolio
- Took Puppeteer screenshot of local `index.html` at 1440×900
- Converted to WebP (69KB) via Sharp
- Added portfolio card to `studio-north/index.html` as card 9 (before Peak Form)
- Card links to `ashdabash2926.github.io/migusta/` — GitHub Pages needs enabling to go live
- Pushed to `github.com/Ashdabash2926/studio-north`

### 8. Navbar logo — image replacing text
- Added `images/megustalogoclear.png` to navbar across all 10 pages
- Replaced `.nav-logo` text (`Me Gusta Spanish`) with `<img class="nav-logo-img">`
- Nav height set to explicit `64px`, vertical padding removed, logo fills full height via `height: 100%`
- `classes.html` had a multiline `#main-nav` block — fixed separately after sed missed it
- Logo switched from `megustalogo.png` to `megustalogoclear.png` across all pages

---

---

## Session — 8 April 2026

### 9. French language option — added then reverted
- Python script added FR as a third language option (flag dropdown replacing EN/ES buttons) across all 10 pages
- Script had two bugs: (1) orphaned `@keyframes` CSS left invalid fragments; (2) HTML regex consumed `nav-cta` and `nav-burger` elements plus the nav-right closing `</div>`, leaving all pages broken
- All attempted fixes in that session failed to commit
- **Decision: reverted all 10 pages to `f35ab6f`** (pre-French EN/ES toggle state)

### 10. cafe.html — nav and section recovery
- `cafe.html` had its real photo redesign (DSC images, carousel, atmosphere section) only in the working directory — never committed separately before the French script ran
- The committed version (`927e334`) had the FR dropdown nav and was missing the hero + atmosphere HTML sections (lost to the Python script)
- Recovery process:
  - Restored `927e334` cafe.html (had DSC photo content + carousel)
  - Replaced FR dropdown nav with EN/ES lang-bubble toggle (CSS + HTML + JS)
  - Fixed two broken `@keyframes` rules (`floatIn` and `tickMove`)
  - Rebuilt missing hero section: DSC06122 background, DSC06175 polaroid card, ticker strip
  - Rebuilt missing atmosphere section: DSC05948 full-bleed left, DSC06100 inset polaroid, left-rule features
  - Added missing `<div id="navMobile">` — its absence caused a JS error that prevented IntersectionObserver from running, making all `.reveal` sections invisible

### 11. Images committed to GitHub
- `images/cafe/` (all `.webp`) and `images/school/` (`.jpg` — not yet used in HTML) added to git and pushed
- Stray `DSC06100 copy 2.tiff` deleted from cafe folder
- GitHub Pages enabled on `migustaschoolprivate` repo (now public)
- Live site: `https://ashdabash2926.github.io/migustaschoolprivate`

### Notes
- `images/school/` contains `.jpg` files — must convert to `.webp` before using in any HTML page
- The nav Python scripts (`fix_nav.py`, `fix_nav2.py`) are still in the project root — can be deleted

---

## Session — 13/14 April 2026

### 12. Teachers page — real photos added
- Converted 7 teacher photos (Abbie, Angel, Anna, Belen, Claudia, Erik, Kiara) from JPG to WebP using `cwebp -q 82 -resize 800 0`
- Original JPGs deleted, teachers.html updated with real images replacing Unsplash placeholders

### 13. Teachers page — full redesign (frontend-design)
- Editorial portrait gallery with dark hero, 12-column grid, aspect-ratio 3/4 portrait cards
- Hover/tap bio overlays with gradient backgrounds, touch support via `.active` class toggle

### 14. Activities page — new page created
- `activities.html` built from scratch with 8 activity cards (Bolivian Cooking, Market Morning, City Walk, Salsa Night, Cinema, Conversation Evening, Tarabuco Day Trip, Photography Walk)
- Dark hero with dual radial gradients, ticker strip animation, 12-column editorial grid
- Hover overlays with activity details, "How it works" 3-step section, bilingual EN/ES/FR

### 15. Nav redesign — "More" dropdown across all pages
- Wrote `update_nav.py` to bulk-update nav in 9 existing pages
- Primary nav: Classes, Teachers, Activities, Cafe, About, Contact
- "More" dropdown: Home, Methodology, Accommodation, FAQs, Blog
- `.nav-cafe-link` class replacing inline styles for Cafe link
- Breakpoint bumped from 960px to 1100px for the mobile hamburger
- Mobile nav updated to include Activities link

### 16. Contact page — full redesign
- Compact `--bg-warm` hero replacing the dark split layout (per feedback)
- Contact methods as pill-shaped links (WhatsApp, Email, Landline) below hero
- WhatsApp link fixed: `tel:+59170001234` changed to `https://wa.me/59170001234`
- Centred form section, "Find us" section with Google Maps embed using real school location
- "Open in Maps" button linking to `https://maps.app.goo.gl/rnyqrN6wnNvEvuTX6`

### 17. About page — founders updated
- Elizabeth & Fernando updated to both Bolivian locals (previously British-Bolivian)
- Hero subtitle, founders intro, Elizabeth's bio, and timeline all rewritten
- Timeline 2003 entry changed from "Elizabeth arrives in Bolivia" to "Elizabeth & Fernando meet"
- Real photos added: Elizabeth.jpg, Fernando.jpg, Elizabeth&Fernando.jpg
- Hero polaroid `aspect-ratio: 4/3` overridden to `auto` for the couple photo (was cropping)

### 18. About page — values section redesign (frontend-design)
- Dark background with radial gradients (terra + gold)
- Split header: title left, description right
- 3x2 borderless grid cells with ghosted numbers, italic Cormorant titles, muted text

### 19. Image workflow updated
- Images exported from Lightroom as sRGB JPG (long edge 800px, quality 82-85) can now be used directly without WebP conversion if already under ~200KB
- Previous cwebp conversion was stripping ICC colour profiles causing colour shifts (greener/more contrasty)
- CLAUDE.md and memory updated with new rule
- Old `.webp` teacher files replaced with Lightroom-exported `.jpg` files

### 20. Language toggle — flag dropdown with French
- EN/ES pill toggle replaced with flag dropdown (🇬🇧 EN, 🇪🇸 ES, 🇫🇷 FR) across all 11 pages
- Wrote `update_lang.py` and `fix_lang_remaining.py` for bulk updates
- Fixed `langBtns` → `langOptions` crash in lang bubble dismiss code (was breaking scroll reveal on all pages)
- JS `setLang` updated to fall back to English if `data-fr` missing: `el.dataset[lang] || el.dataset['en']`

### 21. French translations added
- Wrote `add_french.py` and `add_french_2.py` to programmatically add `data-fr` attributes
- ~540+ strings translated across all 11 pages (~85% coverage)
- Covers nav, headings, body copy, form labels, testimonials, FAQs, blog posts, footer
- Remaining ~99 strings gracefully fall back to English

### 22. Kids Programme page — new page created
- `kids.html` built from scratch with full Kids Programme content
- Dark hero with radial gradients, Cormorant title, trilingual EN/ES/FR
- Classes section: three age-group cards (Little Explorers 4–7, Young Adventurers 8–11, Teen Travellers 12–15) using `.format-card` pattern
- Activities section: six kid-friendly activities with left-rule layout (Treasure Hunts, Cooking Class, Art & Crafts, Market Mornings, Story Time, Dance & Music)
- Family section: Family Accommodation, Parent Classes, Flexible Scheduling info blocks
- CTA section linking to contact page

### 23. Nav restructured across all 12 pages
- Primary nav reduced to 5 links: Home, Classes, Kids, Café, Contact
- "More" dropdown expanded: Teachers, Activities, Methodology, About, Accommodation, FAQs, Blog
- Mobile nav updated to match with all pages listed
- Active states set per-page (primary links and dropdown items)
- Breakpoint standardised to 1100px across all pages (was 960px on index.html and classes.html)

### 24. Footer updated with Kids link
- Kids link added to "Learn" column in footer across all 12 pages

---

## Rules & Conventions

### Image Workflow
- If a JPG/PNG is already exported at a reasonable size (under ~200KB, resized to ~800px long edge, sRGB colour space), it can be used directly — no conversion needed
- For large/unoptimised images, convert to `.webp` using `cwebp -q 82 -resize 800 0`
- After converting, delete the original — no duplicates allowed
- Only one format per image should remain in the `images/` folder
- Reason: keeps the images folder clean and reduces file sizes loaded by the site
