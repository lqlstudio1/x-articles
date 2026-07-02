from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F = {
    "mega": font(170, True),
    "title": font(118, True),
    "h1": font(76, True),
    "h2": font(48, True),
    "body": font(34, False),
    "small": font(25, False),
    "tag": font(30, True),
}

INK = (48, 55, 49)
SAGE = (113, 145, 119)
DEEP = (69, 102, 79)
ORANGE = (221, 132, 75)
CREAM = (248, 244, 232)
PAPER = (252, 249, 240)
WOOD = (174, 132, 86)
MUTED = (126, 132, 119)
LINE = (224, 216, 196)
WHITE = (255, 255, 255)


def rounded(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def shadow_card(im, xy, r=28, fill=WHITE, shadow=(80, 63, 38, 35), offset=(0, 14), blur=18):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = xy
    d.rounded_rectangle((x1 + offset[0], y1 + offset[1], x2 + offset[0], y2 + offset[1]), radius=r, fill=shadow)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(layer)
    ImageDraw.Draw(im).rounded_rectangle(xy, radius=r, fill=fill)


def texture(draw, w, h, seed=8):
    random.seed(seed)
    for _ in range(1400):
        x, y = random.randrange(w), random.randrange(h)
        v = random.randrange(-8, 8)
        draw.point((x, y), fill=(252 + v, 249 + v, 240 + v))
    for x in range(0, w, 88):
        draw.line((x, 0, x, h), fill=(239, 232, 214), width=1)
    for y in range(0, h, 88):
        draw.line((0, y, w, y), fill=(239, 232, 214), width=1)


def text_size(draw, text, ft):
    box = draw.textbbox((0, 0), text, font=ft)
    return box[2] - box[0], box[3] - box[1]


def save(im, name):
    path = ASSETS / name
    im.convert("RGB").save(path, quality=95)
    print(path)


def draw_plant(draw, x, y, scale=1.0):
    rounded(draw, (x + 35 * scale, y + 130 * scale, x + 145 * scale, y + 225 * scale), int(20 * scale), (207, 143, 91))
    draw.rectangle((x + 48 * scale, y + 210 * scale, x + 132 * scale, y + 238 * scale), fill=(171, 108, 72))
    for dx, dy, rx, ry in [
        (20, 85, 34, 18), (95, 60, 40, 20), (60, 30, 32, 18),
        (118, 108, 35, 18), (42, 115, 32, 18)
    ]:
        draw.ellipse((x + dx * scale, y + dy * scale, x + (dx + rx) * scale, y + (dy + ry) * scale), fill=SAGE)
    draw.line((x + 88 * scale, y + 138 * scale, x + 88 * scale, y + 55 * scale), fill=DEEP, width=int(5 * scale))
    draw.line((x + 88 * scale, y + 118 * scale, x + 42 * scale, y + 95 * scale), fill=DEEP, width=int(4 * scale))
    draw.line((x + 88 * scale, y + 92 * scale, x + 132 * scale, y + 70 * scale), fill=DEEP, width=int(4 * scale))


def draw_phone(draw, x, y, scale=1.0):
    rounded(draw, (x, y, x + 170 * scale, y + 285 * scale), int(28 * scale), (44, 50, 49), outline=(78, 86, 82), width=int(4 * scale))
    draw.rectangle((x + 20 * scale, y + 28 * scale, x + 150 * scale, y + 245 * scale), fill=(37, 43, 42))
    draw.line((x + 50 * scale, y + 90 * scale, x + 120 * scale, y + 90 * scale), fill=SAGE, width=int(7 * scale))
    draw.line((x + 44 * scale, y + 130 * scale, x + 132 * scale, y + 130 * scale), fill=ORANGE, width=int(7 * scale))
    draw.line((x + 60 * scale, y + 170 * scale, x + 110 * scale, y + 170 * scale), fill=(179, 188, 176), width=int(7 * scale))


def draw_bowl(draw, x, y, scale=1.0):
    draw.ellipse((x, y + 45 * scale, x + 260 * scale, y + 145 * scale), fill=(235, 225, 203), outline=(190, 174, 146), width=int(4 * scale))
    draw.pieslice((x + 18 * scale, y + 30 * scale, x + 242 * scale, y + 160 * scale), 0, 180, fill=(255, 249, 230))
    draw.arc((x + 28 * scale, y + 45 * scale, x + 232 * scale, y + 145 * scale), 0, 180, fill=(204, 180, 130), width=int(4 * scale))
    for i in range(5):
        draw.ellipse((x + (55 + i * 28) * scale, y + (58 + (i % 2) * 20) * scale, x + (82 + i * 28) * scale, y + (82 + (i % 2) * 20) * scale), fill=(245, 170, 85))


def draw_notebook(draw, x, y, scale=1.0):
    rounded(draw, (x, y, x + 360 * scale, y + 260 * scale), int(22 * scale), WHITE, outline=LINE, width=int(3 * scale))
    draw.rectangle((x + 32 * scale, y, x + 58 * scale, y + 260 * scale), fill=(223, 235, 220))
    for i in range(5):
        yy = y + (58 + i * 36) * scale
        draw.line((x + 86 * scale, yy, x + 305 * scale, yy), fill=(190, 184, 164), width=int(4 * scale))
    draw.text((x + 86 * scale, y + 28 * scale), "today", fill=SAGE, font=font(int(34 * scale), True))


def title_card():
    w, h = 2500, 1000
    im = Image.new("RGBA", (w, h), PAPER + (255,))
    draw = ImageDraw.Draw(im)
    texture(draw, w, h)
    draw.polygon([(1430, 0), (2500, 0), (2500, 1000), (1600, 1000)], fill=(224, 235, 219))
    for x in range(1450, 2500, 110):
        draw.line((x, 0, x - 220, 1000), fill=(206, 224, 204), width=3)

    draw.text((120, 120), "6个方法", fill=SAGE, font=F["title"])
    draw.text((120, 292), "养回自己", fill=INK, font=F["mega"])
    draw.text((132, 545), "少一点内耗，多一点边界", fill=ORANGE, font=F["h2"])
    rounded(draw, (130, 745, 820, 835), 28, WHITE, outline=LINE, width=3)
    draw.text((170, 768), "吃好  睡好  少消耗", fill=DEEP, font=F["tag"])

    # right lifestyle scene
    draw.rounded_rectangle((1470, 725, 2380, 790), radius=28, fill=WOOD)
    draw_bowl(draw, 1540, 520, 1.0)
    draw_notebook(draw, 1850, 420, 0.95)
    draw_phone(draw, 2220, 405, 0.8)
    draw_plant(draw, 1550, 270, 1.0)
    draw.ellipse((2020, 250, 2170, 400), fill=(255, 231, 185))
    draw.line((2095, 395, 2095, 565), fill=(139, 114, 86), width=13)
    draw.ellipse((2035, 535, 2155, 570), fill=(139, 114, 86))

    draw.line((1190, 610, 1515, 555), fill=ORANGE, width=10)
    draw.polygon([(1515, 555), (1458, 535), (1472, 592)], fill=ORANGE)
    save(im, "01-title-5x2.png")


def six_habits_map():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), PAPER + (255,))
    draw = ImageDraw.Draw(im)
    texture(draw, w, h, seed=15)
    draw.text((70, 58), "6 个旺自己的方法", fill=INK, font=F["h1"])
    draw.text((76, 142), "本质是减少内耗，守住边界", fill=MUTED, font=F["h2"])

    items = [
        ("01", "吃饭睡觉", "先稳身体"),
        ("02", "少说少掺和", "收住精力"),
        ("03", "远离轻视", "不再证明"),
        ("04", "放过旧事", "只留教训"),
        ("05", "不改别人", "只管选择"),
        ("06", "善良有锋芒", "守住边界"),
    ]
    x0, y0 = 70, 250
    cw, ch = 455, 230
    for i, (num, title, sub) in enumerate(items):
        x = x0 + (i % 3) * 510
        y = y0 + (i // 3) * 275
        shadow_card(im, (x, y, x + cw, y + ch), r=30, fill=WHITE)
        draw = ImageDraw.Draw(im)
        draw.text((x + 28, y + 26), num, fill=ORANGE if i in [0, 5] else SAGE, font=F["h2"])
        # simple icon dot/line
        cx, cy = x + 92, y + 140
        draw.ellipse((cx - 42, cy - 42, cx + 42, cy + 42), fill=(229, 238, 224))
        if i == 0:
            draw_bowl(draw, cx - 62, cy - 48, 0.48)
        elif i == 1:
            draw.line((cx - 38, cy, cx + 38, cy), fill=DEEP, width=8)
            draw.line((cx - 22, cy - 24, cx + 22, cy + 24), fill=DEEP, width=8)
        elif i == 2:
            draw.line((cx - 36, cy + 28, cx + 36, cy - 28), fill=ORANGE, width=9)
            draw.line((cx - 36, cy - 28, cx + 36, cy + 28), fill=ORANGE, width=9)
        elif i == 3:
            rounded(draw, (cx - 45, cy - 30, cx + 45, cy + 34), 12, CREAM, outline=SAGE, width=4)
            draw.line((cx - 24, cy - 6, cx + 24, cy - 6), fill=SAGE, width=5)
            draw.line((cx - 18, cy + 12, cx + 20, cy + 12), fill=SAGE, width=5)
        elif i == 4:
            draw.arc((cx - 38, cy - 38, cx + 38, cy + 38), 40, 315, fill=SAGE, width=8)
            draw.polygon([(cx + 35, cy - 14), (cx + 55, cy - 2), (cx + 30, cy + 10)], fill=SAGE)
        else:
            draw.polygon([(cx, cy - 48), (cx + 45, cy - 22), (cx + 33, cy + 42), (cx, cy + 55), (cx - 33, cy + 42), (cx - 45, cy - 22)], fill=SAGE)
            draw.ellipse((cx - 18, cy - 8, cx + 18, cy + 28), fill=ORANGE)
        draw.text((x + 176, y + 78), title, fill=INK, font=F["h2"])
        draw.text((x + 180, y + 138), sub, fill=MUTED, font=F["body"])
    save(im, "02-six-habits-map.png")


def let_go_past():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (250, 247, 238, 255))
    draw = ImageDraw.Draw(im)
    texture(draw, w, h, seed=22)
    draw.text((76, 58), "别反复翻旧账", fill=INK, font=F["h1"])
    draw.text((82, 142), "复盘一次是成长，重复责怪是消耗", fill=MUTED, font=F["h2"])

    # desk and box
    draw.rounded_rectangle((120, 690, 1480, 755), radius=26, fill=WOOD)
    shadow_card(im, (190, 300, 640, 660), r=26, fill=WHITE)
    draw = ImageDraw.Draw(im)
    draw.text((240, 345), "过去的事", fill=ORANGE, font=F["h2"])
    for i, t in enumerate(["说错的话", "做错的选择", "结束的关系"]):
        yy = 435 + i * 58
        draw.line((250, yy, 520, yy), fill=LINE, width=6)
        draw.text((250, yy - 28), t, fill=MUTED, font=F["small"])
    # archive box
    rounded(draw, (865, 375, 1330, 680), 28, (211, 177, 130), outline=(150, 113, 76), width=4)
    draw.rectangle((865, 375, 1330, 445), fill=(190, 151, 103))
    draw.text((970, 515), "留下教训", fill=WHITE, font=F["h2"])
    draw.text((972, 575), "放下情绪", fill=(255, 238, 210), font=F["body"])
    # arrow paper into box
    draw.line((650, 500, 845, 520), fill=ORANGE, width=12)
    draw.polygon([(845, 520), (790, 492), (785, 548)], fill=ORANGE)
    draw.text((650, 448), "只存档，不重播", fill=ORANGE, font=F["tag"])
    save(im, "03-let-go-past.png")


