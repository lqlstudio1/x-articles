from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf"),
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
]


def font(size, bold=False):
    for path in FONT_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size=size, index=0)
    return ImageFont.load_default()


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt, stroke_width=0)
    return box[2] - box[0], box[3] - box[1]


def draw_text(draw, xy, text, fnt, fill, stroke=0, stroke_fill=(0, 0, 0)):
    draw.text(xy, text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def background(w, h, seed=1):
    random.seed(seed)
    img = Image.new("RGB", (w, h), "#071016")
    px = img.load()
    for y in range(h):
        for x in range(w):
            base = 10 + int(16 * y / h)
            noise = random.randint(-7, 7)
            px[x, y] = (
                max(0, min(255, base + noise)),
                max(0, min(255, base + 8 + noise)),
                max(0, min(255, base + 14 + noise)),
            )
    img = img.filter(ImageFilter.GaussianBlur(0.25))
    d = ImageDraw.Draw(img, "RGBA")
    grid = max(64, w // 25)
    for x in range(0, w, grid):
        d.line((x, 0, x, h), fill=(255, 255, 255, 32), width=1)
    for y in range(0, h, grid):
        d.line((0, y, w, y), fill=(255, 255, 255, 32), width=1)
    for x in range(-w, w * 2, grid * 3):
        d.line((x, h, x + h, 0), fill=(43, 211, 196, 88), width=2)
    d.polygon([(0, h), (w * 0.45, h * 0.18), (w * 0.75, h * 0.18), (w * 0.18, h)], fill=(255, 109, 71, 46))
    d.polygon([(w * 0.58, h), (w, h * 0.18), (w, h)], fill=(82, 116, 255, 42))
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
    img = background(w, h, seed=11)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    blue = "#5874FF"
    pill(d, (145, 145), "X ALGORITHM", cyan, size=34)
    draw_text(d, (145, 292), "别再奖励", font(146), cream, stroke=5)
    draw_text(d, (145, 468), "争吵", font(210), orange, stroke=6)
    draw_text(d, (145, 724), "算法应该奖励值得被记住的内容", font(48), cream, stroke=2)
    panel(d, (1620, 250, 2290, 720), fill=(6, 13, 18, 242), outline=(244, 239, 231, 230))
    items = [("收藏", cyan), ("精读", "#FFD166"), ("原创", blue), ("理性讨论", orange)]
    y = 322
    for label, color in items:
        draw_text(d, (1700, y), label, font(62), color, stroke=2)
        y += 98
    d.line((1620, 780, 2290, 780), fill=(255, 109, 71, 255), width=8)
    d.line((120, 120, 2380, 120), fill=(244, 239, 231, 180), width=3)
    d.line((120, 870, 2380, 870), fill=(244, 239, 231, 180), width=3)
    img.save(OUT / "01-title-5x2.png")


def save_incentive():
    w, h = 1600, 900
    img = background(w, h, seed=22)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    red = "#E94D4D"
    draw_text(d, (82, 78), "算法奖励什么", font(58), cyan, stroke=2)
    draw_text(d, (80, 154), "内容就会长成什么", font(74), cream, stroke=4)
    panel(d, (110, 318, 690, 685), accent=red)
    panel(d, (910, 318, 1490, 685), accent=cyan)
    draw_text(d, (178, 406), "奖励反应", font(54), cream, stroke=2)
    for i, item in enumerate(["争吵", "站队", "嘲讽", "模板爆款"]):
        draw_text(d, (210, 500 + i * 46), f"x {item}", font(34), "#DDE6E6")
    draw_text(d, (980, 406), "奖励价值", font(54), cream, stroke=2)
    for i, item in enumerate(["收藏", "精读", "原创", "理性讨论"]):
        draw_text(d, (1015, 500 + i * 46), f"+ {item}", font(34), "#DDE6E6")
    d.line((735, 500, 865, 500), fill=(244, 239, 231, 220), width=6)
    d.polygon([(870, 500), (840, 480), (840, 520)], fill=(244, 239, 231, 220))
    draw_text(d, (310, 760), "核心：从情绪互动，转向长期信任", font(45), "#071016")
    d.rounded_rectangle((250, 730, 1350, 815), radius=24, fill=(244, 239, 231, 238))
    draw_text(d, (310, 752), "核心：从情绪互动，转向长期信任", font(45), "#071016")
    img.save(OUT / "02-incentive-map.png")


def save_two_feeds():
    w, h = 1600, 900
    img = background(w, h, seed=33)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    blue = "#5874FF"
    draw_text(d, (80, 78), "双 Feed 隔离", font(62), cyan, stroke=2)
    draw_text(d, (80, 158), "发现和交付，不是一件事", font(68), cream, stroke=4)
    panel(d, (120, 330, 720, 700), accent=blue)
    panel(d, (880, 330, 1480, 700), accent=orange)
    draw_text(d, (195, 410), "推荐流", font(66), cream, stroke=2)
    draw_text(d, (195, 505), "负责发现", font(46), "#DDE6E6")
    draw_text(d, (195, 575), "AI 可介入排序", font(36), "#B9C8C8")
    draw_text(d, (955, 410), "关注流", font(66), cream, stroke=2)
    draw_text(d, (955, 505), "负责交付", font(46), "#DDE6E6")
    draw_text(d, (955, 575), "优先纯时间线", font(36), "#B9C8C8")
    d.line((760, 515, 840, 515), fill=(244, 239, 231, 210), width=6)
    draw_text(d, (360, 765), "用户主动关注，就是一层明确选择权", font(43), "#071016")
    d.rounded_rectangle((290, 735, 1310, 820), radius=24, fill=(244, 239, 231, 238))
    draw_text(d, (360, 757), "用户主动关注，就是一层明确选择权", font(43), "#071016")
    img.save(OUT / "03-two-feeds.png")


def save_creator_trust():
    w, h = 1600, 900
    img = background(w, h, seed=44)
    d = ImageDraw.Draw(img, "RGBA")
    cream = "#F4EFE7"
    cyan = "#2BD3C4"
    orange = "#FF6D47"
    draw_text(d, (82, 80), "创作者信任", font(62), cyan, stroke=2)
    draw_text(d, (80, 160), "比黑箱更重要", font(78), cream, stroke=4)
    labels = [
        ("原因可见", "知道为什么受限", cyan),
        ("限制有期", "负面记录会衰减", "#FFD166"),
        ("申诉有路", "不是终身判死刑", "#9BD56E"),
        ("风控精细", "区分真人和机器", orange),
    ]
    positions = [(115, 330), (850, 330), (115, 555), (850, 555)]
    for (title, sub, color), (x, y) in zip(labels, positions):
        panel(d, (x, y, x + 635, y + 150), outline=(244, 239, 231, 210))
        d.ellipse((x + 35, y + 48, x + 87, y + 100), fill=color)
        draw_text(d, (x + 120, y + 38), title, font(43), cream, stroke=2)
        draw_text(d, (x + 120, y + 94), sub, font(28), "#C9D6D6")
    d.rounded_rectangle((235, 765, 1365, 830), radius=22, fill=(255, 109, 71, 240))
    draw_text(d, (330, 776), "创作者不怕规则严格，怕的是规则不可解释", font(37), "#071016")
    img.save(OUT / "04-creator-trust.png")


if __name__ == "__main__":
    save_title()
    save_incentive()
    save_two_feeds()
    save_creator_trust()
    for path in sorted(OUT.glob("*.png")):
        print(path)
