#!/usr/bin/env python3
"""Fix lang toggle CSS and JS on pages that update_lang.py missed."""
import os

BASE = '/Users/ash/Projects/migusta'
PAGES = ['classes.html', 'methodology.html', 'cafe.html', 'accommodation.html']

# CSS variant with letter-spacing
OLD_CSS_V2 = """    .lang-toggle { display: flex; align-items: center; background: #E8E3DB; border-radius: 50px; padding: 4px; gap: 2px; }
    .lang-btn { padding: 0.28rem 0.65rem; border-radius: 50px; border: none; cursor: pointer; font-family: 'Lora', serif; font-size: 0.72rem; font-weight: 500; letter-spacing: 0.05em; transition: all 0.25s ease; background: transparent; color: #9A8878; line-height: 1; }
    .lang-btn.active { background: var(--ink); color: #fff; box-shadow: 0 1px 4px rgba(28,20,16,0.2); }"""

NEW_CSS = """    .lang-select { position: relative; }
    .lang-current { display: flex; align-items: center; gap: 0.4rem; background: #E8E3DB; border: none; border-radius: 50px; padding: 0.3rem 0.7rem 0.3rem 0.5rem; cursor: pointer; font-family: 'Lora', serif; font-size: 0.72rem; font-weight: 500; color: var(--ink-soft); line-height: 1; transition: background 0.2s; }
    .lang-current:hover { background: #DDD8CF; }
    .lang-flag { font-size: 0.95rem; line-height: 1; }
    .lang-current svg { width: 8px; height: 5px; transition: transform 0.2s; flex-shrink: 0; }
    .lang-current[aria-expanded="true"] svg { transform: rotate(180deg); }
    .lang-menu { display: none; position: absolute; top: calc(100% + 8px); right: 0; background: var(--cream); border: 1px solid var(--border); border-radius: 12px; padding: 0.35rem; list-style: none; box-shadow: 0 8px 28px rgba(28,20,16,0.12); min-width: 130px; z-index: 300; }
    .lang-menu.open { display: block; animation: langDrop 0.15s ease; }
    @keyframes langDrop { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
    .lang-option { display: flex; align-items: center; gap: 0.55rem; padding: 0.45rem 0.7rem; border-radius: 8px; border: none; background: none; width: 100%; cursor: pointer; font-family: 'Lora', serif; font-size: 0.78rem; color: var(--ink-soft); transition: background 0.15s, color 0.15s; }
    .lang-option:hover, .lang-option.active { background: var(--terra-pale); color: var(--terra); }
    .lang-option .lang-flag { font-size: 1rem; }"""

# JS variant with langToggle variable
OLD_JS = """    // Language toggle
    const langToggle = document.getElementById('langToggle');
    const langBtns = langToggle.querySelectorAll('.lang-btn');
    let currentLang = localStorage.getItem('mgLang') || 'en';

    function setLang(lang) {
      currentLang = lang;
      localStorage.setItem('mgLang', lang);
      document.documentElement.lang = lang;
      langBtns.forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
      document.querySelectorAll('[data-en]').forEach(el => {
        const val = el.dataset[lang];
        if (val !== undefined) {
          if (val.includes('<')) { el.innerHTML = val; } else { el.textContent = val; }
        }
      });
    }
    langBtns.forEach(b => b.addEventListener('click', () => setLang(b.dataset.lang)));
    setLang(currentLang);"""

NEW_JS = """  // Lang select dropdown
  const FLAGS = { en: '\\u{1F1EC}\\u{1F1E7}', es: '\\u{1F1EA}\\u{1F1F8}', fr: '\\u{1F1EB}\\u{1F1F7}' };
  const CODES = { en: 'EN', es: 'ES', fr: 'FR' };
  const langCurrentBtn = document.getElementById('langCurrentBtn');
  const langCurrentFlag = document.getElementById('langCurrentFlag');
  const langCurrentCode = document.getElementById('langCurrentCode');
  const langMenu = document.getElementById('langMenu');
  const langOptions = document.querySelectorAll('.lang-option');
  let currentLang = localStorage.getItem('mgLang') || 'en';

  function setLang(lang) {
    currentLang = lang;
    localStorage.setItem('mgLang', lang);
    document.documentElement.lang = lang;
    langCurrentFlag.textContent = FLAGS[lang];
    langCurrentCode.textContent = CODES[lang];
    langOptions.forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
    document.querySelectorAll('[data-en]').forEach(el => {
      const val = el.dataset[lang] || el.dataset['en'];
      if (val !== undefined) {
        if (val.includes('<')) { el.innerHTML = val; } else { el.textContent = val; }
      }
    });
  }

  if (langCurrentBtn && langMenu) {
    langCurrentBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = langMenu.classList.contains('open');
      langMenu.classList.toggle('open', !open);
      langCurrentBtn.setAttribute('aria-expanded', String(!open));
    });
    document.addEventListener('click', () => {
      langMenu.classList.remove('open');
      if (langCurrentBtn) langCurrentBtn.setAttribute('aria-expanded', 'false');
    });
  }
  langOptions.forEach(btn => btn.addEventListener('click', (e) => {
    e.stopPropagation();
    setLang(btn.dataset.lang);
    langMenu.classList.remove('open');
    langCurrentBtn.setAttribute('aria-expanded', 'false');
  }));
  setLang(currentLang);"""

# HTML toggle (already updated by first script, but check)
OLD_HTML = """        <div class="lang-toggle" id="langToggle">
          <button class="lang-btn active" data-lang="en">EN</button>
          <button class="lang-btn" data-lang="es">ES</button>
        </div>"""

NEW_HTML = """        <div class="lang-select" id="langSelect">
          <button class="lang-current" id="langCurrentBtn" aria-expanded="false">
            <span class="lang-flag" id="langCurrentFlag">\U0001F1EC\U0001F1E7</span>
            <span id="langCurrentCode">EN</span>
            <svg viewBox="0 0 8 5" fill="none"><path d="M1 1l3 3 3-3" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <ul class="lang-menu" id="langMenu">
            <li><button class="lang-option active" data-lang="en"><span class="lang-flag">\U0001F1EC\U0001F1E7</span> English</button></li>
            <li><button class="lang-option" data-lang="es"><span class="lang-flag">\U0001F1EA\U0001F1F8</span> Espa\u00f1ol</button></li>
            <li><button class="lang-option" data-lang="fr"><span class="lang-flag">\U0001F1EB\U0001F1F7</span> Fran\u00e7ais</button></li>
          </ul>
        </div>"""

for page in PAGES:
    path = os.path.join(BASE, page)
    with open(path) as f:
        c = f.read()

    css_ok = False
    js_ok = False
    html_ok = False

    if OLD_CSS_V2 in c:
        c = c.replace(OLD_CSS_V2, NEW_CSS)
        css_ok = True

    if OLD_HTML in c:
        c = c.replace(OLD_HTML, NEW_HTML)
        html_ok = True

    if OLD_JS in c:
        c = c.replace(OLD_JS, NEW_JS)
        js_ok = True

    with open(path, 'w') as f:
        f.write(c)
    print(f'✓ {page} — CSS:{"ok" if css_ok else "skip"} HTML:{"ok" if html_ok else "skip"} JS:{"ok" if js_ok else "skip"}')

print('Done.')
