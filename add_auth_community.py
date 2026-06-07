#!/usr/bin/env python3
"""
GlobalTradeHub 用户系统 + 自建评论区 注入脚本
功能:
1. 导航栏增加"用户交流"+注册/登录按钮
2. 注册/登录模态框 (Supabase Auth)
3. 自建评论区 (Supabase 数据库, 替换 Giscus)
4. 18语言 i18n 补充
"""

import os
import re

# ============================================================
# [CONFIG] 用户填入 Supabase 密钥后重新运行
# ============================================================
SUPABASE_URL = 'https://woiwjttrtokwgrhhzobm.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvaXdqdHRydG9rd2dyaGh6b2JtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA2NjQyOTAsImV4cCI6MjA5NjI0MDI5MH0.0t55C_xI2Bxowi2DyOV43tXukU8TVzGlRK0zSZ3j2R8'

WORKSPACE = r'D:\workspace'

# ============================================================
# CSS 注入内容
# ============================================================
AUTH_COMMUNITY_CSS = """
/* Auth Modal */
.auth-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:10001;display:none;align-items:center;justify-content:center}
.auth-overlay.show{display:flex}
.auth-panel{background:var(--c);border-radius:14px;width:min(420px,92vw);box-shadow:0 20px 60px rgba(0,0,0,.35);overflow:hidden;animation:authSlideIn .25s ease}
@keyframes authSlideIn{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
.auth-header{background:var(--p);color:#fff;padding:20px 24px;text-align:center;position:relative}
.auth-header h3{font-size:1.1rem;font-weight:700;margin:0}
.auth-header p{font-size:.78rem;opacity:.8;margin:4px 0 0}
.auth-close{position:absolute;top:12px;right:16px;background:none;border:none;color:rgba(255,255,255,.7);font-size:1.3rem;cursor:pointer;padding:4px;line-height:1}
.auth-close:hover{color:#fff}
.auth-body{padding:24px 24px 8px}
.auth-body label{display:block;font-size:.8rem;font-weight:600;color:var(--p);margin-bottom:4px;margin-top:12px}
.auth-body label:first-child{margin-top:0}
.auth-body input{width:100%;padding:10px 12px;border:1px solid #d0d7e3;border-radius:8px;font-size:.9rem;outline:none;background:var(--bg);transition:.2s}
.auth-body input:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(26,58,92,.08)}
.auth-submit{width:100%;margin-top:18px;padding:11px;background:var(--p);color:#fff;border:none;border-radius:8px;font-size:.9rem;font-weight:700;cursor:pointer;transition:.2s}
.auth-submit:hover{background:#2d6a9f}
.auth-submit:disabled{opacity:.6;cursor:not-allowed}
.auth-error{color:#e74c3c;font-size:.78rem;margin-top:8px;display:none;text-align:center}
.auth-error.show{display:block}
.auth-success{color:#27ae60;font-size:.78rem;margin-top:8px;display:none;text-align:center}
.auth-success.show{display:block}
.auth-footer{padding:0 24px 20px;text-align:center;font-size:.82rem;color:var(--s)}
.auth-footer a{color:var(--p);font-weight:600;cursor:pointer;text-decoration:underline}
.auth-footer a:hover{color:#2d6a9f}
/* Auth Tabs */
.auth-tabs{display:flex;border-bottom:1px solid var(--bdr)}
.auth-tab{flex:1;text-align:center;padding:12px;font-size:.88rem;font-weight:600;color:var(--s);cursor:pointer;border:none;background:none;transition:.2s;border-bottom:2px solid transparent}
.auth-tab.active{color:var(--p);border-bottom-color:var(--p)}
.auth-tab:hover{color:var(--p);background:rgba(26,58,92,.03)}
/* Nav Auth Buttons */
.nav-auth-btns{display:flex;align-items:center;gap:8px}
.nav-btn-login,.nav-btn-register{padding:6px 14px;border-radius:6px;font-size:.8rem;font-weight:600;cursor:pointer;transition:.2s;border:none;white-space:nowrap}
.nav-btn-login{background:rgba(255,255,255,.15);color:#fff}
.nav-btn-login:hover{background:rgba(255,255,255,.25)}
.nav-btn-register{background:var(--a);color:var(--p)}
.nav-btn-register:hover{background:#e0a020}
.nav-user-info{display:flex;align-items:center;gap:8px;cursor:pointer;position:relative}
.nav-user-avatar{width:32px;height:32px;border-radius:50%;background:var(--a);color:var(--p);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem}
.nav-user-name{color:#fff;font-size:.82rem;font-weight:600;max-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nav-user-dropdown{display:none;position:absolute;top:100%;right:0;margin-top:6px;background:var(--c);border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.2);min-width:150px;overflow:hidden;z-index:1000}
.nav-user-info:hover .nav-user-dropdown,.nav-user-dropdown.show{display:block}
.nav-user-dropdown a,.nav-user-dropdown button{display:block;width:100%;padding:10px 16px;font-size:.82rem;color:var(--t);text-align:left;background:none;border:none;cursor:pointer;transition:.15s}
.nav-user-dropdown a:hover,.nav-user-dropdown button:hover{background:#f5f7fa;color:var(--p)}
.nav-user-dropdown button.logout-btn{color:#e74c3c;border-top:1px solid var(--bdr)}
/* Community Comments */
.community-section{max-width:1140px;margin:40px auto 0;padding:0 24px}
.community-section .sec-header{margin-bottom:20px}
.comment-box{background:var(--c);border-radius:var(--r);box-shadow:var(--sh);border:1px solid var(--bdr);overflow:hidden}
.comment-form-wrap{padding:20px 24px;border-bottom:1px solid var(--bdr);background:#fafbfc}
.comment-form-wrap .login-prompt{text-align:center;padding:16px;font-size:.88rem;color:var(--s)}
.comment-form-wrap .login-prompt a{color:var(--p);font-weight:600;cursor:pointer;text-decoration:underline}
.comment-input{width:100%;min-height:80px;padding:12px;border:1px solid #d0d7e3;border-radius:8px;font-size:.9rem;outline:none;resize:vertical;font-family:inherit;background:#fff;transition:.2s}
.comment-input:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(26,58,92,.08)}
.comment-submit-row{display:flex;justify-content:flex-end;align-items:center;gap:10px;margin-top:10px}
.comment-char-count{font-size:.75rem;color:var(--s)}
.comment-submit-btn{padding:8px 20px;background:var(--p);color:#fff;border:none;border-radius:6px;font-size:.85rem;font-weight:600;cursor:pointer;transition:.2s}
.comment-submit-btn:hover{background:#2d6a9f}
.comment-submit-btn:disabled{opacity:.5;cursor:not-allowed}
.comment-list{padding:16px 24px}
.comment-empty{text-align:center;padding:40px 20px;color:var(--s);font-size:.9rem}
.comment-empty .icon{font-size:2.5rem;display:block;margin-bottom:10px}
.comment-item{display:flex;gap:12px;padding:16px 0;border-bottom:1px solid #f0f1f3}
.comment-item:last-child{border-bottom:none}
.comment-avatar{width:36px;height:36px;border-radius:50%;background:var(--p);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.8rem;flex-shrink:0}
.comment-body{flex:1;min-width:0}
.comment-author{font-weight:600;font-size:.85rem;color:var(--p);margin-bottom:2px}
.comment-time{font-size:.72rem;color:#aaa;margin-left:8px;font-weight:400}
.comment-text{font-size:.88rem;color:var(--t);line-height:1.6;word-break:break-word}
.comment-actions{display:flex;gap:14px;margin-top:8px;align-items:center}
.comment-like,.comment-reply-btn,.comment-delete{background:none;border:none;font-size:.78rem;color:var(--s);cursor:pointer;padding:2px 4px;border-radius:4px;transition:.15s;display:flex;align-items:center;gap:4px}
.comment-like:hover,.comment-reply-btn:hover{color:var(--p);background:rgba(26,58,92,.05)}
.comment-delete:hover{color:#e74c3c;background:rgba(231,76,60,.05)}
.comment-like.liked{color:#e74c3c}
/* Reply thread */
.comment-replies{margin-left:32px;border-left:2px solid #edf0f5;padding-left:16px;margin-top:8px}
.comment-reply-form{padding:12px 0}
.comment-reply-form textarea{width:100%;min-height:50px;padding:10px;border:1px solid #d0d7e3;border-radius:6px;font-size:.85rem;outline:none;resize:vertical;font-family:inherit;transition:.2s}
.comment-reply-form textarea:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(26,58,92,.08)}
.comment-reply-actions{display:flex;justify-content:flex-end;gap:8px;margin-top:6px}
.comment-cancel-btn{padding:6px 14px;background:none;border:1px solid #d0d7e3;border-radius:6px;font-size:.8rem;cursor:pointer;color:var(--s);transition:.2s}
.comment-cancel-btn:hover{background:#f0f0f0}
.comment-loading{text-align:center;padding:20px;color:var(--s);font-size:.85rem}
@media(max-width:768px){
.community-section{padding:0 12px;margin:32px auto 0}
.comment-form-wrap{padding:14px 16px}
.comment-list{padding:12px 16px}
.comment-replies{margin-left:16px;padding-left:12px}
.nav-auth-btns .nav-btn-register{display:none}
.nav-user-name{display:none}
}"""

