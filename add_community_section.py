#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_community_section.py
给所有静态 HTML 文件添加 Giscus 用户留言讨论区

使用方法:
  1. 确保 GitHub 仓库已启用 Discussions
  2. 在 https://giscus.app 获取 repo-id 和 category-id
  3. 替换本脚本中的 REPO_ID 和 CATEGORY_ID
  4. 运行: python add_community_section.py
"""

import re
import os

# ========== 配置区 ==========
# 在 giscus.app 获取后填入此处
REPO_ID = "REPO_ID_PLACEHOLDER"        # ← 替换为你的 repo-id
CATEGORY_ID = "CATEGORY_ID_PLACEHOLDER" # ← 替换为你的 category-id
# ==============================

# CSS 片段：插入到 </style> 之前
CSS_BLOCK = """
/* Community Discussion Section */
.community-section{max-width:1140px;margin:40px auto 0;padding:0 24px}
.community-section .sec-header{margin-bottom:20px}
#giscus-wrapper{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);border:1px solid var(--bdr);overflow:hidden;min-height:200px;display:flex;align-items:center;justify-content:center}
.giscus-placeholder{text-align:center;padding:40px 20px;color:var(--s);font-size:.9rem}
.giscus-placeholder .icon{font-size:2.8rem;display:block;margin-bottom:12px}
.giscus-placeholder a{color:var(--p);text-decoration:underline}
@media(max-width:768px){.community-section{padding:0 12px;margin:32px auto 0}}
"""

# HTML 片段：插入到 <footer> 之前
HTML_SECTION = """
<!-- ===== Community Discussion Section ===== -->
<section class="community-section" id="community">
<div class="sec-header">
  <h2><span data-i18n="community_title">💬 全球贸易商交流区</span></h2>
  <div class="sec-divider"></div>
  <p data-i18n="community_desc">跨境贸易同行交流讨论，分享经验、解答疑问。请使用 GitHub 账号登录后参与讨论。</p>
</div>
<div id="giscus-wrapper">
  <div class="giscus-placeholder" id="giscus-placeholder">
    <span class="icon">💬</span>
    <p data-i18n="community_login">请使用 GitHub 账号登录以查看和参与讨论</p>
  </div>
