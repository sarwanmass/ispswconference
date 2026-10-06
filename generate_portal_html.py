import json
import os

print("Generating international dignified conference portal HTML...")

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

json_data_str = json.dumps(db, ensure_ascii=False)

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Annual National Conference of ISPSW – 2026 | Davangere University</title>
  <meta name="description" content="Official Programme Schedule, Abstracts, and Presenter Directory for the Annual National Conference of ISPSW – 2026 on Innovative Technologies for Social Work Practice, Research and Development.">
  
  <!-- Elite Academic Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

  <style>
    :root {
      --navy-950: #060b19;
      --navy-900: #0b132b;
      --navy-850: #101c3d;
      --navy-800: #1c2541;
      --navy-700: #2a3b60;
      --gold-600: #a17717;
      --gold-500: #c59b27;
      --gold-400: #d4af37;
      --gold-300: #e6ca65;
      --gold-100: #fbf5df;
      --gold-50: #fefdf7;
      --maroon-900: #58101a;
      --maroon-800: #701a28;
      --maroon-700: #881337;
      --slate-50: #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1e293b;
      --slate-900: #0f172a;
      
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', SFMono-Regular, monospace;
      --font-display: 'Cinzel', serif;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
      --shadow-gold: 0 10px 25px -5px rgba(197, 155, 39, 0.25);
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-xl: 24px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: var(--font-sans);
      background-color: #f8f9fb;
      color: var(--slate-800);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
    }

    /* Top National Header Stripe */
    .top-academic-bar {
      background: linear-gradient(90deg, var(--navy-950) 0%, var(--maroon-900) 50%, var(--navy-950) 100%);
      color: #fff;
      font-size: 0.82rem;
      padding: 8px 24px;
      border-bottom: 2px solid var(--gold-400);
      letter-spacing: 0.5px;
    }

    .top-academic-bar .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .top-badge-pulse {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(212, 175, 55, 0.2);
      border: 1px solid var(--gold-400);
      padding: 3px 10px;
      border-radius: 999px;
      font-weight: 600;
      color: var(--gold-300);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .pulse-dot {
      width: 7px;
      height: 7px;
      background-color: var(--gold-400);
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7); }
      70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(212, 175, 55, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212, 175, 55, 0); }
    }

    /* Container Utility */
    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Grand Elite Header */
    .grand-header {
      background: linear-gradient(135deg, #070e24 0%, #0d1b3e 60%, #15224a 100%);
      color: #ffffff;
      padding: 40px 0 32px 0;
      position: relative;
      border-bottom: 3px solid var(--gold-400);
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    .grand-header::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: radial-gradient(rgba(212, 175, 55, 0.08) 1px, transparent 1px);
      background-size: 24px 24px;
      pointer-events: none;
    }

    .header-branding {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
      position: relative;
      z-index: 1;
    }

    .logo-container {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .official-logo-box {
      width: 90px;
      height: 90px;
      background: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
      box-shadow: 0 0 20px rgba(212, 175, 55, 0.4), 0 0 0 2px var(--gold-400);
      transition: transform 0.3s ease;
    }

    .official-logo-box:hover {
      transform: scale(1.05);
    }

    .official-logo-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }

    .logo-fallback {
      font-size: 2.2rem;
      color: var(--navy-900);
    }

    .branding-text {
      text-align: center;
      flex: 1;
      min-width: 320px;
    }

    .university-title {
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 700;
      letter-spacing: 2px;
      color: #ffffff;
      text-transform: uppercase;
      margin-bottom: 4px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }

    .department-title {
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--gold-300);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .joint-text {
      font-family: var(--font-serif);
      font-style: italic;
      color: #cbd5e1;
      font-size: 0.95rem;
      margin: 4px 0;
    }

    .society-title {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }

    .society-acronym {
      color: var(--gold-400);
      font-weight: 800;
    }

    .header-quick-actions {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 12px;
    }

    .btn-find-my-paper {
      background: linear-gradient(135deg, var(--gold-500) 0%, var(--gold-400) 100%);
      color: var(--navy-950);
      font-weight: 700;
      font-size: 0.9rem;
      padding: 12px 24px;
      border-radius: var(--radius-md);
      border: 1px solid #fff;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
      transition: all 0.25s ease;
      text-decoration: none;
    }

    .btn-find-my-paper:hover {
      background: linear-gradient(135deg, #fff 0%, var(--gold-300) 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6);
    }

    .header-contacts-chip {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-md);
      padding: 8px 14px;
      font-size: 0.8rem;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Conference Hero Banner */
    .conference-hero-box {
      margin-top: 36px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(212, 175, 55, 0.3);
      border-radius: var(--radius-lg);
      padding: 32px 36px;
      backdrop-filter: blur(10px);
      box-shadow: inset 0 0 30px rgba(0,0,0,0.2);
      text-align: center;
      position: relative;
    }

    .conference-hero-box::after {
      content: "";
      position: absolute;
      bottom: -1px; left: 15%; right: 15%;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--gold-400), transparent);
    }

    .conf-pretitle {
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 3px;
      color: var(--gold-300);
      font-weight: 600;
      margin-bottom: 8px;
    }

    .conf-main-title {
      font-family: var(--font-serif);
      font-size: 2.35rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.5px;
      line-height: 1.25;
      margin-bottom: 12px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.5);
    }

    .conf-theme-quote {
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-style: italic;
      color: var(--gold-300);
      max-width: 950px;
      margin: 0 auto 20px auto;
      line-height: 1.4;
      font-weight: 600;
    }

    .conf-meta-pills {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-top: 18px;
    }

    .meta-pill {
      background: rgba(11, 19, 43, 0.8);
      border: 1px solid rgba(212, 175, 55, 0.4);
      padding: 8px 18px;
      border-radius: 999px;
      font-size: 0.88rem;
      color: #f1f5f9;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 500;
    }

    .meta-pill i {
      color: var(--gold-400);
    }

    /* Key Numbers Showcase */
    .stats-ribbon {
      background: #ffffff;
      border-bottom: 1px solid var(--slate-200);
      padding: 18px 0;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      text-align: center;
    }

    .stat-card {
      padding: 10px 16px;
      border-right: 1px solid var(--slate-200);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .stat-card:last-child {
      border-right: none;
    }

    .stat-number {
      font-family: var(--font-display);
      font-size: 2rem;
      font-weight: 800;
      color: var(--navy-900);
      line-height: 1;
      margin-bottom: 4px;
    }

    .stat-number.gold {
      color: var(--gold-600);
    }

    .stat-label {
      font-size: 0.78rem;
      color: var(--slate-600);
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 600;
    }

    /* Sticky Navigation & Tab Bar */
    .portal-nav-sticky {
      position: sticky;
      top: 0;
      z-index: 100;
      background: #ffffff;
      border-bottom: 2px solid var(--slate-200);
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }

    .nav-tabs-wrapper {
      display: flex;
      gap: 4px;
      overflow-x: auto;
      padding: 6px 0;
      scrollbar-width: none;
    }

    .nav-tabs-wrapper::-webkit-scrollbar {
      display: none;
    }

    .tab-btn {
      background: none;
      border: none;
      padding: 12px 18px;
      border-radius: var(--radius-md);
      font-family: var(--font-sans);
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--slate-600);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: all 0.2s ease;
      position: relative;
    }

    .tab-btn i {
      font-size: 0.95rem;
      color: var(--slate-400);
      transition: color 0.2s ease;
    }

    .tab-btn:hover {
      color: var(--navy-900);
      background: var(--slate-100);
    }

    .tab-btn:hover i {
      color: var(--gold-500);
    }

    .tab-btn.active {
      color: var(--navy-950);
      background: #fff;
      font-weight: 700;
    }

    .tab-btn.active i {
      color: var(--gold-500);
    }

    .tab-btn.active::after {
      content: "";
      position: absolute;
      bottom: -8px;
      left: 12px;
      right: 12px;
      height: 3px;
      background: linear-gradient(90deg, var(--gold-500), var(--maroon-800));
      border-radius: 3px 3px 0 0;
    }

    .badge-tab-count {
      background: var(--slate-200);
      color: var(--slate-700);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
      margin-left: 2px;
    }

    .tab-btn.active .badge-tab-count {
      background: var(--gold-100);
      color: var(--gold-600);
    }

    /* Main Content Sections */
    .tab-content-panel {
      display: none;
      padding: 40px 0 60px 0;
    }

    .tab-content-panel.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Section Headers */
    .academic-section-heading {
      text-align: center;
      margin-bottom: 36px;
      position: relative;
    }

    .academic-section-heading .subtitle {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--gold-600);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 6px;
      display: inline-block;
    }

    .academic-section-heading h2 {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: var(--navy-950);
      font-weight: 700;
      line-height: 1.3;
    }

    .academic-section-heading p {
      color: var(--slate-600);
      font-size: 1rem;
      max-width: 750px;
      margin: 8px auto 0 auto;
    }

    .heading-divider {
      width: 60px;
      height: 3px;
      background: var(--gold-400);
      margin: 14px auto 0 auto;
      border-radius: 2px;
    }

    /* Power Search Toolbar */
    .search-control-deck {
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 28px;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--slate-200);
      margin-bottom: 32px;
      position: relative;
    }

    .search-control-deck::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--gold-500), var(--maroon-800), var(--navy-800));
      border-radius: var(--radius-lg) var(--radius-lg) 0 0;
    }

    .search-primary-row {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 16px;
      margin-bottom: 20px;
    }

    @media (max-width: 850px) {
      .search-primary-row {
        grid-template-columns: 1fr;
      }
    }

    .search-input-group {
      position: relative;
      display: flex;
      align-items: center;
    }

    .search-icon-inside {
      position: absolute;
      left: 18px;
      font-size: 1.15rem;
      color: var(--gold-600);
      pointer-events: none;
    }

    .main-search-input {
      width: 100%;
      padding: 16px 20px 16px 50px;
      font-family: var(--font-sans);
      font-size: 1.05rem;
      border: 2px solid var(--slate-200);
      border-radius: var(--radius-md);
      background: #fff;
      color: var(--slate-900);
      transition: all 0.25s ease;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }

    .main-search-input:focus {
      outline: none;
      border-color: var(--gold-500);
      box-shadow: 0 0 0 4px rgba(197, 155, 39, 0.15);
    }

    .search-mode-select {
      padding: 16px 18px;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 500;
      border: 2px solid var(--slate-200);
      border-radius: var(--radius-md);
      background: var(--slate-50);
      color: var(--slate-800);
      cursor: pointer;
      transition: border-color 0.2s ease;
    }

    .search-mode-select:focus {
      outline: none;
      border-color: var(--gold-500);
    }

    /* Filters Grid */
    .filter-grid-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
      padding-top: 16px;
      border-top: 1px solid var(--slate-200);
    }

    .filter-item {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .filter-label {
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--slate-600);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .filter-select {
      width: 100%;
      padding: 10px 14px;
      font-family: var(--font-sans);
      font-size: 0.88rem;
      border: 1px solid var(--slate-300);
      border-radius: var(--radius-sm);
      background: #fff;
      color: var(--slate-800);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .filter-select:focus {
      outline: none;
      border-color: var(--gold-500);
      box-shadow: 0 0 0 3px rgba(197, 155, 39, 0.12);
    }

    /* Active Filter & Summary Bar */
    .filter-feedback-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px dashed var(--slate-200);
    }

    .results-count-text {
      font-size: 0.92rem;
      color: var(--slate-700);
      font-weight: 600;
    }

    .results-count-text strong {
      color: var(--navy-950);
      font-family: var(--font-mono);
      font-size: 1.05rem;
    }

    .filter-actions-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .view-toggle-btn-group {
      display: inline-flex;
      border: 1px solid var(--slate-300);
      border-radius: var(--radius-sm);
      overflow: hidden;
    }

    .view-btn {
      background: #fff;
      border: none;
      padding: 7px 12px;
      cursor: pointer;
      color: var(--slate-600);
      font-size: 0.85rem;
      transition: all 0.2s;
    }

    .view-btn.active {
      background: var(--navy-900);
      color: #fff;
    }

    .btn-reset-filters {
      background: none;
      border: 1px solid var(--slate-300);
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--maroon-800);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .btn-reset-filters:hover {
      background: #fee2e2;
      border-color: var(--maroon-800);
    }

    /* Quick Theme Chips Row */
    .theme-quick-chips {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 8px 0 16px 0;
      margin-bottom: 24px;
      scrollbar-width: thin;
    }

    .theme-chip {
      background: #ffffff;
      border: 1px solid var(--slate-200);
      border-radius: 999px;
      padding: 6px 14px;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--slate-700);
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    .theme-chip:hover {
      border-color: var(--gold-500);
      transform: translateY(-1px);
    }

    .theme-chip.active {
      background: var(--navy-900);
      color: #ffffff;
      border-color: var(--navy-900);
      box-shadow: 0 4px 10px rgba(11, 19, 43, 0.2);
    }

    .theme-chip.active i {
      color: var(--gold-400);
    }

    /* Papers Results Display */
    .papers-container.grid-view {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
      gap: 22px;
    }

    @media (max-width: 600px) {
      .papers-container.grid-view {
        grid-template-columns: 1fr;
      }
    }

    .papers-container.list-view {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    /* Paper Card Styling */
    .paper-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      transition: all 0.25s ease;
      box-shadow: var(--shadow-sm);
    }

    .paper-card:hover {
      border-color: var(--gold-500);
      transform: translateY(-3px);
      box-shadow: 0 12px 24px -6px rgba(0,0,0,0.08), 0 0 0 1px rgba(197, 155, 39, 0.2);
    }

    .paper-card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }

    .paper-code-badge {
      font-family: var(--font-mono);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--gold-600);
      background: var(--gold-100);
      border: 1px solid var(--gold-300);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.5px;
    }

    .paper-theme-tag {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 999px;
      background: var(--slate-100);
      color: var(--slate-700);
      max-width: 220px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .paper-title {
      font-family: var(--font-serif);
      font-size: 1.18rem;
      font-weight: 700;
      color: var(--navy-950);
      line-height: 1.4;
      margin-bottom: 12px;
    }

    .paper-authors {
      font-size: 0.9rem;
      color: var(--slate-800);
      font-weight: 600;
      margin-bottom: 8px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }

    .paper-authors i {
      color: var(--maroon-700);
      margin-top: 4px;
      font-size: 0.85rem;
    }

    .paper-affiliation {
      font-size: 0.8rem;
      color: var(--slate-500);
      margin-bottom: 16px;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .paper-slot-info-box {
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      margin-bottom: 16px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      font-size: 0.8rem;
    }

    @media (max-width: 480px) {
      .paper-slot-info-box {
        grid-template-columns: 1fr;
      }
    }

    .slot-detail-item {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--slate-700);
    }

    .slot-detail-item i {
      color: var(--gold-600);
      width: 14px;
      font-size: 0.85rem;
    }

    .slot-detail-item strong {
      color: var(--slate-900);
    }

    .paper-footer-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid var(--slate-100);
    }

    .btn-read-abstract {
      background: #ffffff;
      border: 1px solid var(--navy-800);
      color: var(--navy-900);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-read-abstract:hover {
      background: var(--navy-900);
      color: #ffffff;
    }

    .btn-bookmark-paper {
      background: none;
      border: 1px solid var(--slate-200);
      width: 34px;
      height: 34px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--slate-400);
      font-size: 0.95rem;
      transition: all 0.2s;
    }

    .btn-bookmark-paper:hover {
      color: var(--gold-500);
      border-color: var(--gold-400);
      background: var(--gold-50);
    }

    .btn-bookmark-paper.bookmarked {
      color: var(--gold-500);
      border-color: var(--gold-400);
      background: var(--gold-100);
    }

    /* List View Format */
    .papers-container.list-view .paper-card {
      padding: 16px 20px;
    }

    .papers-container.list-view .paper-card-inner-flex {
      display: grid;
      grid-template-columns: 80px 1fr 280px 140px;
      align-items: center;
      gap: 18px;
    }

    @media (max-width: 950px) {
      .papers-container.list-view .paper-card-inner-flex {
        grid-template-columns: 1fr;
        gap: 10px;
      }
    }

    /* Full Programme Timeline View */
    .days-switcher {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 32px;
      flex-wrap: wrap;
    }

    .day-switch-btn {
      background: #ffffff;
      border: 2px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 14px 28px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 200px;
      transition: all 0.25s ease;
      box-shadow: var(--shadow-sm);
    }

    .day-switch-btn:hover {
      border-color: var(--gold-500);
      transform: translateY(-2px);
    }

    .day-switch-btn.active {
      background: var(--navy-900);
      border-color: var(--navy-900);
      color: #ffffff;
      box-shadow: 0 8px 20px rgba(11, 19, 43, 0.2);
    }

    .day-switch-btn .day-title-text {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 1px;
    }

    .day-switch-btn .day-sub-text {
      font-size: 0.8rem;
      color: var(--slate-500);
      margin-top: 2px;
    }

    .day-switch-btn.active .day-sub-text {
      color: var(--gold-300);
    }

    /* Timeline Cards */
    .timeline-wrapper {
      position: relative;
      max-width: 1050px;
      margin: 0 auto;
      padding: 20px 0;
    }

    .timeline-event-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      padding: 22px 28px;
      margin-bottom: 18px;
      display: grid;
      grid-template-columns: 180px 1fr;
      gap: 24px;
      box-shadow: var(--shadow-sm);
      position: relative;
      transition: all 0.2s ease;
    }

    @media (max-width: 768px) {
      .timeline-event-card {
        grid-template-columns: 1fr;
        gap: 12px;
      }
    }

    .timeline-event-card:hover {
      border-color: var(--gold-400);
      box-shadow: var(--shadow-md);
    }

    .timeline-event-card.ceremonial {
      border-left: 5px solid var(--gold-500);
    }

    .timeline-event-card.plenary {
      border-left: 5px solid var(--maroon-700);
    }

    .timeline-event-card.panel {
      border-left: 5px solid #2563eb;
    }

    .timeline-event-card.technical {
      border-left: 5px solid #059669;
    }

    .timeline-event-card.special {
      border-left: 5px solid #7c3aed;
    }

    .timeline-event-card.cultural {
      border-left: 5px solid #e11d48;
    }

    .timeline-event-card.meals {
      border-left: 5px solid var(--slate-400);
      background: var(--slate-50);
    }

    .event-time-col {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    .event-time-badge {
      font-family: var(--font-mono);
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--navy-900);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
    }

    .event-cat-badge {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      width: fit-content;
    }

    .cat-ceremonial { background: var(--gold-100); color: var(--gold-600); }
    .cat-plenary { background: #ffe4e6; color: var(--maroon-700); }
    .cat-panel { background: #dbeafe; color: #1e40af; }
    .cat-technical { background: #d1fae5; color: #065f46; }
    .cat-special { background: #ede9fe; color: #5b21b6; }
    .cat-cultural { background: #fce7f3; color: #9d174d; }
    .cat-meals { background: var(--slate-200); color: var(--slate-700); }

    .event-details-col h4 {
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: var(--navy-950);
      margin-bottom: 6px;
    }

    .event-desc-text {
      color: var(--slate-700);
      font-size: 0.95rem;
      margin-bottom: 10px;
      line-height: 1.5;
    }

    .event-venue-text {
      font-size: 0.82rem;
      color: var(--slate-500);
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 500;
    }

    /* Technical Sessions Matrix */
    .tracks-matrix-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 24px;
    }

    .track-session-box {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--slate-200);
      padding: 26px;
      box-shadow: var(--shadow-md);
      transition: all 0.25s ease;
      position: relative;
    }

    .track-session-box:hover {
      border-color: var(--gold-400);
      transform: translateY(-3px);
      box-shadow: var(--shadow-xl);
    }

    .track-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--slate-200);
    }

    .track-num-pill {
      background: var(--navy-900);
      color: #ffffff;
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      letter-spacing: 1px;
    }

    .track-session-box h3 {
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--navy-950);
      margin-bottom: 8px;
    }

    .track-meta-list {
      list-style: none;
      font-size: 0.88rem;
      color: var(--slate-700);
      margin-bottom: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .track-meta-list li {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }

    .track-meta-list i {
      color: var(--gold-600);
      margin-top: 4px;
      width: 16px;
    }

    .btn-view-track-papers {
      width: 100%;
      background: var(--slate-100);
      border: 1px solid var(--slate-300);
      color: var(--navy-950);
      font-weight: 700;
      font-size: 0.88rem;
      padding: 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
    }

    .btn-view-track-papers:hover {
      background: var(--navy-900);
      color: #ffffff;
      border-color: var(--navy-900);
    }

    /* Themes Showcase Cards */
    .themes-grid-5 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 22px;
    }

    .theme-card-rich {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--slate-200);
      padding: 28px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    .theme-card-rich:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-xl);
      border-color: var(--gold-400);
    }

    .theme-icon-wrap {
      width: 52px;
      height: 52px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      margin-bottom: 18px;
    }

    .theme-card-rich h3 {
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: var(--navy-950);
      margin-bottom: 12px;
      line-height: 1.35;
    }

    .theme-card-rich p {
      color: var(--slate-600);
      font-size: 0.9rem;
      line-height: 1.5;
      margin-bottom: 20px;
    }

    /* Dignitaries Grid */
    .dignitaries-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
    }

    .dignitary-card {
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--slate-200);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      display: flex;
      gap: 20px;
      align-items: center;
      transition: all 0.25s ease;
    }

    .dignitary-card:hover {
      border-color: var(--gold-400);
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
    }

    .dignitary-avatar-wrap {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--gold-100) 0%, var(--gold-300) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      color: var(--navy-900);
      flex-shrink: 0;
      border: 2px solid var(--gold-400);
    }

    .dignitary-info h4 {
      font-family: var(--font-serif);
      font-size: 1.15rem;
      color: var(--navy-950);
      margin-bottom: 4px;
    }

    .dignitary-role-badge {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--gold-600);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      display: inline-block;
    }

    .dignitary-org {
      font-size: 0.82rem;
      color: var(--slate-600);
      line-height: 1.35;
    }

    /* Campus & Helpdesk Guide */
    .helpdesk-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-bottom: 32px;
    }

    .helpdesk-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }

    .helpdesk-card i {
      font-size: 1.8rem;
      color: var(--gold-600);
      margin-bottom: 10px;
    }

    .helpdesk-card h4 {
      font-family: var(--font-serif);
      font-size: 1.05rem;
      color: var(--navy-950);
      margin-bottom: 4px;
    }

    .helpdesk-card .contact-name {
      font-weight: 700;
      color: var(--slate-800);
      font-size: 0.9rem;
      margin-bottom: 6px;
    }

    .helpdesk-card a {
      color: var(--navy-700);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      font-weight: 600;
    }

    .helpdesk-card a:hover {
      text-decoration: underline;
    }

    /* Abstract Modal Drawer */
    .abstract-modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(11, 19, 43, 0.75);
      backdrop-filter: blur(6px);
      z-index: 999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .abstract-modal-overlay.active {
      display: flex;
      opacity: 1;
    }

    .abstract-modal-card {
      background: #ffffff;
      border-radius: var(--radius-xl);
      max-width: 900px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      border: 2px solid var(--gold-400);
      position: relative;
      animation: modalSlideUp 0.3s ease;
    }

    @keyframes modalSlideUp {
      from { transform: translateY(30px) scale(0.97); }
      to { transform: translateY(0) scale(1); }
    }

    .modal-header-banner {
      background: linear-gradient(135deg, var(--navy-950) 0%, var(--navy-850) 100%);
      color: #ffffff;
      padding: 28px 32px;
      position: relative;
      border-bottom: 3px solid var(--gold-400);
    }

    .modal-close-btn {
      position: absolute;
      top: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.15);
      border: none;
      color: #ffffff;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      transition: all 0.2s;
    }

    .modal-close-btn:hover {
      background: var(--gold-400);
      color: var(--navy-950);
      transform: rotate(90deg);
    }

    .modal-code-tag {
      font-family: var(--font-mono);
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--gold-300);
      background: rgba(212, 175, 55, 0.2);
      border: 1px solid var(--gold-400);
      padding: 3px 12px;
      border-radius: 999px;
      display: inline-block;
      margin-bottom: 10px;
    }

    .modal-title-text {
      font-family: var(--font-serif);
      font-size: 1.55rem;
      font-weight: 700;
      line-height: 1.35;
      color: #ffffff;
    }

    .modal-body-content {
      padding: 32px;
    }

    .modal-schedule-meta-box {
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 24px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      font-size: 0.88rem;
    }

    .modal-authors-box {
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--slate-200);
    }

    .modal-authors-title {
      font-size: 0.82rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--gold-600);
      letter-spacing: 1px;
      margin-bottom: 6px;
    }

    .modal-authors-names {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--navy-950);
      margin-bottom: 6px;
    }

    .modal-affiliation-text {
      font-size: 0.88rem;
      color: var(--slate-600);
      line-height: 1.5;
      white-space: pre-line;
    }

    .modal-abstract-section {
      margin-bottom: 24px;
    }

    .modal-abstract-section h4 {
      font-family: var(--font-serif);
      font-size: 1.2rem;
      color: var(--navy-900);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .modal-abstract-body {
      font-size: 0.96rem;
      line-height: 1.7;
      color: var(--slate-800);
      text-align: justify;
      white-space: pre-line;
    }

    .modal-keywords-box {
      margin-top: 24px;
      padding-top: 18px;
      border-top: 1px dashed var(--slate-200);
    }

    .keywords-chips-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 8px;
    }

    .kw-pill {
      background: var(--slate-100);
      color: var(--slate-800);
      font-size: 0.8rem;
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid var(--slate-200);
      font-weight: 500;
    }

    .modal-footer-toolbar {
      padding: 18px 32px;
      background: var(--slate-50);
      border-top: 1px solid var(--slate-200);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .modal-actions-btns {
      display: flex;
      gap: 10px;
    }

    .btn-modal-action {
      background: #ffffff;
      border: 1px solid var(--slate-300);
      padding: 9px 18px;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--navy-900);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-modal-action:hover {
      background: var(--navy-900);
      color: #fff;
    }

    .btn-modal-action.primary {
      background: var(--gold-500);
      color: var(--navy-950);
      border-color: var(--gold-400);
    }

    .btn-modal-action.primary:hover {
      background: var(--navy-900);
      color: #fff;
    }

    /* Candidate Quick Pass Modal */
    .quick-pass-box {
      background: linear-gradient(135deg, #101c3d 0%, #1c2541 100%);
      color: #fff;
      border-radius: var(--radius-lg);
      padding: 24px 30px;
      margin-bottom: 28px;
      border: 2px solid var(--gold-400);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    .quick-pass-text h3 {
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: #ffffff;
      margin-bottom: 4px;
    }

    .quick-pass-text p {
      color: var(--gold-300);
      font-size: 0.9rem;
    }

    .quick-pass-form {
      display: flex;
      gap: 10px;
      flex: 1;
      max-width: 450px;
      min-width: 280px;
    }

    .quick-pass-input {
      flex: 1;
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--gold-400);
      background: #fff;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      color: var(--slate-900);
    }

    .quick-pass-btn {
      background: var(--gold-400);
      color: var(--navy-950);
      font-weight: 700;
      border: none;
      padding: 12px 20px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .quick-pass-btn:hover {
      background: #fff;
      transform: translateY(-1px);
    }

    /* Print Formatting */
    @media print {
      .top-academic-bar,
      .portal-nav-sticky,
      .search-control-deck,
      .theme-quick-chips,
      .quick-pass-box,
      .header-quick-actions,
      .btn-read-abstract,
      .btn-bookmark-paper,
      .modal-footer-toolbar,
      .site-footer {
        display: none !important;
      }
      
      body {
        background: #fff !important;
        color: #000 !important;
      }

      .grand-header {
        background: #fff !important;
        color: #000 !important;
        border-bottom: 2px solid #000;
      }

      .university-title, .society-title, .conf-main-title {
        color: #000 !important;
      }

      .paper-card, .timeline-event-card {
        page-break-inside: avoid;
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        margin-bottom: 12px !important;
      }
    }

    /* Footer */
    .site-footer {
      background: var(--navy-950);
      color: #94a3b8;
      padding: 60px 0 30px 0;
      border-top: 3px solid var(--gold-400);
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 40px;
    }

    @media (max-width: 850px) {
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 24px;
      }
    }

    .footer-col h4 {
      font-family: var(--font-serif);
      color: #ffffff;
      font-size: 1.15rem;
      margin-bottom: 16px;
      position: relative;
      padding-bottom: 8px;
    }

    .footer-col h4::after {
      content: "";
      position: absolute;
      bottom: 0; left: 0;
      width: 40px; height: 2px;
      background: var(--gold-400);
    }

    .footer-col p {
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 12px;
    }

    .footer-links-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.88rem;
    }

    .footer-links-list a {
      color: #94a3b8;
      text-decoration: none;
      transition: color 0.2s;
    }

    .footer-links-list a:hover {
      color: var(--gold-300);
    }

    .bottom-copyright {
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      text-align: center;
      font-size: 0.8rem;
      color: #64748b;
    }

    /* Toast Notification */
    .toast-popup {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--navy-900);
      color: #ffffff;
      border: 1px solid var(--gold-400);
      border-radius: var(--radius-md);
      padding: 14px 22px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s ease;
      font-size: 0.9rem;
    }

    .toast-popup.show {
      transform: translateY(0);
      opacity: 1;
    }

    .toast-popup i {
      color: var(--gold-400);
      font-size: 1.2rem;
    }
  </style>
