from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

RED = "#e90018"
BLACK = "#08080a"
INK = "#151515"
CREAM = "#f7f2e8"
WHITE = "#ffffff"
GRAY = "#6e6e6e"
YELLOW = "#ffd84d"


def font(size, bold=True):
    candidates = []
    if bold:
        candidates += [
            "C:/Windows/Fonts/msyhbd.ttc",
            "C:/Windows/Fonts/simhei.ttf",
            "C:/Windows/Fonts/NotoSansSC-Bold.otf",
        ]
    candidates += [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simsun.ttc",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            pass
    return ImageFont.load_default()


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def bg(draw, w, h, seed=1):
    random.seed(seed)
    draw.rectangle([0, 0, w, h], fill=CREAM)
    for _ in range(260):
        x, y = random.randint(0, w), random.randint(0, h)
        draw.point((x, y), fill=(0, 0, 0, random.randint(18, 45)))
    for i in range(-4, 8):
        y = int(h * 0.1 + i * 58)
        draw.line([(0, y), (w, y + 45)], fill="#ece4d6", width=2)


def brush(draw, pts, color=RED, width=46):
    for offset in range(-2, 3):
        p = [(x, y + offset * 5) for x, y in pts]
        draw.line(p, fill=color, width=max(2, width - abs(offset) * 8), joint="curve")


def rounded(draw, box, radius=24, fill=WHITE, outline=BLACK, width=4):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def shadow_card(img, box, radius=26, fill=WHITE, outline=BLACK, blur=16):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = box
    ld.rounded_rectangle([x1 + 12, y1 + 16, x2 + 12, y2 + 16], radius=radius, fill=(0, 0, 0, 70))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(layer)
    d = ImageDraw.Draw(img)
    rounded(d, box, radius=radius, fill=fill, outline=outline, width=4)


def label(draw, box, text, fill=RED, fg=WHITE):
    rounded(draw, box, radius=18, fill=fill, outline=BLACK, width=4)
    f = font(34, True)
    tw, th = text_size(draw, text, f)
    x1, y1, x2, y2 = box
    draw.text(((x1 + x2 - tw) / 2, (y1 + y2 - th) / 2 - 3), text, font=f, fill=fg)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for ch in text:
        if ch == "\n":
            lines.append(cur)
            cur = ""
            continue
        test = cur + ch
        if text_size(draw, test, fnt)[0] <= width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill=INK, width=420, gap=10):
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        _, th = text_size(draw, line, fnt)
        y += th + gap
    return y


