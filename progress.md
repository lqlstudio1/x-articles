# 项目进度

## 2026-06-28

### 范围

建立 X 文章工作区的长期协作工件规则。

### 已完成

- 新增五个根目录协作工件：
  - `AGENTS.md`
  - `progress.md`
  - `knowledge_map.md`
  - `daily_task.md`
  - `mistakes.md`
- 将“项目协作工件规则”写入 `AGENTS.md`。
- 保留现有写作规则文件：
  - `WRITING_STYLE.md`
  - `ACCOUNT_STRATEGY.md`
- 已形成默认文章交付规则：正文、短版、标题图、正文配图、配图说明、生成脚本和 README 索引。

### 验证结果

- 已确认五个协作工件此前不存在，本次已创建。
- 已按当前项目职责初始化内容。

### 剩余风险

- 部分历史文章还没有补齐所有配图说明或脚本，需要后续按目录逐篇检查。
- 当前工作区有终端中文显示乱码现象，不影响文件内容，但查看命令输出时需要注意编码。

## 2026-06-28

### 范围

更新 `AGENTS.md`，加入 X 增长与 @superfang119 账号策略的长期规则。

### 已完成

- 将账号基础资产规则写入 `AGENTS.md`：Bio、Pinned post、头像/横幅。
- 将内容优先级写入 `AGENTS.md`：工具对比 Thread、完整工作流 Thread、Prompt + 案例拆解、想法到作品、单帖实测。
- 将双主线比例写入 `AGENTS.md`：70% AI 编程/自动化，30% AI 自媒体创作。
- 将三个固定 Thread 模板写入 `AGENTS.md`：工具对比、Codex 工作流、案例复盘。
- 将发帖节奏、战略回复、置顶策略和复盘指标写入 `AGENTS.md`。

### 验证结果

- 已按长期规则形式整理，没有把原始长文整段粘贴进 `AGENTS.md`。
- 已保留合规边界：不鼓励刷量、互赞互粉或把未经证实的算法说法写成确定事实。

### 剩余风险

- 具体发布时间和内容表现仍需根据 X Analytics / 实际发布数据复盘调整。

## 2026-06-29

### 范围

改编 Codex 定时任务自动生成美股日报内容，形成可发布的 X 文章和配套视觉素材。

### 已完成

- 新增专题目录：`2026-06-29/codex-automation-us-stock-daily/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 97 字。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-daily-workflow.png`
  - `assets/03-prompt-guardrails.png`
  - `assets/04-not-investment-advice.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_codex_automation_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已依据 OpenAI Codex 官方手册核对定时任务、联网访问和套餐价格相关边界。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图片 5:2 比例建议。
- 已检查 3 张正文配图尺寸为 1600x900。
- 已检查短版字数为 97 字。

### 剩余风险

- Codex 套餐价格、定时任务能力和联网访问规则后续可能变化，发布前如强调“最新”需重新核对官方文档。
- 美股日报质量取决于可访问的数据源和来源标注，不能把日报写成投资建议、交易信号或收益承诺。

## 2026-06-29

### 范围

改写 X 平台算法 10 条优化建议，形成可发布的观点文章、Thread 拆条版和配套视觉素材。

### 已完成

- 新增专题目录：`2026-06-29/x-algorithm-optimization/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 68 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-incentive-map.png`
  - `assets/03-two-feeds.png`
  - `assets/04-creator-trust.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_x_algorithm_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已将原始清单改成“平台产品建议”口吻，没有把未经验证的 X 算法权重写成事实。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图片 5:2 比例建议。
- 已检查 3 张正文配图尺寸为 1600x900。
- 已检查短版字数为 68 字。

### 剩余风险

- 本文是观点文，不是 X 当前算法机制报告；如要写成事实分析，需要另行检索官方文档、公开源码、工程团队说明和创作者实测数据。
- 发布后需观察评论区是否会引发过度对线，必要时把 CTA 引导到“最该先改哪条”这类具体讨论。

