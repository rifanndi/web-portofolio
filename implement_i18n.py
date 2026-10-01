import codecs
import re

file_path = 'e:/web-portofolio/index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# ==========================================
# STEP 1: Remove Google Translate widget & old manual toggle
# ==========================================
# Remove Google Translate block
content = re.sub(
    r'\s*<div id="google_translate_element".*?</script>\s*<script type="text/javascript" src="//translate\.google\.com.*?</script>',
    '',
    content,
    flags=re.DOTALL
)

# Remove Google Translate CSS cleanup block
content = re.sub(
    r'\s*/\* Google Translate Widget Clean up \*/.*?top: 0 !important;\s*\}',
    '',
    content,
    flags=re.DOTALL
)

# Remove old manual toggle if exists
content = re.sub(
    r'<div class="lang-toggle".*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# Remove old translation scripts at bottom (btn-en, btn-id listeners, typing effect)
content = re.sub(
    r'\s*/\* Translation Script \*/.*?setTimeout\(typeWriter, 1000\);\s*\}',
    '',
    content,
    flags=re.DOTALL
)

# ==========================================
# STEP 2: Change <html lang="id"> to <html lang="en"> (default EN)
# ==========================================
content = content.replace('<html lang="id">', '<html lang="en">')

# ==========================================
# STEP 3: Add Language Toggle Button CSS
# ==========================================
lang_css = """
        /* ===== Language Switcher Button ===== */
        .btn-lang-toggle {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 16px;
            border-radius: var(--radius-full);
            background: rgba(37, 99, 235, 0.08);
            border: 1px solid rgba(37, 99, 235, 0.25);
            color: var(--tone-cyan);
            font-family: var(--font-mono);
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition-smooth);
            letter-spacing: 0.5px;
            margin-left: 12px;
        }
        .btn-lang-toggle:hover {
            background: var(--tone-cyan);
            color: #ffffff;
            border-color: var(--tone-cyan);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }
        .btn-lang-toggle svg {
            width: 15px;
            height: 15px;
        }
"""
content = content.replace('</style>', lang_css + '\n</style>')

# ==========================================
# STEP 4: Add Language Toggle Button into Navbar (before nav-toggle hamburger)
# ==========================================
lang_btn_html = """
            <button class="btn-lang-toggle" id="lang-toggle" aria-label="Switch Language">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                <span id="lang-text">EN</span>
            </button>"""

content = content.replace(
    '<button class="nav-toggle" id="navToggle"',
    lang_btn_html + '\n            <button class="nav-toggle" id="navToggle"'
)

# ==========================================
# STEP 5: Add data-i18n attributes to ALL text elements
# ==========================================

# --- NAVBAR ---
replacements = [
    # Nav links
    ('<a href="#hero" class="active">Beranda</a>',
     '<a href="#hero" class="active" data-i18n="nav_home">Home</a>'),
    ('<a href="#about">Profil &amp; Keahlian</a>',
     '<a href="#about" data-i18n="nav_about">Profile &amp; Skills</a>'),
    ('<a href="#experience">Pengalaman</a>',
     '<a href="#experience" data-i18n="nav_experience">Experience</a>'),
    ('<a href="#projects">Koleksi Proyek</a>',
     '<a href="#projects" data-i18n="nav_projects">Projects</a>'),
    ('<a href="#achievements">Prestasi</a>',
     '<a href="#achievements" data-i18n="nav_achievements">Achievements</a>'),
    ('<a href="#contact">Kontak</a>',
     '<a href="#contact" data-i18n="nav_contact">Contact</a>'),

    # --- HERO ---
    ('FULL-STACK WORDPRESS &amp; FRONT-END DEVELOPER',
     '<span data-i18n="hero_role">FULL-STACK WORDPRESS &amp; FRONT-END DEVELOPER</span>'),

    # Hero H1 - replace the whole block
    ('Membangun Web<br>\n                        <span class="text-glow">Cepat, Berdampak</span><br>\n                        &amp; Bertenaga AI',
     '<span data-i18n="hero_h1_1">Building Web</span><br>\n                        <span class="text-glow" data-i18n="hero_h1_2">Fast, Impactful</span><br>\n                        <span data-i18n="hero_h1_3">&amp; AI-Powered</span>'),

    # Hero description
    ('Spesialis dalam pengembangan arsitektur web modern, kustomisasi tema &amp; plugin WordPress dari nol, integrasi React.js, optimalisasi Core Web Vitals, serta deduksi alur kerja AI/LLM untuk efisiensi bisnis korporat.',
     '<span data-i18n="hero_desc">Specialist in modern web architecture development, WordPress theme &amp; plugin customization from scratch, React.js integration, Core Web Vitals optimization, and AI/LLM workflow deduction for corporate business efficiency.</span>'),

    # Hero Buttons
    ('Jelajahi Portofolio',
     '<span data-i18n="hero_btn_portfolio">Explore Portfolio</span>'),
    ('<span>Hubungi via Email</span>',
     '<span data-i18n="hero_btn_email">Contact via Email</span>'),
    ('LinkedIn Profil\n                            </span>',
     '<span data-i18n="hero_btn_linkedin">LinkedIn Profile</span>\n                            </span>'),

    # Stats
    ('<div class="stat-desc">Tahun Pengalaman Teknis</div>',
     '<div class="stat-desc" data-i18n="stat_years">Years of Technical Experience</div>'),
    ('<div class="stat-desc">Akselerasi Kecepatan Web</div>',
     '<div class="stat-desc" data-i18n="stat_speed">Web Speed Acceleration</div>'),
    ('<div class="stat-desc">Efisiensi Alur Kerja AI/LLM</div>',
     '<div class="stat-desc" data-i18n="stat_ai">AI/LLM Workflow Efficiency</div>'),
    ('<div class="stat-desc">Klien &amp; Web Korporat</div>',
     '<div class="stat-desc" data-i18n="stat_clients">Clients &amp; Corporate Websites</div>'),

    # HUD Card
    ('<span class="hud-title">Developer Intelligence Status</span>',
     '<span class="hud-title" data-i18n="hud_title">Developer Intelligence Status</span>'),
    ('<div class="hud-metric-lbl">Trafik Organik SEO</div>',
     '<div class="hud-metric-lbl" data-i18n="hud_seo">SEO Organic Traffic</div>'),
    ('<div class="hud-metric-lbl">Biaya Operasional Klien</div>',
     '<div class="hud-metric-lbl" data-i18n="hud_cost">Client Operational Cost</div>'),
    ('<div class="hud-metric-lbl">Juara Nasional Hackathon</div>',
     '<div class="hud-metric-lbl" data-i18n="hud_hackathon">National Hackathon Champion</div>'),
    ('CORE SPECIALIZATION STACK:',
     '<span data-i18n="hud_stack">CORE SPECIALIZATION STACK:</span>'),

    # --- ABOUT SECTION ---
    ('Profil &amp; Rekam Jejak',
     '<span data-i18n="about_badge">Profile &amp; Track Record</span>'),
    ('<h2 class="section-title">Dedikasi Teknis &amp; Keahlian</h2>',
     '<h2 class="section-title" data-i18n="about_title">Technical Dedication &amp; Expertise</h2>'),
    ('Menggabungkan ketelitian pengembangan website berbasis WordPress dengan kecepatan teknologi modern React.js dan kapabilitas kecerdasan buatan.',
     '<span data-i18n="about_subtitle">Combining meticulous WordPress-based website development with the speed of modern React.js technology and artificial intelligence capabilities.</span>'),

    # Bento cards - remove old data-id/data-en attributes and use data-i18n
]

for old, new in replacements:
    content = content.replace(old, new)

# Bento About cards - fix them to use data-i18n
bento_replacements = [
    # Card 01
    ('<h3 class="bento-card-title" data-id="Ringkasan Profesional" data-en="Professional Summary">Ringkasan Profesional</h3>',
     '<h3 class="bento-card-title" data-i18n="bento_summary_title">Professional Summary</h3>'),
    ('<p class="about-bio-text" data-id="Full-Stack WordPress &amp; Front-End Developer berpengalaman lebih dari 3 tahun..." data-en="Full-Stack WordPress &amp; Front-End Developer with over 3 years of experience...">',
     '<p class="about-bio-text" data-i18n="bento_summary_p1">'),
    ('Full-Stack WordPress &amp; Front-End Developer berpengalaman lebih dari <strong>3 tahun</strong> dalam siklus pengembangan aplikasi web end-to-end, kustomisasi tema &amp; plugin WordPress, serta optimasi Core Web Vitals.</p>',
     'Full-Stack WordPress &amp; Front-End Developer with over <strong>3 years</strong> of experience in end-to-end web application development, WordPress theme &amp; plugin customization, and Core Web Vitals optimization.</p>'),
    ('<p class="about-bio-text" data-id="Memiliki rekam jejak yang teruji..." data-en="Proven track record in building multinational corporate platforms...">',
     '<p class="about-bio-text" data-i18n="bento_summary_p2">'),
    ('Memiliki rekam jejak yang teruji dalam membangun platform korporat multinasional dan toko online berbasis WooCommerce dengan mengombinasikan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript ES6+). Mampu mengintegrasikan strategi SEO teknis, analisis data, serta optimalisasi Large Language Model (LLM) untuk mendongkrak performa sistem dan efisiensi operasional.</p>',
     'Proven track record in building multinational corporate platforms and WooCommerce-based online stores by combining WordPress expertise and modern front-end technologies (React.js, Material UI, JavaScript ES6+). Capable of integrating technical SEO strategies, data analysis, and Large Language Model (LLM) optimization to boost system performance and operational efficiency.</p>'),
    # Card 02
    ('<h3 class="bento-card-title" data-id="Pendidikan" data-en="Education">Pendidikan</h3>',
     '<h3 class="bento-card-title" data-i18n="bento_edu_title">Education</h3>'),
    ('<div class="year">2022 – 2025 • Fokus pada Rekayasa Perangkat Lunak &amp; Sistem Web</div>',
     '<div class="year" data-i18n="bento_edu_year">2022 – 2025 • Focus on Software Engineering &amp; Web Systems</div>'),
    # Card 03
    ('<h3 class="bento-card-title" data-id="Keahlian Utama" data-en="Core Skills">Keahlian Utama</h3>',
     '<h3 class="bento-card-title" data-i18n="bento_skills_title">Core Skills</h3>'),
    # Remove old data-id/data-en on bento containers
    (' data-id="Ringkasan Profesional" data-en="Professional Summary"', ''),
    (' data-id="Pendidikan" data-en="Education"', ''),
]

for old, new in bento_replacements:
    content = content.replace(old, new)

# --- EXPERIENCE SECTION ---
exp_replacements = [
    ('Karier Profesional',
     '<span data-i18n="exp_badge">Professional Career</span>'),
    ('<h2 class="section-title">Pengalaman Kerja</h2>',
     '<h2 class="section-title" data-i18n="exp_title">Work Experience</h2>'),
    ('Membimbing transformasi digital, arsitektur website berperforma tinggi, dan integrasi kecerdasan buatan di lingkungan profesional.',
     '<span data-i18n="exp_subtitle">Guiding digital transformation, high-performance website architecture, and artificial intelligence integration in professional environments.</span>'),

    # Timeline badges
    ('<span class="timeline-badge">Mei 2023 – Agustus 2026</span>',
     '<span class="timeline-badge" data-i18n="exp1_date">May 2023 – August 2026</span>'),
    ('<span class="timeline-badge">Mei 2024 – Februari 2025</span>',
     '<span class="timeline-badge" data-i18n="exp2_date">May 2024 – February 2025</span>'),
    ('<span class="timeline-badge">September 2024 – Januari 2025</span>',
     '<span class="timeline-badge" data-i18n="exp3_date">September 2024 – January 2025</span>'),
    ('<span class="timeline-badge">November 2023 – Januari 2024</span>',
     '<span class="timeline-badge" data-i18n="exp4_date">November 2023 – January 2024</span>'),

    # Timeline bullets - GMT
    ('<strong>Peningkatan Kecepatan Situs 35%:</strong> Memimpin siklus pengembangan, pemeliharaan, dan optimasi end-to-end pada platform berbasis WordPress serta pembuatan situs web kustom untuk klien korporat.',
     '<span data-i18n="exp1_b1"><strong>35% Site Speed Improvement:</strong> Led end-to-end development, maintenance, and optimization cycles on WordPress-based platforms and custom website creation for corporate clients.</span>'),
    ('<strong>Kustomisasi Tema &amp; Plugin dari Nol:</strong> Mengembangkan plugin dan theme kustom menggunakan PHP dan JavaScript, berhasil menekan biaya operasional klien hingga 20%.',
     '<span data-i18n="exp1_b2"><strong>Custom Theme &amp; Plugin from Scratch:</strong> Developed custom plugins and themes using PHP and JavaScript, successfully reducing client operational costs by 20%.</span>'),
    ('<strong>Alur Kerja Modern:</strong> Membangun platform web berkinerja tinggi dengan WordPress Studio, Elementor, WooCommerce, Antigravity, serta VS Code.',
     '<span data-i18n="exp1_b3"><strong>Modern Workflow:</strong> Built high-performance web platforms using WordPress Studio, Elementor, WooCommerce, Antigravity, and VS Code.</span>'),
    ('<strong>Lonjakan Trafik Organik 30%:</strong> Menerapkan strategi SEO teknis menyeluruh, termasuk implementasi Schema Markup terstruktur dan optimasi kata kunci via Rank Math &amp; Yoast SEO serta memperkuat profil backlink.',
     '<span data-i18n="exp1_b4"><strong>30% Organic Traffic Surge:</strong> Implemented comprehensive technical SEO strategies including structured Schema Markup, keyword optimization via Rank Math &amp; Yoast SEO, and backlink profile strengthening.</span>'),
    ('<strong>Edukasi AI &amp; Workshop Bisnis:</strong> Menjadi pembicara dalam seminar dan pelatihan teknis tentang dasar pemrograman (vibe coding) dan pemanfaatan Large Language Model (LLM), meningkatkan utilisasi AI hingga 60% dalam operasional harian peserta non-teknis.',
     '<span data-i18n="exp1_b5"><strong>AI Education &amp; Business Workshop:</strong> Served as speaker in seminars and technical training on programming basics (vibe coding) and Large Language Model (LLM) utilization, increasing AI usage by 60% in daily operations of non-technical participants.</span>'),

    # Timeline bullets - NCS
    ('<strong>Pengembangan Platform Ekspor B2B:</strong> Mengembangkan serta mengelola platform web korporat ekspor kelapa &amp; arang kelapa terintegrasi agar selalu beroperasi dalam status optimal.',
     '<span data-i18n="exp2_b1"><strong>B2B Export Platform Development:</strong> Developed and managed integrated corporate export web platform for coconut &amp; coconut charcoal products to maintain optimal operational status.</span>'),
    ('<strong>Pertumbuhan Strategi B2B 20%:</strong> Menyusun pembuatan artikel berbahasa internasional dan optimasi SEO terstruktur untuk memperluas jangkauan pembeli global secara organik.',
     '<span data-i18n="exp2_b2"><strong>20% B2B Strategy Growth:</strong> Composed international language articles and structured SEO optimization to expand global buyer reach organically.</span>'),
    ('<strong>Training AI Tim Internal:</strong> Membimbing tim internal dalam mengadopsi AI untuk mendongkrak efisiensi riset dan strategi pemasaran internasional.',
     '<span data-i18n="exp2_b3"><strong>Internal AI Team Training:</strong> Guided the internal team in adopting AI to boost research efficiency and international marketing strategies.</span>'),
    ('<strong>Validasi Dataset &amp; Kualitas Output 30%:</strong> Menganalisis kueri teknis kompleks dan memvalidasi linimasa dataset machine learning demi menjaga akurasi tinggi serta konsistensi sistem.',
     '<span data-i18n="exp2_b4"><strong>30% Dataset Validation &amp; Output Quality:</strong> Analyzed complex technical queries and validated machine learning dataset timelines to maintain high accuracy and system consistency.</span>'),

    # Timeline bullets - Nastech
    ('<strong>Aplikasi Web React.js &amp; MUI:</strong> Mengembangkan aplikasi web dan sistem manajemen data berbasis React.js dengan komponen Material UI yang responsif.',
     '<span data-i18n="exp3_b1"><strong>React.js &amp; MUI Web Application:</strong> Developed web applications and data management systems based on React.js with responsive Material UI components.</span>'),
    ('<strong>Dashboard Manajemen Digital:</strong> Mendesain arsitektur dashboard inventaris terpadu dengan pemantauan stok real-time internal.',
     '<span data-i18n="exp3_b2"><strong>Digital Management Dashboard:</strong> Designed unified inventory dashboard architecture with internal real-time stock monitoring.</span>'),
    ('<strong>Efisiensi Operasional 25%:</strong> Mengoptimalkan alur kerja sistem antarmuka UI/UX untuk mempercepat pelaporan data tim lapangan.',
     '<span data-i18n="exp3_b3"><strong>25% Operational Efficiency:</strong> Optimized UI/UX interface system workflows to accelerate field team data reporting.</span>'),

    # Timeline bullets - Praisindo
    ('<strong>Pengembangan Antarmuka Finansial:</strong> Berkontribusi aktif dalam perancangan modul antarmuka aplikasi web berskala enterprise menggunakan React.js dan Material UI.',
     '<span data-i18n="exp4_b1"><strong>Financial Interface Development:</strong> Actively contributed to designing enterprise-scale web application interface modules using React.js and Material UI.</span>'),
    ('<strong>Standarisasi Kode Bersih:</strong> Mengimplementasikan standar clean HTML, modern CSS, dan modular JavaScript yang memudahkan kolaborasi tim pengembang.',
     '<span data-i18n="exp4_b2"><strong>Clean Code Standardization:</strong> Implemented clean HTML, modern CSS, and modular JavaScript standards to facilitate developer team collaboration.</span>'),
]

for old, new in exp_replacements:
    content = content.replace(old, new)

# --- PROJECTS SECTION ---
proj_replacements = [
    ('Karya &amp; Implementasi',
     '<span data-i18n="proj_badge">Works &amp; Implementations</span>'),
    ('<h2 class="section-title">Koleksi Proyek Berdasarkan Kategori</h2>',
     '<h2 class="section-title" data-i18n="proj_title">Project Collection by Category</h2>'),
    ('Jelajahi berbagai website yang telah saya kembangkan, mulai dari platform ekspor global B2B, produk herbal e-commerce, pabrik konstruksi plafon PVC nasional, hingga hospitality &amp; personal branding.',
     '<span data-i18n="proj_subtitle">Explore various websites I have developed, from global B2B export platforms, herbal e-commerce products, national PVC ceiling manufacturing, to hospitality &amp; personal branding.</span>'),

    # Filter Buttons
    ('>Semua Proyek</button>',
     ' data-i18n="filter_all">All Projects</button>'),
    ('>Ekspor &amp; B2B Global</button>',
     ' data-i18n="filter_export">Export &amp; Global B2B</button>'),
    ('>Herbal &amp; E-Commerce</button>',
     ' data-i18n="filter_herbal">Herbal &amp; E-Commerce</button>'),
    ('>Plafon PVC &amp; Industri</button>',
     ' data-i18n="filter_plafon">PVC Ceiling &amp; Industry</button>'),
    ('>Travel &amp; Umroh</button>',
     ' data-i18n="filter_travel">Travel &amp; Umrah</button>'),
    ('>Edukasi &amp; Personal</button>',
     ' data-i18n="filter_personal">Education &amp; Personal</button>'),
]

for old, new in proj_replacements:
    content = content.replace(old, new)

# Project CTA links
content = content.replace(
    'Detail Proyek\n                                <svg',
    '<span data-i18n="proj_detail">Project Detail</span>\n                                <svg'
)

# --- ACHIEVEMENTS SECTION ---
ach_replacements = [
    ('Pengakuan &amp; Prestasi',
     '<span data-i18n="ach_badge">Recognition &amp; Achievements</span>'),
    ('<h2 class="section-title">Penghargaan &amp; Sertifikasi Nasional</h2>',
     '<h2 class="section-title" data-i18n="ach_title">Awards &amp; National Certifications</h2>'),
    ('Bukti dedikasi, kapabilitas pemecahan masalah, dan kompetensi teruji di kompetisi teknologi nasional dan sertifikasi profesi.',
     '<span data-i18n="ach_subtitle">Proof of dedication, problem-solving capability, and tested competence in national technology competitions and professional certifications.</span>'),
    ('<div class="award-date">Juli 2023 • Inovasi Solusi Digital</div>',
     '<div class="award-date" data-i18n="ach1_date">July 2023 • Digital Solution Innovation</div>'),
    ('<div class="award-date">Juli 2024 • Kategori Model Bisnis Digital</div>',
     '<div class="award-date" data-i18n="ach2_date">July 2024 • Digital Business Model Category</div>'),
    ('<div class="award-date">Desember 2024 • Terlisensi Resmi Nasional</div>',
     '<div class="award-date" data-i18n="ach3_date">December 2024 • Nationally Licensed</div>'),
]

for old, new in ach_replacements:
    content = content.replace(old, new)

# --- FOOTER ---
footer_replacements = [
    ('<h3>Siap Membangun Website Berperforma Tinggi?</h3>',
     '<h3 data-i18n="footer_cta_title">Ready to Build High-Performance Websites?</h3>'),
    ('<p>Konsultasikan kebutuhan pembuatan website kustom, integrasi WordPress, atau alur kerja AI untuk meningkatkan efisiensi bisnis Anda.</p>',
     '<p data-i18n="footer_cta_desc">Consult your custom website creation needs, WordPress integration, or AI workflows to increase your business efficiency.</p>'),
    ('Mulai Konsultasi',
     '<span data-i18n="footer_cta_btn">Start Consultation</span>'),
    ('<p>\n                        Full-Stack WordPress &amp; Front-End Developer berbasis di Yogyakarta, Indonesia. Berdedikasi menciptakan pengalaman web interaktif 3D, kustomisasi WordPress mutakhir, dan pengoptimalan teknologi AI.\n                    </p>',
     '<p data-i18n="footer_brand_desc">\n                        Full-Stack WordPress &amp; Front-End Developer based in Yogyakarta, Indonesia. Dedicated to creating interactive 3D web experiences, cutting-edge WordPress customization, and AI technology optimization.\n                    </p>'),
    ('<h5>Navigasi Halaman</h5>',
     '<h5 data-i18n="footer_nav_title">Page Navigation</h5>'),
    ('<h5>Kontak Langsung</h5>',
     '<h5 data-i18n="footer_contact_title">Direct Contact</h5>'),

    # Footer nav links
    ('<li><a href="#hero">Beranda</a></li>',
     '<li><a href="#hero" data-i18n="nav_home">Home</a></li>'),
    ('<li><a href="#about">Profil &amp; Keahlian</a></li>',
     '<li><a href="#about" data-i18n="nav_about">Profile &amp; Skills</a></li>'),
    ('<li><a href="#experience">Pengalaman Kerja</a></li>',
     '<li><a href="#experience" data-i18n="footer_nav_exp">Work Experience</a></li>'),
    ('<li><a href="#projects">Koleksi Proyek</a></li>',
     '<li><a href="#projects" data-i18n="nav_projects">Projects</a></li>'),
    ('<li><a href="#achievements">Prestasi &amp; Sertifikasi</a></li>',
     '<li><a href="#achievements" data-i18n="footer_nav_ach">Achievements &amp; Certifications</a></li>'),

    # Modal
    ('Kunjungi Live Website',
     '<span data-i18n="modal_visit">Visit Live Website</span>'),
    ('<h5>Spesifikasi Teknis &amp; Dampak Solusi</h5>',
     '<h5 data-i18n="modal_specs">Technical Specifications &amp; Solution Impact</h5>'),
]

for old, new in footer_replacements:
    content = content.replace(old, new)

# ==========================================
# STEP 6: Add the comprehensive i18n dictionary & switcher script
# ==========================================
i18n_script = """
        /* ==========================================================================
           i18n LANGUAGE SWITCHER — FULL BILINGUAL (EN default / ID)
           ========================================================================== */
        const i18n = {
            en: {
                nav_home: "Home",
                nav_about: "Profile & Skills",
                nav_experience: "Experience",
                nav_projects: "Projects",
                nav_achievements: "Achievements",
                nav_contact: "Contact",
                hero_role: "FULL-STACK WORDPRESS & FRONT-END DEVELOPER",
                hero_h1_1: "Building Web",
                hero_h1_2: "Fast, Impactful",
                hero_h1_3: "& AI-Powered",
                hero_desc: "Specialist in modern web architecture development, WordPress theme & plugin customization from scratch, React.js integration, Core Web Vitals optimization, and AI/LLM workflow deduction for corporate business efficiency.",
                hero_btn_portfolio: "Explore Portfolio",
                hero_btn_email: "Contact via Email",
                hero_btn_linkedin: "LinkedIn Profile",
                stat_years: "Years of Technical Experience",
                stat_speed: "Web Speed Acceleration",
                stat_ai: "AI/LLM Workflow Efficiency",
                stat_clients: "Clients & Corporate Websites",
                hud_title: "Developer Intelligence Status",
                hud_seo: "SEO Organic Traffic",
                hud_cost: "Client Operational Cost",
                hud_hackathon: "National Hackathon Champion",
                hud_stack: "CORE SPECIALIZATION STACK:",
                about_badge: "Profile & Track Record",
                about_title: "Technical Dedication & Expertise",
                about_subtitle: "Combining meticulous WordPress-based website development with the speed of modern React.js technology and artificial intelligence capabilities.",
                bento_summary_title: "Professional Summary",
                bento_summary_p1: "Full-Stack WordPress & Front-End Developer with over <strong>3 years</strong> of experience in end-to-end web application development, WordPress theme & plugin customization, and Core Web Vitals optimization.",
                bento_summary_p2: "Proven track record in building multinational corporate platforms and WooCommerce-based online stores by combining WordPress expertise and modern front-end technologies (React.js, Material UI, JavaScript ES6+). Capable of integrating technical SEO strategies, data analysis, and Large Language Model (LLM) optimization to boost system performance and operational efficiency.",
                bento_edu_title: "Education",
                bento_edu_year: "2022 – 2025 • Focus on Software Engineering & Web Systems",
                bento_skills_title: "Core Skills",
                exp_badge: "Professional Career",
                exp_title: "Work Experience",
                exp_subtitle: "Guiding digital transformation, high-performance website architecture, and artificial intelligence integration in professional environments.",
                exp1_date: "May 2023 – August 2026",
                exp1_b1: "<strong>35% Site Speed Improvement:</strong> Led end-to-end development, maintenance, and optimization cycles on WordPress-based platforms and custom website creation for corporate clients.",
                exp1_b2: "<strong>Custom Theme & Plugin from Scratch:</strong> Developed custom plugins and themes using PHP and JavaScript, successfully reducing client operational costs by 20%.",
                exp1_b3: "<strong>Modern Workflow:</strong> Built high-performance web platforms using WordPress Studio, Elementor, WooCommerce, Antigravity, and VS Code.",
                exp1_b4: "<strong>30% Organic Traffic Surge:</strong> Implemented comprehensive technical SEO strategies including structured Schema Markup, keyword optimization via Rank Math & Yoast SEO, and backlink profile strengthening.",
                exp1_b5: "<strong>AI Education & Business Workshop:</strong> Served as speaker in seminars and technical training on programming basics (vibe coding) and Large Language Model (LLM) utilization, increasing AI usage by 60% in daily operations of non-technical participants.",
                exp2_date: "May 2024 – February 2025",
                exp2_b1: "<strong>B2B Export Platform Development:</strong> Developed and managed integrated corporate export web platform for coconut & coconut charcoal products to maintain optimal operational status.",
                exp2_b2: "<strong>20% B2B Strategy Growth:</strong> Composed international language articles and structured SEO optimization to expand global buyer reach organically.",
                exp2_b3: "<strong>Internal AI Team Training:</strong> Guided the internal team in adopting AI to boost research efficiency and international marketing strategies.",
                exp2_b4: "<strong>30% Dataset Validation & Output Quality:</strong> Analyzed complex technical queries and validated machine learning dataset timelines to maintain high accuracy and system consistency.",
                exp3_date: "September 2024 – January 2025",
                exp3_b1: "<strong>React.js & MUI Web Application:</strong> Developed web applications and data management systems based on React.js with responsive Material UI components.",
                exp3_b2: "<strong>Digital Management Dashboard:</strong> Designed unified inventory dashboard architecture with internal real-time stock monitoring.",
                exp3_b3: "<strong>25% Operational Efficiency:</strong> Optimized UI/UX interface system workflows to accelerate field team data reporting.",
                exp4_date: "November 2023 – January 2024",
                exp4_b1: "<strong>Financial Interface Development:</strong> Actively contributed to designing enterprise-scale web application interface modules using React.js and Material UI.",
                exp4_b2: "<strong>Clean Code Standardization:</strong> Implemented clean HTML, modern CSS, and modular JavaScript standards to facilitate developer team collaboration.",
                proj_badge: "Works & Implementations",
                proj_title: "Project Collection by Category",
                proj_subtitle: "Explore various websites I have developed, from global B2B export platforms, herbal e-commerce products, national PVC ceiling manufacturing, to hospitality & personal branding.",
                filter_all: "All Projects",
                filter_export: "Export & Global B2B",
                filter_herbal: "Herbal & E-Commerce",
                filter_plafon: "PVC Ceiling & Industry",
                filter_travel: "Travel & Umrah",
                filter_personal: "Education & Personal",
                proj_detail: "Project Detail",
                ach_badge: "Recognition & Achievements",
                ach_title: "Awards & National Certifications",
                ach_subtitle: "Proof of dedication, problem-solving capability, and tested competence in national technology competitions and professional certifications.",
                ach1_date: "July 2023 • Digital Solution Innovation",
                ach2_date: "July 2024 • Digital Business Model Category",
                ach3_date: "December 2024 • Nationally Licensed",
                footer_cta_title: "Ready to Build High-Performance Websites?",
                footer_cta_desc: "Consult your custom website creation needs, WordPress integration, or AI workflows to increase your business efficiency.",
                footer_cta_btn: "Start Consultation",
                footer_brand_desc: "Full-Stack WordPress & Front-End Developer based in Yogyakarta, Indonesia. Dedicated to creating interactive 3D web experiences, cutting-edge WordPress customization, and AI technology optimization.",
                footer_nav_title: "Page Navigation",
                footer_contact_title: "Direct Contact",
                footer_nav_exp: "Work Experience",
                footer_nav_ach: "Achievements & Certifications",
                modal_visit: "Visit Live Website",
                modal_specs: "Technical Specifications & Solution Impact"
            },
            id: {
                nav_home: "Beranda",
                nav_about: "Profil & Keahlian",
                nav_experience: "Pengalaman",
                nav_projects: "Koleksi Proyek",
                nav_achievements: "Prestasi",
                nav_contact: "Kontak",
                hero_role: "FULL-STACK WORDPRESS & FRONT-END DEVELOPER",
                hero_h1_1: "Membangun Web",
                hero_h1_2: "Cepat, Berdampak",
                hero_h1_3: "& Bertenaga AI",
                hero_desc: "Spesialis dalam pengembangan arsitektur web modern, kustomisasi tema & plugin WordPress dari nol, integrasi React.js, optimalisasi Core Web Vitals, serta deduksi alur kerja AI/LLM untuk efisiensi bisnis korporat.",
                hero_btn_portfolio: "Jelajahi Portofolio",
                hero_btn_email: "Hubungi via Email",
                hero_btn_linkedin: "LinkedIn Profil",
                stat_years: "Tahun Pengalaman Teknis",
                stat_speed: "Akselerasi Kecepatan Web",
                stat_ai: "Efisiensi Alur Kerja AI/LLM",
                stat_clients: "Klien & Web Korporat",
                hud_title: "Developer Intelligence Status",
                hud_seo: "Trafik Organik SEO",
                hud_cost: "Biaya Operasional Klien",
                hud_hackathon: "Juara Nasional Hackathon",
                hud_stack: "CORE SPECIALIZATION STACK:",
                about_badge: "Profil & Rekam Jejak",
                about_title: "Dedikasi Teknis & Keahlian",
                about_subtitle: "Menggabungkan ketelitian pengembangan website berbasis WordPress dengan kecepatan teknologi modern React.js dan kapabilitas kecerdasan buatan.",
                bento_summary_title: "Ringkasan Profesional",
                bento_summary_p1: "Full-Stack WordPress & Front-End Developer berpengalaman lebih dari <strong>3 tahun</strong> dalam siklus pengembangan aplikasi web end-to-end, kustomisasi tema & plugin WordPress, serta optimasi Core Web Vitals.",
                bento_summary_p2: "Memiliki rekam jejak yang teruji dalam membangun platform korporat multinasional dan toko online berbasis WooCommerce dengan mengombinasikan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript ES6+). Mampu mengintegrasikan strategi SEO teknis, analisis data, serta optimalisasi Large Language Model (LLM) untuk mendongkrak performa sistem dan efisiensi operasional.",
                bento_edu_title: "Pendidikan",
                bento_edu_year: "2022 – 2025 • Fokus pada Rekayasa Perangkat Lunak & Sistem Web",
                bento_skills_title: "Keahlian Utama",
                exp_badge: "Karier Profesional",
                exp_title: "Pengalaman Kerja",
                exp_subtitle: "Membimbing transformasi digital, arsitektur website berperforma tinggi, dan integrasi kecerdasan buatan di lingkungan profesional.",
                exp1_date: "Mei 2023 – Agustus 2026",
                exp1_b1: "<strong>Peningkatan Kecepatan Situs 35%:</strong> Memimpin siklus pengembangan, pemeliharaan, dan optimasi end-to-end pada platform berbasis WordPress serta pembuatan situs web kustom untuk klien korporat.",
                exp1_b2: "<strong>Kustomisasi Tema & Plugin dari Nol:</strong> Mengembangkan plugin dan theme kustom menggunakan PHP dan JavaScript, berhasil menekan biaya operasional klien hingga 20%.",
                exp1_b3: "<strong>Alur Kerja Modern:</strong> Membangun platform web berkinerja tinggi dengan WordPress Studio, Elementor, WooCommerce, Antigravity, serta VS Code.",
                exp1_b4: "<strong>Lonjakan Trafik Organik 30%:</strong> Menerapkan strategi SEO teknis menyeluruh, termasuk implementasi Schema Markup terstruktur dan optimasi kata kunci via Rank Math & Yoast SEO serta memperkuat profil backlink.",
                exp1_b5: "<strong>Edukasi AI & Workshop Bisnis:</strong> Menjadi pembicara dalam seminar dan pelatihan teknis tentang dasar pemrograman (vibe coding) dan pemanfaatan Large Language Model (LLM), meningkatkan utilisasi AI hingga 60% dalam operasional harian peserta non-teknis.",
                exp2_date: "Mei 2024 – Februari 2025",
                exp2_b1: "<strong>Pengembangan Platform Ekspor B2B:</strong> Mengembangkan serta mengelola platform web korporat ekspor kelapa & arang kelapa terintegrasi agar selalu beroperasi dalam status optimal.",
                exp2_b2: "<strong>Pertumbuhan Strategi B2B 20%:</strong> Menyusun pembuatan artikel berbahasa internasional dan optimasi SEO terstruktur untuk memperluas jangkauan pembeli global secara organik.",
                exp2_b3: "<strong>Training AI Tim Internal:</strong> Membimbing tim internal dalam mengadopsi AI untuk mendongkrak efisiensi riset dan strategi pemasaran internasional.",
                exp2_b4: "<strong>Validasi Dataset & Kualitas Output 30%:</strong> Menganalisis kueri teknis kompleks dan memvalidasi linimasa dataset machine learning demi menjaga akurasi tinggi serta konsistensi sistem.",
                exp3_date: "September 2024 – Januari 2025",
                exp3_b1: "<strong>Aplikasi Web React.js & MUI:</strong> Mengembangkan aplikasi web dan sistem manajemen data berbasis React.js dengan komponen Material UI yang responsif.",
                exp3_b2: "<strong>Dashboard Manajemen Digital:</strong> Mendesain arsitektur dashboard inventaris terpadu dengan pemantauan stok real-time internal.",
                exp3_b3: "<strong>Efisiensi Operasional 25%:</strong> Mengoptimalkan alur kerja sistem antarmuka UI/UX untuk mempercepat pelaporan data tim lapangan.",
                exp4_date: "November 2023 – Januari 2024",
                exp4_b1: "<strong>Pengembangan Antarmuka Finansial:</strong> Berkontribusi aktif dalam perancangan modul antarmuka aplikasi web berskala enterprise menggunakan React.js dan Material UI.",
                exp4_b2: "<strong>Standarisasi Kode Bersih:</strong> Mengimplementasikan standar clean HTML, modern CSS, dan modular JavaScript yang memudahkan kolaborasi tim pengembang.",
                proj_badge: "Karya & Implementasi",
                proj_title: "Koleksi Proyek Berdasarkan Kategori",
                proj_subtitle: "Jelajahi berbagai website yang telah saya kembangkan, mulai dari platform ekspor global B2B, produk herbal e-commerce, pabrik konstruksi plafon PVC nasional, hingga hospitality & personal branding.",
                filter_all: "Semua Proyek",
                filter_export: "Ekspor & B2B Global",
                filter_herbal: "Herbal & E-Commerce",
                filter_plafon: "Plafon PVC & Industri",
                filter_travel: "Travel & Umroh",
                filter_personal: "Edukasi & Personal",
                proj_detail: "Detail Proyek",
                ach_badge: "Pengakuan & Prestasi",
                ach_title: "Penghargaan & Sertifikasi Nasional",
                ach_subtitle: "Bukti dedikasi, kapabilitas pemecahan masalah, dan kompetensi teruji di kompetisi teknologi nasional dan sertifikasi profesi.",
                ach1_date: "Juli 2023 • Inovasi Solusi Digital",
                ach2_date: "Juli 2024 • Kategori Model Bisnis Digital",
                ach3_date: "Desember 2024 • Terlisensi Resmi Nasional",
                footer_cta_title: "Siap Membangun Website Berperforma Tinggi?",
                footer_cta_desc: "Konsultasikan kebutuhan pembuatan website kustom, integrasi WordPress, atau alur kerja AI untuk meningkatkan efisiensi bisnis Anda.",
                footer_cta_btn: "Mulai Konsultasi",
                footer_brand_desc: "Full-Stack WordPress & Front-End Developer berbasis di Yogyakarta, Indonesia. Berdedikasi menciptakan pengalaman web interaktif 3D, kustomisasi WordPress mutakhir, dan pengoptimalan teknologi AI.",
                footer_nav_title: "Navigasi Halaman",
                footer_contact_title: "Kontak Langsung",
                footer_nav_exp: "Pengalaman Kerja",
                footer_nav_ach: "Prestasi & Sertifikasi",
                modal_visit: "Kunjungi Live Website",
                modal_specs: "Spesifikasi Teknis & Dampak Solusi"
            }
        };

        // Read saved language or default to 'en'
        let currentLang = localStorage.getItem('site_lang') || 'en';

        function setLanguage(lang) {
            currentLang = lang;
            localStorage.setItem('site_lang', lang);
            document.documentElement.setAttribute('lang', lang);

            // Update toggle button label
            const langText = document.getElementById('lang-text');
            if (langText) langText.textContent = lang.toUpperCase();

            // Update all elements with data-i18n attribute
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (i18n[lang] && i18n[lang][key]) {
                    el.innerHTML = i18n[lang][key];
                }
            });
        }

        // Initialize language on page load
        setLanguage(currentLang);

        // Toggle event listener
        document.getElementById('lang-toggle')?.addEventListener('click', () => {
            const nextLang = currentLang === 'en' ? 'id' : 'en';
            setLanguage(nextLang);
        });
"""

# Insert the i18n script BEFORE the closing </script> tag
content = content.replace('    </script>\n</body>', i18n_script + '\n    </script>\n</body>')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("SUCCESS: i18n language switcher implemented.")
