import codecs
import re

file_path = 'e:/web-portofolio/index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Navbar elements
content = re.sub(
    r'<a href="#about"[^>]*>.*?</a>',
    '<a href="#about" data-i18n="nav_about">About</a>',
    content
)
content = re.sub(
    r'<a href="#projects"[^>]*>.*?</a>',
    '<a href="#projects" data-i18n="nav_projects">Projects</a>',
    content
)
content = re.sub(
    r'<a href="#achievements"[^>]*>.*?</a>',
    '<a href="#achievements" data-i18n="nav_achievements">Achievements</a>',
    content
)
content = re.sub(
    r'<a href="#contact"[^>]*>.*?</a>',
    '<a href="#contact" data-i18n="nav_contact">Contact</a>',
    content
)

# 2. Hero HUD Card translations
content = re.sub(
    r'<span class="hud-status-chip">● ACTIVE READY</span>',
    '<span class="hud-status-chip" data-i18n="hud_status">● ACTIVE READY</span>',
    content
)
content = re.sub(
    r'<div class="hud-metric-lbl">Certified Export Strategy</div>',
    '<div class="hud-metric-lbl" data-i18n="hud_export_lbl">Certified Export Strategy</div>',
    content
)

# 3. About Section elements
content = re.sub(
    r'<div class="degree">Associate\'s Degree \(D3\) in Computer Science</div>',
    '<div class="degree" data-i18n="edu_degree">Associate\'s Degree (D3) in Computer Science</div>',
    content
)
content = re.sub(
    r'<div class="year">2022 – 2025 • Fokus pada Rekayasa Perangkat Lunak & Sistem Web</div>',
    '<div class="year" data-i18n="edu_focus">2022 – 2025 • Focused on Software Engineering & Web Systems</div>',
    content
)

# 4. Experience Section elements
# Exp 1
content = re.sub(
    r'<div class="timeline-role">WordPress & Web Developer / Lead AI Trainer</div>',
    '<div class="timeline-role" data-i18n="exp1_role">WordPress & Web Developer / Lead AI Trainer</div>',
    content
)
content = re.sub(
    r'<strong>Kustomisasi Tema & Plugin dari Nol:</strong> Mengembangkan plugin dan theme kustom menggunakan PHP dan JavaScript, berhasil menekan biaya operasional klien hingga 20%\.',
    '<span data-i18n="exp1_b1"><strong>Theme & Plugin Customization from Scratch:</strong> Built custom plugins and themes using PHP and JavaScript, reducing client operational costs by 20%.</span>',
    content
)
content = re.sub(
    r'<strong>Lonjakan Trafik Organik 30%:</strong> Menerapkan strategi SEO teknis menyeluruh, termasuk implementasi Schema Markup terstruktur dan optimasi kata kunci via Rank Math & Yoast SEO serta memperkuat profil backlink\.',
    '<span data-i18n="exp1_b2"><strong>30% Organic Traffic Surge:</strong> Implemented comprehensive technical SEO strategies, including structured Schema Markup and keyword optimization via Rank Math & Yoast SEO and strengthening backlink profiles.</span>',
    content
)
content = re.sub(
    r'<strong>Edukasi AI & Workshop Bisnis:</strong> Menjadi pembicara dalam seminar dan pelatihan teknis tentang dasar pemrograman \(vibe coding\) dan pemanfaatan Large Language Model \(LLM\), meningkatkan utilisasi AI hingga 60% dalam operasional harian peserta non-teknis\.',
    '<span data-i18n="exp1_b3"><strong>AI Education & Business Workshops:</strong> Speaker in seminars and technical workshops on coding fundamentals and LLM utilization, raising AI adoption by 60% in non-technical participants\' daily operations.</span>',
    content
)

