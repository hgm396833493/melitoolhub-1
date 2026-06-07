import os
import re

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 标准导航栏HTML（中文）
standard_nav = '''<div class="nav-links" id="nav-links">
<a href="index.html" data-i18n="nav_home">首页</a>
<a href="index.html#articles" data-i18n="nav_articles">跨境干货</a>
<a href="index.html#policy" data-i18n="nav_policy">政策合规</a>
<a href="index.html#tools" data-i18n="nav_tools">实用工具</a>
<a href="index.html#sourcing" data-i18n="nav_sourcing">采购代办</a>
<a href="index.html#partners" data-i18n="nav_partners">联盟工具</a>
<a href="index.html#community" data-i18n="nav_community">用户交流</a>
</div>'''

modified = 0
for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找现有的 nav-links div
        nav_pattern = r'<div class="nav-links"[^>]*>[\s\S]*?</div>\s*(?=</nav>|<div class="nav-actions")'
        
        if re.search(nav_pattern, content):
            # 替换整个 nav-links 内容
            content = re.sub(nav_pattern, standard_nav.strip(), content)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified += 1
            print(f'Modified: {fname}')
        else:
            print(f'Skipped (no nav-links): {fname}')
    except Exception as e:
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified {modified} files')
