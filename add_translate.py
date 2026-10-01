import codecs
import re

file_path = 'e:/web-portofolio/index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Replace manual toggle with Google Translate Widget
manual_toggle_regex = r'<div class="lang-toggle".*?</div>'
translate_widget = '''
            <div id="google_translate_element" style="margin-left: 15px; display:flex; align-items:center;"></div>
            <script type="text/javascript">
            function googleTranslateElementInit() {
              new google.translate.TranslateElement({
                pageLanguage: 'id', 
                includedLanguages: 'en,id', 
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
              }, 'google_translate_element');
            }
            </script>
            <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
'''

if re.search(manual_toggle_regex, content, flags=re.DOTALL):
    content = re.sub(manual_toggle_regex, translate_widget, content, flags=re.DOTALL)
else:
    # If not found, inject before </nav>
    content = content.replace('</nav>', translate_widget + '</nav>')

# Optional: Add some CSS to make the Google Translate widget look cleaner and hide the top Google bar
clean_translate_css = '''
        /* Google Translate Widget Clean up */
        .goog-te-gadget-simple {
            background-color: var(--bg-card) !important;
            border: 1px solid var(--border-glass) !important;
            border-radius: 8px !important;
            padding: 4px 8px !important;
            font-family: var(--font-body) !important;
        }
        .goog-te-gadget-icon {
            display: none;
        }
        .goog-te-menu-value {
            color: var(--text-main) !important;
        }
        .goog-te-banner-frame {
            display: none !important;
        }
        body {
            top: 0 !important;
        }
'''
content = content.replace('</style>', clean_translate_css + '</style>')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