</head>
<body>

  <!-- Top Academic Stripe -->
  <div class="top-academic-bar">
    <div class="container">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span class="top-badge-pulse"><span class="pulse-dot"></span> Official Conference Portal</span>
        <span>Shivagangotri Campus, Davangere University · Tholahunase, Davanagere – 577007, Karnataka, India</span>
      </div>
      <div>
        <span>Annual National Conference of ISPSW – 2026</span>
        <span style="margin: 0 8px; opacity: 0.4;">|</span>
        <a href="mailto:dumswispswnc2026@gmail.com" style="color: var(--gold-300); text-decoration: none;"><i class="fa-regular fa-envelope"></i> dumswispswnc2026@gmail.com</a>
      </div>
    </div>
  </div>

  <!-- Grand Academic Header -->
  <header class="grand-header">
    <div class="container">
      <div class="header-branding">
        
        <!-- Left Logo: Davangere University -->
        <div class="logo-container">
          <div class="official-logo-box" title="Davangere University Emblem">
            __DAVANGERE_LOGO_HTML__
          </div>
        </div>

        <!-- Centre Academic Typography -->
        <div class="branding-text">
          <h1 class="university-title">DAVANGERE UNIVERSITY</h1>
          <h3 class="department-title">Department of Studies in Social Work</h3>
          <p class="joint-text">&amp;</p>
          <h2 class="society-title">INDIAN SOCIETY OF PROFESSIONAL SOCIAL WORK <span class="society-acronym">[ISPSW]</span></h2>
        </div>

        <!-- Right Logo: ISPSW -->
        <div class="logo-container">
          <div class="official-logo-box" title="Indian Society of Professional Social Work Logo">
            __ISPSW_LOGO_HTML__
          </div>
        </div>

      </div>

      <!-- Conference Title & Focal Theme Hero Banner -->
      <div class="conference-hero-box">
        <p class="conf-pretitle">Jointly Organize the Annual National Conference of ISPSW – 2026</p>
        <h2 class="conf-main-title">“Innovative Technologies for Social Work Practice, Research and Development”</h2>
        
        <div class="conf-meta-pills">
          <span class="meta-pill"><i class="fa-regular fa-calendar-days"></i> <strong>7th – 9th OCTOBER, 2026</strong></span>
          <span class="meta-pill"><i class="fa-solid fa-location-dot"></i> <strong>MBA Auditorium &amp; Lecture Halls, Shivagangotri Campus</strong></span>
          <span class="meta-pill"><i class="fa-solid fa-award"></i> <strong>Theme-wise Peer-Reviewed Compilation</strong></span>
        </div>
      </div>
    </div>
  </header>

  <!-- Key Statistics Ribbon -->
  <section class="stats-ribbon">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-card">
          <span class="stat-number gold" id="stat-total-papers">115</span>
          <span class="stat-label">Accepted Papers &amp; Abstracts</span>
        </div>
        <div class="stat-card">
          <span class="stat-number">3</span>
          <span class="stat-label">Conference Days</span>
        </div>
        <div class="stat-card">
          <span class="stat-number">9</span>
          <span class="stat-label">Technical Tracks</span>
        </div>
        <div class="stat-card">
          <span class="stat-number">4</span>
          <span class="stat-label">Plenary Sessions</span>
        </div>
        <div class="stat-card">
          <span class="stat-number">3</span>
          <span class="stat-label">Panel Discussions</span>
        </div>
        <div class="stat-card">
          <span class="stat-number gold">5</span>
          <span class="stat-label">Core Thematic Domains</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Sticky Portal Navigation Bar -->
  <nav class="portal-nav-sticky">
    <div class="container">
      <div class="nav-tabs-wrapper">
        <button class="tab-btn active" onclick="switchMainTab('directory')">
          <i class="fa-solid fa-magnifying-glass"></i> Presentation Directory &amp; Abstracts
          <span class="badge-tab-count" id="badge-nav-count">115</span>
        </button>
        <button class="tab-btn" onclick="switchMainTab('schedule')">
          <i class="fa-regular fa-calendar-check"></i> Complete Programme Flow (Day 1 - 3)
        </button>
        <button class="tab-btn" onclick="switchMainTab('tracks')">
          <i class="fa-solid fa-network-wired"></i> 9 Technical Tracks Matrix
        </button>
        <button class="tab-btn" onclick="switchMainTab('themes')">
          <i class="fa-solid fa-layer-group"></i> 5 Conference Themes
        </button>
        <button class="tab-btn" onclick="switchMainTab('dignitaries')">
          <i class="fa-solid fa-user-tie"></i> Dignitaries &amp; Leadership
        </button>
        <button class="tab-btn" onclick="switchMainTab('itinerary')">
          <i class="fa-regular fa-bookmark"></i> My Personal Itinerary
          <span class="badge-tab-count" id="badge-bookmark-count" style="display:none;">0</span>
        </button>
        <button class="tab-btn" onclick="switchMainTab('venue')">
          <i class="fa-solid fa-compass"></i> Venue &amp; Helpdesk
        </button>
      </div>
    </div>
  </nav>

  <!-- Main Container -->
  <main class="container">

    <!-- ========================================== -->
    <!-- TAB 1: PRESENTATION DIRECTORY & SEARCH     -->
    <!-- ========================================== -->
    <section id="panel-directory" class="tab-content-panel active">
      
      <!-- Quick Candidate Pass Banner -->
      <div class="quick-pass-box">
        <div class="quick-pass-text">
          <h3><i class="fa-solid fa-id-badge" style="color: var(--gold-400); margin-right: 8px;"></i> Presenter Quick Pass</h3>
          <p>Presenting a paper? Enter your author name, college, or paper code to instantly reveal your exact time slot, hall, and session chair.</p>
        </div>
        <div class="quick-pass-form">
          <input type="text" id="quick-pass-input" class="quick-pass-input" placeholder="Enter author name or code (e.g., Deepika, B4, F12)...">
          <button class="quick-pass-btn" onclick="executeQuickPass()"><i class="fa-solid fa-arrow-right"></i> Find Now</button>
        </div>
      </div>

      <!-- Powerful Search & Filter Toolbar -->
      <div class="search-control-deck">
        
        <!-- Primary Search Row -->
        <div class="search-primary-row">
          <div class="search-input-group">
            <i class="fa-solid fa-magnifying-glass search-icon-inside"></i>
            <input type="text" id="master-search-input" class="main-search-input" placeholder="Search by Author Name, Paper Code (A1..J24), Paper Title, Keywords, Hall, or Topic..." oninput="handleSearchInput()">
          </div>
          <select id="search-mode-select" class="search-mode-select" onchange="applyFilters()">
            <option value="all">🔍 Search In: All Fields</option>
            <option value="author">👤 Search In: Author / Presenter Name</option>
            <option value="title">📄 Search In: Paper Title Only</option>
            <option value="code">🏷️ Search In: Paper Code (A1, B5, etc.)</option>
            <option value="keywords">🔑 Search In: Keywords &amp; Abstract</option>
            <option value="chair">🎓 Search In: Session Chairperson</option>
          </select>
        </div>

        <!-- Filter Grid Row -->
        <div class="filter-grid-row">
          
          <!-- Filter by Theme -->
          <div class="filter-item">
            <label class="filter-label"><i class="fa-solid fa-layer-group"></i> Conference Theme</label>
            <select id="filter-theme" class="filter-select" onchange="applyFilters()">
              <option value="all">All 5 Themes</option>
              <option value="Theme 1">Theme 1: Learning &amp; Tech</option>
              <option value="Theme 2">Theme 2: AI &amp; Interventions</option>
              <option value="Theme 3">Theme 3: Gender Equity &amp; Inclusion</option>
              <option value="Theme 4">Theme 4: Policy, Ethics &amp; Regulation</option>
              <option value="Theme 5">Theme 5: Technologies for Viksit Bharat</option>
            </select>
          </div>

          <!-- Filter by Day / Date -->
          <div class="filter-item">
            <label class="filter-label"><i class="fa-regular fa-calendar"></i> Presentation Day</label>
            <select id="filter-day" class="filter-select" onchange="applyFilters()">
              <option value="all">All Days (Oct 7 – 9)</option>
              <option value="Day 01">Day 01 (07.10.2026, Wed)</option>
              <option value="Day 02">Day 02 (08.10.2026, Thu)</option>
              <option value="Day 03">Day 03 (09.10.2026, Fri)</option>
            </select>
          </div>

          <!-- Filter by Venue -->
          <div class="filter-item">
            <label class="filter-label"><i class="fa-solid fa-location-dot"></i> Venue / Hall</label>
            <select id="filter-venue" class="filter-select" onchange="applyFilters()">
              <option value="all">All Halls</option>
              <option value="MBA Auditorium">MBA Auditorium</option>
              <option value="MBA Lecture Hall-01">MBA Lecture Hall-01</option>
              <option value="MBA Lecture Hall-02">MBA Lecture Hall-02</option>
            </select>
          </div>

          <!-- Filter by Track -->
          <div class="filter-item">
            <label class="filter-label"><i class="fa-solid fa-arrow-down-short-wide"></i> Sort Schedule By</label>
            <select id="sort-order" class="filter-select" onchange="applyFilters()">
              <option value="time">Chronological Presentation Time</option>
              <option value="code-asc">Paper Code (A → Z)</option>
              <option value="code-desc">Paper Code (Z → A)</option>
              <option value="title-asc">Paper Title (A → Z)</option>
              <option value="author-asc">Author Name (A → Z)</option>
              <option value="theme">By Conference Theme</option>
            </select>
          </div>

        </div>

        <!-- Filter Status & View Toggles -->
        <div class="filter-feedback-bar">
          <div class="results-count-text">
            Showing <strong id="visible-papers-count">115</strong> of 115 presentations
            <span id="active-filter-indicators" style="margin-left: 10px; font-weight: normal; color: var(--slate-500);"></span>
          </div>

          <div class="filter-actions-right">
            <button class="btn-reset-filters" onclick="resetAllFilters()">
              <i class="fa-solid fa-rotate-left"></i> Reset Filters
            </button>
            <div class="view-toggle-btn-group">
              <button class="view-btn active" id="btn-view-grid" onclick="setViewMode('grid')" title="Card Grid View">
                <i class="fa-solid fa-grip"></i> Grid
              </button>
              <button class="view-btn" id="btn-view-list" onclick="setViewMode('list')" title="Detailed List View">
                <i class="fa-solid fa-list"></i> List
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- Quick Theme Pills Row -->
      <div class="theme-quick-chips">
        <button class="theme-chip active" onclick="quickFilterTheme('all', this)"><i class="fa-solid fa-border-all"></i> All Presentations</button>
        <button class="theme-chip" onclick="quickFilterTheme('Theme 1', this)"><i class="fa-solid fa-graduation-cap"></i> Theme 1: Learning &amp; Tech</button>
        <button class="theme-chip" onclick="quickFilterTheme('Theme 2', this)"><i class="fa-solid fa-brain"></i> Theme 2: AI &amp; Interventions</button>
        <button class="theme-chip" onclick="quickFilterTheme('Theme 3', this)"><i class="fa-solid fa-people-roof"></i> Theme 3: Gender &amp; Inclusion</button>
        <button class="theme-chip" onclick="quickFilterTheme('Theme 4', this)"><i class="fa-solid fa-scale-balanced"></i> Theme 4: Policy &amp; Ethics</button>
        <button class="theme-chip" onclick="quickFilterTheme('Theme 5', this)"><i class="fa-solid fa-landmark"></i> Theme 5: Viksit Bharat 2047</button>
      </div>

      <!-- Papers Grid / List Output Container -->
      <div id="papers-list-container" class="papers-container grid-view">
        <!-- Rendered dynamically by JavaScript -->
      </div>

      <!-- No Results State -->
      <div id="no-results-box" style="display: none; text-align: center; padding: 60px 20px; background: #fff; border-radius: var(--radius-lg); border: 2px dashed var(--slate-300); margin-top: 20px;">
        <i class="fa-solid fa-file-circle-question" style="font-size: 3rem; color: var(--slate-400); margin-bottom: 16px;"></i>
        <h3 style="font-family: var(--font-serif); font-size: 1.4rem; color: var(--navy-950);">No matching presentations found</h3>
        <p style="color: var(--slate-600); max-width: 500px; margin: 8px auto 20px auto;">Try broadening your search keywords, clearing selected filters, or searching by author surname.</p>
        <button class="btn-reset-filters" style="padding: 10px 20px;" onclick="resetAllFilters()">Reset All Filters</button>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 2: DAY-WISE SCHEDULE (TIMELINE)        -->
    <!-- ========================================== -->
    <section id="panel-schedule" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Official Conference Schedule</span>
        <h2>Comprehensive Programme Flow</h2>
        <p>Follow the complete sequence of inaugural ceremonies, keynote addresses, plenaries, panel deliberations, parallel technical tracks, and cultural evenings across the 3 days.</p>
        <div class="heading-divider"></div>
      </div>

      <!-- Day Selector Switcher -->
      <div class="days-switcher">
        <button class="day-switch-btn active" onclick="switchScheduleDay('day1', this)">
          <span class="day-title-text">DAY 01</span>
          <span class="day-sub-text">07.10.2026 · Wednesday</span>
        </button>
        <button class="day-switch-btn" onclick="switchScheduleDay('day2', this)">
          <span class="day-title-text">DAY 02</span>
          <span class="day-sub-text">08.10.2026 · Thursday</span>
        </button>
        <button class="day-switch-btn" onclick="switchScheduleDay('day3', this)">
          <span class="day-title-text">DAY 03</span>
          <span class="day-sub-text">09.10.2026 · Friday</span>
        </button>
      </div>

      <!-- Timeline Container -->
      <div id="timeline-events-container" class="timeline-wrapper">
        <!-- Rendered dynamically -->
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 3: 9 TECHNICAL TRACKS MATRIX           -->
    <!-- ========================================== -->
    <section id="panel-tracks" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Parallel Academic Sessions</span>
        <h2>9 Technical Presentation Tracks</h2>
        <p>All paper presentations are structured into 9 parallel sessions held across 3 days at the MBA Auditorium and MBA Lecture Halls.</p>
        <div class="heading-divider"></div>
      </div>

      <div id="tracks-matrix-container" class="tracks-matrix-grid">
        <!-- Rendered dynamically -->
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 4: 5 CONFERENCE THEMES                 -->
    <!-- ========================================== -->
    <section id="panel-themes" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Academic Scope &amp; Focus</span>
        <h2>Conference Themes &amp; Research Clusters</h2>
        <p>Explore the five core thematic tracks framing contemporary digital innovation in social work education, clinical intervention, gender equity, regulatory ethics, and Viksit Bharat 2047.</p>
        <div class="heading-divider"></div>
      </div>

      <div class="themes-grid-5" id="themes-cards-container">
        <!-- Rendered dynamically -->
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 5: DIGNITARIES & LEADERSHIP           -->
    <!-- ========================================== -->
    <section id="panel-dignitaries" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Conference Leadership</span>
        <h2>Patrons, Keynote Speakers &amp; Luminaries</h2>
        <p>Distinguished leadership from Davangere University, Dr. Manmohan Singh Bengaluru City University, NIMHANS, and social enterprise pioneers shaping the national conference.</p>
        <div class="heading-divider"></div>
      </div>

      <div class="dignitaries-grid" id="dignitaries-cards-container">
        <!-- Rendered dynamically -->
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 6: MY PERSONAL ITINERARY               -->
    <!-- ========================================== -->
    <section id="panel-itinerary" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Custom Delegate Schedule</span>
        <h2>My Saved Itinerary</h2>
        <p>Keep track of the presentations, plenaries, and panel discussions you plan to attend. Save your personal schedule for quick access or print it out.</p>
        <div class="heading-divider"></div>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 10px; margin-bottom: 24px;">
        <button class="btn-reset-filters" onclick="window.print()" style="padding: 10px 18px; color: var(--navy-900);">
          <i class="fa-solid fa-print"></i> Print My Schedule
        </button>
        <button class="btn-reset-filters" onclick="clearAllBookmarks()" style="padding: 10px 18px;">
          <i class="fa-regular fa-trash-can"></i> Clear All Bookmarks
        </button>
      </div>

      <div id="itinerary-papers-container" class="papers-container grid-view">
        <!-- Rendered dynamically -->
      </div>

      <div id="empty-itinerary-box" style="display: none; text-align: center; padding: 60px 20px; background: #fff; border-radius: var(--radius-lg); border: 2px dashed var(--slate-300);">
        <i class="fa-regular fa-bookmark" style="font-size: 3rem; color: var(--slate-400); margin-bottom: 16px;"></i>
        <h3 style="font-family: var(--font-serif); font-size: 1.4rem; color: var(--navy-950);">Your itinerary is currently empty</h3>
        <p style="color: var(--slate-600); max-width: 500px; margin: 8px auto 20px auto;">Browse the Presentation Directory and click the bookmark ribbon icon on any paper to add it to your custom itinerary.</p>
        <button class="btn-find-my-paper" onclick="switchMainTab('directory')">Browse Directory Now</button>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 7: VENUE & HELPDESK                    -->
    <!-- ========================================== -->
    <section id="panel-venue" class="tab-content-panel">
      
      <div class="academic-section-heading">
        <span class="subtitle">Campus Navigation &amp; Logistics</span>
        <h2>Venue Guide &amp; Organizing Secretariat</h2>
        <p>All sessions will be held at the Shivagangotri Campus, Davangere University. Meals are arranged at the University Guest House behind the Administrative Block.</p>
        <div class="heading-divider"></div>
      </div>

      <!-- Organizing Committee Helpdesk Cards -->
      <h3 style="font-family: var(--font-serif); font-size: 1.4rem; color: var(--navy-950); margin-bottom: 16px; text-align: center;">Official Conference Committee Helpdesk</h3>
      <div class="helpdesk-cards-grid" id="helpdesk-cards-container">
        <!-- Rendered dynamically -->
      </div>

      <!-- Campus Venue Details Card -->
      <div style="background: #ffffff; border-radius: var(--radius-lg); border: 1px solid var(--slate-200); padding: 32px; box-shadow: var(--shadow-md); margin-top: 30px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
          <div>
            <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--navy-950); margin-bottom: 12px;">
              <i class="fa-solid fa-map-location-dot" style="color: var(--gold-600); margin-right: 8px;"></i> Conference Venues
            </h4>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px; font-size: 0.92rem; color: var(--slate-700);">
              <li><strong>MBA Auditorium:</strong> Main Inaugural Hall, Keynote, Plenary Sessions, Valedictory Ceremony, &amp; Track 1 Presentations.</li>
              <li><strong>MBA Lecture Hall-01:</strong> Track 2 Technical Paper Presentations, Annual General Body Meeting (ISPSW), &amp; Suicide Prevention Workshop.</li>
              <li><strong>MBA Lecture Hall-02:</strong> Track 3 Technical Paper Presentations &amp; Parallel Special Sessions.</li>
              <li><strong>MBA Foyer / Entrance:</strong> Registration Desk &amp; Poster Presentations.</li>
              <li><strong>University Guest House:</strong> Breakfast, Lunch, High Tea &amp; Gala Conference Dinner (Behind Administrative Block).</li>
            </ul>
          </div>

          <div>
            <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--navy-950); margin-bottom: 12px;">
              <i class="fa-solid fa-route" style="color: var(--gold-600); margin-right: 8px;"></i> How to Reach
            </h4>
            <p style="font-size: 0.9rem; color: var(--slate-600); line-height: 1.6; margin-bottom: 12px;">
              Davangere University is situated at <strong>Shivagangotri Campus, Tholahunase</strong>, approximately 10 km from Davanagere Railway Station and Central Bus Stand on the NH 48 highway.
            </p>
            <p style="font-size: 0.9rem; color: var(--slate-600); line-height: 1.6;">
              <strong>Auto-rickshaws &amp; City Buses:</strong> Available continuously from Davanagere Railway Station and Bus Stand to Shivagangotri Campus. University transportation assistance is managed by the Transportation Committee.
            </p>
          </div>
        </div>
      </div>

    </section>

  </main>

  <!-- ========================================== -->
  <!-- MODAL: DETAILED ABSTRACT & PAPER PROFILE   -->
  <!-- ========================================== -->
  <div id="abstract-modal-overlay" class="abstract-modal-overlay" onclick="closeModalOnBackdrop(event)">
    <div class="abstract-modal-card" id="modal-card-element">
      
      <!-- Modal Header Banner -->
      <div class="modal-header-banner">
        <button class="modal-close-btn" onclick="closeAbstractModal()" title="Close (Esc)">
          <i class="fa-solid fa-xmark"></i>
        </button>
        <span class="modal-code-tag" id="modal-paper-code">A1</span>
        <h3 class="modal-title-text" id="modal-paper-title">Paper Title Goes Here</h3>
      </div>

      <!-- Modal Body -->
      <div class="modal-body-content">
        
        <!-- Presentation Schedule Context Box -->
        <div class="modal-schedule-meta-box">
          <div class="slot-detail-item">
            <i class="fa-regular fa-calendar-days"></i>
            <div>
              <div style="font-size: 0.75rem; color: var(--slate-500); text-transform: uppercase;">Scheduled Day</div>
              <strong id="modal-sched-day">Day 01 · 07.10.2026</strong>
            </div>
          </div>
          <div class="slot-detail-item">
            <i class="fa-regular fa-clock"></i>
            <div>
              <div style="font-size: 0.75rem; color: var(--slate-500); text-transform: uppercase;">Time Slot</div>
              <strong id="modal-sched-time">4:45 – 5:30 pm</strong>
            </div>
          </div>
          <div class="slot-detail-item">
            <i class="fa-solid fa-location-dot"></i>
            <div>
              <div style="font-size: 0.75rem; color: var(--slate-500); text-transform: uppercase;">Venue &amp; Track</div>
              <strong id="modal-sched-venue">MBA Auditorium (Track 1)</strong>
            </div>
          </div>
          <div class="slot-detail-item">
            <i class="fa-solid fa-user-graduate"></i>
            <div>
              <div style="font-size: 0.75rem; color: var(--slate-500); text-transform: uppercase;">Session Chairperson</div>
              <strong id="modal-sched-chair">Dr. Bhaskar R.</strong>
            </div>
          </div>
        </div>

        <!-- Authors & Affiliations -->
        <div class="modal-authors-box">
          <div class="modal-authors-title">Contributing Authors &amp; Researchers</div>
          <div class="modal-authors-names" id="modal-authors-names">Author Names</div>
          <div class="modal-affiliation-text" id="modal-authors-affil">Affiliation details...</div>
        </div>

        <!-- Abstract Body -->
        <div class="modal-abstract-section">
          <h4><i class="fa-solid fa-book-open" style="color: var(--gold-600);"></i> Paper Abstract</h4>
          <div class="modal-abstract-body" id="modal-abstract-text">
            Abstract body text goes here...
          </div>
        </div>

        <!-- Keywords Box -->
        <div class="modal-keywords-box" id="modal-keywords-wrapper">
          <div class="modal-authors-title">Keywords / Index Terms</div>
          <div class="keywords-chips-wrap" id="modal-keywords-chips">
            <!-- Keyword pills rendered dynamically -->
          </div>
        </div>

      </div>

      <!-- Modal Footer Toolbar -->
      <div class="modal-footer-toolbar">
        <div style="font-size: 0.85rem; color: var(--slate-500);" id="modal-theme-indicator">
          Theme 1: Innovative Technology for Learning
        </div>
        <div class="modal-actions-btns">
          <button class="btn-modal-action" id="modal-btn-bookmark" onclick="toggleModalBookmark()">
            <i class="fa-regular fa-bookmark"></i> Bookmark Presentation
          </button>
          <button class="btn-modal-action" onclick="copyCitation()">
            <i class="fa-regular fa-copy"></i> Copy Citation
          </button>
          <button class="btn-modal-action primary" onclick="closeAbstractModal()">
            Done
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast-popup" class="toast-popup">
    <i class="fa-solid fa-circle-check"></i>
    <span id="toast-message">Notification message</span>
  </div>

  <!-- International Academic Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        
        <div class="footer-col">
          <h4>ISPSW National Conference 2026</h4>
          <p>
            Jointly organized by the <strong>Department of Studies in Social Work, Davangere University</strong> &amp; the <strong>Indian Society of Professional Social Work (ISPSW)</strong>.
          </p>
          <p>
            Theme: <em>“Innovative Technologies for Social Work Practice, Research and Development”</em>. Fostering multidisciplinary discourse and technology-enabled human welfare aligned with Viksit Bharat 2047.
          </p>
          <p style="font-size: 0.82rem; color: var(--gold-300);">
            <i class="fa-solid fa-calendar-day"></i> 7th – 9th October, 2026 | Shivagangotri Campus, Davangere University
          </p>
        </div>

        <div class="footer-col">
          <h4>Quick Navigation</h4>
          <ul class="footer-links-list">
            <li><a href="javascript:void(0)" onclick="switchMainTab('directory')">Search Presentations &amp; Papers</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('schedule')">Full 3-Day Programme Schedule</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('tracks')">9 Parallel Technical Tracks</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('themes')">Browse by 5 Themes</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('itinerary')">My Saved Itinerary</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('venue')">Helpdesk &amp; Transportation</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Conference Secretariat</h4>
          <p>
            Department of Studies in Social Work<br>
            Shivagangotri Campus, Davangere University<br>
            Tholahunase, Davanagere – 577007<br>
            Karnataka, India
          </p>
          <p>
            <strong>Official Email:</strong><br>
            <a href="mailto:dumswispswnc2026@gmail.com" style="color: var(--gold-300);">dumswispswnc2026@gmail.com</a>
          </p>
          <p>
            <strong>Registration Helpline:</strong><br>
            <span style="color: #fff; font-family: var(--font-mono);">+91 98804 52671</span>
          </p>
        </div>

      </div>

      <div class="bottom-copyright">
        &copy; 2026 Davangere University &amp; Indian Society of Professional Social Work (ISPSW). All rights reserved. Peer-reviewed conference proceedings published for academic reference.
      </div>
    </div>
  </footer>

  <!-- EMBEDDED CONFERENCE DATA -->
  <script>
    const CONF_DB = __CONF_DB_JSON__;
  </script>

  <!-- APPLICATION CONTROLLER SCRIPT -->
  <script>
    // State Management
    let currentTab = 'directory';
    let currentScheduleDay = 'day1';
    let currentViewMode = 'grid'; // 'grid' or 'list'
    let currentQuickTheme = 'all';
    let activeModalPaper = null;
    let bookmarkedCodes = new Set();

    // Initialize from LocalStorage
    try {
      const savedBookmarks = localStorage.getItem('ispsw_bookmarks');
      if (savedBookmarks) {
        bookmarkedCodes = new Set(JSON.parse(savedBookmarks));
      }
    } catch (e) {
      console.warn('LocalStorage access error', e);
    }

    // On Document Loaded
    document.addEventListener('DOMContentLoaded', () => {
      renderPapers();
      renderTimeline('day1');
      renderTracksMatrix();
      renderThemes();
      renderDignitaries();
      renderHelpdesk();
      updateBookmarkCounters();

      // Keyboard shortcut for modal close
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeAbstractModal();
        }
      });
    });

    // Main Tab Switching
    function switchMainTab(tabId) {
      currentTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-content-panel').forEach(panel => panel.classList.remove('active'));
      
      const targetBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (targetBtn) targetBtn.classList.add('active');

      const targetPanel = document.getElementById('panel-' + tabId);
      if (targetPanel) targetPanel.classList.add('active');

      if (tabId === 'itinerary') {
        renderItinerary();
      }

      window.scrollTo({ top: 400, behavior: 'smooth' });
    }

    // Schedule Day Switching
    function switchScheduleDay(dayKey, btnElement) {
      currentScheduleDay = dayKey;
      document.querySelectorAll('.day-switch-btn').forEach(btn => btn.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      renderTimeline(dayKey);
    }

    // View Mode Toggle (Grid vs List)
    function setViewMode(mode) {
      currentViewMode = mode;
      const container = document.getElementById('papers-list-container');
      const btnGrid = document.getElementById('btn-view-grid');
      const btnList = document.getElementById('btn-view-list');

      if (mode === 'grid') {
        container.classList.remove('list-view');
        container.classList.add('grid-view');
        btnGrid.classList.add('active');
        btnList.classList.remove('active');
      } else {
        container.classList.remove('grid-view');
        container.classList.add('list-view');
        btnList.classList.add('active');
        btnGrid.classList.remove('active');
      }
      renderPapers();
    }

    // Quick Theme Chip Filter
    function quickFilterTheme(themeKey, btnElement) {
      currentQuickTheme = themeKey;
      document.querySelectorAll('.theme-quick-chips .theme-chip').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');

      const filterThemeSelect = document.getElementById('filter-theme');
      filterThemeSelect.value = themeKey;
      applyFilters();
    }

    // Debounced Search Input
    let searchDebounceTimer = null;
    function handleSearchInput() {
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(() => {
        applyFilters();
      }, 150);
    }

    // Filter, Search, and Sort Logic
    function getFilteredPapers() {
      const query = (document.getElementById('master-search-input').value || '').trim().toLowerCase();
      const mode = document.getElementById('search-mode-select').value;
      const themeFilter = document.getElementById('filter-theme').value;
      const dayFilter = document.getElementById('filter-day').value;
      const venueFilter = document.getElementById('filter-venue').value;
      const sortOrder = document.getElementById('sort-order').value;

      let results = CONF_DB.papers.filter(p => {
        // Theme Filter
        if (themeFilter !== 'all' && !p.theme.toLowerCase().includes(themeFilter.toLowerCase())) {
          return false;
        }

        // Day Filter
        if (dayFilter !== 'all' && !p.day.includes(dayFilter)) {
          return false;
        }

        // Venue Filter
        if (venueFilter !== 'all' && !p.venue.toLowerCase().includes(venueFilter.toLowerCase())) {
          return false;
        }

        // Text Search
        if (query) {
          if (mode === 'author') {
            return p.authors.toLowerCase().includes(query) || (p.affiliation && p.affiliation.toLowerCase().includes(query));
          } else if (mode === 'title') {
            return p.title.toLowerCase().includes(query);
          } else if (mode === 'code') {
            return p.code.toLowerCase().includes(query);
          } else if (mode === 'keywords') {
            const kwMatch = p.keywords.some(k => k.toLowerCase().includes(query));
            const absMatch = p.abstract.toLowerCase().includes(query);
            return kwMatch || absMatch;
          } else if (mode === 'chair') {
            return (p.chairperson && p.chairperson.toLowerCase().includes(query)) || (p.discussant && p.discussant.toLowerCase().includes(query));
          } else {
            // All Fields
            const inCode = p.code.toLowerCase().includes(query);
            const inTitle = p.title.toLowerCase().includes(query);
            const inAuthors = p.authors.toLowerCase().includes(query);
            const inAffil = p.affiliation && p.affiliation.toLowerCase().includes(query);
            const inVenue = p.venue.toLowerCase().includes(query);
            const inTheme = p.theme.toLowerCase().includes(query);
            const inChair = p.chairperson && p.chairperson.toLowerCase().includes(query);
            const inAbstract = p.abstract && p.abstract.toLowerCase().includes(query);
            const inKeywords = p.keywords.some(k => k.toLowerCase().includes(query));
            return inCode || inTitle || inAuthors || inAffil || inVenue || inTheme || inChair || inAbstract || inKeywords;
          }
        }

        return true;
      });

      // Sorting
      results.sort((a, b) => {
        if (sortOrder === 'code-asc') {
          return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
        } else if (sortOrder === 'code-desc') {
          return b.code.localeCompare(a.code, undefined, { numeric: true, sensitivity: 'base' });
        } else if (sortOrder === 'title-asc') {
          return a.title.localeCompare(b.title);
        } else if (sortOrder === 'author-asc') {
          return a.authors.localeCompare(b.authors);
        } else if (sortOrder === 'theme') {
          return a.theme.localeCompare(b.theme);
        } else {
          // Time / Presentation Order
          // prioritize day, then session_id, then code
          if (a.day !== b.day) return a.day.localeCompare(b.day);
          if (a.session_id !== b.session_id) return a.session_id.localeCompare(b.session_id);
          return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
        }
      });

      return results;
    }

    function applyFilters() {
      renderPapers();
    }

    function resetAllFilters() {
      document.getElementById('master-search-input').value = '';
      document.getElementById('search-mode-select').value = 'all';
      document.getElementById('filter-theme').value = 'all';
      document.getElementById('filter-day').value = 'all';
      document.getElementById('filter-venue').value = 'all';
      document.getElementById('sort-order').value = 'time';
      
      document.querySelectorAll('.theme-quick-chips .theme-chip').forEach(b => b.classList.remove('active'));
      const allBtn = document.querySelector('.theme-quick-chips .theme-chip');
      if (allBtn) allBtn.classList.add('active');

      applyFilters();
      showToast('Filters reset to default view');
    }

    // Render Papers
    function renderPapers() {
      const container = document.getElementById('papers-list-container');
      const noResultsBox = document.getElementById('no-results-box');
      const countLabel = document.getElementById('visible-papers-count');

      const filtered = getFilteredPapers();
      countLabel.textContent = filtered.length;

      if (filtered.length === 0) {
        container.innerHTML = '';
        noResultsBox.style.display = 'block';
        return;
      }

      noResultsBox.style.display = 'none';

      let html = '';
      filtered.forEach(p => {
        const isBookmarked = bookmarkedCodes.has(p.code);
        const bookmarkClass = isBookmarked ? 'bookmarked' : '';
        const bookmarkIcon = isBookmarked ? 'fa-solid fa-bookmark' : 'fa-regular fa-bookmark';
        
        let themeBadge = 'Theme';
        if (p.theme.includes('Theme 1')) themeBadge = 'Theme 1 · Learning & Tech';
        else if (p.theme.includes('Theme 2')) themeBadge = 'Theme 2 · AI & Interventions';
        else if (p.theme.includes('Theme 3')) themeBadge = 'Theme 3 · Gender & Inclusion';
        else if (p.theme.includes('Theme 4')) themeBadge = 'Theme 4 · Policy & Ethics';
        else if (p.theme.includes('Theme 5')) themeBadge = 'Theme 5 · Viksit Bharat';

        if (currentViewMode === 'grid') {
          html += `
            <div class="paper-card" id="paper-card-${p.code}">
              <div>
                <div class="paper-card-top">
                  <span class="paper-code-badge"><i class="fa-solid fa-hashtag"></i> ${p.code}</span>
                  <span class="paper-theme-tag" title="${p.theme}">${themeBadge}</span>
                </div>
                
                <h3 class="paper-title">${p.title}</h3>
                
                <div class="paper-authors">
                  <i class="fa-solid fa-user-pen"></i>
                  <span>${p.authors}</span>
                </div>
                
                ${p.affiliation ? `<div class="paper-affiliation" title="${p.affiliation.replace(/"/g, '&quot;')}">${p.affiliation}</div>` : ''}
                
                <div class="paper-slot-info-box">
                  <div class="slot-detail-item">
                    <i class="fa-regular fa-calendar-check"></i>
                    <span>${p.day} (${p.date})</span>
                  </div>
                  <div class="slot-detail-item">
                    <i class="fa-regular fa-clock"></i>
                    <span><strong>${p.time}</strong></span>
                  </div>
                  <div class="slot-detail-item">
                    <i class="fa-solid fa-location-dot"></i>
                    <span>${p.venue.replace(', Davangere University', '')}</span>
                  </div>
                  <div class="slot-detail-item">
                    <i class="fa-solid fa-user-tie"></i>
                    <span title="Session Chair: ${p.chairperson || 'Scientific Committee'}">Chair: ${p.chairperson ? p.chairperson.split(',')[0] : 'Committee'}</span>
                  </div>
                </div>
              </div>

              <div class="paper-footer-actions">
                <button class="btn-read-abstract" onclick="openAbstractModal('${p.code}')">
                  <i class="fa-regular fa-file-lines"></i> View Abstract &amp; Details
                </button>
                <button class="btn-bookmark-paper ${bookmarkClass}" onclick="toggleBookmark('${p.code}')" title="${isBookmarked ? 'Remove bookmark' : 'Bookmark for My Itinerary'}">
                  <i class="${bookmarkIcon}"></i>
                </button>
              </div>
            </div>
          `;
        } else {
          // List View
          html += `
            <div class="paper-card" id="paper-card-${p.code}">
              <div class="paper-card-inner-flex">
                <div>
                  <span class="paper-code-badge">${p.code}</span>
                </div>
                <div>
                  <h4 style="font-family: var(--font-serif); font-size: 1.15rem; color: var(--navy-950); margin-bottom: 4px;">${p.title}</h4>
                  <div style="font-size: 0.88rem; color: var(--slate-700); font-weight: 600;">
                    <i class="fa-solid fa-user-pen" style="color: var(--maroon-700); margin-right: 4px;"></i> ${p.authors}
                  </div>
                  <div style="font-size: 0.76rem; color: var(--slate-500); margin-top: 2px;">${themeBadge}</div>
                </div>
                <div style="font-size: 0.82rem; color: var(--slate-700); line-height: 1.4;">
                  <div><i class="fa-regular fa-clock" style="color: var(--gold-600); width: 14px;"></i> <strong>${p.time}</strong> (${p.day})</div>
                  <div><i class="fa-solid fa-location-dot" style="color: var(--gold-600); width: 14px;"></i> ${p.venue.replace(', Davangere University', '')}</div>
                </div>
                <div style="display: flex; gap: 8px; justify-content: flex-end;">
                  <button class="btn-read-abstract" onclick="openAbstractModal('${p.code}')">
                    <i class="fa-regular fa-file-lines"></i> Abstract
                  </button>
                  <button class="btn-bookmark-paper ${bookmarkClass}" onclick="toggleBookmark('${p.code}')">
                    <i class="${bookmarkIcon}"></i>
                  </button>
                </div>
              </div>
            </div>
          `;
        }
      });

      container.innerHTML = html;
    }

    // Presenter Quick Pass Fast Finder
    function executeQuickPass() {
      const val = (document.getElementById('quick-pass-input').value || '').trim();
      if (!val) {
        showToast('Please enter an author name or paper code');
        return;
      }
      document.getElementById('master-search-input').value = val;
      applyFilters();
      
      const firstCard = document.querySelector('.paper-card');
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstCard.style.outline = '3px solid var(--gold-400)';
        setTimeout(() => { firstCard.style.outline = 'none'; }, 2500);
        showToast(`Found presentations matching "${val}"`);
      } else {
        showToast(`No presentations found for "${val}"`);
      }
    }

    // Render Timeline View for Days
    function renderTimeline(dayKey) {
      const container = document.getElementById('timeline-events-container');
      const dayData = CONF_DB.programme_schedule[dayKey];
      if (!dayData) return;

      let html = `
        <div style="text-align: center; margin-bottom: 24px;">
          <h3 style="font-family: var(--font-serif); font-size: 1.7rem; color: var(--navy-950);">${dayData.title}</h3>
          <p style="color: var(--gold-600); font-weight: 600; font-family: var(--font-mono);">${dayData.date} · ${dayData.day}</p>
        </div>
      `;

      dayData.events.forEach(ev => {
        let catClass = 'general';
        let badgeClass = 'cat-ceremonial';
        const evCat = ev.category.toLowerCase();
        
        if (evCat.includes('ceremonial')) { catClass = 'ceremonial'; badgeClass = 'cat-ceremonial'; }
        else if (evCat.includes('plenary')) { catClass = 'plenary'; badgeClass = 'cat-plenary'; }
        else if (evCat.includes('panel')) { catClass = 'panel'; badgeClass = 'cat-panel'; }
        else if (evCat.includes('technical')) { catClass = 'technical'; badgeClass = 'cat-technical'; }
        else if (evCat.includes('special')) { catClass = 'special'; badgeClass = 'cat-special'; }
        else if (evCat.includes('cultural')) { catClass = 'cultural'; badgeClass = 'cat-cultural'; }
        else if (evCat.includes('meals') || evCat.includes('networking')) { catClass = 'meals'; badgeClass = 'cat-meals'; }

        html += `
          <div class="timeline-event-card ${catClass}">
            <div class="event-time-col">
              <span class="event-time-badge"><i class="fa-regular fa-clock"></i> ${ev.time}</span>
              <span class="event-cat-badge ${badgeClass}">${ev.category}</span>
            </div>
            <div class="event-details-col">
              <h4>${ev.event}</h4>
              ${ev.details ? `<p class="event-desc-text">${ev.details}</p>` : ''}
              ${ev.venue ? `<div class="event-venue-text"><i class="fa-solid fa-location-dot"></i> <strong>Venue:</strong> ${ev.venue}</div>` : ''}
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Render 9 Tracks Matrix
    function renderTracksMatrix() {
      const container = document.getElementById('tracks-matrix-container');
      let html = '';

      CONF_DB.technical_sessions.forEach(ts => {
        html += `
          <div class="track-session-box">
            <div class="track-header-row">
              <span class="track-num-pill">Session ${ts.session_num} · Track ${ts.track_num}</span>
              <span style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: 600; color: var(--gold-600);">${ts.day} (${ts.date})</span>
            </div>
            
            <h3>${ts.session_title}</h3>
            
            <ul class="track-meta-list">
              <li><i class="fa-regular fa-clock"></i> <strong>Time:</strong> ${ts.time}</li>
              <li><i class="fa-solid fa-location-dot"></i> <strong>Venue:</strong> ${ts.venue}</li>
              <li><i class="fa-solid fa-user-graduate"></i> <strong>Chairperson:</strong> ${ts.chairperson}</li>
              ${ts.discussant ? `<li><i class="fa-solid fa-comments"></i> <strong>Discussant:</strong> ${ts.discussant}</li>` : ''}
              ${ts.rapporteurs ? `<li><i class="fa-solid fa-clipboard-user"></i> <strong>Rapporteurs:</strong> ${ts.rapporteurs}</li>` : ''}
              <li><i class="fa-solid fa-file-lines"></i> <strong>Scheduled Papers:</strong> ${ts.papers.length} Contributions</li>
            </ul>

            <button class="btn-view-track-papers" onclick="filterByTrackSession('${ts.day}', '${ts.venue}')">
              <i class="fa-solid fa-arrow-right"></i> View Track Presentations
            </button>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function filterByTrackSession(day, venue) {
      switchMainTab('directory');
      document.getElementById('filter-day').value = day;
      if (venue.includes('Auditorium')) {
        document.getElementById('filter-venue').value = 'MBA Auditorium';
      } else if (venue.includes('01')) {
        document.getElementById('filter-venue').value = 'MBA Lecture Hall-01';
      } else if (venue.includes('02')) {
        document.getElementById('filter-venue').value = 'MBA Lecture Hall-02';
      }
      applyFilters();
      showToast(`Showing presentations for ${day} at ${venue}`);
    }

    // Render Themes Cards
    function renderThemes() {
      const container = document.getElementById('themes-cards-container');
      let html = '';

      CONF_DB.themes.forEach(th => {
        const paperCount = CONF_DB.papers.filter(p => p.theme.includes(th.key)).length;
        html += `
          <div class="theme-card-rich">
            <div>
              <div class="theme-icon-wrap" style="background: ${th.color}18; color: ${th.color};">
                <i class="fa-solid ${th.icon}"></i>
              </div>
              <span style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: 700; color: ${th.color}; text-transform: uppercase;">${th.id}</span>
              <h3>${th.title}</h3>
              <p>${th.desc}</p>
            </div>
            
            <div style="border-top: 1px solid var(--slate-100); padding-top: 16px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 0.85rem; font-weight: 600; color: var(--slate-600);">${paperCount} Accepted Papers</span>
              <button class="btn-read-abstract" onclick="filterBySpecificTheme('${th.key}')" style="border-color: ${th.color}; color: ${th.color};">
                Explore Papers <i class="fa-solid fa-arrow-right"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function filterBySpecificTheme(themeKey) {
      switchMainTab('directory');
      document.getElementById('filter-theme').value = themeKey;
      applyFilters();
      showToast(`Filtered by ${themeKey}`);
    }

    // Render Dignitaries
    function renderDignitaries() {
      const container = document.getElementById('dignitaries-cards-container');
      let html = '';

      CONF_DB.dignitaries.forEach(d => {
        html += `
          <div class="dignitary-card">
            <div class="dignitary-avatar-wrap">
              <i class="fa-solid fa-user-tie"></i>
            </div>
            <div class="dignitary-info">
              <span class="dignitary-role-badge">${d.tag}</span>
              <h4>${d.name}</h4>
              <div style="font-size: 0.88rem; font-weight: 600; color: var(--navy-900);">${d.title}</div>
              <div class="dignitary-org">${d.org}</div>
              <div style="font-size: 0.8rem; color: var(--gold-600); font-weight: 600; margin-top: 4px;">
                <i class="fa-regular fa-star"></i> ${d.role}
              </div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Render Helpdesk Contacts
    function renderHelpdesk() {
      const container = document.getElementById('helpdesk-cards-container');
      let html = '';

      CONF_DB.committee_contacts.forEach(c => {
        html += `
          <div class="helpdesk-card">
            <i class="fa-solid fa-phone-volume"></i>
            <h4>${c.role}</h4>
            <div class="contact-name">${c.name}</div>
            <div style="font-size: 0.78rem; color: var(--slate-500); margin-bottom: 8px;">${c.desig}</div>
            <a href="tel:${c.phone.replace(/\\s+/g, '')}"><i class="fa-solid fa-phone"></i> ${c.phone}</a>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Abstract Modal Controller
    function openAbstractModal(code) {
      const paper = CONF_DB.papers.find(p => p.code === code);
      if (!paper) return;

      activeModalPaper = paper;

      document.getElementById('modal-paper-code').textContent = paper.code;
      document.getElementById('modal-paper-title').textContent = paper.title;
      document.getElementById('modal-sched-day').textContent = `${paper.day} (${paper.date})`;
      document.getElementById('modal-sched-time').textContent = paper.time;
      document.getElementById('modal-sched-venue').textContent = `${paper.venue} (${paper.session_title})`;
      document.getElementById('modal-sched-chair').textContent = paper.chairperson ? paper.chairperson.split(',')[0] : 'Scientific Committee';
      
      document.getElementById('modal-authors-names').textContent = paper.authors;
      document.getElementById('modal-authors-affil').textContent = paper.affiliation || 'Department of Studies in Social Work, Research Scholars & Faculty';
      
      const abstractText = paper.abstract || 'The detailed text for this paper was accepted and published in the ISPSW 2026 Abstract Volume. Please refer to the session proceedings during the presentation.';
      document.getElementById('modal-abstract-text').textContent = abstractText;
      
      // Keywords
      const kwBox = document.getElementById('modal-keywords-wrapper');
      const kwChips = document.getElementById('modal-keywords-chips');
      if (paper.keywords && paper.keywords.length > 0) {
        kwBox.style.display = 'block';
        kwChips.innerHTML = paper.keywords.map(k => `<span class="kw-pill">${k}</span>`).join('');
      } else {
        kwBox.style.display = 'none';
      }

      document.getElementById('modal-theme-indicator').textContent = paper.theme;

      // Update Bookmark button in modal
      updateModalBookmarkButton();

      const overlay = document.getElementById('abstract-modal-overlay');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeAbstractModal() {
      const overlay = document.getElementById('abstract-modal-overlay');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      activeModalPaper = null;
    }

    function closeModalOnBackdrop(e) {
      if (e.target.id === 'abstract-modal-overlay') {
        closeAbstractModal();
      }
    }

    // Bookmark & Itinerary Management
    function toggleBookmark(code) {
      if (bookmarkedCodes.has(code)) {
        bookmarkedCodes.delete(code);
        showToast(`Removed [${code}] from your itinerary`);
      } else {
        bookmarkedCodes.add(code);
        showToast(`Added [${code}] to your personal itinerary!`);
      }

      saveBookmarks();
      renderPapers();
      updateBookmarkCounters();
      if (currentTab === 'itinerary') renderItinerary();
    }

    function toggleModalBookmark() {
      if (!activeModalPaper) return;
      toggleBookmark(activeModalPaper.code);
      updateModalBookmarkButton();
    }

    function updateModalBookmarkButton() {
      if (!activeModalPaper) return;
      const btn = document.getElementById('modal-btn-bookmark');
      const isBookmarked = bookmarkedCodes.has(activeModalPaper.code);
      if (isBookmarked) {
        btn.innerHTML = '<i class="fa-solid fa-bookmark" style="color: var(--gold-500);"></i> Bookmarked in Itinerary';
        btn.classList.add('primary');
      } else {
        btn.innerHTML = '<i class="fa-regular fa-bookmark"></i> Bookmark Presentation';
        btn.classList.remove('primary');
      }
    }

    function saveBookmarks() {
      try {
        localStorage.setItem('ispsw_bookmarks', JSON.stringify(Array.from(bookmarkedCodes)));
      } catch (e) {
        console.warn('LocalStorage error', e);
      }
    }

    function updateBookmarkCounters() {
      const badge = document.getElementById('badge-bookmark-count');
      const count = bookmarkedCodes.size;
      if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'inline-block';
      } else {
        badge.style.display = 'none';
      }
    }

    function clearAllBookmarks() {
      if (confirm('Clear all saved presentations from your personal itinerary?')) {
        bookmarkedCodes.clear();
        saveBookmarks();
        updateBookmarkCounters();
        renderItinerary();
        renderPapers();
        showToast('Itinerary cleared');
      }
    }

    function renderItinerary() {
      const container = document.getElementById('itinerary-papers-container');
      const emptyBox = document.getElementById('empty-itinerary-box');

      if (bookmarkedCodes.size === 0) {
        container.innerHTML = '';
        emptyBox.style.display = 'block';
        return;
      }

      emptyBox.style.display = 'none';
      const bookmarkedPapers = CONF_DB.papers.filter(p => bookmarkedCodes.has(p.code));

      let html = '';
      bookmarkedPapers.forEach(p => {
        html += `
          <div class="paper-card">
            <div>
              <div class="paper-card-top">
                <span class="paper-code-badge"><i class="fa-solid fa-bookmark"></i> ${p.code}</span>
                <span class="paper-theme-tag">${p.day}</span>
              </div>
              <h3 class="paper-title">${p.title}</h3>
              <div class="paper-authors"><i class="fa-solid fa-user-pen"></i> ${p.authors}</div>
              <div class="paper-slot-info-box">
                <div class="slot-detail-item"><i class="fa-regular fa-clock"></i> <strong>${p.time}</strong></div>
                <div class="slot-detail-item"><i class="fa-solid fa-location-dot"></i> ${p.venue}</div>
              </div>
            </div>
            <div class="paper-footer-actions">
              <button class="btn-read-abstract" onclick="openAbstractModal('${p.code}')">
                <i class="fa-regular fa-file-lines"></i> View Details
              </button>
              <button class="btn-bookmark-paper bookmarked" onclick="toggleBookmark('${p.code}')" title="Remove">
                <i class="fa-solid fa-bookmark"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function copyCitation() {
      if (!activeModalPaper) return;
      const text = `${activeModalPaper.authors} (2026). "${activeModalPaper.title}". Annual National Conference of the Indian Society of Professional Social Work (ISPSW), Davangere University, Karnataka. Abstract Code: ${activeModalPaper.code}.`;
      navigator.clipboard.writeText(text).then(() => {
        showToast('Citation copied to clipboard!');
      }).catch(() => {
        showToast('Citation text ready');
      });
    }

    // Toast Popup
    function showToast(msg) {
      const toast = document.getElementById('toast-popup');
      const label = document.getElementById('toast-message');
      label.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3000);
    }
  </script>

</body>
</html>
'''

# Build Logo HTMLs
davangere_logo_html = f'<img src="{db["conference_meta"]["davangere_logo"]}" alt="Davangere University">' if db["conference_meta"]["davangere_logo"] else '<i class="fa-solid fa-building-columns logo-fallback"></i>'
ispsw_logo_html = f'<img src="{db["conference_meta"]["ispsw_logo"]}" alt="ISPSW Logo">' if db["conference_meta"]["ispsw_logo"] else '<i class="fa-solid fa-shield-halved logo-fallback"></i>'

final_html = html_template.replace('__DAVANGERE_LOGO_HTML__', davangere_logo_html)
final_html = final_html.replace('__ISPSW_LOGO_HTML__', ispsw_logo_html)
final_html = final_html.replace('__CONF_DB_JSON__', json_data_str)

output_path = "index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {output_path} successfully ({len(final_html)} bytes)!")

# Also write to conference_portal.html as a duplicate convenience file
with open("conference_portal.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated conference_portal.html as well!")
