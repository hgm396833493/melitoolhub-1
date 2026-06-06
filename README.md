# 🌐 GlobalTradeHub

> 一站式跨境电商服务平台 — 专注拉美 & 全球跨境贸易工具与资讯

[![Live Site](https://img.shields.io/badge/Live-melitoolhub.com-success?style=flat-square)](https://melitoolhub.com)
[![GitHub repo](https://img.shields.io/badge/GitHub-melitoolhub-blue?style=flat-square&logo=github)](https://github.com/hgm396833493/melitoolhub.com)
[![18 Languages](https://img.shields.io/badge/i18n-18%20Languages-blueviolet?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-222?style=flat-square&logo=github)](https://pages.github.com)
[![CDN by Cloudflare](https://img.shields.io/badge/CDN-Cloudflare-f38020?style=flat-square&logo=cloudflare)](https://cloudflare.com)

**在线访问**：https://melitoolhub.com

---

## 📖 项目简介

**GlobalTradeHub** 是一个面向全球跨境电商卖家的一站式服务平台，提供汇率换算、支付费率对比、跨境采购入口、市场准入指南等实用功能。

- 🌍 **18 种语言**：中文、English、Español、Português、Русский、Français、Deutsch、Italiano、العربية、Türkçe、Tiếng Việt、ไทย、Bahasa Indonesia、Bahasa Melayu、한국어、日本語、Polski、Nederlands
- 🔧 **实用工具**：拉美汇率换算、俄罗斯卢布换算、跨境支付费率计算器、阿里巴巴采购入口
- 📰 **11 篇深度文章**：美客多开店、拉美物流、巴西市场准入、墨西哥海关、跨境支付对比等
- 💬 **用户交流区**：注册用户可发表/回复/删除评论
- 🚀 **联盟工具导航**：紫鸟浏览器、小火箭加速器、美客多、Amazon、Shopee 等推荐链接

---

## ✨ 核心功能

### 🔐 用户系统（Supabase Auth）
- 邮箱注册 / 登录（含邮箱验证）
- 昵称自动生成（基于邮箱前缀）
- 登录状态持久化（localStorage）

### 💬 全球贸易商交流区
- 访客可查看所有评论
- 注册用户可发表 / 回复 / 删除自己的评论
- 实时加载，Toast 操作反馈

### 🔧 实用工具

| 工具 | 功能 |
|------|------|
| 💰 **汇率换算器** | 拉美多国货币 + 俄罗斯卢布 ↔ 人民币实时换算 |
| 💳 **支付费率对比** | PayPal / 万里汇 / PingPong / 连连支付 / 空中云汇费率比较 |
| 🛒 **阿里巴巴采购入口** | 一键跳转 1688 / 阿里国际站 |
| 🚀 **联盟工具导航** | 紫鸟浏览器、小火箭加速器等联盟推荐链接 |

### 📰 文章中心（11篇）

| 分类 | 文章 |
|------|------|
| **平台运营** | 美客多开店教程、美客多广告攻略、Mercado Libre 攻略 |
| **市场准入** | 巴西市场准入指南（含 INMETRO/ANVISA/ANATEL 认证） |
| **物流** | 拉美物流对比、海外仓选择指南 |
| **海关法规** | 墨西哥海关新规解读 |
| **选品与包装** | 拉美选品策略、拉美包装标签规范 |
| **支付** | 跨境支付手续费深度对比 |
| **社交电商** | TikTok 拉美电商入门指南 |

### 🤝 采购代办服务
样品采购 / 大货采购 / 质检验厂 / 国际物流一站式服务

---

## 🗂️ 项目结构

```
melitoolhub/
├── index.html                         # 首页（含欢迎词 + 社区评论）
├── tools.html                         # 实用工具专区
├── sourcing.html                      # 采购代办服务
├── cooperation.html                   # 合作与结算说明
├── privacy.html                       # 隐私政策
├── 404.html                          # 404 错误页面
├── news1.html                        # 政策资讯 ①
├── news2.html                        # 政策资讯 ②
├── article-brazil-market.html         # 巴西市场准入指南（葡萄牙语）
├── article-latam-logistics-es.html    # 拉美物流对比（西班牙语）
├── article-latam-packaging.html       # 拉美包装规范（葡萄牙语）
├── article-latam-products.html        # 拉美选品策略（西班牙语）
├── article-meli-ads.html             # 美客多广告攻略（西班牙语）
├── article-meli-es.html              # 美客多开店教程（西班牙语）
├── article-mercado-libre-es.html      # Mercado Libre 攻略（西班牙语）
├── article-mexico-customs.html       # 墨西哥海关（西班牙语）
├── article-overseas-warehouse.html    # 海外仓指南（英语）
├── article-payment-comparison.html    # 支付对比（中文）
├── article-tiktok-latam.html         # TikTok 拉美电商（西班牙语）
├── sitemap.xml                       # 站点地图（19页 + hreflang）
├── robots.txt                        # 爬虫规则
├── favicon.ico                       # 网站图标
├── og-image.jpg                      # 社交分享图（1200×630px）
├── apple-touch-icon.png              # iOS 主屏图标（180×180px）
├── CNAME                             # 自定义域名配置
├── README.md                         # 本文件
└── baidu_verify_codeva-*.html        # 百度站长验证文件（×3）
```

> **技术栈**：纯静态 HTML + CSS + JavaScript，无需 Node.js 构建，直接部署即运行。

---

## 🚀 部署方式

### 当前部署架构

```
用户访问 melitoolhub.com
    ↓
Cloudflare CDN（SSL + 全球加速）
    ↓
GitHub Pages（静态文件托管）
    ↓
melitoolhub.com/index.html
```

### 一键部署

1. Fork 本仓库到你的 GitHub
2. 进入 **Settings → Pages**
3. Source 选择 `main` 分支，`/ (root)`
4. Custom domain 填写你的域名
5. 将域名的 CNAME 记录指向 `yourname.github.io`
6. 可选：接入 Cloudflare 开启 CDN + HTTPS

---

## 📊 搜索引擎优化（SEO）

### 已完成优化

| 优化项 | 覆盖范围 |
|--------|---------|
| ✅ `sitemap.xml` | 19 页，含 `lastmod` / `changefreq` / `priority` / `hreflang` |
| ✅ `robots.txt` | 规范爬虫规则，指向 sitemap |
| ✅ `canonical` 标签 | 全部 21 页 |
| ✅ Open Graph 标签 | og:title / description / image / url / site_name（21页） |
| ✅ Twitter Card | twitter:card / title / description / image（21页） |
| ✅ Schema.org JSON-LD | Article / WebPage / Service 结构化数据（21页） |
| ✅ hreflang 多语言 | 18 种语言 × 各页面（含 x-default） |
| ✅ favicon + apple-touch-icon | 全部 21 页 |
| ✅ og:image | 1200×630px 社交分享图 |
| ✅ 百度 HTML 标签验证 | 全部 21 页 |
| ✅ Bing HTML 标签验证 | 全部 21 页 |

### 搜索引擎收录状态

| 平台 | 状态 | 说明 |
|------|------|------|
| **Bing** | ✅ 已验证 + Sitemap 已提交 | 覆盖 Bing / Yahoo / DuckDuckGo |
| **百度** | ⏳ 验证部署完成 | HTML 标签已添加到全部页面 |
| **Google** | ⏳ 待配置 | 需翻墙 + Google 账号 |

---

## 🔧 环境变量

在全部 21 个 HTML 文件中，`<head>` 内已配置以下标签：

```html
<!-- Supabase -->
<script>
SUPABASE_URL = 'https://woiwjttrtokwgrhhzobm.supabase.co';
SUPABASE_ANON_KEY = 'eyJhbGciOi...';   // anon key
</script>

<!-- 搜索引擎验证 -->
<meta name="baidu-site-verification" content="codeva-ummFdmrg3t" />
<meta name="msvalidate.01" content="BC817C05CD908E47ED9A80EAE5276BBF" />
<meta name="google-site-verification" content="YOUR_VERIFICATION_CODE" />
```

---

## 💾 Supabase 数据库配置

### 数据表结构

```sql
-- 评论表（已配置 RLS）
comments (
  id         BIGSERIAL PRIMARY KEY,
  user_id    UUID REFERENCES auth.users(id),
  content    TEXT NOT NULL,
  parent_id  BIGINT REFERENCES comments(id),  -- NULL=主评论，非NULL=回复
  page_path  TEXT DEFAULT '/',                  -- 所属页面
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 资料表（已配置 RLS + 触发器）
profiles (
  id          UUID REFERENCES auth.users(id) PRIMARY KEY,
  username    TEXT UNIQUE,
  avatar_url  TEXT,
  created_at  TIMESTAMPTZ DEFAULT NOW()
);
```

### RLS 策略

| 表 | 操作 | 策略 |
|----|------|------|
| comments | SELECT | 任何人可读取 |
| comments | INSERT | 仅登录用户可发表（auth.uid() = user_id） |
| comments | UPDATE | 仅用户可更新自己的评论 |
| comments | DELETE | 仅用户可删除自己的评论 |
| profiles | SELECT | 任何人可查看 |
| profiles | UPDATE | 仅用户可更新自己的资料 |

---

## 🌐 外站推广资源

以下平台可用于推广 GlobalTradeHub：

| 渠道 | 操作 | 效果 |
|------|------|------|
| **知乎** | 回答拉美跨境/美客多相关问题，文末附链接 | 百度收录快，SEO 权重高 |
| **小红书** | 发布跨境干货笔记 | 精准外贸用户流量 |
| **抖音/B站** | 制作跨境工具推荐短视频 | 爆发式流量 |
| **福步外贸论坛** | 签名档放链接 | 外贸行业精准流量 |
| **5118/果汁导航** | 提交工具导航站收录 | 工具类 SEO 权重 |
| **GitHub** | 本仓库（Google 高权重） | 搜索引擎优先收录 |

---

## 🛠️ 本地开发

```bash
# 启动本地服务器
cd melitoolhub
python -m http.server 3000
# 或
npx serve . -p 3000

# 访问 http://localhost:3000
```

> 💡 评论和注册功能需要 Supabase 后端支持，本地开发时依然可正常使用（Supabase API 是公开的）。

---

## 📞 联系方式

| 渠道 | 信息 |
|------|------|
| 📧 QQ 邮箱 | 396833493@qq.com |
| 📧 Outlook | hgm123002@outlook.com |
| 💬 微信 | hgm123002 |
| 🐙 GitHub | [@hgm396833493](https://github.com/hgm396833493) |

---

## 📄 开源协议

MIT License — 详见 [LICENSE](LICENSE) 文件。

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star！**

[![Star this repo](https://img.shields.io/github/stars/hgm396833493/melitoolhub.com?style=social)](https://github.com/hgm396833493/melitoolhub.com)

</div>
