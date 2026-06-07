import os
import re

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 标准完整导航栏（包含语言选择器和认证按钮）
standard_nav = '''<nav role="navigation" aria-label="主导航">
<a href="index.html" class="nav-logo">Global<span>Trade</span>Hub</a>
<div class="nav-links" id="nav-links">
<a href="index.html" data-i18n="nav_home">首页</a>
<a href="index.html#articles" data-i18n="nav_articles">跨境干货</a>
<a href="index.html#policy" data-i18n="nav_policy">政策合规</a>
<a href="index.html#tools" data-i18n="nav_tools">实用工具</a>
<a href="index.html#sourcing" data-i18n="nav_sourcing">采购代办</a>
<a href="index.html#partners" data-i18n="nav_partners">联盟工具</a>
<a href="index.html#community" data-i18n="nav_community">用户交流</a>
</div>
<div class="nav-actions">
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
</div>
<div class="nav-auth-btns" id="nav-auth-btns">
<button class="nav-btn-login" id="nav-btn-login" data-i18n="btn_login">登录</button>
<button class="nav-btn-register" id="nav-btn-register" data-i18n="btn_register">注册</button>
<div class="nav-user-info" id="nav-user-info" style="display:none">
<span class="nav-user-avatar" id="nav-user-avatar"></span>
<span class="nav-user-name" id="nav-user-name"></span>
<button class="nav-btn-logout" id="nav-btn-logout" data-i18n="btn_logout">退出</button>
</div>
</div>
<button class="nav-toggle" id="nav-toggle" aria-label="菜单">☰</button>
</div>
</nav>'''

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找现有的 <nav> 标签
        nav_pattern = r'<nav[^>]*>[\s\S]*?</nav>'
        
        if re.search(nav_pattern, content):
            # 替换整个 nav 标签内容
            new_content = re.sub(nav_pattern, standard_nav, content)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
            print(f'Modified: {fname}')
        else:
            print(f'Skipped: {fname} (no nav tag)')
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
