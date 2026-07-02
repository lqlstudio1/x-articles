from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONTS = [
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf"),
]


def font(size):
    for p in FONTS:
        if p.exists():
            return ImageFont.truetype(str(p), size=size, index=0)
    return ImageFont.load_default()


def t(draw, xy, s, fnt, fill, stroke=0, stroke_fill="#000"):
    draw.text(xy, s, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)


def tb(draw, s, fnt):
    b = draw.textbbox((0, 0), s, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def bg(w, h, seed):
    random.seed(seed)
    img = Image.new("RGB", (w, h), "#F8F5EF")
    px = img.load()
    for y in range(h):
        for x in range(w):
            n = random.randint(-4, 4)
            base = 247 + n
            px[x, y] = (base, base - 3, base - 8)
    img = img.filter(ImageFilter.GaussianBlur(0.18))
    d = ImageDraw.Draw(img, "RGBA")
    red = (232, 0, 22, 238)
    d.polygon([(int(w * 0.62), 0), (w, 0), (w, h), (int(w * 0.72), h), (int(w * 0.82), int(h * 0.22))], fill=red)
    d.polygon([(0, h), (int(w * 0.28), int(h * 0.80)), (int(w * 0.45), h)], fill=(232, 0, 22, 150))
    for i in range(8):
        y = int(h * (0.07 + i * 0.10))
        d.line((int(w * 0.58), y, w, y + random.randint(-40, 50)), fill=(232, 0, 22, 62), width=random.randint(10, 28))
    for _ in range(80):
        x = random.randint(0, w)
        y = random.randint(0, h)
        d.ellipse((x, y, x + 2, y + 2), fill=(0, 0, 0, 18))
    return img


def tag(draw, xy, label, fill="#050505", fg="#FFFFFF", size=35):
    f = font(size)
    x, y = xy
    tw, th = tb(draw, label, f)
    draw.rounded_rectangle((x, y, x + tw + 46, y + th + 20), radius=16, fill=fill)
    t(draw, (x + 23, y + 7), label, f, fg)


def corners(draw, x1, y1, x2, y2, color="#E60012"):
    l = 82
    w = 9
    draw.line((x1, y1, x1 + l, y1), fill=color, width=w)
    draw.line((x1, y1, x1, y1 + l), fill=color, width=w)
    draw.line((x2, y1, x2 - l, y1), fill=color, width=w)
    draw.line((x2, y1, x2, y1 + l), fill=color, width=w)
    draw.line((x1, y2, x1 + l, y2), fill=color, width=w)
    draw.line((x1, y2, x1, y2 - l), fill=color, width=w)
    draw.line((x2, y2, x2 - l, y2), fill=color, width=w)
    draw.line((x2, y2, x2, y2 - l), fill=color, width=w)


def panel(draw, box, outline="#050505", fill="#FFFFFF", width=5, radius=30):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle((x1 + 15, y1 + 15, x2 + 15, y2 + 15), radius=radius, fill=(0, 0, 0, 45))
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def save_title():
    w, h = 2500, 1000
    img = bg(w, h, 91)
    d = ImageDraw.Draw(img, "RGBA")
    corners(d, 95, 115, 1360, 760)
    tag(d, (160, 112), "MONETIZATION HEALTH")
    t(d, (150, 235), "账号", font(178), "#E60012", 4, "#FFFFFF")
    t(d, (560, 235), "信用", font(178), "#050505", 4, "#FFFFFF")
    t(d, (165, 515), "付款前，先做一次健康体检", font(70), "#050505", 3, "#FFFFFF")
    d.line((520, 620, 1110, 603), fill="#E60012", width=10)
    d.rounded_rectangle((180, 705, 1040, 800), radius=24, fill="#FFFFFF", outline="#E60012", width=6)
    t(d, (240, 720), "别把短期互动，换成长期风险", font(46), "#050505")
    panel(d, (1540, 150, 2215, 805), outline="#FFFFFF", width=5)
    d.rounded_rectangle((1570, 180, 2185, 248), radius=18, fill="#050505")
    t(d, (1610, 192), "收益化前自检", font(43), "#FFFFFF")
    checks = [
        ("动作像脚本", True),
        ("评论像垃圾", True),
        ("关系像互刷", True),
        ("素材像搬运", True),
        ("原创 + 长评 + 定位", False),
    ]
    y = 310
    for label, bad in checks:
        t(d, (1610, y), "x" if bad else "+", font(45), "#E60012" if bad else "#050505")
        t(d, (1670, y + 3), label, font(41), "#050505")
        y += 82
    img.save(OUT / "01-title-5x2.png")


def save_risk_accounts():
    w, h = 1600, 900
    img = bg(w, h, 92)
    d = ImageDraw.Draw(img, "RGBA")
    t(d, (78, 72), "4类账号最危险", font(74), "#050505", 3, "#FFFFFF")
    t(d, (82, 168), "不是内容差，而是信用信号差", font(43), "#E60012")
    items = [
        ("动作像脚本", "密集重复互动"),
        ("评论像垃圾", "短评/表情/复制"),
        ("关系像互刷", "互关互赞暗号"),
        ("素材像搬运", "旧图旧视频复用"),
    ]
    positions = [(100, 310), (830, 310), (100, 560), (830, 560)]
    for idx, ((title, sub), (x, y)) in enumerate(zip(items, positions), 1):
        panel(d, (x, y, x + 590, y + 170), outline="#050505", width=5, radius=28)
        d.ellipse((x + 32, y + 43, x + 112, y + 123), fill="#E60012")
        t(d, (x + 58, y + 48), str(idx), font(46), "#FFFFFF")
        t(d, (x + 145, y + 38), title, font(48), "#050505")
        t(d, (x + 145, y + 103), sub, font(31), "#555555")
    img.save(OUT / "02-four-risk-accounts.png")


def save_health_system():
    w, h = 1600, 900
    img = bg(w, h, 93)
    d = ImageDraw.Draw(img, "RGBA")
    t(d, (80, 70), "建立账号健康系统", font(72), "#050505", 3, "#FFFFFF")
    d.line((80, 165, 760, 165), fill="#E60012", width=9)
    nodes = [
        ("互动", "有上下文长评"),
        ("素材", "原创截图流程"),
        ("曝光", "垂直领域回复"),
        ("自检", "每周复盘一次"),
    ]
    x = 95
    for title, sub in nodes:
        panel(d, (x, 365, x + 315, 590), outline="#050505", radius=26)
        t(d, (x + 68, 425), title, font(54), "#E60012")
        t(d, (x + 47, 505), sub, font(31), "#050505")
        x += 375
    d.rounded_rectangle((260, 740, 1340, 815), radius=24, fill="#050505")
    t(d, (360, 755), "目标不是避开风控，而是减少伪装感", font(39), "#FFFFFF")
    img.save(OUT / "03-health-system.png")


def save_codex_checklist():
    w, h = 1600, 900
    img = bg(w, h, 94)
    d = ImageDraw.Draw(img, "RGBA")
    t(d, (80, 70), "用 Codex 做周复盘", font(72), "#050505", 3, "#FFFFFF")
    t(d, (82, 165), "不是批量互动，是防止自己变成机器人", font(42), "#E60012")
    panel(d, (150, 300, 1450, 710), outline="#050505", radius=34)
    left = [
        "本周原创内容比例",
        "高质量评论数量",
        "素材来源是否可追溯",
        "是否出现机械互动",
        "下周减少什么 / 增加什么",
    ]
    y = 365
    for item in left:
        t(d, (235, y), "+", font(42), "#E60012")
        t(d, (295, y + 2), item, font(39), "#050505")
        y += 62
    d.rounded_rectangle((1030, 365, 1355, 590), radius=26, fill="#E60012")
    t(d, (1090, 405), "AI 做记录", font(39), "#FFFFFF")
    t(d, (1090, 468), "人做判断", font(39), "#FFFFFF")
    d.rounded_rectangle((300, 760, 1300, 825), radius=22, fill="#050505")
    t(d, (405, 774), "自动化不是刷互动，是维护规则", font(38), "#FFFFFF")
    img.save(OUT / "04-codex-checklist.png")


if __name__ == "__main__":
    save_title()
    save_risk_accounts()
    save_health_system()
    save_codex_checklist()
    for p in sorted(OUT.glob("*.png")):
        print(p)
