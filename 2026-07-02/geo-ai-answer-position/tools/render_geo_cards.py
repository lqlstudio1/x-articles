from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

RED = "#e90018"
BLACK = "#0b0b0d"
INK = "#171717"
CREAM = "#fffaf0"
PAPER = "#f7f3ea"
GRAY = "#6b6b6b"
LIGHT = "#ffffff"


def font(size, bold=True):
    candidates = []
    if bold:
        candidates.extend([
            "C:/Windows/Fonts/msyhbd.ttc",
            "C:/Windows/Fonts/simhei.ttf",
            "C:/Windows/Fonts/NotoSansSC-Bold.otf",
        ])
    candidates.extend([
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simsun.ttc",
        "C:/Windows/Fonts/arial.ttf",
    ])
    for item in candidates:
        try:
            return ImageFont.truetype(item, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_box(draw, text, fnt):
    return draw.textbbox((0, 0), text, font=fnt)


def text_size(draw, text, fnt):
    box = text_box(draw, text, fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_bg(draw, w, h, seed=0):
    random.seed(seed)
    draw.rectangle([0, 0, w, h], fill=PAPER)
    for _ in range(240):
        x = random.randint(0, w)
        y = random.randint(0, h)
        a = random.randint(18, 42)
        draw.point((x, y), fill=(0, 0, 0, a))
    for i in range(-3, 5):
        y = int(h * 0.18 + i * 62)
        draw.line([(0, y), (w, y + 55)], fill="#eee7da", width=2)


def draw_brush(draw, points, color=RED, width=46):
    for offset in range(-2, 3):
        shifted = [(x, y + offset * 5) for x, y in points]
        draw.line(shifted, fill=color, width=max(1, width - abs(offset) * 8), joint="curve")


def draw_corner_marks(draw, box, color=RED, length=72, width=10):
    x1, y1, x2, y2 = box
    marks = [
        ((x1, y1 + length), (x1, y1), (x1 + length, y1)),
        ((x2 - length, y1), (x2, y1), (x2, y1 + length)),
        ((x1, y2 - length), (x1, y2), (x1 + length, y2)),
        ((x2 - length, y2), (x2, y2), (x2, y2 - length)),
    ]
    for a, b, c in marks:
        draw.line([a, b, c], fill=color, width=width)


def wrap_text(draw, text, fnt, max_width):
    lines = []
    current = ""
    for ch in text:
        trial = current + ch
        if ch == "\n":
            lines.append(current)
            current = ""
            continue
        if text_size(draw, trial, fnt)[0] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill=INK, max_width=600, line_gap=12, anchor=None):
    x, y = xy
    for line in wrap_text(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill, anchor=anchor)
        _, h = text_size(draw, line, fnt)
        y += h + line_gap
    return y


def rounded(draw, box, radius=28, fill=LIGHT, outline=None, width=3):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def shadow_card(base, box, radius=28, fill=LIGHT, outline="#111111", shadow="#000000", offset=(12, 16), blur=18):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    sx1, sy1, sx2, sy2 = box[0] + offset[0], box[1] + offset[1], box[2] + offset[0], box[3] + offset[1]
    ld.rounded_rectangle([sx1, sy1, sx2, sy2], radius=radius, fill=shadow)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)
    draw = ImageDraw.Draw(base)
    rounded(draw, box, radius=radius, fill=fill, outline=outline, width=4)


def label(draw, box, text, fill=RED, text_fill=LIGHT):
    rounded(draw, box, radius=18, fill=fill, outline=BLACK, width=4)
    f = font(36, True)
    w, h = text_size(draw, text, f)
    x1, y1, x2, y2 = box
    draw.text(((x1 + x2 - w) / 2, (y1 + y2 - h) / 2 - 4), text, font=f, fill=text_fill)


