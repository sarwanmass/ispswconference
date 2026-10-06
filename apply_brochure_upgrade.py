import json

with open("generate_corporate_portal.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replacement function for renderDignitariesList
new_render_dignitaries = '''    // Render Dignitaries, Valedictory Panel, National Presence & Organizing Committee
    function renderDignitariesList() {
      const container = document.getElementById('dignitaries-shelf-container');
      let html = '';

      // Section 1: Inaugural & Keynote Leadership
      html += `
        <div style="grid-column: 1 / -1; margin-bottom: 8px;">
          <h3 style="font-family: var(--font-brand); font-size: 1.45rem; color: var(--blue-950); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-ribbon" style="color: var(--blue-600);"></i> Inauguration &amp; Keynote Luminaries
          </h3>
          <p style="font-size: 0.88rem; color: var(--slate-600);">Official leadership presiding over the Inaugural Ceremony and Keynote Address at the MBA Auditorium.</p>
        </div>
      `;

      CONF_DB.dignitaries.forEach(d => {
        const photoHtml = d.photo 
          ? `<img src="${d.photo}" alt="${d.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`
          : `<i class="fa-solid fa-user-tie"></i>`;

        html += `
          <div class="dignitary-box-corp">
            <div class="dignitary-avatar-corp" style="${d.photo ? 'border: 2px solid var(--blue-600); padding: 2px; overflow: hidden; background: #fff;' : ''}">
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

      // Section 2: Valedictory Ceremony Official Panel
      if (CONF_DB.valedictory_info) {
        const vi = CONF_DB.valedictory_info;
        html += `
          <div style="grid-column: 1 / -1; margin-top: 32px; margin-bottom: 8px;">
            <div style="background: linear-gradient(135deg, var(--blue-950) 0%, var(--blue-900) 100%); color: #fff; border-radius: var(--radius-lg); padding: 26px 28px; border: 2px solid var(--cyan-400); box-shadow: var(--shadow-card);">
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 18px;">
                <div>
                  <span style="background: rgba(14, 165, 233, 0.25); border: 1px solid var(--cyan-400); padding: 3px 10px; border-radius: 999px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: var(--cyan-400);">Official Ceremony</span>
                  <h3 style="font-family: var(--font-brand); font-size: 1.55rem; color: #fff; margin-top: 4px;">Valedictory Function &amp; Certificate Distribution</h3>
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

              <div style="margin-top: 22px;">
                <div style="font-size: 0.78rem; text-transform: uppercase; color: var(--cyan-400); font-weight: 700; margin-bottom: 10px; letter-spacing: 0.5px;">Guests of Honour</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px;">
                  ${vi.guests_of_honour.map(g => `
                    <div style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: var(--radius-sm); border: 1px solid rgba(255,255,255,0.12);">
                      <strong style="color: #fff; font-size: 0.92rem;">${g.name}</strong>
                      <div style="font-size: 0.76rem; color: var(--blue-200); margin-top: 2px;">${g.desig}</div>
                    </div>
                  `).join('')}
                </div>
              </div>

              <div style="margin-top: 20px;">
                <div style="font-size: 0.78rem; text-transform: uppercase; color: var(--cyan-400); font-weight: 700; margin-bottom: 10px; letter-spacing: 0.5px;">Eminent Presence</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 8px;">
                  ${vi.presence.map(p => `
                    <div style="font-size: 0.8rem; color: #e2e8f0; line-height: 1.4;">
                      <i class="fa-solid fa-check" style="color: var(--cyan-400); margin-right: 5px;"></i> <strong>${p.name}</strong>, <span style="opacity: 0.85;">${p.desig}</span>
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
              <div style="width: 42px; height: 42px; border-radius: 50%; background: var(--blue-50); color: var(--blue-700); display: flex; align-items: center; justify-content: center; font-size: 1.05rem; flex-shrink: 0; border: 1px solid var(--blue-200);">
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
              <h4 style="font-family: var(--font-brand); font-size: 1.15rem; color: var(--blue-950); margin-bottom: 4px;">${oc.name}</h4>
              <div style="font-size: 0.82rem; color: var(--slate-600);">${oc.dept}</div>
            </div>
          `;
        });
      }

      container.innerHTML = html;
    }'''

# Replace in code
old_func_start = code.find("    // Render Dignitaries\n    function renderDignitariesList()")
old_func_end = code.find("    // Render Helpdesk Grid")

if old_func_start != -1 and old_func_end != -1:
    code = code[:old_func_start] + new_render_dignitaries + "\n\n" + code[old_func_end:]
    print("Replaced renderDignitariesList in generate_corporate_portal.py successfully!")
else:
    print("Could not find function markers, checking alternative...")

with open("generate_corporate_portal.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_corporate_portal.py")