## 2026-06-29

### 范围

将“投资盈利属于偏财，是否必须花出去”改写为结合 Codex 的盈利分流和复盘工作流文章。

### 已完成

- 新增专题目录：`2026-06-29/codex-investment-profit-allocation/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 70 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-three-way-split.png`
  - `assets/03-codex-workflow.png`
  - `assets/04-boundary.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_profit_allocation_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已将“必须花出去”的绝对表达改为“必须分流”，避免鼓励挥霍。
- 已明确 Codex 只做记录、分类、复盘和风险提醒，不做荐股、收益预测或自动交易。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图片 5:2 比例建议。
- 已检查 3 张正文配图尺寸为 1600x900。
- 已检查短版字数为 70 字。

### 剩余风险

- 本文包含命理概念和投资场景，发布时需要保留“非投资建议、非命理咨询”的边界。
- `30% / 40% / 30%` 只是示例分流框架，不能暗示适用于所有投资者。

## 2026-06-30

### 范围

沉淀新的标题图视觉参考风格。

### 已完成

- 保存用户提供的参考图到：`references/visual-style/xiaohongshu-cover-high-impact-reference.png`。
- 新增视觉参考说明：`references/visual-style/README.md`。
- 更新 `WRITING_STYLE.md`，加入红黑白高冲击封面风格规则。
- 更新 `README.md` 和 `knowledge_map.md`，登记视觉参考目录。

### 验证结果

- 已目检参考图，提炼为构图、颜色、字体、元素和使用边界。
- 已明确后续只参考风格语言，不复制原图内容、版式细节或具体素材。

### 剩余风险

- 这种风格冲击力强但噪音也高，不适合所有正文解释图；后续应按主题在深色科技风和红黑白封面风之间选择。

## 2026-06-30

### 范围

学习 GitHub 仓库 `ponyodong2026/ponyo-cover-anchor-system`，并将其封面锚点方法适配到本工作区的 X 标题图规则。

### 已完成

- 读取 GitHub 仓库公开内容：
  - `README.md`
  - `cover-anchor-system/SKILL.md`
  - `references/template-formulas.md`
  - `references/cover-diagnosis-checklist.md`
  - `references/finished-cover-prompts.md`
  - `references/doodle-outline-fresh-style.md`
  - `references/sunlit-scrapbook-cutout-style.md`
- 新增本地学习笔记：`references/visual-style/ponyo-cover-anchor-system-notes.md`。
- 更新 `WRITING_STYLE.md`，加入“信息密度 × 视觉锚点”、模板选择、5:2 适配、80px 缩略图测试。
- 更新 `AGENTS.md`，把标题图封面锚点规则设为长期生成规则。
- 更新 `README.md`、`knowledge_map.md` 和 `references/visual-style/README.md`。

### 验证结果

- 已确认 GitHub 仓库公开可访问，默认分支 HEAD 为 `f03b7bc8c751e8b5e2e9ead66fd9aa16def22b84`。
- 已将原 skill 的小红书 3:4 规则转译为当前 X 文章常用的 5:2 标题图规则。
- 已明确不复制第三方示例图、Logo、水印或具体素材，只吸收方法论和诊断框架。

### 剩余风险

- 该仓库当前未显示 license 信息，后续只使用总结后的方法规则，不搬运原文模板或示例图。
- 如果后续要把它安装成全局 Codex skill，需要用户明确授权后再复制到本机 skills 目录。

## 2026-07-01

### 范围

将用户提供的 X 收益化暂停风险提醒改写为“账号健康与真实互动”主题文章，并生成封面锚点式配图。

### 已完成

- 新增专题目录：`2026-07-01/x-monetization-account-health/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 74 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-risk-behaviors.png`
  - `assets/03-human-comment.png`
  - `assets/04-asset-vs-drain.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_account_health_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已将原文的频率数字弱化为账号健康原则，没有把任何互动次数写成“安全阈值”。