# ============================================================
# Auth Modal HTML
# ============================================================
AUTH_MODAL_HTML = """
<!-- ===== Auth Modal ===== -->
<div class="auth-overlay" id="auth-overlay">
<div class="auth-panel">
<div class="auth-header">
<button class="auth-close" id="auth-close">&times;</button>
<h3 id="auth-title" data-i18n="auth_login_title">登录</h3>
<p id="auth-subtitle" data-i18n="auth_login_subtitle">登录后参与社区讨论</p>
</div>
<div class="auth-tabs">
<button class="auth-tab active" data-tab="login" data-i18n="auth_tab_login">登录</button>
<button class="auth-tab" data-tab="register" data-i18n="auth_tab_register">注册</button>
</div>
<div class="auth-body" id="auth-body-login">
<label data-i18n="auth_email">邮箱</label>
<input type="email" id="login-email" placeholder="your@email.com" autocomplete="email">
<label data-i18n="auth_password">密码</label>
<input type="password" id="login-password" placeholder="········" autocomplete="current-password">
<div class="auth-error" id="login-error"></div>
<button class="auth-submit" id="login-submit" data-i18n="auth_btn_login">登录</button>
</div>
<div class="auth-body" id="auth-body-register" style="display:none">
<label data-i18n="auth_nickname">昵称</label>
<input type="text" id="register-nickname" placeholder="" autocomplete="name" data-i18n-attrib="placeholder:auth_nickname_ph">
<label data-i18n="auth_email">邮箱</label>
<input type="email" id="register-email" placeholder="your@email.com" autocomplete="email">
<label data-i18n="auth_password">密码</label>
<input type="password" id="register-password" placeholder="········" autocomplete="new-password">
<label data-i18n="auth_password_confirm">确认密码</label>
<input type="password" id="register-password-confirm" placeholder="········" autocomplete="new-password">
<div class="auth-error" id="register-error"></div>
<div class="auth-success" id="register-success"></div>
<button class="auth-submit" id="register-submit" data-i18n="auth_btn_register">注册</button>
</div>
<div class="auth-footer" id="auth-footer-login">
<span data-i18n="auth_no_account">还没有账号？</span> <a id="switch-to-register" data-i18n="auth_go_register">立即注册</a>
</div>
<div class="auth-footer" id="auth-footer-register" style="display:none">
<span data-i18n="auth_has_account">已有账号？</span> <a id="switch-to-login" data-i18n="auth_go_login">去登录</a>
</div>
</div>
</div>"""

# ============================================================
# Community Section HTML (replaces Giscus)
# ============================================================
COMMUNITY_HTML = """
<!-- ===== Community Discussion Section ===== -->
<section class="community-section" id="community">
<div class="sec-header">
<h2><span data-i18n="community_title">💬 全球贸易商交流区</span></h2>
<div class="sec-divider"></div>
<p data-i18n="community_desc">跨境贸易同行交流讨论，分享经验、解答疑问</p>
</div>
<div class="comment-box">
<div class="comment-form-wrap" id="comment-form-wrap">
<!-- Filled by JS: either login prompt or comment form -->
</div>
<div class="comment-loading" id="comment-loading">⏳ <span data-i18n="comment_loading">加载评论中...</span></div>
<div class="comment-list" id="comment-list"></div>
<div class="comment-empty" id="comment-empty" style="display:none">
<span class="icon">💬</span>
<p data-i18n="comment_empty">暂无评论，成为第一个发言的人吧！</p>
</div>
</div>
</section>"""

# ============================================================
# Navbar additions
# ============================================================
NAV_COMMUNITY_LINK = '\n  <a href="#community" data-i18n="nav_community">用户交流</a>'
NAV_AUTH_BUTTONS = """
<!-- Auth Buttons -->
<div class="nav-auth-btns" id="nav-auth-btns">
<button class="nav-btn-login" id="nav-btn-login" data-i18n="btn_login">登录</button>
<button class="nav-btn-register" id="nav-btn-register" data-i18n="btn_register">注册</button>
<div class="nav-user-info" id="nav-user-info" style="display:none">
<div class="nav-user-avatar" id="nav-user-avatar">?</div>
<span class="nav-user-name" id="nav-user-name"></span>
<div class="nav-user-dropdown" id="nav-user-dropdown">
<a href="#" id="nav-my-comments" data-i18n="nav_my_profile">我的主页</a>
<button class="logout-btn" id="nav-logout" data-i18n="btn_logout">退出登录</button>
</div>
</div>
</div>"""

