# 跨境谷歌SEO建站合规需求方案 — 逐项完成度核查

> 对照文档：`跨境谷歌SEO建站变现合规需求方案_定稿.docx`  
> 核查日期：2026-06-05  
> 核查范围：静态HTML站（D:\workspace\*.html）+ Next.js工程（D:\workspace\melitoolhub-ts\）

---

## 一、项目整体定位 ✅

| 需求项 | 状态 | 说明 |
|--------|:----:|------|
| 谷歌SEO全合规架构 | ✅ | 双项目均实现 |
| AdSense变现 | ⚠️ | 架构就绪，Publisher ID为占位符 |
| 跨境官方联盟佣金 | ⚠️ | 架构就绪，联盟ID为占位符 |
| 陕西西安地域定位 | ✅ | 多处标注 |
| 18语种 | ✅ | Next.js完整18语种；静态站核心页18语种 |

---

## 二、全站违规点整改

### 2.1 收款展示合规 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| 无私人收款码/私户账号 | ✅ | 全站无二维码、无私人账号展示 |
| 合作结算页仅展示正规支付服务商 | ❌ | **cooperation.html 中文内容严重乱码，中文用户无法阅读** |
| 万里汇等官方链接 | ⚠️ | 存在但中文乱码导致不可读 |

### 2.2 汇率功能结构合规 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| 拉美区域汇率（BRL/MXN/COP+CNY/USD） | ✅ | tools.html + Next.js ExchangeCalculator(variant=latam) |
| 俄罗斯卢布（RUB+CNY/USD） | ✅ | tools.html + Next.js ExchangeCalculator(variant=russia) |

### 2.3 内容扩容架构 ⚠️
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 首页标题聚合列表 | ⚠️ | Next.js有文章列表页；静态站index.html无文章聚合 |
| 独立详情页 | ✅ | Next.js articles/[slug] + 静态站news1/news2.html |
| 无大面积空白/薄内容 | ⚠️ | policy-template.html为模板占位 |

### 2.4 广告联盟链接合规分区 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 广告位与主体内容分区 | ✅ | Next.js AdSlot组件独立封装 |
| 无堆砌遮挡 | ✅ | 联盟链接含 rel="sponsored" |

---

## 三、全站核心合规功能

### 3.1 站点部署 & 更新合规 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| 静态页面部署 | ✅ | Next.js output:'export' + 原始HTML |
| 标准化URL目录（/articles/ /policy/ /tools/） | ✅ | Next.js App Router实现 |
| robots.txt | ✅ | 自动生成 + 手动维护 |
| sitemap.xml | ✅ | 自动生成18语种 |
| 地域标注西安 | ✅ | 已标注 |

### 3.2 18语言合规布局 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| 18语种（zh/en/es/pt/ru/fr/de/it/ar/tr/vi/th/id/ms/ko/ja/pl/nl） | ✅ | Next.js 18 JSON + 静态站18语种i18n |
| 单标签下拉切换 | ✅ | 静态站有语言切换组件 |
| 独立URL/独立收录 | ✅ | /zh/ /en/ /es/ 等目录 |
| hreflang标签 | ✅ | 核心页面19个hreflang (含x-default) |
| Cookie缓存语种偏好 | ✅ | Next.js CookieBanner + 静态站localStorage |

**⚠️ 静态站hreflang缺失页面：**
- ❌ news1.html — 无hreflang
- ❌ news2.html — 无hreflang

### 3.3 Core Web Vitals 适配 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| PC+移动端自适应 | ✅ | 两项目均响应式 |
| 无CLS扣分 | ✅ | 布局稳定 |
| 图片压缩+ALT属性 | ⚠️ | 已规范，但og-image.jpg等资产文件缺失 |

### 3.4 全站搜索功能 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 右上角全局搜索 | ✅ | Next.js站内检索 |
| 与语种切换并列 | ✅ | 布局已实现 |

### 3.5 右下角咨询弹窗 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| 静态悬浮按钮 | ✅ | Next.js ConsultModal组件 |
| 用户主动点击唤起 | ✅ | 无自动弹窗 |
| 一键关闭 | ✅ | 已实现 |
| 采购咨询信息 | ✅ | 表单含需求类型字段 |

**⚠️ 静态站覆盖不全：** sourcing/tools/cooperation/news 页面无咨询弹窗

---

## 四、变现体系

### 4.1 核心盈利：中国商品采购代办 ✅
| 要求 | 状态 | 证据 |
|------|:----:|------|
| sourcing.html 完整内容 | ✅ | 全品类货源/比价验货/报关物流/来华采购 |
| 6步服务流程 | ✅ | sourcing.html完整流程 |
| 无私下交易/私人收款 | ✅ | 明确合规声明 |
| SEO关键词 China product sourcing | ✅ | TDK已优化 |

