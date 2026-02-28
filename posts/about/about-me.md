# 关于我

> 更新时间：2026-02-28 · 分类：关于

<style>
/* === 读者分层卡片 === */
.reader-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
.reader-card {
  padding: 1.25rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  background: var(--bg-secondary);
  transition: border-color 250ms ease;
}
.reader-card:hover {
  border-color: var(--theme-color);
}
.reader-card-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--theme-color);
  margin-bottom: 0.5rem;
}
.reader-card-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.4rem;
}
.reader-card-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* === 数据展示网格 === */
.stat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border-color);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  overflow: hidden;
  margin: 1.5rem 0;
}
.stat-item {
  background: var(--bg-secondary);
  padding: 1.5rem 1rem;
  text-align: center;
}
.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: var(--theme-color);
  line-height: 1;
  letter-spacing: -0.03em;
  display: block;
}
.stat-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-top: 0.4rem;
  display: block;
}

/* === 时间线 === */
.timeline {
  position: relative;
  padding-left: 1.5rem;
  margin: 1.5rem 0;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.5rem;
  bottom: 0;
  width: 2px;
  background: var(--border-color);
}
.timeline-item {
  position: relative;
  margin-bottom: 2rem;
}
.timeline-item:last-child {
  margin-bottom: 0;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -1.6rem;
  top: 0.4rem;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--bg-primary);
  border: 2px solid var(--border-color);
}
.timeline-item.active::before {
  border-color: var(--theme-color);
  background: var(--theme-color);
  box-shadow: 0 0 8px rgba(0, 179, 126, 0.3);
}
.timeline-period {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  letter-spacing: 0.05em;
  margin-bottom: 0.3rem;
  font-family: var(--font-family-code);
}
.timeline-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}
.timeline-desc {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* === 服务卡片 === */
.service-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
.service-card {
  padding: 1.5rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  background: var(--bg-card);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: all 250ms ease;
}
.service-card:hover {
  border-color: var(--theme-color);
  box-shadow: 0 0 20px rgba(0, 179, 126, 0.08);
  transform: translateY(-2px);
}
.service-tag {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--theme-color);
  background: var(--theme-color-light);
  padding: 2px 8px;
  border-radius: var(--radius-full);
  display: inline-block;
  width: fit-content;
}
.service-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
}
.service-desc {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.6;
  flex: 1;
}
.service-desc ul {
  margin: 0.5rem 0 0;
  padding-left: 1.2rem;
}
.service-desc li {
  margin-bottom: 0.3rem;
}
.service-action {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--theme-color);
  margin-top: 0.5rem;
}

/* === CTA区块 === */
.cta-block {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  padding: 2rem 2.5rem;
  text-align: center;
  margin: 3rem 0;
}
.cta-block h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.5rem;
  border: none;
  padding: 0;
}
.cta-block p {
  color: var(--text-secondary);
  margin: 0 0 1.5rem;
  font-size: 0.9rem;
}
.cta-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  flex-wrap: wrap;
}
.cta-actions a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 24px;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 150ms ease;
  text-decoration: none !important;
  letter-spacing: 0.02em;
  border: none !important;
}
.cta-actions .btn-primary {
  background-color: var(--text-primary);
  color: var(--bg-primary);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}
.cta-actions .btn-primary:hover {
  background-color: var(--theme-color);
  color: #ffffff;
  box-shadow: 0 0 20px rgba(0, 179, 126, 0.15);
  transform: translateY(-1px);
}
.cta-actions .btn-secondary {
  background-color: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-color-dark) !important;
}
.cta-actions .btn-secondary:hover {
  background-color: var(--bg-secondary);
  border-color: var(--text-primary) !important;
}