# ============================================================
# Supabase SDK + Auth JS + Comment JS
# ============================================================
AUTH_COMMUNITY_JS_TEMPLATE = """
// ===== Supabase Client =====
var SUPABASE_URL = '{supabase_url}';
var SUPABASE_ANON_KEY = '{supabase_anon_key}';
var supabaseClient = null;

function initSupabase(){{
  if(!SUPABASE_URL || SUPABASE_URL==='SUPABASE_URL_PLACEHOLDER'){{
    console.warn('[Auth] Supabase not configured');
    return false;
  }}
  if(supabaseClient)return true;
  try{{
    supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    return true;
  }}catch(e){{
    console.error('[Auth] Failed to init Supabase:', e);
    return false;
  }}
}}

// ===== Auth State =====
var currentUser = null;

async function checkSession(){{
  if(!initSupabase())return;
  try{{
    var d = (await supabaseClient.auth.getSession()).data;
    if(d && d.session){{
      currentUser = d.session.user;
    }}
  }}catch(e){{}}
  updateAuthUI();
}}

function updateAuthUI(){{
  var btns = document.getElementById('nav-auth-btns');
  if(!btns)return;
  var loginBtn = document.getElementById('nav-btn-login');
  var registerBtn = document.getElementById('nav-btn-register');
  var userInfo = document.getElementById('nav-user-info');
  var userName = document.getElementById('nav-user-name');
  var userAvatar = document.getElementById('nav-user-avatar');

  if(currentUser){{
    if(loginBtn)loginBtn.style.display='none';
    if(registerBtn)registerBtn.style.display='none';
    if(userInfo)userInfo.style.display='flex';
    var nick = (currentUser.user_metadata && currentUser.user_metadata.nickname) || currentUser.email.split('@')[0];
    if(userName)userName.textContent = nick;
    if(userAvatar)userAvatar.textContent = (nick[0]||'?').toUpperCase();
  }}else{{
    if(loginBtn)loginBtn.style.display='';
    if(registerBtn)registerBtn.style.display='';
    if(userInfo)userInfo.style.display='none';
  }}
  // Update comment form
  updateCommentForm();
}}

// ===== Auth Modal =====
function openAuthModal(tab){{
  var overlay = document.getElementById('auth-overlay');
  if(!overlay)return;
  overlay.classList.add('show');
  switchAuthTab(tab||'login');
}}

function closeAuthModal(){{
  var overlay = document.getElementById('auth-overlay');
  if(overlay)overlay.classList.remove('show');
  clearAuthErrors();
}}

function switchAuthTab(tab){{
  var loginBody = document.getElementById('auth-body-login');
  var registerBody = document.getElementById('auth-body-register');
  var loginFooter = document.getElementById('auth-footer-login');
  var registerFooter = document.getElementById('auth-footer-register');
  var tabs = document.querySelectorAll('.auth-tab');
  var title = document.getElementById('auth-title');
  var subtitle = document.getElementById('auth-subtitle');
  var d = (I18N[curLang]||I18N.en);

  tabs.forEach(function(t){{ t.classList.remove('active'); }});
  if(tab==='register'){{
    if(loginBody)loginBody.style.display='none';
    if(registerBody)registerBody.style.display='';
    if(loginFooter)loginFooter.style.display='none';
    if(registerFooter)registerFooter.style.display='';
    var regTab = document.querySelector('.auth-tab[data-tab="register"]');
    if(regTab)regTab.classList.add('active');
    if(title)title.textContent = d.auth_register_title||'Register';
    if(subtitle)subtitle.textContent = d.auth_register_subtitle||'Join our community';
  }}else{{
    if(loginBody)loginBody.style.display='';
    if(registerBody)registerBody.style.display='none';
    if(loginFooter)loginFooter.style.display='';
    if(registerFooter)registerFooter.style.display='none';
    var loginTab = document.querySelector('.auth-tab[data-tab="login"]');
    if(loginTab)loginTab.classList.add('active');
    if(title)title.textContent = d.auth_login_title||'Login';
    if(subtitle)subtitle.textContent = d.auth_login_subtitle||'Login to join the discussion';
  }}
  clearAuthErrors();
}}

function clearAuthErrors(){{
  var loginErr = document.getElementById('login-error');
  var regErr = document.getElementById('register-error');
  var regSuccess = document.getElementById('register-success');
  if(loginErr){{loginErr.textContent='';loginErr.classList.remove('show');}}
  if(regErr){{regErr.textContent='';regErr.classList.remove('show');}}
  if(regSuccess){{regSuccess.textContent='';regSuccess.classList.remove('show');}}
}}

async function handleLogin(){{
  if(!initSupabase()){{
    showLoginError('Auth system not configured');
    return;
  }}
  var email = document.getElementById('login-email').value.trim();
  var password = document.getElementById('login-password').value;
  if(!email||!password){{showLoginError('Please enter email and password');return;}}
  var btn = document.getElementById('login-submit');
  if(btn)btn.disabled = true;
  try{{
    var r = await supabaseClient.auth.signInWithPassword({{email:email,password:password}});
    if(r.error){{showLoginError(r.error.message);if(btn)btn.disabled=false;return;}}
    currentUser = r.data.user;
    updateAuthUI();
    closeAuthModal();
    loadComments();
  }}catch(e){{showLoginError(e.message);if(btn)btn.disabled=false;}}
}}

async function handleRegister(){{
  if(!initSupabase()){{
    showRegisterError('Auth system not configured');
    return;
  }}
  var nickname = document.getElementById('register-nickname').value.trim();
  var email = document.getElementById('register-email').value.trim();
  var password = document.getElementById('register-password').value;
  var confirm = document.getElementById('register-password-confirm').value;
  if(!nickname||!email||!password){{showRegisterError('Please fill all fields');return;}}
  if(password!==confirm){{showRegisterError('Passwords do not match');return;}}
  if(password.length<6){{showRegisterError('Password must be at least 6 characters');return;}}
  var btn = document.getElementById('register-submit');
  if(btn)btn.disabled = true;
  try{{
    var r = await supabaseClient.auth.signUp({{
      email:email,
      password:password,
      options:{{data:{{nickname:nickname}}}}
    }});
    if(r.error){{showRegisterError(r.error.message);if(btn)btn.disabled=false;return;}}
    if(r.data.user && !r.data.session){{
      // Email confirmation required
      var success = document.getElementById('register-success');
      var d = (I18N[curLang]||I18N.en);
      if(success){{success.textContent = d.auth_check_email||'Check your email to confirm registration!';success.classList.add('show');}}
      if(btn)btn.disabled = false;
    }}else{{
      currentUser = r.data.user;
      updateAuthUI();
      closeAuthModal();
      loadComments();
    }}
  }}catch(e){{showRegisterError(e.message);if(btn)btn.disabled=false;}}
}}

function showLoginError(msg){{var el=document.getElementById('login-error');if(el){{el.textContent=translateError(msg);el.classList.add('show');}}}}
function showRegisterError(msg){{var el=document.getElementById('register-error');if(el){{el.textContent=translateError(msg);el.classList.add('show');}}}}

function translateError(msg){{
  var map={{
    'Invalid login credentials':'邮箱或密码错误',
    'User already registered':'该邮箱已注册',
    'Password must be at least 6 characters':'密码至少6位',
    'Passwords do not match':'两次密码不一致',
    'Please enter email and password':'请输入邮箱和密码',
    'Please fill all fields':'请填写所有字段',
    'Auth system not configured':'认证系统未配置',
    'Email not confirmed':'邮箱未验证，请检查邮件'
  }};
  return map[msg]||msg;
}}

async function handleLogout(){{
  if(supabaseClient){{
    await supabaseClient.auth.signOut();
  }}
  currentUser = null;
  updateAuthUI();
  loadComments();
}}

// ===== Comment System =====
var currentComments = [];
var activeReplyId = null;

function getPagePath(){{
  var path = window.location.pathname;
  var page = path.split('/').pop()||'index.html';
  if(!page||page==='/')page='index.html';
  var lang = new URLSearchParams(window.location.search).get('lang');
  if(lang)page = page + '?lang=' + lang.substring(0,5);
  return page;
}}

function updateCommentForm(){{
  var wrap = document.getElementById('comment-form-wrap');
  if(!wrap)return;
  var d = (I18N[curLang]||I18N.en);
  if(currentUser){{
    wrap.innerHTML = '<textarea class="comment-input" id="comment-input" maxlength="1000" placeholder="' + (d.comment_placeholder||'Share your thoughts...') + '"></textarea>' +
      '<div class="comment-submit-row">' +
      '<span class="comment-char-count" id="comment-char-count">0/1000</span>' +
      '<button class="comment-submit-btn" id="comment-submit" data-i18n="comment_submit">' + (d.comment_submit||'Post') + '</button>' +
      '</div>';
    var input = document.getElementById('comment-input');
    var count = document.getElementById('comment-char-count');
    if(input&&count){{
      input.addEventListener('input',function(){{count.textContent=input.value.length+'/1000';}});
    }}
    var submit = document.getElementById('comment-submit');
    if(submit)submit.addEventListener('click',submitComment);
  }}else{{
    wrap.innerHTML = '<div class="login-prompt">' +
      '<a id="comment-login-link" data-i18n="comment_login_first">登录</a> ' +
      '<span data-i18n="comment_login_to_post">后发表评论</span></div>';
    var loginLink = document.getElementById('comment-login-link');
    if(loginLink)loginLink.addEventListener('click',function(e){{e.preventDefault();openAuthModal('login');}});
  }}
}}

async function submitComment(){{
  var input = document.getElementById('comment-input');
  if(!input||!input.value.trim())return;
  var content = input.value.trim();
  if(content.length>1000)return;
  var btn = document.getElementById('comment-submit');
  if(btn)btn.disabled = true;
  try{{
    var r = await supabaseClient.from('comments').insert({{
      page_path: getPagePath(),
      user_id: currentUser.id,
      content: content,
      parent_id: null
    }}).select('*, profiles(nickname)').single();
    if(r.error){{console.error(r.error);if(btn)btn.disabled=false;return;}}
    input.value = '';
    document.getElementById('comment-char-count').textContent = '0/1000';
    if(btn)btn.disabled = false;
    await loadComments();
  }}catch(e){{console.error(e);if(btn)btn.disabled=false;}}
}}

async function submitReply(parentId){{
  var form = document.getElementById('reply-form-' + parentId);
  var textarea = form ? form.querySelector('textarea') : null;
  if(!textarea||!textarea.value.trim())return;
  var content = textarea.value.trim();
  try{{
    var r = await supabaseClient.from('comments').insert({{
      page_path: getPagePath(),
      user_id: currentUser.id,
      content: content,
      parent_id: parentId
    }}).select('*, profiles(nickname)').single();
    if(r.error){{console.error(r.error);return;}}
    activeReplyId = null;
    await loadComments();
  }}catch(e){{console.error(e);}}
}}

function showReplyForm(commentId){{
  activeReplyId = activeReplyId===commentId ? null : commentId;
  loadComments();
}}

async function toggleLike(commentId, currentLikes){{
  if(!currentUser){{openAuthModal('login');return;}}
  try{{
    await supabaseClient.from('comments').update({{likes: (currentLikes||0)+1}}).eq('id', commentId);
    await loadComments();
  }}catch(e){{console.error(e);}}
}}

async function deleteComment(commentId){{
  if(!currentUser)return;
  var d = (I18N[curLang]||I18N.en);
  if(!confirm(d.comment_delete_confirm||'Delete this comment?'))return;
  try{{
    await supabaseClient.from('comments').delete().eq('id', commentId);
    await loadComments();
  }}catch(e){{console.error(e);}}
}}

async function loadComments(){{
  var loading = document.getElementById('comment-loading');
  var list = document.getElementById('comment-list');
  var empty = document.getElementById('comment-empty');
  if(loading)loading.style.display = 'block';
  if(list)list.innerHTML = '';
  if(empty)empty.style.display = 'none';

  try{{
    var r = await supabaseClient.from('comments')
      .select('*, profiles!comments_user_id_fkey(nickname)')
      .eq('page_path', getPagePath())
      .order('created_at', {{ascending: true}});

    if(r.error){{console.error(r.error);if(loading)loading.style.display='none';return;}}

    currentComments = r.data||[];
    if(loading)loading.style.display = 'none';

    if(currentComments.length===0){{
      if(empty)empty.style.display = 'block';
      return;
    }}

    // Build nested structure
    var topLevel = currentComments.filter(function(c){{return !c.parent_id;}});
    renderComments(topLevel, list);
  }}catch(e){{console.error(e);if(loading)loading.style.display='none';}}
}}

function renderComments(comments, container){{
  if(!container)return;
  var d = (I18N[curLang]||I18N.en);
  container.innerHTML = '';

  comments.forEach(function(c){{
    var replies = currentComments.filter(function(r){{return r.parent_id===c.id;}});
    var nickname = (c.profiles&&c.profiles.nickname)||'User';
    var timeAgo = formatTimeAgo(c.created_at);
    var isOwner = currentUser && currentUser.id === c.user_id;

    var html = '<div class="comment-item">' +
      '<div class="comment-avatar">' + (nickname[0]||'?').toUpperCase() + '</div>' +
      '<div class="comment-body">' +
      '<div class="comment-author">' + escapeHtml(nickname) + '<span class="comment-time">' + timeAgo + '</span></div>' +
      '<div class="comment-text">' + escapeHtml(c.content) + '</div>' +
      '<div class="comment-actions">' +
      '<button class="comment-like' + (false?' liked':'') + '" onclick="toggleLike('+c.id+','+c.likes+')">❤️ ' + (c.likes||0) + '</button>' +
      '<button class="comment-reply-btn" onclick="showReplyForm('+c.id+')" data-i18n="comment_reply">' + (d.comment_reply||'Reply') + '</button>' +
      (isOwner?'<button class="comment-delete" onclick="deleteComment('+c.id+')" data-i18n="comment_delete">' + (d.comment_delete||'Delete') + '</button>':'') +
      '</div>';

    // Reply form
    if(activeReplyId===c.id){{
      html += '<div class="comment-reply-form" id="reply-form-'+c.id+'">' +
        '<textarea placeholder="' + (d.comment_reply_ph||'Write a reply...') + '" rows="2"></textarea>' +
        '<div class="comment-reply-actions">' +
        '<button class="comment-cancel-btn" onclick="showReplyForm('+c.id+')" data-i18n="comment_cancel">' + (d.comment_cancel||'Cancel') + '</button>' +
        '<button class="comment-submit-btn" onclick="submitReply('+c.id+')" data-i18n="comment_submit">' + (d.comment_submit||'Post') + '</button>' +
        '</div></div>';
    }}

    // Replies
    if(replies.length>0){{
      html += '<div class="comment-replies">';
      replies.forEach(function(r){{
        var rNick = (r.profiles&&r.profiles.nickname)||'User';
        var rTime = formatTimeAgo(r.created_at);
        var rIsOwner = currentUser && currentUser.id === r.user_id;
        html += '<div class="comment-item">' +
          '<div class="comment-avatar">' + (rNick[0]||'?').toUpperCase() + '</div>' +
          '<div class="comment-body">' +
          '<div class="comment-author">' + escapeHtml(rNick) + '<span class="comment-time">' + rTime + '</span></div>' +
          '<div class="comment-text">' + escapeHtml(r.content) + '</div>' +
          '<div class="comment-actions">' +
          '<button class="comment-like" onclick="toggleLike('+r.id+','+r.likes+')">❤️ ' + (r.likes||0) + '</button>' +
          (rIsOwner?'<button class="comment-delete" onclick="deleteComment('+r.id+')" data-i18n="comment_delete">' + (d.comment_delete||'Delete') + '</button>':'') +
          '</div></div></div>';
      }});
      html += '</div>';
    }}

    html += '</div></div>';
    container.innerHTML += html;
  }});
}}

function escapeHtml(text){{
  var map={{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',\"'\":'&#039;'}};
  return (''+text).replace(/[&<>\"']/g,function(m){{return map[m];}});
}}

function formatTimeAgo(dateStr){{
  if(!dateStr)return '';
  var now = new Date();
  var date = new Date(dateStr);
  var diff = Math.floor((now-date)/1000);
  if(diff<60)return 'just now';
  if(diff<3600)return Math.floor(diff/60)+'m ago';
  if(diff<86400)return Math.floor(diff/3600)+'h ago';
  if(diff<604800)return Math.floor(diff/86400)+'d ago';
  return date.toLocaleDateString();
}}

// ===== Init =====
document.addEventListener('DOMContentLoaded', function(){{
  // Load Supabase SDK dynamically
  var supabaseScript = document.getElementById('supabase-sdk');
  if(!supabaseScript){{
    var s = document.createElement('script');
    s.id = 'supabase-sdk';
    s.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js';
    s.onload = function(){{
      checkSession().then(function(){{
        loadComments();
      }});
    }};
    s.onerror = function(){{
      console.warn('[Auth] Failed to load Supabase SDK');
      updateCommentForm();
    }};
    document.head.appendChild(s);
  }}else{{
    checkSession().then(function(){{
      loadComments();
    }});
  }}

  // Auth modal events
  var authOverlay = document.getElementById('auth-overlay');
  var authClose = document.getElementById('auth-close');
  var loginSubmit = document.getElementById('login-submit');
  var registerSubmit = document.getElementById('register-submit');
  var switchReg = document.getElementById('switch-to-register');
  var switchLogin = document.getElementById('switch-to-login');
  var navLogin = document.getElementById('nav-btn-login');
  var navRegister = document.getElementById('nav-btn-register');
  var navLogout = document.getElementById('nav-logout');

  if(authOverlay)authOverlay.addEventListener('click',function(e){{if(e.target===authOverlay)closeAuthModal();}});
  if(authClose)authClose.addEventListener('click',closeAuthModal);
  if(loginSubmit)loginSubmit.addEventListener('click',handleLogin);
  if(registerSubmit)registerSubmit.addEventListener('click',handleRegister);
  if(switchReg)switchReg.addEventListener('click',function(){{switchAuthTab('register');}});
  if(switchLogin)switchLogin.addEventListener('click',function(){{switchAuthTab('login');}});
  if(navLogin)navLogin.addEventListener('click',function(){{openAuthModal('login');}});
  if(navRegister)navRegister.addEventListener('click',function(){{openAuthModal('register');}});
  if(navLogout)navLogout.addEventListener('click',function(e){{e.preventDefault();handleLogout();}});

  // Auth tabs
  document.querySelectorAll('.auth-tab').forEach(function(tab){{
    tab.addEventListener('click',function(){{
      switchAuthTab(tab.dataset.tab);
    }});
  }});

  // Keyboard enter to submit
  var loginPw = document.getElementById('login-password');
  var regPw = document.getElementById('register-password');
  if(loginPw)loginPw.addEventListener('keydown',function(e){{if(e.key==='Enter')handleLogin();}});
  if(regPw)regPw.addEventListener('keydown',function(e){{if(e.key==='Enter')handleRegister();}});

  // Nav dropdown toggle
  var userInfo = document.getElementById('nav-user-info');
  var dropdown = document.getElementById('nav-user-dropdown');
  if(userInfo&&dropdown){{
    userInfo.addEventListener('click',function(e){{
      e.stopPropagation();
      dropdown.classList.toggle('show');
    }});
    document.addEventListener('click',function(){{dropdown.classList.remove('show');}});
  }}
}});
"""

