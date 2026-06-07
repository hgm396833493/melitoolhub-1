#!/usr/bin/env python3
"""
同步首页导航栏到所有文章页面
确保HTML结构、CSS样式、JavaScript功能完全一致
"""
import re
import shutil
from pathlib import Path

WORKSPACE = Path("D:/workspace")

# 需要处理的文章页面
TARGET_FILES = [
    "article-payment-comparison.html",
    "article-meli-es.html",
    "article-latam-logistics-es.html",
    "article-brazil-market.html",
    "article-mexico-customs.html"
]

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_nav_html(content):
    """从首页提取完整的导航栏HTML"""
    # 找到 <nav> 开始到 </nav> 结束
    match = re.search(r'(<nav\s[^>]*>)(.*?)(</nav>)', content, re.DOTALL)
    if match:
        return match.group(0)  # 返回完整的 nav 标签
    return None

def extract_nav_css(content):
    """从首页提取导航栏相关的CSS"""
    css_blocks = []
    
    # 导航栏主要样式
    nav_pattern = r'(nav\s*\{[^}]*\})'
    matches = re.findall(nav_pattern, content, re.DOTALL)
    css_blocks.extend(matches)
    
    # 所有以 .nav- 开头的类
    nav_classes = [
        r'(\.nav-logo[^}]+})',
        r'(\.nav-links[^}]+})',
        r'(\.nav-lang[^}]+})',
        r'(\.nav-auth-btns[^}]+})',
        r'(\.nav-toggle[^}]+})',
        r'(\.nav-btn-login[^}]+})',
        r'(\.nav-btn-register[^}]+})',
        r'(\.nav-user-info[^}]+})',
        r'(\.nav-user-avatar[^}]+})',
        r'(\.nav-user-name[^}]+})',
        r'(\.nav-user-dropdown[^}]+})',
    ]
    
    for pattern in nav_classes:
        matches = re.findall(pattern, content, re.DOTALL)
        css_blocks.extend(matches)
    
    # 移动端样式 (media query)
    media_pattern = r'@media\s*\(max-width:\s*768px\)\s*\{([^}]*\.nav-[^}]*})'
    matches = re.findall(media_pattern, content, re.DOTALL)
    css_blocks.extend(matches)
    
    return '\n'.join(css_blocks)

def replace_nav_bar(content, new_nav_html):
    """替换导航栏HTML"""
    # 找到旧的导航栏并替换
    pattern = r'<nav\s[^>]*>.*?</nav>'
    replacement = new_nav_html
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
    return new_content

def main():
    print("=" * 60)
    print("同步首页导航栏到文章页面")
    print("=" * 60)
    
    # 读取首页
    index_file = WORKSPACE / "index.html"
    if not index_file.exists():
        print(f"ERROR: 首页文件不存在: {index_file}")
        return
    
    print(f"\n读取首页: {index_file.name}")
    index_content = read_file(index_file)
    
    # 提取导航栏HTML
    nav_html = extract_nav_html(index_content)
    if not nav_html:
        print("ERROR: 无法从首页提取导航栏HTML")
        return
    
    print(f"  [OK] 提取导航栏HTML成功 (长度: {len(nav_html)} 字符)")
    
    # 处理每个目标文件
    success_count = 0
    for filename in TARGET_FILES:
        target_file = WORKSPACE / filename
        
        if not target_file.exists():
            print(f"\nWARNING: 文件不存在: {target_file}")
            continue
        
        print(f"\n处理文件: {target_file.name}")
        
        # 创建备份
        backup_file = target_file.with_suffix('.html.nav-bak')
        shutil.copy2(target_file, backup_file)
        print(f"  [OK] 备份已创建: {backup_file.name}")
        
        # 读取目标文件
        content = read_file(target_file)
        
        # 替换导航栏
        new_content = replace_nav_bar(content, nav_html)
        
        if new_content == content:
            print(f"  [WARNING] 导航栏未发生变化，请手动检查")
        else:
            # 写回文件
            write_file(target_file, new_content)
            print(f"  [OK] 导航栏已替换")
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"处理完成: {success_count}/{len(TARGET_FILES)} 个文件成功")
    print("=" * 60)
    print("\n提示: 所有修改已备份为 .nav-bak 文件")

if __name__ == "__main__":
    main()
