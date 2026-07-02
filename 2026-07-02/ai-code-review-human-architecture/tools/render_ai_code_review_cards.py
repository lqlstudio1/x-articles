from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
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
    "title": font(138, True),
    "title_big": font(170, True),
    "subtitle": font(52, True),
    "h1": font(78, True),
    "h2": font(48, True),
    "body": font(34, False),
    "small": font(26, False),
    "tag": font(30, True),
}


COLORS = {
    "ink": (20, 29, 43),
    "navy": (17, 33, 59),
    "blue": (43, 104, 191),
    "cyan": (74, 190, 255),
    "orange": (255, 143, 62),
    "paper": (244, 247, 250),
    "muted": (118, 132, 151),
    "line": (187, 203, 222),
    "green": (51, 178, 129),
    "white": (255, 255, 255),
}


def text_size(draw, text, ft):
    box = draw.textbbox((0, 0), text, font=ft)
    return box[2] - box[0], box[3] - box[1]


def rounded(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def shadow_card(base, xy, r=28, fill=(255, 255, 255), shadow=(20, 30, 50, 45), offset=(0, 16), blur=24):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = xy
    d.rounded_rectangle((x1 + offset[0], y1 + offset[1], x2 + offset[0], y2 + offset[1]), radius=r, fill=shadow)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)
    ImageDraw.Draw(base).rounded_rectangle(xy, radius=r, fill=fill)


def blueprint_grid(draw, w, h, step=64):
    for x in range(0, w, step):
        draw.line((x, 0, x, h), fill=(221, 230, 241), width=1)
    for y in range(0, h, step):
        draw.line((0, y, w, y), fill=(221, 230, 241), width=1)
    for x in range(0, w, step * 4):
        draw.line((x, 0, x, h), fill=(201, 216, 234), width=2)
    for y in range(0, h, step * 4):
        draw.line((0, y, w, y), fill=(201, 216, 234), width=2)


def draw_code_panel(draw, xy, title="agent diff", rows=6):
    x1, y1, x2, y2 = xy
    rounded(draw, xy, 24, (23, 35, 55), outline=(65, 99, 145), width=2)
    draw.rectangle((x1, y1, x2, y1 + 54), fill=(31, 49, 76))
    draw.text((x1 + 24, y1 + 14), title, fill=(215, 228, 245), font=F["small"])
    colors = [COLORS["cyan"], COLORS["green"], COLORS["orange"], (171, 188, 212)]
    for i in range(rows):
        yy = y1 + 86 + i * 42
        draw.rounded_rectangle((x1 + 26, yy, x1 + 58, yy + 16), radius=8, fill=colors[i % len(colors)])
        draw.line((x1 + 78, yy + 8, x2 - 38 - i * 18, yy + 8), fill=(132, 157, 188), width=8)


def draw_architecture_nodes(draw, xy, accent=COLORS["orange"]):
    x1, y1, x2, y2 = xy
    nodes = [
        (x1 + 80, y1 + 95, "UI"),
        (x1 + 280, y1 + 80, "API"),
        (x1 + 500, y1 + 110, "Auth"),
        (x1 + 210, y1 + 260, "State"),
        (x1 + 460, y1 + 300, "DB"),
    ]
    lines = [(0, 1), (1, 2), (1, 3), (3, 4), (2, 4)]
    for a, b in lines:
        ax, ay, _ = nodes[a]
        bx, by, _ = nodes[b]
        draw.line((ax + 50, ay + 28, bx + 50, by + 28), fill=(87, 121, 169), width=4)
    for nx, ny, label in nodes:
        rounded(draw, (nx, ny, nx + 108, ny + 58), 18, (240, 247, 255), outline=(67, 119, 190), width=3)
        tw, th = text_size(draw, label, F["small"])
        draw.text((nx + 54 - tw / 2, ny + 29 - th / 2 - 2), label, fill=COLORS["navy"], font=F["small"])
    draw.arc((x1 + 325, y1 + 10, x1 + 625, y1 + 310), start=22, end=342, fill=accent, width=7)
    draw.polygon([(x1 + 592, y1 + 64), (x1 + 640, y1 + 54), (x1 + 611, y1 + 95)], fill=accent)


