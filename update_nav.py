#!/usr/bin/env python3
"""Update nav across all existing pages: More dropdown, Activities link, 1100px breakpoint."""
import re, os

BASE = '/Users/ash/Projects/migusta'
PAGES = ['index.html', 'classes.html', 'methodology.html', 'teachers.html',
         'cafe.html', 'about.html', 'accommodation.html', 'faqs.html', 'blog.html']

# Active link per page
PRIMARY = {
    'index.html': None, 'classes.html': 'classes.html',
    'methodology.html': None, 'teachers.html': 'teachers.html',
    'cafe.html': 'cafe.html', 'about.html': 'about.html',
    'accommodation.html': None, 'faqs.html': None, 'blog.html': None,
}
DROPDOWN = {
    'index.html': 'index.html', 'classes.html': None,
    'methodology.html': 'methodology.html', 'teachers.html': None,
    'cafe.html': None, 'about.html': None,
    'accommodation.html': 'accommodation.html', 'faqs.html': 'faqs.html',
    'blog.html': 'blog.html',
}

DROPDOWN_CSS = """
    /* Nav dropdown */
    .nav-cafe-link { font-family: 'Caveat', cursive !important; font-size: 1.3rem !important; font-weight: 600 !important; color: var(--terra) !important; font-style: normal !important; }
    .nav-more-item { position: relative; }
    .nav-more-btn { background: none; border: none; cursor: pointer; display: flex; align-items: center; gap: 0.3rem; color: var(--ink-soft); font-family: 'Lora', serif; font-size: 0.78rem; font-style: italic; padding: 0; line-height: 1; transition: color 0.2s; }
    .nav-more-btn:hover, .nav-more-btn.active { color: var(--terra); }
    .nav-more-btn svg { transition: transform 0.2s; flex-shrink: 0; }
    .nav-more-btn[aria-expanded="true"] svg { transform: rotate(180deg); }
    .nav-dropdown { display: none; position: absolute; top: calc(100% + 14px); left: 50%; transform: translateX(-50%); background: var(--cream); border: 1px solid var(--border); border-radius: 14px; padding: 0.5rem; list-style: none; box-shadow: 0 8px 32px rgba(28,20,16,0.12); min-width: 175px; z-index: 300; }
    .nav-dropdown.open { display: block; animation: dropIn 0.18s ease; }
    @keyframes dropIn { from { opacity: 0; transform: translateX(-50%) translateY(-6px); } to { opacity: 1; transform: translateX(-50%) translateY(0); } }
    .nav-dropdown li a { display: block; padding: 0.5rem 0.9rem; color: var(--ink-soft); text-decoration: none; font-family: 'Lora', serif; font-size: 0.8rem; font-style: italic; border-radius: 8px; white-space: nowrap; transition: background 0.15s, color 0.15s; }
    .nav-dropdown li a:hover, .nav-dropdown li a.active { background: var(--terra-pale); color: var(--terra); }"""

DROPDOWN_JS = """  // More dropdown
  const navMoreBtn = document.getElementById('navMoreBtn');
  const navDropdown = document.getElementById('navDropdown');
  if (navMoreBtn && navDropdown) {
    navMoreBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = navDropdown.classList.contains('open');
      navDropdown.classList.toggle('open', !open);
      navMoreBtn.setAttribute('aria-expanded', String(!open));
    });
    document.addEventListener('click', () => {
      navDropdown.classList.remove('open');
      if (navMoreBtn) navMoreBtn.setAttribute('aria-expanded', 'false');
    });
  }

"""

SVG = '<svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def make_ul(page):
    pa = PRIMARY.get(page)
    da = DROPDOWN.get(page)

    def lnk(href, en, es):
        ac = ' class="active"' if href == pa else ''
        return f'    <li><a href="{href}"{ac} data-en="{en}" data-es="{es}">{en}</a></li>'

    cafe_cls = 'nav-cafe-link active' if pa == 'cafe.html' else 'nav-cafe-link'

    def dd(href, en, es):
        ac = ' class="active"' if href == da else ''
        return f'        <li><a href="{href}"{ac} data-en="{en}" data-es="{es}">{en}</a></li>'

    more_ac = ' active' if da else ''

    return '\n'.join([
        '  <ul class="nav-center">',
        lnk('classes.html', 'Classes', 'Clases'),
        lnk('teachers.html', 'Teachers', 'Profesores'),
        lnk('activities.html', 'Activities', 'Actividades'),
        f'    <li><a href="cafe.html" class="{cafe_cls}" data-en="Café" data-es="Café">Café</a></li>',
        lnk('about.html', 'About', 'Sobre Nosotros'),
        lnk('contact.html', 'Contact', 'Contacto'),
        '    <li class="nav-more-item">',
        f'      <button class="nav-more-btn{more_ac}" id="navMoreBtn" aria-expanded="false">',
        '        <span data-en="More" data-es="Más">More</span>',
        f'        {SVG}',
        '      </button>',
        '      <ul class="nav-dropdown" id="navDropdown">',
        dd('index.html', 'Home', 'Inicio'),
        dd('methodology.html', 'Methodology', 'Metodología'),
        dd('accommodation.html', 'Accommodation', 'Alojamiento'),
        dd('faqs.html', 'FAQs', 'Preguntas'),
        dd('blog.html', 'Blog', 'Blog'),
        '      </ul>',
        '    </li>',
        '  </ul>',
    ])