def kindness_boundary():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (244, 249, 241, 255))
    draw = ImageDraw.Draw(im)
    texture(draw, w, h, seed=31)
    draw.text((76, 58), "善良要有边界", fill=INK, font=F["h1"])
    draw.text((82, 142), "真诚给值得的人，热情也要会收回", fill=MUTED, font=F["h2"])

    # shield and heart
    cx, cy = 800, 485
    shield = [(cx, cy - 210), (cx + 230, cy - 90), (cx + 175, cy + 180), (cx, cy + 270), (cx - 175, cy + 180), (cx - 230, cy - 90)]
    draw.polygon(shield, fill=(214, 232, 211), outline=DEEP)
    draw.line((cx, cy - 210, cx, cy + 270), fill=(187, 216, 184), width=6)
    draw.ellipse((cx - 74, cy - 54, cx + 18, cy + 42), fill=ORANGE)
    draw.ellipse((cx - 18, cy - 54, cx + 74, cy + 42), fill=ORANGE)
    draw.polygon([(cx - 77, cy - 4), (cx + 77, cy - 4), (cx, cy + 110)], fill=ORANGE)
    draw.text((cx - 118, cy + 145), "有锋芒", fill=DEEP, font=F["h2"])

    shadow_card(im, (115, 330, 520, 650), r=30, fill=WHITE)
    shadow_card(im, (1080, 330, 1485, 650), r=30, fill=WHITE)
    draw = ImageDraw.Draw(im)
    draw.text((160, 382), "不要这样", fill=ORANGE, font=F["h2"])
    for i, t in enumerate(["一点好就掏心", "无限让步", "底牌全交"]):
        draw.text((165, 465 + i * 52), t, fill=MUTED, font=F["body"])
    draw.text((1125, 382), "改成这样", fill=DEEP, font=F["h2"])
    for i, t in enumerate(["真诚但判断", "帮忙有边界", "越界就收回"]):
        draw.text((1130, 465 + i * 52), t, fill=MUTED, font=F["body"])
    save(im, "04-kindness-boundary.png")


if __name__ == "__main__":
    title_card()
    six_habits_map()
    let_go_past()
    kindness_boundary()
