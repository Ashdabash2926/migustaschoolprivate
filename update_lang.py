#!/usr/bin/env python3
"""Replace EN/ES pill toggle with a flag dropdown supporting EN/ES/FR across all pages."""
import re, os

BASE = '/Users/ash/Projects/migusta'
PAGES = ['index.html', 'classes.html', 'methodology.html', 'teachers.html',
         'activities.html', 'cafe.html', 'about.html', 'accommodation.html',
         'faqs.html', 'blog.html', 'contact.html']

# --- CSS ---

OLD_CSS_PILL = """    .lang-toggle { display: flex; align-items: center; background: #E8E3DB; border-radius: 50px; padding: 4px; gap: 2px; }
    .lang-btn { padding: 0.28rem 0.65rem; border-radius: 50px; border: none; cursor: pointer; font-family: 'Lora', serif; font-size: 0.72rem; font-weight: 500; transition: all 0.25s ease; background: transparent; color: #9A8878; line-height: 1; }
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

# --- HTML ---

OLD_TOGGLE_HTML = re.compile(
    r'<div class="lang-toggle-wrap"[^>]*>\s*'
    r'<div class="lang-toggle" id="langToggle">\s*'
    r'<button class="lang-btn active" data-lang="en">EN</button>\s*'
    r'<button class="lang-btn" data-lang="es">ES</button>\s*'
    r'</div>',
    re.DOTALL
)

NEW_TOGGLE_HTML = """<div class="lang-toggle-wrap" style="position:relative;">
        <div class="lang-select" id="langSelect">
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

# --- JS ---

# The old JS patterns differ per page. We'll replace the core lang toggle JS block.
OLD_JS_PATTERNS = [
    # Pattern for most inner pages
    re.compile(
        r"// Lang toggle\n"
        r"  const langBtns = document\.querySelectorAll\('\.lang-btn'\);\n"
        r"  let currentLang = localStorage\.getItem\('mgLang'\) \|\| 'en';\n"
        r"  function setLang\(lang\) \{\n"
        r"    currentLang = lang;\n"
        r"    localStorage\.setItem\('mgLang', lang\);\n"
        r"    document\.documentElement\.lang = lang;\n"
        r"    langBtns\.forEach\(b => b\.classList\.toggle\('active', b\.dataset\.lang === lang\)\);\n"
        r"    document\.querySelectorAll\('\[data-en\]'\)\.forEach\(el => \{\n"
        r"      const val = el\.dataset\[lang\];\n"
        r"      if \(val !== undefined\) \{\n"
        r"        if \(val\.includes\('<'\)\) \{ el\.innerHTML = val; \} else \{ el\.textContent = val; \}\n"
        r"      \}\n"
        r"    \}\);\n"
        r"  \}\n"
        r"  langBtns\.forEach\(btn => btn\.addEventListener\('click', \(\) => setLang\(btn\.dataset\.lang\)\)\);\n"
        r"  setLang\(currentLang\);",
        re.MULTILINE
    ),
    # Pattern for index.html (slightly different variable names)
    re.compile(
        r"//  LANGUAGE TOGGLE \n"
        r"    const langToggle = document\.getElementById\('langToggle'\);\n"
        r"    const langBtns = langToggle\.querySelectorAll\('\.lang-btn'\);\n"
        r"    let currentLang = localStorage\.getItem\('mgLang'\) \|\| 'en';\n\n"
        r"    function setLang\(lang\) \{\n"
        r"      currentLang = lang;\n"
        r"      localStorage\.setItem\('mgLang', lang\);\n"
        r"      document\.documentElement\.lang = lang;\n\n"
        r"      langBtns\.forEach\(b => b\.classList\.toggle\('active', b\.dataset\.lang === lang\)\);\n\n"
        r"      document\.querySelectorAll\('\[data-en\]'\)\.forEach\(el => \{\n"
        r"        const val = el\.dataset\[lang\];\n"
        r"        if \(val !== undefined\) \{\n"
        r"          // Preserve innerHTML for elements with em tags\n"
        r"          if \(val\.includes\('<'\)\) \{\n"
        r"            el\.innerHTML = val;\n"
        r"          \} else \{\n"
        r"            el\.textContent = val;\n"
        r"          \}\n"
        r"        \}\n"
        r"      \}\);\n"
        r"    \}\n\n"
        r"    langBtns\.forEach\(b => b\.addEventListener\('click', \(\) => setLang\(b\.dataset\.lang\)\)\);\n"
        r"    setLang\(currentLang\);",
        re.MULTILINE
    ),
]

NEW_JS = """// Lang select dropdown
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

# --- NAV data-fr attributes for shared nav items ---
NAV_FR = {
    'Classes': 'Cours',
    'Clases': None,  # skip, we match on data-en
    'Teachers': 'Professeurs',
    'Activities': 'Activit\u00e9s',
    'About': '\u00c0 propos',
    'Contact': 'Contact',
    'More': 'Plus',
    'Home': 'Accueil',
    'Methodology': 'M\u00e9thodologie',
    'Accommodation': 'H\u00e9bergement',
    'FAQs': 'FAQ',
    'Blog': 'Blog',
    'Register Now': "S'inscrire",
}

def add_nav_fr(html):
    """Add data-fr to nav elements that have data-en matching our dict."""
    for en, fr in NAV_FR.items():
        if fr is None:
            continue
        # Match data-en="X" data-es="Y" and add data-fr="Z" if not already present
        pattern = f'data-en="{en}" data-es="([^"]*)"'
        def repl(m):
            full = m.group(0)
            if 'data-fr=' in html[max(0,m.start()-50):m.end()+50]:
                return full
            return f'{full} data-fr="{fr}"'
        html = re.sub(pattern, repl, html)
    return html


for page in PAGES:
    path = os.path.join(BASE, page)
    if not os.path.exists(path):
        print(f'  skip {page} (not found)')
        continue
    with open(path) as f:
        c = f.read()

    # 1. Replace CSS
    c = c.replace(OLD_CSS_PILL, NEW_CSS)

    # 2. Replace HTML toggle
    c = OLD_TOGGLE_HTML.sub(NEW_TOGGLE_HTML, c)

    # 3. Replace JS — try each pattern
    replaced_js = False
    for pat in OLD_JS_PATTERNS:
        if pat.search(c):
            c = pat.sub(lambda m: NEW_JS, c)
            replaced_js = True
            break

    if not replaced_js:
        # Fallback: simple string replacement for contact/activities pages
        old_simple = """// Lang toggle
  const langBtns = document.querySelectorAll('.lang-btn');
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
  langBtns.forEach(btn => btn.addEventListener('click', () => setLang(btn.dataset.lang)));
  setLang(currentLang);"""
        if old_simple in c:
            c = c.replace(old_simple, NEW_JS)
            replaced_js = True

    # 4. Add data-fr to nav items
    c = add_nav_fr(c)

    # 5. Also update lang bubble text to be trilingual
    c = c.replace(
        '¿Quieres este sitio en español?',
        '¿Quieres este sitio en español?'  # keep as-is, it's a nice touch
    )

    with open(path, 'w') as f:
        f.write(c)
    js_note = '(JS updated)' if replaced_js else '(JS NOT found!)'
    print(f'✓ {page} {js_note}')

print('Done.')
