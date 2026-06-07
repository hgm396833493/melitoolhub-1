import os

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 桌面端导航样式（需要添加到 <style> 标签内）
desktop_nav_css = '''.nav-links{display:flex;gap:2px;flex-wrap:wrap}
.nav-links a{color:rgba(255,255,255,.82);font-size:.85rem;padding:7px 12px;border-radius:6px;transition:.2s;white-space:nowrap}
.nav-links a:hover,.nav-links a.active{background:rgba(255,255,255,.14);color:#fff}
.nav-toggle{display:none;background:none;border:none;color:#fff;font-size:1.6rem;cursor:pointer;padding:4px 8px}
'''

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有桌面端 .nav-links{display:flex
        if '.nav-links{display:flex' in content:
            print(f'Skipped (has desktop): {fname}')
            continue
        
        # 检查是否有 <style> 标签
        if '<style>' not in content:
            print(f'Error: {fname} has no <style> tag')
            errors += 1
            continue
        
        # 在 <style> 标签后添加桌面导航样式
        style_pos = content.find('<style>') + 7
        before = content[:style_pos]
        after = content[style_pos:]
        
        new_content = before + '\n/* Nav */\n' + desktop_nav_css + after
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified += 1
        print(f'Added desktop nav: {fname}')
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
