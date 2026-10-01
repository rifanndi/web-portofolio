import re
import codecs

file_path = 'index.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Update CSS variables to a clean light mode
content = re.sub(
    r'--bg-deep:.*?;',
    '--bg-deep: #F9FAFB;',
    content
)
content = re.sub(
    r'--bg-card:.*?;',
    '--bg-card: rgba(255, 255, 255, 0.85);',
    content
)
content = re.sub(
    r'--bg-card-hover:.*?;',
    '--bg-card-hover: rgba(255, 255, 255, 1);',
    content
)
content = re.sub(
    r'--border-glass:.*?;',
    '--border-glass: rgba(0, 0, 0, 0.08);',
    content
)
content = re.sub(
    r'--border-glow:.*?;',
    '--border-glow: rgba(0, 0, 0, 0.1);',
    content
)
content = re.sub(
    r'--tone-cyan:.*?;',
    '--tone-cyan: #2563EB;', # Clean Royal Blue
    content
)
content = re.sub(
    r'--tone-purple:.*?;',
    '--tone-purple: #10B981;', # Clean Emerald Green
    content
)
content = re.sub(
    r'--text-main:.*?;',
    '--text-main: #111827;', # Dark Gray for readability
    content
)
content = re.sub(
    r'--text-muted:.*?;',
    '--text-muted: #4B5563;',
    content
)
content = re.sub(
    r'--text-dim:.*?;',
    '--text-dim: #6B7280;',
    content
)

# 2. Modify hardcoded colors and neon shadows in the file using regex or replace
# Remove text-glow gradient class styling and replace with simple clean styling
content = content.replace('linear-gradient(135deg, #ffffff 20%, #cbd5e1 50%, var(--tone-cyan) 100%)', 'var(--text-main)')
content = content.replace('linear-gradient(135deg, #ffffff 20%, var(--tone-cyan) 60%, var(--tone-purple) 100%)', 'var(--text-main)')
content = content.replace('color: #cbd5e1;', 'color: var(--text-muted);')
content = content.replace('color: #ffffff;', 'color: var(--text-main);')
content = content.replace('color: #05070e;', 'color: #ffffff;')

# Fix navbar backgrounds
content = content.replace('background: rgba(5, 7, 14, 0.6);', 'background: rgba(255, 255, 255, 0.8);')
content = content.replace('background: rgba(5, 7, 14, 0.92);', 'background: rgba(255, 255, 255, 0.98);')
content = content.replace('background: rgba(5, 7, 14, 0.98);', 'background: rgba(255, 255, 255, 0.98);')
content = content.replace('background: rgba(5, 7, 14, 0.85);', 'background: rgba(255, 255, 255, 0.85);')
content = content.replace('background: rgba(5, 7, 14, 0.8);', 'background: rgba(255, 255, 255, 0.8);')

# Fix bento grid background & shadows
content = content.replace('background: linear-gradient(135deg, rgba(44, 133, 138, 0.1), rgba(11, 19, 27, 0.8));', 'background: #FFFFFF;')
content = content.replace('border: 1px solid rgba(44, 133, 138, 0.3);', 'border: 1px solid rgba(0,0,0,0.05);')
content = content.replace('box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);', 'box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);')
content = content.replace('box-shadow: 0 10px 40px rgba(243, 156, 18, 0.2);', 'box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);')

# Fix glass card
content = content.replace('box-shadow: 0 12px 35px rgba(0, 0, 0, 0.45);', 'box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);')
content = content.replace('box-shadow: 0 20px 50px rgba(0, 242, 254, 0.12), 0 0 30px rgba(155, 81, 224, 0.08);', 'box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);')

# Fix Hero HUD Card
content = content.replace('background: linear-gradient(135deg, rgba(13, 18, 36, 0.8), rgba(20, 28, 55, 0.6));', 'background: #FFFFFF;')
content = content.replace('border: 1px solid rgba(0, 242, 254, 0.2);', 'border: 1px solid rgba(0,0,0,0.05);')
content = content.replace('box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), inset 0 0 30px rgba(0, 242, 254, 0.05);', 'box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);')
content = content.replace('background: rgba(5, 7, 14, 0.5);', 'background: #F9FAFB;')
content = content.replace('background: linear-gradient(135deg, #0d1224, #141c37);', 'background: #FFFFFF;')
content = content.replace('box-shadow: 0 15px 35px rgba(0, 242, 254, 0.2);', 'box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);')

# Remove Cyber Grid
content = content.replace('background-image: \n                linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),\n                linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);', 'background-image: none;')

# Fix 3D Renderer (Make stars/lights darker or different color to show on white bg)
content = content.replace('color: 0x00f2fe,', 'color: 0x2563EB,')
content = content.replace('color: 0x9b51e0,', 'color: 0x10B981,')
content = content.replace('0x3d007a', '0xd1d5db')
content = content.replace('new THREE.Color(0x00f2fe);', 'new THREE.Color(0x3B82F6);')
content = content.replace('new THREE.Color(0x9b51e0);', 'new THREE.Color(0x10B981);')
content = content.replace('opacity: 0.22', 'opacity: 0.15')
content = content.replace('opacity: 0.75', 'opacity: 0.3')

# Fix custom cursor follower text color
content = content.replace('color: #05070e;', 'color: #FFFFFF;')

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