def draw_developer_scene(draw, x, y, scale=1.0):
    # desk
    draw.rounded_rectangle((x, y + 330 * scale, x + 680 * scale, y + 380 * scale), radius=int(18 * scale), fill=(183, 141, 103))
    # monitor
    rounded(draw, (x + 80 * scale, y + 35 * scale, x + 560 * scale, y + 315 * scale), int(24 * scale), (17, 31, 52), outline=(78, 118, 166), width=int(3 * scale))
    draw.rectangle((x + 285 * scale, y + 315 * scale, x + 355 * scale, y + 350 * scale), fill=(63, 82, 108))
    rounded(draw, (x + 235 * scale, y + 348 * scale, x + 405 * scale, y + 368 * scale), int(10 * scale), (63, 82, 108))
    # code lines
    for i in range(7):
        yy = y + (78 + i * 30) * scale
        color = [COLORS["cyan"], COLORS["green"], COLORS["orange"], (155, 176, 204)][i % 4]
        draw.line((x + 125 * scale, yy, x + (315 + i * 24) * scale, yy), fill=color, width=int(7 * scale))
        draw.line((x + 380 * scale, yy, x + 510 * scale, yy), fill=(116, 145, 181), width=int(7 * scale))
    # person
    draw.ellipse((x + 580 * scale, y + 170 * scale, x + 650 * scale, y + 240 * scale), fill=(242, 190, 148))
    draw.pieslice((x + 565 * scale, y + 150 * scale, x + 665 * scale, y + 242 * scale), 180, 360, fill=(32, 39, 52))
    draw.rounded_rectangle((x + 560 * scale, y + 245 * scale, x + 672 * scale, y + 345 * scale), radius=int(28 * scale), fill=(45, 88, 142))
    # laptop
    rounded(draw, (x + 430 * scale, y + 260 * scale, x + 590 * scale, y + 348 * scale), int(14 * scale), (235, 243, 250), outline=(120, 144, 170), width=int(2 * scale))
    draw.line((x + 405 * scale, y + 352 * scale, x + 612 * scale, y + 352 * scale), fill=(87, 103, 124), width=int(8 * scale))


def save(im, name):
    path = ASSETS / name
    im.convert("RGB").save(path, quality=95)
    print(path)


def title_card():
    w, h = 2500, 1000
    im = Image.new("RGBA", (w, h), COLORS["paper"] + (255,))
    draw = ImageDraw.Draw(im)
    blueprint_grid(draw, w, h, 70)

    # diagonal blueprint block
    draw.polygon([(1360, 0), (2500, 0), (2500, 1000), (1670, 1000)], fill=(29, 56, 98))
    for i in range(-200, 1300, 105):
        draw.line((1500 + i, 0, 1880 + i, 1000), fill=(41, 77, 132), width=3)

    draw.text((120, 120), "AI代码", fill=COLORS["blue"], font=F["title"])
    draw.text((120, 285), "别审每行", fill=COLORS["ink"], font=F["title_big"])
    draw.text((130, 505), "人要审的是架构", fill=COLORS["orange"], font=F["subtitle"])

    rounded(draw, (130, 710, 915, 805), 28, (255, 255, 255), outline=COLORS["line"], width=3)
    draw.text((172, 732), "测试管行为  AI查规范  人看设计", fill=COLORS["navy"], font=F["tag"])

    draw_developer_scene(draw, 1420, 235, 0.95)
    shadow_card(im, (1660, 90, 2340, 430), r=34, fill=(247, 251, 255), shadow=(0, 0, 0, 70), offset=(0, 22), blur=22)
    d = ImageDraw.Draw(im)
    d.text((1705, 130), "ARCHITECTURE", fill=COLORS["blue"], font=F["h2"])
    draw_architecture_nodes(d, (1705, 175, 2320, 420))

    # orange pointer
    d.line((1220, 652, 1642, 362), fill=COLORS["orange"], width=10)
    d.polygon([(1642, 362), (1580, 360), (1611, 415)], fill=COLORS["orange"])

    save(im, "01-title-5x2.png")


def review_layers():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (242, 247, 251, 255))
    draw = ImageDraw.Draw(im)
    blueprint_grid(draw, w, h, 58)
    draw.text((80, 58), "Review 分三层", fill=COLORS["ink"], font=F["h1"])
    draw.text((84, 145), "不是所有问题都该让人肉眼查", fill=COLORS["muted"], font=F["h2"])

    cards = [
        (90, 250, 500, 720, "机器检查", "lint / type / test / build", COLORS["green"], ["可自动验证", "失败就阻断", "不靠感觉"]),
        (595, 250, 1005, 720, "AI Review", "规范 / 边界 / 重复代码", COLORS["blue"], ["查局部问题", "对照团队规范", "生成风险摘要"]),
        (1100, 250, 1510, 720, "人工 Review", "架构 / 边界 / 长期成本", COLORS["orange"], ["模块该不该存在", "状态放在哪里", "未来是否难维护"]),
    ]
    for x1, y1, x2, y2, title, sub, accent, bullets in cards:
        shadow_card(im, (x1, y1, x2, y2), r=34, fill=COLORS["white"], shadow=(25, 44, 70, 38), offset=(0, 14), blur=18)
        draw = ImageDraw.Draw(im)
        draw.rounded_rectangle((x1, y1, x2, y1 + 18), radius=9, fill=accent)
        draw.text((x1 + 36, y1 + 48), title, fill=COLORS["ink"], font=F["h2"])
        draw.text((x1 + 38, y1 + 116), sub, fill=accent, font=F["small"])
        yy = y1 + 195
        for b in bullets:
            draw.ellipse((x1 + 42, yy + 10, x1 + 64, yy + 32), fill=accent)
            draw.text((x1 + 84, yy), b, fill=COLORS["navy"], font=F["body"])
            yy += 72
    draw.line((500, 485, 595, 485), fill=COLORS["line"], width=8)
    draw.polygon([(595, 485), (560, 465), (560, 505)], fill=COLORS["line"])
    draw.line((1005, 485, 1100, 485), fill=COLORS["line"], width=8)
    draw.polygon([(1100, 485), (1065, 465), (1065, 505)], fill=COLORS["line"])
    save(im, "02-review-layers.png")


