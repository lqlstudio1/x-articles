from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")

INK = "#f5efe4"
MUTED = "#aeb9b6"
BG = "#070b0f"
TEAL = "#27d7c4"
ORANGE = "#ff7043"
YELLOW = "#f6c85f"
BLUE = "#5c7cff"
RED = "#e74b4b"
PANEL = "#111820"


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size=size)


def text_box(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw, x1, x2, y, text, fnt, fill=INK, stroke=0):
    tw, _ = text_box(draw, text, fnt)
    draw.text(((x1 + x2 - tw) / 2, y), text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill="#020304")


def draw_text(draw, xy, text, size, fill=INK, bold=False, stroke=0):
    draw.text(xy, text, font=font(size, bold), fill=fill, stroke_width=stroke, stroke_fill="#020304")


def rounded(draw, box, radius=32, fill=PANEL, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def add_noise(img, opacity=22):
    w, h = img.size
    rnd = random.Random(119)
    small = Image.new("L", (max(1, w // 4), max(1, h // 4)), 0)
    pixels = small.load()
    for y in range(small.height):
        for x in range(small.width):
            pixels[x, y] = rnd.randint(0, 255)
    small = small.resize((w, h), Image.Resampling.BILINEAR)
    noise = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    noise.putalpha(small.point(lambda p: int(p * opacity / 255)))
    return Image.alpha_composite(img, noise)


def base(size):
    w, h = size
    img = Image.new("RGBA", size, BG)
    draw = ImageDraw.Draw(img, "RGBA")

    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(255, 255, 255, 9), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(255, 255, 255, 7), width=1)

    for offset in range(-h, w, 220):
        draw.line((offset, h, offset + h, 0), fill=(39, 215, 196, 12), width=2)

    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.rectangle((0, 0, w, int(h * 0.18)), fill=(14, 24, 31, 160))
    d.polygon([(0, h), (int(w * 0.42), h), (int(w * 0.82), 0), (int(w * 0.62), 0)], fill=(255, 112, 67, 28))
    d.polygon([(int(w * 0.48), h), (w, h), (w, int(h * 0.18)), (int(w * 0.78), int(h * 0.35))], fill=(92, 124, 255, 24))
    layer = layer.filter(ImageFilter.GaussianBlur(0.8))
    img = Image.alpha_composite(img, layer)
    return add_noise(img, 18)


def small_label(draw, x, y, text, color=TEAL):
    rounded(draw, (x, y, x + 380, y + 52), 18, fill=(39, 215, 196, 235), outline=(255, 255, 255, 90), width=1)
    draw_text(draw, (x + 24, y + 8), text, 26, "#061014", True)


def arrow(draw, x1, y1, x2, y2, color="#d9e4df", width=5):
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 18
    pts = [
        (x2, y2),
        (x2 - size * math.cos(angle - 0.55), y2 - size * math.sin(angle - 0.55)),
        (x2 - size * math.cos(angle + 0.55), y2 - size * math.sin(angle + 0.55)),
    ]
    draw.polygon(pts, fill=color)


def title_card():
    w, h = 2500, 1000
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")

    draw.line((120, 120, 2380, 120), fill=(255, 255, 255, 35), width=2)
    draw.line((120, 880, 2380, 880), fill=(255, 255, 255, 35), width=2)
    small_label(draw, 150, 162, "REDDIT + AI 内容套利")

    draw_text(draw, (145, 278), "搬运爆款", 188, INK, True, 3)
    draw_text(draw, (145, 512), "赚不到信任", 205, ORANGE, True, 4)
    draw_text(draw, (152, 774), "信息差只是入口，不是护城河", 54, "#d7e1de", True)

    rounded(draw, (1780, 245, 2325, 720), 40, fill=(10, 16, 21, 190), outline=(255, 255, 255, 45), width=2)
    draw_text(draw, (1840, 305), "短期", 74, TEAL, True)
    draw_text(draw, (1840, 410), "流量", 116, INK, True, 2)
    draw_text(draw, (1840, 580), "≠ 长期资产", 58, YELLOW, True)
    draw.line((1760, 770, 2325, 770), fill=(255, 112, 67, 150), width=8)

    out = OUT_DIR / "01-title-5x2.png"
    img.convert("RGB").save(out, quality=96)
    return out


def arbitrage_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_text(draw, (80, 72), "这不是创作", 54, TEAL, True)
    draw_text(draw, (80, 142), "而是信息套利", 88, INK, True, 2)

    nodes = [
        (125, 365, "Reddit 爆款", "已验证选题", TEAL),
        (600, 365, "AI 包装", "总结 / 改写 / 配图", ORANGE),
        (1075, 365, "X 流量", "吃时间差", BLUE),
    ]
    for x, y, title, desc, color in nodes:
        rounded(draw, (x, y, x + 360, y + 210), 34, fill=(17, 24, 32, 230), outline=(255, 255, 255, 48), width=2)
        draw.rectangle((x, y, x + 360, y + 12), fill=color)
        draw_text(draw, (x + 38, y + 48), title, 44, INK, True)
        draw_text(draw, (x + 38, y + 120), desc, 30, "#c9d5d2", True)
    arrow(draw, 505, 470, 575, 470, "#d9e4df", 5)
    arrow(draw, 980, 470, 1050, 470, "#d9e4df", 5)

    rounded(draw, (185, 690, 1415, 780), 26, fill=(245, 239, 228, 230), outline=None)
    draw_text(draw, (235, 710), "能赚时间差，但沉淀不了账号信任。", 42, "#10161b", True)

    out = OUT_DIR / "02-information-arbitrage.png"
    img.convert("RGB").save(out, quality=95)
    return out


def trust_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_text(draw, (80, 72), "真正的资产", 54, TEAL, True)
    draw_text(draw, (80, 142), "不是素材，是信任复利", 78, INK, True, 2)

    cx, cy = 800, 510
    draw.ellipse((565, 275, 1035, 745), outline=(255, 255, 255, 55), width=3)
    draw.ellipse((610, 320, 990, 700), fill=(11, 18, 24, 230), outline=(39, 215, 196, 160), width=4)
    draw_center(draw, 610, 990, 430, "账号信任", font(70, True), INK, 2)
    draw_center(draw, 610, 990, 535, "长期复利", font(42, True), ORANGE, 1)

    items = [
        (190, 280, "选题判断", "知道什么值得写", TEAL),
        (1015, 280, "事实校验", "不把传言当结论", YELLOW),
        (190, 630, "个人视角", "给出你的判断", ORANGE),
        (1015, 630, "持续交付", "形成稳定栏目", BLUE),
    ]
    for x, y, title, desc, color in items:
        rounded(draw, (x, y, x + 390, y + 150), 30, fill=(17, 24, 32, 230), outline=(255, 255, 255, 44), width=2)
        draw.rectangle((x, y, x + 390, y + 10), fill=color)
        draw_text(draw, (x + 36, y + 36), title, 42, INK, True)
        draw_text(draw, (x + 36, y + 94), desc, 26, "#c9d5d2", True)

    arrow(draw, 580, 360, 645, 410, TEAL, 4)
    arrow(draw, 1020, 360, 955, 410, YELLOW, 4)
    arrow(draw, 580, 705, 650, 620, ORANGE, 4)
    arrow(draw, 1020, 705, 950, 620, BLUE, 4)

    out = OUT_DIR / "03-trust-flywheel.png"
    img.convert("RGB").save(out, quality=95)
    return out


def upgraded_steps_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")

    draw_text(draw, (80, 72), "升级版 7 步", 58, TEAL, True)
    draw_text(draw, (80, 145), "别搬运，做加工", 88, INK, True, 2)
    draw_text(draw, (86, 260), "把爆款拆开、验证、重组，再变成你的内容产品。", 34, "#c9d5d2", True)

    steps = [
        ("1", "选题雷达"),
        ("2", "追溯来源"),
        ("3", "提炼钩子"),
        ("4", "加入判断"),
        ("5", "对齐定位"),
        ("6", "AI 提效"),
        ("7", "数据复盘"),
    ]
    colors = [TEAL, YELLOW, ORANGE, BLUE, "#9bd66f", "#c084fc", RED]
    start_x, start_y = 95, 405
    gap_x, gap_y = 210, 172
    for i, ((num, label), color) in enumerate(zip(steps, colors)):
        row = 0 if i < 4 else 1
        col = i if i < 4 else i - 4
        x = start_x + col * 365 + (0 if row == 0 else 185)
        y = start_y + row * gap_y
        rounded(draw, (x, y, x + 295, y + 118), 24, fill=(17, 24, 32, 232), outline=(255, 255, 255, 42), width=2)
        draw.ellipse((x + 24, y + 28, x + 84, y + 88), fill=color)
        draw_center(draw, x + 24, x + 84, y + 43, num, font(30, True), "#080b0f")
        draw_text(draw, (x + 106, y + 36), label, 36, INK, True)
        if i in [0, 1, 2, 4, 5]:
            arrow(draw, x + 298, y + 59, x + 345, y + 59, "#d9e4df", 4)

    rounded(draw, (330, 760, 1270, 828), 24, fill=(255, 112, 67, 215), outline=None)
    draw_text(draw, (380, 776), "关键问题：这条内容没有我，还成立吗？", 36, "#090d10", True)

    out = OUT_DIR / "04-upgraded-7-steps.png"
    img.convert("RGB").save(out, quality=95)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = [
        title_card(),
        arbitrage_card(),
        trust_card(),
        upgraded_steps_card(),
    ]
    for path in outputs:
        print(path)


if __name__ == "__main__":
    main()