/* === 经验概览 === */
.exp-overview {
  margin: 1.5rem 0;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
.exp-row {
  display: flex;
  align-items: baseline;
  padding: 0.75rem 1.25rem;
  border-bottom: 1px solid var(--border-color);
  gap: 1rem;
}
.exp-row:last-child {
  border-bottom: none;
}
.exp-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--theme-color);
  white-space: nowrap;
  min-width: 4.5rem;
  letter-spacing: 0.03em;
}
.exp-content {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* === 联系区 === */
.contact-grid {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  margin: 1.5rem 0;
}
.contact-email {
  flex: 1;
}
.contact-wechat {
  text-align: center;
}

/* === 响应式 === */
@media (max-width: 768px) {
  .reader-cards { grid-template-columns: 1fr; }
  .stat-grid { grid-template-columns: repeat(2, 1fr); }
  .service-grid { grid-template-columns: 1fr; }
  .contact-grid { flex-direction: column; }
  .cta-block { padding: 1.5rem; }
  .exp-row { flex-direction: column; gap: 0.25rem; }
  .exp-label { min-width: unset; }
}
</style>

## 你好，我是陈君

自2007年毕业后，做企业级软件 19 年了，最近几年一直在做一件事——**把 AI 从演示环境跑进生产系统**。

不是在 PPT 里，是在中大型企业的业务系统里、在工业互联网的核心链路上、在每天有人真正在用的运维工具里。

如果你正好也在做（或想做）类似的事，希望我的经历对你有帮助。

<div class="reader-cards">
  <div class="reader-card">
    <div class="reader-card-label">企业技术决策者</div>
    <div class="reader-card-title">想引入 AI，但不确定风险</div>
    <div class="reader-card-desc">评估过很多方案，Demo 都很好看，但不知道上线后会不会翻车。我帮你做技术可行性判断。</div>
  </div>
  <div class="reader-card">
    <div class="reader-card-label">中小企业老板</div>
    <div class="reader-card-title">想用 AI 降本增效</div>
    <div class="reader-card-desc">听说 AI 能提效，但不知道从哪个场景切入、投多少预算合理。我帮你找到最小可行的切入点。</div>
  </div>
  <div class="reader-card">
    <div class="reader-card-label">开发者 / 技术团队</div>
    <div class="reader-card-title">Demo 做出来了，上不了线</div>
    <div class="reader-card-desc">RAG 命中率不稳、权限没法隔离、评估全靠感觉。我分享从 Demo 到生产的完整工程经验。</div>
  </div>
</div>

---

## 19年，一个软件人的转型

很多人问我："你做了 19 年传统软件，怎么突然转 AI 了？"

其实不是突然。是做了足够多的企业系统之后，发现**最贵的不是技术，而是工程判断力**——知道什么该做、什么不该做、什么时候该停。这种判断力，恰好是 AI 落地最稀缺的东西。

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-period">2007 — 2018 · 打地基的11年</div>
    <div class="timeline-title">从写代码到看懂业务</div>
    <div class="timeline-desc">
      在大型企业级财务系统中磨砺了近 11 年。从初级开发做起，一步步成长为技术骨干。深度参与中*油财务共享中心建设，带领团队完成 6 家地区公司的系统实施，支撑千级并发的业务处理。<br><br>
      这段经历教会我一件事：<strong>企业级系统的复杂度不在技术，在业务</strong>。你不理解业务，写再好的代码都是白搭。
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-period">2019 — 2024 · 架构师阶段</div>
    <div class="timeline-title">从执行者到设计者</div>
    <div class="timeline-desc">
      转型为架构师，主导工业互联网 SaaS 平台从 0 到 1 的设计与落地。主持用 DDD 划分微服务边界，搭建企业级 DevOps 流水线，带领核心人团队交付核心功能。先后服务潍柴、TCL、海信、中海油 等头部企业的 SRM\PLM\MOM 研发与咨询项目，通过架构方案演示成功获取 4 家企业的数字化转型咨询订单。<br><br>
      也是在这个阶段，培养了多名核心技术骨干。我开始意识到：<strong>技术人最大的杠杆不是写代码，是帮别人少走弯路</strong>。
    </div>
  </div>
  <div class="timeline-item active">
    <div class="timeline-period">2024 — 至今 · AI 转型</div>
    <div class="timeline-title">把 AI 跑进生产环境</div>
    <div class="timeline-desc">
      这不是追风口，是解决真实问题。运维工作中重复问题多、响应慢，我自己动手开发了一套桌面运维工具（15,900+ 行代码），把高频问题结构化沉淀为 248 条知识单元，集成 RAG 智能问答，内部验收 Top1 命中率达到 80%。<br><br>
      同时深入实践 Claude Code 全自动开发，构建了企业级 Multi-Agent 协作配置体系，按 6 个专家角色按需调度，消除 6,255 行冗余配置。<br><br>
      <strong>19 年的工程化思维 + AI 技术实践，我找到了自己最独特的定位。</strong>
    </div>
  </div>
</div>

> 他们讲 AI 技术，我讲 AI 如何在年产值数亿的企业系统中真正跑起来。

---

## 我的经验版图

<div class="exp-overview">
  <div class="exp-row">
    <span class="exp-label">系统经验</span>
    <span class="exp-content">财务共享中心 · SRM · PLM · MOM · 工业互联网 SaaS · RAG 智能运维</span>
  </div>
  <div class="exp-row">
    <span class="exp-label">行业覆盖</span>
    <span class="exp-content">石油石化（中石油、中海油）· 家电制造（海信、TCL）· 装备制造（潍柴）</span>
  </div>
  <div class="exp-row">
    <span class="exp-label">角色进化</span>
    <span class="exp-content">初级开发 → 技术骨干 → 架构师 → AI 实践者</span>
  </div>
</div>

<div class="cta-block">
  <h3>有一个 AI 落地的问题想聊聊？</h3>
  <p>发封邮件说说你的场景，或者加微信直接聊。我通常 48 小时内回复。</p>
  <div class="cta-actions">
    <a href="mailto:mouse43992972@gmail.com?subject=来自博客的咨询&body=你好陈君，我在你的博客上看到...%0A%0A我的场景是：%0A我目前遇到的问题：%0A希望你能帮我：" class="btn-primary">发邮件聊聊</a>
    <a href="javascript:void(0)" onclick="document.getElementById('联系我').scrollIntoView({behavior:'smooth'})" class="btn-secondary">加微信</a>
  </div>
</div>

---

## 我提供的服务

<div class="service-grid">
  <div class="service-card">
    <span class="service-tag">咨询</span>
    <div class="service-title">AI 落地咨询</div>
    <div class="service-desc">
      帮你诊断 AI 项目是否在正确的轨道上，避免烧钱踩坑。
      <ul>
        <li>AI 应用场景评估与技术选型</li>
        <li>RAG / 知识库方案设计</li>
        <li>从 Demo 到生产的路径规划</li>
      </ul>
    </div>
    <div class="service-action">适合：企业决策者 / 想引入 AI 的团队</div>
  </div>
  <div class="service-card">
    <span class="service-tag">培训</span>
    <div class="service-title">AI 开发实践培训</div>
    <div class="service-desc">
      不讲理论，只讲能在项目中用上的实操技能。
      <ul>
        <li>RAG 工程化全链路实践</li>
        <li>Claude Code 企业级开发</li>
        <li>Prompt 工程与评估迭代</li>
      </ul>
    </div>
    <div class="service-action">适合：开发者 / 技术团队</div>
  </div>
  <div class="service-card">
    <span class="service-tag">评审</span>
    <div class="service-title">架构评审与优化</div>
    <div class="service-desc">
      已有 AI 系统但效果不稳定？我来帮你找到问题根源。
      <ul>
        <li>现有架构诊断与瓶颈分析</li>
        <li>RAG 命中率优化方案</li>
        <li>改进路线图与优先级建议</li>
      </ul>
    </div>
    <div class="service-action">适合：已有 AI 系统需要改进的团队</div>
  </div>
</div>

<p style="text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 0.5rem;">
  具体内容和形式可以根据你的需求灵活调整，<a href="mailto:mouse43992972@gmail.com">发邮件</a>或<a href="javascript:void(0)" onclick="document.getElementById('联系我').scrollIntoView({behavior:'smooth'})">加微信</a>聊聊。
</p>

---

## 先从这里开始读

如果你还在了解阶段，没关系。先读几篇文章，看看对你有没有帮助：

- **成长蜕变** — 19 年技术人的成长路径与决策复盘 → [查看全部](../growth/README.md)
- **技术方案** — 可复用的落地方案与实操细节 → [查看全部](../tech/README.md)

更多内容：[最新文章](../latest.md) · [所有文章](../all-posts.md)

---

## 联系我

不管是咨询合作、培训需求，还是单纯想交流 AI 落地的经验，都欢迎联系我。

<div class="contact-grid">
  <div class="contact-email">
    <p style="margin: 0 0 0.5rem; font-weight: 600; color: var(--text-primary);">邮箱</p>
    <p style="margin: 0 0 1rem;"><a href="mailto:mouse43992972@gmail.com">mouse43992972@gmail.com</a></p>
    <p style="margin: 0; font-size: 0.85rem; color: var(--text-muted);">
      如果方便的话，来信请附上：<br>
      · 你的业务场景<br>
      · 当前进度和遇到的瓶颈<br>
      · 希望我帮你解决什么问题
    </p>
  </div>
  <div class="contact-wechat">
    <img src="../../assets/images/wechat-qr.png" alt="微信二维码" width="160" style="border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <p style="margin: 0.5rem 0 0; font-weight: 500; font-size: 0.9rem; color: var(--text-primary);">扫码添加微信</p>
    <p style="margin: 0.25rem 0 0; font-size: 0.8rem; color: var(--text-muted);">请备注来源（如：博客 / AI落地）</p>
  </div>
</div>

---

感谢你读到这里。希望下次我们可以在真实的项目里协作。
