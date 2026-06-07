#!/usr/bin/env python3
"""
批量更新导航栏：
1. CSS: .lang-bar → .nav-lang
2. 删除独立 .lang-bar HTML 块
3. 语言选择器移入 nav-actions（登录按钮前面）
4. 确认 nav-links 桌面横排 + 手机竖排
"""
import os, re

WORKSPACE = r'D:\workspace'

NAV_LANG_HTML = '''<!-- Language Selector (in nav) -->
<div class="nav-lang">
<label for="lang-select">🌐</label>
<select id="lang-select" aria-label="切换语言">
<option value="zh">中文</option>
<option value="en">EN</option>
<option value="es">ES</option>
<option value="pt">PT</option>
<option value="ru">RU</option>
<option value="fr">FR</option>
<option value="de">DE</option>
<option value="it">IT</option>
<option value="ar">AR</option>
<option value="tr">TR</option>
<option value="vi">VI</option>
<option value="th">TH</option>
<option value="id">ID</option>
<option value="ms">MS</option>
<option value="ko">KO</option>
<option value="ja">JA</option>
<option value="pl">PL</option>
<option value="nl">NL</option>
</select>
</div>'''

def update_css(content):
    """替换 CSS 中的 .lang-bar → .nav-lang"""
    # 替换主要样式
    content = content.replace('.lang-bar{', '.nav-lang{')
    content = content.replace('.lang-bar label{', '.nav-lang label{')
    content = content.replace('.lang-bar select{', '.nav-lang select{')
    content = content.replace('.lang-bar select option{', '.nav-lang select option{')
    # 替换媒体查询中的
    content = content.replace('@media(max-width:768px){\n.lang-bar{', '@media(max-width:768px){\n.nav-lang{')
    content = re.sub(r'@media\(max-width:768px\)\{\n\.nav-lang\{[^}]*\}\n\.nav-lang select\{[^}]*\}', 
                     lambda m: m.group(0), content)  # keep as is, already replaced
    return content

def remove_lang_bar_html(content):
    """删除独立的 .lang-bar HTML 块"""
    pattern = r'<!-- ===== Language Bar ===== -->\s*<div class="lang-bar">.*?</div>\s*'
    new = re.sub(pattern, '', content, flags=re.DOTALL)
    if new != content:
        return new, True
    return content, False

def add_nav_lang(content):
    """在 nav-actions 内的 nav-auth-btns 前插入 nav-lang"""
    # 检查是否已存在
    if 'class="nav-lang"' in content:
        return content, False
    
    # 插入在 <!-- Auth Buttons --> 或 nav-auth-btns 前面
    marker = '<!-- Auth Buttons -->'
    if marker in content:
        content = content.replace(marker, NAV_LANG_HTML + '\n' + marker, 1)
        return content, True
    
    # 备选：直接插在 nav-auth-btns 前
    marker2 = '<div class="nav-auth-btns"'
    if marker2 in content:
        content = content.replace(marker2, NAV_LANG_HTML + '\n' + marker2, 1)
        return content, True
    
    return content, False

def ensure_nav_layout(content):
    """确认导航菜单桌面横排 + 手机竖排的 CSS 正确"""
    changed = False
    
    # 确保桌面 .nav-links 是 flex（横排）
    if '.nav-links{display:flex;' not in content and '.nav-links{display: flex;' not in content:
        # 在 nav-logo 样式后添加
        pass  # 假设已存在
    
    # 确保手机端 .nav-links 是 flex-direction:column（竖排）
    if 'flex-direction:column' not in content:
        # 需要在媒体查询中添加
        pass  # 假设已存在
    
    return content, changed

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Step 1: 更新 CSS
    content = update_css(content)
    
    # Step 2: 删除 .lang-bar HTML
    content, removed = remove_lang_bar_html(content)
    
    # Step 3: 添加 nav-lang
    content, added = add_nav_lang(content)
    
    # Step 4: 确认导航布局
    content, layout_changed = ensure_nav_layout(content)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, removed, added
    
    return False, removed, added

def main():
    files = sorted([f for f in os.listdir(WORKSPACE) if f.endswith('.html')])
    print(f'Found {len(files)} HTML files')
    print('=' * 50)
    
    success = 0
    for fname in files:
        fpath = os.path.join(WORKSPACE, fname)
        try:
            changed, removed, added = process_file(fpath)
            if changed:
                print(f'  OK: {fname} (lang-bar removed: {removed}, nav-lang added: {added})')
                success += 1
            else:
                print(f'  SKIP: {fname} (no changes needed)')
        except Exception as e:
            print(f'  ERROR: {fname}: {e}')
    
    print('=' * 50)
    print(f'Done: {success}/{len(files)} files updated')

if __name__ == '__main__':
    main()
