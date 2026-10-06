import json
import os

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

json_data_str = json.dumps(db, ensure_ascii=False)

# Let's read the HTML template from generate_corporate_portal.py
with open("generate_corporate_portal.py", "r", encoding="utf-8") as f:
    content = f.read()

# Extract html_template string
start_marker = 'html_template = ''''
end_marker = '''''
idx1 = content.find(start_marker) + len(start_marker)
idx2 = content.rfind(end_marker)
html_template = content[idx1:idx2]

# Enhance renderDignitariesList in the template to show:
# 1. Inaugural Luminaries with real photo badges
# 2. Valedictory Ceremony Official Panel
# 3. National Presence & Advisory Luminaries
# 4. Conference Organizing Committee

new_render_dignitaries_js = """
    function renderDignitariesList() {
      const container = document.getElementById('dignitaries-shelf-container');
      let html = '';

      // Section 1: Inauguration & Keynote Leadership
      html += `
        <div style="grid-column: 1 / -1; margin-bottom: 8px;">
          <h3 style="font-family: var(--font-brand); font-size: 1.45rem; color: var(--blue-950); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-ribbon" style="color: var(--blue-600);"></i> Inauguration &amp; Keynote Leadership
          </h3>
          <p style="font-size: 0.88rem; color: var(--slate-600);">Presiding officers, inaugural speaker, keynote director and chief guest for the Annual National Conference.</p>
        </div>
      `;

      CONF_DB.dignitaries.forEach(d => {
        const photoHtml = d.photo 
          ? `<img src="${d.photo}" alt="${d.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`
          : `<i class="fa-solid fa-user-tie"></i>`;

        html += `
          <div class="dignitary-box-corp">
            <div class="dignitary-avatar-corp" style="${d.photo ? 'border: 2px solid var(--blue-600); padding: 2px; overflow: hidden;' : ''}">
              ${photoHtml}
            </div>
            <div class="dignitary-text-corp">
              <span class="dignitary-tag-pill">${d.tag}</span>
              <h4>${d.name}</h4>
              <div style="font-size: 0.84rem; font-weight: 600; color: var(--blue-800);">${d.title}</div>
              <div class="dignitary-role-desc">${d.org}</div>
              <div style="font-size: 0.78rem; color: var(--blue-600); font-weight: 600; margin-top: 4px;">
                <i class="fa-regular fa-star"></i> ${d.role}
              </div>
            </div>
          </div>
        `;
      });

      // Section 2: Valedictory Ceremony Panel (9th October 2026)
      if (CONF_DB.valedictory_info) {
        const vi = CONF_DB.valedictory_info;
        html += `
          <div style="grid-column: 1 / -1; margin-top: 32px; margin-bottom: 8px;">
            <div style="background: linear-gradient(135deg, var(--blue-950) 0%, var(--blue-900) 100%); color: #fff; border-radius: var(--radius-lg); padding: 24px 28px; border: 2px solid var(--cyan-400); box-shadow: var(--shadow-card);">
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 16px;">
                <div>
                  <span style="background: rgba(14, 165, 233, 0.25); border: 1px solid var(--cyan-400); padding: 3px 10px; border-radius: 999px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: var(--cyan-400);">Official Ceremony</span>
                  <h3 style="font-family: var(--font-brand); font-size: 1.5rem; color: #fff; margin-top: 4px;">Valedictory Function &amp; Certificate Distribution</h3>
                </div>
                <div style="font-family: var(--font-mono); font-size: 0.88rem; color: var(--blue-200); background: rgba(255,255,255,0.1); padding: 8px 14px; border-radius: var(--radius-sm);">
                  <i class="fa-regular fa-calendar-check"></i> ${vi.date} · ${vi.time} · ${vi.venue}
                </div>
              </div>

              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
                <div style="background: rgba(255,255,255,0.08); padding: 16px; border-radius: var(--radius-md); border-left: 4px solid var(--cyan-400);">
                  <div style="font-size: 0.72rem; text-transform: uppercase; color: var(--cyan-400); font-weight: 700;">Presided Over By</div>
                  <h4 style="font-size: 1.15rem; color: #fff; margin-top: 2px;">${vi.presided_by}</h4>
                </div>
                <div style="background: rgba(255,255,255,0.08); padding: 16px; border-radius: var(--radius-md); border-left: 4px solid #22c55e;">
                  <div style="font-size: 0.72rem; text-transform: uppercase; color: #4ade80; font-weight: 700;">Chief Guest &amp; Valedictory Address</div>
                  <h4 style="font-size: 1.15rem; color: #fff; margin-top: 2px;">${vi.chief_guest}</h4>
                </div>
              </div>

              <div style="margin-top: 20px;">
                <div style="font-size: 0.76rem; text-transform: uppercase; color: var(--blue-200); font-weight: 700; margin-bottom: 8px;">Guests of Honour</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px;">
                  ${vi.guests_of_honour.map(g => `
                    <div style="background: rgba(255,255,255,0.05); padding: 10px 14px; border-radius: var(--radius-sm); border: 1px solid rgba(255,255,255,0.1);">
                      <strong style="color: #fff; font-size: 0.9rem;">${g.name}</strong>
                      <div style="font-size: 0.76rem; color: var(--blue-200);">${g.desig}</div>
                    </div>
                  `).join('')}
                </div>
              </div>

              <div style="margin-top: 18px;">
                <div style="font-size: 0.76rem; text-transform: uppercase; color: var(--blue-200); font-weight: 700; margin-bottom: 8px;">Eminent Presence</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px;">
                  ${vi.presence.map(p => `
                    <div style="font-size: 0.8rem; color: #e2e8f0;">
                      <i class="fa-solid fa-check" style="color: var(--cyan-400); margin-right: 4px;"></i> <strong>${p.name}</strong>, <span style="opacity: 0.8;">${p.desig}</span>
                    </div>
                  `).join('')}
                </div>
              </div>

            </div>
          </div>
        `;
      }

      // Section 3: National Presence & Advisory Panel
      if (CONF_DB.national_presence) {
        html += `
          <div style="grid-column: 1 / -1; margin-top: 36px; margin-bottom: 8px;">
            <h3 style="font-family: var(--font-brand); font-size: 1.4rem; color: var(--blue-950); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
              <i class="fa-solid fa-users-viewfinder" style="color: var(--blue-600);"></i> National Presence &amp; Academic Advisory Panel
            </h3>
            <p style="font-size: 0.88rem; color: var(--slate-600);">Eminent professors, department heads, and office bearers from universities and institutions across India.</p>
          </div>
        `;

        CONF_DB.national_presence.forEach(np => {
          html += `
            <div style="background: var(--white); border-radius: var(--radius-md); border: 1px solid var(--slate-200); padding: 14px 18px; box-shadow: var(--shadow-subtle); display: flex; align-items: center; gap: 12px;">
              <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--blue-50); color: var(--blue-700); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
              <div>
                <strong style="color: var(--blue-950); font-size: 0.95rem;">${np.name}</strong>
                <div style="font-size: 0.78rem; color: var(--slate-600); line-height: 1.35;">${np.desig}</div>
              </div>
            </div>
          `;
        });
      }

      // Section 4: Conference Organizing Committee
      if (CONF_DB.organizing_committee) {
        html += `
          <div style="grid-column: 1 / -1; margin-top: 36px; margin-bottom: 8px;">
            <h3 style="font-family: var(--font-brand); font-size: 1.4rem; color: var(--blue-950); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
              <i class="fa-solid fa-sitemap" style="color: var(--blue-600);"></i> Conference Organizing Committee
            </h3>
            <p style="font-size: 0.88rem; color: var(--slate-600);">Department of Studies in Social Work, Davangere University.</p>
          </div>
        `;

        CONF_DB.organizing_committee.forEach(oc => {
          html += `
            <div style="background: var(--white); border-radius: var(--radius-md); border: 1px solid var(--blue-200); padding: 18px; box-shadow: var(--shadow-card); text-align: center; border-top: 4px solid var(--blue-700);">
              <div style="font-size: 0.74rem; font-weight: 700; color: var(--blue-600); text-transform: uppercase; margin-bottom: 4px;">${oc.role}</div>
              <h4 style="font-family: var(--font-brand); font-size: 1.1rem; color: var(--blue-950); margin-bottom: 4px;">${oc.name}</h4>
              <div style="font-size: 0.8rem; color: var(--slate-600);">${oc.dept}</div>
            </div>
          `;
        });
      }

      container.innerHTML = html;
    }
"""

