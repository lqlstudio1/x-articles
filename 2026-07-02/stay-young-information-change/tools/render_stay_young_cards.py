from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

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
    "mega": font(168, True),
    "title": font(112, True),
    "h1": font(76, True),
    "h2": font(48, True),
    "body": font(34, False),
    "small": font(25, False),
    "tag": font(30, True),
}

INK = (230, 236, 232)
DARK = (18, 28, 35)
NIGHT = (23, 35, 51)
BLUE = (73, 168, 255)
CYAN = (71, 222, 211)
ORANGE = (255, 142, 72)
YELLOW = (255, 209, 102)
MUTED = (145, 161, 170)
PAPER = (242, 238, 224)
HOUSE = (95, 72, 60)
WHITE = (255, 255, 255)


def rounded(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def shadow_card(im, xy, r=28, fill=WHITE, shadow=(0, 0, 0, 60), offset=(0, 14), blur=20):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = xy
    d.rounded_rectangle((x1 + offset[0], y1 + offset[1], x2 + offset[0], y2 + offset[1]), radius=r, fill=shadow)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(layer)
    ImageDraw.Draw(im).rounded_rectangle(xy, radius=r, fill=fill)


def save(im, name):
    path = ASSETS / name
    im.convert("RGB").save(path, quality=95)
    print(path)


def starfield(draw, w, h, seed=3):
    random.seed(seed)
    for _ in range(320):
        x, y = random.randrange(w), random.randrange(h)
        c = random.choice([(54, 75, 99), (76, 104, 133), (37, 54, 76)])
        draw.point((x, y), fill=c)
    for x in range(0, w, 90):
        draw.line((x, 0, x, h), fill=(26, 44, 64), width=1)
    for y in range(0, h, 90):
        draw.line((0, y, w, y), fill=(26, 44, 64), width=1)


def draw_house(draw, x, y, scale=1.0, lit=True):
    roof = [(x, y + 145 * scale), (x + 260 * scale, y), (x + 520 * scale, y + 145 * scale)]
    draw.polygon(roof, fill=(74, 55, 46))
    rounded(draw, (x + 55 * scale, y + 140 * scale, x + 465 * scale, y + 460 * scale), int(18 * scale), HOUSE)
    draw.rectangle((x + 225 * scale, y + 270 * scale, x + 315 * scale, y + 460 * scale), fill=(58, 42, 36))
    if lit:
        draw.rectangle((x + 110 * scale, y + 205 * scale, x + 205 * scale, y + 300 * scale), fill=(255, 218, 119))
        draw.rectangle((x + 330 * scale, y + 205 * scale, x + 425 * scale, y + 300 * scale), fill=(255, 218, 119))
        draw.line((x + 157 * scale, y + 205 * scale, x + 157 * scale, y + 300 * scale), fill=HOUSE, width=int(5 * scale))
        draw.line((x + 110 * scale, y + 252 * scale, x + 205 * scale, y + 252 * scale), fill=HOUSE, width=int(5 * scale))
    else:
        draw.rectangle((x + 110 * scale, y + 205 * scale, x + 205 * scale, y + 300 * scale), fill=(44, 39, 38))
        draw.rectangle((x + 330 * scale, y + 205 * scale, x + 425 * scale, y + 300 * scale), fill=(44, 39, 38))


def draw_city(draw, x, y, scale=1.0):
    colors = [(50, 83, 124), (34, 120, 135), (63, 73, 118), (35, 58, 88)]
    for i in range(8):
        bw = random.randint(48, 86) * scale
        bh = random.randint(180, 390) * scale
        bx = x + i * 74 * scale
        by = y + 420 * scale - bh
        draw.rectangle((bx, by, bx + bw, y + 420 * scale), fill=colors[i % len(colors)])
        for wy in range(int(by + 30 * scale), int(y + 395 * scale), int(48 * scale)):
            draw.rectangle((bx + 16 * scale, wy, bx + 30 * scale, wy + 16 * scale), fill=YELLOW if i % 2 else CYAN)


def draw_info_stream(draw, x1, y1, x2, y2, count=8):
    for i in range(count):
        t = i / max(1, count - 1)
        x = x1 + (x2 - x1) * t
        y = y1 + math.sin(t * math.pi * 2) * 40 + (y2 - y1) * t
        col = [CYAN, BLUE, ORANGE, YELLOW][i % 4]
        draw.line((x, y, x + 150, y - 60), fill=col, width=5)
        draw.ellipse((x + 145, y - 66, x + 165, y - 46), fill=col)


def title_card():
    w, h = 2500, 1000
    im = Image.new("RGBA", (w, h), NIGHT + (255,))
    draw = ImageDraw.Draw(im)
    starfield(draw, w, h)
    draw.polygon([(1420, 0), (2500, 0), (2500, 1000), (1600, 1000)], fill=(12, 25, 38))
    draw_city(draw, 1680, 320, 1.1)
    draw_info_stream(draw, 1410, 280, 2210, 260, 9)
    draw_house(draw, 1510, 455, 0.95, lit=True)
    # open window glow
    draw.polygon([(1785, 575), (1940, 510), (1938, 640), (1785, 690)], fill=(255, 224, 132, 130))

    draw.text((115, 115), "人变老", fill=BLUE, font=F["title"])
    draw.text((115, 285), "停止更新", fill=INK, font=F["mega"])
    draw.text((128, 540), "不是年龄，是不再接收变化", fill=ORANGE, font=F["h2"])
    rounded(draw, (130, 745, 875, 835), 28, (34, 50, 66), outline=(69, 90, 110), width=3)
    draw.text((170, 768), "新信息  新尝试  新能力", fill=CYAN, font=F["tag"])
    save(im, "01-title-5x2.png")


def old_house_loop():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), NIGHT + (255,))
    draw = ImageDraw.Draw(im)
    starfield(draw, w, h, seed=8)
    draw.text((76, 58), "脑子里的老宅", fill=INK, font=F["h1"])
    draw.text((82, 142), "熟悉很安全，但也会让信息停止流动", fill=MUTED, font=F["h2"])
    draw_house(draw, 130, 330, 1.0, lit=True)
    # loop arrows
    center = (975, 505)
    r = 210
    for i, label in enumerate(["熟悉信息", "熟悉话题", "熟悉判断", "熟悉抱怨"]):
        ang = math.radians(i * 90 - 35)
        x = center[0] + math.cos(ang) * r
        y = center[1] + math.sin(ang) * r
        shadow_card(im, (x - 115, y - 48, x + 115, y + 48), r=24, fill=(235, 241, 238), shadow=(0, 0, 0, 65))
        draw = ImageDraw.Draw(im)
        draw.text((x - 78, y - 20), label, fill=(38, 50, 55), font=F["small"])
    draw.arc((center[0] - r, center[1] - r, center[0] + r, center[1] + r), 25, 330, fill=ORANGE, width=10)
    draw.polygon([(center[0] + 200, center[1] - 40), (center[0] + 250, center[1] - 25), (center[0] + 210, center[1] + 12)], fill=ORANGE)
    draw.text((760, 755), "稳定，也会僵硬", fill=CYAN, font=F["h2"])
    save(im, "02-old-house-loop.png")


