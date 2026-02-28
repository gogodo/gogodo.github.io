# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 工作语言

**除非必要，请默认使用中文作为工作语言。** 包括但不限于：

- 与用户的对话交流
- 代码注释和文档说明
- 错误信息和提示

仅在以下情况使用英文：

- 代码本身的技术要求（如变量名、函数名、API 调用）
- 技术术语的原文引用
- 用户明确要求使用英文

## 项目概述

这是君的个人博客项目，使用 Docsify 构建静态博客网站，部署在 GitHub Pages 上。

### 项目目标
- 发布个人成长蜕变、技术方案
- 打造君的个人品牌 IP
- 提供简洁优雅的阅读体验

### IP 核心定位
**"把AI从Demo变成生产系统的架构师"**

- 19年企业级软件经验（中石油、中海油、海信、TCL等头部企业）
- AI落地实践专家
- 差异化主张："他们讲AI技术，我讲AI如何在年产值X亿的企业系统中真正应用起来"

### 内容策略
**三位一体IP闭环**：
1. **文章**（轻量深度，1000-2000字，引流）
2. **视频**（深度塑造人设，混合形式：录屏+出镜）
3. **MVP产品**（展示AI在企业系统中的集成效果）

### 核心内容方向
- **Claude Code企业级实践** - AI辅助开发在真实项目中的应用
- **AI+工业软件** - 展示AI在PLM/工业互联网中的实际应用
- **成长蜕变** - 19年技术人的成长路径、转型决策与复盘思考

## 技术栈

- **Docsify** - 无需编译的文档网站生成器，实时解析 Markdown
- **Markdown** - 所有内容以 Markdown 格式编写
- **GitHub Pages** - 静态网站托管

## 项目结构

```
├── index.html          # Docsify 入口文件，包含配置和脚本
├── assets/
│   └── css/
│       └── style.css   # 全局样式文件（从 index.html 中拆分）
├── README.md           # 网站首页
├── _sidebar.md         # 侧边栏导航配置
├── _coverpage.md       # 封面页配置
├── .nojekyll           # GitHub Pages 必需文件（告诉它不要处理 Jekyll）
├── CLAUDE.md           # 此文件
└── posts/              # 博客文章目录
    ├── README.md       # 文章目录页
    ├── all-posts.md    # 所有文章列表
    ├── latest.md       # 最新文章列表
    ├── tech/           # 技术方案类文章
    │   └── README.md   # 技术方案分类索引
    ├── growth/         # 成长蜕变类文章（含原"成长思路"和"心路历程"）
    │   └── README.md   # 成长蜕变分类索引
    ├── thoughts/       # （历史目录，内容归入 growth/）
    └── about/          # 关于页面
```

## 核心配置说明

### Docsify 配置（在 index.html 中）

```javascript
window.$docsify = {
  name: 'Mouse陈的耗子窝',        // 网站名称
  loadSidebar: true,        // 启用侧边栏
  subMaxLevel: 2,           // 侧边栏显示的标题层级
  coverpage: true,          // 启用封面页（需要 _coverpage.md）
  search: { ... },          // 搜索配置
  themeColor: '#00b37e',    // 主题色（翡翠绿）
}
```

### 关键配置点

1. **loadSidebar: true** - 加载 `_sidebar.md` 作为侧边栏导航
2. **subMaxLevel: 2** - 自动提取文章中的二级标题到侧边栏
3. **搜索插件** - 自动索引所有 Markdown 文件
4. **分页插件** - 在文章底部显示上一页/下一页导航

## 内容管理规范

### 文章位置

根据文章分类放置到对应目录（两大分类）：
- 技术方案 → `posts/tech/`
- 成长蜕变 → `posts/growth/`（含原"成长思路"和"心路历程"内容）
- 关于页面 → `posts/about/`

### 文章格式

每篇文章应包含：

```markdown
# 文章标题

> 发布时间：YYYY-MM-DD · 分类：分类名称

文章内容...

---

**标签**：#标签1 #标签2
```

### 更新导航

添加新文章后，需要更新：
1. **`_sidebar.md`** - 添加文章链接到对应分类下
2. **`posts/all-posts.md`** - 添加到文章列表
3. **`posts/latest.md`** - 添加到最新文章（按时间）
4. **`posts/<分类>/README.md`** - 添加到对应分类的索引页

## 本地开发

### 启动本地服务器

由于 Docsify 需要 HTTP 服务器运行，使用以下命令之一：

```bash
# 使用 Python 3
python -m http.server 8000

# 使用 Node.js (需要全局安装 http-server)
npx http-server -p 8000

```

然后在浏览器访问 `http://localhost:8000`

### 实时预览

Docsify 的特性是保存文件后刷新浏览器即可看到更改，无需重新编译。

## 部署到 GitHub Pages

### 首次部署

1. 创建 GitHub 仓库
2. 推送代码到仓库
3. 进入仓库 Settings → Pages
4. Source 选择：Deploy from a branch
5. Branch 选择：master，目录选择 `/ (root)`
6. 访问 `https://gogodo.github.io`

### 更新部署

```bash
git add .
git commit -m "Add new post"
git push
```

GitHub Pages 会自动重新部署，通常需要 1-2 分钟。

### 重要：.nojekyll 文件

`.nojekyll` 文件必须存在且推送到仓库，这告诉 GitHub Pages 不要使用 Jekyll 处理，否则下划线开头的文件（如 `_sidebar.md`）会被忽略。

## 插件扩展

项目已集成的插件（在 index.html 中）：

- **搜索** - 文档全文搜索
- **字数统计** - 显示文章字数和阅读时间
- **分页** - 文章间导航
- **复制代码** - 代码块一键复制

添加新插件时，在 index.html 中添加对应的 `<script>` 标签。

## 代码高亮

已配置的语言（Prism.js）：
- bash, javascript, typescript, python, go, java
- markdown, yaml, json

添加新语言支持：
```html
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-语言名.min.js"></script>
```

## 常见问题

### 侧边栏不显示
- 确认 `loadSidebar: true` 已配置
- 确认 `_sidebar.md` 文件存在
- 确认 `.nojekyll` 文件已推送到仓库

### 搜索不工作
- 确认搜索插件 script 标签已添加
- 等待页面完全加载后使用

### GitHub Pages 样式丢失
- 确认 CDN 链接可访问（cdn.jsdelivr.net）
- 检查浏览器控制台是否有网络错误

## 样式自定义

全局样式在 `assets/css/style.css` 中定义：

```css
:root {
  --theme-color: #00b37e;  /* 翡翠绿主题色 */
}
```

修改 `--theme-color` 可全局更改主题色。注意同步修改 `index.html` 中 Docsify 配置的 `themeColor` 值。
