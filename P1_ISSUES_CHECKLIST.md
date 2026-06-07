# GlobalTradeHub / MeliToolHub — P1 问题清单

> 生成日期：2026-06-05 | 审计范围：D:\workspace\ (静态HTML) + D:\workspace\melitoolhub-ts\ (Next.js)
> 总计：**12 个 P1 问题**，按操作类型分为三大类。

---

## 一、用户必须手动操作（需从第三方平台获取凭证） 🔴

### P1-01 — Google Search Console 验证码

| 属性 | 详情 |
|------|------|
| **影响范围** | 静态HTML (1文件) + Next.js (全站) |
| **严重程度** | 严重 — GSC 无法验证，收录受阻 |

**操作步骤：**

1. 登录 [Google Search Console](https://search.google.com/search-console)
2. 添加资源 → URL 前缀 → 输入 `https://melitoolhub.com`
3. 选择"HTML 标签"验证方式
4. 复制 `<meta name="google-site-verification" content="xxx">` 中的 `content` 值

**需要修改的位置（共2处）：**

| # | 文件 | 行 | 当前值 |
|---|------|----|--------|
| 1 | `D:\workspace\index.html` | 12 | `content="YOUR_VERIFICATION_CODE"` |
| 2 | `.env.local` → `NEXT_PUBLIC_GSC_VERIFICATION` | — | `(空)` → 同时在 Cloudflare Pages 环境变量中设置 |

---

### P1-02 — Google AdSense 激活

| 属性 | 详情 |
|------|------|
| **影响范围** | 静态HTML (14文件) + Next.js (全站广告位) |
| **严重程度** | 严重 — 广告无法展示，变现功能瘫痪 |

**操作步骤：**

1. 前往 [Google AdSense](https://adsense.google.com) 申请账户
2. 获取 Publisher ID（格式：`ca-pub-XXXXXXXXXXXXXXXX`）
3. 在 AdSense 后台创建广告单元，获取各 slot ID

**需要修改的位置（3处）：**

| # | 文件 | 修改内容 |
|---|------|----------|
| 1 | `.env.local` → `NEXT_PUBLIC_ADSENSE_ID` | 填入 `ca-pub-XXXXXXXXXXXXXXXX` |
| 2 | `D:\workspace\melitoolhub-ts\public\ads.txt` | 改为 `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0` |
| 3 | 静态HTML 14个文件 | 将占位符广告位替换为真实 AdSense 代码 |

**受影响的静态HTML文件（14个）：**
- `index.html`（4处广告位占位符）
- `tools.html`
- `sourcing.html`
- `cooperation.html`
- `article-meli-es.html`
- `article-meli-ads.html`
- `article-latam-logistics-es.html`
- `article-brazil-market.html`
- `article-mexico-customs.html`
- `article-payment-comparison.html`
- `article-overseas-warehouse.html`
- `article-tiktok-latam.html`
- `article-latam-packaging.html`
- `article-latam-products.html`
- `article-mercado-libre-es.html`

**Next.js 假 slot ID（2处）：**

| 文件 | 行 | 当前假值 |
|------|----|----------|
| `src/components/HomeContent.tsx` | 138 | `slot="1234567890"` |
| `src/components/HomeContent.tsx` | 154 | `slot="0987654321"` |

---

### P1-03 — 联盟推广 ID 配置

| 属性 | 详情 |
|------|------|
| **影响范围** | Next.js |
| **严重程度** | 高 — 联盟链接无追踪ID，跨境分佣失效 |

**操作步骤：** 分别在以下平台注册联盟计划，获取专属推广 ID：

| 变量名 | 平台 | 注册地址 |
|--------|------|----------|
| `NEXT_PUBLIC_MELI_AFFILIATE_ID` | Mercado Libre 联盟 | [afiliados.mercadolibre.com](https://afiliados.mercadolibre.com) |
| `NEXT_PUBLIC_AMAZON_AFFILIATE_ID` | Amazon Associates | [affiliate-program.amazon.com](https://affiliate-program.amazon.com) |
| `NEXT_PUBLIC_SHOPEE_AFFILIATE_ID` | Shopee 联盟 | [affiliate.shopee.com](https://affiliate.shopee.com) |
| `NEXT_PUBLIC_OZON_AFFILIATE_ID` | Ozon 联盟 | [seller.ozon.ru/affiliate](https://seller.ozon.ru) |

**修改位置：** `.env.local` 中对应4个变量，同时配置到 Cloudflare Pages 环境变量。

---

### P1-04 — 自定义域名绑定 Cloudflare Pages

| 属性 | 详情 |
|------|------|
| **严重程度** | 高 — 网站无法以 melitoolhub.com 正式上线 |

**操作步骤：**

1. 在域名注册商（如 GoDaddy/Namecheap/阿里云）将 `melitoolhub.com` 的 DNS 服务器指向 Cloudflare
2. 在 Cloudflare DNS 中添加 CNAME 记录指向 Cloudflare Pages
3. Cloudflare Pages → Custom domains → 添加 `melitoolhub.com`

---

## 二、用户手动准备资产文件 📁

### P1-05 — og-image.jpg（社交分享封面图）

| 属性 | 详情 |
|------|------|
| **规格** | 1200×630px，JPG，< 300KB |
| **影响范围** | 静态HTML (20文件引用) + Next.js (全站) |
| **严重程度** | 高 — 微信/Facebook/Twitter 分享无预览图 |

**制作要求：**
- 尺寸：1200×630px
- 内容：GlobalTradeHub 品牌标识 + "跨境贸易一站式服务平台" 文案 + 飞机/货船/包裹视觉元素
- 放置位置：
  - `D:\workspace\og-image.jpg`（静态站引用）
  - `D:\workspace\melitoolhub-ts\public\og-image.jpg`（Next.js 引用）

---

### P1-06 — favicon.ico（浏览器标签页图标）

| 属性 | 详情 |
|------|------|
| **规格** | 32×32px 或 16×16px，ICO 格式 |
| **影响范围** | 全部页面 |

**放置位置：**
- `D:\workspace\favicon.ico`
- `D:\workspace\melitoolhub-ts\public\favicon.ico`

---

### P1-07 — apple-touch-icon.png（iOS 主屏幕书签图标）

| 属性 | 详情 |
|------|------|
| **规格** | 180×180px，PNG 格式 |
| **影响范围** | 全部页面（iOS 保存到主屏幕时使用） |

**放置位置：**
- `D:\workspace\apple-touch-icon.png`
- `D:\workspace\melitoolhub-ts\public\apple-touch-icon.png`

---

## 三、AI 可代劳的代码修复（用户确认后执行） 🟡

以下问题不涉及外部凭证，可由 AI 直接修改代码完成：

### P1-08 — Next.js OpenGraph 缺少 image 字段

| 文件 | 行 | 修复内容 |
|------|----|----------|
| `src/app/[locale]/layout.tsx` | ~43 | 在 `openGraph` 中添加 `images: [{ url: '/og-image.jpg', width: 1200, height: 630 }]` |

> ⚠️ 需 P1-05（og-image.jpg）先就位后才能生效。

---

### P1-09 — HomeContent.tsx 假 AdSlot ID 替换

| 文件 | 行 | 当前 | 应改为 |
|------|----|------|--------|
| `src/components/HomeContent.tsx` | 138 | `slot="1234567890"` | 真实 AdSense 广告单元 ID |
| `src/components/HomeContent.tsx` | 154 | `slot="0987654321"` | 真实 AdSense 广告单元 ID |

> ⚠️ 需 P1-02（AdSense 激活）先完成，获取真实 slot ID。

---

### P1-10 — 静态站缺失 sitemap 条目补充

当前 `D:\workspace\sitemap.xml` 缺少以下页面：
- `404.html`
- `article-mercado-libre-es.html`

> 可随时执行，不影响线上功能。

---

### P1-11 — GitHub 推送 & Cloudflare Pages 首次部署

**当前状态：** npm build ✅（310页），代码在本地未推送

**操作：**
1. `git add . && git commit -m "GlobalTradeHub rebrand + SEO fixes" && git push`
2. Cloudflare Pages 连接 GitHub 仓库自动构建
3. 确认部署成功

---

### P1-12 — 静态站 AdSense 占位符批量替换（14个文件）

> ⚠️ 需 P1-02（AdSense 激活）先完成，再将占位符 `<div>` 替换为真实 AdSense `<ins>` 代码。

---

## 汇总执行顺序

```
第一步（域名+凭证） ─────────────────
  P1-04  绑定 melitoolhub.com 到 Cloudflare
  P1-01  获取 GSC 验证码
  P1-02  申请 AdSense → 获取 Publisher ID
  P1-03  注册4个联盟平台 → 获取推广ID

第二步（资产制作）─────────────────
  P1-05  制作 og-image.jpg (1200×630)
  P1-06  制作 favicon.ico
  P1-07  制作 apple-touch-icon.png

第三步（AI代码修复）────────────────
  P1-08  OpenGraph image 字段
  P1-10  sitemap 补充缺失条目
  P1-11  Git 推送 + CF Pages 部署

第四步（AdSense 激活后）────────────
  P1-09  HomeContent 真实 slot ID
  P1-12  静态站14个文件批量替换

第五步（部署后验证）───────────────
  浏览器访问验证
  GSC 提交验证
  AdSense 广告投放验证
  社交分享预览检查
```

---

> 📎 附：本清单对应的详细审计数据由 `seo_audit.py` 生成。所有 P1 问题的根本原因、影响文件、修复方案均可溯源至该审计报告。
