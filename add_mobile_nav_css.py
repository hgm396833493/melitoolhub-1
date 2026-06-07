import os
import re

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 移动端导航CSS（需要添加到 @media(max-width:768px) 块中）
mobile_nav_css = '''
/* Mobile Navigation */
.nav-links{
display:none;
position:absolute;
top:54px;
left:0;
right:0;
background:var(--p);
flex-direction:column;
padding:8px 16px;
box-shadow:0 6px 16px rgba(0,0,0,.3)
}
.nav-links.open{
display:flex
}
.nav-links a{
padding:12px 8px;
border-bottom:1px solid rgba(255,255,255,.08);
font-size:.9rem
}
.nav-toggle{
display:block
}
'''

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有移动端导航样式
        if '@media(max-width:768px)' in content and '.nav-links' in content:
            # 查找 @media 块的位置
            media_index = content.find('@media(max-width:768px)')
            brace_start = content.find('{', media_index)
            
            # 找到匹配的结束括号
            brace_count = 1
            brace_end = brace_start + 1
            while brace_count > 0 and brace_end < len(content):
                if content[brace_end] == '{':
                    brace_count += 1
                elif content[brace_end] == '}':
                    brace_count -= 1
                brace_end += 1
            
            # 在 @media 块的结束括号前插入移动端导航样式
            before_end = content[:brace_end-1]
            after_end = content[brace_end-1:]
            
            # 检查是否已经有了 .nav-links 的移动样式
            media_content = content[brace_start:brace_end]
            if '.nav-links' not in media_content or 'display:none' not in media_content:
                new_content = before_end + mobile_nav_css + after_end
                
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified += 1
                print(f'Modified: {fname}')
            else:
                print(f'Skipped (already has mobile nav): {fname}')
        else:
            print(f'Skipped (no @media or .nav-links): {fname}')
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