# Exp 2
content = re.sub(
    r'<div class="timeline-role">Global Digital Strategy & SEO Lead</div>',
    '<div class="timeline-role" data-i18n="exp2_role">Global Digital Strategy & SEO Lead</div>',
    content
)
content = re.sub(
    r'<strong>Pengembangan Platform Ekspor B2B:</strong> Mengembangkan serta mengelola platform web korporat ekspor kelapa & arang kelapa terintegrasi agar selalu beroperasi dalam status optimal\.',
    '<span data-i18n="exp2_b1"><strong>B2B Export Platform Engineering:</strong> Developed and managed integrated corporate export web platforms for coconut & charcoal products ensuring optimal performance status.</span>',
    content
)
content = re.sub(
    r'<strong>Validasi Dataset & Kualitas Output 30%:</strong> Menganalisis kueri teknis kompleks dan memvalidasi linimasa dataset machine learning demi menjaga akurasi tinggi serta konsistensi sistem\.',
    '<span data-i18n="exp2_b2"><strong>Dataset Validation & 30% Output Quality:</strong> Analyzed complex technical queries and validated machine learning dataset timelines to maintain high accuracy and system consistency.</span>',
    content
)

# Exp 3
content = re.sub(
    r'<strong>Aplikasi Web React\.js & MUI:</strong> Mengembangkan aplikasi web dan sistem manajemen data berbasis React\.js dengan komponen Material UI yang responsif\.',
    '<span data-i18n="exp3_b1"><strong>React.js & MUI Web Applications:</strong> Developed web applications and data management systems based on React.js with responsive Material UI components.</span>',
    content
)

# Exp 4
content = re.sub(
    r'<strong>Portal Web Korporat Finansial:</strong> Berkolaborasi dalam pengembangan dan pengujian modul tampilan antarmuka sistem web korporat perbankan dan sekuritas\.',
    '<span data-i18n="exp4_b1"><strong>Enterprise Financial Web Portals:</strong> Built interactive user interface modules for enterprise financial service platforms.</span>',
    content
)

# 5. Achievements Section Awards
content = re.sub(
    r'<h3 class="award-title">Juara 2 — Digital Business Technology Competition \(Hackathon\)</h3>',
    '<h3 class="award-title" data-i18n="ach1_title">2nd Winner — Digital Business Technology Competition (Hackathon)</h3>',
    content
)
content = re.sub(
    r'<h3 class="award-title">Juara 2 — National Digital Business Competition \(AMICTA\)</h3>',
    '<h3 class="award-title" data-i18n="ach2_title">2nd Winner — National Digital Business Competition (AMICTA)</h3>',
    content
)
content = re.sub(
    r'<h3 class="award-title">Digital Export Business Management Certification</h3>',
    '<h3 class="award-title" data-i18n="ach3_title">Digital Export Business Management Certification</h3>',
    content
)

# 6. Footer Brand and Sub-footer
footer_brand_pattern = r'<div class="footer-brand">\s*<h4>Rifandi <span>Annas Shahruri</span></h4>\s*<p>.*?</p>\s*</div>'
footer_brand_replacement = '''<div class="footer-brand">
                    <h4>Rifandi <span>Annas Shahruri</span></h4>
                    <p data-i18n="footer_brand_desc">
                        Full-Stack WordPress & Front-End Developer based in Yogyakarta, Indonesia. Dedicated to engineering interactive 3D web experiences, modern WordPress customization, and AI workflow optimization.
                    </p>
                </div>'''
content = re.sub(footer_brand_pattern, footer_brand_replacement, content, flags=re.DOTALL)

content = re.sub(
    r'<div>© 2026 Rifandi Annas Shahruri\. All Rights Reserved\.</div>',
    '<div data-i18n="footer_copy">© 2026 Rifandi Annas Shahruri. All Rights Reserved.</div>',
    content
)
content = re.sub(
    r'<div style="font-family: var\(--font-mono\); font-size: 0\.76rem;">Designed with Three\.js WebGL & GSAP 3D\s*Motion</div>',
    '<div style="font-family: var(--font-mono); font-size: 0.76rem;" data-i18n="footer_tech">Designed with Three.js WebGL & GSAP 3D Motion</div>',
    content
)

