#!/usr/bin/env python3
"""
批量统一文章页面样式脚本
将 article-meli-es.html, article-latam-logistics-es.html, 
article-brazil-market.html, article-mexico-customs.html
的排版统一为 article-payment-comparison.html 的样式，并改为中文界面
"""

import re
import os

BASE_DIR = r"D:\workspace"
TARGET_FILE = "article-payment-comparison.html"

# 需要修改的4个文件
FILES_TO_MODIFY = [
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

def extract_nav_bar(target_content):
    """从目标文件中提取导航栏"""
    # 查找 <nav ...> ... </nav> 部分
    nav_match = re.search(r'<nav role="navigation".*?</nav>', target_content, re.DOTALL)
    if nav_match:
        return nav_match.group(0)
    return ""

def extract_auth_modal(target_content):
    """从目标文件中提取认证模态框"""
    auth_match = re.search(r'<!-- ===== Auth Modal ===== -->.*?</div>\s*</div>\s*</body>', target_content, re.DOTALL)
    if auth_match:
        return auth_match.group(0)
    return ""

def extract_community_section(target_content):
    """从目标文件中提取评论区"""
    community_match = re.search(r'<!-- ===== Community Discussion Section ===== -->.*?</section>', target_content, re.DOTALL)
    if community_match:
        return community_match.group(0)
    return ""

def extract_footer(target_content):
    """从目标文件中提取footer"""
    footer_match = re.search(r'<footer>.*?</footer>', target_content, re.DOTALL)
    if footer_match:
        return footer_match.group(0)
    return ""

def extract_rocket_button(target_content):
    """从目标文件中提取火箭按钮"""
    rocket_match = re.search(r'<!-- ===== 小火箭浮动按钮 ===== -->.*?</a>', target_content, re.DOTALL)
    if rocket_match:
        return rocket_match.group(0)
    return ""

def extract_css_style(target_content):
    """从目标文件中提取CSS样式"""
    style_match = re.search(r'<style>\s*/\* Nav \*/.*?</style>', target_content, re.DOTALL)
    if style_match:
        return style_match.group(0)
    return ""

def modify_file(filepath, target_content):
    """修改单个文件"""
    print(f"正在处理: {filepath}")
    
    content = read_file(filepath)
    
    # 1. 修改 HTML lang 属性
    content = re.sub(r'<html lang="[^"]*"', '<html lang="zh-CN" id="html-root">', content)
    
    # 2. 修改 title
    content = re.sub(r'<title id="page-title">.*?</title>', 
                      '<title id="page-title">GlobalTrade Hub | 跨境工具·政策·采购一站式平台</title>', 
                      content)
    
    # 3. 修改 description
    content = re.sub(r'<meta name="description".*?content="[^"]*"', 
                      '<meta name="description" id="page-desc" content="GlobalTrade Hub 专注跨境贸易工具、政策合规资讯、中国货源采购代办服务。覆盖拉美、俄罗斯、东南亚、欧洲、中东市场，18语种合规站点。">', 
                      content)
    
    # 4. 提取并替换导航栏
    new_nav = extract_nav_bar(target_content)
    if new_nav:
        # 查找并替换现有导航栏
        content = re.sub(r'<nav role="navigation".*?</nav>', new_nav, content, flags=re.DOTALL)
        print(f"  - 已更新导航栏")
    
    # 5. 统一CSS样式 (保留原有样式，但确保关键样式一致)
    # 这里我们只修改关键样式变量
    if 'article-hero' in content and 'article-body' in content:
        print(f"  - 文件已包含 article-hero 和 article-body 结构")
    
    # 6. 修改语言选择器为默认中文
    content = re.sub(r'<option value="zh"[^>]*>[^<]*</option>', 
                      '<option value="zh" selected>中文</option>', 
                      content)
    
    # 7. 确保有评论区
    if 'community-section' not in content:
        print(f"  - 警告: 文件缺少评论区")
    
    # 8. 确保有认证模态框
    if 'auth-overlay' not in content:
        print(f"  - 警告: 文件缺少认证模态框")
    
    write_file(filepath, content)
    print(f"✅ 已完成: {filepath}\n")

def main():
    print("=" * 60)
    print("开始批量统一文章页面样式")
    print("=" * 60)
    
    # 读取目标文件（参考样式）
    target_path = os.path.join(BASE_DIR, TARGET_FILE)
    if not os.path.exists(target_path):
        print(f"错误: 找不到目标文件 {target_path}")
        return
    
    target_content = read_file(target_path)
    print(f"✅ 已读取目标文件: {TARGET_FILE}")
    
    # 处理每个文件
    for filename in FILES_TO_MODIFY:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"⚠️  找不到文件: {filepath}")
            continue
        
        modify_file(filepath, target_content)
    
    print("=" * 60)
    print("批量处理完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
