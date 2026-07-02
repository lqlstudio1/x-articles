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
    "mega": font(190, True),
    "title": font(118, True),
    "h1": font(74, True),
    "h2": font(48, True),
    "body": font(34, False),
    "small": font(25, False),
    "tag": font(30, True),
}

INK = (28, 37, 34)
GREEN = (18, 85, 76)
TEAL = (31, 132, 121)
ORANGE = (248, 115, 48)
YELLOW = (255, 190, 84)
PAPER = (247, 244, 234)
MUTED = (116, 122, 111)
LINE = (218, 210, 190)
WHITE = (255, 255, 255)


def rounded(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def shadow_card(im, xy, r=26, fill=WHITE, shadow=(70, 54, 28, 42), offset=(0, 14), blur=18):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = xy
    d.rounded_rectangle((x1 + offset[0], y1 + offset[1], x2 + offset[0], y2 + offset[1]), radius=r, fill=shadow)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(layer)
    ImageDraw.Draw(im).rounded_rectangle(xy, radius=r, fill=fill)


def text_size(draw, text, ft):
    box = draw.textbbox((0, 0), text, font=ft)
    return box[2] - box[0], box[3] - box[1]


def paper_texture(draw, w, h, seed=12):
    random.seed(seed)
    for _ in range(1700):
        x, y = random.randrange(w), random.randrange(h)
        v = random.randrange(-10, 10)
        base = (247 + v, 244 + v, 234 + v)
        draw.point((x, y), fill=base)
    for x in range(0, w, 84):
        draw.line((x, 0, x, h), fill=(234, 228, 211), width=1)
    for y in range(0, h, 84):
        draw.line((0, y, w, y), fill=(234, 228, 211), width=1)


def draw_laptop(draw, x, y, scale=1.0):
    rounded(draw, (x, y, x + 430 * scale, y + 260 * scale), int(22 * scale), (31, 42, 48), outline=(74, 91, 91), width=int(3 * scale))
    draw.rectangle((x + 20 * scale, y + 25 * scale, x + 410 * scale, y + 238 * scale), fill=(18, 32, 38))
    for i, col in enumerate([TEAL, ORANGE, YELLOW, (147, 166, 161), TEAL]):
        yy = y + (60 + i * 34) * scale
        draw.line((x + 55 * scale, yy, x + (350 - i * 24) * scale, yy), fill=col, width=int(8 * scale))
    draw.rectangle((x + 176 * scale, y + 260 * scale, x + 250 * scale, y + 300 * scale), fill=(88, 104, 105))
    rounded(draw, (x + 105 * scale, y + 297 * scale, x + 320 * scale, y + 320 * scale), int(10 * scale), (88, 104, 105))


def draw_invoice(draw, x, y, scale=1.0):
    rounded(draw, (x, y, x + 210 * scale, y + 270 * scale), int(20 * scale), WHITE, outline=LINE, width=int(2 * scale))
    draw.text((x + 24 * scale, y + 28 * scale), "交付单", fill=GREEN, font=font(int(30 * scale), True))
    for i in range(5):
        yy = y + (88 + i * 34) * scale
        draw.line((x + 24 * scale, yy, x + (172 - i * 12) * scale, yy), fill=(187, 178, 157), width=int(5 * scale))
    draw.rounded_rectangle((x + 24 * scale, y + 218 * scale, x + 120 * scale, y + 246 * scale), radius=int(8 * scale), fill=ORANGE)


def draw_path_icon(draw, cx, cy, kind, color):
    if kind == "paint":
        draw.ellipse((cx - 34, cy - 30, cx + 40, cy + 36), fill=color)
        for dx, dy in [(-15, -6), (8, -13), (20, 8)]:
            draw.ellipse((cx + dx - 7, cy + dy - 7, cx + dx + 7, cy + dy + 7), fill=WHITE)
        draw.line((cx + 20, cy + 20, cx + 58, cy + 60), fill=INK, width=8)
    elif kind == "write":
        rounded(draw, (cx - 42, cy - 42, cx + 48, cy + 46), 12, (245, 247, 242), outline=color, width=4)
        for i in range(4):
            draw.line((cx - 22, cy - 16 + i * 18, cx + 25, cy - 16 + i * 18), fill=color, width=5)
    elif kind == "video":
        rounded(draw, (cx - 50, cy - 38, cx + 55, cy + 42), 14, color)
        draw.polygon([(cx - 8, cy - 18), (cx - 8, cy + 20), (cx + 25, cy + 2)], fill=WHITE)
    elif kind == "bot":
        rounded(draw, (cx - 48, cy - 34, cx + 48, cy + 42), 20, color)
        draw.ellipse((cx - 22, cy - 6, cx - 8, cy + 8), fill=WHITE)
        draw.ellipse((cx + 12, cy - 6, cx + 26, cy + 8), fill=WHITE)
        draw.line((cx, cy - 34, cx, cy - 58), fill=color, width=6)
        draw.ellipse((cx - 8, cy - 68, cx + 8, cy - 52), fill=ORANGE)
    elif kind == "course":
        rounded(draw, (cx - 50, cy - 45, cx + 45, cy + 40), 10, (245, 247, 242), outline=color, width=4)
        draw.rectangle((cx - 50, cy - 45, cx - 24, cy + 40), fill=color)
        draw.line((cx - 10, cy - 14, cx + 25, cy - 14), fill=color, width=5)
        draw.line((cx - 10, cy + 8, cx + 18, cy + 8), fill=color, width=5)
    elif kind == "flow":
        points = [(cx - 55, cy - 25), (cx, cy - 25), (cx, cy + 28), (cx + 58, cy + 28)]
        draw.line(points, fill=color, width=8, joint="curve")
        for px, py in [(cx - 55, cy - 25), (cx, cy - 25), (cx, cy + 28), (cx + 58, cy + 28)]:
            draw.ellipse((px - 16, py - 16, px + 16, py + 16), fill=WHITE, outline=color, width=5)


def save(im, name):
    path = ASSETS / name
    im.convert("RGB").save(path, quality=95)
    print(path)


def title_card():
    w, h = 2500, 1000
    im = Image.new("RGBA", (w, h), PAPER + (255,))
    draw = ImageDraw.Draw(im)
    paper_texture(draw, w, h)
    draw.polygon([(1425, 0), (2500, 0), (2500, 1000), (1600, 1000)], fill=(23, 91, 82))
    for i in range(-200, 1100, 110):
        draw.line((1500 + i, 0, 1780 + i, 1000), fill=(34, 112, 102), width=4)

    draw.text((115, 105), "2026 AI赚钱", fill=TEAL, font=F["title"])
    draw.text((115, 278), "6条路", fill=INK, font=F["mega"])
    draw.text((128, 540), "别追工具，先看交付物", fill=ORANGE, font=F["h2"])
    rounded(draw, (130, 745, 895, 835), 28, WHITE, outline=LINE, width=3)
    draw.text((170, 768), "可验收  可复购  可维护", fill=GREEN, font=F["tag"])

    # right scene: workbench
    draw.rounded_rectangle((1510, 725, 2380, 780), radius=22, fill=(167, 122, 78))
    draw_laptop(draw, 1655, 430, 0.98)
    draw_invoice(draw, 2150, 355, 0.9)

    labels = [
        ("绘画", "paint", ORANGE, 1525, 110),
        ("写作", "write", TEAL, 1765, 105),
        ("数字人", "video", YELLOW, 2030, 120),
        ("客服", "bot", (69, 139, 203), 1515, 270),
        ("课程", "course", (126, 102, 190), 1785, 270),
        ("自动化", "flow", (42, 157, 110), 2050, 280),
    ]
    for txt, kind, col, x, y in labels:
        shadow_card(im, (x, y, x + 210, y + 120), r=24, fill=(251, 250, 243), shadow=(0, 0, 0, 44), offset=(0, 12), blur=16)
        draw = ImageDraw.Draw(im)
        draw_path_icon(draw, x + 58, y + 60, kind, col)
        draw.text((x + 112, y + 41), txt, fill=INK, font=F["small"])

    draw.line((1210, 650, 1510, 520), fill=ORANGE, width=12)
    draw.polygon([(1510, 520), (1452, 512), (1488, 565)], fill=ORANGE)
    save(im, "01-title-5x2.png")


def six_paths_map():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), PAPER + (255,))
    draw = ImageDraw.Draw(im)
    paper_texture(draw, w, h, seed=18)
    draw.text((70, 55), "6 条能跑通的路", fill=INK, font=F["h1"])
    draw.text((74, 138), "本质都是把 AI 变成交付物", fill=MUTED, font=F["h2"])

    items = [
        ("01", "绘画定制", "视觉资产", "paint", ORANGE),
        ("02", "写作服务", "内容流水线", "write", TEAL),
        ("03", "数字人视频", "标准化表达", "video", YELLOW),
        ("04", "智能客服", "知识库 + 转人工", "bot", (69, 139, 203)),
        ("05", "知识付费", "行业经验 + AI", "course", (126, 102, 190)),
        ("06", "自动化工作流", "省时间的系统", "flow", (42, 157, 110)),
    ]
    x0, y0 = 70, 240
    cw, ch = 455, 245
    gapx, gapy = 55, 45
    for i, (num, title, sub, kind, col) in enumerate(items):
        colidx = i % 3
        row = i // 3
        x = x0 + colidx * (cw + gapx)
        y = y0 + row * (ch + gapy)
        shadow_card(im, (x, y, x + cw, y + ch), r=30, fill=WHITE, shadow=(74, 61, 34, 36), offset=(0, 12), blur=17)
        draw = ImageDraw.Draw(im)
        draw.text((x + 28, y + 24), num, fill=col, font=F["h2"])
        draw_path_icon(draw, x + 92, y + 130, kind, col)
        draw.text((x + 175, y + 72), title, fill=INK, font=F["h2"])
        draw.text((x + 178, y + 135), sub, fill=MUTED, font=F["body"])
        draw.rounded_rectangle((x + 176, y + 190, x + 360, y + 218), radius=14, fill=(244, 239, 225))
        draw.text((x + 194, y + 187), "可交付", fill=GREEN, font=F["small"])
    save(im, "02-six-paths-map.png")