MOBILE_NAV = """<!-- Mobile nav -->
<div class="nav-mobile" id="navMobile">
  <button class="nav-mobile-close" id="navClose">✕</button>
  <a href="index.html" data-en="Home" data-es="Inicio">Home</a>
  <a href="classes.html" data-en="Classes" data-es="Clases">Classes</a>
  <a href="methodology.html" data-en="Methodology" data-es="Metodología">Methodology</a>
  <a href="teachers.html" data-en="Teachers" data-es="Profesores">Teachers</a>
  <a href="activities.html" data-en="Activities" data-es="Actividades">Activities</a>
  <a href="cafe.html" data-en="Café" data-es="Café">Café</a>
  <a href="about.html" data-en="About" data-es="Sobre Nosotros">About</a>
  <a href="accommodation.html" data-en="Accommodation" data-es="Alojamiento">Accommodation</a>
  <a href="faqs.html" data-en="FAQs" data-es="Preguntas">FAQs</a>
  <a href="blog.html" data-en="Blog" data-es="Blog">Blog</a>
  <a href="contact.html" data-en="Contact" data-es="Contacto">Contact</a>
  <a href="classes.html" class="btn-primary" data-en="Register Now" data-es="Regístrate">Register Now</a>
</div>"""

for page in PAGES:
    path = os.path.join(BASE, page)
    with open(path) as f:
        c = f.read()

    # 1. Add dropdown CSS
    if 'nav-more-btn' not in c:
        c = c.replace('</style>', DROPDOWN_CSS + '\n  </style>', 1)

    # 2. Bump nav breakpoint 960 → 1100
    # One-liner form used by inner pages
    c = c.replace(
        '@media (max-width: 960px) { #main-nav { padding: 0 1.5rem; } .nav-center, .nav-cta { display: none; } .nav-burger { display: flex; } }',
        '@media (max-width: 1100px) { #main-nav { padding: 0 1.5rem; } .nav-center, .nav-cta { display: none; } .nav-burger { display: flex; } }'
    )
    # Multi-line form used by index.html — add a new 1100 rule before existing 960 block
    if page == 'index.html' and '@media (max-width: 1100px)' not in c:
        c = re.sub(
            r'(    /\*  RESPONSIVE  \*/\n    @media \(max-width: 1100px\) \{)',
            r'    /* NAV breakpoint */\n    @media (max-width: 1100px) { #main-nav { padding: 0 1.5rem; } .nav-center, .nav-cta { display: none; } .nav-burger { display: flex; } }\n\n    \1',
            c
        )
    # Also handle multi-line 960px for index (hide nav inside it is already there, add 1100 above it)
    if page == 'index.html':
        # Remove nav-hiding from the inner 960 block (they'll be handled by 1100 now)
        c = c.replace(
            '      #main-nav { padding: 0 1.5rem; }\n      .nav-center { display: none; }\n      .nav-cta { display: none; }\n      .nav-burger { display: flex; }',
            '      #main-nav { padding: 0 1.5rem; }'
        )

    # 3. Replace nav-center ul
    c = re.sub(
        r'<ul class="nav-center">.*?</ul>',
        make_ul(page),
        c,
        flags=re.DOTALL,
        count=1
    )

    # 4. Replace mobile nav
    c = re.sub(
        r'<!--\s*Mobile nav\s*-->.*?class="btn-primary"[^>]*>Register Now</a>\s*\n\s*</div>',
        MOBILE_NAV,
        c,
        flags=re.DOTALL,
        count=1
    )

    # 5. Add dropdown JS
    if 'navMoreBtn' not in c:
        if '// Scroll reveal' in c:
            c = c.replace('  // Scroll reveal', DROPDOWN_JS + '  // Scroll reveal', 1)
        elif '// Lang toggle' in c:
            c = c.replace('  // Lang toggle', DROPDOWN_JS + '  // Lang toggle', 1)

    with open(path, 'w') as f:
        f.write(c)
    print(f'✓ {page}')

print('Done.')