</div>
</section>
"""

# 社区板块 i18n 数据（合并到 I18N 对象）
COMMUNITY_I18N_JS = """
// ===== Community i18n =====
(function(){
  var CK={
    zh:{
      community_title:"💬 全球贸易商交流区",
      community_desc:"跨境贸易同行交流讨论，分享经验、解答疑问。请使用 GitHub 账号登录后参与讨论。",
      community_login:"请使用 GitHub 账号登录以查看和参与讨论"
    },
    en:{
      community_title:"💬 Global Trade Community",
      community_desc:"Join fellow cross-border traders to share experiences and get answers. Log in with your GitHub account to participate.",
      community_login:"Please log in with your GitHub account to view and join the discussion"
    },
    es:{
      community_title:"💬 Comunidad de Comercio Global",
      community_desc:"Únete a otros comerciantes transfronterizos para compartir experiencias y obtener respuestas. Inicia sesión con tu cuenta de GitHub.",
      community_login:"Inicia sesión con tu cuenta de GitHub para ver y participar en la discusión"
    },
    pt:{
      community_title:"💬 Comunidade de Comércio Global",
      community_desc:"Junte-se a outros comerciantes transfronteiriços para compartilhar experiências. Faça login com sua conta do GitHub.",
      community_login:"Faça login com sua conta do GitHub para ver e participar da discussão"
    },
    ru:{
      community_title:"💬 Сообщество Глобальной Торговли",
      community_desc:"Присоединяйтесь к коллегам по кросс-бордерной торговле. Войдите через GitHub для участия.",
      community_login:"Войдите через аккаунт GitHub, чтобы просматривать и участвовать в обсуждении"
    },
    fr:{
      community_title:"💬 Communauté de Commerce Mondial",
      community_desc:"Rejoignez d'autres commerçants transfrontaliers. Connectez-vous avec GitHub pour participer.",
      community_login:"Connectez-vous avec votre compte GitHub pour voir et rejoindre la discussion"
    },
    de:{
      community_title:"💬 Global Trade Community",
      community_desc:"Nehmen Sie teil an der Gemeinschaft der Grenzüberschreitenden Händler. Melden Sie sich mit GitHub an.",
      community_login:"Melden Sie sich mit Ihrem GitHub-Konto an, um die Diskussion zu sehen und teilzunehmen"
    },
    it:{
      community_title:"💬 Comunità di Commercio Globale",
      community_desc:"Unisciti ad altri commercianti transfrontalieri. Accedi con il tuo account GitHub per partecipare.",
      community_login:"Accedi con il tuo account GitHub per visualizzare e partecipare alla discussione"
    },
    ar:{
      community_title:"💬 مجتمع التجارة العالمية",
      community_desc:"انضم إلى تجار التجارة عبر الحدود. سجل الدخول باستخدام حساب GitHub للمشاركة.",
      community_login:"سجل الدخول باستخدام حساب GitHub الخاص بك لعرض ومناقشة النقاش"
    },
    tr:{
      community_title:"💬 Küresel Ticaret Topluluğu",
      community_desc:"Sınır ötesi tüccarlar topluluğuna katılın. Katılmak için GitHub hesabınızla giriş yapın.",
      community_login:"Tartışmayı görmek ve katılmak için GitHub hesabınızla giriş yapın"
    },
    vi:{
      community_title:"💬 Cộng Đồng Thương Mại Toàn Cầu",
      community_desc:"Tham gia cộng đồng thương mại xuyên biên giới. Đăng nhập bằng tài khoản GitHub để tham gia.",
      community_login:"Đăng nhập bằng tài khoản GitHub để xem và tham gia thảo luận"
    },
    th:{
      community_title:"💬 ชุมชนการค้าโลก",
      community_desc:"เข้าร่วมชุมชนผู้ค้าขายข้ามพรมแดน สมัครสมาชิกด้วยบัญชี GitHub เพื่อเข้าร่วม",
      community_login:"กรุณาเข้าสู่ระบบด้วยบัญชี GitHub เพื่อดูและเข้าร่วมการอภิปราย"
    },
    id:{
      community_title:"💬 Komunitas Perdagangan Global",
      community_desc:"Bergabunglah dengan komunitas pedagang lintas batas. Login dengan akun GitHub untuk berpartisipasi.",
      community_login:"Login dengan akun GitHub Anda untuk melihat dan berpartisipasi dalam diskusi"
    },
    ms:{
      community_title:"💬 Komuniti Perdagangan Global",
      community_desc:"Sertai komuniti pedagang rentas sempadan. Log masuk dengan akaun GitHub untuk menyertai.",
      community_login:"Log masuk dengan akaun GitHub anda untuk melihat dan menyertai perbincangan"
    },
    ko:{
      community_title:"💬 글로벌 무역 커뮤니티",
      community_desc:"국경 간 무역 커뮤니티에 참여하세요. GitHub 계정으로 로그인하여 참여하십시오.",
      community_login:"GitHub 계정으로 로그인하여 토론을 보고 참여하십시오"
    },
    ja:{
      community_title:"💬 グローバル貿易コミュニティ",
      community_desc:"越境貿易コミュニティに参加しましょう。GitHubアカウントでログインして参加してください。",
      community_login:"GitHubアカウントでログインしてディスカッションを表示・参加してください"
    },
    pl:{
      community_title:"💬 Społeczność Handlu Globalnego",
      community_desc:"Dołącz do społeczności handlu transgranicznego. Zaloguj się przez GitHub, aby uczestniczyć.",
      community_login:"Zaloguj się przez swoje konto GitHub, aby zobaczyć i dołączyć do dyskusji"
    },
    nl:{
      community_title:"💬 Global Trade Community",
      community_desc:"Doe mee met de cross-border handelsgemeenschap. Log in met je GitHub-account om deel te nemen.",
      community_login:"Log in met je GitHub-account om de discussie te bekijken en deel te nemen"
    }
  };
  for(var l in CK){
    if(!I18N[l])I18N[l]={};
    for(var k in CK[l]){
      if(!I18N[l][k])I18N[l][k]=CK[l][k];
    }
  }
})();
"""

# Giscus 初始化 JS
GISCUS_LOADER_JS = """
// ===== Giscus (Community Comments) =====
function loadGiscus(){
  var repoId='REPO_ID_PLACEHOLDER';
  var categoryId='CATEGORY_ID_PLACEHOLDER';
  if(repoId==='REPO_ID_PLACEHOLDER'||!repoId){
    var ph=document.getElementById('giscus-placeholder');
    if(ph)ph.querySelector('p').textContent='⚠️ Giscus 未配置，请联系站长。';
    return;
  }
  var langMap={zh:'zh-CN',en:'en',es:'es',pt:'pt-BR',ru:'ru',fr:'fr',de:'de',it:'it',ar:'ar',tr:'tr',vi:'vi',th:'th',id:'id',ms:'ms',ko:'ko',ja:'ja',pl:'pl',nl:'nl'};
  var gLang=langMap[curLang]||'en';
  var wrapper=document.getElementById('giscus-wrapper');
  if(!wrapper)return;
  var ph=document.getElementById('giscus-placeholder');
  if(ph)ph.remove();
  var existing=wrapper.querySelector('.giscus-frame-wrapper');
  if(existing)existing.remove();
  var s=document.createElement('script');
  s.src='https://giscus.app/client.js';
  s.setAttribute('data-repo','hgm396833493/melitoolhub');
  s.setAttribute('data-repo-id',repoId);
  s.setAttribute('data-category','Discussions');
  s.setAttribute('data-category-id',categoryId);
  s.setAttribute('data-mapping','pathname');
  s.setAttribute('data-strict','0');
  s.setAttribute('data-reactions-enabled','1');
  s.setAttribute('data-emit-metadata','0');
  s.setAttribute('data-input-position','bottom');
  s.setAttribute('data-theme','light');
  s.setAttribute('data-lang',gLang);
  s.setAttribute('data-loading','lazy');
  s.crossOrigin='anonymous';
  s.async=true;
  wrapper.appendChild(s);
}
"""

def process_file(filepath):
    """处理单个 HTML 文件，添加社区讨论区"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. 插入 CSS（在 </style> 之前）
    if CSS_BLOCK.strip() not in content:
        content = content.replace('</style>', CSS_BLOCK + '\n</style>', 1)
    
    # 2. 插入 HTML 板块（在 <footer> 之前）
    if 'id="community"' not in content and 'class="community-section"' not in content:
        content = content.replace('<footer>', HTML_SECTION + '\n<footer>', 1)
    
    # 3. 插入社区 i18n 数据（在 I18N 对象之后，Current Language 之前）
    if 'Community i18n' not in content:
        # 在 // ===== Current Language ===== 之前插入
        marker = '// ===== Current Language ====='
        if marker in content:
            content = content.replace(marker, COMMUNITY_I18N_JS + '\n' + marker, 1)
        else:
            # 备用：在 var curLang 之前插入
            marker2 = 'var curLang'
            if marker2 in content:
                content = content.replace(marker2, COMMUNITY_I18N_JS + '\n', 1)
    
    # 4. 插入 Giscus 加载器 JS（在 </script> 之前，即 i18n 数据块之后）
    if 'function loadGiscus' not in content:
        # 在 </script> 之前插入（I18N 对象所在的 script 块末尾）
        # 找最后一个 </script>（在 </body> 之前）
        # 更可靠的方式：在 applyLang 函数之后插入
        marker3 = '// ===== Apply Translations ====='
        if marker3 in content:
            content = content.replace(marker3, GISCUS_LOADER_JS + '\n// ===== Apply Translations =====', 1)
        else:
            # 备用：在 DOMContentLoaded 之前插入
            marker4 = 'document.addEventListener(\'DOMContentLoaded\''
            if marker4 in content:
                content = content.replace(marker4, GISCUS_LOADER_JS + '\n' + marker4, 1)
    
    # 5. 在 DOMContentLoaded 回调中调用 loadGiscus
    if 'loadGiscus()' not in content:
        # 使用正则处理两种情况：
        # Case 1: applyLang(curLang);\n   （单独一行）
        # Case 2: applyLang(curLang);document... （同一行，后面紧跟其他代码）
        # 先处理 Case 2（同行代码）
        pattern2 = r'(applyLang\(curLang\);)(\s*)(?=\S)'
        m2 = re.search(pattern2, content)
        if m2:
            # 同一行有后续代码，在分号后插入换行+loadGiscus()
            indent = ''
            pos = m2.start()
            lines_before = content[:pos].splitlines()
            if lines_before:
                last_line = lines_before[-1]
                indent = ' ' * (len(last_line) - len(last_line.lstrip()))
            new = m2.group(1) + '\n' + indent + 'loadGiscus();\n' + indent + m2.group(2)
            content = content[:m2.start()] + new + content[m2.end():]
        else:
            # Case 1: applyLang(curLang); 在行尾
            pattern1 = r'(applyLang\(curLang\);\s*\n)'
            m1 = re.search(pattern1, content)
            if m1:
                indent = ''
                pos = m1.start()
                lines_before = content[:pos].splitlines()
                if lines_before:
                    last_line = lines_before[-1]
                    indent = ' ' * (len(last_line) - len(last_line.lstrip()))
                content = content[:m1.end()-1] + '\n' + indent + 'loadGiscus();' + content[m1.end()-1:]
    
    # 替换占位符
    content = content.replace('REPO_ID_PLACEHOLDER', REPO_ID)
    content = content.replace('CATEGORY_ID_PLACEHOLDER', CATEGORY_ID)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    workspace = r'D:\workspace'
    html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]
    html_files.sort()
    
    print(f'Found {len(html_files)} HTML files')
    print('=' * 50)
    
    if REPO_ID == 'REPO_ID_PLACEHOLDER':
        print('[WARN] REPO_ID and CATEGORY_ID are still placeholders!')
        print('  Please get the real IDs from https://giscus.app first.')
        print('  The script will run in placeholder mode.')
        print('=' * 50)
    
    success = 0
    for fname in html_files:
        fpath = os.path.join(workspace, fname)
        try:
            changed = process_file(fpath)
            if changed:
                print(f'  OK: {fname}')
                success += 1
            else:
                print(f'  SKIP: {fname} (already processed)')
        except Exception as e:
            print(f'  ERROR: {fname}: {e}')
    
    print('=' * 50)
    print(f'Done: {success}/{len(html_files)} files updated')
    
    if REPO_ID == 'REPO_ID_PLACEHOLDER':
        print()
        print('Next steps:')
        print('  1. Visit https://github.com/hgm396833493/melitoolhub/settings')
        print('  2. Enable Discussions')
        print('  3. Visit https://giscus.app/zh-CN')
        print('  4. Fill in repo, get repo-id and category-id')
        print('  5. Replace REPO_ID and CATEGORY_ID at top of this script')
        print('  6. Run this script again')

if __name__ == '__main__':
    main()