def render_title():
    w, h = 2500, 1000
    img = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(img)
    draw_bg(draw, w, h, 7)

    draw.polygon([(1480, 0), (2500, 0), (2500, 1000), (1580, 1000), (1690, 610)], fill="#f0182c")
    draw_brush(draw, [(1550, 155), (1880, 95), (2280, 140), (2480, 75)], color="#d70014", width=95)
    draw_brush(draw, [(0, 885), (620, 820), (1230, 880), (1700, 810)], color="#e90018", width=70)

    draw_corner_marks(draw, (105, 120, 1460, 740), length=86, width=13)

    f_geo = font(265, True)
    f_sub = font(122, True)
    f_line = font(78, True)
    draw.text((160, 145), "GEO", font=f_geo, fill=RED, stroke_width=2, stroke_fill=RED)
    draw.text((175, 420), "不是 SEO", font=f_sub, fill=BLACK)
    draw.text((175, 570), "抢 AI 答案里的位置", font=f_line, fill=BLACK)
    draw.line((175, 674, 1040, 674), fill=RED, width=14)

    label(draw, (175, 760, 1045, 865), "AI 体检  |  信息补齐  |  结构化", fill=LIGHT, text_fill=BLACK)

    shadow_card(img, (1575, 142, 2320, 835), radius=38, fill="#fff7f7", outline=BLACK, shadow=(0, 0, 0, 90))
    draw = ImageDraw.Draw(img)
    draw.text((1660, 210), "AI答案", font=font(82, True), fill=BLACK)
    draw.text((1966, 210), "卡", font=font(82, True), fill=RED)
    draw.line((1660, 315, 2220, 315), fill=RED, width=10)
    items = [("理解你", "品牌是谁？主营什么？"), ("引用你", "事实 / 表格 / FAQ"), ("推荐你", "场景匹配 + 多源验证")]
    y = 380
    for title, desc in items:
        draw.rounded_rectangle((1660, y, 2220, y + 110), radius=22, fill=LIGHT, outline="#222222", width=3)
        draw.ellipse((1690, y + 32, 1738, y + 80), fill=RED)
        draw.text((1765, y + 22), title, font=font(48, True), fill=BLACK)
        draw.text((1965, y + 32), desc, font=font(30, False), fill=GRAY)
        y += 145

    draw.polygon([(2210, 720), (2380, 845), (2305, 875)], fill=BLACK)
    draw.polygon([(2195, 700), (2365, 825), (2290, 855)], fill=LIGHT, outline=BLACK)
    img.convert("RGB").save(ASSETS / "01-title-5x2.png", quality=95)


def render_workflow():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(img)
    draw_bg(draw, w, h, 11)
    draw.text((80, 62), "GEO 五步走", font=font(92, True), fill=BLACK)
    draw.text((80, 172), "不是一次发稿，是一套长期体检系统", font=font(38, False), fill=GRAY)
    draw_brush(draw, [(80, 240), (520, 225), (980, 246), (1450, 226)], color=RED, width=18)

    steps = [
        ("01", "AI体检", "先问模型如何理解你"),
        ("02", "信息补齐", "补事实、参数、案例、边界"),
        ("03", "结构化", "表格 / 清单 / 对比表"),
        ("04", "多源验证", "官网、内容平台、文档互证"),
        ("05", "页面可读", "能读 / 能点 / 可复现"),
    ]
    x = 95
    for idx, title, desc in steps:
        shadow_card(img, (x, 325, x + 260, 720), radius=26, fill=LIGHT, outline=BLACK, shadow=(0, 0, 0, 55), blur=12)
        draw = ImageDraw.Draw(img)
        draw.text((x + 28, 355), idx, font=font(76, True), fill=RED)
        draw.text((x + 28, 465), title, font=font(48, True), fill=BLACK)
        draw_wrapped(draw, (x + 28, 545), desc, font(30, False), fill=GRAY, max_width=200, line_gap=10)
        if idx != "05":
            draw.line((x + 268, 525, x + 324, 525), fill=RED, width=9)
            draw.polygon([(x + 324, 525), (x + 300, 508), (x + 300, 542)], fill=RED)
        x += 294

    label(draw, (86, 775, 575, 842), "主线：体检 -> 补齐 -> 引用", fill=RED, text_fill=LIGHT)
    img.convert("RGB").save(ASSETS / "02-geo-workflow.png", quality=95)


