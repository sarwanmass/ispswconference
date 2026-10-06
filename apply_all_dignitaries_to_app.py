import json

with open("build_mobile_app_portal.py", "r", encoding="utf-8") as f:
    code = f.read()

# We need to update renderDignitariesView in build_mobile_app_portal.py
# Let's inspect where renderDignitariesView is defined

new_dignitaries_js = '''    // Comprehensive Dignitaries Directory with All Invitation Names & Quick Filter
    let activeDigFilter = 'all';

    function setDigFilter(catKey, btnEl) {
      activeDigFilter = catKey;
      document.querySelectorAll('.dig-filter-btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      renderDignitariesView();
    }

    function searchDignitaries() {
      renderDignitariesView();
    }

    function renderDignitariesView() {
      const container = document.getElementById('dignitaries-shelf-target');
      if (!container) return;

      const q = (document.getElementById('dig-search-input')?.value || '').trim().toLowerCase();
      const allData = CONF_DB.all_invitation_dignitaries || {};
      
      let allItems = [];
      if (allData.inauguration) allItems = allItems.concat(allData.inauguration.map(x => ({...x, group: 'inauguration'})));
      if (allData.valedictory) allItems = allItems.concat(allData.valedictory.map(x => ({...x, group: 'valedictory'})));
      if (allData.presence_officers) allItems = allItems.concat(allData.presence_officers.map(x => ({...x, group: 'officers'})));
      if (allData.national_council) allItems = allItems.concat(allData.national_council.map(x => ({...x, group: 'national'})));
      if (allData.organizing_committee) allItems = allItems.concat(allData.organizing_committee.map(x => ({...x, group: 'committee'})));

      // Filter by category
      let filtered = allItems;
      if (activeDigFilter !== 'all') {
        filtered = filtered.filter(item => item.group === activeDigFilter);
      }

      // Filter by query
      if (q) {
        filtered = filtered.filter(item => 
          item.name.toLowerCase().includes(q) ||
          item.title.toLowerCase().includes(q) ||
          item.org.toLowerCase().includes(q) ||
          item.role.toLowerCase().includes(q)
        );
      }

      // Count badge
      const countEl = document.getElementById('dig-results-count');
      if (countEl) countEl.textContent = filtered.length;

      let html = '';

      if (filtered.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 30px 10px; background: #fff; border-radius: var(--radius-md); border: 1px dashed var(--app-border);">
            <i class="fa-solid fa-user-xmark" style="font-size: 2rem; color: var(--app-blue-400); margin-bottom: 8px;"></i>
            <div style="font-weight: 700; color: var(--app-blue-950);">No dignitaries match "${q}"</div>
            <div style="font-size: 0.8rem; color: var(--text-subtle); margin-top: 4px;">Try searching by surname, institution, or university name.</div>
          </div>
        `;
        return;
      }

      filtered.forEach(d => {
        // Photo match
        let photoSrc = '';
        if (d.photo_key && CONF_DB.dignitaries) {
          const match = CONF_DB.dignitaries.find(x => x.name.toLowerCase().includes(d.name.split(' ')[1]?.toLowerCase() || d.name.toLowerCase()));
          if (match && match.photo) photoSrc = match.photo;
        }

        const photoHtml = photoSrc 
          ? `<img src="${photoSrc}" alt="${d.name}">` 
          : `<div class="fallback-ico"><i class="fa-solid fa-user-tie"></i></div>`;

        let groupTag = d.category || 'Dignitary';
        let groupColor = 'var(--app-blue-700)';
        if (d.group === 'inauguration') groupColor = 'var(--app-blue-700)';
        else if (d.group === 'valedictory') groupColor = '#059669';
        else if (d.group === 'officers') groupColor = '#7c3aed';
        else if (d.group === 'national') groupColor = '#d97706';
        else if (d.group === 'committee') groupColor = 'var(--app-blue-600)';

        html += `
          <div class="dignitary-card-mobile" style="border-left: 3.5px solid ${groupColor};">
            <div class="dig-avatar-ring">
              ${photoHtml}
            </div>
            <div class="dig-details-box" style="flex: 1;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 4px;">
                <span class="dig-role-chip" style="color: ${groupColor};">${d.role}</span>
              </div>
              <h4 style="font-size: 1.05rem; margin-top: 1px;">${d.name}</h4>
              <div style="font-size: 0.82rem; font-weight: 700; color: var(--app-blue-900);">${d.title}</div>
              <div class="dig-affil">${d.org}</div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }'''