### 4.2 联盟佣金 ⚠️
| 平台 | 状态 | 说明 |
|------|:----:|------|
| 美客多联盟 | ⚠️ | 占位符 `NEXT_PUBLIC_MELI_AFFILIATE_ID` |
| Amazon Associates | ⚠️ | 占位符 `NEXT_PUBLIC_AMAZON_AFFILIATE_ID` |
| Shopee联盟 | ⚠️ | 占位符 `NEXT_PUBLIC_SHOPEE_AFFILIATE_ID` |
| OZON联盟 | ⚠️ | 占位符 `NEXT_PUBLIC_OZON_AFFILIATE_ID` |
| 万里汇/紫鸟/智赢ERP/妙手ERP | ⚠️ | 链接存在但需确认是否为专属推广链接 |

### 4.3 AdSense 合规 ⚠️
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 广告位组件化 | ✅ | Next.js AdSlot组件 |
| 18语种分区域配置 | ✅ | 架构就绪 |
| Publisher ID | ❌ | **占位符，AdSense未激活** |
| 无诱导点击 | ✅ | 布局合规 |

---

## 五、五大核心内容栏目

### 栏目一：跨境干货文章 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 首页聚合标题列表 | ✅ | Next.js articles/page.tsx |
| 2篇核心西语原创 | ✅ | **已有3篇**：meli-es / latam-logistics-es / mercado-libre-es |
| 全语种译文 | ✅ | MDX文章含多语言元数据 |
| 批量更新模板 | ✅ | article-template.html + MDX模板 |

### 栏目二：政策资讯合规指南 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 墨西哥海关政策 | ✅ | article-mexico-customs.html |
| 巴西合规指南 | ✅ | news2.html (INMETRO/ANVISA) |
| 内容标注发布时间 | ✅ | 文章有date字段 |

### 栏目三：跨境实用工具 ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 双币种汇率换算 | ✅ | 拉美+俄罗斯双模块 |
| 支付费率计算器 | ✅ | 4平台费率对比 |
| 阿里巴巴采购科普 | ✅ | tools.html含采购专区入口 |

### 栏目四：合作结算+全球采购 ❌
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 合作模式科普 | ❌ | **cooperation.html中文完全乱码，用户无法阅读** |
| 服务商费率说明 | ❌ | 同上 |
| 无私收信息 | ✅ | 合规声明存在但乱码 |
| 咨询留资入口 | ⚠️ | 静态站部分页面缺失 |

### 栏目五：隐私政策 + Cookie ✅
| 要求 | 状态 | 说明 |
|------|:----:|------|
| 18语种隐私政策 | ✅ | privacy.html完整10章+附录 |
| GDPR/CCPA/俄罗斯/拉美法规 | ✅ | 已覆盖 |
| 底部固定政策入口 | ✅ | Footer统一入口 |
| Cookie授权弹窗 | ⚠️ | **仅3/20页面有Cookie弹窗**（index/privacy/1个article） |
| 同意/拒绝/查看隐私 | ✅ | 实现完整 |

---

## 六、SEO & 收录标准

| # | SEO要求 | 整体状态 | 详情 |
|---|----------|:----:|------|
| 1 | TDK标准化 | ⚠️ | 核心页OK；sourcing/tools/privacy/cooperation缺twitter:card |
| 2 | H标签层级 | ✅ | 单页唯一H1，H2/H3分层 |
| 3 | URL静态短链接 | ✅ | 无动态参数 |
| 4 | 图片ALT属性 | ⚠️ | 未全面排查，og-image.jpg缺失 |
| 5 | Schema结构化数据 | ✅ | index/sourcing/tools/privacy均有JSON-LD |
| 6 | robots + sitemap自动生成 | ✅ | scripts/generate-sitemap.mjs + generate-robots.mjs |
| 7 | 时间标注 + 过期清理 | ✅ | 文章标注日期 |

### 静态站SEO标签缺失明细

| 页面 | twitter:card | og:image | og:locale | hreflang |
|------|:---:|:---:|:---:|:---:|
| index.html | ✅ | ✅ | ✅ | ✅ |
| cooperation.html | ❌ | ❌ | ❌ | ✅ |
| sourcing.html | ❌ | ❌ | ❌ | ✅ |
| privacy.html | ❌ | ❌ | ❌ | ✅ |
| tools.html | ❌ | ❌ | ❌ | ✅ |
| 404.html | ✅ | ✅ | ❌ | ✅ |
| news1.html | ❌ | ✅ | ❌ | ❌ |
| news2.html | ❌ | ✅ | ❌ | ❌ |

---

## 七、品牌名统一问题 ⚠️

| 位置 | 显示名称 | 状态 |
|------|----------|:----:|
| Next.js Navbar | GlobalTradeHub | ✅ |
| Next.js Footer | GlobalTrade Hub | ✅ |
| Next.js meta.site_name (18语种JSON) | **MeliToolHub** | ❌ |
| 静态 index.html Logo | GlobalTrade Hub | ✅ |
| 静态 sourcing.html/tools.html/404.html | GlobalTrade Hub | ✅ |
| 静态 cooperation.html/privacy.html | **MeliToolHub** | ❌ |
| 静态 news1.html/news2.html | **MeliToolHub** | ❌ |

**需要统一为 GlobalTrade Hub / GlobalTradeHub**

