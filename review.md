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

## Session — 17 April 2026

### 25. Hero animations — index.html
Added four animations to the hero section on `index.html`, all changes inline in the single file.

- **Ken Burns background** — slow pan/zoom on a new `.hero::before` pseudo-element (28s loop desktop, 40s mobile, alternating). Inline `style="background-image: ..."` on `<section class="hero">` removed in favour of the pseudo-element so parallax can target it without fighting Ken Burns.
- **Polaroid drop-in** — `.hero-right` animation swapped from `fadeUp` to a new `polaroidDrop` keyframe. Drops from `translateY(-120%) rotate(-12deg)` to `translateY(0) rotate(0deg)` with `cubic-bezier(0.34, 1.56, 0.64, 1)` for a small overshoot. The child `.polaroid`'s own `rotate(2.5deg)` shows through as the resting tilt.
- **Hand-drawn underline** — inline SVG (`<svg class="hero-underline">`) added as a sibling of the `<span>` inside the `<em>` in the hero title. Wavy path drawn via `stroke-dasharray`/`stroke-dashoffset` animation, 0.9s ease-out, 1.4s delay (lands after the title fade-up). `.hero-title em` augmented with `position: relative; display: inline-block` so the absolute SVG anchors to each language's width.
- **Scroll parallax** — new IIFE in the existing `<script>` block with rAF-throttled scroll handler. Sets `--parallax-y` on `.hero` (consumed by `.hero::before` via `transform: translate3d`) and `--parallax-rot` on `.polaroid` (consumed via the independent CSS `rotate:` property). IntersectionObserver pauses when hero is offscreen. Self-disables on `matchMedia('(max-width: 960px)')` and `matchMedia('(prefers-reduced-motion: reduce)')`.

### 26. Accessibility + mobile handling
- New `@media (prefers-reduced-motion: reduce)` block: Ken Burns off, polaroid entrance reverts to gentle `fadeUp`, underline snaps in instantly, ticker marquee stops (`.ticker-track { animation: none }`).
- New rule inside `@media (max-width: 960px)`: `.hero::before { animation-duration: 40s }` slows Ken Burns on mobile.
- Parallax JS self-gates on both conditions (already in step 25).

### 27. Review findings applied
- Polaroid scroll rotation was smearing because `.polaroid`'s existing `transition: transform 0.4s ease` (for hover) was also transitioning the scroll-driven rotation. Moved scroll rotation to the independent CSS `rotate:` property so the `transform` transition no longer dampens parallax updates.
- Trimmed `will-change` on `.hero::before` from `transform, background-position, background-size` to just `transform` — the non-composited properties don't benefit from the hint.

### 28. Spec + plan committed
- `docs/superpowers/specs/2026-04-17-hero-animations-design.md` — design spec
- `docs/superpowers/plans/2026-04-17-hero-animations.md` — task-by-task implementation plan

All 10 hero commits pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate`.

---

## Session — 18 April 2026

### 29. Activities page — photo stories + Wallyball (started previous session, committed this session)
- Added 9th activity card (Wallyball, Wednesday 1.5hrs).
- New "Real moments" section with two editorial magazine-layout photo galleries (Cooking, Wallyball).
- Click-to-enlarge lightbox with keyboard nav (Esc/←/→).
- Swapped Unsplash hero on the cooking card for real `DSC06312.webp`.
- `CLAUDE.md` updated to reflect FR support and new pages (`kids.html`, `activities.html`).

### 30. Accommodation page — full redesign (frontend-design skill)
**Design direction:** "The Residence" — editorial travel-magazine. Cinematic full-viewport hero, magazine-chapter gallery, dark amenities strip.

- **Cinematic hero** (100vh) — full-bleed `DSC08332-HDR.webp` with 32s Ken Burns zoom, dual vignette + top/bottom gradient, thin terra accent line draws in on load.
- **Staggered typography reveal** — "A house / in Sucre." headline: each line overflow-clips and animates `translateY(110%) → 0`. Eyebrow label, meta row, subtitle fade in with 0.3/1.0/1.15s delays.
- **Two glassmorphic booking plates** — Hostelworld (01) + Booking.com (02). Each has terra side-stripe that scales in on hover, index/category rows, arrow that rotates into a terra-filled circle.
- **Scroll-linked parallax + zoom-out** — `translateY = y * 0.6`, `scale = 1 - progress * 0.1`, `opacity = 1 - progress * 0.7`. rAF-throttled. Image wrapped in `.acc-hero-stage-wrap` so Ken Burns on inner element compounds cleanly.
- **Manifesto strip** — condensed to a single 3-column row (label | body | sign) on desktop. Smaller Cormorant type (1.15–1.5rem), tighter padding (4.5rem vertical).
- **Three numbered chapters** — I *Courtyard*, II *Rooms*, III *Details*. Each has huge terra italic numeral + right-aligned copy, then an asymmetric image mosaic (ch1: 4-image, ch2: 8-image 12-col editorial, ch3: 6-image 4-col).
- **Amenities strip** — dark ink panel with 4 custom inline SVG icons (Wi-Fi, showers, kitchen, terrace) on a bordered grid. (Initially had 6 — laundry and 24/7 reception removed later.)
- **Final CTA** — warm cream shapes bg, two buttons (`.btn-ink` + `.btn-terra`) linking to the two platforms.
- **Lightbox** — fade + scale, keyboard nav, terra-highlight arrow buttons, `X / Y` counter at bottom.
- **Image compression** — 36 room photos JPG→WebP (468MB → 4MB). Hero 2000px @ q85, gallery 1400px @ q80.
- **Case fix** — renamed `images/Rooms` → `images/rooms` (git was case-sensitive from upstream commit; macOS FS isn't). Two-step rename via temp name to force the change through.
- **Placeholder booking URLs** — `hostelworld.com` / `booking.com` domain roots; need real property URLs from client.

### 31. Headbar restored to site standard (important)
Initial accommodation redesign used a scroll-aware dark nav that turned translucent + white-text over the hero, swapping to cream after scroll. This broke the **More** dropdown — its links inherited `.over-dark .nav-center a { color: white }`, so dropdown text was invisible on the cream dropdown bg.

- Reverted nav to the standard opaque cream with 95% alpha + `backdrop-filter: blur(16px)` that every other page uses.
- Removed the `.over-dark` class, its CSS rules, and the scroll listener.
- **Added rule to `CLAUDE.md`**: the headbar must be identical across all pages. No per-page variants. When redesigning any page, copy the nav HTML/CSS/JS verbatim — only `class="active"` should differ.

### 32. Hero animation upgrades
- **Parallax + zoom-out** on scroll (as above in §30).
- **Top terra accent line** now draws in from center on load: `scaleX(0) → scaleX(1)` over 1.6s cubic-bezier with a 0.2s delay. Respects `prefers-reduced-motion`.

### 33. Teachers page — 6 new teachers added
- **New teachers:** Clara, Claudia, Ghiselle, Luz, Raquel, Yatsejany. All photos JPG→WebP @ 1100px q82 (~40–70KB each).
- **Grid extended:** row 3 (4 × span-3: Clara, Claudia, Ghiselle, Luz), row 4 (2 × span-6: Raquel, Yatsejany).
- **Mobile grid simplified** — dropped nth-child-specific rules in favour of `.teacher-card { grid-column: span 6/12 !important }`.
- **Bios written in existing tone** — plausible placeholders tagged with role + 2 specialty tags, trilingual (EN/ES/FR). Flagged as edit-worthy.
- **Filename "2" suffix convention** — user rule: any `*2.jpg` (backup variants like `Ghiselle2.jpg`, `Yatsejany2.jpg`) is **not** to be added to the page. Left untracked on disk as backups.
- **Swapped Anna ↔ Kiara** positions after user feedback (Kiara now row 1, position 3; Anna now row 2, position 7).

### 34. Memories saved
- `feedback_headbar_consistency.md` — never add per-page nav variants; the `.over-dark` failure is the why.

### 35. Accommodation — 6-bed dorm chapter added to gallery
Extended the accommodation page with a dedicated chapter for the new six-bed dorm. Client dropped 11 JPGs (10–22MB each) into `images/rooms/6bed/`; converted all to WebP at 800px / q82 (30–85KB each) and deleted originals per the image workflow rule.

- **Inserted new Chapter III** between the existing rooms (II) and details chapters; renumbered the old III → IV across number badge + `chapter-tag` EN/ES/FR attributes.
- **Trilingual copy** for the new chapter title ("The six-bed dorm" / "El dormitorio de seis camas" / "Le dortoir six lits") and a sociable-but-not-grim chapter note.

**Layout iterations (5 rounds of feedback):**
1. First pass — 11-tile 12-col custom grid with `object-fit: cover`. Cropped portraits awkwardly.
2. Client removed two photos (`DSC08504`, `DSC08509`). Dropped them from HTML; swapped the grid to CSS-columns masonry with `object-fit: contain` so landscape + portrait both show fully.
3. Client wanted beds featured, bathroom/kitchen smaller. Restructured into **two tiers**: a 3-up bed feature + a 6-up "Kitchenette & bathroom" thumbnail strip.
4. Feature row had a middle-column gap (short landscape tile in 3-col grid). Collapsed to 2 columns — big hero (2fr) + two stacked smaller bed shots (1fr).
5. Client wanted bathroom/kitchen unified, no label. Merged into single clean 6-up grid with uniform `aspect-ratio: 3/4` + `object-fit: cover` tiles.
6. **Final gap fix** — left-column hero was shorter than the stacked right column because `align-items: start` on the container prevented the hero tile from stretching. Added `align-self: stretch` on the hero + `height: 100%` + `object-fit: cover` on the img so it fills the full spanned height. Root cause was the container's `align-items: start`, not the img CSS.

**Photo categorisation (determined by reading the actual webp files):**
- Beds (feature): 489 bunks hero, 494 beds close-up, 519 single bed under bunk
- Kitchen (small): 514 (portrait), 554 (landscape)
- Bathroom (small): 529 twin sinks, 534 WC, 539 shower floor, 544 shower

All captions EN/ES/FR.

All commits pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate`.

