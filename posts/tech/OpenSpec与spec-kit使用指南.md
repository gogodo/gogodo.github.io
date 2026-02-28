# OpenSpec 与 spec-kit 使用指南

> **核心理念**：先写规范，后写代码（Write Specs First, Code Later）
> **目标**：让 AI 编程更结构化、可预测、可靠

---

## 为什么要关注 Spec Coding？

**你有没有过这样的经历**？

- 让 AI 写代码，结果反复调试，改了五次还没达到预期
- 提示词写得挺详细，但 AI 总是"理解偏差"
- 项目迭代时，AI 生成的代码和现有代码风格不一致

**问题不在于 AI 能力**，而在于我们的输入方式。**Spec Coding（规范驱动开发）** 就是解决这个问题的答案——把模糊的需求变成结构化的规范，让 AI 精确理解你想要什么。

---

## 📚 目录

1. [什么是 Spec Coding](#什么是-spec-coding)
2. [OpenSpec 详解](#openspec-详解)
3. [spec-kit 详解](#spec-kit-详解)
4. [对比与选型](#对比与选型)
5. [实战工作流](#实战工作流)
6. [最佳实践](#最佳实践)

---

## 什么是 Spec Coding

### 传统 Vibe Coding 的问题

```
用户（模糊描述）→ AI（猜测意图）→ 代码（不确定结果）
❌ 提示词模糊
❌ 边界条件不清晰
❌ 需要反复调试
❌ 难以维护
```

### Spec Coding 的优势

```
用户（编写规范）→ AI（理解规格）→ 代码（精确实现）
✅ 需求结构化
✅ 边界条件明确
✅ 可预测的结果
✅ 易于审查和迭代
```

### 核心要素

一个完整的 Spec 应该包含：

- **功能需求**（Requirements）：系统应该做什么
- **规则约束**（Rules）：必须遵守的规则
- **边界条件**（Boundaries）：什么不该做
- **异常处理**（Exceptions）：如何处理错误
- **验收标准**（Acceptance Criteria）：如何判断完成

---

## OpenSpec 详解

### 简介

- **开发方**：Fission AI 团队
- **GitHub**：https://github.com/Fission-AI/OpenSpec
- **官网**：https://openspec.dev/
- **适用场景**：**已有项目的增量开发**（1→n）

### 核心理念

OpenSpec 将代码变更视为**变更提案（Change Proposal）**，通过管理提案的生命周期来实现安全的迭代开发。

### 安装

```bash
# 全局安装
npm install -g @fission-ai/openspec@latest

# 在项目中初始化
cd your-project
openspec init
```

### 项目结构

```
your-project/
├── specs/              # 规格说明目录
│   ├── system-design.md
│   └── api-contract.md
├── changes/            # 变更提案目录
│   ├── 001-add-auth.md
│   └── 002-refactor-db.md
└── AGENTS.md           # AI 助手指南
```

### 工作流程（5步法）

#### 1. Propose（提出变更）
创建变更提案，描述要做什么

```markdown
# changes/001-add-user-authentication.md

## 变更目标
为系统添加用户认证功能

## 动机
当前系统缺乏用户管理，需要支持多用户

## 提案详情
- 添加 JWT 认证
- 支持注册/登录
- 实现权限控制
```

#### 2. Review & Align（审查并对齐）
与团队/AI 讨论提案，确保理解一致

```bash
openspec propose  # 提交提案供审查
```

#### 3. Plan（规划）
制定详细的实施计划

```markdown
## 实施计划
1. 设计数据库 schema（用户表）
2. 实现 JWT 工具类
3. 创建认证 API 端点
4. 添加中间件
5. 编写测试
```

#### 4. Implement（实施）
执行实施计划，AI 根据 Spec 生成代码

```bash
# 使用 Claude Code 或 Qoder CLI
claude  # AI 会读取 changes/001-*.md 并执行
```

#### 5. Archive（归档）
完成变更后归档提案

```bash
openspec archive 001
```

### 常用命令

```bash
# 初始化项目
openspec init

# 创建新提案
openspec propose

# 查看所有提案
openspec list

# 开始实施某个提案
openspec start <proposal-id>

# 完成并归档
openspec complete <proposal-id>
```

### AGENTS.md 示例

```markdown
# AGENTS.md

## 项目概述
这是一个电商后端系统，使用 Node.js + Express

## 开发原则
1. 遵循 RESTful 设计
2. 所有 API 需要认证
3. 使用 TypeScript
4. 数据库使用 PostgreSQL

## 变更流程
1. 阅读 changes/ 目录下的提案
2. 确认理解后再开始实施
3. 实施完成后更新提案状态
```

---

## spec-kit 详解

### 简介

- **开发方**：GitHub 实验室团队（GitHub Next）
- **GitHub**：https://github.com/github/spec-kit
- **官网**：https://githubnext.com/projects/spec-kit/
- **适用场景**：**从零开始新建项目**（0→1）

### 核心理念

spec-kit 提供从想法到实现的**完整开发框架**，通过5个阶段引导你完成项目。

### 安装

**系统要求**：Python 3.10+

```bash
# 克隆仓库
git clone https://github.com/github/spec-kit.git
cd spec-kit

# 安装依赖（使用 uv）
pip install uv
uv sync

# 初始化新项目
python -m speckit init my-project
```

### 项目结构

```
my-project/
├── .speckit/
│   ├── constitution.md      # 项目原则
│   ├── specs/               # 规格说明
│   ├── plans/               # 实施计划
│   └── tasks/               # 任务列表
└── README.md
```

### 工作流程（5步法）

#### 1. Constitution（设定原则）
定义项目的基本原则和约束

```markdown
# .speckit/constitution.md

## 项目目标
构建一个高性能的博客系统

## 技术栈
- 后端：Python + FastAPI
- 前端：React + TypeScript
- 数据库：PostgreSQL

## 设计原则
1. 简单优于复杂
2. 性能优先
3. 安全第一
4. 可测试性
```

#### 2. Specify（编写规格）
详细描述系统需求

```bash
/specify
```

```markdown
# .speckit/specs/user-management.md

## 功能需求
用户应该能够：
- 注册账号
- 登录系统
- 修改个人信息
- 重置密码

## API 规范
POST /api/users/register
- Request: { email, password, name }
- Response: { userId, token }

POST /api/users/login
- Request: { email, password }
- Response: { userId, token }
```

#### 3. Plan（制定计划）
将规格拆解为实施计划

```bash
/plan
```

```markdown
# .speckit/plans/phase-1-auth.md

## Phase 1: 认证系统

### 步骤
1. 设计用户表结构
2. 实现密码哈希
3. 创建 JWT token 生成
4. 实现注册 API
5. 实现登录 API
6. 编写单元测试

### 依赖
- 需要先配置数据库连接
- 需要准备 JWT secret key
```

#### 4. Task（拆分任务）
将计划拆分为可执行的任务

```bash
/task
```

```markdown
# .speckit/tasks/001-db-schema.md

## 任务：设计用户表

### SQL Schema
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100),
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 验收标准
- [ ] 表创建成功
- [ ] email 字段有唯一索引
- [ ] password 字段加密存储
```

#### 5. Implement（实施）
使用 AI 工具执行任务

```bash
/implement
```

### 常用命令

```bash
# 初始化项目
python -m speckit init <project-name>

# 设定项目原则
/constitution

# 编写规格说明
/specify

# 制定实施计划
/plan

# 拆分任务
/task

# 开始实施
/implement

# 查看进度
/status
```

---

## 对比与选型

### 功能对比表

| 维度 | OpenSpec | spec-kit |
|------|----------|----------|
| **适用场景** | 已有项目迭代 | 新建项目 |
| **变更管理** | ✅ 提案生命周期管理 | ⚠️ 相对较弱 |
| **学习曲线** | 较低 | 中等 |
| **工具集成** | 通用 AI 工具 | GitHub Copilot 深度集成 |
| **工作流重点** | 变更控制 | 完整开发流程 |
| **文档规范** | 自由度较高 | 结构化更强 |

### 选型决策树

```
需要开发新功能
    │
    ├─ 是否已有代码库？
    │   │
    │   ├─ 是 → OpenSpec（管理变更更安全）
    │   └─ 否 → spec-kit（完整框架更合适）
    │
    ├─ 团队规模？
    │   │
    │   ├─ 个人/小团队 → OpenSpec（轻量级）
    │   └─ 中大型团队 → spec-kit（流程更规范）
    │
    └─ 技术栈偏好？
        │
        ├─ Node.js/前端 → OpenSpec
        └─ Python/GitHub 生态 → spec-kit
```

### 实际使用建议

**场景 1：个人开发者 + 新项目**
→ 推荐：**spec-kit**
- 理由：完整框架，避免遗漏步骤

**场景 2：团队协作 + 现有项目**
→ 推荐：**OpenSpec**
- 理由：变更管理更严格，审查流程完善

**场景 3：快速原型 + 迭代优化**
→ 推荐：**OpenSpec**
- 理由：轻量级，快速开始

**场景 4：企业级项目 + 从零开始**
→ 推荐：**spec-kit**
- 理由：流程规范，适合长期维护

---

## 实战工作流

### 场景：为现有项目添加用户认证功能

#### 使用 OpenSpec

```bash
# 1. 初始化（如果还没初始化）
openspec init

# 2. 创建变更提案
# Windows 用户：直接创建文件 changes/001-add-auth.md
# macOS/Linux 用户：可使用以下命令
cat > changes/001-add-auth.md << 'EOF'
# 变更提案：添加用户认证

## 目标
为系统添加 JWT 认证机制

## 范围
- 用户注册/登录
- JWT token 生成与验证
- 认证中间件
- 不包括：OAuth、第三方登录

## 技术方案
- 使用 bcrypt 加密密码
- JWT 有效期 24 小时
- Redis 存储 token 黑名单

## 验收标准
- [ ] 用户可以注册
- [ ] 用户可以登录
- [ ] 受保护路由需要认证
- [ ] Token 过期能正确处理
EOF

# 3. 使用 AI 工具实施
claude  # Claude Code 会读取 changes/001-add-auth.md

# 4. 完成后归档
openspec complete 001
```

#### 使用 spec-kit（如果是新项目）

```bash
# 1. 初始化项目
python -m speckit init my-blog-system
cd my-blog-system

# 2. 设定原则
/constitution
# 编辑 .speckit/constitution.md

# 3. 编写认证规格
/specify
# 创建 .speckit/specs/authentication.md

# 4. 制定计划
/plan
# 创建 .speckit/plans/auth-implementation.md

# 5. 拆分任务
/task
# 创建多个任务文件

# 6. 实施
/implement
# AI 逐个执行任务
```

---

## 最佳实践

### 1. 编写高质量 Spec

#### ✅ 好的 Spec

```markdown
# 用户登录功能

## 功能需求
用户可以通过邮箱和密码登录系统

## API 端点
POST /api/auth/login
Request:
{
  "email": "user@example.com",
  "password": "securepassword"
}

Response (200):
{
  "token": "eyJhbGc...",
  "userId": "12345"
}

Response (401):
{
  "error": "Invalid credentials"
}

## 业务规则
- 密码至少 8 个字符
- 连续失败 5 次锁定账户 15 分钟
- Token 有效期 24 小时

## 异常处理
- 用户不存在 → 404
- 密码错误 → 401
- 账户锁定 → 423
```

#### ❌ 不好的 Spec

```markdown
# 用户登录

做一个登录功能，要安全一点
```

### 2. 与 AI 工具配合

**推荐工具**：
- **Claude Code**：通用性强，支持多工具
- **Qoder CLI**：国内可用，支持 MCP
- **GitHub Copilot**：与 spec-kit 深度集成

**工作流**：

```bash
# 1. 编写 Spec
vim changes/001-feature.md

# 2. 让 AI 阅读并理解
claude  # 启动 Claude Code
> 请先阅读 changes/001-feature.md，确认理解后开始实施

# 3. AI 生成代码
> 根据 Spec 生成代码

# 4. 人工审查
> 代码审查，确保符合 Spec

# 5. 测试验证
> 运行测试，验证功能
```

### 3. 版本控制建议

```bash
# Spec 文件应该纳入版本控制
git add changes/ specs/ .speckit/
git commit -m "docs: add user authentication spec"

# 变更提案可以作为 PR 审查
git checkout -b feature/001-auth
# ... 编写 spec 和代码
git push origin feature/001-auth
# 创建 PR，要求 review spec
```

### 4. 团队协作流程

```
1. 开发者创建 Spec 草稿
2. 团队 Review Spec（不看代码）
3. Spec 通过后，AI 开始实施
4. Code Review（对照 Spec 验证）
5. 测试验收
6. 合并代码
```

### 5. 常见问题

**Q1：Spec 写到多详细？**
A：足够详细即可，目标是让 AI 无需猜测。包括输入输出、边界条件、异常处理。

**Q2：如何处理 Spec 变更？**
A：创建新的变更提案，明确标注"修改 XXX Spec"。OpenSpec 的提案机制很适合。

**Q3：AI 不理解 Spec 怎么办？**
A：在对话中澄清，然后**更新 Spec 文档**，而不是只在对话中说明。

**Q4：可以在一个项目中同时使用两者吗？**
A：不建议。选一个作为主要工具，另一个可以参考其理念。

---

## 进阶技巧

### 1. 结合 CLAUDE.md

在项目根目录创建 `CLAUDE.md`，增强 AI 对项目的理解：

```markdown
# CLAUDE.md

## 项目说明
这是一个使用 OpenSpec 进行规范驱动开发的项目。

## 工作流程
1. 所有变更必须先创建提案（changes/ 目录）
2. 提案通过后才能开始实施
3. 实施时必须遵循 Spec 中的要求

## 代码规范
- 使用 TypeScript
- 遵循 ESLint 规则
- 所有函数必须有 JSDoc
- 测试覆盖率 > 80%

## 禁止事项
- ❌ 不得跳过 Spec 直接写代码
- ❌ 不得修改已归档的提案
- ❌ 不得在生产环境使用开发密钥
```

### 2. 自动化脚本

创建 `scripts/speccing.sh`：

```bash
#!/bin/bash
# 快速创建变更提案

if [ -z "$1" ]; then
  echo "Usage: ./scripts/speccing.sh <feature-name>"
  exit 1
fi

FEATURE=$1
TIMESTAMP=$(date +%Y%m%d)
FILE="changes/${TIMESTAMP}-${FEATURE}.md"

cat > "$FILE" << EOF
# 变更提案：${FEATURE}

## 目标


## 范围
- 包括：
- 不包括：

## 技术方案


## 验收标准
- [ ]

EOF

echo "✅ 创建提案：$FILE"
vim "$FILE"
```

### 3. 模板库

维护常用 Spec 模板：

```
templates/
├── api-endpoint.md
├── database-migration.md
├── frontend-component.md
└── bug-fix.md
```

---

## 资源链接

### 官方资源

- **OpenSpec**：https://github.com/Fission-AI/OpenSpec
- **OpenSpec 官网**：https://openspec.dev/
- **spec-kit**：https://github.com/github/spec-kit
- **Agent Client Protocol**：https://agentclientprotocol.com/

### 相关文章

- [Specification-Driven Development (SDD) 介绍](https://openspec.dev/blog/what-is-sdd)
- [GitHub Engineering: Spec-Kit 发布](https://github.blog/news-insights/product-news/introducing-spec-kit/)
- [Spec Coding vs Vibe Coding](https://www.anthropic.com/blog/spec-driven-development)

### 社区讨论

- Reddit: r/SpecDrivenDevelopment
- Discord: Fission AI Community
- GitHub Discussions: spec-kit discussions

---

## 总结

### 核心要点

1. **Spec First**：先写规范，后写代码
2. **工具选择**：
   - 新项目 → spec-kit
   - 旧项目 → OpenSpec
3. **团队协作**：Spec 作为沟通媒介
4. **持续改进**：根据实践调整 Spec

### 开始使用

```bash
# 现有项目
npm install -g @fission-ai/openspec
openspec init

# 新项目
git clone https://github.com/github/spec-kit.git
python -m speckit init my-project
```

---

**最后更新**：2026-02-28

> **注意**：本文所介绍的工具和功能可能随版本更新而变化，请以 [官方文档](https://github.com/Fission-AI/OpenSpec) 和 [spec-kit 官方仓库](https://github.com/github/spec-kit) 为准。
