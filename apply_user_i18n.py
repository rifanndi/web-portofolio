import codecs
import re

file_path = 'e:/web-portofolio/index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Clean up any previous language toggle in the HTML
content = re.sub(
    r'<div id="google_translate_element".*?</script>\s*<script type="text/javascript" src="//translate\.google\.com.*?</script>',
    '',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<button class="btn-lang-toggle".*?</button>',
    '',
    content,
    flags=re.DOTALL
)

# 2. Add their button to the Navbar HTML
new_btn = '''
            <button id="lang-toggle" class="btn-lang">
                <span id="lang-text">EN | ID</span>
            </button>'''

if 'id="navToggle"' in content:
    content = content.replace(
        '<button class="nav-toggle" id="navToggle"',
        new_btn + '\n            <button class="nav-toggle" id="navToggle"'
    )

# 3. Add their CSS
user_css = '''
        .btn-lang {
            background: rgba(0, 242, 254, 0.1);
            border: 1px solid #00f2fe;
            color: #00f2fe;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-lang:hover {
            background: #00f2fe;
            color: #080b14;
        }
'''
if '.btn-lang' not in content:
    content = content.replace('</style>', user_css + '</style>')

# 4. Add their JS
user_js = '''
        /* ===================================================
           DICTIONARY / KAMUS BAHASA (EN & ID)
           =================================================== */
        const translations = {
            en: {
                nav_home: "Home",
                nav_about: "About",
                nav_experience: "Experience",
                nav_achievements: "Achievements",
                
                hero_location: "Yogyakarta, Indonesia",
                hero_title: "Full-Stack WordPress & Front-End Developer",
                hero_desc: "Experienced Web Developer with 3+ years in custom WordPress themes/plugins, React.js integration, technical SEO, Core Web Vitals, and AI/LLM workflow optimization for business efficiency.",
                btn_contact: "Contact Me",
                btn_linkedin: "LinkedIn Profile",

                about_title: "Profile & Skills",
                about_subtitle: "Summary of professional qualifications and technical stack",
                summary_title: "Profile Summary",
                summary_desc: "Full-Stack WordPress & Front-End Developer with over 3 years of experience in end-to-end web application development, WordPress theme/plugin customization, and Core Web Vitals optimization. Has a strong track record in managing and building corporate platforms and WooCommerce-based online stores by combining WordPress expertise with modern front-end technologies (React.js, Material UI, JavaScript). Proven ability to integrate technical SEO strategies, data analysis, and AI/LLM workflows to improve operational efficiency and system performance.",
                edu_title: "Education",

                exp_title: "Work Experience",
                exp_subtitle: "Career journey and professional impact achieved",

                achieve_title: "Achievements & Certifications",
                achieve_subtitle: "Official awards and certifications earned",

                footer_title: "Let's Collaborate!",
                footer_location: "Location: Yogyakarta, Indonesia"
            },
            id: {
                nav_home: "Beranda",
                nav_about: "Profil",
                nav_experience: "Pengalaman",
                nav_achievements: "Prestasi",
                
                hero_location: "Yogyakarta, Indonesia",
                hero_title: "Full-Stack WordPress & Front-End Developer",
                hero_desc: "Pengembang web berpengalaman 3+ tahun dalam kustomisasi tema/plugin WordPress, integrasi React.js, SEO teknis, Core Web Vitals, serta pengoptimalan alur kerja AI/LLM untuk efisiensi bisnis.",
                btn_contact: "Hubungi Saya",
                btn_linkedin: "Profil LinkedIn",

                about_title: "Profil & Keahlian",
                about_subtitle: "Ringkasan kualifikasi profesional dan teknologi yang dikuasai",
                summary_title: "Ringkasan Profil",
                summary_desc: "Full-Stack WordPress & Front-End Developer dengan pengalaman lebih dari 3 tahun dalam pengembangan aplikasi web end-to-end, kustomisasi tema/plugin WordPress, dan optimasi Core Web Vitals. Memiliki rekam jejak yang kuat dalam mengelola dan membangun platform perusahaan serta toko online berbasis WooCommerce dengan menggabungkan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript). Kemampuan yang terbukti untuk mengintegrasikan strategi SEO teknis, analisis data, dan alur kerja AI/LLM guna meningkatkan efisiensi operasional dan performa sistem.",
                edu_title: "Pendidikan",

                exp_title: "Pengalaman Kerja",
                exp_subtitle: "Perjalanan karir dan dampak profesional yang telah dicapai",

                achieve_title: "Prestasi & Sertifikasi",
                achieve_subtitle: "Penghargaan dan sertifikasi resmi yang diperoleh",

                footer_title: "Mari Berkolaborasi!",
                footer_location: "Lokasi: Yogyakarta, Indonesia"
            }
        };

        /* ===================================================
           LOGIK SWITCHER BAHASA
           =================================================== */
        let currentLang = localStorage.getItem('site_lang') || 'en';

        function setLanguage(lang) {
            currentLang = lang;
            localStorage.setItem('site_lang', lang);
            
            const btnText = document.getElementById('lang-text');
            if (btnText) btnText.innerText = lang === 'en' ? 'EN | ID' : 'ID | EN';

            const elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(element => {
                const key = element.getAttribute('data-i18n');
                if (translations[lang] && translations[lang][key]) {
                    element.innerText = translations[lang][key];
                }
            });
        }

        document.addEventListener('DOMContentLoaded', () => {
            setLanguage(currentLang);
        });

        document.getElementById('lang-toggle')?.addEventListener('click', () => {
            const nextLang = currentLang === 'en' ? 'id' : 'en';
            setLanguage(nextLang);
        });
'''

# Remove any old i18n script blocks if any
content = re.sub(
    r'/\* ==========================================================================\s*i18n LANGUAGE SWITCHER.*?\}\);',
    '',
    content,
    flags=re.DOTALL
)

if 'const translations =' not in content:
    content = content.replace('</body>', user_js + '\n</body>')

# Update the experience section based on the resume
content = re.sub(
    r'<div class="timeline-meta">\s*<div class="timeline-role">WordPress & Front-End Developer / Lead AI Trainer</div>',
    '<div class="timeline-meta">\n<div class="timeline-role">WordPress & Web Developer / Lead AI Trainer</div>',
    content,
    flags=re.DOTALL
)

# Apply HTML replacements with data-i18n
# Just a few examples as per user dictionary:
replacements = [
    ('<a href="#hero" class="active" data-i18n="nav_home">Home</a>', '<a href="#hero" class="active" data-i18n="nav_home">Home</a>'),
    ('<h2 class="section-title" data-i18n="about_title">Technical Dedication &amp; Expertise</h2>', '<h2 class="section-title" data-i18n="about_title">Profile & Skills</h2>'),
    ('<h3 class="bento-card-title" data-i18n="bento_summary_title">Professional Summary</h3>', '<h3 class="bento-card-title" data-i18n="summary_title">Profile Summary</h3>'),
    ('<h2 class="section-title" data-i18n="exp_title">Work Experience</h2>', '<h2 class="section-title" data-i18n="exp_title">Work Experience</h2>'),
    ('<h2 class="section-title" data-i18n="ach_title">Awards &amp; National Certifications</h2>', '<h2 class="section-title" data-i18n="achieve_title">Achievements & Certifications</h2>'),
    ('<span data-i18n="footer_cta_btn">Start Consultation</span>', '<span data-i18n="btn_contact">Contact Me</span>')
]
for old, new in replacements:
    content = content.replace(old, new)


with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