- 已避免提供规避平台风控的方法，重点改为真实互动、原创素材、减少重复和避免平台操纵行为。
- 已使用封面锚点系统：冲突型模板，一眼承诺为“收益化前别让账号像机器人”，视觉锚点为超大标题和风险卡片。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图片 5:2 比例建议。
- 已检查 3 张正文配图尺寸为 1600x900。
- 已检查短版字数为 74 字。

### 剩余风险

- 本文未核验 X 当前官方收益化政策或风控阈值，不能作为官方规则说明。
- 发布时需继续避免读者把文章理解为“卡阈值规避风控”，CTA 应引导讨论账号健康和原创内容。

## 2026-07-01

### 范围

基于用户原始收益化风险提醒，制作升级版文章：从普通账号健康提醒升级为“账号信用系统 + 官方 Authenticity 边界 + Codex 周复盘”。

### 已完成

- 新增专题目录：`2026-07-01/x-monetization-account-health-upgrade/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 73 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-four-risk-accounts.png`
  - `assets/03-health-system.png`
  - `assets/04-codex-checklist.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_account_health_upgrade_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已核对 X 官方 Help Center Authenticity 页面，并在 `source-notes.md` 记录边界。
- 已将原文的频率数字改成账号信用原则，没有把任何互动次数写成“安全阈值”。
- 已明确 Codex 只用于周复盘、素材整理、风险检查和规则维护，不用于批量互动。
- 已使用封面锚点系统：冲突型 + 截图型，一眼承诺为“收益化前先维护账号信用”，视觉锚点为“账号信用”大标题和自检面板。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图片 5:2 比例建议。
- 已检查 3 张正文配图尺寸为 1600x900。
- 已检查短版字数为 73 字。

### 剩余风险

- X 官方规则和收益化政策可能变化；若发布时强调“最新规则”，需要重新核对官方页面。
- 文章应避免让读者理解成规避风控教程，发布文案应突出“真实创作、原创素材、账号信用”。

## 2026-07-02

### 范围

将用户提供的 GEO 草稿改写为可发布的 X 专题文章，并生成配套标题图、正文配图、资料边界和复用脚本。

### 已完成

- 新增专题目录：`2026-07-02/geo-ai-answer-position/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 83 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-geo-workflow.png`
  - `assets/03-ai-readable-content.png`
  - `assets/04-ai-friendly-page.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_geo_cards.py`。
- 更新 `README.md` 和 `knowledge_map.md`。

### 验证结果

- 已核对 Google Search Central 的 AI features 文档边界：基础 SEO 仍然有效，没有额外技术要求，也不要求特殊 AI 文件或特殊 schema。
- 已将 `/.well-known/ai.json` 写成可选工程化信息档案思路，没有写成官方标准或保证推荐方法。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图 5:2 比例建议。
- 已检查 3 张正文配图尺寸均为 1600x900。
- 已检查短版字数为 83 字。

### 剩余风险

- GEO 属于快速变化的话题，发布时如果使用“最新”或“官方”字样，需要重新核对 Google、Bing、国内 AI 搜索和目标平台公开文档。
- AI 对品牌的回答会随模型、检索源和时间变化，文章中的“AI 体检”应作为周期性审计方法，而不是排名承诺。

## 2026-07-02

### 范围

重新学习 GitHub 仓库 `ponyodong2026/ponyo-cover-anchor-system`，并把它转成后续绘制图片时默认执行的规则。

### 已完成

- 核对仓库公开内容，当前 `main` HEAD 为 `f03b7bc8c751e8b5e2e9ead66fd9aa16def22b84`。
- 读取并吸收：
  - `README.md`
  - `cover-anchor-system/SKILL.md`
  - `references/template-formulas.md`
  - `references/finished-cover-prompts.md`
  - `references/cover-diagnosis-checklist.md`
  - `references/doodle-outline-fresh-style.md`
  - `references/sunlit-scrapbook-cutout-style.md`
- 新增绘图执行规则：`references/visual-style/ponyo-cover-anchor-drawing-rules.md`。
- 更新 `AGENTS.md` 和 `knowledge_map.md`。

### 验证结果

- 已明确默认行为：生成完整成品封面，不生成空背景，除非用户明确要求。
- 已把原仓库偏小红书 3:4 的规则适配为本工作区常用 X 文章 5:2 标题图规则。
- 已保留边界：不复制第三方示例图、不硬塞 `波妞` / `PONYO` / 水印、不伪造 Logo、收益、二维码或平台数据。

### 剩余风险

- 该仓库未作为全局 Codex skill 安装；当前是项目级学习规则。如后续需要全局调用，需要用户明确要求安装。
- GitHub 仓库后续可能更新；如果用户要求“最新版本”，需要重新核对远端。

## 2026-07-02

### 范围

撰写“程序员如何靠 AI 写歌赚钱”专题文章，并生成配套标题图、正文配图、资料边界和复用脚本。

### 已完成

- 新增专题目录：`2026-07-02/ai-song-programmer-monetization/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 75 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-product-ladder.png`
  - `assets/03-workflow.png`
  - `assets/04-risk-boundary.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_ai_song_cards.py`。
- 更新 `README.md`、`knowledge_map.md` 和 `daily_task.md`。

### 验证结果

- 已核对 Suno、YouTube、Spotify 和美国版权局相关公开资料边界。
- 已避免把 AI 写歌写成收益保证、刷播放教程或批量低价值内容套利。
- 已生成并目检 4 张图片，标题图尺寸为 2500x1000，符合 X 文章标题图 5:2 比例建议。
- 已检查 3 张正文配图尺寸均为 1600x900。
- 已检查短版字数为 75 字。

### 剩余风险

- AI 音乐工具条款、发行平台规则和版权政策会变化；接客户商用项目前必须重新核对当前条款。
- 本文不是法律意见，涉及版权、授权和商用发行时需要按所在地区和客户使用场景单独确认。

## 2026-07-02

### 范围

更新后续 X 文章配图交付规则：正文里必须标出每张图片在文章中的插入位置。

### 已完成

- 更新 `AGENTS.md`：默认交付物新增“正文中明确标出每张图片插入位置”。
- 更新 `AGENTS.md` 验证标准：交付前检查正文是否已标出标题图和正文配图位置。
- 更新 `WRITING_STYLE.md`：固定交付物新增正文位置标记格式。

### 验证结果

- 后续文章默认不只在 `image-guide.md` 写推荐位置，也要在 `article.md` 正文中直接标注。
- 推荐格式：`配图位置：插入 assets/xx.png`。

### 剩余风险

- 早期已经完成的文章不一定都有正文内配图位置标记，后续如重新整理历史文章需要逐篇补齐。

## 2026-07-02

### 范围

学习用户提供的多风格封面参考图，更新后续图片生成规则，避免标题图长期使用单一视觉风格。

### 已完成

- 保存参考图：`references/visual-style/multi-cover-style-board-reference.png`。
- 新增学习笔记：`references/visual-style/multi-cover-style-board-notes.md`。
- 更新 `AGENTS.md`：加入视觉风格轮换规则。
- 更新 `WRITING_STYLE.md`：加入“视觉风格不要单一化”规则。
- 更新 `knowledge_map.md`：登记多风格封面参考板。

### 验证结果

- 已将参考图拆分为 12 类风格：冲突人像、粗字冲击、改前 VS 改后、巨型数字、纸感清单、霓虹科技、手机截图测评、评论反馈截图、数据结果面板、情绪人像、夜间生活方式、治愈极简。
- 已明确后续出图先按内容类型选风格，连续 3 篇文章标题图尽量不重复同一模板。

### 剩余风险

- 风格多样化不能牺牲缩略图可读性；标题图仍需通过 80px 缩略图判断。

## 2026-07-02

### 范围

更新图片生成规则：后续配图不能全是文字卡片，要结合文章内容加入场景、人物、物体或界面。

### 已完成

- 更新 `AGENTS.md`：绘图执行补充中加入“图片不能只堆文字”的规则。
- 更新 `AGENTS.md`：视觉风格轮换规则中加入“每篇文章至少一张图应有场景感或实物感”。
- 更新 `WRITING_STYLE.md`：固定交付物新增“场景化画面”。
- 更新 `WRITING_STYLE.md`：补充不同主题对应的场景锚点。
- 更新 `references/visual-style/multi-cover-style-board-notes.md`：新增场景锚点参考和禁区。

### 验证结果

- 后续文章标题图和正文图默认采用“文字结论 + 场景锚点”的组合。
- 可选锚点包括人物、物体、设备、桌面、手机、代码界面、工具界面、数据面板、工作现场或生活场景。

### 剩余风险

- 场景化不能变成无关装饰；场景必须服务文章主题和读者理解。

## 2026-07-02

### 范围

改写“到底要不要人工审阅 AI 生成的代码”观点文，产出适合 X 发布的 AI Coding 专题文章，并生成配套标题图、正文配图、资料边界和可复用脚本。

### 已完成

- 新增专题目录：`2026-07-02/ai-code-review-human-architecture/`。
- 完成正式文章：`article.md`。
- 完成 140 字以内短版，当前 104 字。
- 完成 Thread 拆条版，当前 12 条。
- 完成资料边界说明：`source-notes.md`。
- 完成标题图和 3 张正文配图：
  - `assets/01-title-5x2.png`
  - `assets/02-review-layers.png`
  - `assets/03-architecture-lens.png`
  - `assets/04-design-memory.png`
- 完成配图说明：`image-guide.md`。
- 完成可复用配图生成脚本：`tools/render_ai_code_review_cards.py`。
- 更新 `README.md`、`knowledge_map.md` 和 `daily_task.md`。

### 验证结果

- 已检查标题图尺寸为 2500x1000，符合 X 标题图 5:2 比例建议。
- 已检查 3 张正文配图尺寸均为 1600x900。
- 已检查短版字数为 104 字。
- 已目检标题图和正文图，确认非空白、文字清晰，并包含代码窗口、架构图、开发者桌面和设计记忆文档等场景锚点。
- 本文未联网搜索，已在 `source-notes.md` 说明为用户观点改写和工程实践判断。

### 剩余风险

- 本文属于工程方法论，不替代团队安全审计、合规审计或高风险系统专项评审。
- 如果发布后评论区集中追问具体工具链，可后续补一篇“AI code review 工作流模板”或“Codex commit message 架构摘要模板”。

## 2026-07-02

### 范围

初始化 `F:\code\x文章` 为 Git 仓库，并建立后续内容完成后必须提交到 Git 的长期规则。

### 已完成

- 新增 `.gitignore`，排除 `.codex/`、`.agents/`、`.obsidian/`、Python 缓存和系统临时文件。
- 更新 `AGENTS.md`，加入 Git 提交规则。
- 已执行 `git init`，将当前目录初始化为 Git 仓库。

### 验证结果

- 初始化前发现 `.git` 目录存在但为空，`git status` 仍提示不是 Git 仓库。
- `git init` 首次受沙箱限制无法写入 `.git/description`，已通过授权提升权限完成初始化。
- 初始提交将在本次操作中创建，并用 `git status --short` 与 `git log --oneline -1` 验证。

### 剩余风险

- 初始提交会包含当前已有文章、图片、脚本和协作工件；历史文章是否都已完全符合最新规则，需要后续逐篇补齐。
