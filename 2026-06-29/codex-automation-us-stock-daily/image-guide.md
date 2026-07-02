# 配图使用说明

## 图片清单

1. `assets/01-title-5x2.png`
   - 用途：X 文章标题图 / 封面图
   - 尺寸：2500 x 1000
   - 比例：5:2
   - 建议作为第一张图

2. `assets/02-daily-workflow.png`
   - 用途：正文插图 1
   - 建议位置：放在“这件事最适合自动化”之后
   - 作用：展示每天 8 点日报的自动化链路

3. `assets/03-prompt-guardrails.png`
   - 用途：正文插图 2
   - 建议位置：放在“Prompt 里至少写清楚 7 件事”之前
   - 作用：强调来源、反幻觉、结构和免责声明

4. `assets/04-not-investment-advice.png`
   - 用途：正文插图 3
   - 建议位置：放在“这不是投资建议”附近
   - 作用：明确边界，避免读者误解为自动交易信号

## 优先发布组合

如果只发 2 张图：

1. `01-title-5x2.png`
2. `02-daily-workflow.png`

如果发完整图组：

1. `01-title-5x2.png`
2. `02-daily-workflow.png`
3. `03-prompt-guardrails.png`
4. `04-not-investment-advice.png`

## 重新生成

```powershell
& 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'F:\code\x文章\2026-06-29\codex-automation-us-stock-daily\tools\render_codex_automation_cards.py'
```
