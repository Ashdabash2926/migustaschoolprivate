# Hero Animations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add four hero-section animations (Ken Burns background, polaroid drop-in, hand-drawn underline, scroll parallax) to `index.html` while respecting `prefers-reduced-motion` and mobile constraints.

**Architecture:** All changes inline in `index.html`. CSS in the existing `<style>` block, an SVG inline in the hero markup, parallax JS in the existing `<script>` block. Background image moves from inline-style on `<section>` to a `.hero::before` pseudo-element so Ken Burns and parallax can both target it cleanly without conflict.

**Tech Stack:** Vanilla HTML / CSS / JS. No framework, no build step. Verification is visual (browser preview) — there is no automated test suite on this static site.

**Spec:** `docs/superpowers/specs/2026-04-17-hero-animations-design.md`

---

## File Structure

**Modified file (only file touched):**
- `index.html`

**Logical regions inside `index.html` and what each task changes:**

| Region | Lines (approx, pre-change) | Task |
|---|---|---|
| `<style>` — `.hero` block | 236–245 | Tasks 1, 2, 5 |
| `<style>` — `.hero-right` rule | 380–388 | Task 3 |
| `<style>` — `@keyframes fadeUp` area | 1209–1216 | Tasks 2, 3, 4 |
| `<style>` — `@media (max-width: 960px)` | 1236–1242 | Task 6 |
| `<style>` — end (`</style>`) | 1292 | Task 6 (reduced-motion block goes just before this) |
| `<section class="hero">` opening tag | 1368 | Task 1 |
| Hero `<h1>` `<em>` element | 1375 | Task 4 |
| `<script>` block | 1672+ | Task 5 |

---

## Verification approach

There is no JS/CSS test framework on this site. After each task that changes visible behaviour:

1. Open `index.html` in a browser (use `open index.html` from the project root, or run `python3 -m http.server 8000` and visit `http://localhost:8000/`).
2. Hard-reload the page (Cmd+Shift+R) to bypass cache.
3. Visually verify the described behaviour. Check the browser console for errors.

Each task lists **exactly what you should see**.

---

## Task 1: Refactor hero background to a `::before` pseudo-element

**Why:** The current background is an inline `style` attribute on the `<section>`. Both Ken Burns (animates `background-size` / `background-position`) and parallax (animates `transform`) need a single dedicated layer to act on. Moving the background to `.hero::before` decouples it from the section's own transforms and gives both animations one clean target.

**Files:**
- Modify: `index.html` — `.hero` CSS block (around line 236) and the `<section class="hero">` opening tag (around line 1368).

- [ ] **Step 1: Add the `::before` rule and update `.hero` to be a positioning context (it already is `position: relative`)**

In the `<style>` block, replace the existing `.hero` rule (currently lines ~236–245):

```css
    .hero {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      align-items: center;
      padding: 9rem 4.5rem 6rem;
      position: relative;
      overflow: hidden;
      gap: 5rem;
    }
```

with this (adds the `::before` pseudo-element carrying the background image — properties match what the inline `style` attribute used to set):

```css
    .hero {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      align-items: center;
      padding: 9rem 4.5rem 6rem;
      position: relative;
      overflow: hidden;
      gap: 5rem;
    }

    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url('images/school/DSC06152.webp');
      background-position: 0% 24%;
      background-size: 131%;
      background-repeat: no-repeat;
      z-index: 0;
      will-change: transform, background-position, background-size;
    }
```

- [ ] **Step 2: Strip the inline `style` attribute from the hero `<section>`**

Find the line (around 1368):

```html
  <section class="hero" id="hero" style="background-image: url('images/school/DSC06152.webp'); background-position: 0% 24%; background-size: 131%;">
```

Replace with:

```html
  <section class="hero" id="hero">
```

- [ ] **Step 3: Visually verify — hero looks identical**

Open `index.html` in a browser. Hard-reload. The hero should look exactly the same as before this task — same background image, same crop, same content layout. The blobs (`.hero-blob`, `.hero-blob-left`) should still appear in front of the background (they have `z-index: 0` and `1`; the `::before` is `z-index: 0` and renders before them in DOM order, so they layer correctly). The text and polaroid have `z-index: 2` and stay on top.