def change_interaction():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (238, 243, 241, 255))
    draw = ImageDraw.Draw(im)
    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(220, 230, 227), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(220, 230, 227), width=1)
    draw.text((76, 58), "年轻是一种交互状态", fill=(28, 42, 48), font=F["h1"])
    draw.text((82, 142), "新信息 -> 新尝试 -> 新反馈 -> 新能力", fill=(88, 109, 113), font=F["h2"])

    steps = [
        ("新信息", "工具 / 观点 / 人群", BLUE),
        ("新理解", "重新解释世界", CYAN),
        ("新尝试", "做一个小作品", ORANGE),
        ("新反馈", "数据和真实评价", (97, 121, 202)),
        ("新能力", "沉淀成方法", (35, 142, 116)),
    ]
    x0, y = 100, 400
    for i, (title, sub, col) in enumerate(steps):
        x = x0 + i * 290
        shadow_card(im, (x, y, x + 220, y + 190), r=28, fill=WHITE, shadow=(54, 72, 78, 35))
        draw = ImageDraw.Draw(im)
        draw.ellipse((x + 76, y + 30, x + 144, y + 98), fill=col)
        draw.text((x + 48, y + 112), title, fill=(28, 42, 48), font=F["h2"])
        draw.text((x + 38, y + 160), sub, fill=(106, 120, 120), font=F["small"])
        if i < len(steps) - 1:
            draw.line((x + 220, y + 95, x + 288, y + 95), fill=col, width=8)
            draw.polygon([(x + 288, y + 95), (x + 258, y + 78), (x + 258, y + 112)], fill=col)
    save(im, "03-change-interaction.png")


def update_system():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (18, 28, 35, 255))
    draw = ImageDraw.Draw(im)
    starfield(draw, w, h, seed=16)
    draw.text((76, 58), "AI 时代淘汰停止更新的人", fill=INK, font=F["h1"])
    draw.text((82, 142), "不是年龄问题，是系统还更不更新", fill=MUTED, font=F["h2"])

    shadow_card(im, (90, 260, 665, 720), r=34, fill=(241, 246, 244), shadow=(0, 0, 0, 80))
    draw = ImageDraw.Draw(im)
    draw.text((140, 315), "旧系统", fill=(46, 57, 62), font=F["h2"])
    old_items = ["只信旧经验", "只看熟悉信息", "只会抱怨变化", "不愿意试工具"]
    for i, t in enumerate(old_items):
        draw.text((145, 405 + i * 58), t, fill=(108, 117, 118), font=F["body"])

    shadow_card(im, (930, 260, 1505, 720), r=34, fill=(236, 250, 248), shadow=(0, 0, 0, 80))
    draw = ImageDraw.Draw(im)
    draw.text((980, 315), "更新系统", fill=(24, 110, 120), font=F["h2"])
    new_items = ["试一个新工具", "学一个新流程", "和高手交流", "做一个小作品"]
    for i, t in enumerate(new_items):
        yy = 405 + i * 58
        draw.ellipse((982, yy + 7, 1012, yy + 37), fill=CYAN if i % 2 else ORANGE)
        draw.text((1030, yy), t, fill=(33, 53, 56), font=F["body"])

    draw.line((680, 490, 910, 490), fill=ORANGE, width=14)
    draw.polygon([(910, 490), (850, 460), (850, 520)], fill=ORANGE)
    draw.text((710, 425), "从焦虑到行动", fill=ORANGE, font=F["tag"])
    save(im, "04-update-system.png")


if __name__ == "__main__":
    title_card()
    old_house_loop()
    change_interaction()
    update_system()
