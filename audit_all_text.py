import html.parser
import re
import json

with open('e:/web-portofolio/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

body_start = html_content.find('<body')
script_start = html_content.rfind('<!-- Three.js Library -->')
if script_start == -1:
    script_start = html_content.rfind('<script')

body_content = html_content[body_start:script_start]

class TextAuditParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.untranslated = []
        self.translated = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        has_i18n = 'data-i18n' in attrs_dict
        self.stack.append((tag, attrs_dict, has_i18n))

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        text = data.strip()
        if not text or len(text) <= 1:
            return
        has_ancestor_i18n = any(item[2] for item in self.stack)
        current_tag = self.stack[-1] if self.stack else ('unknown', {}, False)
        
        if any(item[0] in ['script', 'style', 'svg', 'path', 'polyline', 'polygon', 'line', 'circle', 'rect'] for item in self.stack):
            return

        if re.match(r'^[\d\+\%\.\,\—\-\/\(\)\s\•\:\@\●\✓]+$', text):
            return

        # ignore names like "Rifandi", "Annas S."
        if text in ["Rifandi", "Annas S.", "Rifandi Annas Shahruri", "EN | ID"]:
            return

        if has_ancestor_i18n:
            self.translated.append({'tag': current_tag[0], 'text': text})
        else:
            path = " > ".join([item[0] for item in self.stack])
            classes = current_tag[1].get('class', '')
            self.untranslated.append({'path': path, 'class': classes, 'text': text})

parser = TextAuditParser()
parser.feed(body_content)

print(f"Total translated: {len(parser.translated)}")
print(f"Total untranslated: {len(parser.untranslated)}")

with open('e:/web-portofolio/untranslated.json', 'w', encoding='utf-8') as f:
    json.dump(parser.untranslated, f, indent=2, ensure_ascii=False)

print("Saved untranslated list to untranslated.json")