If the blobs appear *behind* the background image, raise the blobs' z-index by 1 (set `.hero-blob` to `z-index: 1` and `.hero-blob-left` to `z-index: 2`, then the polaroid/text container `z-index` will already be higher).

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "hero: move background to ::before pseudo-element

Prerequisite for Ken Burns and parallax animations — both need a
single transformable layer to target without conflict."
```

---

## Task 2: Ken Burns animation on the background

**Files:**
- Modify: `index.html` — add `@keyframes kenBurns` near the existing keyframes (around line 1212), add `animation` property to `.hero::before` (the rule added in Task 1).

- [ ] **Step 1: Add the keyframe**

In the `<style>` block, locate the existing `@keyframes fadeUp` (around line 1209). Immediately after it (after the closing `}` of `@keyframes ticker` at ~line 1216 is fine too — anywhere in the keyframes area), add:

```css
    @keyframes kenBurns {
      0%   { background-size: 131%; background-position: 0% 24%; }
      100% { background-size: 140%; background-position: 3% 27%; }
    }
```

- [ ] **Step 2: Apply the animation to `.hero::before`**

Find the `.hero::before` rule (added in Task 1) and add an `animation` line:

```css
    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url('images/school/DSC06152.webp');
      background-position: 0% 24%;
      background-size: 131%;
      background-repeat: no-repeat;
      z-index: 0;
      will-change: transform, background-position, background-size;
      animation: kenBurns 28s ease-in-out infinite alternate;
    }
```

- [ ] **Step 3: Visually verify**

Reload `index.html`. Watch the hero for ~30 seconds. The background photo should *very slowly* zoom in and pan slightly diagonally, then reverse. The motion should be barely perceptible at any single moment but obvious if you look away and look back. No jank, no jumps.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "hero: add slow Ken Burns animation to background"
```

---

## Task 3: Polaroid drop-in with overshoot

**Files:**
- Modify: `index.html` — add `@keyframes polaroidDrop` near other keyframes (around line 1212), update `.hero-right` rule (around line 380–388) to use the new animation.

- [ ] **Step 1: Add the keyframe**

In the `<style>` block, after `@keyframes kenBurns` (added in Task 2), add:

```css
    @keyframes polaroidDrop {
      0%   { opacity: 0; transform: translateY(-120%) rotate(-12deg); }
      100% { opacity: 1; transform: translateY(0) rotate(2.5deg); }
    }
```

Note: the polaroid sits inside `.hero-right`, but `.hero-right` is a flex container — applying transform/rotate to it is what we want, since the existing fade-up already animates `.hero-right`.

Wait — the existing `.polaroid` itself has `transform: rotate(2.5deg)`. If we animate `.hero-right`'s transform, the polaroid's own rotate is independent and stays at 2.5deg the whole time. The drop-in needs to land at the polaroid's natural tilt visually, which means animating `.hero-right`'s `transform` to `translateY(0) rotate(0)` and letting the polaroid's own rotate of 2.5deg sit on top.

