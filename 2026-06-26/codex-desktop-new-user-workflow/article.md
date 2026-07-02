# Codex 桌面版专题 X 草稿

## 选题定位

原文《如果你刚装 Codex 桌面版，这篇可以让你少走 90% 的弯路》是一篇功能总览型文章，覆盖了界面、模式、终端、Review、Git、浏览器、Chrome Extension、Computer Use、Skills、Plugins、MCP、Automations、AGENTS.md、权限和提示词。

这次专题稿不再做“按钮说明书”，而是改成一个更适合 X 的观点型教程：

> 刚装 Codex 桌面版，最重要的不是学会每个按钮，而是建立一套“上下文 -> 计划 -> 小步修改 -> 验证 -> Review -> 沉淀”的工作流。

## 资料依据

- 本地原文：`F:/文档/仓库/codex/如果你刚装 Codex 桌面版，这篇可以让你少走 90% 的弯路.md`
- OpenAI Codex 官方手册，本地刷新时间：2026-06-26。
- Axios 2026-06-25 关于 Codex / AI agents 使用增长的报道。
- Business Insider 2026-06-20 关于 loop engineering 的报道。
- arXiv 2026-01-28 关于 `AGENTS.md` 对 AI coding agents 效率影响的论文。

## 推荐标题

首选：

> 刚装 Codex 桌面版，别先学按钮

标题图：

![标题图：别先学按钮，先学工作流](assets/codex-new-user/01-title-5x2.png)

备选：

1. 我终于明白 Codex 桌面版该怎么入门了
2. Codex 桌面版不是聊天框，而是一个工作流系统
3. 新手用 Codex 最容易犯的错：上来就许愿
4. 如果你刚装 Codex，这套工作流能少走很多弯路
5. Codex 桌面版入门：先学协作方式，再学功能按钮

## X 发布版：10 条 Thread

1/

[配图：assets/codex-new-user/01-title-5x2.png]

如果你刚装 Codex 桌面版，先别急着研究每个按钮。

新手最容易犯的错，是把它当成一个更强的聊天框：

“帮我优化项目”
“帮我修一下”
“帮我做个网站”

这样用，通常只能发挥很小一部分能力。

2/

我看完一篇 Codex 桌面版入门长文，又查了一圈官方手册和近期资料。

我的结论是：

Codex 桌面版真正难的不是功能。

而是你要从“问 AI 要答案”，切换成“和一个能读文件、改代码、跑命令、看浏览器、做 Review 的执行者协作”。

3/

第一次打开 Codex，最稳的第一步不是让它改东西。

而是让它读项目、建地图：

先不要改代码。
请阅读这个项目，告诉我：
1. 它是做什么的
2. 主要目录结构
3. 启动、测试、构建命令
4. 加新功能应该从哪里看起

4/

给 Codex 任务时，最好固定 4 件事：

目标：我要做什么
上下文：哪些文件、错误、页面重要
约束：不要改哪里，不能引入什么
完成标准：什么结果算完成

这比“帮我修一下页面”强太多。

5/

复杂任务不要直接开干。

先让它计划。

OpenAI 官方最佳实践里也强调：复杂、模糊、难描述的任务，先让 Codex 收集上下文、提问、做计划，再实现。

我的经验是：

你越着急让它动手，它越容易扩大范围。

6/

[配图：assets/codex-new-user/02-workflow.png]

Codex 桌面版最值钱的一点：

它可以自己验证结果。

它能开终端、跑测试、看报错、再修一轮。

前端项目还能启动本地服务，用内置浏览器看 localhost 页面，标注溢出、错位、空状态、加载状态。

不要只让它“写”，要让它“验证”。

7/

浏览器能力要分清：

内置 Browser：
适合 localhost、本地预览、公开页面。

Chrome Extension：
适合需要登录态的网站、后台系统、Gmail、Salesforce、内部工具。

Computer Use：
适合必须操作桌面 App 或系统界面的场景。

别把三者混着用。

8/

[配图：assets/codex-new-user/03-compare.png]

新手一定要学 Review。

Codex 改完后，不要直接信。

打开 diff，看它改了哪些文件。

能接受的改动留下，跑偏的地方直接 inline comment：

“只处理这条评论，不要扩大修改范围。”

这一步决定你是在协作，还是在盲信。

9/

真正进阶的用法，是把重复经验沉淀下来。

AGENTS.md：写项目长期规则。
Skills：沉淀可复用工作流。
Automations：让稳定任务定时执行。
Worktree：让新功能和实验隔离运行。

现在外部也开始讨论 loop engineering。

本质就是：别每次重新提示，而是设计能重复运转的流程。

10/

TL;DR：

- 刚装 Codex，先让它读项目，不要急着改
- 提需求时给目标、上下文、约束、完成标准
- 复杂任务先计划，再小步实现
- 每次改完都要跑测试、看浏览器、Review diff
- 重复工作沉淀到 AGENTS.md、Skills 和 Automations

Codex 不是许愿机。

它更像一个需要你会管理的 AI 同事。

如果你也刚开始用 Codex，评论区可以说一个你最想让它帮你做的重复工作。

## 单条短帖版本

刚装 Codex 桌面版，别先学按钮。

先学工作流：

读项目 -> 做计划 -> 小步修改 -> 跑测试 -> 看浏览器 -> Review diff -> 留评论 -> 再修一轮 -> 沉淀 AGENTS.md / Skills / Automations。

Codex 不是许愿机。

它更像一个需要你会管理的 AI 同事。

## 配图建议

已生成 3 张原创配图：

1. 标题图：`assets/codex-new-user/01-title-5x2.png`
2. 工作流图：`assets/codex-new-user/02-workflow.png`
3. 对比图：`assets/codex-new-user/03-compare.png`

建议发布位置：

- 第 1 条：标题图
- 第 6 条：工作流图
- 第 8 条：对比图

## 来源链接建议

不要把链接放在 Thread 中间，建议放末条评论或文章尾部：

- OpenAI Codex 官方文档：https://developers.openai.com/codex/
- OpenAI Codex app features：https://developers.openai.com/codex/app/features
- OpenAI Codex best practices：https://developers.openai.com/codex/learn/best-practices
- Axios: https://www.axios.com/2026/06/25/codex-agents-growth-openai
- Business Insider: https://www.businessinsider.com/what-are-loops-ai-engineering-tips-2026-6
- arXiv AGENTS.md paper: https://arxiv.org/abs/2601.20404
