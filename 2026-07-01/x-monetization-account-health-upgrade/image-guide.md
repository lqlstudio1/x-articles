# 配图使用说明

## 封面锚点方案

```text
模板类型：冲突型 + 截图型
一眼承诺：收益化前先维护账号信用
视觉锚点：超大标题“账号信用” + 右侧健康检查面板
锚点位置：左侧 55% 主标题，右侧 45% 风险面板
文字层级：主标题 70%，副标题 20%，标签/角标 10%
```

## 图片清单

1. `assets/01-title-5x2.png`
   - 用途：X 文章标题图 / 封面图
   - 尺寸：2500 x 1000
   - 比例：5:2
   - 建议作为第一张图

2. `assets/02-four-risk-accounts.png`
   - 用途：正文插图 1
   - 建议位置：放在“我把高风险账号分成 4 类”附近
   - 作用：概括动作像脚本、评论像垃圾信息、关系像互刷网络、素材像搬运号

3. `assets/03-health-system.png`
   - 用途：正文插图 2
   - 建议位置：放在“建立一套账号健康系统”附近
   - 作用：展示质量互动、原创素材、垂直曝光、每周自检

4. `assets/04-codex-checklist.png`
   - 用途：正文插图 3
   - 建议位置：放在“如果你用 Codex”附近
   - 作用：展示 Codex 只做复盘、素材、风险、下周计划

## 优先发布组合

如果只发 2 张图：

1. `01-title-5x2.png`
2. `02-four-risk-accounts.png`

如果发完整图组：

1. `01-title-5x2.png`
2. `02-four-risk-accounts.png`
3. `03-health-system.png`
4. `04-codex-checklist.png`

## 重新生成

```powershell
python 'F:\code\x文章\2026-07-01\x-monetization-account-health-upgrade\tools\render_account_health_upgrade_cards.py'
```
