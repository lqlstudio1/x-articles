# 资料边界

## 原始素材

- 用户提供的文本：推荐使用 Codex 定时任务，每天早上 8 点自动产出美股财经日报，并给出日报 Prompt 框架。

## 官方资料核对

本次涉及 OpenAI Codex 产品能力，已使用本地拉取的 OpenAI Codex Manual 核对。

Manual path:

```text
C:\Users\admin\AppData\Local\Temp\openai-docs-cache\codex-manual.md
```

相关章节：

- `Codex Pricing`：manual lines 39-135。Plus 计划显示为 `$20 /month`，Business 显示为 `$20 / user / month*`，API Key 模式适合 CI 等共享环境自动化，但没有云端功能。
- `Agent internet access`：manual lines 4335-4476。Codex 默认在 agent phase 阻止互联网访问；需要时可按环境开启，并建议限制域名和 HTTP 方法。
- `Automations`：manual lines 4477-4612。Codex 支持后台 recurring tasks，结果进入 Triage / inbox；standalone automation 适合独立定时运行；thread automation 适合保留同一线程上下文；设置前建议先在普通 thread 测试 prompt。

官方页面：

- `https://developers.openai.com/codex/pricing`
- `https://developers.openai.com/codex/cloud/internet-access`
- `https://developers.openai.com/codex/app/automations`

## 写作边界

- 文章没有把日报输出写成投资建议。
- 没有承诺自动化结果一定准确。
- 没有鼓励自动交易。
- 明确要求关键数据给来源，拿不到数据写“暂无可靠数据”。
- 文章里的 `$20/月` 只作为官方 manual 当前显示的 Plus 定价背景，不作为长期价格承诺。
