# 🌐 GlobalTradeHub

> 一站式跨境电商服务平台 — 专注拉美 & 俄罗斯跨境贸易工具与资讯

[![Deploy to Cloudflare Pages](https://img.shields.io/badge/Deploy%20to-Cloudflare%20Pages-orange?logo=cloudflare)](https://pages.cloudflare.com)
[![GitHub repo](https://img.shields.io/badge/GitHub-hgm396833493%2Fmelitoolhub-blue?logo=github)](https://github.com/hgm396833493/melitoolhub)
[![Languages](https://img.shields.io/badge/18%20Languages-🌍-green)]()
[![Live Site](https://img.shields.io/badge/Live-melitoolhub.com-success)](https://melitoolhub.com)

---

## 📋 目录

- [项目简介](#项目简介)
- [✨ 功能特性](#-功能特性)
- [🗂️ 项目结构](#️-项目结构)
- [🚀 快速部署](#-快速部署)
- [🔧 环境变量](#-环境变量)
- [📊 Supabase 配置](#-supabase-配置)
- [🔍 SEO 优化](#-seo-优化)
- [🛠️ 本地开发](#️-本地开发)
- [📞 联系方式](#-联系方式)
- [📄 开源协议](#-开源协议)

---

## 项目简介

**GlobalTradeHub** 是一个面向跨境电商卖家的一站式服务平台，专注**拉美市场**（巴西、墨西哥、哥伦比亚等）和**俄罗斯市场**的跨境贸易工具与资讯。

- 🌍 **18种语言**支持，覆盖全球主要跨境电商市场
- 🔧 **实用工具**：汇率换算、支付费率对比、采购入口
- 📰 **干货文章**：平台运营、物流、海关、包装等实战指南
- 💬 **用户交流区**：注册用户可留言交流
- 🤝 **采购代办服务**：一站式跨境采购解决方案

**在线访问**：https://melitoolhub.com

---

## ✨ 功能特性

### 🔐 用户系统（Supabase Auth）
- 邮箱注册 / 登录
- 用户资料管理
- 登录状态持久化

### 💬 全球贸易商交流区
- 所有访客可**查看**评论
- 注册用户可**发表 / 删除**自己的评论
- 实时加载，自动刷新

### 🔧 实用工具
| 工具 | 说明 |
|------|------|
| 💰 汇率换算 | 拉美货币 / 俄罗斯卢布 ↔ 人民币 |
| 💳 支付费率对比 | PayPal / 万里汇 / PingPong / 连连支付 |
| 🛒 阿里巴巴采购入口 | 一键跳转 1688 / 阿里国际站 |
| 📦 联盟工具 | Mercado Libre / Amazon / Shopee 联盟链接 |

### 📰 11篇干货文章
- 美客多（Mercado Libre）开店全攻略
- 拉美物流方式对比与选择
- 巴西市场准入指南
- 墨西哥海关新规解读
- 跨境支付费率全面对比
- ... 更多持续更新

### 🤝 采购代办服务
- 样品采购 / 大货采购 / 质检 / 验厂 / 国际物流

---

## 🗂️ 项目结构

```
melitoolhub/
├── index.html                      # 首页
├── tools.html                      # 实用工具
├── sourcing.html                   # 采购代办
├── cooperation.html                # 合作与结算
├── privacy.html                    # 隐私政策
├── 404.html                       # 404 错误页
├── news1.html / news2.html        # 政策资讯
│
├── article-*.html                  # 11篇干货文章
│
├── sitemap.xml                    # 站点地图（19页）
├── robots.txt                     # 爬虫规则
│
├── favicon.ico                   # 网站图标
├── og-image.jpg                   # 社交分享图（1200×630px）
├── apple-touch-icon.png           # iOS 主屏图标
│
└── README.md                     # 本文件
```

> **注意**：本项目为**纯静态 HTML/CSS/JS**，无需 Node.js / 构建步骤，直接部署即可运行。

---

## 🚀 快速部署

### 方式一：Cloudflare Pages（推荐）

1. 登录 [Cloudflare Pages](https://pages.cloudflare.com)
2. 点击 **"Create a project"** → 连接 GitHub 仓库 `hgm396833493/melitoolhub`
3. 构建设置：
   - **Build command**：留空（无需构建）
   - **Build output directory**：`/`（根目录）
   - **Root directory**：留空
4. 点击 **"Save and Deploy"**
5. 前往 **Custom domains** 绑定 `melitoolhub.com`

### 方式二：GitHub Pages

1. 进入仓库 **Settings → Pages**
2. **Source** 选择 `main` 分支，`/ (root)`
3. 点击 **Save**
4. 访问 `https://hgm396833493.github.io/melitoolhub/`

### 方式三：任意静态托管

只需将 `D:\workspace\` 下所有文件上传至任意支持静态文件的 Web 服务器即可。

---

## 🔧 环境变量

在 `index.html`（及所有 `.html` 文件）的 `<script>` 标签中，需要配置以下变量：

```html
<script>
const SUPABASE_URL = 'https://woiwjttrtokwgrhhzobm.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp...'; // 你的 anon key
const GSC_VERIFICATION = 'YOUR_GOOGLE_VERIFICATION_CODE';        // Google Search Console 验证码
</script>
```

| 变量 | 说明 | 获取方式 |
|------|------|----------|
| `SUPABASE_URL` | Supabase 项目 URL | [Supabase Dashboard](https://supabase.com/dashboard) → Settings → API |
| `SUPABASE_ANON_KEY` | Supabase 公开 anon key | 同上 |
| `GSC_VERIFICATION` | Google Search Console 验证码 | [GSC](https://search.google.com/search-console) → 资源设置 → HTML 标签 |

---

## 📊 Supabase 配置

### 1. 创建 Supabase 项目

1. 注册 [Supabase](https://supabase.com) 账号
2. 新建项目，记录 `URL` 和 `anon key`
3. 替换所有 HTML 文件中的 `SUPABASE_URL` 和 `SUPABASE_ANON_KEY`

### 2. 执行建表 SQL

在 Supabase **SQL Editor** 中执行以下 SQL：

```sql
-- 用户资料表
CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID REFERENCES auth.users(id) PRIMARY KEY,
  username TEXT UNIQUE,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 评论表
CREATE TABLE IF NOT EXISTS public.comments (
  id BIGSERIAL PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id),
  content TEXT NOT NULL,
  parent_id BIGINT REFERENCES public.comments(id) NULL,
  page_path TEXT DEFAULT '/',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 启用行级安全
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.comments ENABLE ROW LEVEL SECURITY;

-- 评论：所有人可查看
CREATE POLICY "评论可公开读取" ON public.comments FOR SELECT USING (true);

-- 评论：登录用户可插入
CREATE POLICY "登录用户可评论" ON public.comments FOR INSERT WITH CHECK (auth.uid() = user_id);

-- 评论：用户可删除自己的评论
CREATE POLICY "用户可删除自己的评论" ON public.comments FOR DELETE USING (auth.uid() = user_id);

-- 资料：所有人可查看
CREATE POLICY "用户可查看所有资料" ON public.profiles FOR SELECT USING (true);

-- 资料：用户可更新自己的资料
CREATE POLICY "用户只能更新自己的资料" ON public.profiles FOR UPDATE USING (auth.uid() = id);

-- 新用户注册时自动创建资料
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, username, avatar_url)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'username', split_part(NEW.email, '@', 1)),
    NEW.raw_user_meta_data->>'avatar_url'
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

### 3. 配置邮件模板（可选）

在 Supabase Dashboard → **Authentication → Email Templates** 中自定义邮件内容。

---

## 🔍 SEO 优化

本项目已全面优化 Google SEO：

| 优化项 | 状态 |
|--------|------|
| ✅ `sitemap.xml`（19页，含 `lastmod` / `changefreq` / `priority`) | 已完成 |
| ✅ `robots.txt`（规范爬虫规则） | 已完成 |
| ✅ `canonical` 标签（防重复内容） | 已完成 |
| ✅ Open Graph（og:title / description / image / url） | 已完成 |
| ✅ Twitter Card（twitter:card / title / description / image） | 已完成 |
| ✅ `hreflang`（18种语言，首页） | 已完成 |
| ✅ Schema.org 结构化数据（JSON-LD） | 已完成 |
| ✅ 语义化 HTML（H1 / H2 / alt 属性） | 已完成 |
| ✅ 移动端适配（viewport meta + 响应式 CSS） | 已完成 |
| ⚠️ `og-image.jpg`（1200×630px） | 待制作 |
| ⚠️ Google Search Console 验证码 | 待替换 |

### 提交 Sitemap 到 Google

1. 登录 [Google Search Console](https://search.google.com/search-console)
2. 添加资源：`https://melitoolhub.com`
3. 左侧菜单 → **"站点地图"**
4. 输入：`sitemap.xml` → 点击 **"提交"**

---

## 🛠️ 本地开发

### 方式一：直接打开（最简单）

双击 `index.html` 用浏览器打开即可（部分功能需联网）。

### 方式二：本地 HTTP 服务器（推荐）

```bash
# Python
cd D:\workspace
python -m http.server 3000

# 或 Node.js
npx serve . -p 3000
```

然后访问：**http://localhost:3000**

### 修改内容

- **导航栏菜单**：编辑每个 `.html` 文件中的 `<div class="nav-links">`
- **文章**：修改 `article-*.html` 中的内容
- **工具**：修改 `tools.html`
- **评论**：通过 Supabase Dashboard 管理 `comments` 表

---

## 📞 联系方式

- 📧 **邮箱**：396833493@qq.com
- 💬 **微信**：hgm123002
- 📧 **Outlook**：hgm123002@outlook.com
- 🐙 **GitHub**：[@hgm396833493](https://github.com/hgm396833493)

---

## 📄 开源协议

本项目仅供学习与交流使用。  
商业使用请提前联系作者。

---

## 🙏 致谢

- [Supabase](https://supabase.com) — 开源后端即服务
- [Cloudflare Pages](https://pages.cloudflare.com) — 免费静态托管
- [Mercado Libre](https://www.mercadolibre.com) — 拉美最大电商平台
- 所有为跨境电商提供价值的平台与工具

---

<div align="center">

**⭐ 如果这个项目对你有帮助，欢迎 Star！**

[![Star this repo](https://img.shields.io/github/stars/hgm396833493/melitoolhub?style=social)](https://github.com/hgm396833493/melitoolhub)

</div>