def waveform(draw, x, y, w, h, color=RED):
    mid = y + h // 2
    step = max(8, w // 52)
    pts = []
    for i in range(0, w, step):
        amp = math.sin(i / 38) * 0.38 + math.sin(i / 17) * 0.22
        yy = mid + int(amp * h)
        pts.append((x + i, yy))
    draw.line(pts, fill=color, width=8)
    draw.line([(x, mid), (x + w, mid)], fill="#222222", width=2)


def draw_corner_marks(draw, box, color=RED, length=72, width=10):
    x1, y1, x2, y2 = box
    for pts in [
        [(x1, y1 + length), (x1, y1), (x1 + length, y1)],
        [(x2 - length, y1), (x2, y1), (x2, y1 + length)],
        [(x1, y2 - length), (x1, y2), (x1 + length, y2)],
        [(x2 - length, y2), (x2, y2), (x2, y2 - length)],
    ]:
        draw.line(pts, fill=color, width=width)


def render_title():
    w, h = 2500, 1000
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    bg(draw, w, h, 31)
    draw.polygon([(1550, 0), (2500, 0), (2500, h), (1650, h), (1760, 590)], fill=RED)
    brush(draw, [(0, 865), (620, 800), (1230, 860), (1710, 820)], width=76)
    draw_corner_marks(draw, (90, 112, 1455, 742), length=88, width=13)

    draw.text((155, 132), "AI写歌", font=font(220, True), fill=RED)
    draw.text((168, 398), "赚钱", font=font(190, True), fill=BLACK)
    draw.text((170, 615), "别先发歌，先做系统", font=font(74, True), fill=BLACK)
    draw.line((170, 715, 1050, 715), fill=RED, width=15)
    label(draw, (170, 780, 1010, 880), "定制音乐  |  素材包  |  自动化工具", fill=WHITE, fg=BLACK)

    shadow_card(img, (1580, 128, 2325, 842), radius=38, fill="#fff8f8", outline=BLACK, blur=18)
    draw = ImageDraw.Draw(img)
    draw.text((1660, 200), "声音生产系统", font=font(70, True), fill=BLACK)
    draw.line((1660, 300, 2235, 300), fill=RED, width=10)
    waveform(draw, 1668, 350, 560, 120, RED)
    steps = ["需求", "生成", "审听", "授权", "交付"]
    x = 1660
    y = 535
    for i, step in enumerate(steps):
        draw.rounded_rectangle((x, y, x + 102, y + 76), radius=18, fill=BLACK if i % 2 else RED)
        tw, th = text_size(draw, step, font(34, True))
        draw.text((x + (102 - tw) / 2, y + (76 - th) / 2 - 3), step, font=font(34, True), fill=WHITE)
        if i < len(steps) - 1:
            draw.line((x + 110, y + 38, x + 150, y + 38), fill=BLACK, width=5)
            draw.polygon([(x + 150, y + 38), (x + 132, y + 27), (x + 132, y + 49)], fill=BLACK)
        x += 150
    draw.rounded_rectangle((1660, 675, 2220, 770), radius=20, fill=WHITE, outline=BLACK, width=3)
    draw.text((1690, 700), "程序员优势：流程 + 脚本 + 交付", font=font(38, True), fill=BLACK)
    img.convert("RGB").save(ASSETS / "01-title-5x2.png", quality=95)


def render_product_ladder():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    bg(draw, w, h, 32)
    draw.text((70, 60), "5 条变现路径", font=font(86, True), fill=BLACK)
    draw.text((70, 158), "别卖生成次数，卖交付价值", font=font(38, False), fill=GRAY)
    brush(draw, [(72, 225), (530, 207), (970, 230), (1460, 210)], width=16)
    items = [
        ("01", "垂直定制", "播客片头 / 游戏BGM / 课程音乐"),
        ("02", "素材包", "转场音 / 提示音 / 短视频BGM"),
        ("03", "工作流", "Prompt / 风格表 / 授权记录"),
        ("04", "自动化工具", "批量整理 / 标签 / 交付清单"),
        ("05", "B端资产库", "品牌声音规范 + 维护"),
    ]
    x = 85
    for idx, title, desc in items:
        shadow_card(img, (x, 322, x + 265, 735), radius=28, fill=WHITE, outline=BLACK, blur=12)
        draw = ImageDraw.Draw(img)
        draw.text((x + 28, 352), idx, font=font(72, True), fill=RED)
        draw.text((x + 28, 458), title, font=font(43, True), fill=BLACK)
        draw_wrapped(draw, (x + 28, 535), desc, font(29, False), fill=GRAY, width=205, gap=8)
        x += 294
    label(draw, (86, 782, 675, 846), "主线：从一首歌升级成系统", fill=RED, fg=WHITE)
    img.convert("RGB").save(ASSETS / "02-product-ladder.png", quality=95)


def render_workflow():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    bg(draw, w, h, 33)
    draw.text((74, 58), "AI 写歌工作流", font=font(84, True), fill=BLACK)
    draw.text((76, 158), "生成只是毛坯，交付才是产品", font=font(38, False), fill=GRAY)
    label(draw, (1030, 74, 1455, 142), "程序员负责系统化", fill=RED, fg=WHITE)

    steps = [
        ("需求", "场景 / 时长 / 商用"),
        ("歌词", "钩子 / 结构 / 禁用词"),
        ("生成", "多风格 / 多版本"),
        ("审听", "记忆点 / 人声 / 循环"),
        ("后期", "裁剪 / 音量 / 格式"),
        ("交付", "授权 / 文件库 / 说明"),
    ]
    positions = [(95, 300), (545, 300), (995, 300), (95, 575), (545, 575), (995, 575)]
    for i, ((title, desc), (x, y)) in enumerate(zip(steps, positions), start=1):
        shadow_card(img, (x, y, x + 390, y + 175), radius=24, fill=WHITE, outline=BLACK, blur=10)
        draw = ImageDraw.Draw(img)
        draw.ellipse((x + 25, y + 27, x + 88, y + 90), fill=RED)
        draw.text((x + 45, y + 34), str(i), font=font(35, True), fill=WHITE)
        draw.text((x + 112, y + 28), title, font=font(48, True), fill=BLACK)
        draw.text((x + 36, y + 112), desc, font=font(31, False), fill=GRAY)
    brush(draw, [(90, 248), (450, 232), (850, 248), (1450, 232)], width=14)
    img.convert("RGB").save(ASSETS / "03-workflow.png", quality=95)


def render_risk_boundary():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), CREAM)
    draw = ImageDraw.Draw(img)
    bg(draw, w, h, 34)
    draw.text((72, 58), "4 个坑先避开", font=font(86, True), fill=BLACK)
    draw.text((74, 160), "音乐生意最怕不是难听，是不能用", font=font(38, False), fill=GRAY)
    draw.line((72, 232, 790, 232), fill=RED, width=14)

    items = [
        ("免费商用", "别靠印象，看当前工具条款"),
        ("纯AI版权", "保留人工选择、编排、后期证据"),
        ("刷播放", "别买播放，别制造虚假互动"),
        ("授权缺失", "范围、平台、独占、署名写清楚"),
    ]
    positions = [(92, 310), (850, 310), (92, 585), (850, 585)]
    for i, ((title, desc), (x, y)) in enumerate(zip(items, positions), start=1):
        shadow_card(img, (x, y, x + 620, y + 190), radius=26, fill="#fff8f8" if i % 2 else WHITE, outline=BLACK, blur=10)
        draw = ImageDraw.Draw(img)
        draw.text((x + 35, y + 35), f"0{i}", font=font(60, True), fill=RED)
        draw.text((x + 150, y + 42), title, font=font(50, True), fill=BLACK)
        draw.text((x + 38, y + 118), desc, font=font(32, False), fill=GRAY)
    label(draw, (980, 80, 1450, 148), "赚钱前先留证据链", fill=BLACK, fg=WHITE)
    img.convert("RGB").save(ASSETS / "04-risk-boundary.png", quality=95)


def main():
    render_title()
    render_product_ladder()
    render_workflow()
    render_risk_boundary()
    for file in sorted(ASSETS.glob("*.png")):
        print(file)


if __name__ == "__main__":
    main()
