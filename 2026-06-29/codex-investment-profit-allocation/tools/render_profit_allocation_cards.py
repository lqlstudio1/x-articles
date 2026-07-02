from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
]


def font(size):
    for path in FONT_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size=size, index=0)
    return ImageFont.load_default()


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_text(draw, xy, text, fnt, fill, stroke=0, stroke_fill=(0, 0, 0)):
    draw.text(xy, text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def background(w, h, seed=1):
    random.seed(seed)
    img = Image.new("RGB", (w, h), "#071016")
    px = img.load()
    for y in range(h):
        for x in range(w):
            base = 9 + int(18 * y / h)
            noise = random.randint(-7, 7)
            px[x, y] = (
                max(0, min(255, base + noise)),
                max(0, min(255, base + 8 + noise)),
                max(0, min(255, base + 14 + noise)),
            )
    img = img.filter(ImageFilter.GaussianBlur(0.2))
    d = ImageDraw.Draw(img, "RGBA")
    grid = max(64, w // 25)
    for x in range(0, w, grid):
        d.line((x, 0, x, h), fill=(255, 255, 255, 30), width=1)
    for y in range(0, h, grid):
        d.line((0, y, w, y), fill=(255, 255, 255, 30), width=1)
    for x in range(-w, w * 2, grid * 3):
        d.line((x, h, x + h, 0), fill=(43, 211, 196, 72), width=2)
    d.polygon([(0, h), (w * 0.42, h * 0.20), (w * 0.73, h * 0.20), (w * 0.16, h)], fill=(255, 109, 71, 44))
    d.polygon([(w * 0.58, h), (w, h * 0.20), (w, h)], fill=(82, 116, 255, 38))
    return img


def panel(draw, box, fill=(12, 22, 30, 238), outline=(235, 238, 232, 230), accent=None):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=34, fill=fill, outline=outline, width=3)
    if accent:
        draw.rounded_rectangle((x1, y1, x2, y1 + 18), radius=8, fill=accent)


def pill(draw, xy, text, fill, fg="#071016", pad_x=26, pad_y=10, size=34):
    f = font(size)
    x, y = xy
    tw, th = text_size(draw, text, f)
    draw.rounded_rectangle((x, y, x + tw + pad_x * 2, y + th + pad_y * 2), radius=18, fill=fill)
    draw_text(draw, (x + pad_x, y + pad_y - 3), text, f, fg)


def save_title():
    w, h = 2500, 1000
    img = background(w, h, seed=51)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    blue = "#5874FF"
    pill(d, (145, 145), "CODEX WORKFLOW", cyan, size=34)
    draw_text(d, (145, 292), "偏财", font(165), cream, stroke=5)
    draw_text(d, (145, 500), "别乱花", font(195), orange, stroke=6)
    draw_text(d, (145, 738), "把投资盈利变成一套分流系统", font(52), cream, stroke=2)
    panel(d, (1605, 250, 2295, 720), fill=(6, 13, 18, 242), outline=(244, 239, 231, 230))
    items = [("记录来源", cyan), ("确认落袋", "#FFD166"), ("三类分流", blue), ("定期复盘", orange)]
    y = 320
    for label, color in items:
        draw_text(d, (1690, y), label, font(60), color, stroke=2)
        y += 98
    d.line((1605, 780, 2295, 780), fill=(255, 109, 71, 255), width=8)
    d.line((120, 120, 2380, 120), fill=(244, 239, 231, 180), width=3)
    d.line((120, 870, 2380, 870), fill=(244, 239, 231, 180), width=3)
    img.save(OUT / "01-title-5x2.png")


def save_split():
    w, h = 1600, 900
    img = background(w, h, seed=52)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    blue = "#5874FF"
    draw_text(d, (82, 78), "偏财三分法", font(62), cyan, stroke=2)
    draw_text(d, (80, 158), "流动，不等于流失", font(74), cream, stroke=4)
    cards = [
        ("30%", "适度流通", "消费 / 家人 / 公益", cyan),
        ("40%", "固化资产", "存款 / 技能 / 保障", "#FFD166"),
        ("30%", "保留再投", "本金 / 策略 / 复盘", orange),
    ]
    x = 110
    for pct, title, sub, color in cards:
        panel(d, (x, 345, x + 420, 665), accent=color)
        draw_text(d, (x + 70, 415), pct, font(72), color, stroke=2)
        draw_text(d, (x + 70, 510), title, font(46), cream, stroke=2)
        draw_text(d, (x + 70, 580), sub, font(28), "#C9D6D6")
        x += 535
    d.rounded_rectangle((250, 740, 1350, 815), radius=24, fill=(244, 239, 231, 238))
    draw_text(d, (330, 760), "重点：每次盈利后，先分流，再决定下一步", font(39), "#071016")
    img.save(OUT / "02-three-way-split.png")


def save_workflow():
    w, h = 1600, 900
    img = background(w, h, seed=53)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    blue = "#5874FF"
    draw_text(d, (82, 78), "Codex 管什么", font(62), cyan, stroke=2)
    draw_text(d, (80, 158), "不荐股，只执行流程", font(74), cream, stroke=4)
    nodes = [
        ("Record", "记录来源", cyan),
        ("Classify", "确认落袋", "#FFD166"),
        ("Allocate", "三类分配", blue),
        ("Review", "定期复盘", orange),
    ]
    x = 95
    for i, (en, cn, color) in enumerate(nodes):
        panel(d, (x, 390, x + 300, 580), accent=color)
        draw_text(d, (x + 55, 440), en, font(39), cream, stroke=2)
        draw_text(d, (x + 72, 505), cn, font(34), "#DDE6E6")
        if i < len(nodes) - 1:
            d.line((x + 315, 485, x + 365, 485), fill=(244, 239, 231, 220), width=6)
            d.polygon([(x + 370, 485), (x + 345, 468), (x + 345, 502)], fill=(244, 239, 231, 220))
        x += 375
    d.rounded_rectangle((230, 725, 1370, 815), radius=24, fill=(244, 239, 231, 238))
    draw_text(d, (300, 750), "人做判断，AI 做记录、提醒和复盘", font(42), "#071016")
    img.save(OUT / "03-codex-workflow.png")


def save_boundary():
    w, h = 1600, 900
    img = background(w, h, seed=54)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    red = "#E94D4D"
    draw_text(d, (82, 80), "边界要写清楚", font(62), cyan, stroke=2)
    draw_text(d, (80, 160), "复盘，不是交易信号", font(76), cream, stroke=4)
    panel(d, (150, 335, 725, 690), accent=cyan)
    panel(d, (875, 335, 1450, 690), accent=red)
    draw_text(d, (215, 405), "应该做", font(56), cream, stroke=2)
    for i, item in enumerate(["记录来源", "检查回撤", "分流利润", "复盘情绪"]):
        draw_text(d, (250, 500 + i * 44), f"+ {item}", font(34), "#DDE6E6")
    draw_text(d, (940, 405), "不要做", font(56), cream, stroke=2)
    for i, item in enumerate(["替你下单", "保证收益", "情绪加仓", "荐股预测"]):
        draw_text(d, (975, 500 + i * 44), f"x {item}", font(34), "#DDE6E6")
    d.rounded_rectangle((300, 760, 1300, 825), radius=22, fill=(255, 109, 71, 240))
    draw_text(d, (390, 772), "让利润进入系统，而不是进入情绪", font(38), "#071016")
    img.save(OUT / "04-boundary.png")


if __name__ == "__main__":
    save_title()
    save_split()
    save_workflow()
    save_boundary()
    for path in sorted(OUT.glob("*.png")):
        print(path)