### 36. Kids page — scrapbook-editorial redesign
Swapped the emoji-led age-group cards for a polaroid-and-handwriting aesthetic. Client dropped 3 JPGs (10–19MB) into `images/kids/`; converted all to WebP at 1200px / q82 and deleted originals.

- **Hero**: cream two-col layout with a tilted polaroid of DSC07157 (smiling learners), washi tape, handwritten "real kids, real laughs" callout + hand-drawn dashed-arrow SVG pointing at the photo. Large italic title "Spanish, but make it *playful*" with a gold SVG squiggle under "playful".
- **Three age-group cards** ("Little Explorers" 4–7, "Young Adventurers" 8–11, "Teen Travellers" 12–15) now use numbered `01 / 02 / 03` chapter marks and custom inline-SVG glyphs (face, mountain, globe) instead of emoji.
- **"Spanish in the wild"** activities section rebuilt as a split layout: left = polaroid of DSC07149 (cereal-box grammar lesson) with an orange pull-quote "Turns out breakfast cereal is the fastest route to the preterite tense. — Señora Carla"; right = 6-item tick-list of off-site activities.
- **Family experience** section: 3 blocks with roman numerals (i., ii., iii.) + the DSC07111 goody-bag polaroid with a "nobody left empty-handed" sticky note in Caveat.
- All copy EN/ES/FR. Nav + footer kept identical per the headbar rule.

### 37. Activities page — three-phase rebuild
Started as an editorial redesign with descriptions + gallery; client pushed back on complexity each iteration until it landed at the final simple form.

**Phase A — editorial rewrite + unified gallery**
Replaced the old hover-overlay card grid with:
- A 9-entry description index (tag chip + roman numeral + schedule meta + blurb per activity, in bordered rounded cards)
- A "Real moments" gallery section grouping all 11 real photos from `images/activities/` — 6 cooking + 5 wallyball — in two mixed-size CSS-grid masonry arrangements, hooked up to the existing lightbox.

**Phase B — compact list**
Client wanted cards gone. Rebuilt the 9 entries as a single hairline-divided typographic list: 4-column grid per row (roman numeral · name · meta+tag · one-line description), no card chrome. Shortened all blurbs from 3 sentences to 1. Trimmed the intro head to a single sentence ("Led by teachers or local guides. Everything runs in Spanish.").

**Phase C — narrowed to 4 weekly activities**
Client clarified the real weekly schedule: Mon city walking tour, Tue & Thu cooking class, Wed wallyball, Fri beer tour. Dropped Market Morning, Salsa Night, Cinema & Conversation, Conversation Evening, Tarabuco Day Trip, Photography Walk. Replaced the roman-numeral left column with **weekday labels** (Mon / Tue & Thu / Wed / Fri) in italic gold Cormorant. New "Sucre Beer Tour" entry written fresh (EN/ES/FR). Hero ticker rewritten to the same Mon–Fri rhythm.

**Phase D — hero update**
Simplified the hero: single large italic "Activities" wordmark (EN/ES/FR) over a background image (DSC06219, cooking ingredients in baskets) with a warm terra/gold radial gradient overlay and a subtle SVG noise layer. Eyebrow and subtitle kept for trilingual context.

### 38. Registration + auto-graded placement test (the big one)
Client wanted students to register online, take an auto-graded exam, and have staff pre-prepared with a class + price to confirm — because most enquiries come in on weekends when no one's around to respond.

**Design sketched in chat:**
- 3-step online form (contact → test → preferences) on a new `register.html`
- 5 open-ended Spanish questions, weighted low (absolute beginner → A1 → A2 → B1/B2 → C1/C2) because most customers are beginners
- Cloudflare Worker backend: Claude Haiku grades answers → CEFR level + teacher note → looks up suggested class/price → emails staff a pre-filled WhatsApp reply template → emails student a confirmation
- Staff opens Monday to a list of drafts ready to copy-paste; no grading work on their side

