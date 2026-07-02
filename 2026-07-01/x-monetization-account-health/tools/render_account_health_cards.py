from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf"),
]


def font(size):
    for path in FONT_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size=size, index=0)
    return ImageFont.load_default()


def text(draw, xy, value, fnt, fill, stroke=0, stroke_fill="#000000"):
    draw.text(xy, value, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def text_box(draw, value, fnt):
    box = draw.textbbox((0, 0), value, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def paper_bg(w, h, seed=1):
    random.seed(seed)
    img = Image.new("RGB", (w, h), "#F7F4EF")
    px = img.load()
    for y in range(h):
        for x in range(w):
            noise = random.randint(-5, 5)
            base = 246 + noise
            px[x, y] = (
                max(0, min(255, base)),
                max(0, min(255, base - 3)),
                max(0, min(255, base - 8)),
            )
    img = img.filter(ImageFilter.GaussianBlur(0.2))
    d = ImageDraw.Draw(img, "RGBA")
    for _ in range(90):
        x = random.randint(0, w)
        y = random.randint(0, h)
        r = random.randint(1, 3)
        d.ellipse((x, y, x + r, y + r), fill=(20, 20, 20, random.randint(10, 24)))
    return img


def red_brush(draw, w, h):
    red = (230, 0, 18, 235)
    draw.polygon(
        [
            (int(w * 0.55), 0),
            (w, 0),
            (w, h),
            (int(w * 0.67), h),
            (int(w * 0.78), int(h * 0.25)),
        ],
        fill=red,
    )
    for i in range(9):
        y = int(h * (0.06 + i * 0.095))
        draw.line((int(w * 0.62), y, w, y + random.randint(-50, 60)), fill=(230, 0, 18, 70), width=random.randint(12, 34))
    draw.polygon([(0, h), (int(w * 0.28), int(h * 0.78)), (int(w * 0.45), h)], fill=(230, 0, 18, 170))


def corner_marks(draw, box, color="#E60012", width=10, length=72):
    x1, y1, x2, y2 = box
    c = color
    draw.line((x1, y1, x1 + length, y1), fill=c, width=width)
    draw.line((x1, y1, x1, y1 + length), fill=c, width=width)
    draw.line((x2, y1, x2 - length, y1), fill=c, width=width)
    draw.line((x2, y1, x2, y1 + length), fill=c, width=width)
    draw.line((x1, y2, x1 + length, y2), fill=c, width=width)
    draw.line((x1, y2, x1, y2 - length), fill=c, width=width)
    draw.line((x2, y2, x2 - length, y2), fill=c, width=width)
    draw.line((x2, y2, x2, y2 - length), fill=c, width=width)


def tag(draw, xy, label, fill="#E60012", fg="#FFFFFF", size=40):
    f = font(size)
    x, y = xy
    tw, th = text_box(draw, label, f)
    draw.rounded_rectangle((x, y, x + tw + 48, y + th + 22), radius=18, fill=fill)
    text(draw, (x + 24, y + 8), label, f, fg)


def phone_card(draw, x, y, w, h, title, lines):
    draw.rounded_rectangle((x + 18, y + 18, x + w + 18, y + h + 18), radius=34, fill=(0, 0, 0, 55))
    draw.rounded_rectangle((x, y, x + w, y + h), radius=34, fill=(255, 255, 255, 238), outline="#FFFFFF", width=5)
    draw.rounded_rectangle((x + 28, y + 28, x + w - 28, y + 88), radius=18, fill="#050505")
    text(draw, (x + 55, y + 38), title, font(43), "#FFFFFF")
    cy = y + 130
    for label, bad in lines:
        mark = "x" if bad else "+"
        color = "#E60012" if bad else "#111111"
        text(draw, (x + 60, cy), mark, font(42), color)
        text(draw, (x + 112, cy + 2), label, font(39), "#050505")
        cy += 67


def save_title():
    w, h = 2500, 1000
    img = paper_bg(w, h, seed=71)
    d = ImageDraw.Draw(img, "RGBA")
    red_brush(d, w, h)
    corner_marks(d, (96, 115, 1360, 760), width=9, length=90)
    tag(d, (160, 116), "ACCOUNT HEALTH", "#050505", "#FFFFFF", 34)
    text(d, (155, 235), "别像", font(170), "#E60012", 4, "#FFFFFF")
    text(d, (570, 235), "机器人", font(170), "#050505", 4, "#FFFFFF")
    text(d, (170, 508), "收益化之前，先把账号养健康", font(72), "#050505", 3, "#FFFFFF")
    d.line((630, 615, 1130, 600), fill="#E60012", width=10)
    d.line((650, 645, 1060, 630), fill="#E60012", width=5)
    d.rounded_rectangle((180, 695, 1025, 790), radius=24, fill="#FFFFFF", outline="#E60012", width=6)
    text(d, (238, 710), "原创内容  /  真实互动  /  稳定节奏", font(48), "#050505")
    phone_card(
        d,
        1575,
        155,
        625,
        655,
        "高风险信号",
        [
            ("批量关注取关", True),
            ("复制粘贴评论", True),
            ("机械点赞转推", True),
            ("重复搬运素材", True),
            ("真实长评原创图", False),
        ],
    )
    draw_cursor(d, 2115, 780, 1.2)
    img.save(OUT / "01-title-5x2.png")


def draw_cursor(draw, x, y, scale=1.0):
    pts = [
        (x, y),
        (x + int(105 * scale), y + int(210 * scale)),
        (x + int(139 * scale), y + int(130 * scale)),
        (x + int(218 * scale), y + int(124 * scale)),
    ]
    draw.polygon(pts, fill="#FFFFFF", outline="#E60012")
    draw.line((pts[0], pts[1]), fill="#E60012", width=int(8 * scale))
    draw.line((pts[1], pts[2]), fill="#E60012", width=int(8 * scale))
    draw.line((pts[2], pts[3]), fill="#E60012", width=int(8 * scale))


def save_risk_behaviors():
    w, h = 1600, 900
    img = paper_bg(w, h, seed=72)
    d = ImageDraw.Draw(img, "RGBA")
    red_brush(d, w, h)
    text(d, (80, 72), "哪些行为像机器人", font(70), "#050505", 3, "#FFFFFF")
    text(d, (82, 165), "不是卡阈值，而是减少机器人特征", font(44), "#E60012")
    items = [
        ("关注取关", "短期交换关系"),
        ("复制评论", "同一句话刷多处"),
        ("机械互动", "连续点赞转推"),
        ("重复素材", "别人发过的图和视频"),
    ]
    positions = [(100, 310), (830, 310), (100, 560), (830, 560)]
    for idx, ((title, sub), (x, y)) in enumerate(zip(items, positions), 1):
        d.rounded_rectangle((x, y, x + 590, y + 170), radius=28, fill="#FFFFFF", outline="#050505", width=5)
        d.ellipse((x + 30, y + 42, x + 112, y + 124), fill="#E60012")
        text(d, (x + 58, y + 47), str(idx), font(48), "#FFFFFF")
        text(d, (x + 145, y + 38), title, font(52), "#050505")
        text(d, (x + 145, y + 105), sub, font(32), "#555555")
    img.save(OUT / "02-risk-behaviors.png")


def save_human_comment():
    w, h = 1600, 900
    img = paper_bg(w, h, seed=73)
    d = ImageDraw.Draw(img, "RGBA")
    red_brush(d, w, h)
    text(d, (80, 70), "评论要像人", font(74), "#E60012", 3, "#FFFFFF")
    text(d, (520, 70), "不要像任务", font(74), "#050505", 3, "#FFFFFF")
    d.rounded_rectangle((120, 280, 700, 700), radius=36, fill="#FFFFFF", outline="#050505", width=5)
    d.rounded_rectangle((900, 280, 1480, 700), radius=36, fill="#FFFFFF", outline="#E60012", width=5)
    text(d, (190, 350), "低质量回复", font(54), "#050505")
    for i, item in enumerate(["只发表情", "无关短评", "复制模板", "没有上下文"]):
        text(d, (225, 445 + i * 55), "x " + item, font(36), "#E60012")
    text(d, (970, 350), "高质量回复", font(54), "#050505")
    for i, item in enumerate(["补经历", "补数据", "补反例", "问具体问题"]):
        text(d, (1005, 445 + i * 55), "+ " + item, font(36), "#050505")
    d.rounded_rectangle((305, 760, 1295, 825), radius=22, fill="#E60012")
    text(d, (390, 771), "每条评论都应该有一个真实增量", font(38), "#FFFFFF")
    img.save(OUT / "03-human-comment.png")


def save_asset_vs_drain():
    w, h = 1600, 900
    img = paper_bg(w, h, seed=74)
    d = ImageDraw.Draw(img, "RGBA")
    red_brush(d, w, h)
    text(d, (80, 70), "别把消耗当增长", font(78), "#050505", 3, "#FFFFFF")
    d.line((80, 165, 700, 165), fill="#E60012", width=9)
    d.rounded_rectangle((105, 300, 720, 705), radius=36, fill="#FFFFFF", outline="#050505", width=5)
    d.rounded_rectangle((880, 300, 1495, 705), radius=36, fill="#FFFFFF", outline="#E60012", width=5)
    text(d, (175, 370), "资产动作", font(58), "#050505")
    for i, item in enumerate(["原创内容", "实测结果", "工作流", "高质量评论"]):
        text(d, (215, 470 + i * 52), "+ " + item, font(37), "#050505")
    text(d, (950, 370), "消耗动作", font(58), "#E60012")
    for i, item in enumerate(["批量点赞", "机械转推", "复制评论", "搬运素材"]):
        text(d, (990, 470 + i * 52), "x " + item, font(37), "#E60012")
    d.rounded_rectangle((330, 765, 1270, 828), radius=22, fill="#050505")
    text(d, (420, 776), "收益化账号，先维护长期信用", font(38), "#FFFFFF")
    img.save(OUT / "04-asset-vs-drain.png")


if __name__ == "__main__":
    save_title()
    save_risk_behaviors()
    save_human_comment()
    save_asset_vs_drain()
    for path in sorted(OUT.glob("*.png")):
        print(path)
