# Migusta — Claude Instructions

## Project Overview

Me Gusta Spanish — a Spanish language school in Bolivia. Multi-page static site with EN/ES/FR language toggle.

**Stack:** HTML, CSS (custom properties, no Tailwind), Vanilla JS  
**Repo:** `github.com/Ashdabash2926/migustaschoolprivate` (private)

---

## Design System

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

## Pages

`index.html`, `classes.html`, `kids.html`, `methodology.html`, `teachers.html`, `activities.html`, `cafe.html`, `about.html`, `accommodation.html`, `faqs.html`, `blog.html`, `contact.html`

---

## Rules & Conventions

### Image Workflow
- If a JPG/PNG is already exported at a reasonable size (under ~200KB, resized to ~800px long edge, sRGB colour space), it can be used directly — no conversion needed
- For large/unoptimised images, convert to `.webp` using `cwebp -q 82 -resize 800 0` before using in the site
- After converting, delete the original — no duplicates allowed
- Only one format per image should remain in the `images/` folder
- Reason: keeps the images folder clean and reduces file sizes loaded by the site

### Language Toggle
- All user-facing text must have `data-en`, `data-es`, and `data-fr` attributes (English, Spanish, French)
- Toggle is handled by existing JS — just add the attributes correctly
- **Whenever new text or content is added to any page, it must be translated across all 3 languages**

### General
- No frameworks — vanilla JS only
- No Tailwind — use the existing CSS custom properties
- Mobile-first responsive design
- Always commit and push to `origin main` after changes