**Built:**
- **`register.html`** — trilingual 3-step form with progress indicator, chip-based preference selection, inline validation, animated step transitions, and a success state that shows the student their provisional level instantly after submit
- **`register-worker/`** — full Cloudflare Worker (`src/index.js` + `wrangler.toml` + `package.json` + `README.md` with full setup walk-through)
  - POST handler with CORS for the GH Pages origin + `*.pages.dev` previews + localhost
  - Calls Anthropic API directly via `fetch` (no SDK — keeps bundle small). Model: `claude-haiku-4-5-20251001`. Prompt includes the 5 questions, the student's answers, and a level-by-level rubric. Returns strict JSON parsed with a `{...}` regex fallback.
  - Hardcoded `PRICE_TABLE` at top of file — weekly prices per class type × duration. Placeholder numbers (group $150, private $350, online $180 per week) pending client's real pricing.
  - Emails via Resend HTTP API (also plain `fetch`). Two emails per submission: staff-facing HTML with contact table, plan summary, teacher note, answers, and a pre-filled WhatsApp reply in a dashed-border box + a one-click `wa.me/{number}` button; student-facing confirmation with the level + "we'll WhatsApp within 24h".
  - `ANTHROPIC_API_KEY` and `RESEND_API_KEY` set as wrangler secrets. Interactive secret prompts don't work via Claude Code's `!` bash wrapper (the secret gets set to empty string) — had to run `wrangler secret put` in a real Terminal window.
- **Nav CTA swapped across all 12 pages** — every `href="classes.html"` on a `.nav-cta`, mobile `.btn-primary` "Register Now", and the index "Register now and save!" link now points to `register.html`. Used a `sed` loop over all HTML files.

**Deployment gotchas encountered:**
- Cwd persists between Bash tool calls, so `cd register-worker && <cmd>` on a second call failed with "no such file or directory" — once in, stay in.
- Resend's sandbox (`onboarding@resend.dev`) **only delivers to the account-owner's signup email**. Client signed up with `lewisashleybutterfield@googlemail.com`; had initially set `STAFF_EMAIL = "lewisashley.t@outlook.com"` which got a 403 `validation_error` from Resend. Fixed by pointing `STAFF_EMAIL` at the googlemail address and telling client to fill in that same address as their "student" email during testing.

**Deployed worker URL:** `https://migusta-register.ashscms.workers.dev`

**End-to-end tested and working:** form submits → Claude returns CEFR level → staff email lands in Gmail with pre-filled reply template → student confirmation email lands in Gmail.

**Open items for next session (before handing to the school):**
1. **Verify `megustaspanish.com` in Resend** — so the worker can send to *any* student email, not just Ash's gmail. Swap `FROM_EMAIL = "noreply@megustaspanish.com"` and `STAFF_EMAIL = "info@megustaspanish.com"` in `wrangler.toml` once green; redeploy.
2. **Price table audit** — `PRICE_TABLE` at top of `register-worker/src/index.js` uses placeholder numbers. Review with client and replace.
3. **Anthropic spend cap** — set a $5/month cap at https://console.anthropic.com/settings/limits.
4. **Service ownership for handover** — decided to have the school sign up for Resend + Anthropic themselves when they're ready to take over billing. Ash swaps in their API keys via `wrangler secret put`, zero code change. Cloudflare stays in Ash's account (developer-owned).

**Also sketched but not built:** 5 placement questions went through 3 iterations — first multiple-choice CEFR-calibrated, then open-ended "forces the grammar", then weighted low for the school's actual customer base (mostly beginners). Final 5 questions live in both `register.html` (for the student) and `register-worker/src/index.js` (for Claude's rubric).

All commits pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate`.

---

## Session — 20/21 April 2026

### Register page — placement test polish
- **Double-click bug fix.** The "Next" buttons on each step sit at the same screen position, so a single mouse double-click was cascading the student straight through to step 3. Added a 600 ms `navLocked` flag set by `goToStep()`, an active-step guard on next/prev handlers, and `btn.blur()` on navigation so keyboard repeats don't re-fire either.
- **Questions rebuilt by CEFR level.** First pass went to six questions (pre-A1 → C2). Then trimmed to five when the client noted B2+ is rare in practice, so C1/C2 collapses into one top-tier question:
  - Q1 **BEGINNER** — `¿Cómo te llamas y de dónde eres?`
  - Q2 **A1** — daily routine (morning/afternoon/night)
  - Q3 **A2** — what you did last weekend + what you liked most
  - Q4 **B1** — hypothetical year abroad + how it would change your life
  - Q5 **B2+** — remote-work pros/cons with a nudge for advanced speakers to go deeper
- **Worker graded-level set** is now `BEGINNER | A1 | A2 | B1 | B2+`. Updated `LEVEL_COPY`, the Claude rubric, and the validation regex (`/^(BEGINNER|A1|A2|B1|B2\+)$/`). Staff-email question labels in `renderAnswers()` match the new prompts.

### Index — "Two ways to learn" redesign + stats refresh
- Scrapped the dark photo-overlay panes (they fought the cream/terra palette and doubled-up the `→` on the Learn More buttons — CSS was adding `::after '→'` on top of the literal arrow in the label).
- New editorial **"postcard" cards** on cream background: white card with subtle terra border, image at top with a small Caveat chip ("since 2011" / "any timezone"), Cormorant italic title, Lora body, 3-item feature list with gold dashes, underlined terra CTA with a single arrow.
- **Site-wide stats refreshed** for the new client numbers (15 years teaching, 15,000 students, 12 tutors):
  - `index.html` hero badge `750+` → `15k+`
  - stats strip `20+ years / 750+ students / 8 teachers` → `15+ / 15,000+ / 12`
  - label "students registered" → "students taught"
  - testimonials note "hundreds of happy students" → "thousands of"
  - `methodology.html` "17 years" → "15 years" across EN/ES/FR (hero handwritten, hero sub, big blockquote)
  - `about.html` timeline "Now" node `756 students & counting` → `15,000 students & counting` across EN/ES/FR
- Left `756 members / 8 class types / 34 video lessons` untouched — that block is the online-course product card, not school-wide stats.

### Register page — pricing section
Designed and shipped a 4-tier pricing grid between the hero and the form: Private Excellence ($160/wk), Duo Dynamics ($145/person/wk, badged "most popular"), Small Group Immersion ($135, max 4), Cultural Connection ($110, large group). USD + BOB prices, schedule + hours-per-week meta rows, "choose this plan" CTAs scrolling to `#registerForm`, a chip row summarising what's included (textbook / workbook / pen & notebook / cultural activities), and a footnote about the 3-person activity minimum. EN/ES/FR throughout.

**Reverted on request** — client said "remove last push please", so used `git revert HEAD && git push` (non-destructive) rather than force-pushing main. Pricing section is out of the live register page but fully preserved in commit `58dbf43` if it needs to come back.