# 7. Modal Project Details translations
content = re.sub(
    r'<span class="modal-category-tag" id="modalCategory">Kategori</span>',
    '<span class="modal-category-tag" id="modalCategory" data-i18n="modal_category_fallback">Project Category</span>',
    content
)

# 8. Complete comprehensive script replacement
master_script = '''
    <!-- Language Switcher & Master Translation Dictionary -->
    <script>
        /* ===================================================
           MASTER DICTIONARY / KAMUS BAHASA LENGKAP (EN & ID)
           =================================================== */
        const translations = {
            en: {
                nav_home: "Home",
                nav_about: "About",
                nav_experience: "Experience",
                nav_projects: "Projects",
                nav_achievements: "Achievements",
                nav_contact: "Contact",
                
                hero_location: "Yogyakarta, Indonesia",
                hero_title: "FULL-STACK WORDPRESS <br>FRONT-END DEVELOPER",
                hero_desc: "Specialist in modern web architecture development, WordPress theme and plugin customization, and SEO from scratch, React.js integration, Core Web Vitals optimization, and AI/LLM workflow design for corporate business efficiency.",
                hero_btn_portfolio: "Explore Portfolio",
                hero_btn_email: "Contact via Email",
                hero_btn_linkedin: "LinkedIn Profile",
                btn_contact: "Contact Me",
                btn_linkedin: "LinkedIn Profile",
                
                stat_years: "Years of Technical Experience",
                stat_speed: "Web Speed Acceleration",
                stat_ai: "AI/LLM Workflow Efficiency",
                
                hud_title: "Developer Intelligence Status",
                hud_status: "● ACTIVE READY",
                hud_stack: "Tech Stack Matrix",
                hud_seo: "Technical SEO Audit",
                hud_cost: "Optimization ROI",
                hud_hackathon: "Fast Delivery",
                hud_export_lbl: "Certified Export Strategy",
                
                about_badge: "Profile & Track Record",
                about_title: "Technical Dedication & Expertise",
                about_subtitle: "Combining meticulous WordPress-based website development with the speed of modern React.js technology and artificial intelligence capabilities.",
                summary_title: "Profile Summary",
                summary_desc: "Full-Stack WordPress & Front-End Developer with over 3 years of experience in end-to-end web application development, WordPress theme/plugin customization, and Core Web Vitals optimization. Has a strong track record in managing and building corporate platforms and WooCommerce-based online stores by combining WordPress expertise with modern front-end technologies (React.js, Material UI, JavaScript). Proven ability to integrate technical SEO strategies, data analysis, and AI/LLM workflows to improve operational efficiency and system performance.",
                bento_summary_p1: "Full-Stack WordPress & Front-End Developer with over <strong>3 years</strong> of experience in end-to-end web application development cycles, WordPress theme & plugin customization, and Core Web Vitals optimization.",
                bento_summary_p2: "Proven track record in building multinational corporate platforms and WooCommerce-based online stores by combining WordPress expertise and modern front-end technologies (React.js, Material UI, JavaScript ES6+). Capable of integrating technical SEO strategies, data analysis, and Large Language Model (LLM) optimization to boost system performance and operational efficiency.",
                bento_skills_title: "Core Competencies & Skills",
                bento_edu_title: "Education & Background",
                edu_title: "Education",
                edu_degree: "Associate's Degree (D3) in Computer Science",
                edu_focus: "2022 – 2025 • Focused on Software Engineering & Web Systems",
                
                exp_badge: "Career Track",
                exp_title: "Work Experience",
                exp_subtitle: "Career journey and professional impact achieved",
                exp1_role: "WordPress & Web Developer / Lead AI Trainer",
                exp1_date: "2023 – Present",
                exp1_b1: "<strong>Theme & Plugin Customization from Scratch:</strong> Built custom plugins and themes using PHP and JavaScript, reducing client operational costs by 20%.",
                exp1_b2: "<strong>30% Organic Traffic Surge:</strong> Implemented comprehensive technical SEO strategies, including structured Schema Markup and keyword optimization via Rank Math & Yoast SEO and strengthening backlink profiles.",
                exp1_b3: "<strong>AI Education & Business Workshops:</strong> Speaker in seminars and technical workshops on coding fundamentals and LLM utilization, raising AI adoption by 60% in non-technical participants' daily operations.",
                
                exp2_role: "Global Digital Strategy & SEO Lead",
                exp2_date: "2022 – 2023",
                exp2_b1: "<strong>B2B Export Platform Engineering:</strong> Developed and managed integrated corporate export web platforms for coconut & charcoal products ensuring optimal performance status.",
                exp2_b2: "<strong>Dataset Validation & 30% Output Quality:</strong> Analyzed complex technical queries and validated machine learning dataset timelines to maintain high accuracy and system consistency.",
                exp2_b3: "Streamlined business operations using custom AI prompts and automation scripts.",
                
                exp3_date: "2021 – 2022",
                exp3_b1: "<strong>React.js & MUI Web Applications:</strong> Developed web applications and data management systems based on React.js with responsive Material UI components.",
                exp3_b2: "Implemented technical on-page SEO, increasing organic search visibility by over 40%.",
                exp3_b3: "Managed server configurations, DNS, SSL, and security hardening for corporate clients.",
                
                exp4_date: "2020 – 2021",
                exp4_b1: "<strong>Enterprise Financial Web Portals:</strong> Built interactive user interface modules for enterprise financial service platforms.",
                exp4_b2: "Tested cross-browser responsiveness across mobile, tablet, and desktop devices.",
                
                proj_badge: "Portfolio & Implementations",
                proj_title: "Project Collection by Category",
                proj_subtitle: "Explore high-performance websites I have engineered, ranging from global B2B export platforms and herbal e-commerce to national PVC ceiling manufacturing and hospitality brands.",
                filter_all: "All Projects",
                filter_export: "Export & Global B2B",
                filter_herbal: "Herbal & E-Commerce",
                filter_plafon: "PVC Ceiling & Industry",
                filter_travel: "Travel & Umrah",
                filter_personal: "Education & Personal",
                proj_detail: "Project Detail",
                modal_visit: "Visit Live Website",
                modal_specs: "Technical Highlights & Impact",
                modal_category_fallback: "Project Category",
                
                p1_badge: "Export & B2B",
                p1_desc: "International standard organic coco fiber export platform with targeted B2B SEO.",
                p1_tag: "Live B2B",
                
                p2_badge: "Export & B2B",
                p2_desc: "Export-grade coconut charcoal briquette manufacturing website with technical laboratory specs.",
                p2_tag: "B2B Export",
                
                p3_badge: "Industry & Factory",
                p3_desc: "Official website for the largest PVC ceiling manufacturer in Indonesia with a nationwide distributor network.",
                p3_tag: "Nationwide",
                
                p4_badge: "Herbal & E-Commerce",
                p4_desc: "High-conversion diabetes herbal product sales landing page with interactive checkout.",
                p4_tag: "E-Commerce",
                
                p5_badge: "Herbal & E-Commerce",
                p5_desc: "Premium royal etawa goat milk brand & sales platform featuring an elegant and fast UI.",
                p5_tag: "Herbal Product",
                
                p6_badge: "PVC Ceiling",
                p6_desc: "Modern decorative PVC ceiling specialist platform showcasing interior projects and installation guides.",
                p6_tag: "Modern PVC",
                
                p7_badge: "Hospitality & Resort",
                p7_desc: "Exclusive nature resort & cafe website featuring online room reservations and stunning visual galleries.",
                p7_tag: "Resort & Cafe",
                
                p8_badge: "Umrah & Hajj",
                p8_desc: "Trusted Umrah & Hajj travel agency platform displaying departure schedules and comprehensive packages.",
                p8_tag: "Umrah & Hajj",
                
                p9_badge: "Education & E-Comm",
                p9_desc: "Kids study desk WooCommerce store featuring custom character design selections and secure payments.",
                p9_tag: "E-Commerce",
                
                p10_badge: "Personal Branding",
                p10_desc: "Professional personal branding website featuring article publications, seminar schedules, and consulting.",
                p10_tag: "Branding",
                
                p11_badge: "Healthy Diet",
                p11_desc: "Low-calorie konjac rice sales and education platform for healthy diets with an interactive calorie calculator.",
                p11_tag: "Diet Food",
                
                p12_badge: "Construction Services",
                p12_desc: "Trusted PVC ceiling installation contractor in Yogyakarta featuring instant cost estimation tools.",
                p12_tag: "Local Service",
                
                ach_badge: "Recognition & Awards",
                ach_subtitle: "Proof of dedication, problem-solving capability, and tested competence in national technology competitions and professional certifications.",
                achieve_title: "National Awards & Certifications",
                achieve_subtitle: "Official awards and certifications earned",
                ach1_title: "2nd Winner — Digital Business Technology Competition (Hackathon)",
                ach1_date: "July 2023 • Digital Solution Innovation",
                ach2_title: "2nd Winner — National Digital Business Competition (AMICTA)",
                ach2_date: "July 2024 • Digital Business Model Category",
                ach3_title: "Digital Export Business Management Certification",
                ach3_date: "December 2024 • Nationally Licensed",
                
                footer_cta_title: "Ready to Build Something Extraordinary?",
                footer_cta_desc: "Whether you need a high-converting WordPress platform, a snappy React application, or technical SEO optimization, let's connect.",
                footer_contact_title: "Direct Contact",
                footer_nav_title: "Quick Navigation",
                footer_nav_exp: "Work Experience",
                footer_title: "Let's Collaborate!",
                footer_location: "Location: Yogyakarta, Indonesia",
                footer_brand_desc: "Full-Stack WordPress & Front-End Developer based in Yogyakarta, Indonesia. Dedicated to engineering interactive 3D web experiences, modern WordPress customization, and AI workflow optimization.",
                footer_copy: "© 2026 Rifandi Annas Shahruri. All Rights Reserved.",
                footer_tech: "Designed with Three.js WebGL & GSAP 3D Motion"
            },
            id: {
                nav_home: "Beranda",
                nav_about: "Profil",
                nav_experience: "Pengalaman",
                nav_projects: "Proyek",
                nav_achievements: "Prestasi",
                nav_contact: "Kontak",
                
                hero_location: "Yogyakarta, Indonesia",
                hero_title: "FULL-STACK WORDPRESS <br>FRONT-END DEVELOPER",
                hero_desc: "Spesialis dalam pengembangan arsitektur web modern, kustomisasi tema dan plugin WordPress, SEO dari awal, integrasi React.js, optimasi Core Web Vitals, dan perancangan alur kerja AI/LLM untuk efisiensi bisnis korporat.",
                hero_btn_portfolio: "Lihat Portofolio",
                hero_btn_email: "Hubungi via Email",
                hero_btn_linkedin: "Profil LinkedIn",
                btn_contact: "Hubungi Saya",
                btn_linkedin: "Profil LinkedIn",
                
                stat_years: "Tahun Pengalaman Teknis",
                stat_speed: "Akselerasi Kecepatan Web",
                stat_ai: "Efisiensi Alur Kerja AI/LLM",
                
                hud_title: "Status Intelijen Pengembang",
                hud_status: "● AKTIF & SIAP",
                hud_stack: "Matriks Tech Stack",
                hud_seo: "Audit SEO Teknis",
                hud_cost: "ROI Optimasi",
                hud_hackathon: "Pengiriman Cepat",
                hud_export_lbl: "Strategi Ekspor Tersertifikasi",
                
                about_badge: "Profil & Rekam Jejak",
                about_title: "Dedikasi Teknis & Keahlian",
                about_subtitle: "Menggabungkan ketelitian pengembangan website berbasis WordPress dengan kecepatan teknologi React.js modern serta kapabilitas kecerdasan buatan.",
                summary_title: "Ringkasan Profil",
                summary_desc: "Full-Stack WordPress & Front-End Developer dengan pengalaman lebih dari 3 tahun dalam pengembangan aplikasi web end-to-end, kustomisasi tema/plugin WordPress, dan optimasi Core Web Vitals. Memiliki rekam jejak yang kuat dalam mengelola dan membangun platform perusahaan serta toko online berbasis WooCommerce dengan menggabungkan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript). Kemampuan yang terbukti untuk mengintegrasikan strategi SEO teknis, analisis data, dan alur kerja AI/LLM guna meningkatkan efisiensi operasional dan performa sistem.",
                bento_summary_p1: "Full-Stack WordPress & Front-End Developer berpengalaman lebih dari <strong>3 tahun</strong> dalam siklus pengembangan aplikasi web end-to-end, kustomisasi tema & plugin WordPress, serta optimasi Core Web Vitals.",
                bento_summary_p2: "Rekam jejak terbukti dalam membangun platform korporat multinasional dan toko online berbasis WooCommerce dengan menggabungkan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript ES6+). Mampu mengintegrasikan strategi SEO teknis, analisis data, dan optimasi Large Language Model (LLM) guna mendongkrak performa sistem dan efisiensi operasional.",
                bento_skills_title: "Kompetensi Inti & Keahlian",
                bento_edu_title: "Pendidikan & Latar Belakang",
                edu_title: "Pendidikan",
                edu_degree: "Ahli Madya (D3) Ilmu Komputer",
                edu_focus: "2022 – 2025 • Fokus pada Rekayasa Perangkat Lunak & Sistem Web",
                
                exp_badge: "Jejak Karir",
                exp_title: "Pengalaman Kerja",
                exp_subtitle: "Perjalanan karir dan dampak profesional yang telah dicapai",
                exp1_role: "WordPress & Web Developer / Lead AI Trainer",
                exp1_date: "2023 – Sekarang",
                exp1_b1: "<strong>Kustomisasi Tema & Plugin dari Nol:</strong> Mengembangkan plugin dan theme kustom menggunakan PHP dan JavaScript, berhasil menekan biaya operasional klien hingga 20%.",
                exp1_b2: "<strong>Lonjakan Trafik Organik 30%:</strong> Menerapkan strategi SEO teknis menyeluruh, termasuk implementasi Schema Markup terstruktur dan optimasi kata kunci via Rank Math & Yoast SEO serta memperkuat profil backlink.",
                exp1_b3: "<strong>Edukasi AI & Workshop Bisnis:</strong> Menjadi pembicara dalam seminar dan pelatihan teknis tentang dasar pemrograman dan pemanfaatan Large Language Model (LLM), meningkatkan utilisasi AI hingga 60% dalam operasional harian peserta non-teknis.",
                
                exp2_role: "Global Digital Strategy & SEO Lead",
                exp2_date: "2022 – 2023",
                exp2_b1: "<strong>Pengembangan Platform Ekspor B2B:</strong> Mengembangkan serta mengelola platform web korporat ekspor kelapa & arang kelapa terintegrasi agar selalu beroperasi dalam status optimal.",
                exp2_b2: "<strong>Validasi Dataset & Kualitas Output 30%:</strong> Menganalisis kueri teknis kompleks dan memvalidasi linimasa dataset machine learning demi menjaga akurasi tinggi serta konsistensi sistem.",
                exp2_b3: "Menyederhanakan operasional bisnis menggunakan prompt kustom AI dan skrip otomasi.",
                
                exp3_date: "2021 – 2022",
                exp3_b1: "<strong>Aplikasi Web React.js & MUI:</strong> Mengembangkan aplikasi web dan sistem manajemen data berbasis React.js dengan komponen Material UI yang responsif.",
                exp3_b2: "Menerapkan SEO teknis on-page, meningkatkan visibilitas pencarian organik lebih dari 40%.",
                exp3_b3: "Mengelola konfigurasi server, DNS, SSL, dan pengamanan sistem klien korporat.",
                
                exp4_date: "2020 – 2021",
                exp4_b1: "<strong>Portal Web Korporat Finansial:</strong> Berkolaborasi dalam pengembangan dan pengujian modul tampilan antarmuka sistem web korporat perbankan dan sekuritas.",
                exp4_b2: "Menguji responsivitas lintas browser pada perangkat seluler, tablet, dan desktop.",
                
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
                modal_visit: "Kunjungi Situs Langsung",
                modal_specs: "Spesifikasi Teknis & Dampak Solusi",
                modal_category_fallback: "Kategori Proyek",
                
                p1_badge: "Ekspor & B2B",
                p1_desc: "Platform ekspor produk serat kelapa organik standar internasional dengan optimasi SEO pasar B2B.",
                p1_tag: "Live B2B",
                
                p2_badge: "Ekspor & B2B",
                p2_desc: "Situs profil pabrik arang briket batok kelapa grade ekspor dengan showcase spesifikasi teknis.",
                p2_tag: "Ekspor B2B",
                
                p3_badge: "Industri & Pabrik",
                p3_desc: "Situs web resmi pabrik manufaktur plafon PVC dengan jaringan distributor nasional terbesar.",
                p3_tag: "Nasional",
                
                p4_badge: "Herbal & E-Commerce",
                p4_desc: "Landing page penjualan produk herbal diabetes dengan rasio konversi tinggi dan checkout interaktif.",
                p4_tag: "E-Commerce",
                
                p5_badge: "Herbal & E-Commerce",
                p5_desc: "Platform branding dan penjualan susu kambing etawa royal premium dengan UI elegan & cepat.",
                p5_tag: "Produk Herbal",
                
                p6_badge: "Plafon PVC",
                p6_desc: "Website spesialis plafon dekoratif modern dengan portofolio proyek interior dan panduan pasang.",
                p6_tag: "PVC Modern",
                
                p7_badge: "Hospitality & Resort",
                p7_desc: "Website resort eksklusif bernuansa alam terbuka dengan reservasi kamar online dan galeri visual memukau.",
                p7_tag: "Resort & Cafe",
                
                p8_badge: "Umroh & Haji",
                p8_desc: "Website biro umroh & haji plus terpercaya dengan jadwal keberangkatan dan katalog paket ibadah lengkap.",
                p8_tag: "Umroh & Haji",
                
                p9_badge: "Edukasi & E-Comm",
                p9_desc: "Toko online meja belajar anak dengan WooCommerce, fitur custom desain karakter dan pembayaran aman.",
                p9_tag: "E-Commerce",
                
                p10_badge: "Personal Branding",
                p10_desc: "Website personal branding profesional dengan publikasi artikel, jadwal pelatihan dan konsultasi bisnis.",
                p10_tag: "Branding",
                
                p11_badge: "Diet Sehat",
                p11_desc: "Platform edukasi dan penjualan beras porang rendah kalori untuk program diet sehat dengan kalkulator kalori.",
                p11_tag: "Makanan Diet",
                
                p12_badge: "Jasa Konstruksi",
                p12_desc: "Platform penyedia jasa pemasangan plafon PVC terpercaya di area Yogyakarta dengan fitur estimasi biaya cepat.",
                p12_tag: "Jasa Lokal",
                
                ach_badge: "Pengakuan & Prestasi",
                ach_subtitle: "Bukti dedikasi, kemampuan pemecahan masalah, dan kompetensi teruji dalam kompetisi teknologi nasional serta sertifikasi profesional.",
                achieve_title: "Penghargaan & Sertifikasi Nasional",
                achieve_subtitle: "Penghargaan dan sertifikasi resmi yang diperoleh",
                ach1_title: "Juara 2 — Kompetisi Teknologi Bisnis Digital (Hackathon)",
                ach1_date: "Juli 2023 • Inovasi Solusi Digital",
                ach2_title: "Juara 2 — Kompetisi Bisnis Digital Nasional (AMICTA)",
                ach2_date: "Juli 2024 • Kategori Model Bisnis Digital",
                ach3_title: "Sertifikasi Manajemen Bisnis Ekspor Digital",
                ach3_date: "Desember 2024 • Lisensi Nasional BNSP",
                
                footer_cta_title: "Siap Membangun Sesuatu yang Luar Biasa?",
                footer_cta_desc: "Baik Anda membutuhkan platform WordPress dengan konversi tinggi, aplikasi React cepat, atau optimasi SEO teknis, mari berdiskusi.",
                footer_contact_title: "Kontak Langsung",
                footer_nav_title: "Navigasi Cepat",
                footer_nav_exp: "Pengalaman Kerja",
                footer_title: "Mari Berkolaborasi!",
                footer_location: "Lokasi: Yogyakarta, Indonesia",
                footer_brand_desc: "Full-Stack WordPress & Front-End Developer berbasis di Yogyakarta, Indonesia. Berdedikasi menciptakan pengalaman web interaktif 3D, kustomisasi WordPress mutakhir, dan pengoptimalan teknologi AI.",
                footer_copy: "© 2026 Rifandi Annas Shahruri. Hak Cipta Dilindungi.",
                footer_tech: "Dirancang dengan Three.js WebGL & Animasi 3D GSAP"
            }
        };

        /* ===================================================
           LOGIKA SWITCHER BAHASA (OPTIMIZED & PERSISTENT)
           =================================================== */
        let currentLang = localStorage.getItem('site_lang') || 'en';

        function updateButtonUI(lang) {
            const btnText = document.getElementById('lang-text');
            if (btnText) {
                // Clear and neat button showing current language & toggle
                if (lang === 'en') {
                    btnText.innerHTML = '<span style="color:#2563EB; font-weight:800;">EN</span> <span style="opacity:0.4;">|</span> <span style="color:#6B7280; font-weight:500;">ID</span>';
                } else {
                    btnText.innerHTML = '<span style="color:#6B7280; font-weight:500;">EN</span> <span style="opacity:0.4;">|</span> <span style="color:#2563EB; font-weight:800;">ID</span>';
                }
            }
            document.documentElement.setAttribute('lang', lang);
        }

        function setLanguage(lang) {
            currentLang = lang;
            localStorage.setItem('site_lang', lang);
            updateButtonUI(lang);

            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(element => {
                const key = element.getAttribute('data-i18n');
                if (translations[lang] && translations[lang][key] !== undefined) {
                    element.innerHTML = translations[lang][key];
                }
            });
        }

        // Initialize immediately
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => setLanguage(currentLang));
        } else {
            setLanguage(currentLang);
        }

        // Click listener for Toggle
        document.getElementById('lang-toggle')?.addEventListener('click', () => {
            const nextLang = currentLang === 'en' ? 'id' : 'en';
            setLanguage(nextLang);
        });
    </script>
'''

# Replace script at the bottom
script_start = content.rfind('<!-- Language Switcher &')
if script_start != -1:
    body_idx = content.rfind('</body>')
    content = content[:script_start] + master_script.strip() + '\n\n' + content[body_idx:]

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Master translations and complete coverage applied successfully!")
