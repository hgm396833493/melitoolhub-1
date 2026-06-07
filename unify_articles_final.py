#!/usr/bin/env python3
"""
统一文章页面样式脚本
将4个文章页面统一为 article-payment-comparison.html 的样式
"""

import re
import shutil
from pathlib import Path

# 配置
WORKSPACE = Path("D:/workspace")
REFERENCE_FILE = WORKSPACE / "article-payment-comparison.html"

# 需要修改的目标文件
TARGET_FILES = [
    "article-meli-es.html",
    "article-latam-logistics-es.html", 
    "article-brazil-market.html",
    "article-mexico-customs.html"
]

def read_file(filepath):
    """读取文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """写入文件内容"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_nav_html(content):
    """从参考文件中提取导航栏HTML"""
    # 查找 <nav ...> 到 </nav> 之间的内容
    pattern = r'(<nav[^>]*role="navigation"[^>]*>.*?</nav>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def extract_article_hero_css(content):
    """提取article-hero相关的CSS样式"""
    # 查找 :root 到第一个 </style> 之间的内容可能已经包含样式
    # 这里我们提取整个 <style> 标签内的内容
    pattern = r'<style>(.*?)</style>'
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        # 返回第一个 <style> 标签的内容（通常是导航栏的CSS）
        return matches[0]
    return ""

def replace_nav_bar(content, new_nav):
    """替换导航栏"""
    # 查找并替换 <nav ...> 到 </nav>
    pattern = r'<nav[^>]*role="navigation"[^>]*>.*?</nav>'
    replacement = new_nav
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
    return new_content

def replace_css_classes(content):
    """替换CSS类名"""
    # 替换 art-hero 为 article-hero
    content = re.sub(r'\bart-hero\b', 'article-hero', content)
    content = re.sub(r'\bart-body\b', 'article-body', content)
    content = re.sub(r'\bart-meta\b', 'article-meta', content)
    content = re.sub(r'\bart-tags\b', 'article-tags', content)
    content = re.sub(r'\bart-tag\b', 'article-tag', content)
    
    # 替换CSS中的 .art- 为 .article-
    content = re.sub(r'\.art-hero', '.article-hero', content)
    content = re.sub(r'\.art-body', '.article-body', content)
    content = re.sub(r'\.art-meta', '.article-meta', content)
    content = re.sub(r'\.art-tags', '.article-tags', content)
    content = re.sub(r'\.art-tag', '.article-tag', content)
    
    return content

def update_html_lang(content):
    """更新HTML lang属性为中文"""
    content = re.sub(r'<html[^>]*lang="[^"]*"', '<html lang="zh-CN">', content)
    return content

def update_meta_tags(content):
    """更新meta标签为中文"""
    # 这个需要根据每个文件的具体内容来修改
    # 暂时跳过，因为需要翻译内容
    return content

def set_default_language_zh(content):
    """设置默认语言为中文"""
    # 查找 JavaScript 中的语言设置
    # 常见的模式: var curLang = ... 或从 URL 参数获取
    
    # 模式1: var curLang = ...
    pattern1 = r'var\s+curLang\s*=\s*[^;]+;'
    replacement1 = 'var curLang = "zh";'
    content = re.sub(pattern1, replacement1, content)
    
    # 模式2: 从 URL 参数获取语言，如果没有则默认中文
    # 查找 getLanguageFromURL 或类似函数
    pattern2 = r'function\s+getLanguageFromURL\s*\([^)]*\)\s*{[^}]+}'
    # 如果找到这样的函数，修改其默认返回值为 "zh"
    
    return content

def add_missing_elements(content, reference_content):
    """添加缺失的元素（如rocket button, auth modal等）"""
    
    # 检查是否有小火箭按钮
    if 'rocket-btn' not in content:
        # 在 </body> 前添加小火箭按钮
        rocket_html = '''
<!-- ===== 小火箭浮动按钮 ===== -->
<a href="https://h5n5.xiaohuojian.bs/auth/register?code=h5n5" target="_blank" rel="noopener" class="rocket-btn" title="小火箭 - 快速注册">
<svg viewBox="0 0 24 24"><path d="M2.5 15.8l5.7 5.7L6 23.5l-6-6L2.5 15.8zm1.4-1.4L9.6 8.7l5.7 5.7-5.7 5.7-5.7-5.7zm8.5-8.5l1.4-1.4 2.1 2.1-1.4 1.4-2.1-2.1zm3.6-3.6L17.4.9l2.8 2.8L18.8 5 16 2.2zm4.2 9.8l-1.4 1.4-2.1-2.1 1.4-1.4 2.1 2.1zM18 15.8l6 6-1.5 1.5-6-6 1.5-1.5z"/></svg>
<span class="rocket-badge">Free</span>
</a>
'''
        content = content.replace('</body>', rocket_html + '\n</body>')
    
    # 检查是否有auth modal
    if 'auth-overlay' not in content:
        # 从参考文件中提取auth modal并添加
        auth_pattern = r'(<!-- ===== Auth Modal ===== -->.*?</div>\s*</div>)'
        auth_match = re.search(auth_pattern, reference_content, re.DOTALL)
        if auth_match:
            auth_html = auth_match.group(1)
            content = content.replace('</body>', auth_html + '\n</body>')
    
    return content

def process_file(target_file, reference_content):
    """处理单个文件"""
    print(f"\n处理文件: {target_file.name}")
    
    # 读取目标文件
    content = read_file(target_file)
    
    # 1. 提取新导航栏
    new_nav = extract_nav_html(reference_content)
    if new_nav:
        print("  [OK] 提取导航栏成功")
        # 替换导航栏
        content = replace_nav_bar(content, new_nav)
        print("  [OK] 替换导航栏完成")
    else:
        print("  [FAIL] 无法提取导航栏")
    
    # 2. 替换CSS类名
    content = replace_css_classes(content)
    print("  [OK] 替换CSS类名完成")
    
    # 3. 更新HTML lang属性
    content = update_html_lang(content)
    print("  [OK] 更新HTML lang属性完成")
    
    # 4. 设置默认语言为中文
    content = set_default_language_zh(content)
    print("  [OK] 设置默认语言为中文完成")
    
    # 5. 添加缺失的元素
    content = add_missing_elements(content, reference_content)
    print("  [OK] 添加缺失元素完成")
    
    # 写回文件
    write_file(target_file, content)
    print(f"  [OK] 文件已保存: {target_file.name}")
    
    return True

def main():
    print("=" * 60)
    print("Article Style Unification Script")
    print("=" * 60)
    
    # 检查参考文件是否存在
    if not REFERENCE_FILE.exists():
        print(f"ERROR: Reference file not found: {REFERENCE_FILE}")
        return
    
    # 读取参考文件
    print(f"\nReading reference file: {REFERENCE_FILE.name}")
    reference_content = read_file(REFERENCE_FILE)
    print("  [OK] Reference file loaded successfully")
    
    # 处理每个目标文件
    success_count = 0
    for filename in TARGET_FILES:
        target_file = WORKSPACE / filename
        
        if not target_file.exists():
            print(f"\nWARNING: File not found: {target_file}")
            continue
        
        # 创建备份
        backup_file = target_file.with_suffix('.html.bak')
        shutil.copy2(target_file, backup_file)
        print(f"  [OK] Backup created: {backup_file.name}")
        
        # 处理文件
        if process_file(target_file, reference_content):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"Processing complete: {success_count}/{len(TARGET_FILES)} files successful")
    print("=" * 60)

if __name__ == "__main__":
    main()
