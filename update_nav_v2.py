import os
import re

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 标准导航栏链接（中文）
standard_links = '''
<a href="index.html" data-i18n="nav_home">首页</a>
<a href="index.html#articles" data-i18n="nav_articles">跨境干货</a>
<a href="index.html#policy" data-i18n="nav_policy">政策合规</a>
<a href="index.html#tools" data-i18n="nav_tools">实用工具</a>
<a href="index.html#sourcing" data-i18n="nav_sourcing">采购代办</a>
<a href="index.html#partners" data-i18n="nav_partners">联盟工具</a>
<a href="index.html#community" data-i18n="nav_community">用户交流</a>
'''

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 方法1: 查找 <div class="nav-links" ...> 直到 </div>
        # 使用更灵活的正则表达式
        pattern1 = r'(<div class="nav-links"[^>]*>)[\s\S]*?(</div>)'
        
        if re.search(pattern1, content):
            # 保留开头的 <div> 标签和结尾的 </div>
            replacement = r'\1' + standard_links + r'\2'
            new_content = re.sub(pattern1, replacement, content)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
            print(f'Modified: {fname}')
        else:
            # 方法2: 尝试查找任何包含 nav 相关链接的 div
            if 'nav-links' in content or 'navLinks' in content:
                print(f'Warning: {fname} has nav but pattern not matched')
            else:
                print(f'Skipped: {fname} (no navigation found)')
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