---

## 八、联系方式不统一 ⚠️

| 位置 | 微信 | 邮箱 | QQ邮箱 |
|------|:---:|------|:---:|
| 文档要求 | hgm123002 | — | 396833493@qq.com |
| 404.html | ✅ hgm123002 | — | ✅ 396833493@qq.com |
| index.html | ✅ hgm123002 | hgm123002@outlook.com | ❌ 缺 |
| cooperation.html | ❌ 无 | hgm123002@outlook.com | ❌ 缺 |
| sourcing.html | ❌ 无 | hgm123002@outlook.com | ❌ 缺 |
| privacy.html | ❌ 无 | hgm123002@outlook.com | ❌ 缺 |
| tools.html | ❌ 无 | ❌ 无 | ❌ 缺 |
| news1/news2 | ❌ 无 | hgm123002@outlook.com | ❌ 缺 |

---

## 九、GSC验证码状态 ❌

| 位置 | 状态 |
|------|:----:|
| Next.js .env.local.example | 占位符 `NEXT_PUBLIC_GSC_VERIFICATION=YOUR_VERIFICATION_CODE` |
| 静态 index.html | 占位符 `YOUR_VERIFICATION_CODE` |
| 其他7个静态页面 | 完全缺失 |

---

## 十、资产文件状态

| 文件 | 状态 | 规格 |
|------|:----:|------|
| og-image.jpg | ❌ **不存在** | 1200×630px |
| favicon.ico | ❌ **不存在** | 32×32px (标签已写但文件缺失) |
| apple-touch-icon.png | ❌ **不存在** | 180×180px |
| ads.txt | ⚠️ 格式不完整 | 仅 `google.com` 一行，缺 publisher ID |

---

## 十一、最终交付清单对照

| # | 文档要求 | 状态 |
|---|----------|:----:|
| 1 | 双合规首页（自适应/多语言/搜索/合规广告） | ✅ |
| 2 | robots.txt + sitemap.xml | ✅ |
| 3 | 2篇核心西语原创 + 全语种译文 | ✅ (有3篇) |
| 4 | 文章/政策/工具/采购模板 | ✅ |
| 5 | 汇率计算器 + 支付费率计算器 | ✅ |
| 6 | 联盟产品展示 | ⚠️ 占位符ID |
| 7 | 采购代办落地页 | ✅ |
| 8 | 咨询弹窗组件 | ✅ Next.js / ⚠️ 静态站覆盖不全 |
| 9 | 合作结算页 + 隐私政策 + Cookie弹窗 | ❌ cooperation乱码 / ⚠️ Cookie覆盖不全 |
| 10 | 内容时效体系 | ✅ |
| 11 | 网站底部联系方式 | ⚠️ 不统一 |
| 12 | TS完整工程源码 | ✅ |
| 13 | CF部署配置清单 | ✅ |
| 14 | sitemap/robots自动打包脚本 | ✅ |
| 15 | 上线验收+运维文档 | ✅ UPDATE_GUIDE.md |

---

## 总结

### ✅ 已完成（20项）
双合规首页、18语种i18n、Navbar 6项导航、Footer 4列布局、Hero跨境视觉、汇率/支付计算器、MDX西语文章(3篇)、全部页面路由、build脚本、CF配置、环境变量模板、sourcing.html采购页、privacy.html隐私政策(18语种)、JSON-LD Schema、hreflang标签(核心页)、咨询弹窗(Next.js)、广告组件、部署文档

### ❌/⚠️ 未完成（需要修复）

| 优先级 | 问题 | 影响 |
|:---:|------|------|
| **P0** | **cooperation.html 中文严重乱码** | 用户无法阅读中文合作页 |
| **P0** | **品牌名不统一**（GlobalTrade Hub vs MeliToolHub） | 搜索引擎认知混乱 |
| **P1** | **联系方式不统一**（微信/QQ邮箱部分页面缺失） | 商务转化受损 |
| **P1** | **5个静态页面缺 twitter:card + og:image + og:locale** | SEO社交分享效果差 |
| **P1** | **GSC验证码为占位符** | Google无法验证站点 |
| **P1** | **AdSense Publisher ID为占位符** | 广告无法展示 |
| **P1** | **联盟推广ID为占位符** | 佣金无法追踪 |
| **P1** | **3个关键资产文件缺失**（og-image.jpg/favicon.ico/apple-touch-icon.png） | 影响品牌形象和SEO |
| **P1** | **Cookie弹窗仅覆盖3/20页面** | 合规风险（GDPR） |
| **P2** | news1/news2无hreflang | 多语种SEO不完整 |
| **P2** | 咨询弹窗静态站覆盖不全 | 转化触点不足 |
| **P2** | 静态站index.html无文章聚合 | 体验不够完善 |

---

**下一步建议：**
1. **立即修复**：cooperation.html重建 + 品牌名统一（AI可代劳）
2. **用户准备**：3个图片资产 + GSC验证码 + AdSense ID + 联盟ID
3. **批量修复**：SEO标签补齐 + Cookie/咨询弹窗全面覆盖
