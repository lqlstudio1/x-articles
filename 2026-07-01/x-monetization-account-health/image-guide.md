# 配图使用说明

## 封面锚点方案

```text
模板类型：冲突型
一眼承诺：收益化前，别让账号行为像机器人
视觉锚点：超大标题“别像机器人” + 右侧风险卡片
锚点位置：左侧 55% 主标题，右侧 45% 手机/风险卡片
文字层级：主标题 70%，副标题 20%，底部标签 10%
```

## 图片清单

1. `assets/01-title-5x2.png`
   - 用途：X 文章标题图 / 封面图
   - 尺寸：2500 x 1000
   - 比例：5:2
   - 建议作为第一张图

2. `assets/02-risk-behaviors.png`
   - 用途：正文插图 1
   - 建议位置：放在“账号行为越来越像机器人”附近
   - 作用：把风险行为压缩成 4 类

3. `assets/03-human-comment.png`
   - 用途：正文插图 2
   - 建议位置：放在“评论要像人，不要像任务”附近
   - 作用：说明高质量评论的构成

4. `assets/04-asset-vs-drain.png`
   - 用途：正文插图 3
   - 建议位置：放在“资产动作 / 消耗动作”附近
   - 作用：区分长期账号信用和短期消耗动作

## 优先发布组合

如果只发 2 张图：

1. `01-title-5x2.png`
2. `02-risk-behaviors.png`

如果发完整图组：

1. `01-title-5x2.png`
2. `02-risk-behaviors.png`
3. `03-human-comment.png`
4. `04-asset-vs-drain.png`

## 重新生成

```powershell
python 'F:\code\x文章\2026-07-01\x-monetization-account-health\tools\render_account_health_cards.py'
```
