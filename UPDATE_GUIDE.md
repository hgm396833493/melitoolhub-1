# GlobalTrade Hub 更新指南

## 项目信息
- 仓库: https://github.com/hgm396833493/melitoolhub
- 域名: melitoolhub.com
- 技术栈: 单文件HTML + CSS + JS，无框架
- 语言: 18语种（zh/en/es/pt/ru/fr/de/it/ar/tr/vi/th/id/ms/ko/ja/pl/nl）
- 响应式: 4断点（1024/768/680/480px）
- 变现: Google AdSense + 多平台官方联盟佣金 + 中国采购代办服务

## 文件结构
```
├── index.html                    # 主首页（18语种、5大栏目）
├── privacy.html                  # 隐私政策（18语种+GDPR合规）
├── cooperation.html              # 合作与结算说明（18语种）
├── tools.html                    # 跨境工具专区（汇率+费率计算器）
├── sourcing.html                 # 中国采购代办服务页
├── article-meli-es.html          # 美客多开店教程（西语+17语种）
├── article-latam-logistics-es.html # 拉美物流对比（西语+17语种）
├── article-brazil-market.html    # 巴西市场准入指南
├── article-mexico-customs.html   # 墨西哥海关指南
├── article-payment-comparison.html # 跨境支付费率对比
├── article-template.html         # 通用文章模板（18语种）
├── policy-template.html          # 政策资讯模板（18语种）
├── news1.html                    # 政策资讯1
├── news2.html                    # 政策资讯2
├── robots.txt                    # 搜索引擎爬虫规则
├── sitemap.xml                   # 站点地图
└── UPDATE_GUIDE.md               # 本文件
```

---

## 一、语言系统说明

### i18n架构
每个页面使用内嵌的 `I18N` JavaScript对象存储18种语言翻译，通过 `data-i18n` 属性绑定DOM元素。

### 语言代码对照
| 代码 | 语言 | 代码 | 语言 |
|------|------|------|------|
| zh | 中文 | tr | 土耳其语 |
| en | 英文 | vi | 越南语 |
| es | 西班牙语 | th | 泰语 |
| pt | 葡萄牙语 | id | 印尼语 |
| ru | 俄语 | ms | 马来语 |
| fr | 法语 | ko | 韩语 |
| de | 德语 | ja | 日语 |
| it | 意大利语 | pl | 波兰语 |
| ar | 阿拉伯语 | nl | 荷兰语 |

---

## 二、发布新文章（复制模板三步法）

### 第1步：复制模板
```bash
cp article-template.html article-新文章名.html
```

### 第2步：修改内容
在 `article-新文章名.html` 中搜索 `<!-- TODO`，逐一替换：

| 占位符 | 替换内容 | 示例 |
|--------|----------|------|
| `<!-- TODO: 替换标题 -->` | 文章标题（50-60字符） | 墨西哥NOM认证完整指南 |
| `<!-- TODO: 替换描述 -->` | 文章描述（120-155字） | 详解墨西哥NOM认证... |
| `<!-- TODO: 替换关键词 -->` | 3-5个精准关键词 | 墨西哥,NOM认证,清关 |
| `<!-- TODO: 替换canonical -->` | 新文章URL | ...article-mexico-nom.html |
| `<!-- TODO: 日期 -->` | YYYY-MM-DD | 2026-06-15 |
| `<!-- TODO: 阅读时间 -->` | X分钟 | 8分钟 |

### 第3步：填写i18n内容
在 `I18N` 对象中填写18语种的译文。**至少填写 zh/en/es/pt/ru/fr/de/it/ar 9种核心语言**，其余语言会自动fallback到英文。

### 第4步：在首页添加文章链接
编辑 `index.html`，在 `articles` 数组末尾添加：
```javascript
{n:序号, url:'article-新文章名.html', lang:'zh', 
 title:{zh:'中文标题', en:'English Title', es:'Título en Español', /*...其他语言*/},
 excerpt:{zh:'中文摘要30-50字', en:'English excerpt', /*...其他语言*/},
 date:'2026-06-15'}
```

---

## 三、发布新政策资讯

### 使用 policy-template.html
```bash
cp policy-template.html news3.html
```
然后按模板内的 `<!-- TODO -->` 注释修改内容，填写18语种译文。

---

## 四、AdSense 配置

### 1. 申请Google AdSense
访问 https://adsense.google.com 注册，获取发布商ID（格式：`ca-pub-XXXXXXXXXX`）

### 2. 替换广告代码
在所有HTML文件中搜索 `<div class="ad-ph">`，替换为：
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX" crossorigin="anonymous"></script>
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXXX" data-ad-slot="YYYYYYYYYY" data-ad-format="auto" data-full-width-responsive="true"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script>
```

---

## 五、Google Search Console 配置

### 1. 验证网站
1. 打开 https://search.google.com/search-console
2. 添加资源 → 输入 `https://hgm396833493.github.io/melitoolhub/`
3. 选择"HTML标签"验证方式
4. 复制验证码，替换 `index.html` 中的 `YOUR_VERIFICATION_CODE`
5. 推送并验证

### 2. 提交Sitemap
验证成功后 → 站点地图 → 输入 `sitemap.xml` → 提交

### 3. 请求索引
每次发布新文章后在GSC中：URL检查 → 输入文章URL → 请求编入索引

---

## 六、Git 更新推送

```bash
cd D:\workspace
git add -A
git commit -m "更新内容描述"
git push origin main
```

推送后1-3分钟自动部署到 GitHub Pages。

---

## 七、联盟推广链接

| 平台 | 联盟计划 | 获取方式 |
|------|----------|----------|
| Mercado Libre | Programa de Afiliados | mercadolibre.com/afiliados |
| Amazon | Amazon Associates | affiliate-program.amazon.com |
| Shopee | AMS联盟 | shopee.com 注册后获取 |
| OZON | 官方联盟 | ozon.ru 注册后获取 |
| 万里汇 WorldFirst | 推荐计划 | 后台获取专属链接 |
| PingPong | 推荐计划 | 注册后后台获取 |
| Airwallex | 推荐计划 | airwallex.com/referral |
| 紫鸟浏览器 | 推荐计划 | ziniao.com 注册后获取 |
| 智赢ERP | 推荐计划 | https://www.zying.net/ |
| 妙手ERP | 推荐计划 | https://erp.91miaoshou.com/ |

> 获取专属推荐链接后，在 index.html 的 `partners` 数组中替换 `url` 字段。

---

## 八、合规注意事项

1. **严禁**在页面展示个人收款码、私人账号、线下转账方式
2. **严禁**自动弹窗骚扰用户（Cookie弹窗仅首次访问展示一次）
3. **严禁**堆砌广告链接，广告位与主体内容物理分区
4. **必须**保持全站原创内容，不可搬运、抄袭
5. **必须**每个新页面在sitemap.xml中注册
6. AdSense申请前确保隐私政策页完整、Cookie弹窗就绪