Updated keyframe (final landing point is `rotate(0)` on `.hero-right`, which lets the polaroid's own 2.5deg rotation show through):

```css
    @keyframes polaroidDrop {
      0%   { opacity: 0; transform: translateY(-120%) rotate(-12deg); }
      100% { opacity: 1; transform: translateY(0) rotate(0deg); }
    }
```

- [ ] **Step 2: Update `.hero-right` to use the new animation**

Find the `.hero-right` rule (around lines 380–388):

```css
    .hero-right {
      position: relative;
      z-index: 2;
      display: flex;
      justify-content: center;
      align-items: center;
      opacity: 0;
      animation: fadeUp 1s ease 0.45s forwards;
    }
```

Replace the `animation` line so the rule becomes:

```css
    .hero-right {
      position: relative;
      z-index: 2;
      display: flex;
      justify-content: center;
      align-items: center;
      opacity: 0;
      animation: polaroidDrop 1.1s cubic-bezier(0.34, 1.56, 0.64, 1) 0.45s forwards;
    }
```

- [ ] **Step 3: Visually verify**

Hard-reload `index.html`. Watch the right side of the hero on page load. The polaroid (with the students photo) should fall in from above the hero, with a slight tilt during the fall, then settle into its 2.5° rest tilt with a small overshoot/bounce. Total motion ~1.1 seconds, starting 0.45s after page load.

Hover over the polaroid: it should still rotate to ~0.5deg and scale up 1.5% (existing hover behaviour, unchanged).

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "hero: polaroid drops in with overshoot instead of fading up"
```

---

## Task 4: Hand-drawn underline under "fun & friendly"

**Files:**
- Modify: `index.html` — add `.hero-underline` CSS rule and `@keyframes drawUnderline` in `<style>`, add inline SVG inside the hero `<h1>` next to the `<em>`.

- [ ] **Step 1: Add the CSS for the underline SVG**

In the `<style>` block, near the other hero CSS rules (after `.hero-title em` at ~line 298 is a good spot), add:

```css
    .hero-title em {
      position: relative;
      display: inline-block;
    }
    .hero-underline {
      position: absolute;
      left: 0;
      right: 0;
      bottom: -0.2em;
      width: 100%;
      height: 0.35em;
      pointer-events: none;
      overflow: visible;
    }
    .hero-underline path {
      fill: none;
      stroke: var(--terra);
      stroke-width: 3;
      stroke-linecap: round;
      stroke-dasharray: 300;
      stroke-dashoffset: 300;
      animation: drawUnderline 0.9s ease-out 1.4s forwards;
    }
```

Note: the existing `.hero-title em` rule (line ~298) already sets `font-style: italic; font-weight: 500; color: var(--terra);`. We need to **augment** it, not replace it. So instead of adding a new `.hero-title em` rule, find the existing one:

```css
    .hero-title em { font-style: italic; font-weight: 500; color: var(--terra); }
```

and replace it with:

```css
    .hero-title em { font-style: italic; font-weight: 500; color: var(--terra); position: relative; display: inline-block; }
```

Then add only the `.hero-underline` and `.hero-underline path` rules (and the keyframe in the next step).

- [ ] **Step 2: Add the keyframe**

After `@keyframes polaroidDrop` (added in Task 3), add:

```css
    @keyframes drawUnderline {
      to { stroke-dashoffset: 0; }
    }
```

- [ ] **Step 3: Add the inline SVG inside the `<em>` in the hero title**

Find the hero title (around line 1373–1377):

```html
      <h1 class="hero-title">
        <span data-en="Probably the most" data-es="Probablemente la escuela" data-fr="Probablement la plus">Probably the most</span><br>
        <em><span data-en="fun &amp; friendly" data-es="más divertida" data-fr="fun &amp; accueillante">fun &amp; friendly</span></em><br>
        <span data-en="Spanish School in Sucre!" data-es="Probablemente la escuela" data-fr="École d'espagnol à Sucre !">Spanish School in Sucre!</span>
      </h1>
```

Inside the `<em>`, after the inner `<span>`, add the SVG so the line becomes:

```html
        <em><span data-en="fun &amp; friendly" data-es="más divertida" data-fr="fun &amp; accueillante">fun &amp; friendly</span><svg class="hero-underline" viewBox="0 0 300 12" preserveAspectRatio="none" aria-hidden="true"><path d="M2,8 Q40,2 80,7 T160,6 T240,8 T298,5"/></svg></em>
```

The path is a slightly wavy curve using SVG `Q` (quadratic) and `T` (smooth quadratic) commands, drawn across a 300×12 viewBox stretched to fill the `<em>`'s width.

- [ ] **Step 4: Visually verify**

Hard-reload `index.html`. After the title fades in (~1.4s after load), a wavy terra-cotta underline should draw itself under "fun & friendly" from left to right over about 0.9 seconds. The line should look slightly hand-drawn (not perfectly straight) and span the width of the italic phrase.

Switch the language to Spanish using the language toggle. The underline should now sit under "más divertida" (the new italic text). Same for French.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "hero: add hand-drawn underline that animates under fun & friendly"
```

---

## Task 5: Scroll parallax (background + polaroid rotation)

**Files:**
- Modify: `index.html` — add JS at the top of the existing `<script>` block (just inside `<script>` at line 1672).

**Why these targets:** The background lives on `.hero::before`, so parallax on the background applies a `transform` to that pseudo-element via a CSS variable on `.hero`. The polaroid rotation is applied to `.polaroid` directly (not `.hero-right`) because `.hero-right`'s transform is already owned by the `polaroidDrop` entrance animation — we don't want to fight it.

- [ ] **Step 1: Add the parallax JS**

Find the `<script>` block (line 1672 and below). Just inside the `<script>` tag, *before* the existing `// STICKY NAV` block, add:

```javascript
    //  HERO PARALLAX 
    (() => {
      const hero = document.getElementById('hero');
      const polaroid = document.querySelector('.hero .polaroid');
      if (!hero || !polaroid) return;

      // Skip on mobile (matches the @media breakpoint that hides hero-blob)
      if (window.matchMedia('(max-width: 960px)').matches) return;

      // Skip if user prefers reduced motion
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

      let heroVisible = true;
      let ticking = false;

      // Detach scroll work when hero leaves the viewport
      const io = new IntersectionObserver((entries) => {
        heroVisible = entries[0].isIntersecting;
      }, { threshold: 0 });
      io.observe(hero);

      const update = () => {
        ticking = false;
        if (!heroVisible) return;
        const rect = hero.getBoundingClientRect();
        const heroHeight = rect.height || 1;
        // 0 at top of hero in view, 1 when hero is fully scrolled past
        const progress = Math.min(Math.max(-rect.top / heroHeight, 0), 1);

        // Background lags scroll at ~0.4x
        hero.style.setProperty('--parallax-y', `${progress * heroHeight * 0.4}px`);

        // Polaroid rotation eases from 0 → 3.5 extra degrees (on top of polaroid's own 2.5deg)
        polaroid.style.setProperty('--parallax-rot', `${progress * 3.5}deg`);
      };

      window.addEventListener('scroll', () => {
        if (!ticking) {
          requestAnimationFrame(update);
          ticking = true;
        }
      }, { passive: true });

      update();
    })();

```

- [ ] **Step 2: Wire `--parallax-y` into `.hero::before`**

Find the `.hero::before` rule (last updated in Task 2). Add a `transform` line. Final rule:

```css
    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url('images/school/DSC06152.webp');
      background-position: 0% 24%;
      background-size: 131%;
      background-repeat: no-repeat;
      z-index: 0;
      will-change: transform, background-position, background-size;
      animation: kenBurns 28s ease-in-out infinite alternate;
      transform: translate3d(0, var(--parallax-y, 0), 0);
    }
```

(CSS variables cascade into pseudo-elements, so `--parallax-y` set on `.hero` is readable on `.hero::before`.)

- [ ] **Step 3: Wire `--parallax-rot` into `.polaroid`**

Find the existing `.polaroid` rule (around line 390):

```css
    .polaroid {
      background: #fff;
      padding: 14px 14px 52px;
      box-shadow: var(--shadow-warm), 0 0 0 1px rgba(74,58,44,0.06);
      transform: rotate(2.5deg);
      transition: transform 0.4s ease;
      position: relative;
      max-width: 420px;
      width: 100%;
    }
```

Change the `transform` line to include the parallax rotation:

```css
    .polaroid {
      background: #fff;
      padding: 14px 14px 52px;
      box-shadow: var(--shadow-warm), 0 0 0 1px rgba(74,58,44,0.06);
      transform: rotate(calc(2.5deg + var(--parallax-rot, 0deg)));
      transition: transform 0.4s ease;
      position: relative;
      max-width: 420px;
      width: 100%;
    }
```

The `:hover` rule (line 400) — `transform: rotate(0.5deg) scale(1.015);` — overrides this on hover, which is fine: the user hovering pauses the parallax visual on the polaroid, which matches the polaroid behaving like a static physical object when interacted with.

- [ ] **Step 4: Visually verify**

Hard-reload `index.html`. Slowly scroll down. As you scroll:
- The background image should appear to move *more slowly* than the page (lagging behind by ~60% of the scroll distance).
- The polaroid should slowly rotate further clockwise (from ~2.5° up to ~6°) as the hero scrolls out of view.
- Scrolling should remain smooth (60fps) — no jank or stutter.
- Open DevTools → Performance, record a scroll, confirm no long frames during scroll.
- Check the console for any errors — there should be none.

Resize the browser to <960px wide and reload. Scroll. Parallax should be **disabled** (background and polaroid don't move on scroll — only the page scrolls normally).

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "hero: add scroll parallax for background and polaroid rotation"
```

---

## Task 6: Reduced-motion + mobile media queries

The Ken Burns and polaroid drop-in animations are CSS-driven and currently run unconditionally. Wrap them so users with `prefers-reduced-motion: reduce` get a calmer experience, and slow Ken Burns on mobile. (Parallax already self-disables in JS — Task 5 handled that.)

**Files:**
- Modify: `index.html` — add a `@media (prefers-reduced-motion: reduce)` block, update the existing `@media (max-width: 960px)` block.

- [ ] **Step 1: Add reduced-motion overrides**

In the `<style>` block, immediately *before* the closing `</style>` (line ~1292), add:

```css
    @media (prefers-reduced-motion: reduce) {
      .hero::before {
        animation: none;
      }
      .hero-right {
        animation: fadeUp 0.6s ease 0.2s forwards;
      }
      .hero-underline path {
        animation-duration: 0.01s;
        animation-delay: 0s;
      }
    }
```

This:
- Stops Ken Burns (background sits at its initial 131% / 0% 24%).
- Replaces the polaroid drop/bounce with the gentler existing `fadeUp`.
- Makes the underline appear instantly instead of drawing.
- (Parallax is already disabled in JS via `matchMedia` check.)

- [ ] **Step 2: Slow Ken Burns on mobile**

Find the existing `@media (max-width: 960px)` block (around line 1236). Inside it, alongside the existing `.hero` rule overrides (which currently set `grid-template-columns: 1fr; padding: 8rem 1.5rem 5rem; gap: 3rem; min-height: auto;`), add:

```css
      .hero::before {
        animation-duration: 40s;
      }
```

So the relevant section of the media query becomes:

```css
    @media (max-width: 960px) {

      .hero { grid-template-columns: 1fr; padding: 8rem 1.5rem 5rem; gap: 3rem; min-height: auto; }
      .hero::before { animation-duration: 40s; }
      .hero-blob { display: none; }
      .hero-blob-left { left: 0; top: 0; width: 100%; height: 72%; border-radius: 0 0 50% 50% / 0 0 8% 8%; }
      .hero-right { justify-content: center; }
      .polaroid { max-width: 300px; }
```

- [ ] **Step 3: Verify reduced motion**

Open macOS System Settings → Accessibility → Display → toggle on **Reduce motion**. Hard-reload `index.html`. The hero should:
- Have a static background (no Ken Burns).
- The polaroid fades up gently (no drop/overshoot).
- Underline appears immediately.
- Scrolling does not produce parallax.

Toggle Reduce motion **off** and reload — all animations should return.

- [ ] **Step 4: Verify mobile**

In Chrome/Safari DevTools, switch to a mobile device emulation (e.g. iPhone 14, 390×844). Hard-reload. The hero should:
- Single-column layout (existing behaviour).
- Ken Burns plays but slower (40s loop).
- Polaroid drop-in still plays.
- Underline draws.
- Parallax disabled when scrolling.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "hero: respect prefers-reduced-motion; slow Ken Burns on mobile"
```

---

## Task 7: Final QA + push

- [ ] **Step 1: Full visual pass**

Hard-reload `index.html` in Chrome. Walk through:
1. Page loads → polaroid drops in with overshoot, settles at tilt
2. Title appears → wavy underline draws under "fun & friendly"
3. Background slowly Ken-Burns
4. Scroll down → background lags, polaroid rotates further
5. Hover polaroid → still rotates to 0.5° and scales 1.015x
6. Switch language EN → ES → FR → underline still positioned under the italic phrase in each language
7. Console is clean (no errors or warnings related to these changes)

- [ ] **Step 2: Cross-browser sanity check**

Open in Safari (the iOS engine's CSS quirks are the main risk). Confirm:
- Ken Burns runs.
- Polaroid drops in.
- Underline draws.
- Scrolling is smooth and parallax works.

- [ ] **Step 3: Push to origin**

```bash
git push origin main
```

(Per the project's CLAUDE.md and saved memory: always push to GitHub after changes.)

- [ ] **Step 4: Verify live site**

Visit `https://ashdabash2926.github.io/migustaschoolprivate` after GitHub Pages rebuilds (~30–60 seconds). Confirm all four animations play on the live site.
