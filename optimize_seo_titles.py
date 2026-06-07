import os
import re

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# SEO 优化建议：
# Google 建议 title 长度：50-60 字符（中文约 20-30 字）
# Meta description 长度：150-160 字符（中文约 70-80 字）

# 标题模板
title_templates = {
    'index.html': 'GlobalTrade Hub | 跨境工具·政策·采购一站式平台',
    'tools.html': '跨境工具 - GlobalTrade Hub',
    'sourcing.html': '采购代办服务 - GlobalTrade Hub',
    'cooperation.html': '商务合作 - GlobalTrade Hub',
    'privacy.html': '隐私政策 - GlobalTrade Hub',
    '404.html': '页面未找到 - GlobalTrade Hub',
}

# Description 模板
desc_templates = {
    'index.html': 'GlobalTrade Hub 专注跨境贸易工具、政策合规资讯、中国货源采购代办服务。覆盖拉美、俄罗斯、东南亚、欧洲、中东市场，18语种合规站点。',
    'tools.html': '免费跨境工具：汇率换算、物流追踪、平台费用计算、关税查询。助力中国卖家拓展全球市场。',
    'sourcing.html': '专业中国采购代办服务：供应商筛选、验货、物流、报关一站式服务。帮您安全便捷地从中国采购。',
    'cooperation.html': 'GlobalTrade Hub 商务合作：联盟推广、内容合作、工具开发。携手共赢跨境贸易市场。',
    'privacy.html': 'GlobalTrade Hub 隐私政策：我们如何收集、使用和保护您的个人信息。',
}

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = 0
        
        # 1. 优化 title（如果太长 > 60 字符）
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', content)
        if title_match:
            title = title_match.group(1)
            if len(title) > 60:
                # 如果文件有预设模板，使用模板
                if fname in title_templates:
                    new_title = title_templates[fname]
                else:
                    # 否则截断
                    new_title = title[:57] + '...'
                
                content = content.replace(title_match.group(0), f'<title id="page-title">{new_title}</title>')
                changes += 1
                print(f'{fname}: Title optimized ({len(title)} -> {len(new_title)})')
        
        # 2. 优化 description（如果太长 > 160 字符）
        desc_match = re.search(r'<meta name="description"[^>]*content="([^"]+)"', content, re.I)
        if desc_match:
            desc = desc_match.group(1)
            if len(desc) > 160:
                if fname in desc_templates:
                    new_desc = desc_templates[fname]
                else:
                    new_desc = desc[:157] + '...'
                
                old_tag = desc_match.group(0)
                new_tag = old_tag.replace(f'content="{desc}"', f'content="{new_desc}"')
                content = content.replace(old_tag, new_tag)
                changes += 1
                print(f'{fname}: Description optimized ({len(desc)} -> {len(new_desc)})')
        
        if changes > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified += 1
        else:
            print(f'OK: {fname}')
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
