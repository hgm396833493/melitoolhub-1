# MeliToolHub 一键更新指南

## 📌 快速流程（发布新文章只需 3 步）

```
第1步：复制模板创建文章 → 第2步：提交到Git → 第3步：推送到GitHub
```

---

## 一、发布新文章

### 1. 复制模板
```bash
cp article-template.html article-新文章名.html
```

### 2. 编辑文章内容
打开 `article-新文章名.html`，修改以下内容：

| 位置 | 修改内容 |
|------|----------|
| `<title>` | 文章标题 - MeliToolHub拉美跨境电商平台（50-60字符） |
| `<meta description>` | 文章描述（120-155字符） |
| `<meta keywords>` | 3-5个精准关键词 |
| `<link rel="canonical">` | 改为新文章的URL |
| JSON-LD `headline` | 文章标题 |
| JSON-LD `description` | 文章描述 |
| JSON-LD `datePublished` | 发布日期 YYYY-MM-DD |
| `<h1>` | 文章标题 |
| `<span>📅` | 发布日期 |
| `<span>⏱️` | 预计阅读时间 |
| `.article-tags` | 文章标签 |
| `<article>` 正文 | 文章内容（800-2000中文字） |

### 3. SEO规范要求
- ✅ H1唯一且只有一个
- ✅ H标签层级：H1 → H2 → H3（不能跳级）
- ✅ 每段不超过4-5行
- ✅ 原创内容，不复制粘贴
- ✅ 图片加 alt 属性和 loading="lazy"
- ✅ 关键词自然分布，不堆砌
- ✅ 文章末尾有明确的行动建议

### 4. 在首页添加文章链接
编辑 `index.html`，找到文章列表区域（搜索 `<!-- ===== 已发布`），在最新文章后面添加：

```html
<div class="article-list-item">
  <div class="art-num">11</div>
  <div class="art-info">
    <a href="article-新文章名.html" class="art-title-link">文章标题</a>
    <span class="art-excerpt">文章简介，30-50字</span>
  </div>
  <div class="art-badge-cell">
    <span class="badge badge-zh">ZH</span>
  </div>
  <div class="art-date">2025-06-03</div>
</div>
```

---

## 二、添加/更新推荐链接（联盟营销）

### 修改推荐链接
1. 编辑 `index.html`
2. 搜索 `data-pid="xxx"` 找到对应工具卡片
3. 修改 `<a href="...">` 为你的专属推荐链接
4. 修改佣金描述 `partner-commission`

### 添加新推荐工具
复制一个 `partner-card` 的 HTML 结构，修改：
- `data-pid`：唯一标识
- `.partner-logo`：图标emoji
- `.partner-name`：工具名称（4个语言都要改）
- `.partner-desc`：描述（4个语言都要改）
- `.partner-tags`：分类标签
- `.partner-commission`：佣金/奖励说明
- `<a href="...">`：你的专属推荐链接
- `rel="noopener noreferrer sponsored"`：标注为赞助链接（SEO要求）

### i18n多语言
在每个语言的翻译对象中添加对应的key：
- `p13_name`, `p13_desc`, `p13_comm`, `p13_btn`（以此类推）

---

## 三、Git 一键更新推送

### 基本命令
```bash
cd D:\workspace

# 查看修改了哪些文件
git status

# 添加所有修改
git add -A

# 提交（写清楚改了什么）
git commit -m "新增文章：xxx - 描述"

# 推送到GitHub
git push origin main
```

### 批量更新多条命令
```bash
cd D:\workspace && git add -A && git commit -m "更新内容" && git push origin main
```

### GitHub Pages 自动更新
推送后约1-3分钟，网站自动更新。访问：
- https://hgm396833493.github.io/melitoolhub/

---

## 四、Google Search Console 设置

### 1. 验证网站
1. 打开 https://search.google.com/search-console
2. 添加资源 → 输入 `https://hgm396833493.github.io/melitoolhub/`
3. 选择 "HTML标签" 验证方式
4. 复制验证码（格式：`xxxxxxx`）
5. 编辑 `index.html`，找到 `google-site-verification` meta标签
6. 将 `YOUR_VERIFICATION_CODE` 替换为你的验证码
7. 保存并推送到GitHub
8. 点击验证

### 2. 提交Sitemap
验证成功后：
1. 进入 Search Console → 站点地图
2. 输入 `sitemap.xml`
3. 点击提交

### 3. 请求索引（新文章）
每次发布新文章后：
1. Search Console → URL检查
2. 输入文章URL
3. 点击 "请求编入索引"

---

## 五、联盟推广链接获取方式

| 平台 | 联盟计划 | 注册地址 |
|------|----------|----------|
| Mercado Libre | Programa de Afiliados | https://www.mercadolibre.com/afiliados |
| 万里汇 WorldFirst | 推荐计划 | 注册后在后台获取专属链接 |
| PingPong | 推荐计划 | 注册后在后台获取专属链接 |
| 空中云汇 Airwallex | 推荐计划 | https://www.airwallex.com/referral |
| 紫鸟浏览器 | 推荐计划 | https://www.ziniao.com 注册后获取 |
| 智赢ERP | 推荐计划 | 注册后联系客服获取 |
| 妙手ERP | 推荐计划 | https://www.miaoshou.com 注册后获取 |
| 店小秘ERP | 推荐计划 | https://www.dianxiaomi.com 注册后获取 |
| Helium 10 | Affiliate Program | https://h10.me/affiliate |

> ⚠️ 以上链接为官方网站，获取你的专属推荐链接后替换 index.html 中的 href 即可。

---

## 六、自定义域名绑定（可选）

如果购买了 `melitoolhub.com` 域名：

### 1. 创建CNAME文件
```bash
echo "melitoolhub.com" > CNAME
git add CNAME && git commit -m "Add CNAME" && git push origin main
```

### 2. GitHub Pages设置
1. 仓库 Settings → Pages
2. Custom domain 填入 `melitoolhub.com`
3. 勾选 Enforce HTTPS

### 3. 域名DNS配置
在域名商后台添加：
| 类型 | 名称 | 值 |
|------|------|-----|
| CNAME | www | hgm396833493.github.io |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