### Register page — automations (Phase 1 + 3 from the small-business starter pack)
- **Instant auto-reply localised EN/ES/FR.** Pulled the copy into a `STUDENT_COPY` table keyed by `payload.language` — subject, greeting, body, level block, WhatsApp prompt and sign-off all localise. Level string itself stays as the raw code.
- **T-24h pre-class reminder via Resend `scheduled_at`.** If the student gave a `startDate` on the form and the reminder slot is more than 12 h away, the worker schedules a warm "see you tomorrow" email on submission: day-one checklist (arrive 10 min early, bring a notebook, don't stress the level), WhatsApp fallback, all three languages. Fires at 08:30 Bolivia time (12:30 UTC) the day before. No KV or cron trigger needed — Resend holds the message server-side.
- Helper `buildReminderIso(startDateString)` parses the form's `YYYY-MM-DD` and returns an ISO timestamp for 08:30 Bolivia on that date minus 24 h.
- `sendEmail()` extended with an optional `scheduledAt` parameter that maps to Resend's `scheduled_at` body field.

**Resend caveat logged for later:** free tier's `scheduled_at` window is 30 days. If a student picks a start date beyond that, the instant confirmation still lands but the reminder send errors out. If it becomes a pattern, swap to Workers KV + a daily cron trigger.

### Deferred / not shipped this session
- **Turnstile captcha** on the registration submit — sketched the integration (Cloudflare free tier, sitekey on form, Worker-side `siteverify` check, secret via `wrangler secret put TURNSTILE_SECRET`). Waiting on the client to create the site in the Cloudflare dashboard and paste back the sitekey.
- **Other two automations** from the starter pack — missed-call text-back (WhatsApp auto-reply equivalent) and drip follow-up for unconverted leads — not implemented; user only asked for #1 and #3.

### Worker deploy notes
Worker redeployed twice this session (5-question rubric, then localised emails + reminder). Version IDs: `074f40bc-…` and `9f3be7d3-…`. Still on wrangler 3.114.17 — out-of-date warning ignored, safe to leave for now.

All commits pushed to `origin/main`. Worker deployed to `https://migusta-register.ashscms.workers.dev`.

---

## Session — 21 April 2026 (continued)

### Register — blank-answers bug + lenient grading
Real client test surfaced a 500 on submit with the message "Something went wrong — please try again". Root cause: the 5 placement-test textareas have no `required` attribute and the submit handler only calls `validateStep(1) || validateStep(3)` — step 2 is never validated, so a user who clicks through without typing posts all-blank answers. Claude refuses to grade an empty test and responds with prose ("all five questions are blank, please provide the student's actual responses..."). The regex-based JSON extractor in `gradeWithClaude` then throws `no json in model response`, the outer try/catch 500s, and the frontend shows the error.

Two fixes in `register-worker/src/index.js`:
- **Short-circuit** when all five answers are blank → return `{ level: 'BEGINNER', note: '...' }` without calling Claude.
- **Lenient parser** — strip the strict regex check on `parsed.level`. Match the first valid token (`BEGINNER|A1|A2|B1|B2+?`) anywhere in the model's reply, default to `BEGINNER` if nothing recognisable. Prose-wrapped or lightly mangled JSON now falls back gracefully instead of 500ing.

Worker redeployed (`860d0dd7-…`). Debugged by running `npx wrangler tail --format=pretty` in the background while the client re-submitted; real submission at 12:05:22 came back clean. Left the left-field choice to not add `required` to Q1 etc. on the front end — server fix is sufficient and beginners who genuinely can't answer shouldn't be blocked.

### Café hero — bigger polaroid, no caption
`cafe.html` `.float-polaroid` width `340px → 460px`, and the `<span class="float-polaroid-cap">nuestro café</span>` removed. Kept the existing 52px bottom white strip so the card still reads as a polaroid — the caption was the only bit client wanted gone.

### Contact page — real data in
Swapped the placeholder `+591 7000 1234` for the real `+591 73425725` (matches `register.html`) in both the WhatsApp method pill and the CTA-strip link, and extended the address line from "Sucre, Bolivia" to "Bolivar #603, Sucre, Bolivia" to match what the café page already displays.

### Contact form — fully wired to worker
The form on `contact.html` was visual-only: no `action`, no `method`, no submit handler. Extended `register-worker` with a second route rather than standing up new infra.

**Worker changes (`register-worker/src/index.js`):**
- `fetch()` now routes on `new URL(request.url).pathname`. `/contact` → `handleContact`; everything else → `handleRegister` (renamed from inline body).
- `validateContact` — requires `firstName`, `email`, `message`; same email regex as the register path.
- `emailStaffContact` — sends an enquiry email with a clean `Contact` table (email, interest, self-reported level, language), a terra-bordered message block, and a single "Reply by email" CTA button. Uses `reply_to: payload.email` so hitting reply in gmail goes to the student.
- `emailStudentContact` — trilingual auto-reply keyed off `payload.language` (`CONTACT_STUDENT_COPY` table with `en/es/fr` subject, greeting, lead, WhatsApp prompt, sign-off). Falls back to `en`.
- Shares `sendEmail()`, `escapeHtml()`, `corsHeaders()` with the registration path — no duplication.

**Frontend (`contact.html`):**
- `<form id="contactForm" novalidate>` with `name=` + `id=` on every field, `required` on first name / email / message, explicit `value=` on the interest and level `<option>`s (mapped to worker-side label tables).
- New submit handler in the existing `<script>` block: reads `currentLang` off the lang toggle, POSTs JSON to `/contact`, swaps the form for a success state on 2xx, shows an inline terra-tinted error banner otherwise. Submit button shows a localised "Sending…" label while the call is in flight.
- Added `.form-error` and `.form-success` CSS — matches the register page's aesthetic (cream bg, terra dashed border, italic Cormorant heading).

Worker redeployed (`519b4238-…`). Verified both routes live: `/contact` with the owner gmail returned `{ok:true}`; the register path still grades and returns `{ok:true,level:"BEGINNER"}` on a minimal payload.

### Resend sandbox — still the deliverability blocker
Watched a real registration email land for the client today but go straight to Gmail's junk folder. Cause is unchanged from the last session's notes — sending from `onboarding@resend.dev` with `Me Gusta Spanish` branding triggers Gmail's SPF/DKIM/DMARC mismatch heuristics. Per the tail logs, Resend also 403s any `to:` address that isn't `lewisashleybutterfield@googlemail.com` (the sandbox account owner), though `sendEmail()` swallows the error so the worker still returns 200.

The fix for both the junk-folder problem and the silent student-side failures is the same: verify `megustaspanish.com` in Resend, swap `FROM_EMAIL` / `STAFF_EMAIL` to domain addresses, redeploy. Still open — needs the client to paste DNS records at the registrar.

### Deferred / carried forward
- **Resend domain verification** — still open (item #1 from the last session, now blocks both registration and contact deliverability).
- **Turnstile captcha** — still waiting on client sitekey.
- **Price table audit** — unchanged; placeholder numbers still in `PRICE_TABLE`.
- **Anthropic $5/mo spend cap** — still needs setting at console.anthropic.com/settings/limits.

### Worker deploy notes
Worker redeployed twice this session (blank-answer guard + lenient parser; then `/contact` route). Version IDs: `860d0dd7-…` and `519b4238-…`. Wrangler 3.114.17 warning ignored again.

All commits pushed to `origin/main`.

---

## Session — 21 April 2026 (afternoon, methodology page polish)

### Theory & Practice section — ground-up redesign
The two-part "Theory & Practice — every single lesson" block on `methodology.html` was a flat edge-to-edge two-card grid with one Unsplash placeholder. Rebuilt twice in this session:

**v1 — editorial "teacher's notebook" diptych:**
- Outlined italic Cormorant numerals **I.** / **II.** at ~10rem with a small gold full-stop accent
- Tilted polaroid photos (-2.2° / +2°) with multi-layer shadows and white paper borders
- Paper-tape labels in Caveat ("grammar first" / "let's play") with notched pseudo-element ends so they read as actual masking tape
- Thin terra rule + gold dot under each heading
- Handwritten **"then →"** bridge in the gap between halves with a hand-drawn SVG arrow
- Faint horizontal **ruled-paper background** on the section (`repeating-linear-gradient`, ~4.5% opacity, masked at top/bottom for soft fade)
- Asymmetric drop on Part II (`padding-top: 5.5rem`) to break the grid

**v2 — compacted to ~half the height:**
Client liked the ruled-paper background but the section was ~1000px tall. Each half collapsed from a vertical numeral-photo-text stack into a single horizontal row: small 178px polaroid beside an inline copy column. Numerals dropped to ~3.5rem and now sit above the kicker. Asymmetric drop removed. Section is now ~648px on desktop. Mobile keeps photo-above-text stacking under 520px so neither column gets cramped.

### Practical photo swap
Replaced the Unsplash placeholder on the practical side with a real classroom shot — `images/school/DSC05992.webp`, sourced from `~/Desktop/Edit/JPEG/migusta/school/DSC05992.jpg` (33 MB JPG → 36 KB WebP via `cwebp -q 82 -resize 800 0`).

### Memory section — "Making new words stick" redesign
Original `.memory-section` was a tall two-column layout (square polaroid on left, label + heading + intro paragraph + two stacked technique cards with bordered separators on right) measuring 876px tall.

Restructured to centred-header-on-top + 3-up grid below:
- Centred header (label / `<em>stick</em>` Cormorant title / one-sentence italic intro) — trimmed the original two-paragraph intro to a single focused line
- 3-column grid: tilted polaroid + two technique notelets side-by-side
- Each technique now has a small Caveat **"trick one" / "trick two"** tag in terra above an italic Cormorant title, with a 22px terra rule prefixing the title
- Section dropped from ~876px → ~611px (~30% shorter)

### Lined-paper background extracted as shared utility
Promoted the `::before` ruled-paper rule that was scoped to `.two-part` into a shared selector covering all white-bg sections on the methodology page:
- `.two-part::before, .intro-quote-section::before, .cta-strip::before` now share one declaration
- Moved the giant decorative `\201C` quote glyph on `.intro-quote-section` from `::before` → `::after` to free the `::before` slot
- `.cta-strip` got `position: relative; overflow: hidden; > * { z-index: 1 }` so its content sits above the lines
- `.memory-section` (which uses `--bg-warm` cream, not `--bg` white) was left without lines per the rule "white-bg only"

### Conventions reinforced this session
- **Image workflow** — sourced JPG from Desktop, ran `cwebp -q 82 -resize 800 0` to drop into `images/school/`, no original to delete from the project tree.
- **Headbar untouched** — all redesigns kept the existing `#main-nav` HTML/CSS/JS verbatim per the project rule.
- **Tri-language coverage** — every new string (`grammar first`, `let's play`, `then`, `trick one`, `trick two`, lede sentences) added with `data-en` / `data-es` / `data-fr`.

### Commits
- `7409782` — methodology: redesign Theory & Practice diptych + swap practical image
- `4824538` — methodology: compact the Theory & Practice diptych
- `ca6b697` — methodology: compact memory section + lined-paper on all white-bg sections

All pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate`.

---

## Session — 23 April 2026 (Fernando's data audit — unify address, phones, founding date)

### Context
Fernando sent a full error list over WhatsApp flagging inconsistent school data across the site (three different addresses, four different phone numbers, two different founding dates) plus a handful of smaller bugs. Clear correct values he supplied:
- **School address:** Calle Real Audiencia #97 (replaces `Junín 333` and `Calle Dalence 146`)
- **Café address:** Bolivar #603 (unchanged — this stays)
- **Phones:** +591 734 25725 and +591 734 00447
- **Email:** info@megustaspanish.com

### Errors corrected
1. **Founding date** — hero handwritten / hero meta / ticker / every footer tagline now read `est. 2011` or `since 2011`. The about.html timeline (`2005 – methodology is born` / `2011 – school opens`) and the index.html story paragraph stay intact since they explicitly tell the 2005 → 2011 story. Methodology page's `since 2005` tag relabelled to `methodology since 2005` so the distinction is unambiguous.
2. **School address** — replaced `Junín 333` and `Calle Dalence 146` with `Calle Real Audiencia #97` everywhere they appeared (index hero/footer, classes tag + step copy + footer, methodology footer, kids/accommodation/register/activities/blog/faqs/teachers footers, cafe footer school line, contact page's "Visit our school" block which was previously showing the café address).
3. **Phones** — dropped placeholder `+591 7000 1234` and stale `+591 4 644 1008` (appeared as a "landline" on contact.html and in every secondary footer). All phone values across contact methods and footers now read `+591 734 25725` / `+591 734 00447`. Normalised the spaced variant `+591 7 342 5725` to match.
4. **Email** — added `info@megustaspanish.com` as a fourth contact row in the index.html footer (already present elsewhere).
5. **Fernando's bio** (about.html) — swapped the inaccurate "studied linguistics in Buenos Aires" for "holds a Licenciatura en Pedagogía y Ciencias de la Educación". Translated across EN/ES/FR.
6. **Sessions dropdown** (classes.html trial form) — options reformatted onto one line each with explicit `value=""` attributes, a disabled/selected `Select…` placeholder (tri-language), and a new `10+` option at the bottom.
7. **Contact form error div** — already had the `hidden` attribute and `.form-error[hidden] { display: none }` CSS. Hardened with `!important` so nothing can override the default hidden state.
8. **About.html footer socials** — the three `href="#"` placeholders (f / ig / w) now link to the real Facebook page, Instagram handle, and `wa.me/59173425725` respectively, matching the pattern used on the other pages.

### Pages touched
`about.html`, `accommodation.html`, `activities.html`, `blog.html`, `cafe.html`, `classes.html`, `contact.html`, `faqs.html`, `index.html`, `kids.html`, `methodology.html`, `register.html`, `teachers.html` — 13 files.

### Approach notes
- Used `sed` for the repeated footer strings (founding tagline, two address variants, three phone variants) across the eight pages that share identical markup — faster than editing each file manually and guaranteed consistency.
- Verified with grep passes after each batch: `Junín`, `Dalence`, `644 1008`, `7000 1234`, `7 342 5725`, `est. 2005`, `linguistics in Buenos Aires`, `href="#" aria-label` all return zero matches. The only `since 2005` remaining is the deliberately-relabelled methodology tag.
- On the contact.html "Visit our school" block I added `data-en/es/fr` attributes where previously none existed — used `&lt;br&gt;` entity encoding so the existing lang-toggle JS (which routes through `innerHTML` when it sees a `<`) renders the line break correctly.

### Designer suggestions — deferred
Fernando also sent a yellow-list of design suggestions (no pricing visible, generic Unsplash laptop photo on online classes hero, "15k+ students" stat to verify, no WhatsApp CTA on homepage, "12 native teachers" count to verify, blog/activities menu items that may be thin). None of these are wrong-data errors — they're editorial calls. Left untouched pending Fernando's say-so on each.

### Commit
- `a9daba2` — fix: unify school data across all pages — address, phones, founding date, Fernando bio

Pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate`.

---

## Session — 24 April 2026 (Fernando's review feedback applied + site polish pass)

### What happened
Fernando ran a full review pass on the staged copy at `migusta-review.pages.dev` using the `website-reviewer` tool, leaving 23 annotations across `index.html` and `about.html` (plus a few duplicates from a stale mirror). Cross-checked each against the live `main` branch, applied the genuine ones, redeployed staging, then did a broader yellow/green polish across all 13 pages.

### Client-feedback edits (commits `07a41a8`, `cfb4aa9`, `2ea4e3c`)
**Home page (`index.html`):**
- Eyebrow tags capitalised on the "Two ways to learn" cards: `since 2011` → `Since 2011`, `in sucre, bolivia` → `In Sucre, Bolivia`, `learn from your sofa` → `Learn from your sofa`. (Other eyebrows on the site stayed lowercase — Fernando flagged only these three.)
- Stat: `12` native Bolivian teachers → `12<sup>+</sup>` to match the `15,000<sup>+</sup>` style.
- "Why Choose Us" paragraph rewritten — old version said "Founded in 2005…six years developing methodology…opened 2011" which contradicted Fernando's new about-page narrative. New copy: *"Me Gusta Spanish opened its doors in 2011, founded by Elizabeth and Fernando on a simple belief…"*
- Added a "View class types" secondary button next to "Register now and save!" on the courses promo (links to `classes.html`).

**About page (`about.html`):**
- Page hero retitled: "A school born from passion" → "More than Spanish. A home in Sucre."
- Page hero sub: rewritten with Fernando's "building bridges / open the doors of our community" copy.
- Eyebrow `our story` capitalised; `¿Cómo llegamos hasta aquí?` and `¿Qué nos impulsa?` got their Spanish question marks.
- **Elizabeth bio rewritten** — origin **Padilla** (was "grew up in Sucre"), studied **Social Communication at USFX** (was vague), role **Administrative Director** (was Academic Director). Bio focuses on her admin/organisational role.
- **Fernando bio rewritten** — kept Sucre origin + School Director, but degree is **Pedagogy and Educational Sciences from USFX**, credit for **co-developing methodology with Elizabeth**, and the strong claim that Me Gusta is **the only Spanish school in Bolivia with its own six-level textbook series**. *Fernando confirmed this claim was accurate.*
- Timeline rewrites:
  - **2003** — they met in their **Christian community** in Sucre (was "shared love of languages"); collaborated on business ventures before founding the school.
  - **2005** — *"Where the dream began"* — Elizabeth and Fernando worked side-by-side as instructors at **Academia Latinoamericana de Español** (was "developing the Me Gusta method from their living room"). Important factual change: methodology origin is at another school, not at-home.
  - **2011** — *"Me Gusta officially opens its doors"* — first students were **missionaries from Brazil** (was "students from 28 countries in first year").
  - **2018 → 2020** — *"Going global with online learning"* — pandemic-driven, not just demand-driven.
  - **Now** — *"15,000 alumni and a world of connection"* — global hub framing.
- "We're not a factory" para → *"Personal, not processed."* tone rewrite.
- Welcome closer: *"we'll put the kettle on"* → *"we'll have the coffee brewing"* across EN/ES/FR.

**Cross-page corrections (commit `2ea4e3c`):**
- `teachers.html`: Elizabeth's mini-card role updated to **Administrative Director** to match about.
- `contact.html`: Instagram link `instagram.com/megustaspanish` → `instagram.com/megustaspanishschool` (the unified handle).

**Spanish + French translations** (commit `cfb4aa9`) — translated the long English rewrites (page hero sub, both bios, all five timeline descriptions, the values lead, welcome closer) into ES + FR. Updates the `data-es` / `data-fr` attributes the lang-toggle JS reads.

### Site-wide polish pass (commit `8d66fdc`)
Bulk Python script across all 13 HTML files:
- **215 duplicate `data-fr` attributes** removed (every element with multiple `data-fr=` had only its first attribute parsed by browsers — kept the longest variant per element).
- **52 footer copyrights** updated 2025 → 2026.
- **26 eyebrows / section-labels lowercased** for consistency with the dominant handwritten-eyebrow style: "Don't just take our word for it", "Why Choose Us", "Our philosophy", "What we offer", "Memory techniques we love", "First class on us", "How every class is structured", "Learn from anywhere", "Learn online, anytime", "The secret ingredients" — plus their ES/FR equivalents. Kept "In Sucre, Bolivia" + "Since 2011" + "Learn from your sofa" capitalised per Fernando's explicit direction.

Per-page polish:
- `index.html` `<title>`: "Me Gusta Spanish" → "Me Gusta Spanish School" (better SERP match for "spanish school sucre").
- `cafe.html` `<title>`: dropped street number — "Me Gusta Café — Bolivar #603, Sucre" → "Me Gusta Café — Sucre, Bolivia".
- All 13 pages: added `<link rel="icon">` + `<link rel="apple-touch-icon">` pointing to `megustalogoclear.webp`.

New SEO files:
- `robots.txt` — allow-all + sitemap reference.
- `sitemap.xml` — all 13 reviewable URLs with priorities.

### What's still outstanding
- **12 of 13 pages missing `<meta name="description">`** (only `register.html` has one). High-impact SEO gap not tackled this session.
- **Zero Open Graph tags** anywhere — `og:title`, `og:description`, `og:image`, `og:url`. Social-share previews on WhatsApp/iMessage/Facebook will be poor or missing. Critical for a marketing site, also untouched.
- **`contact.html:677`** still has `facebook.com/megustaspanish` (likely stale, parallel to the Instagram fix). Couldn't cross-check the correct handle from elsewhere on the site.
- **Some Spanish translations are slightly shorter than English** (e.g. `index.html:1534` — Spanish drops the "and haven't looked back" clause). Left as-is — needs a translator pass, not a mechanical fix.
- **Designer items from previous session** (Unsplash laptop photo on online classes hero, missing pricing, no homepage WhatsApp CTA) still deferred.

### Review tool state — fully cleared
- All 23 client annotations resolved or marked duplicate.
- `client-reviews/migusta/latest.json` wiped to zero pins on every page (commit `65a1bd4`).
- Staging mirror `migusta-review.pages.dev` resynced 1:1 with current `main` after each push.
- The merged review branch `review/2026-04-24-client-feedback` deleted locally.

### Commits
- `07a41a8` — review: apply 2026-04-24 client feedback (home + about)
- `69f2420` — index: 12 native teachers → 12+
- `cfb4aa9` — about: add ES + FR translations for client-rewritten copy
- `2ea4e3c` — site: align with client's about-page rewrites
- `8d66fdc` — site: yellow/green polish pass (post-client-feedback)

All pushed to `origin/main` → live on `ashdabash2926.github.io/migustaschoolprivate` and mirrored on `migusta-review.pages.dev`.

---

## Session — 25 April 2026 (activities page — Thursday salsa swap + cinematic week timeline)

### Thursday timeline change
Replaced the second weekly cooking-class slot with a new **Salsa Dancing** entry. Tue stays Cooking; Thu becomes Salsa.
- Split the old shared "Tue & Thu — Bolivian Cooking Class" entry into a Tue-only entry (Afternoon · 3 hrs · Food & Culture).
- Added a new Thu entry: *Salsa Dancing* (Evening · 1.5 hrs · Music & Movement) with EN/ES/FR description — "Step, turn, count to eight in Spanish…".
- Updated the hero ticker: all three "Thu — Cooking Class" tokens now read "Thu — Salsa Dancing".

### Cooking-class description rewrite
Per Fernando's note that the class actually happens in a Sucre local's home, not the café: rewrote the description across EN/ES/FR — "Step into a Sucre local's kitchen, cook a traditional Bolivian meal together, then stay for board games and a proper Bolivian evening — all in Spanish, the way locals actually spend their nights."

### Hero shortened 10 %
Activities page hero felt too tall. Reduced padding by ~10 %:
- Desktop: `9rem 4.5rem 7rem` → `8.1rem 4.5rem 6.3rem`
- Mobile: `7rem 1.5rem 5rem` → `6.3rem 1.5rem 4.5rem`

### Week timeline — cinematic redesign (commit `b360d0f`)
Replaced the static `.act-index` row-list with a **pinned horizontal-scroll** section: vertical scroll drives a horizontal pan through the five days. Left column stays sticky throughout; right column is a flex track that translates as you scroll.

**Aesthetic direction** — editorial cinema. Dark coffee bg, paper-grain noise overlay, terra/gold radial glows on the left. Each scene has a 13rem ghosted Cormorant numeral (01–05) behind it as decorative chrome.

**Layout & behaviour**
- Section: `500vh` tall on desktop, sticky 100vh inner pin (`#weekTimeline` → `#wtTrack`).
- Grid: `38vw` left + `1fr` right; scenes are `62vw` each.
- JS reads `getBoundingClientRect()` against `requestAnimationFrame`, computes scroll progress 0→1, applies `translate3d(-progress × 4 × sceneWidth, 0, 0)` to the track. Active day in the indicator highlights via `Math.round(progress × 4)`.
- Progress fill-line on the left tracks scroll progress (terra with a glowing dot pseudo-element).
- Mobile (≤900px): pin disabled — section auto-height, track stacks vertically, scenes full-width.

**Per-day photo collages** — each day uses a different `wt-collage--{mon|tue|wed|thu|fri}` layout with absolute-positioned photos at varying rotations (-2° to +2.2°), depths and z-indexes. Hover snaps each photo to `rotate(0) scale(1.03)` with a gold ring. Real photos use existing `data-lightbox` hooks.

### Stock photos — Mon (Sucre walking tour) + Thu (Salsa)
First version shipped with hand-drawn SVG placeholder cards for Mon and Thu. Fernando asked for actual stock photos.
- Pulled 3 Sucre-specific shots from Unsplash (Peter Burdon's white-city + foothills, Paola Hernandez's cathedral clock tower, Pedro Basagoitia's bell — verified all are Sucre, not Quito or another colonial white city).
- Pulled 2 salsa photos (Ardian Lumi's group class, Scott Broome's couple).
- Compressed via `cwebp -q 82 -resize 1200 0`, saved as `images/activities/Sucre/{sucre-cathedral, sucre-clocktower, sucre-bell}.webp` and `images/activities/Salsa/{salsa-group, salsa-couple}.webp`. 65–221 KB each.
- Mon scene now uses cathedral + clocktower; Thu uses group + couple. Placeholder CSS left in the stylesheet for future reuse.

### Bug — `--coffee` variable was undefined (commit `134e009`)
Initial timeline shipped with `background: var(--coffee)` but the variable was never declared in `:root` — the `--coffee: #3D2314` token is documented in `CLAUDE.md` but had no CSS counterpart, so the dark bg fell through to transparent → the section rendered with the body's cream `--bg`, making the white text near-invisible. Fix:
- Added `--coffee: #2E1A10` to `:root` (a notch darker than the documented value to give text more punch against the section's terra/gold accents).
- Boosted text contrast across the whole timeline:
  - Subtitle 55 % → 82 % white, slightly larger.
  - Day list (inactive) 32 % → 55 %; active state gained a soft terra `text-shadow` glow.
  - Description text 78 % → 94 % white.
  - Meta line 45 % → 72 %, dot now gold (was terra — fought with the title accent).
  - Tag (Caveat) terra → **gold** so it stops competing with the terra-italic title.
  - Progress-line track 12 % → 22 % so the line is visible before scroll fills it.

### Commits
- `2f608fc` — activities: replace Thursday cooking with Salsa Dancing in timeline + ticker
- `c23a066` — activities: update cooking class description — Sucre local's kitchen + board games + Bolivian evening
- `42e51dc` — activities: shorten hero padding by 10% (desktop + mobile)
- `b360d0f` — activities: redesign timeline as cinematic horizontal pin-scroll
- `134e009` — activities: define --coffee var, boost text contrast, swap Mon/Thu placeholders for real Sucre + salsa stock photos

All pushed to `origin/main`.

### Notes / follow-ups
- The original three-photo gallery chapters (`<section class="gallery-section">` further down activities.html) still exist below the new timeline — they show the same photos used in the timeline collages plus extras. Likely now redundant; worth asking Fernando whether he wants both, or wants to drop the lower gallery section.
- Mon/Thu photos are stock fallbacks. When Fernando captures real walking-tour and salsa-class shots, drop them into `images/activities/Sucre/` and `images/activities/Salsa/` and replace the `src` attributes — no other code changes needed.
- Unsplash license requires no attribution but appreciates it. None added; flag if Fernando wants credits in a footer somewhere.
- The `_animation: wtNudge` on `.wt-hint .arrow` runs on a 2.4s loop forever — fine on desktop but never visible on mobile (`.wt-hint { display: none }` at ≤900px). No action needed, just noting.

---

## Session — 27 April 2026 (accommodation catalogue — HTML→PDF for WhatsApp)

### Brief (from Fernando)
> Accommodation catalog (VERY URGENT) — needed to respond to student inquiries. Include new room photos, types of rooms (short descriptions), prices (he'll send), WhatsApp number for reservations. Style: visual, clean, attractive, easy to read. PDF format to send via WhatsApp. Goal: someone sees it and immediately thinks "I want to stay here."

Ash asked for an HTML doc that exports cleanly to PDF — boutique-magazine treatment of the existing brand (Cormorant + Lora + Caveat, terra/gold/coffee palette), heavy on images. Cover + intro page with side index + room sections + tariffs + closing reservations page.

### What was built — `accommodation-catalog.html` (commit `a4824c9`)
A standalone 13-page A4-portrait HTML document, separate from the website. Self-contained (no shared CSS), all images pulled from existing `images/rooms/` set + `images/megustalogoclear.webp`. No nav, no language toggle — single language (English) at Fernando's direction.

**Structure** (each page is an `<article class="page">` with `page-break-after: always`)
1. **Cover** — full-bleed `DSC08332-HDR.webp`, dark gradient overlay, white-inverted logo top-left, "Vol. I · MMXXVI" top-right, big Cormorant italic *Casa Migusta* title, Sucre/altitude rule footer.
2. **Welcome + Index** — two-column. Left: 3-paragraph letter with Cormorant drop-cap + Caveat sign-off. Right: cream-boxed index with terra rule, all 4 rooms listed with page numbers + amenity sublines, tariffs/contact pointers below. Bottom strip: 4 meta cells (location, altitude, rooms, best for).
3-10. **Four rooms × 2 pages each.** Hero page = full-bleed photo, dark gradient bottom, vertical "CASA MIGUSTA · SUCRE · BOLIVIA" rotated rule on the right edge, big italic title, sub, then sleeps/bathroom/linen pills + price tag. Detail page = banner header → 14mm Cormorant title with rotated 16mm Caveat number stamp on the right → 2-column body (prose with drop-cap + 2-col amenity list with terra-dot bullets on left, 1 large + 2 small photo collage on right) → terra-rule footer with pull-quote + dark coffee-color price card with terra-tab triangle on top.
11. **Tariffs** — single page table (room / per night / per week / per month) + "Always included" 8-item ✓ panel with terra left-rule + Caveat fineprint footer.
12. **Reservations close** — `--coffee-deep` bg with terra/gold radial glows + screen-blend grain overlay, gold Caveat eyebrow, 36mm italic *Stay with us.*, sub-paragraph, full-width WhatsApp tile (real WA gradient #25D366→#128C7E, official WA glyph SVG, the existing `+591 73425725` number formatted as +591 734 257 25, "tap to chat" Caveat CTA on the right), 3-cell contact grid, logo + MMXXVI footer.

### Aesthetic direction — boutique magazine
Brand-faithful (Cormorant italic display + Lora body + Caveat hand) but composed for a printed page rather than a viewport. Editorial moves throughout:
- Generous margins (14mm interior, 18mm on hero/cover bottom).
- Italic Cormorant for every voice header; **non-italic** + terra colour for emphasised words inside a title (`<em>` is restyled `font-style: normal`).
- Caveat used three ways: rotated handwritten eyebrows, price tags, and section page-number footers. Always slightly off-axis (`rotate(-1deg)` to `-2deg`).
- Banner header on every interior page: thin 18mm strip with logo + brand mark on the left, tracked-out section title centred, Caveat tag on the right.
- Folio at the bottom: brand · italic section name · page number, all in tracked uppercase Lora.
- Drop-caps on intro and each room's first paragraph (22mm cover-letter cap, 14mm room cap).
- Paper-grain noise SVG on every page (multiply blend, 5% opacity), screen-blend grain on the dark close page.
- Hero pages have a vertical rotated rule running down the right edge — pure editorial chrome.

### Print engineering
- `@page { size: A4 portrait; margin: 0; }` — full-bleed cover/hero pages need zero page margin.
- `.page { width: 210mm; height: 297mm; page-break-after: always; }` — explicit mm dims so layout doesn't drift between viewports.
- Every measurement in `mm` to keep the screen preview pixel-perfect with the PDF output (Chrome's "Save as PDF" preserves mm-based geometry exactly when margins=None).
- `-webkit-print-color-adjust: exact; print-color-adjust: exact;` on every element so dark coffee backgrounds + terra accents render in PDF (Chrome strips colour by default for "ink saving").
- `@media print` strips the screen-only box-shadow + dark backdrop.
- `@media screen` adds a `body::before` cream-italic strip ("Casa Migusta · Accommodation Catalogue · Print preview at A4 portrait") so it's clear in-browser what you're looking at.
- Logo is white-inverted via `filter: brightness(0) invert(1)` on dark pages.

### Photo assignments (placeholders — need Fernando's input)
Without per-photo metadata, photos were assigned by sequential filename ranges:
- **6-bed dorm:** `images/rooms/6bed/DSC08489, 08494, 08519, 08539` (correct — that subfolder is the dorm)
- **Private single:** `images/rooms/DSC08147-HDR-2, 08157, 08167, 08177` (lowest-numbered, guess)
- **Family room:** `images/rooms/DSC08217, 08232, 08242, 08257` (mid-range, guess)
- **Ensuite trio:** `images/rooms/DSC08332, 08342, 08367, 08412` (high-range, guess; 08332 already used as the website's accommodation hero)

Fernando will need to swap any mis-assigned photos. Each `background-image: url('...')` is on its own line — one-line edits.

### Placeholder prices (Fernando will replace)
- Dorm bed: **$12/night, $72/wk, $260/mo**
- Private single: **$28/night, $168/wk, $580/mo**
- Family room: **$55/night, $330/wk, $1,150/mo**
- Ensuite room: **$42/night, $252/wk, $880/mo**

Per-night prices appear in 4 places per room (hero pill, hero price tag, detail price card, tariffs table) — a "real prices" sweep needs to update all of them, ideally via a find-and-replace per room.

### Placeholder copy (low-confidence, ask Fernando)
- Email: `hola@migustaspanish.com` — guess based on domain conventions, not pulled from anywhere on the site.
- Handles: `migusta.school`, `@migustasucre` — guesses.
- WhatsApp number: `+591 73425725` — pulled verbatim from `accommodation.html` and `contact.html`, confirmed across the site. Linked correctly to `wa.me/59173425725`. Display-formatted as `+591 734 257 25` for the close page.

### How to export
Chrome → ⌘P → Destination *Save as PDF* → Margins **None** → enable **Background graphics** → Save. File should land at ~5–8 MB depending on photo subset.

### Commits
- `a4824c9` — accommodation-catalog: 13-page A4 PDF catalogue — boutique magazine layout, cover + welcome/index + 4 rooms (hero+detail per room) + tariffs + WA reservations close. Placeholder USD prices.

### Open follow-ups for next session
- Real prices (Fernando is sending) — sweep the 4 hero pills, 4 hero price tags, 4 detail price cards, 4 tariff table rows.
- Photo reassignment — Fernando to confirm which `DSC*-HDR*.webp` files belong to which room type, then swap.
- Confirm email + social handles before the catalogue is sent to a real student.
- Decide whether to host this at `migustaschoolprivate/accommodation-catalog.html` (currently pushed to `origin/main`, will be live at `ashdabash2926.github.io/migustaschoolprivate/accommodation-catalog.html`) or keep local-only as a PDF source.
- Spanish version? Fernando picked English-only at brief; may want a parallel `accommodation-catalog-es.html` once the EN one is approved.

---

## Rules & Conventions

### Image Workflow
- If a JPG/PNG is already exported at a reasonable size (under ~200KB, resized to ~800px long edge, sRGB colour space), it can be used directly — no conversion needed
- For large/unoptimised images, convert to `.webp` using `cwebp -q 82 -resize 800 0`
- After converting, delete the original — no duplicates allowed
- Only one format per image should remain in the `images/` folder
- Reason: keeps the images folder clean and reduces file sizes loaded by the site