def render_readable_content():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(img)
    draw_bg(draw, w, h, 19)
    draw.text((75, 55), "AI 能引用什么？", font=font(88, True), fill=BLACK)
    draw.text((75, 158), "漂亮话不够，事实才是答案素材", font=font(39, False), fill=GRAY)

    shadow_card(img, (80, 260, 700, 780), radius=28, fill="#fff6f6", outline=BLACK, shadow=(0, 0, 0, 45))
    shadow_card(img, (900, 220, 1520, 815), radius=28, fill=LIGHT, outline=BLACK, shadow=(0, 0, 0, 60))
    draw = ImageDraw.Draw(img)
    draw.text((125, 305), "难被引用", font=font(58, True), fill=RED)
    draw.line((125, 390, 610, 390), fill=RED, width=8)
    bad = ["专注多年", "团队专业", "服务贴心", "高质量方案"]
    y = 445
    for item in bad:
        draw.text((150, y), "×", font=font(48, True), fill=RED)
        draw.text((215, y + 4), item, font=font(42, True), fill=BLACK)
        y += 78

    draw.text((950, 265), "更容易被引用", font=font(58, True), fill=BLACK)
    draw.line((950, 350, 1430, 350), fill=RED, width=8)
    good = [
        ("参数", "服务对象 / 周期 / 范围"),
        ("案例", "真实场景 + 结果"),
        ("价格", "区间 + 影响因素"),
        ("FAQ", "适合谁 / 不适合谁"),
        ("对比表", "差异、边界、选择建议"),
    ]
    y = 410
    for k, v in good:
        draw.rounded_rectangle((950, y, 1435, y + 66), radius=16, fill="#fff1f1", outline="#111111", width=2)
        draw.text((975, y + 10), k, font=font(36, True), fill=RED)
        draw.text((1090, y + 15), v, font=font(30, False), fill=BLACK)
        y += 82
    label(draw, (110, 805, 790, 862), "把形容词拆成事实、表格、清单", fill=BLACK, text_fill=LIGHT)
    img.convert("RGB").save(ASSETS / "03-ai-readable-content.png", quality=95)


def render_ai_page():
    w, h = 1600, 900
    img = Image.new("RGBA", (w, h), PAPER)
    draw = ImageDraw.Draw(img)
    draw_bg(draw, w, h, 23)
    draw.text((72, 54), "网页也要 AI 友好", font=font(84, True), fill=BLACK)
    draw.text((72, 154), "能读懂、点得动、可复现，才有机会被可靠使用", font=font(38, False), fill=GRAY)
    draw_brush(draw, [(65, 225), (465, 205), (870, 225), (1470, 205)], color=RED, width=16)

    cards = [
        ("语义标签", "main / article / h1-h3"),
        ("稳定按钮", "button + aria-label"),
        ("URL状态", "筛选 / 分页 / 排序写进网址"),
        ("文本错误", "别只靠红框和动画"),
        ("原生表单", "select / checkbox\nradio"),
        ("分页加载", "有终点，有 loading 状态"),
    ]
    positions = [(90, 300), (555, 300), (1020, 300), (90, 580), (555, 580), (1020, 580)]
    for i, ((title, desc), (x, y)) in enumerate(zip(cards, positions), start=1):
        shadow_card(img, (x, y, x + 390, y + 190), radius=24, fill=LIGHT, outline=BLACK, shadow=(0, 0, 0, 45), blur=10)
        draw = ImageDraw.Draw(img)
        draw.ellipse((x + 26, y + 26, x + 86, y + 86), fill=RED)
        draw.text((x + 44, y + 34), str(i), font=font(34, True), fill=LIGHT)
        draw.text((x + 105, y + 28), title, font=font(43, True), fill=BLACK)
        draw_wrapped(draw, (x + 34, y + 107), desc, font(30, False), fill=GRAY, max_width=315, line_gap=8)

    label(draw, (925, 84, 1460, 156), "不是特殊玄学，是基础可读性", fill=RED, text_fill=LIGHT)
    img.convert("RGB").save(ASSETS / "04-ai-friendly-page.png", quality=95)


def main():
    render_title()
    render_workflow()
    render_readable_content()
    render_ai_page()
    for file in sorted(ASSETS.glob("*.png")):
        print(file)


if __name__ == "__main__":
    main()