# Replace renderDignitariesView in build_mobile_app_portal.py
old_start = code.find("    // Render Dignitaries & Ceremonial Panels\n    function renderDignitariesView()")
old_end = code.find("    // Render Helpdesk Cards\n    function renderHelpdeskCards()")

if old_start != -1 and old_end != -1:
    code = code[:old_start] + new_dignitaries_js + "\n\n" + code[old_end:]
    print("Replaced renderDignitariesView successfully!")
else:
    print("Could not find function bounds!")

# Now also update the HTML markup in SECTION 5 (Dignitaries) to have:
# 1. Search bar for dignitaries
# 2. Touch filter chips for categories: All (38), Inauguration (4), Valedictory (6), Officers (6), National Council (17), Committee (5)
old_sec_dig = '''    <!-- ========================================================= -->
    <!-- SECTION 5: DIGNITARIES & CEREMONIAL PANELS                -->
    <!-- ========================================================= -->
    <section id="sec-dignitaries" class="app-section-panel">
      <div style="margin-bottom: 14px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">Conference Leadership</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">Eminent patrons, keynote leaders, valedictory officers, and organizing committee.</p>
      </div>

      <div class="dignitaries-mobile-shelf" id="dignitaries-shelf-target">
        <!-- Rendered by JavaScript -->
      </div>
    </section>'''

new_sec_dig = '''    <!-- ========================================================= -->
    <!-- SECTION 5: ALL DIGNITARIES & CEREMONIAL PANELS (INVITATIONS) -->
    <!-- ========================================================= -->
    <section id="sec-dignitaries" class="app-section-panel">
      <div style="margin-bottom: 12px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">Conference Dignitaries &amp; Leadership</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">All 38 distinguished patrons, inaugural luminaries, valedictory guests of honour, and national council members mentioned across the official invitations.</p>
      </div>

      <!-- Dignitaries Fast Search Box -->
      <div style="background: #ffffff; border-radius: var(--radius-md); border: 1px solid var(--app-border); padding: 10px 14px; margin-bottom: 12px; box-shadow: var(--shadow-sm); display: flex; align-items: center; gap: 8px;">
        <i class="fa-solid fa-magnifying-glass" style="color: var(--app-blue-600); font-size: 0.95rem;"></i>
        <input type="text" id="dig-search-input" placeholder="Search dignitary name, university, or designation..." style="width: 100%; border: none; outline: none; font-family: var(--font-body); font-size: 0.88rem; color: var(--text-main);" oninput="searchDignitaries()">
      </div>

      <!-- Category Filter Chips Row -->
      <div class="quick-chips-scroller" style="margin-bottom: 14px;">
        <button class="touch-chip dig-filter-btn active" onclick="setDigFilter('all', this)"><i class="fa-solid fa-users"></i> All (<span id="dig-results-count">38</span>)</button>
        <button class="touch-chip dig-filter-btn" onclick="setDigFilter('inauguration', this)"><i class="fa-solid fa-ribbon"></i> Inauguration &amp; Keynote (4)</button>
        <button class="touch-chip dig-filter-btn" onclick="setDigFilter('valedictory', this)"><i class="fa-solid fa-award"></i> Valedictory Guests (6)</button>
        <button class="touch-chip dig-filter-btn" onclick="setDigFilter('officers', this)"><i class="fa-solid fa-building-columns"></i> University &amp; ISPSW Officers (6)</button>
        <button class="touch-chip dig-filter-btn" onclick="setDigFilter('national', this)"><i class="fa-solid fa-graduation-cap"></i> National Presence (17)</button>
        <button class="touch-chip dig-filter-btn" onclick="setDigFilter('committee', this)"><i class="fa-solid fa-sitemap"></i> Organizing Committee (5)</button>
      </div>

      <div class="dignitaries-mobile-shelf" id="dignitaries-shelf-target">
        <!-- Rendered by JavaScript -->
      </div>
    </section>'''

if old_sec_dig in code:
    code = code.replace(old_sec_dig, new_sec_dig)
    print("Replaced Dignitaries section markup successfully!")
else:
    print("Could not find old_sec_dig markup!")

with open("build_mobile_app_portal.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved build_mobile_app_portal.py")
