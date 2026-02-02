# 如何使用 Docsify 搭建个人博客

> 发布时间：2026-02-02 · 分类：技术方案

## 什么是 Docsify？

Docsify 是一个无需编译的文档网站生成器，它不会生成静态 HTML 文件，而是实时解析 Markdown 文件。这使得它非常适合用于快速搭建个人博客。

## 为什么选择 Docsify？

- ✅ **简单易用**：无需编译，直接运行
- ✅ **Markdown 原生**：用 Markdown 写作，专注于内容
- ✅ **轻量级**：加载速度快
- ✅ **插件丰富**：搜索、评论、分享等功能
- ✅ **GitHub Pages 友好**：部署极其简单

## 快速开始

### 1. 创建项目

创建一个新目录并初始化：

```bash
mkdir my-blog
cd my-blog
git init
```

### 2. 创建入口文件

创建 `index.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>我的博客</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '我的博客',
      repo: '',
      loadSidebar: true,
      subMaxLevel: 2,
      search: 'auto',
    }
  </script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
</body>
</html>
```

### 3. 创建侧边栏

创建 `_sidebar.md`：

```markdown
- [首页](/)
- 📝 博客
  - [第一篇文章](posts/post1.md)
  - [第二篇文章](posts/post2.md)
```

### 4. 部署到 GitHub Pages

1. 将代码推送到 GitHub 仓库
2. 在仓库设置中启用 GitHub Pages
3. 选择主分支作为源
4. 访问 `https://your-username.github.io/repo-name`

## 高级配置

### 自定义主题色

```javascript
window.$docsify = {
  themeColor: '#42b983',
}
```

### 添加字数统计

```html
<script src="//unpkg.com/docsify-count/dist/countable.min.js"></script>
```

### 启用代码复制

```html
<script src="//unpkg.com/docsify-copy-code@2"></script>
```

## 总结

Docsify 是一个简单而强大的博客解决方案。如果你想要快速开始写作，而不想折腾复杂的构建工具，Docsify 是一个很好的选择。

---

**标签**：#Docsify #博客 #GitHubPages
