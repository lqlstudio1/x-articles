# 配图使用说明

## 图片清单

1. `assets/01-title-5x2.png`
   - 用途：X 文章标题图 / 封面图
   - 尺寸：2500 x 1000
   - 比例：5:2
   - 建议作为第一张图

2. `assets/02-incentive-map.png`
   - 用途：正文插图 1
   - 建议位置：放在“算法真正该优化的，不是推荐参数，而是内容激励”附近
   - 作用：说明算法奖励什么，创作者就会生产什么

3. `assets/03-two-feeds.png`
   - 用途：正文插图 2
   - 建议位置：放在“关注流应该彻底还给用户和创作者”附近
   - 作用：解释推荐流和关注流应该分工

4. `assets/04-creator-trust.png`
   - 用途：正文插图 3
   - 建议位置：放在“算法要可解释 / 风控要精细化”附近
   - 作用：强调透明、申诉、衰减和真人互动识别

## 优先发布组合

如果只发 2 张图：

1. `01-title-5x2.png`
2. `02-incentive-map.png`

如果发完整图组：

1. `01-title-5x2.png`
2. `02-incentive-map.png`
3. `03-two-feeds.png`
4. `04-creator-trust.png`

## 重新生成

```powershell
& 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'F:\code\x文章\2026-06-29\x-algorithm-optimization\tools\render_x_algorithm_cards.py'
```