def architecture_lens():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (22, 36, 58, 255))
    draw = ImageDraw.Draw(im)
    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(32, 52, 82), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(32, 52, 82), width=1)
    draw.text((78, 60), "先看设计摘要", fill=(238, 246, 255), font=F["h1"])
    draw.text((82, 150), "再决定要不要读代码", fill=(137, 172, 218), font=F["h2"])

    shadow_card(im, (86, 255, 640, 760), r=28, fill=(246, 250, 255), shadow=(0, 0, 0, 85), offset=(0, 18), blur=24)
    draw = ImageDraw.Draw(im)
    draw.text((132, 302), "Commit 摘要", fill=COLORS["blue"], font=F["h2"])
    rows = ["改了哪些模块", "为什么这样改", "影响哪些接口", "哪些地方重点看"]
    for i, row in enumerate(rows):
        yy = 390 + i * 76
        draw.rounded_rectangle((132, yy, 182, yy + 38), radius=12, fill=COLORS["orange"] if i == 1 else COLORS["blue"])
        draw.text((205, yy - 3), row, fill=COLORS["ink"], font=F["body"])

    shadow_card(im, (790, 170, 1505, 790), r=30, fill=(237, 246, 255), shadow=(0, 0, 0, 90), offset=(0, 20), blur=26)
    draw = ImageDraw.Draw(im)
    draw.text((838, 218), "架构图", fill=COLORS["blue"], font=F["h2"])
    draw_architecture_nodes(draw, (850, 280, 1450, 660), accent=COLORS["orange"])

    # magnifier
    draw.ellipse((1090, 370, 1408, 688), outline=COLORS["orange"], width=14)
    draw.line((1342, 636, 1500, 790), fill=COLORS["orange"], width=22)
    draw.line((1342, 636, 1500, 790), fill=(255, 194, 121), width=8)
    draw.text((890, 700), "人审方向、边界、长期成本", fill=COLORS["navy"], font=F["body"])
    save(im, "03-architecture-lens.png")


def design_memory():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (248, 246, 238, 255))
    draw = ImageDraw.Draw(im)
    # warm paper texture
    random.seed(7)
    for _ in range(900):
        x, y = random.randrange(w), random.randrange(h)
        c = random.randrange(220, 242)
        draw.point((x, y), fill=(c, c - 4, c - 12))
    draw.text((76, 56), "维护设计记忆", fill=COLORS["ink"], font=F["h1"])
    draw.text((80, 145), "让人和 AI 都少走弯路", fill=(102, 98, 87), font=F["h2"])

    # laptop / docs scene
    shadow_card(im, (100, 245, 690, 730), r=32, fill=(255, 255, 255), shadow=(80, 64, 35, 45), offset=(0, 16), blur=20)
    draw = ImageDraw.Draw(im)
    draw.text((146, 292), "Project Memory", fill=COLORS["blue"], font=F["h2"])
    docs = [("AGENTS.md", COLORS["orange"]), ("knowledge_map.md", COLORS["blue"]), ("mistakes.md", COLORS["green"]), ("progress.md", (128, 98, 190))]
    for i, (name, color) in enumerate(docs):
        yy = 380 + i * 72
        draw.rounded_rectangle((150, yy, 630, yy + 48), radius=16, fill=(244, 247, 250), outline=(222, 228, 235), width=2)
        draw.rectangle((150, yy, 168, yy + 48), fill=color)
        draw.text((190, yy + 6), name, fill=COLORS["ink"], font=F["body"])

    # AI / human sides
    shadow_card(im, (880, 245, 1480, 730), r=32, fill=(22, 36, 58), shadow=(80, 64, 35, 45), offset=(0, 16), blur=20)
    draw = ImageDraw.Draw(im)
    draw.text((930, 295), "下一次任务", fill=(239, 247, 255), font=F["h2"])
    draw_code_panel(draw, (930, 380, 1230, 630), title="AI reads docs", rows=4)
    # human icon and arrows
    draw.ellipse((1295, 398, 1375, 478), fill=(242, 190, 148))
    draw.pieslice((1284, 380, 1386, 476), 180, 360, fill=(37, 43, 55))
    draw.rounded_rectangle((1275, 500, 1398, 635), radius=32, fill=(67, 119, 190))
    draw.text((1260, 665), "人看设计", fill=(210, 226, 247), font=F["small"])

    draw.line((700, 490, 870, 490), fill=COLORS["orange"], width=12)
    draw.polygon([(870, 490), (820, 462), (820, 518)], fill=COLORS["orange"])
    draw.text((700, 430), "每次修改后更新", fill=COLORS["orange"], font=F["tag"])
    save(im, "04-design-memory.png")


if __name__ == "__main__":
    title_card()
    review_layers()
    architecture_lens()
    design_memory()
