import os

html_code = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Rifandi Annas S | Full-Stack WordPress & Front-End Developer</title>
    <meta name="description" content="Portfolio of Rifandi Annas S - Full-Stack WordPress & Front-End Developer with 3+ years experience engineering high-performance web applications and e-commerce platforms.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-body: #FAFAFD;
            --bg-surface: #FFFFFF;
            --bg-subtle: #F4F4F8;
            --border: #E4E4EE;
            --border-hover: #CBD5E1;
            
            /* Vibrant Modern Multi-Color Accents (Inspired by Canva PDF) */
            --color-blue: #004AAC;
            --color-purple: #8B5CF6;
            --color-pink: #EC4899;
            --color-amber: #FAB03B;
            --color-emerald: #009145;
            --color-cyan: #178AB9;
            --color-orange: #F15924;
            
            --text-main: #0F172A;
            --text-muted: #475569;
            --text-light: #64748B;
            
            --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.06);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.05);
            --shadow-lg: 0 10px 25px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.05);
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
            line-height: 1.65;
            overflow-x: hidden;
        }

        /* 3D Modern Box Buttons without Emoticons */
        .btn-3d {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 13px 28px;
            font-weight: 700;
            font-size: 0.95rem;
            border-radius: 12px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.15s ease;
            user-select: none;
            border: 2px solid #002D6B;
            background: var(--color-blue);
            color: #FFFFFF;
            box-shadow: 0 4px 0 0 #002D6B;
            position: relative;
            top: 0;
        }

        .btn-3d:hover {
            background: #1A5BB8;
            transform: translateY(-2px);
            box-shadow: 0 6px 0 0 #002D6B;
        }

        .btn-3d:active {
            transform: translateY(4px);
            box-shadow: 0 0 0 0 #002D6B;
        }

        .btn-3d-purple {
            background: var(--color-purple);
            border-color: #5B21B6;
            box-shadow: 0 4px 0 0 #5B21B6;
        }
        .btn-3d-purple:hover {
            background: #7C3AED;
            box-shadow: 0 6px 0 0 #5B21B6;
        }
        .btn-3d-purple:active {
            box-shadow: 0 0 0 0 #5B21B6;
        }

        .btn-3d-secondary {
            background: #FFFFFF;
            color: var(--text-main);
            border: 2px solid var(--border-hover);
            box-shadow: 0 4px 0 0 #94A3B8;
        }

        .btn-3d-secondary:hover {
            background: var(--bg-subtle);
            border-color: #64748B;
            box-shadow: 0 6px 0 0 #64748B;
            color: var(--color-blue);
        }

        .btn-3d-secondary:active {
            transform: translateY(4px);
            box-shadow: 0 0 0 0 #64748B;
        }

        /* Multi-Color Accent Cards (3D Box Style) */
        .card-3d {
            background: var(--bg-surface);
            border: 2px solid var(--border);
            border-radius: 20px;
            box-shadow: 0 8px 0 0 #E2E8F0;
            transition: all 0.25s ease;
            overflow: hidden;
            position: relative;
            top: 0;
        }

        .card-3d:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 0 0 #CBD5E1;
            border-color: #94A3B8;
        }

        /* Color accent bars for cards */
        .card-accent-blue { border-top: 6px solid var(--color-blue); }
        .card-accent-purple { border-top: 6px solid var(--color-purple); }
        .card-accent-pink { border-top: 6px solid var(--color-pink); }
        .card-accent-emerald { border-top: 6px solid var(--color-emerald); }
        .card-accent-amber { border-top: 6px solid var(--color-amber); }
        .card-accent-cyan { border-top: 6px solid var(--color-cyan); }
        .card-accent-orange { border-top: 6px solid var(--color-orange); }

        /* Container */
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

        /* Floating Clean Header */
        nav {
            position: fixed;
            top: 16px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1240px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(16px);
            border: 2px solid var(--border);
            border-radius: 16px;
            padding: 12px 24px;
            box-shadow: 0 4px 0 0 #E2E8F0;
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
            gap: 10px;
        }

        .logo-box {
            width: 34px;
            height: 34px;
            background: linear-gradient(135deg, var(--color-blue), var(--color-purple));
            color: white;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 1.1rem;
            box-shadow: 0 2px 0 0 #002D6B;
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
            font-weight: 700;
            font-size: 0.92rem;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: var(--color-blue);
        }

        /* Badge Pills without Emoticons */
        .pill-tag {
            background: #EFF6FF;
            color: var(--color-blue);
            border: 1.5px solid #BFDBFE;
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 0.82rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        /* Interactive Filter Tabs */
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
            border-color: var(--color-blue);
            color: var(--color-blue);
            transform: translateY(-2px);
            box-shadow: 0 5px 0 0 #93C5FD;
        }

        .filter-tab.active {
            background: var(--color-blue);
            color: #FFFFFF;
            border-color: #002D6B;
            box-shadow: 0 4px 0 0 #002D6B;
        }

        .filter-tab:active {
            transform: translateY(3px);
            box-shadow: 0 0 0 0 transparent;
        }

        /* Image Mockup Frame */
        .mockup-frame {
            position: relative;
            background: #F1F5F9;
            border-bottom: 2px solid var(--border);
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

        .card-3d:hover .mockup-frame img {
            transform: scale(1.06) translateY(-4px);
        }

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
                <div class="logo-box">R</div>
                RIFANDI<span style="color: var(--color-blue);">.ANNAS</span>
            </a>
            
            <ul class="nav-links">
                <li><a href="#summary">Summary</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#portfolio">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <div style="display: flex; align-items: center; gap: 14px;">
                <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d" style="padding: 8px 18px; font-size: 0.85rem;">Contact Me</a>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section class="hero-padding" style="padding: 150px 0 80px 0;">
        <div class="container hero-layout" style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 48px; align-items: center;">
            <div>
                <div style="margin-bottom: 16px;">
                    <span class="pill-tag">
                        <span style="color: var(--color-emerald); font-weight: 900;">●</span> Full-Stack WordPress & Front-End Developer
                    </span>
                </div>
                
                <h1 style="font-size: 3.25rem; font-weight: 900; line-height: 1.15; color: var(--text-main); margin-bottom: 20px;">
                    Building High-Performance Web &<br>
                    <span style="color: var(--color-blue);">Optimized E-Commerce Solutions</span>
                </h1>
                
                <p style="color: var(--text-muted); font-size: 1.08rem; margin-bottom: 32px; max-width: 600px;">
                    3+ years of experience engineering end-to-end web applications, custom WordPress themes/plugins, and Core Web Vitals optimizations. Proven track record in architecting B2B corporate platforms, global export portals, and WooCommerce online stores.
                </p>

                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <a href="#portfolio" class="btn-3d">Explore Live Projects</a>
                    <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d btn-3d-secondary">Get in Touch</a>
                </div>
            </div>

            <!-- 3D Stat Box Cluster (Multi-Color PDF Accent) -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div class="card-3d card-accent-blue" style="padding: 24px;">
                    <div style="font-size: 2.75rem; font-weight: 900; color: var(--color-blue); font-family: 'Outfit';">3+</div>
                    <div style="font-weight: 800; font-size: 1rem; color: var(--text-main); margin-top: 4px;">Years Experience</div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 4px;">Full-Stack WordPress & Front-End</div>
                </div>

                <div class="card-3d card-accent-purple" style="padding: 24px;">
                    <div style="font-size: 2.75rem; font-weight: 900; color: var(--color-purple); font-family: 'Outfit';">20+</div>
                    <div style="font-weight: 800; font-size: 1rem; color: var(--text-main); margin-top: 4px;">Live Web Projects</div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 4px;">B2B, Export & E-Commerce</div>
                </div>

                <div class="card-3d card-accent-orange" style="padding: 24px;">
                    <div style="font-size: 2.75rem; font-weight: 900; color: var(--color-orange); font-family: 'Outfit';">100%</div>
                    <div style="font-weight: 800; font-size: 1rem; color: var(--text-main); margin-top: 4px;">Responsive Layouts</div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 4px;">Pixel-Perfect Scaling</div>
                </div>

                <div class="card-3d card-accent-emerald" style="padding: 24px;">
                    <div style="font-size: 2.75rem; font-weight: 900; color: var(--color-emerald); font-family: 'Outfit';">SEO</div>
                    <div style="font-weight: 800; font-size: 1rem; color: var(--text-main); margin-top: 4px;">Technical & On-Page</div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 4px;">Console Indexed & Ranked</div>
                </div>
            </div>
        </div>
    </section>

    <!-- EXECUTIVE SUMMARY SECTION -->
    <section id="summary" style="padding: 70px 0; background: var(--bg-surface); border-top: 2px solid var(--border); border-bottom: 2px solid var(--border);">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto; text-align: center;">
                <span class="pill-tag" style="margin-bottom: 16px;">Executive Summary</span>
                <h2 class="section-title" style="margin-bottom: 20px;">Bridging Technical Precision & Business Impact</h2>
                <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.8;">
                    Full-Stack WordPress & Front-End Developer with over 3 years of experience engineering end-to-end web applications, custom WordPress themes/plugins, and Core Web Vitals optimizations. Proven track record in managing and architecting B2B corporate platforms, global export portals, and WooCommerce online stores by seamlessly combining WordPress expertise with modern front-end technologies (React.js, Material UI, JavaScript). Integrates Technical SEO strategies, Google Search Console analytics, and AI/LLM workflows to improve operational efficiency, search performance, and business conversion rates globally.
                </p>
            </div>
        </div>
    </section>

    <!-- TECHNICAL SKILLS SECTION -->
    <section id="skills" style="padding: 90px 0;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 48px;">
                <h2 class="section-title">Technical Skills & Expertise</h2>
                <p class="section-subtitle" style="margin: 8px auto 0 auto;">Specializing in modern web development, WordPress architecture, and data-driven SEO.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 24px;">
                
                <div class="card-3d card-accent-blue" style="padding: 28px;">
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--color-blue); margin-bottom: 12px;">Core & Front-End</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;">
                        HTML5, CSS3, JavaScript (ES6+), React.js, Material UI, Mobile-First Responsive Layouts, Custom CSS/JS Animations.
                    </p>
                </div>

                <div class="card-3d card-accent-purple" style="padding: 28px;">
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--color-purple); margin-bottom: 12px;">WordPress Ecosystem</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;">
                        Theme & Plugin Customization, Custom Post Types (CPT), Elementor Pro Template Kits, Custom Checkout Flows, WooCommerce Modifications.
                    </p>
                </div>

                <div class="card-3d card-accent-orange" style="padding: 28px;">
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--color-orange); margin-bottom: 12px;">SEO & Performance</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;">
                        Technical & On-Page SEO, Strategic Keyword Targeting, Yoast / Rank Math Setup, Core Web Vitals, Google Search Console Optimization.
                    </p>
                </div>

                <div class="card-3d card-accent-emerald" style="padding: 28px;">
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--color-emerald); margin-bottom: 12px;">Conversion & API</h3>
                    <p style="color: var(--text-muted); font-size: 0.92rem;">
                        Direct WhatsApp Order Systems, Custom Forms, API Integrations, Data Analytics, AI/LLM Workflow Optimization.
                    </p>
                </div>

            </div>
        </div>
    </section>

    <!-- PORTFOLIO PROJECTS SECTION -->
    <section id="portfolio" style="padding: 90px 0; background: var(--bg-surface); border-top: 2px solid var(--border);">
        <div class="container">
            <div style="text-align: center; margin-bottom: 36px;">
                <h2 class="section-title">Featured Live Web Projects</h2>
                <p class="section-subtitle" style="margin: 8px auto 28px auto;">20 Live websites engineered with clean architecture, high speed, and search optimization.</p>

                <!-- Filter Tabs -->
                <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
                    <button class="filter-tab active" onclick="filterProjects('all', this)">All Projects (20)</button>
                    <button class="filter-tab" onclick="filterProjects('b2b', this)">B2B & Export</button>
                    <button class="filter-tab" onclick="filterProjects('factory', this)">Factory & Industrial</button>
                    <button class="filter-tab" onclick="filterProjects('food', this)">Food & Brand</button>
                    <button class="filter-tab" onclick="filterProjects('health', this)">Herbal & Health</button>
                    <button class="filter-tab" onclick="filterProjects('branding', this)">Personal Branding</button>
                    <button class="filter-tab" onclick="filterProjects('ecom', this)">E-Commerce WA</button>
                    <button class="filter-tab" onclick="filterProjects('property', this)">Interior & Property</button>
                    <button class="filter-tab" onclick="filterProjects('travel', this)">Umrah & Travel</button>
                </div>
            </div>

            <!-- PROJECTS GRID -->
            <div id="projectsGrid" class="projects-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 28px;">

                <!-- 1. Abadi Charcoal -->
                <div class="card-3d card-accent-blue project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-abadicharcoal.com.png" alt="Abadi Charcoal Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">International B2B</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">abadicharcoal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            B2B company profile website showcasing premium coconut charcoal briquettes for international export markets.
                        </p>
                        <a href="https://abadicharcoal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 2. Indonesia Briquettes Charcoal -->
                <div class="card-3d card-accent-blue project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-indonesiabriquettescharcoal.com (1).png" alt="Indonesia Briquettes Charcoal Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Global On-Page SEO</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">indonesiabriquettescharcoal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Indonesian charcoal manufacturing gallery platform optimized for multi-country global search visibility.
                        </p>
                        <a href="https://indonesiabriquettescharcoal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 3. Indofon PVC -->
                <div class="card-3d card-accent-purple project-card" data-category="factory property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-indofon.com.png" alt="Indofon PVC Factory Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Factory & Industrial</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">indofon.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Enterprise-level website for Indonesia's premier PVC ceiling manufacturer featuring interactive product catalogs.
                        </p>
                        <a href="https://indofon.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 4. Maklon Mie Porang -->
                <div class="card-3d card-accent-purple project-card" data-category="factory food">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-maklonmieporang.com.png" alt="Maklon Mie Porang Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Food Factory B2B</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">maklonmieporang.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            B2B manufacturing inquiry service for healthy porang noodle white-labeling with fast quotation integration.
                        </p>
                        <a href="https://maklonmieporang.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 5. Coco Fiber Indonesia -->
                <div class="card-3d card-accent-blue project-card" data-category="b2b">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-cocofiberindonesia.com.png" alt="Coco Fiber Indonesia Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Global Export Portal</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">cocofiberindonesia.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Global export portal for coconut fiber and processed products, fully indexed and structured for Search Console.
                        </p>
                        <a href="https://cocofiberindonesia.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 6. Beras Porang Diet Meal -->
                <div class="card-3d card-accent-amber project-card" data-category="food">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-berasporangdietmeal.com.png" alt="Beras Porang Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Healthy Food Brand</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">berasporangdietmeal.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            High-converting sales page for healthy porang rice diet products featuring clean nutritional layouts.
                        </p>
                        <a href="https://berasporangdietmeal.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 7. Yaconis GLUKO -->
                <div class="card-3d card-accent-emerald project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-yaconis.id.png" alt="Yaconis Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Herbal Product Brand</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">yaconis.id</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Herbal product showcase for Yacon leaves with elegant layout and direct customer order funnels.
                        </p>
                        <a href="https://yaconis.id" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 8. Kudaplus -->
                <div class="card-3d card-accent-emerald project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-kudaplus.com.png" alt="Kudaplus Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Healthy Milk Showcase</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">kudaplus.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Official digital platform for wild horse milk with health benefit education features.
                        </p>
                        <a href="https://kudaplus.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 9. King Etawa -->
                <div class="card-3d card-accent-emerald project-card" data-category="health">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-kingetawa.com.png" alt="King Etawa Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Multi-Brand Ecosystem</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">kingetawa.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Multi-brand ecosystem for premium goat milk products (Kingetawa, Etawakids, Etawamommy, Etawasure, Kalsigrow).
                        </p>
                        <a href="https://kingetawa.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 10. MasGun Personal Branding -->
                <div class="card-3d card-accent-pink project-card" data-category="branding">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-masgun.id.png" alt="MasGun Portfolio Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Personal Branding</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">masgun.id</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Sleek personal branding website designed for executive showcase and community engagement.
                        </p>
                        <a href="https://masgun.id" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 11. Toko Plafon PVC Bali -->
                <div class="card-3d card-accent-amber project-card" data-category="ecom property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-tokoplafonpvcbali.com.png" alt="Toko Plafon PVC Bali Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">WhatsApp Checkout E-Com</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">tokoplafonpvcbali.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Online building materials store featuring automated WhatsApp checkout and variation catalogs.
                        </p>
                        <a href="https://tokoplafonpvcbali.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 12. Sarana Ilmu -->
                <div class="card-3d card-accent-amber project-card" data-category="ecom">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-saranailmu.com.png" alt="Sarana Ilmu Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Educational Store</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">saranailmu.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Educational supply store catalog website engineered for rapid purchasing flow.
                        </p>
                        <a href="https://saranailmu.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 13. Probosiwi Resort -->
                <div class="card-3d card-accent-cyan project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-probosiwiresort.com.png" alt="Probosiwi Resort Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Resort Booking Site</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">probosiwiresort.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Villa & resort presentation site with direct online booking features and stunning visual galleries.
                        </p>
                        <a href="https://probosiwiresort.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 14. Plafindo -->
                <div class="card-3d card-accent-cyan project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-plafindo.com.png" alt="Plafindo Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Interior Contracting</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">plafindo.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Professional PVC ceiling installation contracting service with cost estimation calculators.
                        </p>
                        <a href="https://plafindo.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 15. Fonda Plafon -->
                <div class="card-3d card-accent-cyan project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-fondaplafon.com.png" alt="Fonda Plafon Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Interior Finishing</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">fondaplafon.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Property interior finishing portfolio site with structured material catalogs.
                        </p>
                        <a href="https://fondaplafon.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 16. Pasang Plafon PVC Jogja -->
                <div class="card-3d card-accent-cyan project-card" data-category="property">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-pasangplafonpvcjogja.com.png" alt="Pasang Plafon PVC Jogja Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Local Service SEO</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">pasangplafonpvcjogja.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Local contractor service landing page targeting regional keywords in Jogja & Central Java.
                        </p>
                        <a href="https://pasangplafonpvcjogja.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 17. Romani Umroh Jogja -->
                <div class="card-3d card-accent-purple project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romaniumrohjogja.com.png" alt="Romani Umroh Jogja Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Umrah & Travel Agency</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romaniumrohjogja.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Official branch portal for Umrah & Hajj travel packages featuring complete departure schedules.
                        </p>
                        <a href="https://romaniumrohjogja.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 18. Romani Travel Jakarta -->
                <div class="card-3d card-accent-purple project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romanitraveljakarta.com.png" alt="Romani Travel Jakarta Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Umrah & Travel Agency</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romanitraveljakarta.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Capital city registration portal for pilgrimage packages with direct customer assistance.
                        </p>
                        <a href="https://romanitraveljakarta.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 19. Royal Madina Umroh -->
                <div class="card-3d card-accent-purple project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-royalmadinaumroh.com.png" alt="Royal Madina Umroh Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">VIP Umrah Tour</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">royalmadinaumroh.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            VIP Umrah & Hajj Tour platform featuring luxury itineraries and package comparison layouts.
                        </p>
                        <a href="https://royalmadinaumroh.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

                <!-- 20. Romani Travel International -->
                <div class="card-3d card-accent-purple project-card" data-category="travel">
                    <div class="mockup-frame">
                        <img src="assets/mockups/Macbook-Air-romanitravel.com.png" alt="Romani Travel Showcase">
                    </div>
                    <div style="padding: 24px;">
                        <span class="pill-tag" style="margin-bottom: 10px; font-size: 0.75rem;">Global Travel Portal</span>
                        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 8px;">romanitravel.com</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            Global travel agency portal integrated with 24/7 customer assistance and international itineraries.
                        </p>
                        <a href="https://romanitravel.com" target="_blank" class="btn-3d btn-3d-secondary" style="width: 100%; font-size: 0.85rem;">Visit Live Website</a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer id="contact" style="padding: 60px 0 30px 0; background: var(--bg-surface); border-top: 2px solid var(--border);">
        <div class="container" style="text-align: center;">
            <h2 style="font-size: 2rem; font-weight: 900; margin-bottom: 8px; color: var(--text-main);">RIFANDI ANNAS S</h2>
            <p style="color: var(--text-muted); margin-bottom: 24px; font-size: 1.05rem;">Full-Stack WordPress & Front-End Developer | Yogyakarta, Indonesia</p>
            
            <div style="display: flex; justify-content: center; gap: 16px; margin-bottom: 32px; flex-wrap: wrap;">
                <a href="https://wa.me/6285842754076" target="_blank" class="btn-3d">WhatsApp: +62 858 4275 4076</a>
                <a href="mailto:Rifandiannas@gmail.com" class="btn-3d btn-3d-purple">Email: Rifandiannas@gmail.com</a>
            </div>

            <p style="color: var(--text-light); font-size: 0.88rem;">&copy; 2026 Rifandi Annas S. All rights reserved.</p>
        </div>
    </footer>

    <!-- INTERACTIVE FILTER JS -->
    <script>
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
    f.write(html_code)

print("Updated index.html to English PDF colorful design without emoticons!")
