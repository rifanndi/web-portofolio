import re
import codecs

file_path = 'index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Update CSS variables for the requested color scheme
content = re.sub(
    r'--bg-deep:.*?;',
    '--bg-deep: #0B131B;',
    content
)
content = re.sub(
    r'--bg-card:.*?;',
    '--bg-card: rgba(11, 19, 27, 0.65);',
    content
)
content = re.sub(
    r'--tone-cyan:.*?;',
    '--tone-cyan: #2C858A;',
    content
)
content = re.sub(
    r'--tone-purple:.*?;',
    '--tone-purple: #F39C12;',
    content
)

# 2. Add language toggle to navbar
lang_toggle_html = '''
            <div class="lang-toggle" style="display:flex; gap:8px; margin-left: 20px; align-items:center;">
                <button id="btn-id" style="background:var(--tone-cyan); color:#fff; border:none; padding:4px 10px; border-radius:12px; cursor:pointer; font-size:0.8rem; font-weight:bold;">ID</button>
                <button id="btn-en" style="background:transparent; color:var(--text-muted); border:1px solid var(--text-muted); padding:4px 10px; border-radius:12px; cursor:pointer; font-size:0.8rem; font-weight:bold;">EN</button>
            </div>
'''
content = content.replace('</nav>', lang_toggle_html + '</nav>')

# 3. Add Bento grid CSS
bento_css = '''
        /* Game-Inspired Sci-Fi HUD Bento Layout */
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            grid-auto-rows: minmax(180px, auto);
        }
        .bento-item {
            background: linear-gradient(135deg, rgba(44, 133, 138, 0.1), rgba(11, 19, 27, 0.8));
            border: 1px solid rgba(44, 133, 138, 0.3);
            border-radius: 24px;
            padding: 24px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        .bento-item:hover {
            transform: translateY(-5px);
            border-color: var(--tone-purple);
            box-shadow: 0 10px 40px rgba(243, 156, 18, 0.2);
        }
        .bento-span-2 {
            grid-column: span 2;
        }
        .bento-span-3 {
            grid-column: span 3;
        }
        .bento-row-2 {
            grid-row: span 2;
        }
        .bento-floating-num {
            position: absolute;
            top: 15px;
            right: 15px;
            font-family: var(--font-mono);
            font-size: 2rem;
            color: rgba(255,255,255,0.05);
            font-weight: 900;
        }
        .bento-card-title {
            font-family: var(--font-display);
            font-size: 1.2rem;
            color: var(--tone-cyan);
            margin-bottom: 12px;
        }
        @media (max-width: 900px) {
            .bento-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 600px) {
            .bento-grid {
                grid-template-columns: 1fr;
            }
        }
'''
content = content.replace('</style>', bento_css + '</style>')

