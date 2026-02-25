# Git 提交规范

本文档定义了项目中使用的 Git 提交信息规范，基于 [约定式提交（Conventional Commits）](https://www.conventionalcommits.org/) 标准。

## 一、提交信息结构规范

### 基本格式

```
<type>(<scope>): <subject>

[optional body]

[optional footer(s)]
```

### 标题（必填）

- **格式**：`<type>(<scope>): <subject>`
- **示例**：`feat(auth): 添加用户登录功能`

#### 类型（type）

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复问题 |
| `docs` | 文档变更 |
| `style` | 代码格式（不影响功能） |
| `refactor` | 代码重构 |
| `perf` | 性能优化 |
| `test` | 测试相关 |
| `build` | 构建系统或外部依赖变更 |
| `ci` | CI 配置文件和脚本变更 |
| `chore` | 构建工具或辅助工具变动 |
| `revert` | 回退提交 |

#### 范围（scope）

可选，用括号包裹，说明提交影响的部分：

- `auth` - 认证相关
- `ui` - 用户界面
- `api` - API 接口
- `config` - 配置文件
- 或具体模块名称

#### 描述（subject）

- 简明扼要（50 字符内）
- 以动词开头（使用祈使句，如「添加」而非「添加了」）
- 不以句号结尾
- 使用中文

### 正文（可选）

- 详细说明变更背景、原因和影响
- 说明「是什么」和「为什么」，而非「怎么做」
- 每行不超过 72 个字符

示例：

```
修复用户登录时的验证逻辑错误，避免空密码提交。
修改了 `auth.js` 中的验证函数，增加空值检查。
```

### 脚注（可选）

#### 关联 Issue

```
Closes `#123`
Fixes `#456`
Refs `#789`
```

#### 破坏性变更

若引入不兼容改动，需以 `BREAKING CHANGE:` 开头说明：

```
BREAKING CHANGE: 认证接口从 `/api/v1/login` 变更为 `/api/v2/auth/login`，
请求参数格式也发生改变，请参考文档更新调用方式。
```

或在类型后加 `!` 标记：

```
feat(auth)!: 修改用户认证 API 接口
```

## 二、完整示例

### 1. 新增功能

```
feat(auth): 添加用户登录功能

实现用户登录功能，包括表单验证和 API 调用。
Closes #789
```

### 2. 修复问题

```
fix(login): 修复空密码提交问题

修复用户可提交空密码的问题，增加前端验证。
```

### 3. 带范围的修复

```
fix(ui): 修复移动端导航栏遮挡问题

在 iOS Safari 浏览器中，底部导航栏会遮挡内容区域。
通过增加页面底部 padding 解决此问题。

Closes #123
```

### 4. 文档变更

```
docs(readme): 更新安装指南

更新安装指南，添加 Windows 系统的安装步骤。
```

### 5. 破坏性变更

```
feat(api)!: 修改用户数据接口

BREAKING CHANGE: 用户数据接口响应格式变更，
旧版 `data.user` 改为 `data.userInfo`。
```

## 三、工具配置

### 1. Commitizen（交互式提交工具）

**安装**：

```bash
npm install -g commitizen

# 在项目中使用
npm install -D cz-conventional-changelog
echo '{ "path": "cz-conventional-changelog" }' > .czrc
```

**使用**：

```bash
git cz  # 替代 git commit
```

### 2. Commitlint（提交信息校验）

**安装**：

```bash
npm install -D @commitlint/cli @commitlint/config-conventional
```

**配置**（创建 `commitlint.config.js`）：

```javascript
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', [
      'feat', 'fix', 'docs', 'style', 'refactor',
      'perf', 'test', 'build', 'ci', 'chore', 'revert'
    ]],
    'type-case': [0],
    'type-empty': [2, 'never'],
    'subject-empty': [2, 'never'],
    'subject-case': [0],
    'header-max-length': [2, 'always', 72]
  }
};
```

### 3. Husky（Git 钩子集成）

**作用**：在提交前自动校验提交信息

**配置**（在 `package.json` 中添加）：

```json
{
  "husky": {
    "hooks": {
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  }
}
```

或使用 Husky v9+：

```bash
npm install -D husky
npx husky init
echo "npx --no -- commitlint --edit \$1" > .husky/commit-msg
```

### 4. Git 提交模板

创建 `.gitmessage` 文件：

```
# 类型:
# feat: 新功能
# fix: 修复问题
# docs: 文档变更
# style: 代码格式（不影响功能）
# refactor: 代码重构
# perf: 性能优化
# test: 测试相关
# build: 构建系统或外部依赖变更
# ci: CI 配置文件和脚本变更
# chore: 构建工具或辅助工具变动
# revert: 回退提交
#
# --------------------
# 范围: (可选) auth/ui/api/config 等
# --------------------
#
# --------------------
# 简短描述: (必填) 使用中文，不超过50字，以动词开头
# --------------------
#
# --------------------
# 详细描述: (可选) 说明是什么和为什么
# --------------------
#
# --------------------
# 页脚: (可选) 关联 Issue 或 BREAKING CHANGE
# Closes #123
# BREAKING CHANGE:
# --------------------
```

配置 Git 使用模板：

```bash
git config commit.template .gitmessage
```

## 四、最佳实践

### 1. 分支策略

- **主分支**：`master` 作为生产分支
- **开发分支**：`develop` 用于集成新功能
- **功能分支**：从 `develop` 分出，命名如 `feature-yymmdd-增加单点登录逻辑`
- **修复分支**：从 `master` 分出，命名如 `hotfix-yymmdd-修复登录代码bug`


### 2. 提交原则

- **原子性**：每次提交仅包含一个逻辑变更
- **清晰描述**：使用清晰、简洁的语言说明变更
- **及时提交**：小步快跑，避免大批量变更堆积
- **关联问题**：在提交信息中关联相关 Issue

### 3. 团队协作

- **统一规范**：团队共同遵守提交规范
- **工具强制**：通过工具（如 husky + commitlint）强制执行
- **代码审查**：在 PR 中检查提交信息规范性

## 五、规范优势

| 优势 | 说明 |
| --- | --- |
| **清晰历史** | 快速定位变更内容和原因 |
| **自动化工具** | 支持自动生成 Change Log |
| **团队协作** | 统一代码提交标准，提升可维护性 |
| **版本管理** | 便于语义化版本控制（Semantic Versioning） |