def delivery_filter():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (20, 67, 62, 255))
    draw = ImageDraw.Draw(im)
    for x in range(0, w, 90):
        draw.line((x, 0, x, h), fill=(28, 82, 76), width=1)
    for y in range(0, h, 90):
        draw.line((0, y, w, y), fill=(28, 82, 76), width=1)
    draw.text((76, 58), "能跑通的共同点", fill=(250, 250, 240), font=F["h1"])
    draw.text((80, 142), "不是工具强，是交付清楚", fill=(174, 211, 201), font=F["h2"])

    # funnel
    funnel = [(150, 270), (760, 270), (630, 480), (520, 480), (520, 650), (390, 720), (390, 480), (280, 480)]
    draw.polygon(funnel, fill=(240, 247, 235), outline=(144, 196, 184))
    draw.line((250, 372, 662, 372), fill=LINE, width=4)
    draw.line((310, 480, 630, 480), fill=LINE, width=4)
    draw.text((245, 305), "需求明确", fill=GREEN, font=F["h2"])
    draw.text((330, 410), "结果可验收", fill=GREEN, font=F["h2"])
    draw.text((395, 535), "能复购", fill=GREEN, font=F["h2"])

    # checklist panel
    shadow_card(im, (895, 245, 1490, 725), r=34, fill=(249, 248, 238), shadow=(0, 0, 0, 86), offset=(0, 18), blur=24)
    draw = ImageDraw.Draw(im)
    draw.text((945, 295), "交付过滤器", fill=GREEN, font=F["h2"])
    checks = [
        ("客户是否真有痛点？", ORANGE),
        ("结果能否被验收？", TEAL),
        ("能否形成复购？", (42, 157, 110)),
        ("维护成本是否可控？", (69, 139, 203)),
    ]
    for i, (txt, col) in enumerate(checks):
        yy = 390 + i * 72
        draw.ellipse((950, yy, 987, yy + 37), fill=col)
        draw.line((959, yy + 20, 968, yy + 29), fill=WHITE, width=4)
        draw.line((968, yy + 29, 981, yy + 9), fill=WHITE, width=4)
        draw.text((1018, yy - 4), txt, fill=INK, font=F["body"])
    draw.rounded_rectangle((945, 660, 1378, 703), radius=18, fill=ORANGE)
    draw.text((970, 664), "没有验收标准，就先别卖", fill=WHITE, font=F["small"])
    save(im, "03-delivery-filter.png")