# ============================================================
# i18n additions (18 languages)
# ============================================================
I18N_ADDITIONS = {
    "zh": {
        "nav_community": "用户交流",
        "btn_login": "登录",
        "btn_register": "注册",
        "btn_logout": "退出登录",
        "nav_my_profile": "我的主页",
        "auth_login_title": "登录 GlobalTrade Hub",
        "auth_login_subtitle": "登录后参与社区讨论",
        "auth_register_title": "注册 GlobalTrade Hub",
        "auth_register_subtitle": "加入跨境贸易社区",
        "auth_tab_login": "登录",
        "auth_tab_register": "注册",
        "auth_email": "邮箱",
        "auth_password": "密码",
        "auth_password_confirm": "确认密码",
        "auth_nickname": "昵称",
        "auth_nickname_ph": "您的昵称",
        "auth_btn_login": "登录",
        "auth_btn_register": "创建账号",
        "auth_no_account": "还没有账号？",
        "auth_go_register": "立即注册",
        "auth_has_account": "已有账号？",
        "auth_go_login": "去登录",
        "auth_check_email": "注册成功！请检查邮箱确认。",
        "community_title": "💬 全球贸易商交流区",
        "community_desc": "跨境贸易同行交流讨论，分享经验、解答疑问",
        "comment_loading": "加载评论中...",
        "comment_empty": "暂无评论，成为第一个发言的人吧！",
        "comment_placeholder": "分享您的跨境贸易经验或疑问...",
        "comment_submit": "发表",
        "comment_login_first": "登录",
        "comment_login_to_post": "后发表评论",
        "comment_reply": "回复",
        "comment_delete": "删除",
        "comment_cancel": "取消",
        "comment_reply_ph": "写下回复...",
        "comment_delete_confirm": "确定要删除这条评论吗？"
    },
    "en": {
        "nav_community": "Community",
        "btn_login": "Login",
        "btn_register": "Register",
        "btn_logout": "Logout",
        "nav_my_profile": "My Profile",
        "auth_login_title": "Login to GlobalTrade Hub",
        "auth_login_subtitle": "Login to join the discussion",
        "auth_register_title": "Register at GlobalTrade Hub",
        "auth_register_subtitle": "Join the cross-border trade community",
        "auth_tab_login": "Login",
        "auth_tab_register": "Register",
        "auth_email": "Email",
        "auth_password": "Password",
        "auth_password_confirm": "Confirm Password",
        "auth_nickname": "Nickname",
        "auth_nickname_ph": "Your nickname",
        "auth_btn_login": "Login",
        "auth_btn_register": "Create Account",
        "auth_no_account": "Don't have an account?",
        "auth_go_register": "Register now",
        "auth_has_account": "Already have an account?",
        "auth_go_login": "Login",
        "auth_check_email": "Registration successful! Check your email to confirm.",
        "community_title": "💬 Global Trade Community",
        "community_desc": "Connect with fellow traders, share insights and get answers",
        "comment_loading": "Loading comments...",
        "comment_empty": "No comments yet. Be the first to share!",
        "comment_placeholder": "Share your cross-border trade experience...",
        "comment_submit": "Post",
        "comment_login_first": "Login",
        "comment_login_to_post": "to post a comment",
        "comment_reply": "Reply",
        "comment_delete": "Delete",
        "comment_cancel": "Cancel",
        "comment_reply_ph": "Write a reply...",
        "comment_delete_confirm": "Are you sure you want to delete this comment?"
    },
    "es": {
        "nav_community": "Comunidad",
        "btn_login": "Iniciar sesión",
        "btn_register": "Registrarse",
        "btn_logout": "Cerrar sesión",
        "nav_my_profile": "Mi Perfil",
        "auth_login_title": "Iniciar sesión en GlobalTrade Hub",
        "auth_login_subtitle": "Inicia sesión para participar",
        "auth_register_title": "Registrarse en GlobalTrade Hub",
        "auth_register_subtitle": "Únete a la comunidad de comercio",
        "auth_tab_login": "Iniciar sesión",
        "auth_tab_register": "Registrarse",
        "auth_email": "Correo electrónico",
        "auth_password": "Contraseña",
        "auth_password_confirm": "Confirmar contraseña",
        "auth_nickname": "Apodo",
        "auth_nickname_ph": "Tu apodo",
        "auth_btn_login": "Entrar",
        "auth_btn_register": "Crear cuenta",
        "auth_no_account": "¿No tienes cuenta?",
        "auth_go_register": "Regístrate",
        "auth_has_account": "¿Ya tienes cuenta?",
        "auth_go_login": "Iniciar sesión",
        "auth_check_email": "¡Registro exitoso! Revisa tu correo.",
        "community_title": "💬 Comunidad de Comercio Global",
        "community_desc": "Conecta con otros comerciantes, comparte ideas",
        "comment_loading": "Cargando comentarios...",
        "comment_empty": "Sin comentarios aún. ¡Sé el primero!",
        "comment_placeholder": "Comparte tu experiencia...",
        "comment_submit": "Publicar",
        "comment_login_first": "Inicia sesión",
        "comment_login_to_post": "para comentar",
        "comment_reply": "Responder",
        "comment_delete": "Eliminar",
        "comment_cancel": "Cancelar",
        "comment_reply_ph": "Escribe una respuesta...",
        "comment_delete_confirm": "¿Eliminar este comentario?"
    },
    "pt": {
        "nav_community": "Comunidade",
        "btn_login": "Entrar",
        "btn_register": "Registrar",
        "btn_logout": "Sair",
        "nav_my_profile": "Meu Perfil",
        "auth_login_title": "Entrar no GlobalTrade Hub",
        "auth_login_subtitle": "Entre para participar das discussões",
        "auth_register_title": "Registrar no GlobalTrade Hub",
        "auth_register_subtitle": "Junte-se à comunidade de comércio",
        "auth_tab_login": "Entrar",
        "auth_tab_register": "Registrar",
        "auth_email": "E-mail",
        "auth_password": "Senha",
        "auth_password_confirm": "Confirmar senha",
        "auth_nickname": "Apelido",
        "auth_nickname_ph": "Seu apelido",
        "auth_btn_login": "Entrar",
        "auth_btn_register": "Criar conta",
        "auth_no_account": "Não tem conta?",
        "auth_go_register": "Registre-se",
        "auth_has_account": "Já tem conta?",
        "auth_go_login": "Entrar",
        "auth_check_email": "Registro concluído! Verifique seu e-mail.",
        "community_title": "💬 Comunidade de Comércio Global",
        "community_desc": "Conecte-se com outros comerciantes",
        "comment_loading": "Carregando comentários...",
        "comment_empty": "Sem comentários. Seja o primeiro!",
        "comment_placeholder": "Compartilhe sua experiência...",
        "comment_submit": "Publicar",
        "comment_login_first": "Entrar",
        "comment_login_to_post": "para comentar",
        "comment_reply": "Responder",
        "comment_delete": "Excluir",
        "comment_cancel": "Cancelar",
        "comment_reply_ph": "Escreva uma resposta...",
        "comment_delete_confirm": "Excluir este comentário?"
    },
    "ru": {
        "nav_community": "Сообщество",
        "btn_login": "Войти",
        "btn_register": "Регистрация",
        "btn_logout": "Выйти",
        "nav_my_profile": "Профиль",
        "auth_login_title": "Войти в GlobalTrade Hub",
        "auth_login_subtitle": "Войдите для участия в обсуждениях",
        "auth_register_title": "Регистрация в GlobalTrade Hub",
        "auth_register_subtitle": "Присоединяйтесь к сообществу",
        "auth_tab_login": "Войти",
        "auth_tab_register": "Регистрация",
        "auth_email": "Эл. почта",
        "auth_password": "Пароль",
        "auth_password_confirm": "Подтвердите пароль",
        "auth_nickname": "Никнейм",
        "auth_nickname_ph": "Ваш никнейм",
        "auth_btn_login": "Войти",
        "auth_btn_register": "Создать аккаунт",
        "auth_no_account": "Нет аккаунта?",
        "auth_go_register": "Зарегистрироваться",
        "auth_has_account": "Уже есть аккаунт?",
        "auth_go_login": "Войти",
        "auth_check_email": "Регистрация успешна! Проверьте почту.",
        "community_title": "💬 Сообщество трейдеров",
        "community_desc": "Общайтесь с коллегами, делитесь опытом",
        "comment_loading": "Загрузка комментариев...",
        "comment_empty": "Нет комментариев. Будьте первым!",
        "comment_placeholder": "Поделитесь опытом...",
        "comment_submit": "Отправить",
        "comment_login_first": "Войти",
        "comment_login_to_post": "чтобы комментировать",
        "comment_reply": "Ответить",
        "comment_delete": "Удалить",
        "comment_cancel": "Отмена",
        "comment_reply_ph": "Напишите ответ...",
        "comment_delete_confirm": "Удалить этот комментарий?"
    },
    "fr": {
        "nav_community": "Communauté",
        "btn_login": "Connexion",
        "btn_register": "S'inscrire",
        "btn_logout": "Déconnexion",
        "nav_my_profile": "Mon Profil",
        "auth_login_title": "Connexion à GlobalTrade Hub",
        "auth_login_subtitle": "Connectez-vous pour participer",
        "auth_register_title": "Inscription à GlobalTrade Hub",
        "auth_register_subtitle": "Rejoignez la communauté",
        "auth_tab_login": "Connexion",
        "auth_tab_register": "Inscription",
        "auth_email": "E-mail",
        "auth_password": "Mot de passe",
        "auth_password_confirm": "Confirmer le mot de passe",
        "auth_nickname": "Pseudo",
        "auth_nickname_ph": "Votre pseudo",
        "auth_btn_login": "Se connecter",
        "auth_btn_register": "Créer un compte",
        "auth_no_account": "Pas de compte ?",
        "auth_go_register": "S'inscrire",
        "auth_has_account": "Déjà un compte ?",
        "auth_go_login": "Se connecter",
        "auth_check_email": "Inscription réussie ! Vérifiez votre e-mail.",
        "community_title": "💬 Communauté Commerciale",
        "community_desc": "Échangez avec d'autres commerçants",
        "comment_loading": "Chargement des commentaires...",
        "comment_empty": "Aucun commentaire. Soyez le premier !",
        "comment_placeholder": "Partagez votre expérience...",
        "comment_submit": "Publier",
        "comment_login_first": "Connectez-vous",
        "comment_login_to_post": "pour commenter",
        "comment_reply": "Répondre",
        "comment_delete": "Supprimer",
        "comment_cancel": "Annuler",
        "comment_reply_ph": "Écrivez une réponse...",
        "comment_delete_confirm": "Supprimer ce commentaire ?"
    },
    "de": {
        "nav_community": "Community",
        "btn_login": "Anmelden",
        "btn_register": "Registrieren",
        "btn_logout": "Abmelden",
        "nav_my_profile": "Mein Profil",
        "auth_login_title": "Anmeldung bei GlobalTrade Hub",
        "auth_login_subtitle": "Melden Sie sich an, um teilzunehmen",
        "auth_register_title": "Registrierung bei GlobalTrade Hub",
        "auth_register_subtitle": "Treten Sie der Community bei",
        "auth_tab_login": "Anmelden",
        "auth_tab_register": "Registrieren",
        "auth_email": "E-Mail",
        "auth_password": "Passwort",
        "auth_password_confirm": "Passwort bestätigen",
        "auth_nickname": "Spitzname",
        "auth_nickname_ph": "Ihr Spitzname",
        "auth_btn_login": "Anmelden",
        "auth_btn_register": "Konto erstellen",
        "auth_no_account": "Noch kein Konto?",
        "auth_go_register": "Jetzt registrieren",
        "auth_has_account": "Bereits ein Konto?",
        "auth_go_login": "Anmelden",
        "auth_check_email": "Registrierung erfolgreich! Prüfen Sie Ihre E-Mails.",
        "community_title": "💬 Handels-Community",
        "community_desc": "Vernetzen Sie sich mit anderen Händlern",
        "comment_loading": "Kommentare werden geladen...",
        "comment_empty": "Noch keine Kommentare. Seien Sie der Erste!",
        "comment_placeholder": "Teilen Sie Ihre Erfahrungen...",
        "comment_submit": "Senden",
        "comment_login_first": "Anmelden",
        "comment_login_to_post": "um zu kommentieren",
        "comment_reply": "Antworten",
        "comment_delete": "Löschen",
        "comment_cancel": "Abbrechen",
        "comment_reply_ph": "Antwort schreiben...",
        "comment_delete_confirm": "Diesen Kommentar löschen?"
    },
    "it": {
        "nav_community": "Community",
        "btn_login": "Accedi",
        "btn_register": "Registrati",
        "btn_logout": "Esci",
        "nav_my_profile": "Mio Profilo",
        "auth_login_title": "Accedi a GlobalTrade Hub",
        "auth_login_subtitle": "Accedi per partecipare",
        "auth_register_title": "Registrati su GlobalTrade Hub",
        "auth_register_subtitle": "Unisciti alla community",
        "auth_tab_login": "Accedi",
        "auth_tab_register": "Registrati",
        "auth_email": "Email",
        "auth_password": "Password",
        "auth_password_confirm": "Conferma password",
        "auth_nickname": "Nickname",
        "auth_nickname_ph": "Il tuo nickname",
        "auth_btn_login": "Accedi",
        "auth_btn_register": "Crea account",
        "auth_no_account": "Non hai un account?",
        "auth_go_register": "Registrati",
        "auth_has_account": "Hai già un account?",
        "auth_go_login": "Accedi",
        "auth_check_email": "Registrazione completata! Controlla la tua email.",
        "community_title": "💬 Community di Commercio",
        "community_desc": "Connettiti con altri commercianti",
        "comment_loading": "Caricamento commenti...",
        "comment_empty": "Nessun commento. Sii il primo!",
        "comment_placeholder": "Condividi la tua esperienza...",
        "comment_submit": "Pubblica",
        "comment_login_first": "Accedi",
        "comment_login_to_post": "per commentare",
        "comment_reply": "Rispondi",
        "comment_delete": "Elimina",
        "comment_cancel": "Annulla",
        "comment_reply_ph": "Scrivi una risposta...",
        "comment_delete_confirm": "Eliminare questo commento?"
    },
    "ar": {
        "nav_community": "المجتمع",
        "btn_login": "تسجيل الدخول",
        "btn_register": "التسجيل",
        "btn_logout": "تسجيل الخروج",
        "nav_my_profile": "ملفي",
        "auth_login_title": "تسجيل الدخول إلى GlobalTrade Hub",
        "auth_login_subtitle": "سجل الدخول للمشاركة",
        "auth_register_title": "التسجيل في GlobalTrade Hub",
        "auth_register_subtitle": "انضم إلى مجتمع التجارة",
        "auth_tab_login": "تسجيل الدخول",
        "auth_tab_register": "التسجيل",
        "auth_email": "البريد الإلكتروني",
        "auth_password": "كلمة المرور",
        "auth_password_confirm": "تأكيد كلمة المرور",
        "auth_nickname": "اللقب",
        "auth_nickname_ph": "لقبك",
        "auth_btn_login": "دخول",
        "auth_btn_register": "إنشاء حساب",
        "auth_no_account": "ليس لديك حساب؟",
        "auth_go_register": "سجل الآن",
        "auth_has_account": "لديك حساب بالفعل؟",
        "auth_go_login": "تسجيل الدخول",
        "auth_check_email": "تم التسجيل بنجاح! تحقق من بريدك الإلكتروني.",
        "community_title": "💬 مجتمع التجارة العالمي",
        "community_desc": "تواصل مع التجار الآخرين",
        "comment_loading": "جاري تحميل التعليقات...",
        "comment_empty": "لا توجد تعليقات. كن أول من يشارك!",
        "comment_placeholder": "شارك تجربتك...",
        "comment_submit": "نشر",
        "comment_login_first": "تسجيل الدخول",
        "comment_login_to_post": "للتعليق",
        "comment_reply": "رد",
        "comment_delete": "حذف",
        "comment_cancel": "إلغاء",
        "comment_reply_ph": "اكتب رداً...",
        "comment_delete_confirm": "هل تريد حذف هذا التعليق؟"
    },
    "tr": {
        "nav_community": "Topluluk",
        "btn_login": "Giriş",
        "btn_register": "Kayıt",
        "btn_logout": "Çıkış",
        "nav_my_profile": "Profilim",
        "auth_login_title": "GlobalTrade Hub'a Giriş",
        "auth_login_subtitle": "Tartışmalara katılmak için giriş yapın",
        "auth_register_title": "GlobalTrade Hub'a Kayıt",
        "auth_register_subtitle": "Ticaret topluluğuna katılın",
        "auth_tab_login": "Giriş",
        "auth_tab_register": "Kayıt",
        "auth_email": "E-posta",
        "auth_password": "Şifre",
        "auth_password_confirm": "Şifreyi Onayla",
        "auth_nickname": "Takma Ad",
        "auth_nickname_ph": "Takma adınız",
        "auth_btn_login": "Giriş Yap",
        "auth_btn_register": "Hesap Oluştur",
        "auth_no_account": "Hesabınız yok mu?",
        "auth_go_register": "Kayıt olun",
        "auth_has_account": "Zaten hesabınız var mı?",
        "auth_go_login": "Giriş yapın",
        "auth_check_email": "Kayıt başarılı! E-postanızı kontrol edin.",
        "community_title": "💬 Küresel Ticaret Topluluğu",
        "community_desc": "Diğer tüccarlarla bağlantı kurun",
        "comment_loading": "Yorumlar yükleniyor...",
        "comment_empty": "Henüz yorum yok. İlk paylaşan siz olun!",
        "comment_placeholder": "Deneyiminizi paylaşın...",
        "comment_submit": "Gönder",
        "comment_login_first": "Giriş yap",
        "comment_login_to_post": "yorum yapmak için",
        "comment_reply": "Yanıtla",
        "comment_delete": "Sil",
        "comment_cancel": "İptal",
        "comment_reply_ph": "Yanıt yaz...",
        "comment_delete_confirm": "Bu yorumu silmek istediğinize emin misiniz?"
    },
    "vi": {
        "nav_community": "Cộng đồng",
        "btn_login": "Đăng nhập",
        "btn_register": "Đăng ký",
        "btn_logout": "Đăng xuất",
        "nav_my_profile": "Hồ sơ",
        "auth_login_title": "Đăng nhập GlobalTrade Hub",
        "auth_login_subtitle": "Đăng nhập để tham gia thảo luận",
        "auth_register_title": "Đăng ký GlobalTrade Hub",
        "auth_register_subtitle": "Tham gia cộng đồng thương mại",
        "auth_tab_login": "Đăng nhập",
        "auth_tab_register": "Đăng ký",
        "auth_email": "Email",
        "auth_password": "Mật khẩu",
        "auth_password_confirm": "Xác nhận mật khẩu",
        "auth_nickname": "Biệt danh",
        "auth_nickname_ph": "Biệt danh của bạn",
        "auth_btn_login": "Đăng nhập",
        "auth_btn_register": "Tạo tài khoản",
        "auth_no_account": "Chưa có tài khoản?",
        "auth_go_register": "Đăng ký ngay",
        "auth_has_account": "Đã có tài khoản?",
        "auth_go_login": "Đăng nhập",
        "auth_check_email": "Đăng ký thành công! Kiểm tra email.",
        "community_title": "💬 Cộng đồng Thương mại",
        "community_desc": "Kết nối với các thương nhân khác",
        "comment_loading": "Đang tải bình luận...",
        "comment_empty": "Chưa có bình luận. Hãy là người đầu tiên!",
        "comment_placeholder": "Chia sẻ kinh nghiệm của bạn...",
        "comment_submit": "Đăng",
        "comment_login_first": "Đăng nhập",
        "comment_login_to_post": "để bình luận",
        "comment_reply": "Trả lời",
        "comment_delete": "Xóa",
        "comment_cancel": "Hủy",
        "comment_reply_ph": "Viết trả lời...",
        "comment_delete_confirm": "Xóa bình luận này?"
    },
    "th": {
        "nav_community": "ชุมชน",
        "btn_login": "เข้าสู่ระบบ",
        "btn_register": "สมัครสมาชิก",
        "btn_logout": "ออกจากระบบ",
        "nav_my_profile": "โปรไฟล์",
        "auth_login_title": "เข้าสู่ระบบ GlobalTrade Hub",
        "auth_login_subtitle": "เข้าสู่ระบบเพื่อร่วมสนทนา",
        "auth_register_title": "สมัครสมาชิก GlobalTrade Hub",
        "auth_register_subtitle": "เข้าร่วมชุมชนการค้า",
        "auth_tab_login": "เข้าสู่ระบบ",
        "auth_tab_register": "สมัครสมาชิก",
        "auth_email": "อีเมล",
        "auth_password": "รหัสผ่าน",
        "auth_password_confirm": "ยืนยันรหัสผ่าน",
        "auth_nickname": "ชื่อเล่น",
        "auth_nickname_ph": "ชื่อเล่นของคุณ",
        "auth_btn_login": "เข้าสู่ระบบ",
        "auth_btn_register": "สร้างบัญชี",
        "auth_no_account": "ยังไม่มีบัญชี?",
        "auth_go_register": "สมัครตอนนี้",
        "auth_has_account": "มีบัญชีแล้ว?",
        "auth_go_login": "เข้าสู่ระบบ",
        "auth_check_email": "สมัครสำเร็จ! ตรวจสอบอีเมลของคุณ",
        "community_title": "💬 ชุมชนการค้าโลก",
        "community_desc": "เชื่อมต่อกับผู้ค้ารายอื่น",
        "comment_loading": "กำลังโหลดความคิดเห็น...",
        "comment_empty": "ยังไม่มีความคิดเห็น เป็นคนแรก!",
        "comment_placeholder": "แบ่งปันประสบการณ์ของคุณ...",
        "comment_submit": "โพสต์",
        "comment_login_first": "เข้าสู่ระบบ",
        "comment_login_to_post": "เพื่อแสดงความคิดเห็น",
        "comment_reply": "ตอบกลับ",
        "comment_delete": "ลบ",
        "comment_cancel": "ยกเลิก",
        "comment_reply_ph": "เขียนตอบกลับ...",
        "comment_delete_confirm": "ลบความคิดเห็นนี้?"
    },
    "id": {
        "nav_community": "Komunitas",
        "btn_login": "Masuk",
        "btn_register": "Daftar",
        "btn_logout": "Keluar",
        "nav_my_profile": "Profil Saya",
        "auth_login_title": "Masuk ke GlobalTrade Hub",
        "auth_login_subtitle": "Masuk untuk berpartisipasi",
        "auth_register_title": "Daftar di GlobalTrade Hub",
        "auth_register_subtitle": "Bergabung dengan komunitas",
        "auth_tab_login": "Masuk",
        "auth_tab_register": "Daftar",
        "auth_email": "Email",
        "auth_password": "Kata Sandi",
        "auth_password_confirm": "Konfirmasi Sandi",
        "auth_nickname": "Nama Panggilan",
        "auth_nickname_ph": "Nama panggilan Anda",
        "auth_btn_login": "Masuk",
        "auth_btn_register": "Buat Akun",
        "auth_no_account": "Belum punya akun?",
        "auth_go_register": "Daftar sekarang",
        "auth_has_account": "Sudah punya akun?",
        "auth_go_login": "Masuk",
        "auth_check_email": "Pendaftaran berhasil! Periksa email Anda.",
        "community_title": "💬 Komunitas Perdagangan",
        "community_desc": "Terhubung dengan pedagang lain",
        "comment_loading": "Memuat komentar...",
        "comment_empty": "Belum ada komentar. Jadilah yang pertama!",
        "comment_placeholder": "Bagikan pengalaman Anda...",
        "comment_submit": "Kirim",
        "comment_login_first": "Masuk",
        "comment_login_to_post": "untuk berkomentar",
        "comment_reply": "Balas",
        "comment_delete": "Hapus",
        "comment_cancel": "Batal",
        "comment_reply_ph": "Tulis balasan...",
        "comment_delete_confirm": "Hapus komentar ini?"
    },
    "ms": {
        "nav_community": "Komuniti",
        "btn_login": "Log Masuk",
        "btn_register": "Daftar",
        "btn_logout": "Log Keluar",
        "nav_my_profile": "Profil Saya",
        "auth_login_title": "Log Masuk ke GlobalTrade Hub",
        "auth_login_subtitle": "Log masuk untuk menyertai perbincangan",
        "auth_register_title": "Daftar di GlobalTrade Hub",
        "auth_register_subtitle": "Sertai komuniti perdagangan",
        "auth_tab_login": "Log Masuk",
        "auth_tab_register": "Daftar",
        "auth_email": "E-mel",
        "auth_password": "Kata Laluan",
        "auth_password_confirm": "Sahkan Kata Laluan",
        "auth_nickname": "Nama Samaran",
        "auth_nickname_ph": "Nama samaran anda",
        "auth_btn_login": "Log Masuk",
        "auth_btn_register": "Cipta Akaun",
        "auth_no_account": "Tiada akaun?",
        "auth_go_register": "Daftar sekarang",
        "auth_has_account": "Sudah ada akaun?",
        "auth_go_login": "Log masuk",
        "auth_check_email": "Pendaftaran berjaya! Semak e-mel anda.",
        "community_title": "💬 Komuniti Perdagangan",
        "community_desc": "Berhubung dengan peniaga lain",
        "comment_loading": "Memuat komen...",
        "comment_empty": "Tiada komen. Jadi yang pertama!",
        "comment_placeholder": "Kongsi pengalaman anda...",
        "comment_submit": "Hantar",
        "comment_login_first": "Log masuk",
        "comment_login_to_post": "untuk mengulas",
        "comment_reply": "Balas",
        "comment_delete": "Padam",
        "comment_cancel": "Batal",
        "comment_reply_ph": "Tulis balasan...",
        "comment_delete_confirm": "Padam komen ini?"
    },
    "ko": {
        "nav_community": "커뮤니티",
        "btn_login": "로그인",
        "btn_register": "회원가입",
        "btn_logout": "로그아웃",
        "nav_my_profile": "내 프로필",
        "auth_login_title": "GlobalTrade Hub 로그인",
        "auth_login_subtitle": "토론에 참여하려면 로그인하세요",
        "auth_register_title": "GlobalTrade Hub 회원가입",
        "auth_register_subtitle": "무역 커뮤니티에 참여하세요",
        "auth_tab_login": "로그인",
        "auth_tab_register": "회원가입",
        "auth_email": "이메일",
        "auth_password": "비밀번호",
        "auth_password_confirm": "비밀번호 확인",
        "auth_nickname": "닉네임",
        "auth_nickname_ph": "닉네임",
        "auth_btn_login": "로그인",
        "auth_btn_register": "계정 만들기",
        "auth_no_account": "계정이 없으신가요?",
        "auth_go_register": "지금 가입",
        "auth_has_account": "이미 계정이 있으신가요?",
        "auth_go_login": "로그인",
        "auth_check_email": "가입 완료! 이메일을 확인하세요.",
        "community_title": "💬 글로벌 무역 커뮤니티",
        "community_desc": "다른 무역업자와 소통하세요",
        "comment_loading": "댓글 로딩 중...",
        "comment_empty": "아직 댓글이 없습니다. 첫 댓글을 남겨보세요!",
        "comment_placeholder": "경험을 공유하세요...",
        "comment_submit": "등록",
        "comment_login_first": "로그인",
        "comment_login_to_post": "하여 댓글 작성",
        "comment_reply": "답글",
        "comment_delete": "삭제",
        "comment_cancel": "취소",
        "comment_reply_ph": "답글 작성...",
        "comment_delete_confirm": "이 댓글을 삭제하시겠습니까?"
    },
    "ja": {
        "nav_community": "コミュニティ",
        "btn_login": "ログイン",
        "btn_register": "登録",
        "btn_logout": "ログアウト",
        "nav_my_profile": "マイプロフィール",
        "auth_login_title": "GlobalTrade Hub ログイン",
        "auth_login_subtitle": "ディスカッションに参加するにはログイン",
        "auth_register_title": "GlobalTrade Hub 登録",
        "auth_register_subtitle": "貿易コミュニティに参加",
        "auth_tab_login": "ログイン",
        "auth_tab_register": "登録",
        "auth_email": "メール",
        "auth_password": "パスワード",
        "auth_password_confirm": "パスワード確認",
        "auth_nickname": "ニックネーム",
        "auth_nickname_ph": "ニックネーム",
        "auth_btn_login": "ログイン",
        "auth_btn_register": "アカウント作成",
        "auth_no_account": "アカウントをお持ちでないですか？",
        "auth_go_register": "今すぐ登録",
        "auth_has_account": "すでにアカウントをお持ちですか？",
        "auth_go_login": "ログイン",
        "auth_check_email": "登録完了！メールを確認してください。",
        "community_title": "💬 グローバル貿易コミュニティ",
        "community_desc": "他のトレーダーとつながる",
        "comment_loading": "コメント読み込み中...",
        "comment_empty": "まだコメントはありません。最初に投稿しましょう！",
        "comment_placeholder": "経験を共有...",
        "comment_submit": "投稿",
        "comment_login_first": "ログイン",
        "comment_login_to_post": "してコメント",
        "comment_reply": "返信",
        "comment_delete": "削除",
        "comment_cancel": "キャンセル",
        "comment_reply_ph": "返信を書く...",
        "comment_delete_confirm": "このコメントを削除しますか？"
    },
    "pl": {
        "nav_community": "Społeczność",
        "btn_login": "Zaloguj",
        "btn_register": "Rejestracja",
        "btn_logout": "Wyloguj",
        "nav_my_profile": "Mój Profil",
        "auth_login_title": "Zaloguj się do GlobalTrade Hub",
        "auth_login_subtitle": "Zaloguj się, aby dołączyć do dyskusji",
        "auth_register_title": "Zarejestruj się w GlobalTrade Hub",
        "auth_register_subtitle": "Dołącz do społeczności handlowej",
        "auth_tab_login": "Logowanie",
        "auth_tab_register": "Rejestracja",
        "auth_email": "E-mail",
        "auth_password": "Hasło",
        "auth_password_confirm": "Potwierdź hasło",
        "auth_nickname": "Pseudonim",
        "auth_nickname_ph": "Twój pseudonim",
        "auth_btn_login": "Zaloguj się",
        "auth_btn_register": "Utwórz konto",
        "auth_no_account": "Nie masz konta?",
        "auth_go_register": "Zarejestruj się",
        "auth_has_account": "Masz już konto?",
        "auth_go_login": "Zaloguj się",
        "auth_check_email": "Rejestracja udana! Sprawdź e-mail.",
        "community_title": "💬 Społeczność Handlowa",
        "community_desc": "Połącz się z innymi handlowcami",
        "comment_loading": "Ładowanie komentarzy...",
        "comment_empty": "Brak komentarzy. Bądź pierwszy!",
        "comment_placeholder": "Podziel się doświadczeniem...",
        "comment_submit": "Opublikuj",
        "comment_login_first": "Zaloguj się",
        "comment_login_to_post": "aby skomentować",
        "comment_reply": "Odpowiedz",
        "comment_delete": "Usuń",
        "comment_cancel": "Anuluj",
        "comment_reply_ph": "Napisz odpowiedź...",
        "comment_delete_confirm": "Usunąć ten komentarz?"
    },
    "nl": {
        "nav_community": "Community",
        "btn_login": "Inloggen",
        "btn_register": "Registreren",
        "btn_logout": "Uitloggen",
        "nav_my_profile": "Mijn Profiel",
        "auth_login_title": "Inloggen bij GlobalTrade Hub",
        "auth_login_subtitle": "Log in om deel te nemen",
        "auth_register_title": "Registreren bij GlobalTrade Hub",
        "auth_register_subtitle": "Word lid van de community",
        "auth_tab_login": "Inloggen",
        "auth_tab_register": "Registreren",
        "auth_email": "E-mail",
        "auth_password": "Wachtwoord",
        "auth_password_confirm": "Bevestig wachtwoord",
        "auth_nickname": "Bijnaam",
        "auth_nickname_ph": "Jouw bijnaam",
        "auth_btn_login": "Inloggen",
        "auth_btn_register": "Account aanmaken",
        "auth_no_account": "Nog geen account?",
        "auth_go_register": "Registreer nu",
        "auth_has_account": "Al een account?",
        "auth_go_login": "Inloggen",
        "auth_check_email": "Registratie gelukt! Controleer je e-mail.",
        "community_title": "💬 Handelscommunity",
        "community_desc": "Verbind met andere handelaren",
        "comment_loading": "Reacties laden...",
        "comment_empty": "Nog geen reacties. Wees de eerste!",
        "comment_placeholder": "Deel je ervaring...",
        "comment_submit": "Plaatsen",
        "comment_login_first": "Inloggen",
        "comment_login_to_post": "om te reageren",
        "comment_reply": "Reageren",
        "comment_delete": "Verwijderen",
        "comment_cancel": "Annuleren",
        "comment_reply_ph": "Schrijf een reactie...",
        "comment_delete_confirm": "Deze reactie verwijderen?"
    }
}