# Replace renderDignitariesList in html_template
old_render_start = html_template.find("function renderDignitariesList()")
old_render_end = html_template.find("function renderHelpdeskGrid()")

html_template = html_template[:old_render_start] + new_render_dignitaries_js + "

    " + html_template[old_render_end:]

# Logos Injection
davangere_logo_html = f'<img src="{db["conference_meta"]["davangere_logo"]}" alt="Davangere University">' if db["conference_meta"]["davangere_logo"] else '<i class="fa-solid fa-building-columns" style="font-size: 2rem; color: #1e3a8a;"></i>'
ispsw_logo_html = f'<img src="{db["conference_meta"]["ispsw_logo"]}" alt="ISPSW Logo">' if db["conference_meta"]["ispsw_logo"] else '<i class="fa-solid fa-shield-halved" style="font-size: 2rem; color: #1e3a8a;"></i>'

final_html = html_template.replace('__DAVANGERE_LOGO_HTML__', davangere_logo_html)
final_html = final_html.replace('__ISPSW_LOGO_HTML__', ispsw_logo_html)
final_html = final_html.replace('__CONF_DB_JSON__', json_data_str)

output_path = "index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

with open("conference_portal.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated updated {output_path} ({len(final_html)} bytes) successfully with official brochure details & portraits!")
