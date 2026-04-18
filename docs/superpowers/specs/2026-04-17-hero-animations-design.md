# Hero Section Animations — Design

**Date:** 2026-04-17
**Page:** `index.html` (hero section only)
**Scope:** Add four animations to the existing hero. CSS-only where possible; minimal JS for parallax. All changes inline in `index.html`.

---

## Goals

Add subtle motion that reinforces the warm, handcrafted, scrapbook feel of the site without competing with the copy or hurting performance.

## Animations

### Background layer refactor (prerequisite for #1 and #4)

The current hero uses an inline `style="background-image: ..."` on the `<section>`. To enable both Ken Burns *and* parallax cleanly, move the background to a `.hero::before` pseudo-element (absolutely positioned, `inset: 0`, `z-index: 0`). Ken Burns animates its `background-size` / `background-position`; parallax animates its `transform: translate3d`. The two animations don't conflict because they target different properties. The inline `style` attribute on `<section class="hero">` is removed.

### 1. Ken Burns on background image

The hero's background photo (`images/school/DSC06152.webp`) slowly pans and zooms.

- **Mechanism:** CSS `@keyframes` animating `background-size` and `background-position` on `.hero::before`
- **Range:** `background-size` 131% → 140%; `background-position` drifts ~3% diagonally
- **Duration:** 28s, `ease-in-out`, `alternate`, infinite

### 2. Polaroid drop-in (replaces existing fadeUp on `.hero-right`)

The polaroid drops in from above and settles into its rotated position with a small overshoot.

- **Mechanism:** New `@keyframes polaroidDrop` replaces the current `fadeUp` animation on `.hero-right`
- **From:** `opacity: 0; transform: translateY(-120%) rotate(-12deg)`
- **To:** `opacity: 1; transform: translateY(0) rotate(2.5deg)`
- **Timing:** `1.1s cubic-bezier(0.34, 1.56, 0.64, 1) 0.45s forwards` (overshoot/settle)
- **Existing hover behaviour preserved:** `.polaroid:hover { transform: rotate(0.5deg) scale(1.015); }`

### 3. Hand-drawn underline under "fun & friendly"

A wavy SVG squiggle draws itself under the italic terra-cotta line in the title.

- **Mechanism:** Inline SVG appended after the `<em>` containing "fun & friendly", positioned absolutely below it
- **Path:** Slightly wavy curve (~3 gentle bumps), not a straight line — matches Caveat handwriting feel
- **Stroke:** `var(--terra)`, 3px, round caps
- **Animation:** `stroke-dasharray` + `stroke-dashoffset` keyframe to draw the stroke from 0 → full length over 0.9s, `ease-out`, delay 1.4s (lands just after title fade-up completes)
- **Layout:** SVG sits inside the `<em>` or as a sibling, positioned with `position: absolute` so it doesn't affect text flow. Width matches the italic line; `viewBox` keeps it scalable.

### 4. Parallax on scroll

Background and polaroid move at different rates relative to scroll, only while the hero is in view.

- **Mechanism:** Single JS scroll listener using `requestAnimationFrame`
- **Background:** `transform: translate3d(0, scrollProgress * 0.4, 0)` applied to `.hero::before` (the same element Ken Burns runs on)
- **Polaroid:** rotation eases from 2.5° → 6° as the hero scrolls out, using a normalized scroll progress
- **Performance:** rAF-throttled, `will-change: transform` on animated elements, listener detaches via `IntersectionObserver` when hero exits viewport
- **JS location:** added to the existing `<script>` block at the bottom of `index.html`

---

## Cross-cutting concerns

### Reduced motion

Wrap Ken Burns, parallax, and the polaroid bounce in:

```css
@media (prefers-reduced-motion: no-preference) { ... }
```

When `prefers-reduced-motion: reduce` is set:
- Ken Burns: disabled (static background)
- Parallax: JS checks `matchMedia` and skips initialization
- Polaroid drop-in: falls back to a simple fade (existing `fadeUp`)
- Underline draw: still draws (it's a one-time short animation, not vestibular-triggering) but instantly visible if reduced motion is preferred

### Mobile (≤768px)

- **Parallax:** disabled (scroll performance + the hero layout collapses to single column with a different blob shape, parallax adds little visually)
- **Ken Burns:** keep, but slow to 40s duration
- **Polaroid drop-in:** keep
- **Underline draw:** keep

### Files touched

- `index.html` — only file changed. New CSS in the `<style>` block, new SVG inline in the title, new JS in the existing `<script>` block.

### Out of scope

- No new image assets
- No font changes
- No layout/structural changes to the hero
- No changes to other pages

---

## Acceptance criteria

1. Ken Burns visibly pans/zooms the background, looping seamlessly
2. Polaroid enters from above with a small overshoot, then sits at its 2.5° tilt; hover still works
3. SVG underline draws in cleanly under "fun & friendly" after the title settles
4. Scrolling causes the background to lag behind page scroll and the polaroid rotation to increase
5. `prefers-reduced-motion: reduce` disables Ken Burns, parallax, and the polaroid bounce
6. On mobile (≤768px) parallax is off; other animations behave as specified
7. No console errors; no visible jank during scroll
8. Translations (`data-en` / `data-es` / `data-fr`) on the title remain functional
