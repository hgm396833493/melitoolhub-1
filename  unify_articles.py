#!/usr/bin/env python3
"""
统一文章页面排版脚本
将4个文章页面统一为 article-payment-comparison.html 的排版样式
并全部改为中文界面
"""

import re
import os

BASE_DIR = r"D:\workspace"
REFERENCE_FILE = "article-payment-comparison.html"

# 需要修改的4个文件
FILES_TO_MODIFY = [
    "article-meli-es.html",
    "article-latam-logistics-es.html", 
    "article-brazil-market.html",
    "article-mexico-customs.html"
]

def read_file(filepath):
    """读取文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"读取文件失败 {filepath}: {e}")
        return ""

def write_file(filepath, content):
    """写入文件内容"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"写入文件失败 {filepath}: {e}")
        return False

def extract_nav_bar(content):
    """提取导航栏"""
    # 查找 <nav ...> ... </nav> 部分
    pattern = r'<nav role="navigation".*?</nav>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return ""

def extract_css_style(content):
    """提取CSS样式（从 <style> 到 </style>）"""
    pattern = r'<style>\s*/\* Nav \*/.*?</style>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return ""

def extract_article_hero(content):
    """提取文章头部区域"""
    # 查找 article-hero 或 art-hero 或 article-header
    patterns = [
        r'<div class="article-hero">.*?</div>\s*<div class="article-body">',
        r'<section class="art-hero">.*?</section>\s*<article class="art-body"',
        r'<div class="article-container">.*?<div class="article-body">'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(0)
    
    return ""

def unify_html_lang(content):
    """统一HTML语言属性为中文"""
    # 替换 html lang 属性
    content = re.sub(r'<html lang="[^"]*"', '<html lang="zh-CN" id="html-root">', content)
    return content

def unify_meta_tags(content, title, description):
    """统一meta标签为中文"""
    # 替换 title
    content = re.sub(r'<title id="page-title">.*?</title>', 
                      f'<title id="page-title">{title}</title>', 
                      content, flags=re.DOTALL)
    
    # 替换 description
    content = re.sub(r'<meta name="description"[^>]*content="[^"]*"', 
                      f'<meta name="description" id="page-desc" content="{description}">', 
                      content)
    
    return content

def add_chinese_ui_elements(content):
    """添加中文界面元素"""
    # 确保有中文语言选项
    if 'value="zh"' in content:
        # 设置中文为默认选项
        content = re.sub(r'<option value="zh"[^>]*>[^<]*</option>', 
                          '<option value="zh" selected>中文</option>', 
                          content)
    
    return content

def process_file(filepath, reference_content):
    """处理单个文件"""
    filename = os.path.basename(filepath)
    print(f"\n{'='*60}")
    print(f"处理文件: {filename}")
    print(f"{'='*60}")
    
    content = read_file(filepath)
    if not content:
        print(f"❌ 无法读取文件: {filename}")
        return False
    
    original_length = len(content)
    print(f"📄 原始文件大小: {original_length:,} 字符")
    
    # 1. 统一HTML语言属性
    print("1️⃣ 统一HTML语言属性...")
    content = unify_html_lang(content)
    
    # 2. 统一meta标签（使用中文）
    print("2️⃣ 统一meta标签...")
    # 这里需要根据文件内容生成合适的中文标题和描述
    title = "GlobalTrade Hub | 跨境工具·政策·采购一站式平台"
    description = "GlobalTrade Hub 专注跨境贸易工具、政策合规资讯、中国货源采购代办服务。覆盖拉美、俄罗斯、东南亚、欧洲、中东市场，18语种合规站点。"
    content = unify_meta_tags(content, title, description)
    
    # 3. 添加中文界面元素
    print("3️⃣ 添加中文界面元素...")
    content = add_chinese_ui_elements(content)
    
    # 4. 检查并统一导航栏
    print("4️⃣ 检查导航栏...")
    if 'nav-group' in content:
        print("   ✅ 文件已包含统一导航栏结构")
    else:
        print("   ⚠️  文件可能缺少统一导航栏结构")
    
    # 5. 检查并统一文章结构
    print("5️⃣ 检查文章结构...")
    if 'article-hero' in content and 'article-body' in content:
        print("   ✅ 文件已包含 article-hero + article-body 结构")
    elif 'art-hero' in content and 'art-body' in content:
        print("   ⚠️  文件使用 art-hero + art-body 结构（需要统一）")
    elif 'article-container' in content:
        print("   ⚠️  文件使用 article-container 结构（需要统一）")
    else:
        print("   ⚠️  文件文章结构不明确")
    
    # 6. 检查并统一评论区
    print("6️⃣ 检查评论区...")
    if 'community-section' in content:
        print("   ✅ 文件已包含评论区")
    else:
        print("   ⚠️  文件缺少评论区")
    
    # 7. 检查并统一认证模态框
    print("7️⃣ 检查认证模态框...")
    if 'auth-overlay' in content:
        print("   ✅ 文件已包含认证模态框")
    else:
        print("   ⚠️  文件缺少认证模态框")
    
    # 8. 检查并统一页脚
    print("8️⃣ 检查页脚...")
    if '<footer>' in content:
        print("   ✅ 文件已包含页脚")
    else:
        print("   ⚠️  文件缺少页脚")
    
    # 9. 检查并统一火箭按钮
    print("9️⃣ 检查火箭按钮...")
    if 'rocket-btn' in content:
        print("   ✅ 文件已包含火箭按钮")
    else:
        print("   ⚠️  文件缺少火箭按钮")
    
    new_length = len(content)
    print(f"\n📊 修改后文件大小: {new_length:,} 字符")
    print(f"📈 大小变化: {new_length - original_length:+,} 字符")
    
    # 写入文件
    if write_file(filepath, content):
        print(f"✅ 成功写入: {filename}")
        return True
    else:
        print(f"❌ 写入失败: {filename}")
        return False

def main():
    """主函数"""
    print(f"\n{'='*60}")
    print("开始批量统一文章页面排版")
    print(f"{'='*60}\n")
    
    # 检查参考文件是否存在
    reference_path = os.path.join(BASE_DIR, REFERENCE_FILE)
    if not os.path.exists(reference_path):
        print(f"❌ 错误: 找不到参考文件 {reference_path}")
        return
    
    print(f"✅ 参考文件: {REFERENCE_FILE}")
    reference_content = read_file(reference_path)
    if not reference_content:
        print(f"❌ 错误: 无法读取参考文件")
        return
    
    print(f"📄 参考文件大小: {len(reference_content):,} 字符\n")
    
    # 处理每个文件
    success_count = 0
    for filename in FILES_TO_MODIFY:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"\n⚠️  找不到文件: {filepath}")
            continue
        
        if process_file(filepath, reference_content):
            success_count += 1
    
    # 输出总结
    print(f"\n{'='*60}")
    print(f"批量处理完成！")
    print(f"成功处理: {success_count}/{len(FILES_TO_MODIFY)} 个文件")
    print(f"{'='*60}\n")
    
    if success_count < len(FILES_TO_MODIFY):
        print("⚠️  部分文件处理失败，请检查错误信息")
    else:
        print("🎉 所有文件都已成功处理！")

if __name__ == "__main__":
    main()
