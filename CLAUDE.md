# Migusta — Claude Instructions

## Project Overview

Me Gusta Spanish — a Spanish language school in Bolivia. Multi-page static site with EN/ES language toggle.

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

`index.html`, `classes.html`, `methodology.html`, `teachers.html`, `cafe.html`, `about.html`, `accommodation.html`, `faqs.html`, `blog.html`, `contact.html`

---

## Rules & Conventions

### Image Workflow
- **Always convert images to `.webp` before using them in the site**
- After converting, delete the original (jpg/png/etc) — no duplicates allowed
- Only the `.webp` version should remain in the `images/` folder
- Reference the `.webp` path in the HTML
- Reason: keeps the images folder clean and reduces file sizes loaded by the site

### Language Toggle
- All user-facing text must have both `data-en` and `data-es` attributes
- Toggle is handled by existing JS — just add the attributes correctly

### General
- No frameworks — vanilla JS only
- No Tailwind — use the existing CSS custom properties
- Mobile-first responsive design
- Always commit and push to `origin main` after changes
