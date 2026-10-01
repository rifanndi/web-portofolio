import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/web-portofolio/untranslated.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(min(50, len(items))):
    it = items[i]
    p = it['path']
    c = it['class']
    t = it['text']
    print(f"{i+1}. [{p}] ({c}) -> {t}")
