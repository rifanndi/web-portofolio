code = """<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rifandi Annas S - Front-End & Full-Stack WordPress Developer</title>
    <meta name="description" content="Portofolio Interaktif Rifandi Annas S - Front-End & Full-Stack WordPress Developer (3+ Tahun Pengalaman)">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-body: #F8FAFC;
            --bg-surface: #FFFFFF;
            --bg-subtle: #F1F5F9;
            --border: #E2E8F0;
            --border-hover: #CBD5E1;
            
            --primary: #2563EB;
            --primary-hover: #1D4ED8;
            --primary-light: #EFF6FF;
            --accent-cyan: #0EA5E9;
            --accent-purple: #7C3AED;
            --accent-emerald: #10B981;
            
            --text-main: #0F172A;
            --text-muted: #475569;
            --text-light: #64748B;
            
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05);
            --shadow-lg: 0 10px 25px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.04);
            --shadow-3d: 0 8px 0 0 #1E40AF;
            --btn-3d: 0 4px 0 0 #1E3A8A;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        h1, h2, h3, h4, .font-heading {
            font-family: 'Outfit', sans-serif;
        }

        code, .font-code {
            font-family: 'Fira Code', monospace;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* 3D Interactive Buttons */
        .btn-3d {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 26px;
            font-weight: 700;
            font-size: 0.95rem;
            border-radius: 12px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.1s ease;
            user-select: none;
            border: 2px solid #1E3A8A;
            background: var(--primary);
            color: #FFFFFF;
            box-shadow: 0 4px 0 0 #1E3A8A;
            position: relative;
            top: 0;
        }

        .btn-3d:hover {
            background: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 6px 0 0 #1E3A8A;
        }

        .btn-3d:active {
            transform: translateY(4px);
            box-shadow: 0 0 0 0 #1E3A8A;
        }

        .btn-3d-secondary {
            background: #FFFFFF;
            color: var(--text-main);
            border: 2px solid var(--border-hover);
            box-shadow: 0 4px 0 0 #CBD5E1;
        }

        .btn-3d-secondary:hover {
            background: var(--bg-subtle);
            border-color: #94A3B8;
            box-shadow: 0 6px 0 0 #94A3B8;
            color: var(--primary);
        }

        .btn-3d-secondary:active {
            transform: translateY(4px);
            box-shadow: 0 0 0 0 #94A3B8;
        }

        /* Clean White Cards */
        .card-white {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            box-shadow: var(--shadow-md);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            overflow: hidden;
        }

        .card-white:hover {
            transform: translateY(-6px);
            border-color: #93C5FD;
            box-shadow: var(--shadow-lg);
        }

        /* Container & Typography */
        .container {
            max-width: 1240px;
            margin: 0 auto;
            padding: 0 24px;
        }

        .section-title {
            font-size: 2.25rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--text-main);
        }

        .section-subtitle {
            color: var(--text-muted);
            font-size: 1.05rem;
            max-width: 650px;
        }

        /* Floating Navbar */
        nav {
            position: fixed;
            top: 16px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1240px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 12px 24px;
            box-shadow: var(--shadow-md);
        }

        .nav-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .nav-logo {
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .nav-logo span {
            color: var(--primary);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 28px;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-muted);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.92rem;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        /* Language Toggle Switch */
        .lang-switch {
            display: inline-flex;
            background: var(--bg-subtle);
            border: 1px solid var(--border);
            border-radius: 30px;
            padding: 3px;
            cursor: pointer;
            user-select: none;
        }

        .lang-option {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-light);
            transition: all 0.2s ease;
        }

        .lang-option.active {
            background: var(--primary);
            color: #FFFFFF;
            box-shadow: var(--shadow-sm);
        }

        /* Code Badge & Pill */
        .code-pill {
            background: var(--primary-light);
            color: var(--primary);
            border: 1px solid #BFDBFE;
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 0.82rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        /* Interactive Filter Tab */
        .filter-tab {
            background: var(--bg-surface);
            border: 2px solid var(--border);
            color: var(--text-muted);
            padding: 10px 20px;
            border-radius: 12px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            box-shadow: 0 3px 0 0 #E2E8F0;
            position: relative;
            top: 0;
        }

        .filter-tab:hover {
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 5px 0 0 #93C5FD;
        }

        .filter-tab.active {
            background: var(--primary);
            color: #FFFFFF;
            border-color: #1E3A8A;
            box-shadow: 0 4px 0 0 #1E3A8A;
        }

        .filter-tab:active {
            transform: translateY(3px);
            box-shadow: 0 0 0 0 transparent;
        }

        /* Interactive Image Mockup Card */
        .mockup-frame {
            position: relative;
            background: #F1F5F9;
            border-bottom: 1px solid var(--border);
            padding: 20px 20px 0 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            height: 220px;
        }

        .mockup-frame img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .card-white:hover .mockup-frame img {
            transform: scale(1.06) translateY(-4px);
        }

        /* Code Terminal Widget */
        .code-widget {
            background: #0F172A;
            color: #F8FAFC;
            border-radius: 16px;
            padding: 20px;
            font-size: 0.85rem;
            box-shadow: var(--shadow-lg);
            border: 1px solid #1E293B;
        }

        .code-header {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 14px;
            border-bottom: 1px solid #334155;
            padding-bottom: 10px;
        }

        .dot { width: 10px; height: 10px; border-radius: 50%; }
        .dot-red { background: #EF4444; }
        .dot-yellow { background: #F59E0B; }
        .dot-green { background: #10B981; }

        /* Responsive Breakpoints */
        @media (max-width: 992px) {
            .hero-layout {
                grid-template-columns: 1fr !important;
                gap: 40px !important;
            }
            .section-title { font-size: 1.85rem; }
        }

        @media (max-width: 768px) {
            nav {
                width: calc(100% - 24px);
                top: 12px;
                padding: 10px 16px;
            }
            .nav-links { display: none; }
            .section-title { font-size: 1.65rem; }
            .hero-padding { padding-top: 120px !important; }
            .projects-grid {
                grid-template-columns: 1fr !important;
            }
        }
    </style>
</head>
<body>

    <!-- FLOATING NAVBAR -->
    <nav>
        <div class="nav-inner">
            <a href="#" class="nav-logo">
                <div style="width: 32px; height: 32px; background: var(--primary); color: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 1.1rem;">R</div>
                RIFANDI<span>.ANNAS</span>
            </a>
            
            <ul class="nav-links">
                <li><a href="#about" data-i18n="nav_about">Tentang</a></li>
                <li><a href="#skills" data-i18n="nav_skills">Keahlian Front-End</a></li>
                <li><a href="#portfolio" data-i18n="nav_portfolio">Portofolio Live</a></li>
                <li><a href="#contact" data-i18n="nav_contact">Kontak</a></li>
            </ul>

            <div style="display: flex; align-items: center; gap: 14px;">
                <!-- Language Toggle -->
                <div class="lang-switch" onclick="toggleLanguage()">
                    <div id="lang-id" class="lang-option active">ID</div>
                    <div id="lang-en" class="lang-option">EN</div>
                </div>

                <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d" style="padding: 8px 18px; font-size: 0.85rem;" data-i18n="btn_hire">Hubungi Saya</a>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section class="hero-padding" style="padding: 150px 0 80px 0;">
        <div class="container hero-layout" style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 48px; align-items: center;">
            <div>
                <div style="margin-bottom: 16px;">
                    <span class="code-pill">
                        <span style="color: var(--accent-emerald);">●</span> Front-End & Full-Stack WordPress Dev
                    </span>
                </div>
                
                <h1 style="font-size: 3.25rem; font-weight: 900; line-height: 1.15; color: var(--text-main); margin-bottom: 20px;">
                    <span data-i18n="hero_title1">Merancang Web Front-End</span><br>
                    <span style="color: var(--primary);" data-i18n="hero_title2">Interaktif, Cepat & Presisi.</span>
                </h1>
                
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 32px; max-width: 600px;" data-i18n="hero_desc">
                    Pengalaman 3+ tahun membangun platform B2B internasional, e-commerce WooCommerce, custom plugin WordPress, serta optimasi Core Web Vitals & Technical SEO.
                </p>

                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <a href="#portfolio" class="btn-3d" data-i18n="btn_explore">🚀 Jelajahi 20+ Projek Live</a>
                    <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d btn-3d-secondary" data-i18n="btn_consult">💬 Diskusi Projek</a>
                </div>
            </div>

            <!-- Code Terminal Widget Interactive -->
            <div>
                <div class="code-widget">
                    <div class="code-header font-code">
                        <span class="dot dot-red"></span>
                        <span class="dot dot-yellow"></span>
                        <span class="dot dot-green"></span>
                        <span style="margin-left: 8px; color: #94A3B8; font-size: 0.75rem;">developer_profile.js</span>
                    </div>
                    <pre class="font-code" style="line-height: 1.7; color: #E2E8F0;">
<span style="color: #F472B6;">const</span> <span style="color: #38BDF8;">developer</span> = {
  <span style="color: #A7F3D0;">name</span>: <span style="color: #FDE047;">'Rifandi Annas S'</span>,
  <span style="color: #A7F3D0;">role</span>: <span style="color: #FDE047;">'Front-End & WordPress Dev'</span>,
  <span style="color: #A7F3D0;">experience</span>: <span style="color: #FDE047;">'3+ Years'</span>,
  <span style="color: #A7F3D0;">techStack</span>: [
    <span style="color: #FDE047;">'JavaScript (ES6+)'</span>, <span style="color: #FDE047;">'React.js'</span>,
    <span style="color: #FDE047;">'WordPress Custom'</span>, <span style="color: #FDE047;">'CSS3/HTML5'</span>
  ],
  <span style="color: #A7F3D0;">seoTargeting</span>: <span style="color: #FDE047;">'Technical & On-Page'</span>,
  <span style="color: #A7F3D0;">status</span>: <span style="color: #34D399;">'Ready for New Projects'</span>
};

<span style="color: #F472B6;">console</span>.<span style="color: #38BDF8;">log</span>(developer.<span style="color: #38BDF8;">status</span>);
</pre>
                </div>
            </div>
        </div>
    </section>

    <!-- SKILLS & EXPERTISE SECTION -->
    <section id="skills" style="padding: 70px 0; background: var(--bg-surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
        <div class="container">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 class="section-title" data-i18n="skills_title">Keahlian Teknikal Developer</h2>
                <p class="section-subtitle" style="margin: 8px auto 0 auto;" data-i18n="skills_subtitle">Kombinasi kekuatan WordPress kustom, modern Front-End UI/UX, dan optimasi SEO terstruktur.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
                <div class="card-white" style="padding: 28px;">
                    <div style="width: 48px; height: 48px; background: var(--primary-light); color: var(--primary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; margin-bottom: 16px;">💻</div>
                    <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 10px;" data-i18n="s1_title">Front-End & UI Layout</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;" data-i18n="s1_desc">Penerapan HTML5 semantik, CSS3 modern, JavaScript, React.js, Material UI, serta pengembangan layout responsif mobile-first berpiksel presisi.</p>
                </div>

                <div class="card-white" style="padding: 28px;">
                    <div style="width: 48px; height: 48px; background: #F0FDF4; color: var(--accent-emerald); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; margin-bottom: 16px;">⚙️</div>
                    <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 10px;" data-i18n="s2_title">WordPress & Custom Plugin</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;" data-i18n="s2_desc">Kustomisasi tema & plugin WordPress, Elementor Pro Template Kit kustom, modul checkout otomatis WhatsApp, dan integrasi API sistem bisnis.</p>
                </div>

                <div class="card-white" style="padding: 28px;">
                    <div style="width: 48px; height: 48px; background: #FAF5FF; color: var(--accent-purple); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; margin-bottom: 16px;">📈</div>
                    <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 10px;" data-i18n="s3_title">Technical & On-Page SEO</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;" data-i18n="s3_desc">Riset kata kunci strategis, Yoast/Rank Math, struktur internal linking kontekstual, optimasi Core Web Vitals, dan integrasi Google Search Console.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- PORTFOLIO LIVE SECTION -->
    <section id="portfolio" style="padding: 90px 0;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 36px;">
                <h2 class="section-title" data-i18n="port_title">Portofolio Projek Website Live</h2>
                <p class="section-subtitle" style="margin: 8px auto 28px auto;" data-i18n="port_subtitle">20+ Website hasil pengerjaan nyata menggunakan asset visual dari folder gambar baru.</p>

                <!-- Filter Tabs Interaktif -->
                <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
                    <button class="filter-tab active" onclick="filterProjects('all', this)" data-i18n="filter_all">Semua Projek (20)</button>
                    <button class="filter-tab" onclick="filterProjects('b2b', this)" data-i18n="filter_b2b">B2B Export & Pabrik</button>
                    <button class="filter-tab" onclick="filterProjects('food', this)" data-i18n="filter_food">Food & Brand</button>
                    <button class="filter-tab" onclick="filterProjects('health', this)" data-i18n="filter_health">Herbal & Health</button>
                    <button class="filter-tab" onclick="filterProjects('branding', this)" data-i18n="filter_branding">Personal Branding</button>
                    <button class="filter-tab" onclick="filterProjects('ecom', this)" data-i18n="filter_ecom">E-Commerce WA</button>
                    <button class="filter-tab" onclick="filterProjects('property', this)" data-i18n="filter_property">Interior & Properti</button>
                    <button class="filter-tab" onclick="filterProjects('travel', this)" data-i18n="filter_travel">Umrah & Travel</button>
                </div>
            </div>

            <!-- PROJECTS GRID -->
            <div id="projectsGrid" class="projects-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 28px;">

                <!-- 1. Abadi Charcoal -->
                <div class="card-white project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-abadicharcoal.com.png" alt="Abadi Charcoal Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">International B2B Export</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">abadicharcoal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p1_desc">
                            Website profil B2B internasional ekspor briket kelapa berkualitas tinggi ke pasar global.
                        </p>
                        <a href="https://abadicharcoal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 2. Indonesia Briquettes Charcoal -->
                <div class="card-white project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-indonesiabriquettescharcoal.com (1).png" alt="Indonesia Briquettes Charcoal Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Global On-Page SEO</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">indonesiabriquettescharcoal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p2_desc">
                            Platform galeri manufaktur briket Indonesia teroptimasi On-Page SEO multi-negara.
                        </p>
                        <a href="https://indonesiabriquettescharcoal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 3. Indofon PVC -->
                <div class="card-white project-card" data-category="b2b property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-indofon.com.png" alt="Indofon PVC Factory Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Pabrik Manufacturing B2B</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">indofon.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p3_desc">
                            Website pabrik produsen plafon PVC terbesar dengan katalog interaktif dan jaringan distributor.
                        </p>
                        <a href="https://indofon.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 4. Maklon Mie Porang -->
                <div class="card-white project-card" data-category="b2b food">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-maklonmieporang.com.png" alt="Maklon Mie Porang Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Food Factory B2B</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">maklonmieporang.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p4_desc">
                            Layanan maklon manufaktur mie porang sehat dengan integrasi sistem penawaran cepat.
                        </p>
                        <a href="https://maklonmieporang.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 5. Coco Fiber Indonesia -->
                <div class="card-white project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-cocofiberindonesia.com.png" alt="Coco Fiber Indonesia Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Export SEO Console</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">cocofiberindonesia.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p5_desc">
                            Website ekspor sabut kelapa terstruktur Google Search Console dan optimasi kata kunci global.
                        </p>
                        <a href="https://cocofiberindonesia.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 6. Beras Porang Diet Meal -->
                <div class="card-white project-card" data-category="food">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-berasporangdietmeal.com.png" alt="Beras Porang Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Healthy Food Landing</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">berasporangdietmeal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p6_desc">
                            Landing page konversi tinggi produk beras porang diet rendah kalori dengan tampilan visual segar.
                        </p>
                        <a href="https://berasporangdietmeal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 7. Yaconis GLUKO -->
                <div class="card-white project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-yaconis.id.png" alt="Yaconis Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Herbal Brand Showcase</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">yaconis.id</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p7_desc">
                            Website produk herbal spesialis daun yakon dengan tata letak visual elegan & alur pemesanan cepat.
                        </p>
                        <a href="https://yaconis.id" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 8. Kudaplus -->
                <div class="card-white project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-kudaplus.com.png" alt="Kudaplus Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Healthy Milk Brand</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">kudaplus.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p8_desc">
                            Website official susu kuda liar premium dengan fitur edukasi manfaat kesehatan dan varian produk.
                        </p>
                        <a href="https://kudaplus.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 9. King Etawa -->
                <div class="card-white project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-kingetawa.com.png" alt="King Etawa Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Multi-Brand Showcase</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">kingetawa.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p9_desc">
                            Platform multi-brand susu etawa (Kingetawa, Etawakids, Etawamommy, Etawasure, Kalsigrow).
                        </p>
                        <a href="https://kingetawa.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 10. MasGun Personal Branding -->
                <div class="card-white project-card" data-category="branding">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-masgun.id.png" alt="MasGun Portfolio Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Personal Branding</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">masgun.id</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p10_desc">
                            Website portofolio dan personal branding profesional dengan tampilan bersih dan modern.
                        </p>
                        <a href="https://masgun.id" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 11. Toko Plafon PVC Bali -->
                <div class="card-white project-card" data-category="ecom property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-tokoplafonpvcbali.com.png" alt="Toko Plafon PVC Bali Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">E-Commerce WhatsApp</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">tokoplafonpvcbali.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p11_desc">
                            Toko online bahan plafon PVC Bali terintegrasi sistem order WhatsApp otomatis.
                        </p>
                        <a href="https://tokoplafonpvcbali.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 12. Sarana Ilmu -->
                <div class="card-white project-card" data-category="ecom">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-saranailmu.com.png" alt="Sarana Ilmu Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Educational Store</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">saranailmu.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p12_desc">
                            Website katalog toko perlengkapan edukasi dan buku dengan alur pemesanan efisien.
                        </p>
                        <a href="https://saranailmu.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 13. Probosiwi Resort -->
                <div class="card-white project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-probosiwiresort.com.png" alt="Probosiwi Resort Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Property & Booking</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">probosiwiresort.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p13_desc">
                            Website villa & resort eksklusif dengan sistem reservasi online dan galeri visual memukau.
                        </p>
                        <a href="https://probosiwiresort.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 14. Plafindo -->
                <div class="card-white project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-plafindo.com.png" alt="Plafindo Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Interior Service</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">plafindo.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p14_desc">
                            Penyedia jasa pemasangan plafon PVC profesional dengan kalkulator estimasi biaya.
                        </p>
                        <a href="https://plafindo.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 15. Fonda Plafon -->
                <div class="card-white project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-fondaplafon.com.png" alt="Fonda Plafon Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Interior Contractor</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">fondaplafon.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p15_desc">
                            Web layanan pemasangan interior plafon dengan fitur portofolio proyek terstruktur.
                        </p>
                        <a href="https://fondaplafon.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 16. Pasang Plafon PVC Jogja -->
                <div class="card-white project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-pasangplafonpvcjogja.com.png" alt="Pasang Plafon PVC Jogja Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Local Service SEO</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">pasangplafonpvcjogja.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p16_desc">
                            Website jasa lokal teroptimasi kata kunci wilayah Jogja & Jateng.
                        </p>
                        <a href="https://pasangplafonpvcjogja.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 17. Romani Umroh Jogja -->
                <div class="card-white project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romaniumrohjogja.com.png" alt="Romani Umroh Jogja Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Umrah & Travel Agency</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romaniumrohjogja.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p17_desc">
                            Platform agen travel umroh resmi cabang Jogja dengan pilihan paket keberangkatan lengkap.
                        </p>
                        <a href="https://romaniumrohjogja.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 18. Romani Travel Jakarta -->
                <div class="card-white project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romanitraveljakarta.com.png" alt="Romani Travel Jakarta Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Umrah & Travel Agency</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romanitraveljakarta.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p18_desc">
                            Portal informasi dan pendaftaran paket haji & umroh terpercaya area Jakarta.
                        </p>
                        <a href="https://romanitraveljakarta.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 19. Royal Madina Umroh -->
                <div class="card-white project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-royalmadinaumroh.com.png" alt="Royal Madina Umroh Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">VIP Hajj & Umrah Tour</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">royalmadinaumroh.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p19_desc">
                            Website travel haji plus & umroh vip dengan tampilan mewah dan itinerary terstruktur.
                        </p>
                        <a href="https://royalmadinaumroh.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

                <!-- 20. Romani Travel International -->
                <div class="card-white project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romanitravel.com.png" alt="Romani Travel Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="code-pill" style="margin-bottom: 10px; font-size: 0.75rem;">Global Travel Agency</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romanitravel.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;" data-i18n="p20_desc">
                            Portal utama agen perjalanan internasional & umrah terintegrasi layanan bantuan 24/7.
                        </p>
                        <a href="https://romanitravel.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;" data-i18n="btn_visit">Kunjungi Website Live ↗</a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer id="contact" style="padding: 60px 0 30px 0; background: var(--bg-surface); border-top: 1px solid var(--border);">
        <div class="container" style="text-align: center;">
            <h2 style="font-size: 2rem; font-weight: 900; margin-bottom: 8px; color: var(--text-main);">RIFANDI ANNAS S</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px; font-size: 1.05rem;" data-i18n="footer_subtitle">Front-End & Full-Stack WordPress Developer | Yogyakarta, Indonesia</p>
            
            <div style="display: flex; justify-content: center; gap: 16px; margin-bottom: 32px; flex-wrap: wrap;">
                <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d">📱 WhatsApp: 085842754076</a>
                <a href="mailto:Rifandiannas@gmail.com" class="btn-3d btn-3d-secondary">✉️ Email: Rifandiannas@gmail.com</a>
            </div>

            <p style="color: var(--text-light); font-size: 0.88rem;">&copy; 2026 Rifandi Annas S. Built with modern white responsive layout.</p>
        </div>
    </footer>

    <!-- I18N DICTIONARY & FILTER INTERACTIVE JS -->
    <script>
        const i18n = {
            id: {
                nav_about: "Tentang",
                nav_skills: "Keahlian Front-End",
                nav_portfolio: "Portofolio Live",
                nav_contact: "Kontak",
                btn_hire: "Hubungi Saya",
                hero_title1: "Merancang Web Front-End",
                hero_title2: "Interaktif, Cepat & Presisi.",
                hero_desc: "Pengalaman 3+ tahun membangun platform B2B internasional, e-commerce WooCommerce, custom plugin WordPress, serta optimasi Core Web Vitals & Technical SEO.",
                btn_explore: "🚀 Jelajahi 20+ Projek Live",
                btn_consult: "💬 Diskusi Projek",
                skills_title: "Keahlian Teknikal Developer",
                skills_subtitle: "Kombinasi kekuatan WordPress kustom, modern Front-End UI/UX, dan optimasi SEO terstruktur.",
                s1_title: "Front-End & UI Layout",
                s1_desc: "Penerapan HTML5 semantik, CSS3 modern, JavaScript, React.js, Material UI, serta pengembangan layout responsif mobile-first berpiksel presisi.",
                s2_title: "WordPress & Custom Plugin",
                s2_desc: "Kustomisasi tema & plugin WordPress, Elementor Pro Template Kit kustom, modul checkout otomatis WhatsApp, dan integrasi API sistem bisnis.",
                s3_title: "Technical & On-Page SEO",
                s3_desc: "Riset kata kunci strategis, Yoast/Rank Math, struktur internal linking kontekstual, optimasi Core Web Vitals, dan integrasi Google Search Console.",
                port_title: "Portofolio Projek Website Live",
                port_subtitle: "20+ Website hasil pengerjaan nyata menggunakan asset visual dari folder gambar baru.",
                filter_all: "Semua Projek (20)",
                filter_b2b: "B2B Export & Pabrik",
                filter_food: "Food & Brand",
                filter_health: "Herbal & Health",
                filter_branding: "Personal Branding",
                filter_ecom: "E-Commerce WA",
                filter_property: "Interior & Properti",
                filter_travel: "Umrah & Travel",
                btn_visit: "Kunjungi Website Live ↗",
                p1_desc: "Website profil B2B internasional ekspor briket kelapa berkualitas tinggi ke pasar global.",
                p2_desc: "Platform galeri manufaktur briket Indonesia teroptimasi On-Page SEO multi-negara.",
                p3_desc: "Website pabrik produsen plafon PVC terbesar dengan katalog interaktif dan jaringan distributor.",
                p4_desc: "Layanan maklon manufaktur mie porang sehat dengan integrasi sistem penawaran cepat.",
                p5_desc: "Website ekspor sabut kelapa terstruktur Google Search Console dan optimasi kata kunci global.",
                p6_desc: "Landing page konversi tinggi produk beras porang diet rendah kalori dengan tampilan visual segar.",
                p7_desc: "Website produk herbal spesialis daun yakon dengan tata letak visual elegan & alur pemesanan cepat.",
                p8_desc: "Website official susu kuda liar premium dengan fitur edukasi manfaat kesehatan dan varian produk.",
                p9_desc: "Platform multi-brand susu etawa (Kingetawa, Etawakids, Etawamommy, Etawasure, Kalsigrow).",
                p10_desc: "Website portofolio dan personal branding profesional dengan tampilan bersih dan modern.",
                p11_desc: "Toko online bahan plafon PVC Bali terintegrasi sistem order WhatsApp otomatis.",
                p12_desc: "Website katalog toko perlengkapan edukasi dan buku dengan alur pemesanan efisien.",
                p13_desc: "Website villa & resort eksklusif dengan sistem reservasi online dan galeri visual memukau.",
                p14_desc: "Penyedia jasa pemasangan plafon PVC profesional dengan kalkulator estimasi biaya.",
                p15_desc: "Web layanan pemasangan interior plafon dengan fitur portofolio proyek terstruktur.",
                p16_desc: "Website jasa lokal teroptimasi kata kunci wilayah Jogja & Jateng.",
                p17_desc: "Platform agen travel umroh resmi cabang Jogja dengan pilihan paket keberangkatan lengkap.",
                p18_desc: "Portal informasi dan pendaftaran paket haji & umroh terpercaya area Jakarta.",
                p19_desc: "Website travel haji plus & umroh vip dengan tampilan mewah dan itinerary terstruktur.",
                p20_desc: "Portal utama agen perjalanan internasional & umrah terintegrasi layanan bantuan 24/7.",
                footer_subtitle: "Front-End & Full-Stack WordPress Developer | Yogyakarta, Indonesia"
            },
            en: {
                nav_about: "About",
                nav_skills: "Front-End Skills",
                nav_portfolio: "Live Portfolio",
                nav_contact: "Contact",
                btn_hire: "Hire Me",
                hero_title1: "Engineering Interactive,",
                hero_title2: "Fast & Precise Front-End Web.",
                hero_desc: "3+ years of experience engineering international B2B platforms, WooCommerce stores, custom WordPress plugins, and Technical SEO / Core Web Vitals optimization.",
                btn_explore: "🚀 Explore 20+ Live Projects",
                btn_consult: "💬 Project Discussion",
                skills_title: "Technical Developer Skills",
                skills_subtitle: "Combining custom WordPress power, modern Front-End UI/UX, and structured SEO optimization.",
                s1_title: "Front-End & UI Layout",
                s1_desc: "Semantic HTML5, modern CSS3, JavaScript, React.js, Material UI, and pixel-perfect mobile-first responsive design.",
                s2_title: "WordPress & Custom Plugin",
                s2_desc: "Custom WordPress themes & plugins, bespoke Elementor Pro template kits, automated WhatsApp checkout modules, and business API integrations.",
                s3_title: "Technical & On-Page SEO",
                s3_desc: "Strategic keyword targeting, Yoast/Rank Math setup, contextual internal linking, Core Web Vitals optimization, and Google Search Console integration.",
                port_title: "Live Web Projects Portfolio",
                port_subtitle: "20+ Live websites crafted with visual assets from the new image folder.",
                filter_all: "All Projects (20)",
                filter_b2b: "B2B Export & Factory",
                filter_food: "Food & Brand",
                filter_health: "Herbal & Health",
                filter_branding: "Personal Branding",
                filter_ecom: "E-Commerce WA",
                filter_property: "Interior & Property",
                filter_travel: "Umrah & Travel",
                btn_visit: "Visit Live Website ↗",
                p1_desc: "International B2B profile site exporting premium coconut charcoal briquettes globally.",
                p2_desc: "Indonesian charcoal manufacturing gallery platform optimized for multi-country On-Page SEO.",
                p3_desc: "Largest PVC ceiling manufacturer website featuring interactive product catalogs & distributor networks.",
                p4_desc: "B2B manufacturing inquiry service for healthy porang noodles with rapid quotation systems.",
                p5_desc: "Coconut fiber export site structured for Google Search Console and global search terms.",
                p6_desc: "High-converting landing page for low-calorie porang diet rice with vibrant visual layouts.",
                p7_desc: "Herbal product showcase for Yacon leaves featuring elegant layouts & direct ordering funnels.",
                p8_desc: "Official website for premium wild horse milk featuring health education & product showcases.",
                p9_desc: "Multi-brand goat milk platform (Kingetawa, Etawakids, Etawamommy, Etawasure, Kalsigrow).",
                p10_desc: "Professional portfolio and personal branding website with a sleek white modern look.",
                p11_desc: "Online PVC ceiling store in Bali integrated with automated WhatsApp ordering.",
                p12_desc: "Educational supply store catalog site engineered for rapid purchasing flow.",
                p13_desc: "Exclusive villa & resort website featuring online reservation & stunning visual galleries.",
                p14_desc: "Professional PVC ceiling installation service provider with cost estimation calculator.",
                p15_desc: "Interior ceiling installation service website featuring structured project portfolio.",
                p16_desc: "Local service website optimized for regional target keywords in Jogja & Central Java.",
                p17_desc: "Official Umrah travel agency platform (Jogja Branch) with complete departure package options.",
                p18_desc: "Trusted Hajj & Umrah package registration and info portal for Jakarta area.",
                p19_desc: "VIP Hajj & Umrah travel website featuring luxury design and structured itineraries.",
                p20_desc: "Main portal for international travel & Umrah agency integrated with 24/7 support.",
                footer_subtitle: "Front-End & Full-Stack WordPress Developer | Yogyakarta, Indonesia"
            }
        };

        let currentLang = 'id';

        function toggleLanguage() {
            currentLang = currentLang === 'id' ? 'en' : 'id';
            
            document.getElementById('lang-id').classList.toggle('active', currentLang === 'id');
            document.getElementById('lang-en').classList.toggle('active', currentLang === 'en');

            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (i18n[currentLang][key]) {
                    el.textContent = i18n[currentLang][key];
                }
            });
        }

        function filterProjects(category, btnEl) {
            document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('active'));
            btnEl.classList.add('active');

            const cards = document.querySelectorAll('.project-card');
            cards.forEach(card => {
                if (category === 'all') {
                    card.style.display = 'block';
                } else {
                    const cats = card.getAttribute('data-category').split(' ');
                    if (cats.includes(category)) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                }
            });
        }
    </script>
</body>
</html>
"""
with open(r"e:\web-portofolio\index.html", "w", encoding="utf-8") as f:
    f.write(code)
print("Successfully updated white responsive portfolio!")