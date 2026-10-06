import json
import os

print("Generating Dynamic Corporate Blue & White Conference Portal...")

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

json_data_str = json.dumps(db, ensure_ascii=False)

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>ISPSW 2026 | Annual National Conference | Davangere University</title>
  <meta name="description" content="Official Corporate Portal for the Annual National Conference of ISPSW 2026 on Innovative Technologies for Social Work Practice, Research and Development. Search presentations, view schedules, and read abstracts.">
  <meta name="theme-color" content="#0f2b5c">

  <!-- Elite Corporate Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

  <style>
    /* ========================================================= */
    /* DYNAMIC CORPORATE BLUE & WHITE COLOR SYSTEM & DESIGN TOKENS */
    /* ========================================================= */
    :root {
      /* Corporate Blue Palette */
      --blue-950: #091936;
      --blue-900: #0f2b5c;
      --blue-850: #143775;
      --blue-800: #1a448e;
      --blue-700: #1d4ed8;
      --blue-600: #2563eb;
      --blue-500: #3b82f6;
      --blue-400: #60a5fa;
      --blue-300: #93c5fd;
      --blue-200: #bfdbfe;
      --blue-100: #dbeafe;
      --blue-50:  #eff6ff;
      --blue-25:  #f5f9ff;
      
      /* Vibrant Electric Cyan Accents */
      --cyan-600: #0284c7;
      --cyan-500: #0ea5e9;
      --cyan-400: #38bdf8;
      --cyan-100: #e0f2fe;

      /* Crisp Neutral & White Scales */
      --white: #ffffff;
      --slate-50:  #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1e293b;
      --slate-900: #0f172a;

      /* Corporate Alert / Success / Warm Tokens */
      --teal-600: #0d9488;
      --emerald-600: #059669;
      --emerald-50: #ecfdf5;
      --amber-600: #d97706;
      --amber-50: #fffbeb;
      --indigo-600: #4f46e5;

      /* Typography */
      --font-brand: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', SFMono-Regular, monospace;

      /* Modern Corporate Elevations & Shadows */
      --shadow-subtle: 0 1px 3px 0 rgba(15, 43, 92, 0.06);
      --shadow-card: 0 4px 20px -2px rgba(15, 43, 92, 0.08);
      --shadow-hover: 0 14px 34px -4px rgba(29, 78, 216, 0.16);
      --shadow-glow: 0 0 25px rgba(37, 99, 235, 0.25);
      --shadow-modal: 0 25px 60px -15px rgba(9, 25, 54, 0.35);

      /* Radii */
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 26px;
      --radius-full: 9999px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--blue-25);
      color: var(--slate-800);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      padding-bottom: 70px; /* Space for mobile bottom bar */
    }

    @media (min-width: 769px) {
      body {
        padding-bottom: 0;
      }
    }

    /* Container */
    .container {
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 16px;
    }

    @media (min-width: 768px) {
      .container {
        padding: 0 28px;
      }
    }

    /* ========================================================= */
    /* TOP CORPORATE ANNOUNCEMENT STRIPE */
    /* ========================================================= */
    .corporate-top-bar {
      background: linear-gradient(90deg, var(--blue-950) 0%, var(--blue-900) 60%, var(--blue-850) 100%);
      color: var(--white);
      font-size: 0.8rem;
      padding: 9px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }

    .corporate-top-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .live-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(37, 99, 235, 0.3);
      border: 1px solid var(--cyan-400);
      color: var(--white);
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-weight: 600;
      font-size: 0.72rem;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }

    .live-dot {
      width: 8px;
      height: 8px;
      background-color: #22c55e;
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
      animation: pulseGreen 2s infinite;
    }

    @keyframes pulseGreen {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
      70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
    }

    .top-email-link {
      color: var(--cyan-400);
      text-decoration: none;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: color 0.2s;
    }

    .top-email-link:hover {
      color: var(--white);
    }

    /* ========================================================= */
    /* DYNAMIC CORPORATE HERO HEADER */
    /* ========================================================= */
    .corporate-header {
      background: linear-gradient(135deg, var(--blue-950) 0%, var(--blue-900) 50%, #0c2d64 100%);
      color: var(--white);
      padding: 32px 0 28px 0;
      position: relative;
      border-bottom: 3px solid var(--blue-600);
      box-shadow: 0 10px 30px rgba(9, 25, 54, 0.15);
      overflow: hidden;
    }

    /* Subtle geometric mesh background */
    .corporate-header::before {
      content: "";
      position: absolute;
      top: -50%; right: -20%;
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(37, 99, 235, 0.2) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .corporate-header::after {
      content: "";
      position: absolute;
      bottom: -40%; left: -10%;
      width: 500px; height: 500px;
      background: radial-gradient(circle, rgba(14, 165, 233, 0.15) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .header-branding-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      position: relative;
      z-index: 2;
    }

    .logo-badge {
      width: 72px;
      height: 72px;
      background: var(--white);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25), 0 0 0 2px rgba(255, 255, 255, 0.8);
      flex-shrink: 0;
      transition: transform 0.25s ease;
    }

    @media (min-width: 768px) {
      .logo-badge {
        width: 88px;
        height: 88px;
        padding: 8px;
        border-radius: var(--radius-lg);
      }
    }

    .logo-badge:hover {
      transform: scale(1.04);
    }

    .logo-badge img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }

    .header-titles-box {
      text-align: center;
      flex: 1;
      padding: 0 6px;
    }

    .org-main-name {
      font-family: var(--font-brand);
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--white);
      line-height: 1.2;
      margin-bottom: 3px;
    }

    @media (min-width: 768px) {
      .org-main-name {
        font-size: 1.85rem;
        letter-spacing: 1.5px;
      }
    }

    .dept-subtitle {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--cyan-400);
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 3px;
    }

    @media (min-width: 768px) {
      .dept-subtitle {
        font-size: 0.95rem;
      }
    }

    .joint-separator {
      font-size: 0.82rem;
      color: var(--blue-200);
      font-weight: 500;
      margin: 2px 0;
    }

    .society-name {
      font-family: var(--font-brand);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--white);
      line-height: 1.25;
    }

    @media (min-width: 768px) {
      .society-name {
        font-size: 1.4rem;
      }
    }

    .society-acronym-badge {
      background: var(--blue-600);
      color: var(--white);
      padding: 1px 7px;
      border-radius: 4px;
      font-size: 0.85em;
      margin-left: 4px;
      display: inline-block;
    }

    /* Hero Theme Card */
    .hero-conference-card {
      margin-top: 26px;
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.16);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-radius: var(--radius-lg);
      padding: 22px 20px;
      text-align: center;
      position: relative;
      z-index: 2;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.18);
    }

    @media (min-width: 768px) {
      .hero-conference-card {
        padding: 32px 36px;
        margin-top: 32px;
      }
    }

    .conf-edition-label {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--cyan-400);
      margin-bottom: 8px;
    }

    .conf-theme-display {
      font-family: var(--font-brand);
      font-size: 1.45rem;
      font-weight: 800;
      line-height: 1.3;
      color: var(--white);
      margin-bottom: 14px;
      max-width: 1050px;
      margin-left: auto;
      margin-right: auto;
    }

    @media (min-width: 768px) {
      .conf-theme-display {
        font-size: 2.25rem;
      }
    }

    .hero-pills-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .hero-meta-pill {
      background: rgba(9, 25, 54, 0.65);
      border: 1px solid rgba(96, 165, 250, 0.35);
      padding: 7px 14px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--blue-100);
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }

    .hero-meta-pill i {
      color: var(--cyan-400);
    }

    /* Fast Action Bar in Hero */
    .hero-fast-action {
      margin-top: 18px;
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .btn-hero-primary {
      background: linear-gradient(135deg, var(--blue-600) 0%, var(--blue-700) 100%);
      color: var(--white);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 11px 22px;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    }

    .btn-hero-primary:hover, .btn-hero-primary:active {
      background: linear-gradient(135deg, var(--cyan-600) 0%, var(--blue-600) 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6);
    }

    .btn-hero-secondary {
      background: rgba(255, 255, 255, 0.12);
      color: var(--white);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 11px 20px;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
    }

    .btn-hero-secondary:hover {
      background: rgba(255, 255, 255, 0.22);
    }

    /* ========================================================= */
    /* KEY STATS BAR */
    /* ========================================================= */
    .corporate-stats-strip {
      background: var(--white);
      border-bottom: 1px solid var(--slate-200);
      padding: 14px 0;
      box-shadow: var(--shadow-subtle);
    }

    .stats-scroll-container {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      text-align: center;
    }

    @media (min-width: 640px) {
      .stats-scroll-container {
        grid-template-columns: repeat(6, 1fr);
      }
    }

    .stat-metric-card {
      padding: 6px 8px;
      border-right: 1px solid var(--slate-200);
    }

    .stat-metric-card:last-child {
      border-right: none;
    }

    @media (max-width: 639px) {
      .stat-metric-card:nth-child(3) {
        border-right: none;
      }
    }

    .stat-huge-number {
      font-family: var(--font-brand);
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--blue-700);
      line-height: 1;
      margin-bottom: 3px;
    }

    .stat-micro-title {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--slate-600);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* ========================================================= */
    /* STICKY CORPORATE TAB NAVIGATION (TOUCH & DESKTOP) */
    /* ========================================================= */
    .sticky-nav-shell {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--white);
      border-bottom: 2px solid var(--slate-200);
      box-shadow: 0 4px 15px rgba(15, 43, 92, 0.05);
    }

    .nav-horizontal-scroller {
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      padding: 8px 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .nav-horizontal-scroller::-webkit-scrollbar {
      display: none;
    }

    .corp-nav-tab {
      background: none;
      border: 1px solid transparent;
      padding: 9px 16px;
      border-radius: var(--radius-md);
      font-family: var(--font-body);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--slate-600);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      white-space: nowrap;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }

    .corp-nav-tab i {
      font-size: 0.95rem;
      color: var(--slate-400);
      transition: color 0.2s;
    }

    .corp-nav-tab:hover {
      background: var(--blue-50);
      color: var(--blue-700);
    }

    .corp-nav-tab:hover i {
      color: var(--blue-600);
    }

    .corp-nav-tab.active {
      background: linear-gradient(135deg, var(--blue-700) 0%, var(--blue-600) 100%);
      color: var(--white);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }

    .corp-nav-tab.active i {
      color: var(--white);
    }

    .tab-counter-badge {
      background: var(--slate-200);
      color: var(--slate-700);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-full);
      margin-left: 2px;
    }

    .corp-nav-tab.active .tab-counter-badge {
      background: var(--white);
      color: var(--blue-700);
    }

    /* ========================================================= */
    /* DYNAMIC SEARCH & FILTER CONTROL CENTRE */
    /* ========================================================= */
    .search-cockpit-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid var(--blue-100);
      box-shadow: var(--shadow-card);
      padding: 18px;
      margin-top: 24px;
      margin-bottom: 24px;
      position: relative;
    }

    @media (min-width: 768px) {
      .search-cockpit-card {
        padding: 26px;
      }
    }

    .search-input-wrapper {
      display: flex;
      align-items: center;
      position: relative;
      width: 100%;
    }

    .search-icon-fixed {
      position: absolute;
      left: 16px;
      font-size: 1.15rem;
      color: var(--blue-600);
      pointer-events: none;
    }

    .corp-search-input {
      width: 100%;
      padding: 15px 44px 15px 48px;
      font-family: var(--font-body);
      font-size: 1rem;
      border: 2px solid var(--blue-200);
      border-radius: var(--radius-md);
      background: var(--white);
      color: var(--slate-900);
      transition: all 0.25s ease;
      box-shadow: inset 0 2px 4px rgba(15, 43, 92, 0.03);
    }

    .corp-search-input:focus {
      outline: none;
      border-color: var(--blue-600);
      box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
    }

    .clear-search-btn {
      position: absolute;
      right: 14px;
      background: none;
      border: none;
      color: var(--slate-400);
      font-size: 1.1rem;
      cursor: pointer;
      padding: 6px;
      display: none;
      transition: color 0.2s;
    }

    .clear-search-btn:hover {
      color: var(--slate-700);
    }

    /* Mobile Filters Collapsible Header */
    .filter-toggle-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid var(--slate-200);
    }

    .btn-toggle-filters {
      background: var(--blue-50);
      border: 1px solid var(--blue-200);
      color: var(--blue-700);
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s;
    }

    .btn-toggle-filters:hover {
      background: var(--blue-100);
    }

    /* Filters Tray (Collapsible on Mobile, always open on desktop) */
    .filters-tray-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
      margin-top: 14px;
    }

    @media (min-width: 600px) {
      .filters-tray-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 992px) {
      .filters-tray-grid {
        grid-template-columns: repeat(5, 1fr);
      }
    }

    .filter-field-cell {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    .filter-field-label {
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--slate-600);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .filter-field-label i {
      color: var(--blue-600);
    }

    .corp-select {
      width: 100%;
      padding: 10px 12px;
      font-family: var(--font-body);
      font-size: 0.88rem;
      font-weight: 500;
      border: 1px solid var(--slate-300);
      border-radius: var(--radius-sm);
      background: var(--white);
      color: var(--slate-800);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .corp-select:focus {
      outline: none;
      border-color: var(--blue-600);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }

    /* Active Summary & View Control Bar */
    .search-summary-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px dashed var(--slate-200);
    }

    .summary-counter-text {
      font-size: 0.9rem;
      color: var(--slate-700);
      font-weight: 600;
    }

    .summary-counter-text strong {
      color: var(--blue-700);
      font-family: var(--font-mono);
      font-size: 1.05rem;
    }

    .view-mode-buttons {
      display: inline-flex;
      border: 1px solid var(--slate-300);
      border-radius: var(--radius-sm);
      overflow: hidden;
      background: var(--white);
    }

    .btn-view-toggle {
      background: none;
      border: none;
      padding: 7px 12px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--slate-600);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-view-toggle.active {
      background: var(--blue-700);
      color: var(--white);
    }

    .btn-clear-all-filters {
      background: none;
      border: 1px solid var(--slate-300);
      color: var(--slate-700);
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }

    .btn-clear-all-filters:hover {
      background: #fee2e2;
      border-color: #ef4444;
      color: #b91c1c;
    }

    /* Quick Theme Filters Horizon */
    .quick-theme-chips-row {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 4px 0 16px 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .quick-theme-chips-row::-webkit-scrollbar {
      display: none;
    }

    .theme-chip-btn {
      background: var(--white);
      border: 1px solid var(--slate-300);
      padding: 7px 14px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--slate-700);
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-subtle);
      flex-shrink: 0;
    }

    .theme-chip-btn:hover {
      border-color: var(--blue-500);
      color: var(--blue-700);
    }

    .theme-chip-btn.active {
      background: var(--blue-700);
      border-color: var(--blue-700);
      color: var(--white);
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.25);
    }

    /* ========================================================= */
    /* PAPERS DISPLAY (RESPONSIVE CARDS & LIST) */
    /* ========================================================= */
    .papers-grid-layout {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    @media (min-width: 680px) {
      .papers-grid-layout {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1100px) {
      .papers-grid-layout {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .papers-list-layout {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* Individual Corporate Paper Card */
    .corp-paper-card {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .corp-paper-card:hover {
      border-color: var(--blue-400);
      transform: translateY(-3px);
      box-shadow: var(--shadow-hover);
    }

    .card-top-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
      margin-bottom: 12px;
    }

    .code-badge-corp {
      background: var(--blue-50);
      color: var(--blue-700);
      border: 1px solid var(--blue-200);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .theme-pill-corp {
      background: var(--slate-100);
      color: var(--slate-700);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      max-width: 180px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .paper-headline {
      font-family: var(--font-brand);
      font-size: 1.12rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--blue-950);
      margin-bottom: 10px;
    }

    .authors-line-corp {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--slate-800);
      display: flex;
      align-items: flex-start;
      gap: 7px;
      margin-bottom: 6px;
    }

    .authors-line-corp i {
      color: var(--blue-600);
      margin-top: 4px;
      font-size: 0.85rem;
    }

    .affil-snippet {
      font-size: 0.78rem;
      color: var(--slate-500);
      margin-bottom: 14px;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* Slot Schedule Info Block */
    .schedule-info-block {
      background: var(--blue-25);
      border: 1px solid var(--blue-100);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      margin-bottom: 16px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      font-size: 0.78rem;
    }

    .sched-item {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--slate-700);
    }

    .sched-item i {
      color: var(--blue-600);
      width: 14px;
    }

    .sched-item strong {
      color: var(--blue-950);
    }

    /* Actions Footer in Card */
    .card-actions-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid var(--slate-100);
    }

    .btn-view-abstract {
      background: var(--white);
      border: 1px solid var(--blue-600);
      color: var(--blue-700);
      font-size: 0.84rem;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s;
    }

    .btn-view-abstract:hover, .btn-view-abstract:active {
      background: var(--blue-700);
      color: var(--white);
    }

    .btn-star-bookmark {
      background: var(--white);
      border: 1px solid var(--slate-300);
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--slate-400);
      font-size: 1rem;
      transition: all 0.2s;
    }

    .btn-star-bookmark:hover {
      border-color: var(--blue-600);
      color: var(--blue-600);
    }

    .btn-star-bookmark.active {
      background: var(--blue-50);
      border-color: var(--blue-600);
      color: var(--blue-600);
    }

    /* List View Tweaks */
    .papers-list-layout .corp-paper-card {
      padding: 14px 18px;
    }

    .list-card-inner {
      display: grid;
      grid-template-columns: 80px 1fr 240px 130px;
      align-items: center;
      gap: 16px;
    }

    @media (max-width: 900px) {
      .list-card-inner {
        grid-template-columns: 1fr;
        gap: 10px;
      }
    }

    /* ========================================================= */
    /* FULL PROGRAMME TIMELINE (DAYS 1, 2, 3) */
    /* ========================================================= */
    .day-selector-pills {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 28px;
      flex-wrap: wrap;
    }

    .day-pill-btn {
      background: var(--white);
      border: 2px solid var(--blue-200);
      border-radius: var(--radius-md);
      padding: 12px 24px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 170px;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-subtle);
    }

    .day-pill-btn:hover {
      border-color: var(--blue-600);
    }

    .day-pill-btn.active {
      background: linear-gradient(135deg, var(--blue-850) 0%, var(--blue-700) 100%);
      border-color: var(--blue-700);
      color: var(--white);
      box-shadow: 0 6px 18px rgba(29, 78, 216, 0.25);
    }

    .day-pill-title {
      font-family: var(--font-brand);
      font-size: 1.15rem;
      font-weight: 800;
    }

    .day-pill-date {
      font-size: 0.78rem;
      color: var(--slate-500);
    }

    .day-pill-btn.active .day-pill-date {
      color: var(--blue-200);
    }

    /* Timeline Cards */
    .timeline-stream {
      max-width: 980px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .timeline-corp-card {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 18px 22px;
      display: grid;
      grid-template-columns: 160px 1fr;
      gap: 18px;
      position: relative;
      border-left: 5px solid var(--blue-600);
      transition: all 0.2s;
    }

    @media (max-width: 650px) {
      .timeline-corp-card {
        grid-template-columns: 1fr;
        gap: 10px;
        padding: 16px;
      }
    }

    .timeline-corp-card:hover {
      border-color: var(--blue-400);
      box-shadow: var(--shadow-hover);
    }

    .timeline-corp-card.ceremonial { border-left-color: var(--blue-600); }
    .timeline-corp-card.plenary { border-left-color: #0284c7; }
    .timeline-corp-card.panel { border-left-color: #4f46e5; }
    .timeline-corp-card.technical { border-left-color: #059669; }
    .timeline-corp-card.special { border-left-color: #7c3aed; }
    .timeline-corp-card.cultural { border-left-color: #e11d48; }
    .timeline-corp-card.meals { border-left-color: var(--slate-400); background: var(--slate-50); }

    .tl-time-box {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 6px;
    }

    .tl-time-badge {
      font-family: var(--font-mono);
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--blue-900);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .tl-category-tag {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 7px;
      border-radius: 4px;
      width: fit-content;
      background: var(--blue-50);
      color: var(--blue-700);
    }

    .tl-content-box h4 {
      font-family: var(--font-brand);
      font-size: 1.15rem;
      color: var(--blue-950);
      margin-bottom: 5px;
    }

    .tl-desc-p {
      color: var(--slate-700);
      font-size: 0.9rem;
      margin-bottom: 8px;
      line-height: 1.5;
    }

    .tl-venue-label {
      font-size: 0.8rem;
      color: var(--slate-500);
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
    }

    .tl-venue-label i {
      color: var(--blue-600);
    }

    /* ========================================================= */
    /* 9 TECHNICAL TRACKS MATRIX */
    /* ========================================================= */
    .tracks-grid-3x3 {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    @media (min-width: 680px) {
      .tracks-grid-3x3 {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1080px) {
      .tracks-grid-3x3 {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .track-grid-card {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }

    .track-grid-card:hover {
      border-color: var(--blue-400);
      box-shadow: var(--shadow-hover);
      transform: translateY(-2px);
    }

    .track-pill-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--slate-100);
    }

    .track-pill-badge {
      background: var(--blue-700);
      color: var(--white);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      letter-spacing: 0.5px;
    }

    .track-grid-card h3 {
      font-family: var(--font-brand);
      font-size: 1.25rem;
      color: var(--blue-950);
      margin-bottom: 8px;
    }

    .track-details-list {
      list-style: none;
      font-size: 0.85rem;
      color: var(--slate-700);
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .track-details-list li {
      display: flex;
      align-items: flex-start;
      gap: 7px;
    }

    .track-details-list i {
      color: var(--blue-600);
      margin-top: 3px;
      width: 14px;
    }

    .btn-track-action {
      width: 100%;
      background: var(--blue-50);
      border: 1px solid var(--blue-200);
      color: var(--blue-700);
      font-weight: 700;
      font-size: 0.86rem;
      padding: 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      transition: all 0.2s;
    }

    .btn-track-action:hover {
      background: var(--blue-700);
      color: var(--white);
    }

    /* ========================================================= */
    /* 5 THEMES SECTION */
    /* ========================================================= */
    .themes-cards-shelf {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    @media (min-width: 600px) {
      .themes-cards-shelf {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1100px) {
      .themes-cards-shelf {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .theme-detail-card {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }

    .theme-detail-card:hover {
      border-color: var(--blue-400);
      box-shadow: var(--shadow-hover);
      transform: translateY(-3px);
    }

    .theme-icon-orb {
      width: 48px;
      height: 48px;
      border-radius: var(--radius-md);
      background: var(--blue-50);
      color: var(--blue-600);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      margin-bottom: 14px;
    }

    .theme-detail-card h3 {
      font-family: var(--font-brand);
      font-size: 1.2rem;
      color: var(--blue-950);
      margin-bottom: 10px;
      line-height: 1.35;
    }

    .theme-detail-card p {
      color: var(--slate-600);
      font-size: 0.88rem;
      line-height: 1.5;
      margin-bottom: 18px;
    }

    /* ========================================================= */
    /* DIGNITARIES & LEADERSHIP */
    /* ========================================================= */
    .dignitaries-shelf {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    @media (min-width: 680px) {
      .dignitaries-shelf {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1100px) {
      .dignitaries-shelf {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .dignitary-box-corp {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 20px;
      display: flex;
      gap: 16px;
      align-items: center;
      transition: all 0.2s ease;
    }

    .dignitary-box-corp:hover {
      border-color: var(--blue-400);
      box-shadow: var(--shadow-hover);
    }

    .dignitary-avatar-corp {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: var(--blue-50);
      border: 2px solid var(--blue-300);
      color: var(--blue-700);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      flex-shrink: 0;
    }

    .dignitary-text-corp h4 {
      font-family: var(--font-brand);
      font-size: 1.1rem;
      color: var(--blue-950);
      margin-bottom: 2px;
    }

    .dignitary-tag-pill {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--blue-600);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 3px;
      display: inline-block;
    }

    .dignitary-role-desc {
      font-size: 0.8rem;
      color: var(--slate-600);
      line-height: 1.35;
    }

    /* ========================================================= */
    /* HELPDESK & VENUE GUIDE */
    /* ========================================================= */
    .helpdesk-cards-shelf {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
      margin-bottom: 24px;
    }

    @media (min-width: 600px) {
      .helpdesk-cards-shelf {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1000px) {
      .helpdesk-cards-shelf {
        grid-template-columns: repeat(5, 1fr);
      }
    }

    .helpdesk-unit-card {
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      padding: 18px 14px;
      box-shadow: var(--shadow-subtle);
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .helpdesk-unit-card i {
      font-size: 1.5rem;
      color: var(--blue-600);
      margin-bottom: 8px;
    }

    .helpdesk-unit-card h4 {
      font-family: var(--font-brand);
      font-size: 0.95rem;
      color: var(--blue-950);
      margin-bottom: 3px;
    }

    .helpdesk-unit-card .name-text {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--slate-800);
      margin-bottom: 6px;
    }

    .helpdesk-phone-anchor {
      color: var(--blue-700);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--blue-50);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      margin-top: 8px;
      transition: background 0.2s;
    }

    .helpdesk-phone-anchor:hover {
      background: var(--blue-100);
    }

    /* ========================================================= */
    /* MODAL: FULL ABSTRACT & RESEARCH PROFILE */
    /* ========================================================= */
    .corp-modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(9, 25, 54, 0.75);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 14px;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .corp-modal-overlay.active {
      display: flex;
      opacity: 1;
    }

    .corp-modal-window {
      background: var(--white);
      border-radius: var(--radius-lg);
      max-width: 880px;
      width: 100%;
      max-height: 92vh;
      overflow-y: auto;
      box-shadow: var(--shadow-modal);
      border: 1px solid var(--blue-200);
      display: flex;
      flex-direction: column;
      animation: modalSlide 0.25s ease-out;
    }

    @keyframes modalSlide {
      from { transform: translateY(20px) scale(0.98); opacity: 0; }
      to { transform: translateY(0) scale(1); opacity: 1; }
    }

    .modal-corp-head {
      background: linear-gradient(135deg, var(--blue-950) 0%, var(--blue-900) 100%);
      color: var(--white);
      padding: 22px 24px;
      position: relative;
      border-bottom: 3px solid var(--blue-600);
    }

    .btn-modal-dismiss {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.15);
      border: none;
      color: var(--white);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-modal-dismiss:hover {
      background: var(--blue-600);
      transform: rotate(90deg);
    }

    .modal-code-chip {
      background: rgba(59, 130, 246, 0.3);
      border: 1px solid var(--cyan-400);
      color: var(--white);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      display: inline-block;
      margin-bottom: 8px;
    }

    .modal-paper-heading {
      font-family: var(--font-brand);
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.35;
      color: var(--white);
      padding-right: 36px;
    }

    .modal-body-scrollable {
      padding: 24px;
      overflow-y: auto;
      flex: 1;
    }

    .modal-meta-grid {
      background: var(--blue-25);
      border: 1px solid var(--blue-100);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      margin-bottom: 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      gap: 12px;
      font-size: 0.85rem;
    }

    .modal-authors-section {
      margin-bottom: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--slate-200);
    }

    .modal-section-micro {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--blue-700);
      margin-bottom: 4px;
    }

    .modal-author-names-bold {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--blue-950);
      margin-bottom: 4px;
    }

    .modal-affil-text {
      font-size: 0.85rem;
      color: var(--slate-600);
      line-height: 1.5;
      white-space: pre-line;
    }

    .modal-abstract-block h4 {
      font-family: var(--font-brand);
      font-size: 1.15rem;
      color: var(--blue-950);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 7px;
    }

    .modal-abstract-text {
      font-size: 0.94rem;
      line-height: 1.7;
      color: var(--slate-800);
      text-align: justify;
      white-space: pre-line;
    }

    .modal-keywords-container {
      margin-top: 20px;
      padding-top: 16px;
      border-top: 1px dashed var(--slate-200);
    }

    .keywords-badge-shelf {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      margin-top: 8px;
    }

    .kw-chip-corp {
      background: var(--blue-50);
      color: var(--blue-800);
      font-size: 0.78rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      border: 1px solid var(--blue-200);
    }

    .modal-actions-footer {
      padding: 16px 24px;
      background: var(--slate-50);
      border-top: 1px solid var(--slate-200);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .btn-corp-modal-action {
      background: var(--white);
      border: 1px solid var(--slate-300);
      color: var(--slate-800);
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-corp-modal-action:hover {
      background: var(--blue-50);
      border-color: var(--blue-600);
      color: var(--blue-700);
    }

    .btn-corp-modal-action.primary {
      background: var(--blue-700);
      border-color: var(--blue-700);
      color: var(--white);
    }

    .btn-corp-modal-action.primary:hover {
      background: var(--blue-800);
    }

    /* ========================================================= */
    /* MOBILE BOTTOM APP NAVIGATION BAR (FOR SMARTPHONES) */
    /* ========================================================= */
    .mobile-bottom-app-bar {
      display: flex;
      position: fixed;
      bottom: 0; left: 0; right: 0;
      background: var(--white);
      border-top: 1px solid var(--slate-200);
      box-shadow: 0 -4px 20px rgba(15, 43, 92, 0.1);
      z-index: 1000;
      height: 60px;
      justify-content: space-around;
      align-items: center;
      padding: 0 4px;
    }

    @media (min-width: 769px) {
      .mobile-bottom-app-bar {
        display: none !important;
      }
    }

    .mobile-nav-item {
      background: none;
      border: none;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: var(--slate-500);
      font-size: 0.7rem;
      font-weight: 600;
      cursor: pointer;
      flex: 1;
      height: 100%;
      transition: color 0.2s;
      position: relative;
    }

    .mobile-nav-item i {
      font-size: 1.15rem;
      margin-bottom: 2px;
    }

    .mobile-nav-item.active {
      color: var(--blue-700);
      font-weight: 700;
    }

    .mobile-nav-item.active i {
      color: var(--blue-700);
    }

    .mobile-badge-dot {
      position: absolute;
      top: 6px;
      right: 25%;
      background: var(--blue-600);
      color: var(--white);
      font-size: 0.65rem;
      padding: 1px 5px;
      border-radius: 999px;
      font-weight: 800;
    }

    /* ========================================================= */
    /* TOAST NOTIFICATION */
    /* ========================================================= */
    .corp-toast {
      position: fixed;
      bottom: 74px;
      right: 20px;
      background: var(--blue-900);
      color: var(--white);
      border-left: 4px solid var(--cyan-400);
      border-radius: var(--radius-sm);
      padding: 12px 18px;
      box-shadow: var(--shadow-modal);
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1100;
      transform: translateY(80px);
      opacity: 0;
      transition: all 0.25s ease;
      font-size: 0.88rem;
      font-weight: 500;
      max-width: 90%;
    }

    @media (min-width: 769px) {
      .corp-toast {
        bottom: 24px;
      }
    }

    .corp-toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    .corp-toast i {
      color: var(--cyan-400);
      font-size: 1.1rem;
    }

    /* Section Panels */
    .tab-section-panel {
      display: none;
      padding: 24px 0 40px 0;
    }

    .tab-section-panel.active {
      display: block;
      animation: fadeInFast 0.25s ease;
    }

    @keyframes fadeInFast {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .section-intro-header {
      text-align: center;
      margin-bottom: 24px;
    }

    .section-intro-header .sub-kicker {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--blue-600);
      margin-bottom: 4px;
      display: inline-block;
    }

    .section-intro-header h2 {
      font-family: var(--font-brand);
      font-size: 1.8rem;
      color: var(--blue-950);
      font-weight: 800;
      line-height: 1.25;
    }

    .section-intro-header p {
      font-size: 0.95rem;
      color: var(--slate-600);
      max-width: 700px;
      margin: 6px auto 0 auto;
    }

    /* Corporate Footer */
    .corporate-footer {
      background: var(--blue-950);
      color: var(--slate-400);
      padding: 48px 0 28px 0;
      border-top: 3px solid var(--blue-600);
      font-size: 0.88rem;
    }

    .footer-columns-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
      margin-bottom: 32px;
    }

    @media (min-width: 768px) {
      .footer-columns-grid {
        grid-template-columns: 2fr 1fr 1fr;
      }
    }

    .footer-col-corp h4 {
      font-family: var(--font-brand);
      font-size: 1.1rem;
      color: var(--white);
      margin-bottom: 14px;
      position: relative;
      padding-bottom: 6px;
    }

    .footer-col-corp h4::after {
      content: "";
      position: absolute;
      bottom: 0; left: 0;
      width: 32px; height: 2px;
      background: var(--cyan-400);
    }

    .footer-col-corp p {
      line-height: 1.6;
      margin-bottom: 10px;
    }

    .footer-col-corp a {
      color: var(--cyan-400);
      text-decoration: none;
    }

    .footer-col-corp a:hover {
      text-decoration: underline;
    }

    .footer-links-col {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .footer-links-col a {
      color: var(--slate-300);
      transition: color 0.2s;
    }

    .footer-links-col a:hover {
      color: var(--cyan-400);
    }

    .sub-footer-copyright {
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      text-align: center;
      font-size: 0.78rem;
      color: var(--slate-500);
    }

    /* Print Optimizations */
    @media print {
      .corporate-top-bar, .sticky-nav-shell, .search-cockpit-card,
      .quick-theme-chips-row, .btn-hero-primary, .btn-hero-secondary,
      .card-actions-bar, .mobile-bottom-app-bar, .corporate-footer,
      .filter-toggle-header {
        display: none !important;
      }

      body {
        background: #fff !important;
        color: #000 !important;
        padding-bottom: 0 !important;
      }

      .corporate-header {
        background: #fff !important;
        color: #000 !important;
        border-bottom: 2px solid #000 !important;
      }

      .org-main-name, .society-name, .conf-theme-display {
        color: #000 !important;
      }

      .corp-paper-card {
        page-break-inside: avoid;
        box-shadow: none !important;
        border: 1px solid #999 !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Announcement Stripe -->
  <div class="corporate-top-bar">
    <div class="container">
      <div class="corporate-top-inner">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span class="live-badge"><span class="live-dot"></span> Live Conference Portal</span>
          <span>Shivagangotri Campus, Davangere University · Karnataka, India</span>
        </div>
        <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
          <span>7th – 9th OCTOBER, 2026</span>
          <span style="opacity: 0.35;">|</span>
          <span style="color: var(--cyan-400); font-weight: 600;"><i class="fa-solid fa-code"></i> Designed &amp; Architected by Dr. Saravana Kadirvel</span>
          <span style="opacity: 0.35;">|</span>
          <a href="mailto:dumswispswnc2026@gmail.com" class="top-email-link">
            <i class="fa-regular fa-envelope"></i> dumswispswnc2026@gmail.com
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Dynamic Corporate Header -->
  <header class="corporate-header">
    <div class="container">
      
      <!-- Brand & Logos Row -->
      <div class="header-branding-row">
        <!-- University Emblem -->
        <div class="logo-badge" title="Davangere University Emblem">
          __DAVANGERE_LOGO_HTML__
        </div>

        <!-- Centre Typography -->
        <div class="header-titles-box">
          <h1 class="org-main-name">DAVANGERE UNIVERSITY</h1>
          <div class="dept-subtitle">Department of Studies in Social Work</div>
          <div class="joint-separator">&amp;</div>
          <div class="society-name">INDIAN SOCIETY OF PROFESSIONAL SOCIAL WORK <span class="society-acronym-badge">ISPSW</span></div>
        </div>

        <!-- ISPSW Emblem -->
        <div class="logo-badge" title="ISPSW Logo">
          __ISPSW_LOGO_HTML__
        </div>
      </div>

      <!-- Hero Focal Theme Banner -->
      <div class="hero-conference-card">
        <div class="conf-edition-label">Annual National Conference of ISPSW – 2026</div>
        <h2 class="conf-theme-display">“Innovative Technologies for Social Work Practice, Research and Development”</h2>
        
        <div class="hero-pills-row">
          <span class="hero-meta-pill"><i class="fa-regular fa-calendar-days"></i> 7th – 9th October, 2026</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-location-dot"></i> MBA Auditorium &amp; Academic Complex</span>
          <span class="hero-meta-pill"><i class="fa-solid fa-graduation-cap"></i> 115 Accepted Papers &amp; Abstracts</span>
        </div>

        <div style="margin-top: 14px; display: flex; justify-content: center;">
          <span style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(56, 189, 248, 0.3); padding: 5px 16px; border-radius: 999px; font-size: 0.82rem; color: #e0f2fe; font-weight: 600; display: inline-flex; align-items: center; gap: 7px; backdrop-filter: blur(8px);">
            <i class="fa-solid fa-compass-drafting" style="color: var(--cyan-400);"></i> Digital Portal Designed &amp; Architected by <strong style="color: #fff;">Dr. Saravana Kadirvel</strong>
          </span>
        </div>

        <div class="hero-fast-action">
          <button class="btn-hero-primary" onclick="focusQuickSearch()">
            <i class="fa-solid fa-magnifying-glass"></i> Find My Presentation
          </button>
          <button class="btn-hero-secondary" onclick="switchMainTab('schedule')">
            <i class="fa-regular fa-calendar-check"></i> View 3-Day Schedule
          </button>
        </div>
      </div>

    </div>
  </header>

  <!-- Key Conference Metrics Ribbon -->
  <section class="corporate-stats-strip">
    <div class="container">
      <div class="stats-scroll-container">
        <div class="stat-metric-card">
          <div class="stat-huge-number" id="metric-papers">115</div>
          <div class="stat-micro-title">Accepted Papers</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-huge-number">3</div>
          <div class="stat-micro-title">Days</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-huge-number">9</div>
          <div class="stat-micro-title">Parallel Tracks</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-huge-number">4</div>
          <div class="stat-micro-title">Plenary Sessions</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-huge-number">3</div>
          <div class="stat-micro-title">Panel Debates</div>
        </div>
        <div class="stat-metric-card">
          <div class="stat-huge-number">5</div>
          <div class="stat-micro-title">Core Themes</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Sticky Nav Tabs -->
  <nav class="sticky-nav-shell" id="sticky-navbar">
    <div class="container">
      <div class="nav-horizontal-scroller">
        <button class="corp-nav-tab active" data-tab="directory" onclick="switchMainTab('directory')">
          <i class="fa-solid fa-magnifying-glass"></i> Search Directory
          <span class="tab-counter-badge" id="counter-directory">115</span>
        </button>
        <button class="corp-nav-tab" data-tab="schedule" onclick="switchMainTab('schedule')">
          <i class="fa-regular fa-calendar-check"></i> 3-Day Schedule
        </button>
        <button class="corp-nav-tab" data-tab="tracks" onclick="switchMainTab('tracks')">
          <i class="fa-solid fa-network-wired"></i> 9 Tracks Matrix
        </button>
        <button class="corp-nav-tab" data-tab="themes" onclick="switchMainTab('themes')">
          <i class="fa-solid fa-layer-group"></i> 5 Themes
        </button>
        <button class="corp-nav-tab" data-tab="dignitaries" onclick="switchMainTab('dignitaries')">
          <i class="fa-solid fa-user-tie"></i> Dignitaries
        </button>
        <button class="corp-nav-tab" data-tab="itinerary" onclick="switchMainTab('itinerary')">
          <i class="fa-regular fa-bookmark"></i> My Itinerary
          <span class="tab-counter-badge" id="counter-itinerary" style="display:none;">0</span>
        </button>
        <button class="corp-nav-tab" data-tab="venue" onclick="switchMainTab('venue')">
          <i class="fa-solid fa-compass"></i> Venue &amp; Helpdesk
        </button>
      </div>
    </div>
  </nav>

  <!-- Main View Container -->
  <main class="container">

    <!-- ========================================================= -->
    <!-- TAB 1: PRESENTATION SEARCH DIRECTORY -->
    <!-- ========================================================= -->
    <section id="tab-directory" class="tab-section-panel active">
      
      <!-- Search & Filters Cockpit Card -->
      <div class="search-cockpit-card">
        
        <!-- Search Input Bar -->
        <div class="search-input-wrapper">
          <i class="fa-solid fa-magnifying-glass search-icon-fixed"></i>
          <input type="text" id="master-search-input" class="corp-search-input" placeholder="Search presenter name, paper title, code (A1..J24), time, or keywords..." oninput="handleSearchInputChange()">
          <button class="clear-search-btn" id="btn-clear-search" onclick="clearSearchInput()" title="Clear search">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Filter Toggle (for mobile) -->
        <div class="filter-toggle-header">
          <button class="btn-toggle-filters" id="btn-toggle-filters" onclick="toggleFiltersPanel()">
            <i class="fa-solid fa-sliders"></i> <span id="toggle-filter-label">Filter &amp; Sort Options</span>
          </button>
          <button class="btn-clear-all-filters" onclick="resetAllFilters()">
            <i class="fa-solid fa-rotate-left"></i> Reset
          </button>
        </div>

        <!-- Filters Tray Grid (Collapsible on mobile) -->
        <div class="filters-tray-grid" id="filters-tray-grid">
          
          <!-- Filter Search Scope -->
          <div class="filter-field-cell">
            <label class="filter-field-label"><i class="fa-solid fa-crosshairs"></i> Search Field</label>
            <select id="filter-scope" class="corp-select" onchange="runFilters()">
              <option value="all">All Fields</option>
              <option value="author">Author / Presenter Name</option>
              <option value="title">Paper Title Only</option>
              <option value="code">Paper Code (A1, B4...)</option>
              <option value="keywords">Keywords &amp; Abstract</option>
              <option value="chair">Session Chairperson</option>
            </select>
          </div>

          <!-- Filter Theme -->
          <div class="filter-field-cell">
            <label class="filter-field-label"><i class="fa-solid fa-layer-group"></i> Conference Theme</label>
            <select id="filter-theme" class="corp-select" onchange="runFilters()">
              <option value="all">All 5 Themes</option>
              <option value="Theme 1">Theme 1: Learning &amp; Tech</option>
              <option value="Theme 2">Theme 2: AI &amp; Interventions</option>
              <option value="Theme 3">Theme 3: Gender Equity &amp; Inclusion</option>
              <option value="Theme 4">Theme 4: Policy &amp; Ethics</option>
              <option value="Theme 5">Theme 5: Viksit Bharat 2047</option>
            </select>
          </div>

          <!-- Filter Day -->
          <div class="filter-field-cell">
            <label class="filter-field-label"><i class="fa-regular fa-calendar"></i> Presentation Day</label>
            <select id="filter-day" class="corp-select" onchange="runFilters()">
              <option value="all">All 3 Days</option>
              <option value="Day 01">Day 01 (07.10.2026, Wed)</option>
              <option value="Day 02">Day 02 (08.10.2026, Thu)</option>
              <option value="Day 03">Day 03 (09.10.2026, Fri)</option>
            </select>
          </div>

          <!-- Filter Venue -->
          <div class="filter-field-cell">
            <label class="filter-field-label"><i class="fa-solid fa-location-dot"></i> Venue / Hall</label>
            <select id="filter-venue" class="corp-select" onchange="runFilters()">
              <option value="all">All Halls</option>
              <option value="MBA Auditorium">MBA Auditorium</option>
              <option value="MBA Lecture Hall-01">MBA Lecture Hall-01</option>
              <option value="MBA Lecture Hall-02">MBA Lecture Hall-02</option>
            </select>
          </div>

          <!-- Sort Order -->
          <div class="filter-field-cell">
            <label class="filter-field-label"><i class="fa-solid fa-arrow-down-short-wide"></i> Sort Order</label>
            <select id="filter-sort" class="corp-select" onchange="runFilters()">
              <option value="time">Chronological Time</option>
              <option value="code-asc">Paper Code (A → Z)</option>
              <option value="code-desc">Paper Code (Z → A)</option>
              <option value="title-asc">Paper Title (A → Z)</option>
              <option value="author-asc">Author Name (A → Z)</option>
              <option value="theme">By Theme</option>
            </select>
          </div>

        </div>

        <!-- Summary & Views Row -->
        <div class="search-summary-bar">
          <div class="summary-counter-text">
            Displaying <strong id="papers-visible-count">115</strong> of 115 presentations
          </div>

          <div class="view-mode-buttons">
            <button class="btn-view-toggle active" id="btn-grid-view" onclick="changeViewMode('grid')">
              <i class="fa-solid fa-grip"></i> Cards
            </button>
            <button class="btn-view-toggle" id="btn-list-view" onclick="changeViewMode('list')">
              <i class="fa-solid fa-list"></i> List
            </button>
          </div>
        </div>

      </div>

      <!-- Quick Theme Filter Chips -->
      <div class="quick-theme-chips-row">
        <button class="theme-chip-btn active" onclick="setQuickTheme('all', this)">
          <i class="fa-solid fa-border-all"></i> All Presentations
        </button>
        <button class="theme-chip-btn" onclick="setQuickTheme('Theme 1', this)">
          <i class="fa-solid fa-graduation-cap"></i> Theme 1: Learning &amp; Tech
        </button>
        <button class="theme-chip-btn" onclick="setQuickTheme('Theme 2', this)">
          <i class="fa-solid fa-brain"></i> Theme 2: AI &amp; Interventions
        </button>
        <button class="theme-chip-btn" onclick="setQuickTheme('Theme 3', this)">
          <i class="fa-solid fa-people-roof"></i> Theme 3: Gender &amp; Inclusion
        </button>
        <button class="theme-chip-btn" onclick="setQuickTheme('Theme 4', this)">
          <i class="fa-solid fa-scale-balanced"></i> Theme 4: Policy &amp; Ethics
        </button>
        <button class="theme-chip-btn" onclick="setQuickTheme('Theme 5', this)">
          <i class="fa-solid fa-landmark"></i> Theme 5: Viksit Bharat 2047
        </button>
      </div>

      <!-- Papers Container -->
      <div id="papers-display-container" class="papers-grid-layout">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Empty State -->
      <div id="empty-state-box" style="display: none; text-align: center; padding: 50px 20px; background: #fff; border-radius: var(--radius-lg); border: 2px dashed var(--slate-300); margin-top: 20px;">
        <i class="fa-solid fa-file-circle-question" style="font-size: 3rem; color: var(--blue-400); margin-bottom: 14px;"></i>
        <h3 style="font-family: var(--font-brand); font-size: 1.35rem; color: var(--blue-950);">No matching presentations found</h3>
        <p style="color: var(--slate-600); max-width: 480px; margin: 6px auto 16px auto;">Try adjusting your search terms or reset the filters to see all accepted papers.</p>
        <button class="btn-corp-modal-action primary" onclick="resetAllFilters()">Reset All Filters</button>
      </div>

    </section>

    <!-- ========================================================= -->
    <!-- TAB 2: DAY-WISE SCHEDULE (TIMELINE) -->
    <!-- ========================================================= -->
    <section id="tab-schedule" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Conference Programme Flow</span>
        <h2>3-Day Comprehensive Time-Table</h2>
        <p>Complete schedule of the inauguration, keynote addresses, plenary sessions, panel discussions, technical paper presentations, workshops, cultural evenings, and meals.</p>
      </div>

      <div class="day-selector-pills">
        <button class="day-pill-btn active" onclick="setTimelineDay('day1', this)">
          <span class="day-pill-title">DAY 01</span>
          <span class="day-pill-date">07.10.2026 · Wednesday</span>
        </button>
        <button class="day-pill-btn" onclick="setTimelineDay('day2', this)">
          <span class="day-pill-title">DAY 02</span>
          <span class="day-pill-date">08.10.2026 · Thursday</span>
        </button>
        <button class="day-pill-btn" onclick="setTimelineDay('day3', this)">
          <span class="day-pill-title">DAY 03</span>
          <span class="day-pill-date">09.10.2026 · Friday</span>
        </button>
      </div>

      <div class="timeline-stream" id="timeline-stream-container">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TAB 3: 9 TECHNICAL TRACKS MATRIX -->
    <!-- ========================================================= -->
    <section id="tab-tracks" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Parallel Academic Tracks</span>
        <h2>9 Technical Presentation Sessions</h2>
        <p>Explore the track structure, assigned halls, session chairpersons, discussants, and scheduled presentations at a glance.</p>
      </div>

      <div class="tracks-grid-3x3" id="tracks-matrix-container">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TAB 4: 5 CONFERENCE THEMES -->
    <!-- ========================================================= -->
    <section id="tab-themes" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Academic Scope</span>
        <h2>5 Core Thematic Domains</h2>
        <p>Multidisciplinary research clusters addressing technology adoption, AI, gender inclusion, ethics, and social development in India.</p>
      </div>

      <div class="themes-cards-shelf" id="themes-shelf-container">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TAB 5: DIGNITARIES -->
    <!-- ========================================================= -->
    <section id="tab-dignitaries" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Distinguished Leadership</span>
        <h2>Patrons &amp; Keynote Speakers</h2>
        <p>Eminent vice-chancellors, social entrepreneurs, psychiatric social work scholars, and national leaders presiding over the conference.</p>
      </div>

      <div class="dignitaries-shelf" id="dignitaries-shelf-container">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TAB 6: MY PERSONAL ITINERARY -->
    <!-- ========================================================= */
    <section id="tab-itinerary" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Custom Delegate Schedule</span>
        <h2>My Saved Itinerary</h2>
        <p>Bookmarked presentations and sessions saved for quick access on your device. Ready for print or offline reference.</p>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 10px; margin-bottom: 20px;">
        <button class="btn-corp-modal-action" onclick="window.print()">
          <i class="fa-solid fa-print"></i> Print My Schedule
        </button>
        <button class="btn-corp-modal-action" onclick="clearAllSavedBookmarks()">
          <i class="fa-regular fa-trash-can"></i> Clear All
        </button>
      </div>

      <div class="papers-grid-layout" id="itinerary-display-container">
        <!-- Rendered by JavaScript -->
      </div>

      <div id="itinerary-empty-box" style="display: none; text-align: center; padding: 50px 20px; background: #fff; border-radius: var(--radius-lg); border: 2px dashed var(--slate-300);">
        <i class="fa-regular fa-bookmark" style="font-size: 3rem; color: var(--blue-300); margin-bottom: 14px;"></i>
        <h3 style="font-family: var(--font-brand); font-size: 1.35rem; color: var(--blue-950);">Your itinerary is currently empty</h3>
        <p style="color: var(--slate-600); max-width: 480px; margin: 6px auto 16px auto;">Click the bookmark icon on any presentation in the directory to pin it to your personal schedule.</p>
        <button class="btn-corp-modal-action primary" onclick="switchMainTab('directory')">Browse Papers Directory</button>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TAB 7: VENUE & HELPDESK -->
    <!-- ========================================================= -->
    <section id="tab-venue" class="tab-section-panel">
      <div class="section-intro-header">
        <span class="sub-kicker">Logistics &amp; Assistance</span>
        <h2>Venue Guide &amp; Secretariat Helpline</h2>
        <p>Official contact personnel for registration, accommodations, transportation, food, cultural activities, and campus navigation.</p>
      </div>

      <div class="helpdesk-cards-shelf" id="helpdesk-shelf-container">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Campus Directions Card -->
      <div style="background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--slate-200); padding: 26px; box-shadow: var(--shadow-card); margin-top: 20px;">
        <h3 style="font-family: var(--font-brand); font-size: 1.3rem; color: var(--blue-950); margin-bottom: 14px;">
          <i class="fa-solid fa-map-location-dot" style="color: var(--blue-600); margin-right: 8px;"></i> Conference Locations &amp; Transportation
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; font-size: 0.9rem; color: var(--slate-700);">
          <div>
            <strong style="color: var(--blue-900);">Main Venues:</strong>
            <ul style="margin-top: 6px; padding-left: 18px; line-height: 1.6;">
              <li><strong>MBA Auditorium:</strong> Inauguration, Keynote, Plenary Sessions, Track 1 &amp; Valedictory.</li>
              <li><strong>MBA Lecture Hall-01:</strong> Track 2 Paper Presentations, Suicide Prevention Workshop &amp; ISPSW AGM.</li>
              <li><strong>MBA Lecture Hall-02:</strong> Track 3 Paper Presentations.</li>
              <li><strong>MBA Foyer:</strong> Registration Desk &amp; Poster Presentations.</li>
              <li><strong>University Guest House:</strong> Breakfast, Lunch, &amp; Dinner (Behind Administrative Block).</li>
            </ul>
          </div>
          <div>
            <strong style="color: var(--blue-900);">Transit &amp; Accessibility:</strong>
            <p style="margin-top: 6px; line-height: 1.6;">
              Davangere University is situated at <strong>Shivagangotri Campus, Tholahunase</strong>, 10 km from Davanagere Railway Station and Central Bus Stand on NH 48. Continuous auto-rickshaws and KSRTC city buses connect to the campus. For local pickup assistance, contact the Transportation Committee.
            </p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ========================================================= -->
  <!-- MODAL: FULL ABSTRACT & RESEARCH PROFILE -->
  <!-- ========================================================= -->
  <div id="corp-abstract-modal" class="corp-modal-overlay" onclick="handleModalBackdropClick(event)">
    <div class="corp-modal-window" id="corp-modal-inner">
      
      <div class="modal-corp-head">
        <button class="btn-modal-dismiss" onclick="closeAbstractModal()" title="Close (Esc)">
          <i class="fa-solid fa-xmark"></i>
        </button>
        <span class="modal-code-chip" id="modal-code-display">A1</span>
        <h3 class="modal-paper-heading" id="modal-title-display">Paper Title</h3>
      </div>

      <div class="modal-body-scrollable">
        
        <!-- Presentation Schedule Box -->
        <div class="modal-meta-grid">
          <div>
            <div style="font-size: 0.72rem; color: var(--slate-500); text-transform: uppercase;">Scheduled Day</div>
            <strong style="color: var(--blue-950);" id="modal-day-display">Day 01 (07.10.2026)</strong>
          </div>
          <div>
            <div style="font-size: 0.72rem; color: var(--slate-500); text-transform: uppercase;">Time Slot</div>
            <strong style="color: var(--blue-950);" id="modal-time-display">4:45 – 5:30 pm</strong>
          </div>
          <div>
            <div style="font-size: 0.72rem; color: var(--slate-500); text-transform: uppercase;">Venue &amp; Track</div>
            <strong style="color: var(--blue-950);" id="modal-venue-display">MBA Auditorium</strong>
          </div>
          <div>
            <div style="font-size: 0.72rem; color: var(--slate-500); text-transform: uppercase;">Session Chair</div>
            <strong style="color: var(--blue-950);" id="modal-chair-display">Chairperson Name</strong>
          </div>
        </div>

        <!-- Authors & Affiliations -->
        <div class="modal-authors-section">
          <div class="modal-section-micro">Authors &amp; Presenters</div>
          <div class="modal-author-names-bold" id="modal-authors-display">Author Names</div>
          <div class="modal-affil-text" id="modal-affil-display">Affiliation text</div>
        </div>

        <!-- Abstract Text -->
        <div class="modal-abstract-block">
          <h4><i class="fa-regular fa-file-lines" style="color: var(--blue-600);"></i> Paper Abstract</h4>
          <div class="modal-abstract-text" id="modal-abstract-body">
            Full abstract text...
          </div>
        </div>

        <!-- Keywords -->
        <div class="modal-keywords-container" id="modal-keywords-box">
          <div class="modal-section-micro">Keywords</div>
          <div class="keywords-badge-shelf" id="modal-keywords-shelf">
            <!-- Pill tags rendered dynamically -->
          </div>
        </div>

      </div>

      <div class="modal-actions-footer">
        <div style="font-size: 0.82rem; color: var(--slate-500);" id="modal-theme-indicator">
          Theme Indicator
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn-corp-modal-action" id="modal-bookmark-btn" onclick="toggleModalBookmark()">
            <i class="fa-regular fa-bookmark"></i> Bookmark
          </button>
          <button class="btn-corp-modal-action" onclick="copyCitationFromModal()">
            <i class="fa-regular fa-copy"></i> Copy Citation
          </button>
          <button class="btn-corp-modal-action primary" onclick="closeAbstractModal()">
            Done
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- Mobile Bottom Floating Bar (Native App Style) -->
  <div class="mobile-bottom-app-bar">
    <button class="mobile-nav-item active" data-tab="directory" onclick="switchMainTab('directory')">
      <i class="fa-solid fa-magnifying-glass"></i>
      <span>Search</span>
    </button>
    <button class="mobile-nav-item" data-tab="schedule" onclick="switchMainTab('schedule')">
      <i class="fa-regular fa-calendar-check"></i>
      <span>Schedule</span>
    </button>
    <button class="mobile-nav-item" data-tab="tracks" onclick="switchMainTab('tracks')">
      <i class="fa-solid fa-network-wired"></i>
      <span>Tracks</span>
    </button>
    <button class="mobile-nav-item" data-tab="itinerary" onclick="switchMainTab('itinerary')">
      <i class="fa-regular fa-bookmark"></i>
      <span>Saved</span>
      <span class="mobile-badge-dot" id="mobile-bookmark-badge" style="display:none;">0</span>
    </button>
    <button class="mobile-nav-item" data-tab="venue" onclick="switchMainTab('venue')">
      <i class="fa-solid fa-compass"></i>
      <span>Helpdesk</span>
    </button>
  </div>

  <!-- Toast Notification Popup -->
  <div class="corp-toast" id="corp-toast">
    <i class="fa-solid fa-circle-check"></i>
    <span id="toast-text-msg">Action performed successfully</span>
  </div>

  <!-- Corporate Footer -->
  <footer class="corporate-footer">
    <div class="container">
      <div class="footer-columns-grid">
        
        <div class="footer-col-corp">
          <h4>ISPSW National Conference 2026</h4>
          <p>
            Jointly organized by the <strong>Department of Studies in Social Work, Davangere University</strong> &amp; the <strong>Indian Society of Professional Social Work (ISPSW)</strong>.
          </p>
          <p>
            Theme: <em>“Innovative Technologies for Social Work Practice, Research and Development”</em>. Fostering technology-enabled social welfare aligned with Viksit Bharat 2047.
          </p>
          <p style="color: var(--cyan-400); font-weight: 600; font-size: 0.82rem;">
            <i class="fa-solid fa-calendar-day"></i> 7th – 9th October, 2026 | Shivagangotri Campus, Davangere University
          </p>
        </div>

        <div class="footer-col-corp">
          <h4>Quick Navigation</h4>
          <ul class="footer-links-col">
            <li><a href="javascript:void(0)" onclick="switchMainTab('directory')">Search Presentations &amp; Papers</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('schedule')">Full 3-Day Programme Flow</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('tracks')">9 Parallel Technical Tracks</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('themes')">Browse by 5 Themes</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('itinerary')">My Saved Itinerary</a></li>
            <li><a href="javascript:void(0)" onclick="switchMainTab('venue')">Helpdesk &amp; Transportation</a></li>
          </ul>
        </div>

        <div class="footer-col-corp">
          <h4>Secretariat &amp; Helpdesk</h4>
          <p>
            Department of Studies in Social Work<br>
            Shivagangotri Campus, Davangere University<br>
            Tholahunase, Davanagere – 577007, Karnataka
          </p>
          <p>
            <strong>Official Email:</strong><br>
            <a href="mailto:dumswispswnc2026@gmail.com">dumswispswnc2026@gmail.com</a>
          </p>
          <p>
            <strong>Registration Helpline:</strong><br>
            <span style="color: var(--white); font-family: var(--font-mono);">+91 98804 52671</span>
          </p>
        </div>

      </div>

      <div class="sub-footer-copyright">
        <div style="margin-bottom: 8px; font-size: 0.88rem; color: #cbd5e1;">
          <i class="fa-solid fa-laptop-code" style="color: var(--cyan-400); margin-right: 6px;"></i>
          Portal Designed &amp; Architected by <strong style="color: #fff;">Dr. Saravana Kadirvel</strong>
        </div>
        &copy; 2026 Davangere University &amp; Indian Society of Professional Social Work (ISPSW). All rights reserved. Peer-reviewed conference proceedings published for academic reference.
      </div>
    </div>
  </footer>

  <!-- EMBEDDED CONFERENCE DATA -->
  <script>
    const CONF_DB = __CONF_DB_JSON__;
  </script>

  <!-- APPLICATION CONTROLLER LOGIC -->
  <script>
    let activeTabId = 'directory';
    let activeTimelineDay = 'day1';
    let activeViewMode = 'grid';
    let activeThemeFilter = 'all';
    let modalActivePaper = null;
    let savedBookmarks = new Set();
    let filtersPanelOpen = false;

    // Load LocalStorage bookmarks
    try {
      const stored = localStorage.getItem('ispsw_corporate_bookmarks');
      if (stored) {
        savedBookmarks = new Set(JSON.parse(stored));
      }
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }

    document.addEventListener('DOMContentLoaded', () => {
      // Set responsive default for filters on mobile
      if (window.innerWidth < 992) {
        const tray = document.getElementById('filters-tray-grid');
        tray.style.display = 'none';
        filtersPanelOpen = false;
      } else {
        filtersPanelOpen = true;
      }

      renderPapersList();
      renderTimelineView('day1');
      renderTracksGrid();
      renderThemesCards();
      renderDignitariesList();
      renderHelpdeskGrid();
      refreshBookmarkBadges();

      // Keyboard escape for modal
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeAbstractModal();
      });
    });

    // Main Tab Switching (Desktop & Mobile)
    function switchMainTab(tabId) {
      activeTabId = tabId;

      // Update Desktop tabs
      document.querySelectorAll('.corp-nav-tab').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
      });

      // Update Mobile bottom tabs
      document.querySelectorAll('.mobile-nav-item').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
      });

      // Update Panels
      document.querySelectorAll('.tab-section-panel').forEach(p => {
        p.classList.remove('active');
      });
      const targetPanel = document.getElementById('tab-' + tabId);
      if (targetPanel) targetPanel.classList.add('active');

      if (tabId === 'itinerary') renderItineraryList();

      // Smooth scroll to top of content
      if (window.scrollY > 300) {
        window.scrollTo({ top: 320, behavior: 'smooth' });
      }
    }

    // Toggle Filters Panel on Mobile
    function toggleFiltersPanel() {
      const tray = document.getElementById('filters-tray-grid');
      const label = document.getElementById('toggle-filter-label');
      if (filtersPanelOpen) {
        tray.style.display = 'none';
        filtersPanelOpen = false;
        label.textContent = 'Show Filters & Sort';
      } else {
        tray.style.display = 'grid';
        filtersPanelOpen = true;
        label.textContent = 'Hide Filters & Sort';
      }
    }

    // View Mode Toggle (Grid vs List)
    function changeViewMode(mode) {
      activeViewMode = mode;
      const container = document.getElementById('papers-display-container');
      const btnGrid = document.getElementById('btn-grid-view');
      const btnList = document.getElementById('btn-list-view');

      if (mode === 'grid') {
        container.className = 'papers-grid-layout';
        btnGrid.classList.add('active');
        btnList.classList.remove('active');
      } else {
        container.className = 'papers-list-layout';
        btnList.classList.add('active');
        btnGrid.classList.remove('active');
      }
      renderPapersList();
    }

    // Quick Search Input
    function focusQuickSearch() {
      switchMainTab('directory');
      const input = document.getElementById('master-search-input');
      input.focus();
      input.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    let searchTimer = null;
    function handleSearchInputChange() {
      const input = document.getElementById('master-search-input');
      const btnClear = document.getElementById('btn-clear-search');
      btnClear.style.display = input.value.trim() ? 'block' : 'none';

      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        runFilters();
      }, 120);
    }

    function clearSearchInput() {
      const input = document.getElementById('master-search-input');
      input.value = '';
      document.getElementById('btn-clear-search').style.display = 'none';
      runFilters();
      input.focus();
    }

    // Quick Theme Horizon Filter
    function setQuickTheme(themeKey, btnElement) {
      activeThemeFilter = themeKey;
      document.querySelectorAll('.theme-chip-btn').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');

      document.getElementById('filter-theme').value = themeKey;
      runFilters();
    }

    // Filter Logic
    function getFilteredData() {
      const q = (document.getElementById('master-search-input').value || '').trim().toLowerCase();
      const scope = document.getElementById('filter-scope').value;
      const themeVal = document.getElementById('filter-theme').value;
      const dayVal = document.getElementById('filter-day').value;
      const venueVal = document.getElementById('filter-venue').value;
      const sortVal = document.getElementById('filter-sort').value;

      let list = CONF_DB.papers.filter(p => {
        if (themeVal !== 'all' && !p.theme.toLowerCase().includes(themeVal.toLowerCase())) return false;
        if (dayVal !== 'all' && !p.day.includes(dayVal)) return false;
        if (venueVal !== 'all' && !p.venue.toLowerCase().includes(venueVal.toLowerCase())) return false;

        if (q) {
          if (scope === 'author') {
            return p.authors.toLowerCase().includes(q) || (p.affiliation && p.affiliation.toLowerCase().includes(q));
          } else if (scope === 'title') {
            return p.title.toLowerCase().includes(q);
          } else if (scope === 'code') {
            return p.code.toLowerCase().includes(q);
          } else if (scope === 'keywords') {
            return p.keywords.some(k => k.toLowerCase().includes(q)) || p.abstract.toLowerCase().includes(q);
          } else if (scope === 'chair') {
            return (p.chairperson && p.chairperson.toLowerCase().includes(q)) || (p.discussant && p.discussant.toLowerCase().includes(q));
          } else {
            // All Fields
            return p.code.toLowerCase().includes(q) ||
                   p.title.toLowerCase().includes(q) ||
                   p.authors.toLowerCase().includes(q) ||
                   (p.affiliation && p.affiliation.toLowerCase().includes(q)) ||
                   p.venue.toLowerCase().includes(q) ||
                   p.theme.toLowerCase().includes(q) ||
                   p.time.toLowerCase().includes(q) ||
                   p.keywords.some(k => k.toLowerCase().includes(q)) ||
                   p.abstract.toLowerCase().includes(q);
          }
        }
        return true;
      });

      // Sorting
      list.sort((a, b) => {
        if (sortVal === 'code-asc') return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
        if (sortVal === 'code-desc') return b.code.localeCompare(a.code, undefined, { numeric: true, sensitivity: 'base' });
        if (sortVal === 'title-asc') return a.title.localeCompare(b.title);
        if (sortVal === 'author-asc') return a.authors.localeCompare(b.authors);
        if (sortVal === 'theme') return a.theme.localeCompare(b.theme);
        
        // Time / Presentation Schedule Order
        if (a.day !== b.day) return a.day.localeCompare(b.day);
        if (a.session_id !== b.session_id) return a.session_id.localeCompare(b.session_id);
        return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
      });

      return list;
    }

    function runFilters() {
      renderPapersList();
    }

    function resetAllFilters() {
      document.getElementById('master-search-input').value = '';
      document.getElementById('btn-clear-search').style.display = 'none';
      document.getElementById('filter-scope').value = 'all';
      document.getElementById('filter-theme').value = 'all';
      document.getElementById('filter-day').value = 'all';
      document.getElementById('filter-venue').value = 'all';
      document.getElementById('filter-sort').value = 'time';

      document.querySelectorAll('.theme-chip-btn').forEach(b => b.classList.remove('active'));
      const allBtn = document.querySelector('.theme-chip-btn');
      if (allBtn) allBtn.classList.add('active');

      runFilters();
      showToast('Filters reset to default view');
    }

    // Render Papers List
    function renderPapersList() {
      const container = document.getElementById('papers-display-container');
      const emptyBox = document.getElementById('empty-state-box');
      const countDisplay = document.getElementById('papers-visible-count');

      const papers = getFilteredData();
      countDisplay.textContent = papers.length;

      if (papers.length === 0) {
        container.innerHTML = '';
        emptyBox.style.display = 'block';
        return;
      }
      emptyBox.style.display = 'none';

      let html = '';
      papers.forEach(p => {
        const isStarred = savedBookmarks.has(p.code);
        const starClass = isStarred ? 'active' : '';
        const starIcon = isStarred ? 'fa-solid fa-bookmark' : 'fa-regular fa-bookmark';

        let themeTag = 'Theme';
        if (p.theme.includes('Theme 1')) themeTag = 'Theme 1 · Learning & Tech';
        else if (p.theme.includes('Theme 2')) themeTag = 'Theme 2 · AI & Intervention';
        else if (p.theme.includes('Theme 3')) themeTag = 'Theme 3 · Gender & Inclusion';
        else if (p.theme.includes('Theme 4')) themeTag = 'Theme 4 · Policy & Ethics';
        else if (p.theme.includes('Theme 5')) themeTag = 'Theme 5 · Viksit Bharat';

        if (activeViewMode === 'grid') {
          html += `
            <div class="corp-paper-card" id="paper-node-${p.code}">
              <div>
                <div class="card-top-row">
                  <span class="code-badge-corp"><i class="fa-solid fa-hashtag"></i> ${p.code}</span>
                  <span class="theme-pill-corp" title="${p.theme}">${themeTag}</span>
                </div>

                <h3 class="paper-headline">${p.title}</h3>

                <div class="authors-line-corp">
                  <i class="fa-solid fa-user-pen"></i>
                  <span>${p.authors}</span>
                </div>

                ${p.affiliation ? `<div class="affil-snippet" title="${p.affiliation.replace(/"/g, '&quot;')}">${p.affiliation}</div>` : ''}

                <div class="schedule-info-block">
                  <div class="sched-item">
                    <i class="fa-regular fa-calendar-check"></i>
                    <span>${p.day} (${p.date})</span>
                  </div>
                  <div class="sched-item">
                    <i class="fa-regular fa-clock"></i>
                    <span><strong>${p.time}</strong></span>
                  </div>
                  <div class="sched-item">
                    <i class="fa-solid fa-location-dot"></i>
                    <span title="${p.venue}">${p.venue.replace(', Davangere University', '')}</span>
                  </div>
                  <div class="sched-item">
                    <i class="fa-solid fa-user-graduate"></i>
                    <span title="Session Chair: ${p.chairperson}">Chair: ${p.chairperson ? p.chairperson.split(',')[0] : 'Committee'}</span>
                  </div>
                </div>
              </div>

              <div class="card-actions-bar">
                <button class="btn-view-abstract" onclick="openAbstractModal('${p.code}')">
                  <i class="fa-regular fa-file-lines"></i> Abstract &amp; Details
                </button>
                <button class="btn-star-bookmark ${starClass}" onclick="toggleBookmark('${p.code}')" title="${isStarred ? 'Remove from itinerary' : 'Save to My Itinerary'}">
                  <i class="${starIcon}"></i>
                </button>
              </div>
            </div>
          `;
        } else {
          // List View
          html += `
            <div class="corp-paper-card" id="paper-node-${p.code}">
              <div class="list-card-inner">
                <div>
                  <span class="code-badge-corp">${p.code}</span>
                </div>
                <div>
                  <h4 style="font-family: var(--font-brand); font-size: 1.1rem; color: var(--blue-950); margin-bottom: 3px;">${p.title}</h4>
                  <div style="font-size: 0.86rem; color: var(--slate-700); font-weight: 600;">
                    <i class="fa-solid fa-user-pen" style="color: var(--blue-600); margin-right: 4px;"></i> ${p.authors}
                  </div>
                  <div style="font-size: 0.74rem; color: var(--slate-500);">${themeTag}</div>
                </div>
                <div style="font-size: 0.8rem; color: var(--slate-700);">
                  <div><i class="fa-regular fa-clock" style="color: var(--blue-600); width: 14px;"></i> <strong>${p.time}</strong> (${p.day})</div>
                  <div><i class="fa-solid fa-location-dot" style="color: var(--blue-600); width: 14px;"></i> ${p.venue.replace(', Davangere University', '')}</div>
                </div>
                <div style="display: flex; gap: 8px; justify-content: flex-end;">
                  <button class="btn-view-abstract" onclick="openAbstractModal('${p.code}')" style="padding: 6px 12px; font-size: 0.8rem;">
                    Abstract
                  </button>
                  <button class="btn-star-bookmark ${starClass}" onclick="toggleBookmark('${p.code}')">
                    <i class="${starIcon}"></i>
                  </button>
                </div>
              </div>
            </div>
          `;
        }
      });

      container.innerHTML = html;
    }

    // Render Timeline View
    function setTimelineDay(dayKey, btnElement) {
      activeTimelineDay = dayKey;
      document.querySelectorAll('.day-pill-btn').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      renderTimelineView(dayKey);
    }

    function renderTimelineView(dayKey) {
      const container = document.getElementById('timeline-stream-container');
      const dayData = CONF_DB.programme_schedule[dayKey];
      if (!dayData) return;

      let html = '';
      dayData.events.forEach(ev => {
        let catClass = 'general';
        const evCat = ev.category.toLowerCase();
        if (evCat.includes('ceremonial')) catClass = 'ceremonial';
        else if (evCat.includes('plenary')) catClass = 'plenary';
        else if (evCat.includes('panel')) catClass = 'panel';
        else if (evCat.includes('technical')) catClass = 'technical';
        else if (evCat.includes('special')) catClass = 'special';
        else if (evCat.includes('cultural')) catClass = 'cultural';
        else if (evCat.includes('meals') || evCat.includes('networking')) catClass = 'meals';

        html += `
          <div class="timeline-corp-card ${catClass}">
            <div class="tl-time-box">
              <span class="tl-time-badge"><i class="fa-regular fa-clock"></i> ${ev.time}</span>
              <span class="tl-category-tag">${ev.category}</span>
            </div>
            <div class="tl-content-box">
              <h4>${ev.event}</h4>
              ${ev.details ? `<p class="tl-desc-p">${ev.details}</p>` : ''}
              ${ev.venue ? `<div class="tl-venue-label"><i class="fa-solid fa-location-dot"></i> Venue: ${ev.venue}</div>` : ''}
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Render Tracks Grid
    function renderTracksGrid() {
      const container = document.getElementById('tracks-matrix-container');
      let html = '';

      CONF_DB.technical_sessions.forEach(ts => {
        html += `
          <div class="track-grid-card">
            <div>
              <div class="track-pill-header">
                <span class="track-pill-badge">Session ${ts.session_num} · Track ${ts.track_num}</span>
                <span style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: 700; color: var(--blue-700);">${ts.day} (${ts.date})</span>
              </div>

              <h3>${ts.session_title}</h3>

              <ul class="track-details-list">
                <li><i class="fa-regular fa-clock"></i> <strong>Time:</strong> ${ts.time}</li>
                <li><i class="fa-solid fa-location-dot"></i> <strong>Venue:</strong> ${ts.venue}</li>
                <li><i class="fa-solid fa-user-graduate"></i> <strong>Chair:</strong> ${ts.chairperson}</li>
                ${ts.discussant ? `<li><i class="fa-solid fa-comments"></i> <strong>Discussant:</strong> ${ts.discussant}</li>` : ''}
                ${ts.rapporteurs ? `<li><i class="fa-solid fa-clipboard-user"></i> <strong>Rapporteurs:</strong> ${ts.rapporteurs}</li>` : ''}
                <li><i class="fa-solid fa-file-lines"></i> <strong>Presentations:</strong> ${ts.papers.length} Contributions</li>
              </ul>
            </div>

            <button class="btn-track-action" onclick="jumpToTrackPresentations('${ts.day}', '${ts.venue}')">
              View ${ts.papers.length} Presentations <i class="fa-solid fa-arrow-right"></i>
            </button>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function jumpToTrackPresentations(day, venue) {
      switchMainTab('directory');
      document.getElementById('filter-day').value = day;
      if (venue.includes('Auditorium')) {
        document.getElementById('filter-venue').value = 'MBA Auditorium';
      } else if (venue.includes('01')) {
        document.getElementById('filter-venue').value = 'MBA Lecture Hall-01';
      } else if (venue.includes('02')) {
        document.getElementById('filter-venue').value = 'MBA Lecture Hall-02';
      }
      runFilters();
      showToast(`Showing presentations for ${day} at ${venue}`);
    }

    // Render Themes Shelf
    function renderThemesCards() {
      const container = document.getElementById('themes-shelf-container');
      let html = '';

      CONF_DB.themes.forEach(th => {
        const count = CONF_DB.papers.filter(p => p.theme.includes(th.key)).length;
        html += `
          <div class="theme-detail-card">
            <div>
              <div class="theme-icon-orb">
                <i class="fa-solid ${th.icon}"></i>
              </div>
              <span style="font-family: var(--font-mono); font-size: 0.78rem; font-weight: 700; color: var(--blue-700); text-transform: uppercase;">${th.id}</span>
              <h3>${th.title}</h3>
              <p>${th.desc}</p>
            </div>

            <div style="border-top: 1px solid var(--slate-100); padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 0.82rem; font-weight: 700; color: var(--slate-600);">${count} Papers</span>
              <button class="btn-view-abstract" onclick="jumpToThemeFilter('${th.key}')" style="padding: 6px 12px; font-size: 0.82rem;">
                Explore Papers <i class="fa-solid fa-arrow-right"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function jumpToThemeFilter(themeKey) {
      switchMainTab('directory');
      document.getElementById('filter-theme').value = themeKey;
      runFilters();
      showToast(`Filtered by ${themeKey}`);
    }

    // Render Dignitaries, Valedictory Panel, National Presence & Organizing Committee
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
    }

    // Render Helpdesk Grid
    function renderHelpdeskGrid() {
      const container = document.getElementById('helpdesk-shelf-container');
      let html = '';

      CONF_DB.committee_contacts.forEach(c => {
        html += `
          <div class="helpdesk-unit-card">
            <div>
              <i class="fa-solid fa-phone-volume"></i>
              <h4>${c.role}</h4>
              <div class="name-text">${c.name}</div>
              <div style="font-size: 0.74rem; color: var(--slate-500);">${c.desig}</div>
            </div>
            <a href="tel:${c.phone.replace(/\\s+/g, '')}" class="helpdesk-phone-anchor">
              <i class="fa-solid fa-phone"></i> ${c.phone}
            </a>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Modal Operations
    function openAbstractModal(code) {
      const paper = CONF_DB.papers.find(p => p.code === code);
      if (!paper) return;

      modalActivePaper = paper;

      document.getElementById('modal-code-display').textContent = paper.code;
      document.getElementById('modal-title-display').textContent = paper.title;
      document.getElementById('modal-day-display').textContent = `${paper.day} (${paper.date})`;
      document.getElementById('modal-time-display').textContent = paper.time;
      document.getElementById('modal-venue-display').textContent = `${paper.venue} (${paper.session_title})`;
      document.getElementById('modal-chair-display').textContent = paper.chairperson ? paper.chairperson.split(',')[0] : 'Scientific Committee';
      
      document.getElementById('modal-authors-display').textContent = paper.authors;
      document.getElementById('modal-affil-display').textContent = paper.affiliation || 'Department of Studies in Social Work, Research Scholars & Faculty';
      
      const abstractContent = paper.abstract || 'The detailed text for this paper was accepted and published in the ISPSW 2026 Abstract Volume. Please refer to the session proceedings during the presentation.';
      document.getElementById('modal-abstract-body').textContent = abstractContent;

      const kwBox = document.getElementById('modal-keywords-box');
      const kwShelf = document.getElementById('modal-keywords-shelf');
      if (paper.keywords && paper.keywords.length > 0) {
        kwBox.style.display = 'block';
        kwShelf.innerHTML = paper.keywords.map(k => `<span class="kw-chip-corp">${k}</span>`).join('');
      } else {
        kwBox.style.display = 'none';
      }

      document.getElementById('modal-theme-indicator').textContent = paper.theme;

      updateModalBookmarkStatus();

      const modal = document.getElementById('corp-abstract-modal');
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeAbstractModal() {
      const modal = document.getElementById('corp-abstract-modal');
      modal.classList.remove('active');
      document.body.style.overflow = '';
      modalActivePaper = null;
    }

    function handleModalBackdropClick(e) {
      if (e.target.id === 'corp-abstract-modal') {
        closeAbstractModal();
      }
    }

    // Bookmarking Logic
    function toggleBookmark(code) {
      if (savedBookmarks.has(code)) {
        savedBookmarks.delete(code);
        showToast(`Removed [${code}] from your itinerary`);
      } else {
        savedBookmarks.add(code);
        showToast(`Saved [${code}] to your itinerary!`);
      }

      saveBookmarksToStorage();
      renderPapersList();
      refreshBookmarkBadges();
      if (activeTabId === 'itinerary') renderItineraryList();
    }

    function toggleModalBookmark() {
      if (!modalActivePaper) return;
      toggleBookmark(modalActivePaper.code);
      updateModalBookmarkStatus();
    }

    function updateModalBookmarkStatus() {
      if (!modalActivePaper) return;
      const btn = document.getElementById('modal-bookmark-btn');
      const has = savedBookmarks.has(modalActivePaper.code);
      if (has) {
        btn.innerHTML = '<i class="fa-solid fa-bookmark" style="color: var(--blue-600);"></i> Saved in Itinerary';
        btn.classList.add('primary');
      } else {
        btn.innerHTML = '<i class="fa-regular fa-bookmark"></i> Bookmark Presentation';
        btn.classList.remove('primary');
      }
    }

    function saveBookmarksToStorage() {
      try {
        localStorage.setItem('ispsw_corporate_bookmarks', JSON.stringify(Array.from(savedBookmarks)));
      } catch (e) {
        console.warn('Storage error:', e);
      }
    }

    function refreshBookmarkBadges() {
      const desktopBadge = document.getElementById('counter-itinerary');
      const mobileBadge = document.getElementById('mobile-bookmark-badge');
      const count = savedBookmarks.size;

      if (count > 0) {
        desktopBadge.textContent = count;
        desktopBadge.style.display = 'inline-block';
        mobileBadge.textContent = count;
        mobileBadge.style.display = 'inline-block';
      } else {
        desktopBadge.style.display = 'none';
        mobileBadge.style.display = 'none';
      }
    }

    function clearAllSavedBookmarks() {
      if (confirm('Clear all bookmarked presentations from your itinerary?')) {
        savedBookmarks.clear();
        saveBookmarksToStorage();
        refreshBookmarkBadges();
        renderItineraryList();
        renderPapersList();
        showToast('Itinerary cleared');
      }
    }

    function renderItineraryList() {
      const container = document.getElementById('itinerary-display-container');
      const emptyBox = document.getElementById('itinerary-empty-box');

      if (savedBookmarks.size === 0) {
        container.innerHTML = '';
        emptyBox.style.display = 'block';
        return;
      }
      emptyBox.style.display = 'none';

      const list = CONF_DB.papers.filter(p => savedBookmarks.has(p.code));
      let html = '';
      list.forEach(p => {
        html += `
          <div class="corp-paper-card">
            <div>
              <div class="card-top-row">
                <span class="code-badge-corp"><i class="fa-solid fa-bookmark"></i> ${p.code}</span>
                <span class="theme-pill-corp">${p.day}</span>
              </div>
              <h3 class="paper-headline">${p.title}</h3>
              <div class="authors-line-corp"><i class="fa-solid fa-user-pen"></i> ${p.authors}</div>
              <div class="schedule-info-block">
                <div class="sched-item"><i class="fa-regular fa-clock"></i> <strong>${p.time}</strong></div>
                <div class="sched-item"><i class="fa-solid fa-location-dot"></i> ${p.venue}</div>
              </div>
            </div>
            <div class="card-actions-bar">
              <button class="btn-view-abstract" onclick="openAbstractModal('${p.code}')">
                <i class="fa-regular fa-file-lines"></i> Details
              </button>
              <button class="btn-star-bookmark active" onclick="toggleBookmark('${p.code}')" title="Remove">
                <i class="fa-solid fa-bookmark"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function copyCitationFromModal() {
      if (!modalActivePaper) return;
      const citation = `${modalActivePaper.authors} (2026). "${modalActivePaper.title}". In Proceedings of the Annual National Conference of ISPSW – 2026, Davangere University, Karnataka. Paper Code: ${modalActivePaper.code}.`;
      navigator.clipboard.writeText(citation).then(() => {
        showToast('Citation copied to clipboard!');
      }).catch(() => {
        showToast('Citation ready');
      });
    }

    // Toast Notification
    function showToast(msg) {
      const toast = document.getElementById('corp-toast');
      const text = document.getElementById('toast-text-msg');
      text.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2800);
    }
  </script>

</body>
</html>
'''

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

print(f"Generated {output_path} ({len(final_html)} bytes) successfully!")