# 4. Refactor About section into Bento Grid
about_html_new = '''
            <div class="bento-grid">
                <div class="bento-item bento-span-2 bento-row-2" data-id="Ringkasan Profesional" data-en="Professional Summary">
                    <div class="bento-floating-num">01</div>
                    <h3 class="bento-card-title" data-id="Ringkasan Profesional" data-en="Professional Summary">Ringkasan Profesional</h3>
                    <p class="about-bio-text" data-id="Full-Stack WordPress & Front-End Developer berpengalaman lebih dari 3 tahun..." data-en="Full-Stack WordPress & Front-End Developer with over 3 years of experience...">Full-Stack WordPress & Front-End Developer berpengalaman lebih dari <strong>3 tahun</strong> dalam siklus pengembangan aplikasi web end-to-end, kustomisasi tema & plugin WordPress, serta optimasi Core Web Vitals.</p>
                    <p class="about-bio-text" data-id="Memiliki rekam jejak yang teruji..." data-en="Proven track record in building multinational corporate platforms...">Memiliki rekam jejak yang teruji dalam membangun platform korporat multinasional dan toko online berbasis WooCommerce dengan mengombinasikan keahlian WordPress dan teknologi front-end modern (React.js, Material UI, JavaScript ES6+). Mampu mengintegrasikan strategi SEO teknis, analisis data, serta optimalisasi Large Language Model (LLM) untuk mendongkrak performa sistem dan efisiensi operasional.</p>
                </div>
                <div class="bento-item bento-span-2" data-id="Pendidikan" data-en="Education">
                    <div class="bento-floating-num">02</div>
                    <h3 class="bento-card-title" data-id="Pendidikan" data-en="Education">Pendidikan</h3>
                    <div class="edu-card" style="background:transparent; border:none; padding:0;">
                        <div class="edu-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                        </div>
                        <div class="edu-details">
                            <h4>Universitas AMIKOM Yogyakarta</h4>
                            <div class="degree">Associate's Degree (D3) in Computer Science</div>
                            <div class="year">2022 – 2025 • Fokus pada Rekayasa Perangkat Lunak & Sistem Web</div>
                        </div>
                    </div>
                </div>
                <div class="bento-item bento-span-2">
                    <div class="bento-floating-num">03</div>
                    <h3 class="bento-card-title" data-id="Keahlian Utama" data-en="Core Skills">Keahlian Utama</h3>
                    <div class="skill-pills">
                        <span class="skill-pill">Custom Theme & Plugin Dev</span>
                        <span class="skill-pill">React.js & Material UI (MUI)</span>
                        <span class="skill-pill highlight">Technical SEO & Schema Markup</span>
                        <span class="skill-pill">LLM Prompt & Workflow</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''
content = re.sub(r'<div class="about-layout">.*?</div>\s*</div>\s*</section>', about_html_new, content, flags=re.DOTALL)

# 5. Add scripts for Translation & Typing Effect
js_scripts = '''
        /* Translation Script */
        const translations = {
            id: {
                'Beranda': 'Beranda', 'Profil & Keahlian': 'Profil & Keahlian', 'Pengalaman': 'Pengalaman', 'Koleksi Proyek': 'Koleksi Proyek', 'Prestasi': 'Prestasi', 'Kontak': 'Kontak',
                'Membangun Web<br>': 'Membangun Web<br>', '<span class="text-glow">Cepat, Berdampak</span><br>': '<span class="text-glow">Cepat, Berdampak</span><br>', '& Bertenaga AI': '& Bertenaga AI'
            },
            en: {
                'Beranda': 'Home', 'Profil & Keahlian': 'Profile & Skills', 'Pengalaman': 'Experience', 'Koleksi Proyek': 'Projects', 'Prestasi': 'Achievements', 'Kontak': 'Contact',
                'Membangun Web<br>': 'Building Web<br>', '<span class="text-glow">Cepat, Berdampak</span><br>': '<span class="text-glow">Fast, Impactful</span><br>', '& Bertenaga AI': '& AI-Powered'
            }
        };

        document.getElementById('btn-en')?.addEventListener('click', () => {
            document.querySelectorAll('[data-en]').forEach(el => el.innerHTML = el.getAttribute('data-en'));
            document.getElementById('btn-en').style.background = 'var(--tone-cyan)';
            document.getElementById('btn-en').style.color = '#fff';
            document.getElementById('btn-en').style.border = 'none';
            document.getElementById('btn-id').style.background = 'transparent';
            document.getElementById('btn-id').style.color = 'var(--text-muted)';
            document.getElementById('btn-id').style.border = '1px solid var(--text-muted)';
        });

        document.getElementById('btn-id')?.addEventListener('click', () => {
            document.querySelectorAll('[data-id]').forEach(el => el.innerHTML = el.getAttribute('data-id'));
            document.getElementById('btn-id').style.background = 'var(--tone-cyan)';
            document.getElementById('btn-id').style.color = '#fff';
            document.getElementById('btn-id').style.border = 'none';
            document.getElementById('btn-en').style.background = 'transparent';
            document.getElementById('btn-en').style.color = 'var(--text-muted)';
            document.getElementById('btn-en').style.border = '1px solid var(--text-muted)';
        });

        /* Typing Effect for Hero Subtitle */
        const typingEl = document.querySelector('.hero-desc');
        if(typingEl) {
            const originalTextID = typingEl.innerText;
            typingEl.setAttribute('data-id', originalTextID);
            typingEl.setAttribute('data-en', 'Specialist in modern web architecture, WordPress theme & plugin customization from scratch, React.js integration, Core Web Vitals optimization, and AI/LLM workflow deduction for corporate business efficiency.');
            
            typingEl.innerHTML = '';
            let charIndex = 0;
            function typeWriter() {
                const text = typingEl.getAttribute('data-id');
                if (charIndex < text.length) {
                    typingEl.innerHTML += text.charAt(charIndex);
                    charIndex++;
                    setTimeout(typeWriter, 20);
                } else {
                    typingEl.innerHTML += '<span class="type-cursor">|</span>';
                }
            }
            setTimeout(typeWriter, 1000);
        }
'''
content = content.replace('</script>\n</body>', js_scripts + '\n</script>\n</body>')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
