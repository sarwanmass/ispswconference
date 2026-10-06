import json
import base64
import os

print("Rebuilding mobile-first corporate app conference portal...")

with open("conference_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

json_data_str = json.dumps(db, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes, viewport-fit=cover">
  <title>ISPSW 2026 | Conference App &amp; Schedule Portal</title>
  <meta name="description" content="Official Mobile App & Schedule Portal for the Annual National Conference of ISPSW 2026 at Davangere University. Search 115 papers, view 3-day schedule, tracks, and abstracts.">
  <meta name="theme-color" content="#0e2a5c">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- Elite Mobile Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

  <style>
    /* ========================================================= */
    /* MOBILE-FIRST CORPORATE APP DESIGN SYSTEM                  */
    /* ========================================================= */
    :root {
      --app-blue-950: #081630;
      --app-blue-900: #0e2a5c;
      --app-blue-800: #143b7d;
      --app-blue-700: #1a56db;
      --app-blue-600: #2563eb;
      --app-blue-500: #3b82f6;
      --app-blue-400: #60a5fa;
      --app-blue-200: #bfdbfe;
      --app-blue-100: #dbeafe;
      --app-blue-50:  #eff6ff;
      --app-cyan:     #0ea5e9;
      --app-cyan-light: #e0f2fe;

      --app-bg:       #f4f7fc;
      --app-card:     #ffffff;
      --app-border:   #e2e8f0;
      --app-border-focus: #3b82f6;
      
      --text-main:    #0f172a;
      --text-muted:   #475569;
      --text-subtle:  #64748b;
      --text-light:   #94a3b8;
      --text-white:   #ffffff;

      --font-heading: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body:    'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono:    'JetBrains Mono', monospace;

      --shadow-sm:    0 1px 3px rgba(14, 42, 92, 0.05);
      --shadow-card:  0 4px 16px -2px rgba(14, 42, 92, 0.08);
      --shadow-lift:  0 10px 28px -4px rgba(26, 86, 219, 0.16);
      --shadow-sheet: 0 -10px 40px rgba(8, 22, 48, 0.28);

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --radius-full: 9999px;

      --safe-bottom: env(safe-area-inset-bottom, 12px);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html, body {
      font-family: var(--font-body);
      background-color: var(--app-bg);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
    }

    /* Container */
    .app-shell {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 14px;
    }

    @media (min-width: 768px) {
      .app-shell {
        padding: 0 24px;
      }
    }

    /* ========================================================= */
    /* TOP MOBILE APP BAR (SLEEK & TOUCH-FRIENDLY)               */
    /* ========================================================= */
    .mobile-app-header {
      position: sticky;
      top: 0;
      z-index: 900;
      background: linear-gradient(135deg, var(--app-blue-950) 0%, var(--app-blue-900) 100%);
      color: var(--text-white);
      border-bottom: 2px solid var(--app-blue-700);
      box-shadow: 0 4px 16px rgba(8, 22, 48, 0.18);
    }

    .app-top-nav-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 62px;
      padding: 0 4px;
      gap: 10px;
    }

    .app-brand-lockup {
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      text-decoration: none;
      color: inherit;
      min-width: 0;
    }

    .app-emblem-pair {
      display: flex;
      align-items: center;
      gap: 4px;
      flex-shrink: 0;
    }

    .app-mini-emblem {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #ffffff;
      padding: 3px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1.5px solid var(--app-cyan);
      box-shadow: 0 2px 6px rgba(0,0,0,0.25);
    }

    .app-mini-emblem img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }

    .app-brand-text {
      min-width: 0;
    }

    .app-brand-title {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .app-brand-title .badge-ispsw {
      background: var(--app-blue-700);
      font-size: 0.72rem;
      padding: 1px 6px;
      border-radius: 4px;
      color: #fff;
    }

    .app-brand-sub {
      font-size: 0.72rem;
      color: var(--app-cyan);
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .app-top-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }

    .btn-top-icon {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.18);
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      cursor: pointer;
      position: relative;
      transition: all 0.2s;
    }

    .btn-top-icon:active {
      transform: scale(0.92);
      background: var(--app-blue-700);
    }

    .top-count-dot {
      position: absolute;
      top: -3px;
      right: -3px;
      background: #ef4444;
      color: #ffffff;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 1px 5px;
      border-radius: 999px;
      border: 1.5px solid var(--app-blue-900);
    }

    /* Sub-bar Architect Attribution */
    .app-sub-credit-bar {
      background: rgba(8, 22, 48, 0.95);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 5px 12px;
      font-size: 0.75rem;
      color: #cbd5e1;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }

    .credit-tag-link {
      color: var(--app-cyan);
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    /* ========================================================= */
    /* HERO MOBILE APP CARD                                      */
    /* ========================================================= */
    .hero-app-banner {
      background: linear-gradient(135deg, var(--app-blue-900) 0%, var(--app-blue-800) 50%, var(--app-blue-700) 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 20px 18px;
      margin-top: 14px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-card);
      position: relative;
      overflow: hidden;
    }

    @media (min-width: 768px) {
      .hero-app-banner {
        padding: 30px 28px;
        margin-top: 20px;
        margin-bottom: 24px;
      }
    }

    .hero-app-banner::before {
      content: "";
      position: absolute;
      top: -30%; right: -20%;
      width: 250px; height: 250px;
      background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .hero-event-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .hero-main-title {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.35;
      color: #ffffff;
      margin-bottom: 8px;
    }

    @media (min-width: 768px) {
      .hero-main-title {
        font-size: 1.85rem;
      }
    }

    .hero-venue-line {
      font-size: 0.82rem;
      color: var(--app-cyan-light);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 14px;
      font-weight: 500;
    }

    .hero-venue-line i {
      color: var(--app-cyan);
    }

    /* Key Metrics Mini Chips */
    .hero-metrics-chips {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .hero-metrics-chips::-webkit-scrollbar {
      display: none;
    }

    .h-chip {
      background: rgba(8, 22, 48, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-size: 0.78rem;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #f1f5f9;
      flex-shrink: 0;
    }

    .h-chip strong {
      color: #ffffff;
      font-weight: 800;
    }

    /* Hero Fast Candidate Finder */
    .hero-fast-finder {
      margin-top: 14px;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: var(--radius-md);
      padding: 4px;
      display: flex;
      gap: 6px;
    }

    .hero-fast-input {
      flex: 1;
      background: #ffffff;
      border: none;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      font-family: var(--font-body);
      font-size: 0.9rem;
      color: var(--text-main);
      outline: none;
    }

    .hero-fast-btn {
      background: var(--app-cyan);
      color: #ffffff;
      font-weight: 800;
      border: none;
      padding: 0 16px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.85rem;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s;
    }

    .hero-fast-btn:active {
      background: #0284c7;
    }

    /* ========================================================= */
    /* APP HORIZONTAL SWIPEABLE TAB NAVIGATION                   */
    /* ========================================================= */
    .app-nav-scroller-wrap {
      margin-bottom: 14px;
    }

    .app-nav-pills-row {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 4px 0 8px 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .app-nav-pills-row::-webkit-scrollbar {
      display: none;
    }

    .app-pill-tab {
      background: var(--app-card);
      border: 1px solid var(--app-border);
      border-radius: var(--radius-full);
      padding: 8px 16px;
      font-family: var(--font-body);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s;
      flex-shrink: 0;
      box-shadow: var(--shadow-sm);
    }

    .app-pill-tab i {
      font-size: 0.9rem;
      color: var(--app-blue-600);
    }

    .app-pill-tab:hover {
      border-color: var(--app-blue-500);
      color: var(--app-blue-700);
    }

    .app-pill-tab.active {
      background: var(--app-blue-700);
      border-color: var(--app-blue-700);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(26, 86, 219, 0.25);
    }

    .app-pill-tab.active i {
      color: #ffffff;
    }

    .pill-counter {
      background: var(--app-blue-100);
      color: var(--app-blue-700);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 1px 6px;
      border-radius: 999px;
    }

    .app-pill-tab.active .pill-counter {
      background: rgba(255, 255, 255, 0.25);
      color: #ffffff;
    }

    /* ========================================================= */
    /* APP SEARCH & INSTANT TOUCH FILTER CHIPS                   */
    /* ========================================================= */
    .app-search-deck {
      background: var(--app-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--app-border);
      padding: 14px;
      box-shadow: var(--shadow-card);
      margin-bottom: 14px;
    }

    .app-search-box {
      display: flex;
      align-items: center;
      position: relative;
      width: 100%;
    }

    .app-search-icon {
      position: absolute;
      left: 14px;
      font-size: 1.05rem;
      color: var(--app-blue-600);
      pointer-events: none;
    }

    .app-main-input {
      width: 100%;
      height: 48px;
      padding: 0 40px 0 44px;
      font-family: var(--font-body);
      font-size: 0.95rem;
      font-weight: 500;
      background: var(--app-bg);
      border: 1.5px solid var(--app-border);
      border-radius: var(--radius-md);
      color: var(--text-main);
      outline: none;
      transition: all 0.2s ease;
    }

    .app-main-input:focus {
      background: #ffffff;
      border-color: var(--app-blue-600);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }

    .btn-clear-q {
      position: absolute;
      right: 12px;
      background: none;
      border: none;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      color: var(--text-subtle);
      font-size: 0.9rem;
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
    }

    .btn-clear-q:hover {
      background: var(--app-border);
      color: var(--text-main);
    }

    /* Touch-friendly Quick Chips */
    .quick-chips-scroller {
      display: flex;
      gap: 7px;
      overflow-x: auto;
      padding: 10px 0 4px 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }

    .quick-chips-scroller::-webkit-scrollbar {
      display: none;
    }

    .touch-chip {
      background: var(--app-bg);
      border: 1px solid var(--app-border);
      padding: 6px 12px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.18s;
      flex-shrink: 0;
    }

    .touch-chip:active {
      transform: scale(0.95);
    }

    .touch-chip.active {
      background: var(--app-blue-600);
      border-color: var(--app-blue-600);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
    }

    /* Search Action Controls */
    .search-meta-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px dashed var(--app-border);
      font-size: 0.82rem;
    }

    .results-badge-text {
      color: var(--text-muted);
      font-weight: 600;
    }

    .results-badge-text strong {
      color: var(--app-blue-700);
      font-family: var(--font-mono);
      font-size: 0.95rem;
    }

    .search-sub-actions {
      display: flex;
      gap: 8px;
    }

    .btn-sub-tool {
      background: var(--app-bg);
      border: 1px solid var(--app-border);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .btn-sub-tool:active {
      background: var(--app-blue-100);
      color: var(--app-blue-700);
    }

    /* Advanced Filters Drawer (Inline) */
    .advanced-filters-box {
      display: none;
      grid-template-columns: 1fr;
      gap: 10px;
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px solid var(--app-border);
    }

    @media (min-width: 600px) {
      .advanced-filters-box {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .adv-filter-cell {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .adv-filter-cell label {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-subtle);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .adv-select {
      height: 38px;
      border: 1px solid var(--app-border);
      border-radius: var(--radius-sm);
      background: #ffffff;
      padding: 0 10px;
      font-family: var(--font-body);
      font-size: 0.85rem;
      color: var(--text-main);
      outline: none;
    }

    /* ========================================================= */
    /* MOBILE-PERFECT PAPER CARD                                 */
    /* ========================================================= */
    .app-cards-feed {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
      margin-bottom: 24px;
    }

    @media (min-width: 768px) {
      .app-cards-feed {
        grid-template-columns: repeat(2, 1fr);
        gap: 18px;
      }
    }

    @media (min-width: 1100px) {
      .app-cards-feed {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .paper-mobile-card {
      background: var(--app-card);
      border-radius: var(--radius-md);
      border: 1px solid var(--app-border);
      padding: 16px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.18s, box-shadow 0.18s, border-color 0.18s;
      position: relative;
    }

    .paper-mobile-card:hover {
      border-color: var(--app-blue-400);
      box-shadow: var(--shadow-lift);
      transform: translateY(-2px);
    }

    .card-meta-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }

    .paper-code-tag {
      background: var(--app-blue-50);
      color: var(--app-blue-700);
      border: 1px solid var(--app-blue-200);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.5px;
    }

    .paper-theme-badge {
      background: var(--app-bg);
      color: var(--text-muted);
      font-size: 0.7rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      max-width: 170px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .paper-card-title {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 700;
      line-height: 1.35;
      color: var(--app-blue-950);
      margin-bottom: 8px;
    }

    .paper-card-author {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 6px;
      margin-bottom: 10px;
    }

    .paper-card-author i {
      color: var(--app-blue-600);
      margin-top: 3px;
      font-size: 0.82rem;
    }

    /* Micro Slot Schedule Chip Block */
    .card-slot-strip {
      background: var(--app-blue-50);
      border: 1px solid var(--app-blue-100);
      border-radius: var(--radius-sm);
      padding: 9px 12px;
      margin-bottom: 12px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      font-size: 0.78rem;
    }

    .slot-cell {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--text-muted);
    }

    .slot-cell i {
      color: var(--app-blue-600);
      width: 13px;
      font-size: 0.8rem;
    }

    .slot-cell strong {
      color: var(--app-blue-950);
    }

    /* Card Action Buttons */
    .card-bottom-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--app-border);
    }

    .btn-tap-abstract {
      flex: 1;
      height: 42px;
      background: #ffffff;
      border: 1.5px solid var(--app-blue-600);
      color: var(--app-blue-700);
      font-family: var(--font-body);
      font-size: 0.84rem;
      font-weight: 700;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.18s;
    }

    .btn-tap-abstract:active {
      background: var(--app-blue-700);
      color: #ffffff;
      transform: scale(0.98);
    }

    .btn-tap-star {
      width: 42px;
      height: 42px;
      background: #ffffff;
      border: 1.5px solid var(--app-border);
      border-radius: var(--radius-sm);
      color: var(--text-light);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.05rem;
      cursor: pointer;
      transition: all 0.18s;
      flex-shrink: 0;
    }

    .btn-tap-star:active {
      transform: scale(0.9);
    }

    .btn-tap-star.active {
      background: var(--app-blue-50);
      border-color: var(--app-blue-600);
      color: var(--app-blue-600);
    }

    /* Empty state */
    .app-empty-state {
      text-align: center;
      padding: 40px 16px;
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 2px dashed var(--app-border);
      margin-top: 14px;
    }

    .app-empty-state i {
      font-size: 2.5rem;
      color: var(--app-blue-400);
      margin-bottom: 12px;
    }

    .app-empty-state h3 {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      color: var(--app-blue-950);
      margin-bottom: 6px;
    }

    .app-empty-state p {
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-bottom: 16px;
    }

    /* ========================================================= */
    /* TIMELINE VIEW (PROGRAMME FLOW DAYS 1, 2, 3)               */
    /* ========================================================= */
    .day-selector-segment {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      overflow-x: auto;
      scrollbar-width: none;
    }

    .day-segment-btn {
      flex: 1;
      min-width: 100px;
      background: #ffffff;
      border: 1.5px solid var(--app-border);
      border-radius: var(--radius-md);
      padding: 10px 8px;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .day-segment-btn.active {
      background: var(--app-blue-900);
      border-color: var(--app-blue-900);
      color: #ffffff;
      box-shadow: var(--shadow-card);
    }

    .day-segment-btn .ds-title {
      font-family: var(--font-heading);
      font-size: 0.95rem;
      font-weight: 800;
    }

    .day-segment-btn .ds-sub {
      font-size: 0.72rem;
      color: var(--text-subtle);
    }

    .day-segment-btn.active .ds-sub {
      color: var(--app-cyan);
    }

    .timeline-card-stream {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .app-timeline-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--app-border);
      padding: 14px 16px;
      box-shadow: var(--shadow-sm);
      border-left: 4px solid var(--app-blue-600);
    }

    .app-timeline-card.ceremonial { border-left-color: var(--app-blue-600); }
    .app-timeline-card.plenary { border-left-color: var(--app-cyan); }
    .app-timeline-card.panel { border-left-color: #6366f1; }
    .app-timeline-card.technical { border-left-color: #10b981; }
    .app-timeline-card.special { border-left-color: #8b5cf6; }
    .app-timeline-card.cultural { border-left-color: #ec4899; }
    .app-timeline-card.meals { border-left-color: var(--text-light); background: #fafafa; }

    .tl-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }

    .tl-time-chip {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--app-blue-900);
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .tl-cat-badge {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--app-blue-50);
      color: var(--app-blue-700);
    }

    .tl-title {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--app-blue-950);
      margin-bottom: 4px;
    }

    .tl-details {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 6px;
      line-height: 1.45;
    }

    .tl-venue {
      font-size: 0.78rem;
      color: var(--text-subtle);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .tl-venue i {
      color: var(--app-blue-600);
    }

    /* ========================================================= */
    /* 9 TRACKS MATRIX & THEMES                                  */
    /* ========================================================= */
    .tracks-app-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    @media (min-width: 768px) {
      .tracks-app-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .tracks-app-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .track-tile-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--app-border);
      padding: 16px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .track-badge-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .track-title-h3 {
      font-family: var(--font-heading);
      font-size: 1.12rem;
      font-weight: 800;
      color: var(--app-blue-950);
      margin-bottom: 8px;
    }

    .track-info-list {
      list-style: none;
      font-size: 0.82rem;
      color: var(--text-muted);
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 12px;
    }

    .btn-open-track {
      height: 38px;
      background: var(--app-blue-50);
      border: 1px solid var(--app-blue-200);
      color: var(--app-blue-700);
      font-weight: 700;
      font-size: 0.82rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }

    .btn-open-track:active {
      background: var(--app-blue-700);
      color: #ffffff;
    }

    /* ========================================================= */
    /* DIGNITARIES & CEREMONIAL PANELS                           */
    /* ========================================================= */
    .dignitaries-mobile-shelf {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    @media (min-width: 600px) {
      .dignitaries-mobile-shelf {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .dignitary-card-mobile {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--app-border);
      padding: 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: var(--shadow-sm);
    }

    .dig-avatar-ring {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      border: 2px solid var(--app-blue-600);
      padding: 2px;
      overflow: hidden;
      flex-shrink: 0;
      background: #ffffff;
    }

    .dig-avatar-ring img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 50%;
    }

    .dig-avatar-ring .fallback-ico {
      width: 100%;
      height: 100%;
      background: var(--app-blue-50);
      color: var(--app-blue-700);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      border-radius: 50%;
    }

    .dig-details-box h4 {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--app-blue-950);
      margin-bottom: 2px;
    }

    .dig-role-chip {
      font-size: 0.68rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--app-blue-700);
      letter-spacing: 0.5px;
      display: block;
    }

    .dig-affil {
      font-size: 0.78rem;
      color: var(--text-subtle);
      line-height: 1.35;
    }

    /* ========================================================= */
    /* MOBILE BOTTOM SHEET / MODAL (NATIVE APP FEEL)             */
    /* ========================================================= */
    .app-sheet-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(8, 22, 48, 0.7);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      z-index: 1200;
      display: none;
      align-items: flex-end;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.22s ease;
    }

    @media (min-width: 768px) {
      .app-sheet-backdrop {
        align-items: center;
        padding: 20px;
      }
    }

    .app-sheet-backdrop.active {
      display: flex;
      opacity: 1;
    }

    .app-bottom-sheet {
      background: #ffffff;
      width: 100%;
      max-width: 760px;
      max-height: 90vh;
      border-radius: 24px 24px 0 0;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sheet);
      animation: sheetSlideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    @media (min-width: 768px) {
      .app-bottom-sheet {
        border-radius: var(--radius-xl);
        max-height: 85vh;
      }
    }

    @keyframes sheetSlideUp {
      from { transform: translateY(100%); }
      to { transform: translateY(0); }
    }

    /* Mobile Sheet Drag Handle */
    .sheet-handle-pill {
      width: 44px;
      height: 5px;
      background: #cbd5e1;
      border-radius: 999px;
      margin: 10px auto 4px auto;
      flex-shrink: 0;
    }

    .sheet-top-header {
      padding: 12px 18px 14px 18px;
      border-bottom: 1px solid var(--app-border);
      position: relative;
    }

    .sheet-close-x {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--app-bg);
      border: 1px solid var(--app-border);
      color: var(--text-main);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      cursor: pointer;
    }

    .sheet-code-pill {
      background: var(--app-blue-50);
      color: var(--app-blue-700);
      border: 1px solid var(--app-blue-200);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      display: inline-block;
      margin-bottom: 4px;
    }

    .sheet-heading {
      font-family: var(--font-heading);
      font-size: 1.18rem;
      font-weight: 800;
      color: var(--app-blue-950);
      line-height: 1.35;
      padding-right: 36px;
    }

    .sheet-scroll-body {
      padding: 16px 18px;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      flex: 1;
    }

    .sheet-slot-box {
      background: var(--app-blue-50);
      border: 1px solid var(--app-blue-100);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      margin-bottom: 16px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      font-size: 0.8rem;
    }

    .sheet-abstract-text {
      font-size: 0.92rem;
      line-height: 1.65;
      color: var(--text-main);
      text-align: justify;
      white-space: pre-line;
      margin-top: 8px;
    }

    .sheet-sticky-footer {
      padding: 12px 18px;
      padding-bottom: calc(12px + var(--safe-bottom));
      background: #ffffff;
      border-top: 1px solid var(--app-border);
      display: flex;
      gap: 10px;
    }

    .btn-sheet-action {
      flex: 1;
      height: 44px;
      border-radius: var(--radius-md);
      font-family: var(--font-body);
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-sheet-action.secondary {
      background: var(--app-bg);
      border: 1px solid var(--app-border);
      color: var(--text-main);
    }

    .btn-sheet-action.primary {
      background: var(--app-blue-700);
      border: none;
      color: #ffffff;
    }

    /* ========================================================= */
    /* FIXED MOBILE APP BOTTOM BAR                               */
    /* ========================================================= */
    .app-bottom-dock {
      position: fixed;
      bottom: 0; left: 0; right: 0;
      height: calc(56px + var(--safe-bottom));
      padding-bottom: var(--safe-bottom);
      background: #ffffff;
      border-top: 1px solid var(--app-border);
      display: flex;
      justify-content: space-around;
      align-items: center;
      z-index: 1000;
      box-shadow: 0 -4px 16px rgba(8, 22, 48, 0.08);
    }

    .dock-tab-btn {
      background: none;
      border: none;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: var(--text-subtle);
      font-size: 0.68rem;
      font-weight: 700;
      cursor: pointer;
      flex: 1;
      height: 100%;
      position: relative;
      transition: color 0.18s;
    }

    .dock-tab-btn i {
      font-size: 1.15rem;
      margin-bottom: 2px;
      transition: transform 0.18s;
    }

    .dock-tab-btn.active {
      color: var(--app-blue-700);
    }

    .dock-tab-btn.active i {
      transform: translateY(-2px);
      color: var(--app-blue-700);
    }

    .dock-bubble-badge {
      position: absolute;
      top: 4px;
      right: 24%;
      background: #ef4444;
      color: #ffffff;
      font-size: 0.62rem;
      font-weight: 800;
      padding: 1px 5px;
      border-radius: 999px;
    }

    /* Padding for bottom dock on mobile */
    .app-content-area {
      padding-bottom: calc(75px + var(--safe-bottom));
    }

    /* View Panel Switches */
    .app-section-panel {
      display: none;
      animation: tabFadeIn 0.2s ease;
    }

    .app-section-panel.active {
      display: block;
    }

    @keyframes tabFadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Toast Notification */
    .app-toast-box {
      position: fixed;
      bottom: calc(68px + var(--safe-bottom));
      left: 16px;
      right: 16px;
      max-width: 440px;
      margin: 0 auto;
      background: var(--app-blue-950);
      color: #ffffff;
      border-left: 4px solid var(--app-cyan);
      border-radius: var(--radius-sm);
      padding: 11px 16px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1300;
      transform: translateY(60px);
      opacity: 0;
      transition: all 0.22s ease;
      font-size: 0.85rem;
      font-weight: 600;
    }

    .app-toast-box.show {
      transform: translateY(0);
      opacity: 1;
    }

    .app-toast-box i {
      color: var(--app-cyan);
    }

    /* Footer */
    .app-mobile-footer {
      background: var(--app-blue-950);
      color: var(--text-light);
      padding: 30px 16px 20px 16px;
      border-top: 3px solid var(--app-blue-600);
      border-radius: var(--radius-lg) var(--radius-lg) 0 0;
      margin-top: 30px;
      font-size: 0.82rem;
    }
  </style>
</head>
<body>

  <!-- Top Mobile App Bar -->
  <header class="mobile-app-header">
    <div class="app-shell">
      <div class="app-top-nav-row">
        
        <!-- App Brand Logo & Title -->
        <a href="javascript:void(0)" class="app-brand-lockup" onclick="switchAppTab('directory')">
          <div class="app-emblem-pair">
            <div class="app-mini-emblem" title="Davangere University">
              __DAVANGERE_LOGO_HTML__
            </div>
            <div class="app-mini-emblem" title="ISPSW">
              __ISPSW_LOGO_HTML__
            </div>
          </div>
          <div class="app-brand-text">
            <div class="app-brand-title">ISPSW 2026 <span class="badge-ispsw">National Conf</span></div>
            <div class="app-brand-sub">Davangere University · 7–9 Oct</div>
          </div>
        </a>

        <!-- Top Right Actions -->
        <div class="app-top-actions">
          <button class="btn-top-icon" onclick="focusSearchInput()" title="Search">
            <i class="fa-solid fa-magnifying-glass"></i>
          </button>
          <button class="btn-top-icon" onclick="switchAppTab('itinerary')" title="My Itinerary">
            <i class="fa-regular fa-bookmark"></i>
            <span class="top-count-dot" id="top-itinerary-badge" style="display:none;">0</span>
          </button>
        </div>

      </div>
    </div>

    <!-- Official Attribution Sub-Bar -->
    <div class="app-sub-credit-bar">
      <div class="app-shell" style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
        <span><i class="fa-solid fa-calendar-day" style="color: var(--app-cyan); margin-right: 4px;"></i> 7th – 9th OCTOBER, 2026</span>
        <span class="credit-tag-link"><i class="fa-solid fa-code"></i> Designed &amp; Architected by <strong>Dr. Saravana Kadirvel</strong></span>
      </div>
    </div>
  </header>

  <!-- Main App Shell -->
  <div class="app-shell app-content-area">

    <!-- ========================================================= -->
    <!-- HERO APP CARD                                             -->
    <!-- ========================================================= -->
    <div class="hero-app-banner">
      <div class="hero-event-tag">
        <i class="fa-solid fa-award"></i> Annual National Conference
      </div>
      <h1 class="hero-main-title">“Innovative Technologies for Social Work Practice, Research and Development”</h1>
      <div class="hero-venue-line">
        <i class="fa-solid fa-location-dot"></i> MBA Auditorium &amp; Academic Complex, Shivagangotri Campus
      </div>

      <!-- Quick Metrics Chips -->
      <div class="hero-metrics-chips">
        <div class="h-chip"><i class="fa-regular fa-file-lines"></i> <strong>115</strong> Papers</div>
        <div class="h-chip"><i class="fa-solid fa-network-wired"></i> <strong>9</strong> Tracks</div>
        <div class="h-chip"><i class="fa-regular fa-calendar-check"></i> <strong>3</strong> Days</div>
        <div class="h-chip"><i class="fa-solid fa-users"></i> <strong>4</strong> Plenaries</div>
        <div class="h-chip"><i class="fa-solid fa-comments"></i> <strong>3</strong> Panels</div>
      </div>

      <!-- Fast Candidate Lookup -->
      <div class="hero-fast-finder">
        <input type="text" id="hero-quick-find" class="hero-fast-input" placeholder="Find my paper (enter name or code A1..J24)...">
        <button class="hero-fast-btn" onclick="executeHeroFind()">
          <i class="fa-solid fa-arrow-right"></i> Find
        </button>
      </div>
    </div>

    <!-- Horizontal Swipeable Pill Tabs -->
    <div class="app-nav-scroller-wrap">
      <div class="app-nav-pills-row">
        <button class="app-pill-tab active" data-tab="directory" onclick="switchAppTab('directory')">
          <i class="fa-solid fa-magnifying-glass"></i> Directory
          <span class="pill-counter" id="pill-count-total">115</span>
        </button>
        <button class="app-pill-tab" data-tab="schedule" onclick="switchAppTab('schedule')">
          <i class="fa-regular fa-calendar-check"></i> 3-Day Schedule
        </button>
        <button class="app-pill-tab" data-tab="tracks" onclick="switchAppTab('tracks')">
          <i class="fa-solid fa-network-wired"></i> 9 Tracks
        </button>
        <button class="app-pill-tab" data-tab="themes" onclick="switchAppTab('themes')">
          <i class="fa-solid fa-layer-group"></i> 5 Themes
        </button>
        <button class="app-pill-tab" data-tab="dignitaries" onclick="switchAppTab('dignitaries')">
          <i class="fa-solid fa-user-tie"></i> Dignitaries
        </button>
        <button class="app-pill-tab" data-tab="itinerary" onclick="switchAppTab('itinerary')">
          <i class="fa-regular fa-bookmark"></i> My Saved
          <span class="pill-counter" id="pill-count-saved" style="display:none;">0</span>
        </button>
        <button class="app-pill-tab" data-tab="venue" onclick="switchAppTab('venue')">
          <i class="fa-solid fa-compass"></i> Helpdesk
        </button>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SECTION 1: SEARCH & PRESENTATION DIRECTORY                -->
    <!-- ========================================================= -->
    <section id="sec-directory" class="app-section-panel active">
      
      <!-- App Search Cockpit -->
      <div class="app-search-deck">
        <div class="app-search-box">
          <i class="fa-solid fa-magnifying-glass app-search-icon"></i>
          <input type="text" id="app-search-input" class="app-main-input" placeholder="Search presenter, title, code (A1..J24), time, hall..." oninput="handleSearchType()">
          <button class="btn-clear-q" id="btn-clear-search-x" onclick="clearSearchInput()" title="Clear">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Touch-Friendly Instant Quick Filter Chips -->
        <div class="quick-chips-scroller">
          <button class="touch-chip active" onclick="setChipFilter('all', this)"><i class="fa-solid fa-border-all"></i> All (115)</button>
          <button class="touch-chip" onclick="setChipFilter('Day 01', this)"><i class="fa-regular fa-calendar"></i> Day 1 (Wed)</button>
          <button class="touch-chip" onclick="setChipFilter('Day 02', this)"><i class="fa-regular fa-calendar"></i> Day 2 (Thu)</button>
          <button class="touch-chip" onclick="setChipFilter('Day 03', this)"><i class="fa-regular fa-calendar"></i> Day 3 (Fri)</button>
          <button class="touch-chip" onclick="setChipFilter('Theme 1', this)">Theme 1: Tech &amp; Learning</button>
          <button class="touch-chip" onclick="setChipFilter('Theme 2', this)">Theme 2: AI &amp; Interventions</button>
          <button class="touch-chip" onclick="setChipFilter('Theme 3', this)">Theme 3: Gender &amp; Inclusion</button>
          <button class="touch-chip" onclick="setChipFilter('Theme 4', this)">Theme 4: Policy &amp; Ethics</button>
          <button class="touch-chip" onclick="setChipFilter('Theme 5', this)">Theme 5: Viksit Bharat</button>
          <button class="touch-chip" onclick="setChipFilter('MBA Auditorium', this)"><i class="fa-solid fa-location-dot"></i> MBA Auditorium</button>
          <button class="touch-chip" onclick="setChipFilter('Hall-01', this)"><i class="fa-solid fa-location-dot"></i> Lecture Hall 01</button>
          <button class="touch-chip" onclick="setChipFilter('Hall-02', this)"><i class="fa-solid fa-location-dot"></i> Lecture Hall 02</button>
        </div>

        <!-- Meta Results & Tools Bar -->
        <div class="search-meta-bar">
          <div class="results-badge-text">
            Showing <strong id="papers-count-view">115</strong> presentations
          </div>
          <div class="search-sub-actions">
            <button class="btn-sub-tool" onclick="toggleAdvancedOptions()">
              <i class="fa-solid fa-sliders"></i> <span id="lbl-adv-toggle">Sort / More</span>
            </button>
            <button class="btn-sub-tool" onclick="resetAppFilters()">
              <i class="fa-solid fa-rotate-left"></i> Reset
            </button>
          </div>
        </div>

        <!-- Collapsible Sort & Scope Options -->
        <div class="advanced-filters-box" id="adv-filter-tray">
          <div class="adv-filter-cell">
            <label>Sort Schedule By</label>
            <select id="sel-sort" class="adv-select" onchange="runAppFilters()">
              <option value="time">Chronological Time</option>
              <option value="code-asc">Paper Code (A → Z)</option>
              <option value="code-desc">Paper Code (Z → A)</option>
              <option value="title-asc">Paper Title (A → Z)</option>
              <option value="author-asc">Author Name (A → Z)</option>
              <option value="theme">By Theme</option>
            </select>
          </div>
          <div class="adv-filter-cell">
            <label>Search Field</label>
            <select id="sel-scope" class="adv-select" onchange="runAppFilters()">
              <option value="all">All Fields</option>
              <option value="author">Author Name</option>
              <option value="title">Paper Title Only</option>
              <option value="code">Paper Code Only</option>
              <option value="keywords">Keywords / Abstract</option>
            </select>
          </div>
          <div class="adv-filter-cell">
            <label>Venue / Hall</label>
            <select id="sel-venue" class="adv-select" onchange="runAppFilters()">
              <option value="all">All Halls</option>
              <option value="MBA Auditorium">MBA Auditorium</option>
              <option value="MBA Lecture Hall-01">MBA Lecture Hall-01</option>
              <option value="MBA Lecture Hall-02">MBA Lecture Hall-02</option>
            </select>
          </div>
        </div>

      </div>

      <!-- Feed Cards Container -->
      <div id="papers-feed-container" class="app-cards-feed">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Empty Results State -->
      <div id="feed-empty-box" class="app-empty-state" style="display: none;">
        <i class="fa-solid fa-file-circle-question"></i>
        <h3>No matching presentations</h3>
        <p>Try searching by presenter surname, paper code (e.g. A1, B4), or tap a chip above.</p>
        <button class="btn-sheet-action primary" style="max-width: 200px; margin: 0 auto;" onclick="resetAppFilters()">Reset Search</button>
      </div>

    </section>

    <!-- ========================================================= -->
    <!-- SECTION 2: 3-DAY TIMELINE SCHEDULE                        -->
    <!-- ========================================================= -->
    <section id="sec-schedule" class="app-section-panel">
      
      <div style="margin-bottom: 14px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">Official Conference Flow</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">Complete sequence of ceremonies, plenaries, panels, technical sessions, and meals.</p>
      </div>

      <!-- Day Switcher Segment Control -->
      <div class="day-selector-segment">
        <button class="day-segment-btn active" onclick="switchDaySegment('day1', this)">
          <div class="ds-title">DAY 01</div>
          <div class="ds-sub">07 Oct · Wed</div>
        </button>
        <button class="day-segment-btn" onclick="switchDaySegment('day2', this)">
          <div class="ds-title">DAY 02</div>
          <div class="ds-sub">08 Oct · Thu</div>
        </button>
        <button class="day-segment-btn" onclick="switchDaySegment('day3', this)">
          <div class="ds-title">DAY 03</div>
          <div class="ds-sub">09 Oct · Fri</div>
        </button>
      </div>

      <div class="timeline-card-stream" id="timeline-stream-target">
        <!-- Rendered by JavaScript -->
      </div>

    </section>

    <!-- ========================================================= -->
    <!-- SECTION 3: 9 TECHNICAL TRACKS                             -->
    <!-- ========================================================= -->
    <section id="sec-tracks" class="app-section-panel">
      <div style="margin-bottom: 14px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">9 Parallel Technical Tracks</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">Technical presentation tracks with assigned halls, chairs, and papers.</p>
      </div>

      <div class="tracks-app-grid" id="tracks-grid-target">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- SECTION 4: 5 THEMES                                       -->
    <!-- ========================================================= -->
    <section id="sec-themes" class="app-section-panel">
      <div style="margin-bottom: 14px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">5 Thematic Clusters</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">Core academic tracks framing digital technology adoption in social work.</p>
      </div>

      <div class="tracks-app-grid" id="themes-grid-target">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ========================================================= -->
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
    </section>

    <!-- ========================================================= -->
    <!-- SECTION 6: MY PERSONAL ITINERARY                          -->
    <!-- ========================================================= -->
    <section id="sec-itinerary" class="app-section-panel">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <div>
          <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">My Saved Itinerary</h2>
          <p style="font-size: 0.85rem; color: var(--text-subtle);">Presentations bookmarked for your personal conference schedule.</p>
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn-sub-tool" onclick="window.print()"><i class="fa-solid fa-print"></i> Print</button>
          <button class="btn-sub-tool" onclick="clearAllBookmarks()"><i class="fa-regular fa-trash-can"></i> Clear</button>
        </div>
      </div>

      <div class="app-cards-feed" id="itinerary-feed-target">
        <!-- Rendered by JavaScript -->
      </div>

      <div id="itinerary-empty-prompt" class="app-empty-state" style="display: none;">
        <i class="fa-regular fa-bookmark"></i>
        <h3>No saved presentations yet</h3>
        <p>Tap the bookmark ribbon on any presentation in the Directory to add it to your schedule.</p>
        <button class="btn-sheet-action primary" style="max-width: 200px; margin: 0 auto;" onclick="switchAppTab('directory')">Browse Papers</button>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- SECTION 7: VENUE & HELPDESK                               -->
    <!-- ========================================================= -->
    <section id="sec-venue" class="app-section-panel">
      <div style="margin-bottom: 14px;">
        <h2 style="font-family: var(--font-heading); font-size: 1.4rem; color: var(--app-blue-950);">Secretariat &amp; Helpdesk</h2>
        <p style="font-size: 0.85rem; color: var(--text-subtle);">Official contact numbers for Registration, Accommodation, Transport, &amp; Venues.</p>
      </div>

      <div class="tracks-app-grid" id="helpdesk-grid-target">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Campus Directions -->
      <div style="background: #ffffff; border-radius: var(--radius-md); border: 1px solid var(--app-border); padding: 16px; margin-top: 14px; box-shadow: var(--shadow-sm);">
        <h3 style="font-family: var(--font-heading); font-size: 1.15rem; color: var(--app-blue-950); margin-bottom: 10px;">
          <i class="fa-solid fa-map-location-dot" style="color: var(--app-blue-600); margin-right: 6px;"></i> Campus Locations &amp; Transit
        </h3>
        <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.55;">
          <p style="margin-bottom: 8px;"><strong>Halls:</strong> MBA Auditorium (Main Hall), MBA Lecture Hall-01 (Track 2), MBA Lecture Hall-02 (Track 3), MBA Foyer (Registration).</p>
          <p style="margin-bottom: 8px;"><strong>Meals:</strong> University Guest House (Behind Administrative Block).</p>
          <p><strong>Transit:</strong> Shivagangotri Campus, Tholahunase, Davanagere. 10 km from Railway Station / Bus Stand on NH 48.</p>
        </div>
      </div>
    </section>

  </div>

  <!-- ========================================================= -->
  <!-- MOBILE NATIVE BOTTOM SHEET (FOR ABSTRACT DETAILS)         -->
  <!-- ========================================================= -->
  <div id="abstract-bottom-sheet" class="app-sheet-backdrop" onclick="handleBackdropClick(event)">
    <div class="app-bottom-sheet" id="sheet-modal-window">
      
      <!-- Drag Handle for Mobile -->
      <div class="sheet-handle-pill"></div>

      <!-- Sheet Top Header -->
      <div class="sheet-top-header">
        <button class="sheet-close-x" onclick="closeAbstractSheet()" title="Close">
          <i class="fa-solid fa-xmark"></i>
        </button>
        <span class="sheet-code-pill" id="sheet-code">A1</span>
        <h3 class="sheet-heading" id="sheet-title">Paper Title</h3>
      </div>

      <!-- Sheet Scrollable Body -->
      <div class="sheet-scroll-body">
        
        <!-- Slot Box -->
        <div class="sheet-slot-box">
          <div><i class="fa-regular fa-calendar-check" style="color: var(--app-blue-600);"></i> <strong id="sheet-day">Day 01 (07.10.2026)</strong></div>
          <div><i class="fa-regular fa-clock" style="color: var(--app-blue-600);"></i> <strong id="sheet-time">4:45 – 5:30 pm</strong></div>
          <div><i class="fa-solid fa-location-dot" style="color: var(--app-blue-600);"></i> <span id="sheet-venue">MBA Auditorium</span></div>
          <div><i class="fa-solid fa-user-graduate" style="color: var(--app-blue-600);"></i> <span id="sheet-chair">Chair: Committee</span></div>
        </div>

        <!-- Authors -->
        <div style="margin-bottom: 14px; padding-bottom: 12px; border-bottom: 1px solid var(--app-border);">
          <div style="font-size: 0.72rem; font-weight: 800; text-transform: uppercase; color: var(--app-blue-700); margin-bottom: 2px;">Authors &amp; Presenters</div>
          <div style="font-weight: 800; font-size: 0.98rem; color: var(--app-blue-950);" id="sheet-authors">Author Names</div>
          <div style="font-size: 0.82rem; color: var(--text-subtle); margin-top: 2px;" id="sheet-affil">Affiliation</div>
        </div>

        <!-- Abstract Body -->
        <div>
          <div style="font-size: 0.72rem; font-weight: 800; text-transform: uppercase; color: var(--app-blue-700); margin-bottom: 2px;">Peer-Reviewed Abstract</div>
          <div class="sheet-abstract-text" id="sheet-abstract-body">Abstract text...</div>
        </div>

        <!-- Keywords -->
        <div id="sheet-keywords-section" style="margin-top: 14px; padding-top: 10px; border-top: 1px dashed var(--app-border);">
          <div style="font-size: 0.72rem; font-weight: 800; text-transform: uppercase; color: var(--app-blue-700); margin-bottom: 6px;">Keywords</div>
          <div style="display: flex; flex-wrap: wrap; gap: 6px;" id="sheet-keywords-tags"></div>
        </div>

      </div>

      <!-- Sheet Sticky Footer Actions -->
      <div class="sheet-sticky-footer">
        <button class="btn-sheet-action secondary" id="btn-sheet-bookmark" onclick="toggleSheetBookmark()">
          <i class="fa-regular fa-bookmark"></i> Bookmark
        </button>
        <button class="btn-sheet-action secondary" onclick="copyCitation()">
          <i class="fa-regular fa-copy"></i> Citation
        </button>
        <button class="btn-sheet-action primary" onclick="closeAbstractSheet()">
          Done
        </button>
      </div>

    </div>
  </div>

  <!-- ========================================================= -->
  <!-- FIXED MOBILE APP BOTTOM DOCK                              -->
  <!-- ========================================================= -->
  <div class="app-bottom-dock">
    <button class="dock-tab-btn active" data-tab="directory" onclick="switchAppTab('directory')">
      <i class="fa-solid fa-magnifying-glass"></i>
      <span>Search</span>
    </button>
    <button class="dock-tab-btn" data-tab="schedule" onclick="switchAppTab('schedule')">
      <i class="fa-regular fa-calendar-check"></i>
      <span>Schedule</span>
    </button>
    <button class="dock-tab-btn" data-tab="tracks" onclick="switchAppTab('tracks')">
      <i class="fa-solid fa-network-wired"></i>
      <span>Tracks</span>
    </button>
    <button class="dock-tab-btn" data-tab="itinerary" onclick="switchAppTab('itinerary')">
      <i class="fa-regular fa-bookmark"></i>
      <span>Saved</span>
      <span class="dock-bubble-badge" id="dock-itinerary-badge" style="display:none;">0</span>
    </button>
    <button class="dock-tab-btn" data-tab="venue" onclick="switchAppTab('venue')">
      <i class="fa-solid fa-compass"></i>
      <span>Helpdesk</span>
    </button>
  </div>

  <!-- Toast Notification Popup -->
  <div class="app-toast-box" id="app-toast">
    <i class="fa-solid fa-circle-check"></i>
    <span id="toast-msg-text">Notification message</span>
  </div>

  <!-- Mobile-Friendly Footer -->
  <footer class="app-mobile-footer">
    <div class="app-shell">
      <div style="text-align: center; margin-bottom: 16px;">
        <h4 style="font-family: var(--font-heading); font-size: 1.15rem; color: #fff; margin-bottom: 4px;">ISPSW National Conference 2026</h4>
        <p style="font-size: 0.8rem; color: #94a3b8; max-width: 500px; margin: 0 auto;">Department of Studies in Social Work, Davangere University &amp; Indian Society of Professional Social Work</p>
      </div>

      <div style="background: rgba(255,255,255,0.06); padding: 12px; border-radius: var(--radius-md); text-align: center; margin-bottom: 16px; border: 1px solid rgba(56, 189, 248, 0.25);">
        <div style="color: var(--app-cyan); font-weight: 700; font-size: 0.88rem;">
          <i class="fa-solid fa-laptop-code" style="margin-right: 6px;"></i> Designed &amp; Architected by <strong>Dr. Saravana Kadirvel</strong>
        </div>
        <div style="font-size: 0.74rem; color: #94a3b8; margin-top: 2px;">Peer-Reviewed Conference Proceedings &amp; Interactive Academic Portal</div>
      </div>

      <div style="text-align: center; font-size: 0.74rem; color: #64748b;">
        &copy; 2026 Davangere University &amp; ISPSW. All rights reserved.
      </div>
    </div>
  </footer>

  <!-- EMBEDDED CONFERENCE DATA -->
  <script>
    const CONF_DB = __CONF_DB_JSON__;
  </script>

  <!-- APPLICATION LOGIC CONTROLLER -->
  <script>
    let currentAppTab = 'directory';
    let currentTimelineDay = 'day1';
    let activeQuickFilter = 'all';
    let activeSheetPaper = null;
    let savedBookmarksSet = new Set();
    let advancedTrayOpen = false;

    // Load Bookmarks from LocalStorage
    try {
      const stored = localStorage.getItem('ispsw_app_bookmarks');
      if (stored) savedBookmarksSet = new Set(JSON.parse(stored));
    } catch(e) {
      console.warn('LocalStorage error:', e);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderFeedCards();
      renderTimelineView('day1');
      renderTracksMatrix();
      renderThemesCards();
      renderDignitariesView();
      renderHelpdeskCards();
      updateBookmarkIndicators();

      // Keyboard escape
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeAbstractSheet();
      });
    });

    // App Tab Switching
    function switchAppTab(tabId) {
      currentAppTab = tabId;

      // Update Pill Tabs
      document.querySelectorAll('.app-pill-tab').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
      });

      // Update Bottom Dock Tabs
      document.querySelectorAll('.dock-tab-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
      });

      // Update Panels
      document.querySelectorAll('.app-section-panel').forEach(p => p.classList.remove('active'));
      const targetPanel = document.getElementById('sec-' + tabId);
      if (targetPanel) targetPanel.classList.add('active');

      if (tabId === 'itinerary') renderItineraryFeed();

      // Scroll smoothly to navigation on mobile
      window.scrollTo({ top: 180, behavior: 'smooth' });
    }

    // Toggle Advanced Filters Tray
    function toggleAdvancedOptions() {
      const tray = document.getElementById('adv-filter-tray');
      const lbl = document.getElementById('lbl-adv-toggle');
      if (advancedTrayOpen) {
        tray.style.display = 'none';
        advancedTrayOpen = false;
        lbl.textContent = 'Sort / More';
      } else {
        tray.style.display = 'grid';
        advancedTrayOpen = true;
        lbl.textContent = 'Hide Options';
      }
    }

    // Focus Search Input
    function focusSearchInput() {
      switchAppTab('directory');
      const input = document.getElementById('app-search-input');
      input.focus();
      input.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    let searchDebounce = null;
    function handleSearchType() {
      const input = document.getElementById('app-search-input');
      const btnX = document.getElementById('btn-clear-search-x');
      btnX.style.display = input.value.trim() ? 'flex' : 'none';

      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {
        runAppFilters();
      }, 100);
    }

    function clearSearchInput() {
      const input = document.getElementById('app-search-input');
      input.value = '';
      document.getElementById('btn-clear-search-x').style.display = 'none';
      runAppFilters();
      input.focus();
    }

    // Fast Finder in Hero
    function executeHeroFind() {
      const q = (document.getElementById('hero-quick-find').value || '').trim();
      if (!q) {
        showAppToast('Please enter an author name or paper code');
        return;
      }
      switchAppTab('directory');
      document.getElementById('app-search-input').value = q;
      document.getElementById('btn-clear-search-x').style.display = 'flex';
      runAppFilters();

      const firstCard = document.querySelector('.paper-mobile-card');
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstCard.style.outline = '3px solid var(--app-blue-600)';
        setTimeout(() => { firstCard.style.outline = 'none'; }, 2400);
        showAppToast(`Found presentations matching "${q}"`);
      } else {
        showAppToast(`No match for "${q}"`);
      }
    }

    // Quick Chip Filter
    function setChipFilter(chipVal, btnElement) {
      activeQuickFilter = chipVal;
      document.querySelectorAll('.quick-chips-scroller .touch-chip').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      runAppFilters();
    }

    // Filter Logic
    function getFilteredList() {
      const q = (document.getElementById('app-search-input').value || '').trim().toLowerCase();
      const scope = document.getElementById('sel-scope').value;
      const venue = document.getElementById('sel-venue').value;
      const sortVal = document.getElementById('sel-sort').value;

      return CONF_DB.papers.filter(p => {
        // Quick Chip Match
        if (activeQuickFilter !== 'all') {
          if (activeQuickFilter.startsWith('Day') && !p.day.includes(activeQuickFilter)) return false;
          if (activeQuickFilter.startsWith('Theme') && !p.theme.includes(activeQuickFilter)) return false;
          if (activeQuickFilter.includes('Auditorium') && !p.venue.toLowerCase().includes('auditorium')) return false;
          if (activeQuickFilter.includes('Hall-01') && !p.venue.toLowerCase().includes('01')) return false;
          if (activeQuickFilter.includes('Hall-02') && !p.venue.toLowerCase().includes('02')) return false;
        }

        // Venue Select
        if (venue !== 'all' && !p.venue.toLowerCase().includes(venue.toLowerCase())) return false;

        // Search Query
        if (q) {
          if (scope === 'author') {
            return p.authors.toLowerCase().includes(q) || (p.affiliation && p.affiliation.toLowerCase().includes(q));
          } else if (scope === 'title') {
            return p.title.toLowerCase().includes(q);
          } else if (scope === 'code') {
            return p.code.toLowerCase().includes(q);
          } else if (scope === 'keywords') {
            return p.keywords.some(k => k.toLowerCase().includes(q)) || p.abstract.toLowerCase().includes(q);
          } else {
            // All Fields
            return p.code.toLowerCase().includes(q) ||
                   p.title.toLowerCase().includes(q) ||
                   p.authors.toLowerCase().includes(q) ||
                   (p.affiliation && p.affiliation.toLowerCase().includes(q)) ||
                   p.venue.toLowerCase().includes(q) ||
                   p.time.toLowerCase().includes(q) ||
                   p.theme.toLowerCase().includes(q) ||
                   p.keywords.some(k => k.toLowerCase().includes(q)) ||
                   p.abstract.toLowerCase().includes(q);
          }
        }
        return true;
      }).sort((a, b) => {
        if (sortVal === 'code-asc') return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
        if (sortVal === 'code-desc') return b.code.localeCompare(a.code, undefined, { numeric: true, sensitivity: 'base' });
        if (sortVal === 'title-asc') return a.title.localeCompare(b.title);
        if (sortVal === 'author-asc') return a.authors.localeCompare(b.authors);
        if (sortVal === 'theme') return a.theme.localeCompare(b.theme);
        // Time order
        if (a.day !== b.day) return a.day.localeCompare(b.day);
        if (a.session_id !== b.session_id) return a.session_id.localeCompare(b.session_id);
        return a.code.localeCompare(b.code, undefined, { numeric: true, sensitivity: 'base' });
      });
    }

    function runAppFilters() {
      renderFeedCards();
    }

    function resetAppFilters() {
      document.getElementById('app-search-input').value = '';
      document.getElementById('btn-clear-search-x').style.display = 'none';
      document.getElementById('sel-scope').value = 'all';
      document.getElementById('sel-venue').value = 'all';
      document.getElementById('sel-sort').value = 'time';

      document.querySelectorAll('.quick-chips-scroller .touch-chip').forEach(b => b.classList.remove('active'));
      const allChip = document.querySelector('.quick-chips-scroller .touch-chip');
      if (allChip) allChip.classList.add('active');
      activeQuickFilter = 'all';

      runAppFilters();
      showAppToast('Filters reset to default');
    }

    // Render Cards Feed
    function renderFeedCards() {
      const container = document.getElementById('papers-feed-container');
      const emptyBox = document.getElementById('feed-empty-box');
      const countLabel = document.getElementById('papers-count-view');

      const papers = getFilteredList();
      countLabel.textContent = papers.length;

      if (papers.length === 0) {
        container.innerHTML = '';
        emptyBox.style.display = 'block';
        return;
      }
      emptyBox.style.display = 'none';

      let html = '';
      papers.forEach(p => {
        const isStarred = savedBookmarksSet.has(p.code);
        const starClass = isStarred ? 'active' : '';
        const starIco = isStarred ? 'fa-solid fa-bookmark' : 'fa-regular fa-bookmark';

        let themeTag = 'Theme';
        if (p.theme.includes('Theme 1')) themeTag = 'Theme 1 · Learning & Tech';
        else if (p.theme.includes('Theme 2')) themeTag = 'Theme 2 · AI & Interventions';
        else if (p.theme.includes('Theme 3')) themeTag = 'Theme 3 · Gender & Inclusion';
        else if (p.theme.includes('Theme 4')) themeTag = 'Theme 4 · Policy & Ethics';
        else if (p.theme.includes('Theme 5')) themeTag = 'Theme 5 · Viksit Bharat';

        html += `
          <div class="paper-mobile-card" id="card-${p.code}">
            <div>
              <div class="card-meta-header">
                <span class="paper-code-tag"><i class="fa-solid fa-hashtag"></i> ${p.code}</span>
                <span class="paper-theme-badge" title="${p.theme}">${themeTag}</span>
              </div>

              <h3 class="paper-card-title">${p.title}</h3>

              <div class="paper-card-author">
                <i class="fa-solid fa-user-pen"></i>
                <span>${p.authors}</span>
              </div>

              <div class="card-slot-strip">
                <div class="slot-cell">
                  <i class="fa-regular fa-calendar-check"></i>
                  <span>${p.day}</span>
                </div>
                <div class="slot-cell">
                  <i class="fa-regular fa-clock"></i>
                  <span><strong>${p.time}</strong></span>
                </div>
                <div class="slot-cell">
                  <i class="fa-solid fa-location-dot"></i>
                  <span>${p.venue.replace(', Davangere University', '')}</span>
                </div>
                <div class="slot-cell">
                  <i class="fa-solid fa-user-graduate"></i>
                  <span title="${p.chairperson}">Chair: ${p.chairperson ? p.chairperson.split(',')[0] : 'Committee'}</span>
                </div>
              </div>
            </div>

            <div class="card-bottom-actions">
              <button class="btn-tap-abstract" onclick="openAbstractSheet('${p.code}')">
                <i class="fa-regular fa-file-lines"></i> View Abstract &amp; Details
              </button>
              <button class="btn-tap-star ${starClass}" onclick="toggleBookmark('${p.code}')" title="Bookmark">
                <i class="${starIco}"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Render Timeline View
    function switchDaySegment(dayKey, btnElement) {
      currentTimelineDay = dayKey;
      document.querySelectorAll('.day-segment-btn').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      renderTimelineView(dayKey);
    }

    function renderTimelineView(dayKey) {
      const container = document.getElementById('timeline-stream-target');
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
          <div class="app-timeline-card ${catClass}">
            <div class="tl-header-row">
              <span class="tl-time-chip"><i class="fa-regular fa-clock"></i> ${ev.time}</span>
              <span class="tl-cat-badge">${ev.category}</span>
            </div>
            <h4 class="tl-title">${ev.event}</h4>
            ${ev.details ? `<div class="tl-details">${ev.details}</div>` : ''}
            ${ev.venue ? `<div class="tl-venue"><i class="fa-solid fa-location-dot"></i> Venue: ${ev.venue}</div>` : ''}
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Render 9 Tracks Matrix
    function renderTracksMatrix() {
      const container = document.getElementById('tracks-grid-target');
      let html = '';

      CONF_DB.technical_sessions.forEach(ts => {
        html += `
          <div class="track-tile-card">
            <div>
              <div class="track-badge-top">
                <span class="paper-code-tag">Session ${ts.session_num} · Track ${ts.track_num}</span>
                <span style="font-family: var(--font-mono); font-size: 0.78rem; font-weight: 700; color: var(--app-blue-700);">${ts.day} (${ts.date})</span>
              </div>
              <h3 class="track-title-h3">${ts.session_title}</h3>
              <ul class="track-info-list">
                <li><i class="fa-regular fa-clock"></i> <strong>Time:</strong> ${ts.time}</li>
                <li><i class="fa-solid fa-location-dot"></i> <strong>Venue:</strong> ${ts.venue}</li>
                <li><i class="fa-solid fa-user-graduate"></i> <strong>Chair:</strong> ${ts.chairperson}</li>
                ${ts.discussant ? `<li><i class="fa-solid fa-comments"></i> <strong>Discussant:</strong> ${ts.discussant}</li>` : ''}
                <li><i class="fa-solid fa-file-lines"></i> <strong>Papers:</strong> ${ts.papers.length} Contributions</li>
              </ul>
            </div>
            <button class="btn-open-track" onclick="openTrackPapers('${ts.day}', '${ts.venue}')">
              Explore Track Papers <i class="fa-solid fa-arrow-right"></i>
            </button>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function openTrackPapers(day, venue) {
      switchAppTab('directory');
      if (day.includes('01')) setChipFilter('Day 01', null);
      else if (day.includes('02')) setChipFilter('Day 02', null);
      else if (day.includes('03')) setChipFilter('Day 03', null);

      if (venue.includes('Auditorium')) {
        document.getElementById('sel-venue').value = 'MBA Auditorium';
      } else if (venue.includes('01')) {
        document.getElementById('sel-venue').value = 'MBA Lecture Hall-01';
      } else if (venue.includes('02')) {
        document.getElementById('sel-venue').value = 'MBA Lecture Hall-02';
      }
      runAppFilters();
      showAppToast(`Showing ${day} at ${venue}`);
    }

    // Render Themes Cards
    function renderThemesCards() {
      const container = document.getElementById('themes-grid-target');
      let html = '';

      CONF_DB.themes.forEach(th => {
        const count = CONF_DB.papers.filter(p => p.theme.includes(th.key)).length;
        html += `
          <div class="track-tile-card">
            <div>
              <div style="width: 44px; height: 44px; border-radius: 12px; background: var(--app-blue-50); color: var(--app-blue-700); display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-bottom: 10px;">
                <i class="fa-solid ${th.icon}"></i>
              </div>
              <span style="font-family: var(--font-mono); font-size: 0.74rem; font-weight: 800; color: var(--app-blue-700); text-transform: uppercase;">${th.id}</span>
              <h3 class="track-title-h3">${th.title}</h3>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px; line-height: 1.45;">${th.desc}</p>
            </div>
            <div style="border-top: 1px solid var(--app-border); padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-subtle);">${count} Papers</span>
              <button class="btn-open-track" onclick="filterByThemeChip('${th.key}')" style="padding: 6px 12px; height: auto;">
                Explore <i class="fa-solid fa-arrow-right"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function filterByThemeChip(themeKey) {
      switchAppTab('directory');
      setChipFilter(themeKey, null);
      showAppToast(`Filtered by ${themeKey}`);
    }

    // Render Dignitaries & Ceremonial Panels
    function renderDignitariesView() {
      const container = document.getElementById('dignitaries-shelf-target');
      let html = '';

      // Section 1: Inaugural & Keynote Luminaries
      html += `
        <div style="grid-column: 1 / -1; margin-bottom: 4px;">
          <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--app-blue-950); display: flex; align-items: center; gap: 7px;">
            <i class="fa-solid fa-ribbon" style="color: var(--app-blue-600);"></i> Inaugural Luminaries &amp; Keynote
          </h3>
        </div>
      `;

      CONF_DB.dignitaries.forEach(d => {
        const photoHtml = d.photo 
          ? `<img src="${d.photo}" alt="${d.name}">` 
          : `<div class="fallback-ico"><i class="fa-solid fa-user-tie"></i></div>`;

        html += `
          <div class="dignitary-card-mobile">
            <div class="dig-avatar-ring">
              ${photoHtml}
            </div>
            <div class="dig-details-box">
              <span class="dig-role-chip">${d.tag}</span>
              <h4>${d.name}</h4>
              <div style="font-size: 0.82rem; font-weight: 700; color: var(--app-blue-700);">${d.title}</div>
              <div class="dig-affil">${d.org}</div>
            </div>
          </div>
        `;
      });

      // Section 2: Valedictory Ceremony Panel Card
      if (CONF_DB.valedictory_info) {
        const vi = CONF_DB.valedictory_info;
        html += `
          <div style="grid-column: 1 / -1; margin-top: 18px; margin-bottom: 4px;">
            <div style="background: linear-gradient(135deg, var(--app-blue-950) 0%, var(--app-blue-900) 100%); color: #fff; border-radius: var(--radius-lg); padding: 18px; border: 1.5px solid var(--app-cyan); box-shadow: var(--shadow-card);">
              <div style="margin-bottom: 12px;">
                <span style="background: rgba(14, 165, 233, 0.25); border: 1px solid var(--app-cyan); padding: 2px 8px; border-radius: 999px; font-size: 0.68rem; font-weight: 700; text-transform: uppercase; color: var(--app-cyan);">Day 3 Ceremony</span>
                <h3 style="font-family: var(--font-heading); font-size: 1.35rem; color: #fff; margin-top: 4px;">Valedictory Function &amp; Certificate Distribution</h3>
                <div style="font-size: 0.8rem; color: var(--app-cyan-light); margin-top: 2px;">
                  <i class="fa-regular fa-clock"></i> ${vi.date} · ${vi.time} · ${vi.venue}
                </div>
              </div>

              <div style="display: grid; grid-template-columns: 1fr; gap: 10px; margin-top: 10px;">
                <div style="background: rgba(255,255,255,0.08); padding: 12px; border-radius: var(--radius-sm); border-left: 3px solid var(--app-cyan);">
                  <div style="font-size: 0.68rem; text-transform: uppercase; color: var(--app-cyan); font-weight: 700;">Presided Over By</div>
                  <strong style="font-size: 1.05rem; color: #fff;">${vi.presided_by}</strong>
                </div>
                <div style="background: rgba(255,255,255,0.08); padding: 12px; border-radius: var(--radius-sm); border-left: 3px solid #4ade80;">
                  <div style="font-size: 0.68rem; text-transform: uppercase; color: #4ade80; font-weight: 700;">Chief Guest &amp; Valedictory Address</div>
                  <strong style="font-size: 1.05rem; color: #fff;">${vi.chief_guest}</strong>
                </div>
              </div>

              <div style="margin-top: 14px;">
                <div style="font-size: 0.72rem; text-transform: uppercase; color: var(--app-cyan); font-weight: 700; margin-bottom: 6px;">Guests of Honour</div>
                <div style="display: flex; flex-direction: column; gap: 6px;">
                  ${vi.guests_of_honour.map(g => `
                    <div style="font-size: 0.82rem; color: #e2e8f0;">
                      <i class="fa-solid fa-medal" style="color: var(--app-cyan); margin-right: 5px;"></i> <strong>${g.name}</strong>, <span style="opacity: 0.8;">${g.desig}</span>
                    </div>
                  `).join('')}
                </div>
              </div>

            </div>
          </div>
        `;
      }

      // Section 3: Organizing Committee
      if (CONF_DB.organizing_committee) {
        html += `
          <div style="grid-column: 1 / -1; margin-top: 18px; margin-bottom: 4px;">
            <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--app-blue-950); display: flex; align-items: center; gap: 7px;">
              <i class="fa-solid fa-sitemap" style="color: var(--app-blue-600);"></i> Conference Organizing Committee
            </h3>
          </div>
        `;

        CONF_DB.organizing_committee.forEach(oc => {
          html += `
            <div style="background: #ffffff; border-radius: var(--radius-md); border: 1px solid var(--app-border); padding: 14px; text-align: center; border-top: 3px solid var(--app-blue-700);">
              <span class="dig-role-chip" style="margin-bottom: 2px;">${oc.role}</span>
              <h4 style="font-family: var(--font-heading); font-size: 1.05rem; color: var(--app-blue-950); margin-bottom: 2px;">${oc.name}</h4>
              <div style="font-size: 0.78rem; color: var(--text-subtle);">${oc.dept}</div>
            </div>
          `;
        });
      }

      container.innerHTML = html;
    }

    // Render Helpdesk Cards
    function renderHelpdeskCards() {
      const container = document.getElementById('helpdesk-grid-target');
      let html = '';

      CONF_DB.committee_contacts.forEach(c => {
        html += `
          <div class="track-tile-card" style="text-align: center; align-items: center;">
            <div>
              <i class="fa-solid fa-phone-volume" style="font-size: 1.4rem; color: var(--app-blue-600); margin-bottom: 6px;"></i>
              <span class="paper-code-tag" style="margin-bottom: 4px; display: inline-block;">${c.role}</span>
              <h4 style="font-family: var(--font-heading); font-size: 1.05rem; color: var(--app-blue-950); margin-bottom: 2px;">${c.name}</h4>
              <div style="font-size: 0.76rem; color: var(--text-subtle); margin-bottom: 10px;">${c.desig}</div>
            </div>
            <a href="tel:${c.phone.replace(/\\s+/g, '')}" class="btn-open-track" style="text-decoration: none; width: 100%;">
              <i class="fa-solid fa-phone"></i> ${c.phone}
            </a>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // Abstract Mobile Bottom Sheet Operations
    function openAbstractSheet(code) {
      const paper = CONF_DB.papers.find(p => p.code === code);
      if (!paper) return;

      activeSheetPaper = paper;

      document.getElementById('sheet-code').textContent = paper.code;
      document.getElementById('sheet-title').textContent = paper.title;
      document.getElementById('sheet-day').textContent = `${paper.day} (${paper.date})`;
      document.getElementById('sheet-time').textContent = paper.time;
      document.getElementById('sheet-venue').textContent = `${paper.venue} (${paper.session_title})`;
      document.getElementById('sheet-chair').textContent = paper.chairperson ? `Chair: ${paper.chairperson.split(',')[0]}` : 'Chair: Scientific Committee';
      
      document.getElementById('sheet-authors').textContent = paper.authors;
      document.getElementById('sheet-affil').textContent = paper.affiliation || 'Department of Studies in Social Work, Research Scholars & Faculty';
      
      const abstractContent = paper.abstract || 'The detailed text for this paper was accepted and published in the ISPSW 2026 Abstract Volume. Please refer to the session proceedings during the presentation.';
      document.getElementById('sheet-abstract-body').textContent = abstractContent;

      const kwBox = document.getElementById('sheet-keywords-section');
      const kwTags = document.getElementById('sheet-keywords-tags');
      if (paper.keywords && paper.keywords.length > 0) {
        kwBox.style.display = 'block';
        kwTags.innerHTML = paper.keywords.map(k => `<span class="paper-code-tag" style="font-size: 0.72rem; padding: 2px 7px;">${k}</span>`).join('');
      } else {
        kwBox.style.display = 'none';
      }

      updateSheetBookmarkBtn();

      const sheet = document.getElementById('abstract-bottom-sheet');
      sheet.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeAbstractSheet() {
      const sheet = document.getElementById('abstract-bottom-sheet');
      sheet.classList.remove('active');
      document.body.style.overflow = '';
      activeSheetPaper = null;
    }

    function handleBackdropClick(e) {
      if (e.target.id === 'abstract-bottom-sheet') {
        closeAbstractSheet();
      }
    }

    // Bookmarking Logic
    function toggleBookmark(code) {
      if (savedBookmarksSet.has(code)) {
        savedBookmarksSet.delete(code);
        showAppToast(`Removed [${code}] from your saved list`);
      } else {
        savedBookmarksSet.add(code);
        showAppToast(`Saved [${code}] to your itinerary!`);
      }

      saveBookmarks();
      renderFeedCards();
      updateBookmarkIndicators();
      if (currentAppTab === 'itinerary') renderItineraryFeed();
    }

    function toggleSheetBookmark() {
      if (!activeSheetPaper) return;
      toggleBookmark(activeSheetPaper.code);
      updateSheetBookmarkBtn();
    }

    function updateSheetBookmarkBtn() {
      if (!activeSheetPaper) return;
      const btn = document.getElementById('btn-sheet-bookmark');
      const isStarred = savedBookmarksSet.has(activeSheetPaper.code);
      if (isStarred) {
        btn.innerHTML = '<i class="fa-solid fa-bookmark" style="color: var(--app-blue-600);"></i> Saved in Itinerary';
        btn.classList.add('primary');
        btn.classList.remove('secondary');
      } else {
        btn.innerHTML = '<i class="fa-regular fa-bookmark"></i> Bookmark';
        btn.classList.remove('primary');
        btn.classList.add('secondary');
      }
    }

    function saveBookmarks() {
      try {
        localStorage.setItem('ispsw_app_bookmarks', JSON.stringify(Array.from(savedBookmarksSet)));
      } catch (e) {
        console.warn('Storage error:', e);
      }
    }

    function updateBookmarkIndicators() {
      const topBadge = document.getElementById('top-itinerary-badge');
      const dockBadge = document.getElementById('dock-itinerary-badge');
      const pillBadge = document.getElementById('pill-count-saved');
      const count = savedBookmarksSet.size;

      if (count > 0) {
        topBadge.textContent = count; topBadge.style.display = 'block';
        dockBadge.textContent = count; dockBadge.style.display = 'block';
        pillBadge.textContent = count; pillBadge.style.display = 'inline-block';
      } else {
        topBadge.style.display = 'none';
        dockBadge.style.display = 'none';
        pillBadge.style.display = 'none';
      }
    }

    function clearAllBookmarks() {
      if (confirm('Clear all saved presentations from your itinerary?')) {
        savedBookmarksSet.clear();
        saveBookmarks();
        updateBookmarkIndicators();
        renderItineraryFeed();
        renderFeedCards();
        showAppToast('Itinerary cleared');
      }
    }

    function renderItineraryFeed() {
      const container = document.getElementById('itinerary-feed-target');
      const emptyBox = document.getElementById('itinerary-empty-prompt');

      if (savedBookmarksSet.size === 0) {
        container.innerHTML = '';
        emptyBox.style.display = 'block';
        return;
      }
      emptyBox.style.display = 'none';

      const list = CONF_DB.papers.filter(p => savedBookmarksSet.has(p.code));
      let html = '';
      list.forEach(p => {
        html += `
          <div class="paper-mobile-card">
            <div>
              <div class="card-meta-header">
                <span class="paper-code-tag"><i class="fa-solid fa-bookmark"></i> ${p.code}</span>
                <span class="paper-theme-badge">${p.day}</span>
              </div>
              <h3 class="paper-card-title">${p.title}</h3>
              <div class="paper-card-author"><i class="fa-solid fa-user-pen"></i> ${p.authors}</div>
              <div class="card-slot-strip">
                <div class="slot-cell"><i class="fa-regular fa-clock"></i> <strong>${p.time}</strong></div>
                <div class="slot-cell"><i class="fa-solid fa-location-dot"></i> ${p.venue}</div>
              </div>
            </div>
            <div class="card-bottom-actions">
              <button class="btn-tap-abstract" onclick="openAbstractSheet('${p.code}')">
                <i class="fa-regular fa-file-lines"></i> View Details
              </button>
              <button class="btn-tap-star active" onclick="toggleBookmark('${p.code}')" title="Remove">
                <i class="fa-solid fa-bookmark"></i>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function copyCitation() {
      if (!activeSheetPaper) return;
      const citation = `${activeSheetPaper.authors} (2026). "${activeSheetPaper.title}". In Proceedings of the Annual National Conference of ISPSW – 2026, Davangere University, Karnataka. Paper Code: ${activeSheetPaper.code}.`;
      navigator.clipboard.writeText(citation).then(() => {
        showAppToast('Citation copied to clipboard!');
      }).catch(() => {
        showAppToast('Citation ready');
      });
    }

    // Toast
    function showAppToast(msg) {
      const toast = document.getElementById('app-toast');
      const lbl = document.getElementById('toast-msg-text');
      lbl.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2600);
    }
  </script>

</body>
</html>
'''

# Logos Injection
davangere_logo_html = f'<img src="{db["conference_meta"]["davangere_logo"]}" alt="Davangere University">' if db["conference_meta"]["davangere_logo"] else '<i class="fa-solid fa-building-columns" style="font-size: 1.2rem; color: #1e3a8a;"></i>'
ispsw_logo_html = f'<img src="{db["conference_meta"]["ispsw_logo"]}" alt="ISPSW Logo">' if db["conference_meta"]["ispsw_logo"] else '<i class="fa-solid fa-shield-halved" style="font-size: 1.2rem; color: #1e3a8a;"></i>'

final_html = html_content.replace('__DAVANGERE_LOGO_HTML__', davangere_logo_html)
final_html = final_html.replace('__ISPSW_LOGO_HTML__', ispsw_logo_html)
final_html = final_html.replace('__CONF_DB_JSON__', json_data_str)

# Write to both index.html and conference_portal.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

with open("conference_portal.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated clean, high-performance mobile-first corporate app portal!")
print(f"File size: {len(final_html)} bytes")