def programmer_priority():
    w, h = 1600, 900
    im = Image.new("RGBA", (w, h), (246, 246, 238, 255))
    draw = ImageDraw.Draw(im)
    paper_texture(draw, w, h, seed=33)
    draw.text((72, 58), "程序员优先看这两条", fill=INK, font=F["h1"])
    draw.text((76, 142), "客服系统 + 自动化工作流，更像长期生意", fill=MUTED, font=F["h2"])

    # terminal panel
    shadow_card(im, (80, 250, 720, 735), r=32, fill=(25, 38, 42), shadow=(70, 54, 28, 44), offset=(0, 16), blur=20)
    draw = ImageDraw.Draw(im)
    draw.text((126, 300), "AI Automation Stack", fill=(227, 247, 239), font=F["h2"])
    lines = [
        ("Coze", "客服入口"),
        ("Dify", "知识库 / RAG"),
        ("n8n", "流程编排"),
        ("Script", "定制逻辑"),
        ("Feishu", "通知 / 审核"),
    ]
    for i, (a, b) in enumerate(lines):
        yy = 390 + i * 58
        draw.text((130, yy), f"> {a}", fill=YELLOW if i == 2 else TEAL, font=F["body"])
        draw.text((300, yy), b, fill=(198, 215, 207), font=F["body"])

    # workflow cards
    cards = [
        (875, 250, 1450, 390, "智能客服", "FAQ -> 知识库 -> 转人工 -> 月维护", ORANGE),
        (875, 455, 1450, 595, "自动化工作流", "表单 -> AI 判断 -> 分配 -> 提醒", TEAL),
        (875, 660, 1450, 800, "收费逻辑", "按节省时间和减少错误报价", (42, 157, 110)),
    ]
    for x1, y1, x2, y2, title, sub, col in cards:
        shadow_card(im, (x1, y1, x2, y2), r=28, fill=WHITE, shadow=(70, 54, 28, 34), offset=(0, 12), blur=16)
        draw = ImageDraw.Draw(im)
        draw.rounded_rectangle((x1, y1, x1 + 18, y2), radius=9, fill=col)
        draw.text((x1 + 44, y1 + 30), title, fill=INK, font=F["h2"])
        draw.text((x1 + 48, y1 + 88), sub, fill=MUTED, font=F["small"])
    # arrows
    draw.line((720, 492, 855, 320), fill=ORANGE, width=10)
    draw.polygon([(855, 320), (800, 326), (832, 365)], fill=ORANGE)
    draw.line((720, 492, 855, 525), fill=TEAL, width=10)
    draw.polygon([(855, 525), (805, 500), (798, 550)], fill=TEAL)
    save(im, "04-programmer-priority.png")


if __name__ == "__main__":
    title_card()
    six_paths_map()
    delivery_filter()
    programmer_priority()
