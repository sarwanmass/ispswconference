import json
import re

print("Adding official attribution: Designed & Architected by Dr. Saravana Kadirvelu...")

with open("generate_corporate_portal.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Top Bar attribution
old_top_bar = '''        <div style="display: flex; align-items: center; gap: 14px;">
          <span>7th – 9th OCTOBER, 2026</span>
          <a href="mailto:dumswispswnc2026@gmail.com" class="top-email-link">
            <i class="fa-regular fa-envelope"></i> dumswispswnc2026@gmail.com
          </a>
        </div>'''

new_top_bar = '''        <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
          <span>7th – 9th OCTOBER, 2026</span>
          <span style="opacity: 0.35;">|</span>
          <span style="color: var(--cyan-400); font-weight: 600;"><i class="fa-solid fa-code"></i> Designed &amp; Architected by Dr. Saravana Kadirvelu</span>
          <span style="opacity: 0.35;">|</span>
          <a href="mailto:dumswispswnc2026@gmail.com" class="top-email-link">
            <i class="fa-regular fa-envelope"></i> dumswispswnc2026@gmail.com
          </a>
        </div>'''

if old_top_bar in code:
    code = code.replace(old_top_bar, new_top_bar)
    print("Top bar attribution added!")
else:
    print("Could not find exact old_top_bar match, checking fallback...")

# 2. Hero Card attribution badge
old_hero_pills = '''        <div class="hero-pills-row">
          <span class="hero-meta-pill"><i class="fa-regular fa-calendar-days"></i> 7th – 9th October, 2026</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-location-dot"></i> MBA Auditorium &amp; Academic Complex</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-graduation-cap"></i> 115 Accepted Papers &amp; Abstracts</span>
        </div>'''

new_hero_pills = '''        <div class="hero-pills-row">
          <span class="hero-meta-pill"><i class="fa-regular fa-calendar-days"></i> 7th – 9th October, 2026</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-location-dot"></i> MBA Auditorium &amp; Academic Complex</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-graduation-cap"></i> 115 Accepted Papers &amp; Abstracts</span>
        </div>

        <div style="margin-top: 14px; display: flex; justify-content: center;">
          <span style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(56, 189, 248, 0.3); padding: 5px 16px; border-radius: 999px; font-size: 0.82rem; color: #e0f2fe; font-weight: 600; display: inline-flex; align-items: center; gap: 7px; backdrop-filter: blur(8px);">
            <i class="fa-solid fa-compass-drafting" style="color: var(--cyan-400);"></i> Digital Portal Designed &amp; Architected by <strong style="color: #fff;">Dr. Saravana Kadirvelu</strong>
          </span>
        </div>'''

if old_hero_pills in code:
    code = code.replace(old_hero_pills, new_hero_pills)
    print("Hero card badge added!")

# 3. Footer attribution & copyright
old_sub_footer = '''      <div class="sub-footer-copyright">
        &copy; 2026 Davangere University &amp; Indian Society of Professional Social Work (ISPSW). All rights reserved. Peer-reviewed conference proceedings published for academic reference.
      </div>'''

new_sub_footer = '''      <div class="sub-footer-copyright">
        <div style="margin-bottom: 8px; font-size: 0.88rem; color: #cbd5e1;">
          <i class="fa-solid fa-laptop-code" style="color: var(--cyan-400); margin-right: 6px;"></i>
          Portal Designed &amp; Architected by <strong style="color: #fff;">Dr. Saravana Kadirvelu</strong>
        </div>
        &copy; 2026 Davangere University &amp; Indian Society of Professional Social Work (ISPSW). All rights reserved. Peer-reviewed conference proceedings published for academic reference.
      </div>'''

if old_sub_footer in code:
    code = code.replace(old_sub_footer, new_sub_footer)
    print("Footer attribution added!")

with open("generate_corporate_portal.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved generate_corporate_portal.py")
