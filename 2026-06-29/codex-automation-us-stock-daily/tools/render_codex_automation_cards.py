from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")

BG = "#070b0f"
INK = "#f6f0e6"
MUTED = "#b7c3c0"
TEAL = "#2bd6c4"
ORANGE = "#ff7043"
YELLOW = "#f6c85f"
BLUE = "#5c7cff"
RED = "#e84d4d"
PANEL = "#111820"


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size=size)


def box(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def text(draw, xy, s, size, fill=INK, bold=False, stroke=0):
    draw.text(xy, s, font=font(size, bold), fill=fill, stroke_width=stroke, stroke_fill="#020304")


def center(draw, x1, x2, y, s, fnt, fill=INK, stroke=0):
    tw, _ = box(draw, s, fnt)
    draw.text(((x1 + x2 - tw) / 2, y), s, font=fnt, fill=fill, stroke_width=stroke, stroke_fill="#020304")


def rounded(draw, xy, radius=30, fill=PANEL, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def base(size):
    w, h = size
    img = Image.new("RGBA", size, BG)
    draw = ImageDraw.Draw(img, "RGBA")

    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(255, 255, 255, 9), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(255, 255, 255, 7), width=1)
    for off in range(-h, w, 220):
        draw.line((off, h, off + h, 0), fill=(43, 214, 196, 12), width=2)

    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.polygon([(0, h), (int(w * 0.42), h), (int(w * 0.84), 0), (int(w * 0.63), 0)], fill=(255, 112, 67, 30))
    d.polygon([(int(w * 0.50), h), (w, h), (w, int(h * 0.16)), (int(w * 0.78), int(h * 0.35))], fill=(92, 124, 255, 26))
    d.rectangle((0, 0, w, int(h * 0.18)), fill=(14, 24, 31, 160))
    img = Image.alpha_composite(img, layer.filter(ImageFilter.GaussianBlur(0.8)))

    rnd = random.Random(829)
    small = Image.new("L", (max(1, w // 4), max(1, h // 4)), 0)
    px = small.load()
    for y in range(small.height):
        for x in range(small.width):
            px[x, y] = rnd.randint(0, 255)
    noise = small.resize((w, h), Image.Resampling.BILINEAR)
    n = Image.new("RGBA", size, (255, 255, 255, 0))
    n.putalpha(noise.point(lambda p: int(p * 18 / 255)))
    return Image.alpha_composite(img, n)


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
    draw.line((120, 120, 2380, 120), fill=(255, 255, 255, 36), width=2)
    draw.line((120, 880, 2380, 880), fill=(255, 255, 255, 36), width=2)

    rounded(draw, (150, 162, 520, 214), 18, fill=(43, 214, 196, 235), outline=(255, 255, 255, 90), width=1)
    text(draw, (174, 170), "CODEX AUTOMATIONS", 25, "#061014", True)

    text(draw, (145, 275), "每天 8 点", 186, INK, True, 3)
    text(draw, (145, 505), "自动复盘", 214, ORANGE, True, 4)
    text(draw, (152, 777), "把财经日报变成自动交付工作流", 54, "#d7e1de", True)

    rounded(draw, (1745, 250, 2325, 735), 42, fill=(10, 16, 21, 205), outline=(255, 255, 255, 45), width=2)
    text(draw, (1810, 310), "固定时间", 56, TEAL, True)
    text(draw, (1810, 410), "固定结构", 56, YELLOW, True)
    text(draw, (1810, 510), "固定来源", 56, BLUE, True)
    text(draw, (1810, 610), "固定输出", 56, ORANGE, True)
    draw.line((1745, 780, 2325, 780), fill=(255, 112, 67, 155), width=8)

    out = OUT_DIR / "01-title-5x2.png"
    img.convert("RGB").save(out, quality=96)
    return out


def workflow_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    text(draw, (80, 70), "自动化链路", 54, TEAL, True)
    text(draw, (80, 142), "不是写日报，是交付系统", 78, INK, True, 2)

    items = [
        ("08:00", "定时唤醒", TEAL),
        ("Sources", "可靠来源", YELLOW),
        ("Report", "结构日报", BLUE),
        ("Review", "人工复盘", ORANGE),
    ]
    x0, y = 95, 390
    for i, (top, bottom, color) in enumerate(items):
        x = x0 + i * 370
        rounded(draw, (x, y, x + 300, y + 190), 34, fill=(17, 24, 32, 232), outline=(255, 255, 255, 48), width=2)
        draw.rectangle((x, y, x + 300, y + 12), fill=color)
        center(draw, x, x + 300, y + 45, top, font(48, True), INK, 1)
        center(draw, x, x + 300, y + 115, bottom, font(36, True), "#c9d5d2")
        if i < len(items) - 1:
            arrow(draw, x + 315, y + 95, x + 360, y + 95, "#d9e4df", 5)

    rounded(draw, (245, 705, 1355, 790), 28, fill=(245, 239, 228, 230))
    text(draw, (300, 724), "关键：固定输入、固定结构、固定校验、固定输出", 40, "#10161b", True)

    out = OUT_DIR / "02-daily-workflow.png"
    img.convert("RGB").save(out, quality=95)
    return out


def guardrails_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    text(draw, (80, 70), "Prompt 骨架", 54, TEAL, True)
    text(draw, (80, 142), "先写边界，再写内容", 86, INK, True, 2)

    items = [
        ("角色", "美股收盘日报分析师", TEAL),
        ("时间", "每天北京时间 8 点", YELLOW),
        ("来源", "关键数据必须标注", BLUE),
        ("反幻觉", "拿不到就写暂无可靠数据", ORANGE),
        ("结构", "大盘 / 宏观 / 板块 / 个股 / 风险", "#9bd66f"),
        ("边界", "复盘观察，不是投资建议", RED),
    ]
    for i, (title, desc, color) in enumerate(items):
        col = i % 2
        row = i // 2
        x = 115 + col * 710
        y = 330 + row * 150
        rounded(draw, (x, y, x + 650, y + 105), 24, fill=(17, 24, 32, 232), outline=(255, 255, 255, 42), width=2)
        draw.ellipse((x + 28, y + 28, x + 78, y + 78), fill=color)
        text(draw, (x + 105, y + 24), title, 34, INK, True)
        text(draw, (x + 230, y + 28), desc, 28, "#c9d5d2", True)

    out = OUT_DIR / "03-prompt-guardrails.png"
    img.convert("RGB").save(out, quality=95)
    return out


def boundary_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    text(draw, (80, 70), "边界要写清楚", 54, TEAL, True)
    text(draw, (80, 142), "日报不是交易信号", 86, INK, True, 2)

    left = (150, 320, 720, 690)
    right = (880, 320, 1450, 690)
    rounded(draw, left, 38, fill=(17, 24, 32, 235), outline=(255, 255, 255, 44), width=2)
    rounded(draw, right, 38, fill=(17, 24, 32, 235), outline=(255, 255, 255, 44), width=2)
    draw.rectangle((left[0], left[1], left[2], left[1] + 14), fill=TEAL)
    draw.rectangle((right[0], right[1], right[2], right[1] + 14), fill=RED)

    text(draw, (205, 382), "应该做", 58, INK, True)
    for i, s in enumerate(["整理信息", "标注来源", "提示风险", "辅助复盘"]):
        text(draw, (220, 480 + i * 48), f"✓ {s}", 32, "#d7e1de", True)

    text(draw, (935, 382), "不要做", 58, INK, True)
    for i, s in enumerate(["替你下单", "编造数据", "保证收益", "自动交易"]):
        text(draw, (950, 480 + i * 48), f"× {s}", 32, "#d7e1de", True)

    rounded(draw, (285, 760, 1315, 828), 24, fill=(255, 112, 67, 218))
    text(draw, (345, 776), "真正的价值：稳定复盘框架，而不是买卖建议", 35, "#090d10", True)

    out = OUT_DIR / "04-not-investment-advice.png"
    img.convert("RGB").save(out, quality=95)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [title_card(), workflow_card(), guardrails_card(), boundary_card()]:
        print(path)


if __name__ == "__main__":
    main()
