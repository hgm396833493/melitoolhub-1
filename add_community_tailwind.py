#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_community_tailwind.py
给 Tailwind 风格的 HTML 文件（news1.html / news2.html）添加 Giscus 留言区
"""

import re, os

REPO_ID  = "REPO_ID_PLACEHOLDER"
CATEGORY_ID = "CATEGORY_ID_PLACEHOLDER"

# news 页社区板块 HTML（使用 Tailwind 类名）
NEWS_COMMUNITY_HTML = """
    <!-- ===== 读者讨论区 ===== -->
    <section class="max-w-6xl mx-auto px-4 mt-12 mb-8">
      <div class="text-center mb-6">
        <h2 class="text-2xl font-bold text-gray-800">💬 读者讨论区</h2>
        <div class="w-16 h-1 bg-yellow-400 mx-auto mt-3 rounded"></div>
        <p class="text-gray-500 text-sm mt-2">欢迎跨境电商同行交流讨论，分享经验、解答疑问</p>
      </div>
      <div id="giscus-wrapper" class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden min-h-[200px] flex items-center justify-center">
        <div id="giscus-placeholder" class="text-center p-10 text-gray-500">
          <span class="text-5xl block mb-3">💬</span>
          <p>请使用 GitHub 账号登录以查看和参与讨论</p>
        </div>
      </div>
    </section>
"""

GISCUS_SCRIPT_HTML = """
    <!-- Giscus Comments -->
    <script src="https://giscus.app/client.js"
            data-repo="hgm396833493/melitoolhub"
            data-repo-id="REPO_ID_PLACEHOLDER"
            data-category="Discussions"
            data-category-id="CATEGORY_ID_PLACEHOLDER"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="bottom"
            data-theme="light"
            data-lang="zh-CN"
            data-loading="lazy"
            crossorigin="anonymous"
            async>
    </script>
"""

def process_tailwind_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. 插入社区 HTML（在 <footer> 之前）
    if 'id="giscus-wrapper"' not in content:
        content = content.replace('<footer', NEWS_COMMUNITY_HTML + '\n    <footer', 1)

    # 2. 插入 Giscus <script>（在 </body> 之前）
    if 'giscus.app/client.js' not in content:
        # 将占位符替换
        script_html = GISCUS_SCRIPT_HTML.replace('REPO_ID_PLACEHOLDER', REPO_ID)
        script_html = script_html.replace('CATEGORY_ID_PLACEHOLDER', CATEGORY_ID)
        content = content.replace('</body>', script_html + '\n</body>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    workspace = r'D:\workspace'
    files = ['news1.html', 'news2.html']
    print('Processing Tailwind pages:')
    print('=' * 40)
    for fname in files:
        fpath = os.path.join(workspace, fname)
        if not os.path.exists(fpath):
            print(f'  SKIP: {fname} (not found)')
            continue
        try:
            changed = process_tailwind_file(fpath)
            if changed:
                print(f'  OK: {fname}')
            else:
                print(f'  SKIP: {fname} (already processed)')
        except Exception as e:
            print(f'  ERROR: {fname}: {e}')
    print('=' * 40)
    if REPO_ID == 'REPO_ID_PLACEHOLDER':
        print()
        print('[WARN] Placeholder IDs detected!')
        print('  Get real IDs from https://giscus.app, then:')
        print('  1. Edit REPO_ID and CATEGORY_ID in this script')
        print('  2. Re-run this script')

if __name__ == '__main__':
    main()