def process_file(filepath, filename):
    """Process a single HTML file: inject auth modal, update navbar, replace community section."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changed = False

    # --- Check if already processed ---
    if 'auth-overlay' in content and 'id="comment-list"' in content:
        # Already has auth + community, skip
        return False

    # 1. Inject CSS (before </style> or after existing community CSS)
    if '/* Auth Modal */' not in content:
        # Find </style>
        style_end = content.find('</style>')
        if style_end > 0:
            content = content[:style_end] + '\n' + AUTH_COMMUNITY_CSS + '\n' + content[style_end:]
            changed = True

    # 2. Add nav_community link to nav-links
    if 'data-i18n="nav_community"' not in content:
        # Find nav-links div and add community link after the last nav item (before </div>)
        # The nav-links section ends with </div> after the last <a> tag
        # Simpler approach: directly replace the partners link + closing div + nav-actions
        nav_links_pattern = r'(<a href="#partners"[^>]*>.*?</a>)(\s*</div>\s*<div class="nav-actions">)'
        m = re.search(nav_links_pattern, content)
        if m:
            # Build replacement: community link + closing div + nav-actions with auth buttons
            replacement = m.group(1) + NAV_COMMUNITY_LINK + m.group(2) + '\n' + NAV_AUTH_BUTTONS
            content = content[:m.start()] + replacement + content[m.end():]
            changed = True
        else:
            # Fallback: try simpler approach using string replacement on entire content
            if '<div class="nav-actions">' in content:
                # Insert community link before </div> of nav-links
                content = content.replace(
                    '<a href="#partners" data-i18n="nav_partners">联盟工具</a>',
                    '<a href="#partners" data-i18n="nav_partners">联盟工具</a>\n  <a href="#community" data-i18n="nav_community">用户交流</a>',
                    1
                )
                # Insert auth buttons in nav-actions
                content = content.replace(
                    '<div class="nav-actions">',
                    '<div class="nav-actions">\n' + NAV_AUTH_BUTTONS,
                    1
                )
                if 'nav_community' in content:
                    changed = True
                else:
                    print(f'  WARN: {filename}: fallback nav insert also failed')
            else:
                print(f'  WARN: {filename}: could not find nav-links pattern')

    # 3. Inject auth modal HTML (before <footer>)
    # Use id="auth-overlay" to check for the actual HTML element, not just CSS reference
    if 'id="auth-overlay"' not in content and 'class="auth-overlay"' not in content:
        footer_pos = content.find('<footer>')
        if footer_pos > 0:
            content = content[:footer_pos] + '\n' + AUTH_MODAL_HTML + '\n' + content[footer_pos:]
            changed = True
        else:
            # Try before </body>
            body_end = content.find('</body>')
            if body_end > 0:
                content = content[:body_end] + '\n' + AUTH_MODAL_HTML + '\n' + content[body_end:]
                changed = True

    # 4. Replace Giscus community section with Supabase community
    # Check for actual HTML element, not just CSS class
    if 'id="comment-list"' not in content and 'id="comment-form-wrap"' not in content:
        # Find and replace the community section
        # Pattern: <!-- ===== Community Discussion Section ===== --> ... </section>
        comm_pattern = r'<!-- ===== Community Discussion Section ===== -->.*?</section>'
        m_comm = re.search(comm_pattern, content, re.DOTALL)
        if m_comm:
            content = content[:m_comm.start()] + COMMUNITY_HTML + content[m_comm.end():]
            changed = True
        else:
            # Try version without exactly this comment
            comm_pattern2 = r'<section class="community-section".*?</section>'
            m_comm2 = re.search(comm_pattern2, content, re.DOTALL)
            if m_comm2 and 'id="community"' in m_comm2.group():
                content = content[:m_comm2.start()] + COMMUNITY_HTML + content[m_comm2.end():]
                changed = True

    # 5. Replace loadGiscus JS with auth+comment JS
    if 'initSupabase' not in content:
        # Remove old Giscus JS block
        giscus_js_pattern = r'// ===== Giscus \(Community Comments\) =====.*?^\}'
        giscus_js_pattern2 = r'function loadGiscus\(\)\{.*?^\}'
        content = re.sub(giscus_js_pattern, '', content, flags=re.DOTALL|re.MULTILINE)
        content = re.sub(giscus_js_pattern2, '', content, flags=re.DOTALL|re.MULTILINE)

        # Remove loadGiscus() call
        content = content.replace('loadGiscus();\n', '')

        # Inject new JS before applyLang function (or before </script>)
        js_code = AUTH_COMMUNITY_JS_TEMPLATE.format(
            supabase_url=SUPABASE_URL,
            supabase_anon_key=SUPABASE_ANON_KEY
        )
        # Find a good insertion point - after the last closing } of existing JS, before applyLang
        apply_lang_pos = content.find('function applyLang(lang){')
        if apply_lang_pos > 0:
            content = content[:apply_lang_pos] + '\n' + js_code + '\n\n' + content[apply_lang_pos:]
        else:
            # Fallback: before </script>
            script_end = content.rfind('</script>')
            if script_end > 0:
                content = content[:script_end] + '\n' + js_code + '\n' + content[script_end:]
        changed = True

    # 6. Add i18n keys for auth/community
    # Find the last language block in I18N and merge additions
    for lang_code, translations in I18N_ADDITIONS.items():
        if lang_code in content:
            # Find the last key in this language block and append after it
            # Pattern: find the lang block, find the last key-value pair
            lang_pattern = rf'{lang_code}:\{{'
            lang_start = content.find(lang_pattern)
            if lang_start < 0:
                continue
            # Find closing } of this language block
            # Simple approach: find next language block start or end of I18N
            next_lang = None
            for other_lang in sorted(I18N_ADDITIONS.keys()):
                if other_lang != lang_code:
                    pos = content.find(other_lang + ':{', lang_start + len(lang_pattern))
                    if pos > lang_start and (next_lang is None or pos < next_lang):
                        next_lang = pos
            if next_lang is None:
                # Last language block, find the closing }; of I18N
                block_end = content.find('};', lang_start)
                if block_end < 0:
                    block_end = content.find('}', lang_start + 100)
            else:
                block_end = next_lang - 2  # before newline+next lang

            if block_end < 0:
                continue

            # Check if already has these keys
            if 'nav_community' in content[lang_start:block_end]:
                continue

            # Build insertion string
            insert_lines = []
            for key, val in translations.items():
                escaped_val = val.replace("'", "\\'")
                insert_lines.append(f'{key}:"{escaped_val}",')

            insert_str = '\n' + '\n'.join(insert_lines) + '\n'
            content = content[:block_end] + insert_str + content[block_end:]
            changed = True

    if not changed:
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True


def main():
    html_files = [f for f in os.listdir(WORKSPACE) if f.endswith('.html')]
    html_files.sort()

    print(f'Found {len(html_files)} HTML files')
    print('=' * 50)

    if SUPABASE_URL == 'SUPABASE_URL_PLACEHOLDER':
        print('[WARN] SUPABASE_URL and SUPABASE_ANON_KEY are still placeholders!')
        print('  Please create a Supabase project first, then update this script.')
        print('=' * 50)

    success = 0
    for fname in html_files:
        fpath = os.path.join(WORKSPACE, fname)
        try:
            changed = process_file(fpath, fname)
            if changed:
                print(f'  OK: {fname}')
                success += 1
            else:
                print(f'  SKIP: {fname} (already processed or no changes needed)')
        except Exception as e:
            print(f'  ERROR: {fname}: {e}')

    print('=' * 50)
    print(f'Done: {success}/{len(html_files)} files updated')

    if SUPABASE_URL == 'SUPABASE_URL_PLACEHOLDER':
        print()
        print('Next steps:')
        print('  1. Go to https://supabase.com and create a project')
        print('  2. Run the SQL from the guidance to create tables')
        print('  3. Get SUPABASE_URL and SUPABASE_ANON_KEY from Project Settings > API')
        print('  4. Update them at the top of this script')
        print('  5. Re-run: python add_auth_community.py')


if __name__ == '__main__':
    main()
