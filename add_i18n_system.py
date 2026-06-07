#!/usr/bin/env python3
"""
为文章页面添加 I18N 对象和 applyLang 函数
确保中文翻译正常工作
"""
from pathlib import Path

WORKSPACE = Path("D:/workspace")
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

# 最小化的 I18N 对象 - 包含导航栏和通用翻译
MINIMAL_I18N = """
// ===== Minimal I18N System =====
var I18N = {
zh:{
  site_name:"GlobalTrade Hub | 跨境工具·政策·采购一站式平台",
  nav_home:"首页", nav_articles:"跨境干货", nav_policy:"政策合规",
  nav_tools:"实用工具", nav_sourcing:"采购代办", nav_partners:"联盟工具",
  nav_community:"用户交流", btn_login:"登录", btn_register:"注册", btn_logout:"退出",
  cookie_accept:"同意授权", cookie_reject:"拒绝", cookie_policy:"查看隐私政策",
  search_placeholder:"搜索文章、工具、政策...", search_hint:"输入关键词开始搜索",
  ad_placeholder:"Google AdSense 横幅广告位（申请通过后启用）",
  auth_login_title:"欢迎回来", auth_login_subtitle:"登录您的 GlobalTrade Hub 账号",
  auth_register_title:"创建账号", auth_register_subtitle:"加入 GlobalTrade Hub 社区",
  comment_placeholder:"分享您的想法...", comment_submit:"发表评论",
  consult_title:"免费咨询", consult_name:"您的称呼", consult_email:"联系邮箱",
  consult_service:"咨询类型", consult_message:"详细需求", consult_submit:"提交咨询",
  footer_tools:"跨境工具", footer_articles:"干货文章", footer_policy:"政策合规",
  footer_about:"关于我们", footer_contact:"联系方式", footer_social:"关注我们",
  footer_copyright:" GlobalTrade Hub. All rights reserved."
},
en:{
  site_name:"GlobalTrade Hub | Cross-border Tools & Sourcing",
  nav_home:"Home", nav_articles:"Articles", nav_policy:"Policy",
  nav_tools:"Tools", nav_sourcing:"Sourcing", nav_partners:"Partners",
  nav_community:"Community", btn_login:"Login", btn_register:"Register", btn_logout:"Logout",
  cookie_accept:"Accept", cookie_reject:"Reject", cookie_policy:"Privacy Policy",
  search_placeholder:"Search articles, tools, policies...",
  auth_login_title:"Welcome Back", auth_register_title:"Create Account",
  comment_placeholder:"Share your thoughts...", comment_submit:"Post Comment",
  consult_title:"Free Consultation", consult_submit:"Submit"
}
};

var allLangs = ['zh','en','es','pt','ru','fr','de','it','ar','tr','vi','th','id','ms','ko','ja','pl','nl'];

var curLang = (function(){
  var saved = localStorage.getItem('gthLang') || 'zh';
  var url = new URL(location.href);
  var p = url.searchParams.get('lang');
  if(p && allLangs.indexOf(p) >= 0){ saved = p; localStorage.setItem('gthLang', p); }
  return saved;
})();
if(allLangs.indexOf(curLang) < 0) curLang = 'zh';

function applyLang(lang){
  curLang = lang;
  localStorage.setItem('gthLang', lang);
  var d = I18N[lang] || I18N.en;
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : lang === 'pt' ? 'pt-BR' : lang;
  // Update title
  document.title = d.site_name || document.title;
  // Update data-i18n elements
  var els = document.querySelectorAll('[data-i18n]');
  for(var i = 0; i < els.length; i++){
    var e = els[i], key = e.getAttribute('data-i18n');
    if(d[key]) e.textContent = d[key];
  }
  // Update data-i18n-attrib elements
  var attrEls = document.querySelectorAll('[data-i18n-attrib]');
  for(var i = 0; i < attrEls.length; i++){
    var e = attrEls[i], attrKey = e.getAttribute('data-i18n-attrib');
    if(attrKey && attrKey.indexOf(':') >= 0){
      var parts = attrKey.split(':');
      var attr = parts[0], key = parts[1];
      if(d[key]) e.setAttribute(attr, d[key]);
    }
  }
  // Update language select
  var sel = document.getElementById('lang-select');
  if(sel) sel.value = lang;
}
"""

def add_i18n_system(content):
    """在第一个 <script> 标签后添加 I18N 系统"""
    if 'var I18N' in content or 'function applyLang' in content:
        return content, False
    
    # 找到第一个 <script> 标签
    script_pos = content.find('<script>')
    if script_pos < 0:
        script_pos = content.find('<script ')
    
    if script_pos >= 0:
        # 在 <script> 后插入
        insert_pos = content.find('>', script_pos) + 1
        new_content = content[:insert_pos] + '\n' + MINIMAL_I18N + '\n' + content[insert_pos:]
        return new_content, True
    
    # 如果没有 script 标签，在 </head> 前添加
    head_pos = content.find('</head>')
    if head_pos >= 0:
        new_content = content[:head_pos] + '<script>\n' + MINIMAL_I18N + '\n</script>\n' + content[head_pos:]
        return new_content, True
    
    return content, False

def main():
    print("=" * 60)
    print("Add I18N system to article pages")
    print("=" * 60)
    
    for filename in TARGET_FILES:
        target_file = WORKSPACE / filename
        if not target_file.exists():
            print(f"\nSKIP: {filename} not found")
            continue
        
        print(f"\nProcessing: {filename}")
        content = read_file(target_file)
        
        content, changed = add_i18n_system(content)
        
        if changed:
            write_file(target_file, content)
            print("  [OK] Added I18N system")
        else:
            print("  [OK] I18N system already exists")
    
    print("\n" + "=" * 60)
    print("All pages now have I18N support!")
    print("=" * 60)

if __name__ == "__main__":
    main()
