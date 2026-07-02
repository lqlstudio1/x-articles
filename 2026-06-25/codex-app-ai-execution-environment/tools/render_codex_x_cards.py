from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "codex-x"
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_SERIF = Path(r"C:\Windows\Fonts\NotoSerifSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")

W, H = 1600, 900


def font(size, bold=False, serif=False):
    path = FONT_SERIF if serif else (FONT_BOLD if bold else FONT_REG)
    return ImageFont.truetype(str(path), size=size)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw, text, fnt, max_width):
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for ch in paragraph:
            trial = current + ch
            if text_size(draw, trial, fnt)[0] <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill, max_width, line_gap=10, anchor=None):
    x, y = xy
    lines = wrap_text(draw, text, fnt, max_width)
    for line in lines:
        if anchor == "mm":
            tw, th = text_size(draw, line, fnt)
            draw.text((x - tw / 2, y), line, font=fnt, fill=fill)
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def make_background(base="#f5f0e7", accent="#0b6f6a"):
    img = Image.new("RGB", (W, H), base)
    draw = ImageDraw.Draw(img)

    # Quiet paper texture.
    for y in range(0, H, 4):
        shade = 2 if (y // 4) % 2 == 0 else -1
        col = tuple(max(0, min(255, c + shade)) for c in Image.new("RGB", (1, 1), base).getpixel((0, 0)))
        draw.line((0, y, W, y), fill=col)

    # Soft geometric fields.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((-220, -180, 620, 540), fill=(11, 111, 106, 34))
    od.ellipse((1050, 460, 1830, 1180), fill=(214, 89, 46, 28))
    od.polygon([(1100, 0), (1600, 0), (1600, 340), (1260, 260)], fill=(28, 76, 120, 26))
    overlay = overlay.filter(ImageFilter.GaussianBlur(8))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def draw_grid(draw, color=(28, 28, 24, 26)):
    for x in range(80, W, 80):
        draw.line((x, 0, x, H), fill=color, width=1)
    for y in range(60, H, 60):
        draw.line((0, y, W, y), fill=color, width=1)


def footer(draw, label):
    draw.text((84, 820), label, font=font(24), fill="#5f625b")
    draw.line((84, 800, 1516, 800), fill="#c8c0b2", width=2)


def save(img, name):
    path = OUT_DIR / name
    img.save(path, quality=95)
    return path


def card_cover():
    img = make_background()
    draw = ImageDraw.Draw(img, "RGBA")
    draw_grid(draw)

    rounded(draw, (86, 86, 1514, 814), 34, (255, 252, 245, 210), outline="#2e2f2b", width=3)
    draw.text((132, 128), "CODEX APP", font=font(34, bold=True), fill="#0b6f6a")
    draw.text((132, 188), "不是聊天框，", font=font(96, bold=True, serif=True), fill="#20211e")
    draw.text((132, 302), "是 AI 执行环境", font=font(110, bold=True, serif=True), fill="#20211e")
    draw_wrapped(
        draw,
        (138, 460),
        "写文件 · 跑代码 · 控浏览器\n做内容 · 搭自动化",
        font(42, bold=True),
        "#d6592e",
        760,
        line_gap=18,
    )
    draw_wrapped(
        draw,
        (138, 600),
        "把想法变成真实文件、网页、视频和可复用流程。",
        font(34),
        "#3e413b",
        760,
        line_gap=14,
    )

    # Command center motif.
    panel = (980, 170, 1440, 675)
    rounded(draw, panel, 28, (32, 33, 30, 236), outline="#20211e", width=2)
    for i, txt in enumerate(["DOC", "WEB", "MEDIA", "AUTO"]):
        y = 230 + i * 92
        rounded(draw, (1032, y, 1390, y + 58), 18, (245, 240, 231, 238))
        draw.text((1062, y + 12), txt, font=font(28, bold=True), fill="#20211e")
        draw.ellipse((1332, y + 17, 1366, y + 51), fill=["#0b6f6a", "#d6592e", "#345d89", "#8a6f2a"][i])
    draw.line((1210, 545, 1210, 590), fill="#f5f0e7", width=4)
    draw.polygon([(1210, 612), (1188, 582), (1232, 582)], fill="#f5f0e7")
    draw.text((1120, 622), "SHIP", font=font(38, bold=True), fill="#f5f0e7")

    footer(draw, "配图 01 / 封面")
    return save(img, "01-cover.png")


def card_ladder():
    img = make_background("#f8f6ef")
    draw = ImageDraw.Draw(img, "RGBA")
    draw_grid(draw, color=(28, 28, 24, 18))

    draw.text((88, 82), "新手路线", font=font(38, bold=True), fill="#0b6f6a")
    draw.text((88, 138), "先建立信任，再做复杂自动化", font=font(70, bold=True, serif=True), fill="#20211e")

    steps = [
        ("01", "办公文件", "Word / PDF / PPT / Sheets"),
        ("02", "网页上线", "页面、预览、部署"),
        ("03", "图文教程", "结构、截图、风格"),
        ("04", "视频内容", "脚本、素材、合成"),
        ("05", "业务自动化", "表格 / 后台\n日志"),
    ]

    x0, y0 = 130, 320
    step_w, step_h = 252, 300
    colors = ["#0b6f6a", "#d6592e", "#345d89", "#8a6f2a", "#20211e"]
    for i, (num, title, desc) in enumerate(steps):
        x = x0 + i * 286
        y = y0 - i * 34
        rounded(draw, (x, y, x + step_w, y + step_h), 28, (255, 252, 245, 235), outline="#2e2f2b", width=2)
        draw.text((x + 28, y + 26), num, font=font(34, bold=True), fill=colors[i])
        next_y = draw_wrapped(draw, (x + 28, y + 96), title, font(34, bold=True), "#20211e", step_w - 56)
        draw_wrapped(draw, (x + 28, max(next_y + 18, y + 185)), desc, font(24), "#555850", step_w - 56, line_gap=8)
        if i < len(steps) - 1:
            draw.line((x + step_w + 18, y + 148, x + 286 - 24, y + 148), fill=colors[i], width=5)
            draw.polygon([(x + 286 - 20, y + 148), (x + 286 - 42, y + 134), (x + 286 - 42, y + 162)], fill=colors[i])

    footer(draw, "配图 02 / 学习路线")
    return save(img, "02-learning-ladder.png")


def card_content_chain():
    img = make_background("#f3f0e8")
    draw = ImageDraw.Draw(img, "RGBA")
    draw_grid(draw, color=(28, 28, 24, 18))

    draw.text((88, 82), "内容生产", font=font(38, bold=True), fill="#d6592e")
    draw.text((88, 138), "AI 负责加速，不负责替你思考", font=font(68, bold=True, serif=True), fill="#20211e")

    chain = [
        ("观点", "你先定义\n要表达什么"),
        ("结构", "每节只写\n一句要点"),
        ("素材", "截图、案例\n和证据"),
        ("风格", "用 Skill\n沉淀语气"),
        ("发布", "改标题\n配图上线"),
    ]
    colors = ["#0b6f6a", "#345d89", "#d6592e", "#8a6f2a", "#20211e"]
    cx0, cy = 210, 500
    for i, (title, desc) in enumerate(chain):
        cx = cx0 + i * 292
        draw.ellipse((cx - 86, cy - 86, cx + 86, cy + 86), fill=colors[i])
        tw, _ = text_size(draw, title, font(36, bold=True))
        draw.text((cx - tw / 2, cy - 24), title, font=font(36, bold=True), fill="#fffaf0")
        draw_wrapped(draw, (cx - 86, cy + 122), desc, font(28), "#3e413b", 172, line_gap=6, anchor="mm")
        if i < len(chain) - 1:
            x1, x2 = cx + 104, cx + 292 - 104
            draw.line((x1, cy, x2, cy), fill="#999184", width=5)
            draw.polygon([(x2 + 14, cy), (x2 - 10, cy - 15), (x2 - 10, cy + 15)], fill="#999184")

    rounded(draw, (208, 694, 1394, 756), 24, (255, 252, 245, 230), outline="#c8c0b2", width=2)
    draw.text((246, 708), "关键：给 AI 的不是一个方向，而是一套清楚的写作流程。", font=font(30, bold=True), fill="#20211e")

    footer(draw, "配图 03 / 图文教程链路")
    return save(img, "03-content-chain.png")


def card_automation():
    img = make_background("#f7f2ea")
    draw = ImageDraw.Draw(img, "RGBA")
    draw_grid(draw, color=(28, 28, 24, 18))

    draw.text((88, 82), "业务自动化", font=font(38, bold=True), fill="#345d89")
    draw.text((88, 138), "从点鼠标，到沉淀流程资产", font=font(70, bold=True, serif=True), fill="#20211e")

    columns = [
        ("输入", ["商品底表", "图片素材", "字段规则"], "#0b6f6a"),
        ("处理", ["读取 Excel", "映射字段", "生成模板"], "#d6592e"),
        ("执行", ["打开后台", "填写表单", "截图确认"], "#345d89"),
        ("沉淀", ["成功日志", "错误截图", "复用 Skill"], "#20211e"),
    ]
    x = 96
    for idx, (title, items, color) in enumerate(columns):
        bx = x + idx * 374
        rounded(draw, (bx, 322, bx + 322, 675), 26, (255, 252, 245, 235), outline="#2e2f2b", width=2)
        draw.rectangle((bx, 322, bx + 322, 392), fill=color)
        draw.text((bx + 28, 339), title, font=font(34, bold=True), fill="#fffaf0")
        for j, item in enumerate(items):
            y = 430 + j * 70
            draw.ellipse((bx + 30, y + 11, bx + 50, y + 31), fill=color)
            draw.text((bx + 68, y), item, font=font(29), fill="#20211e")
        if idx < len(columns) - 1:
            y = 498
            draw.line((bx + 332, y, bx + 366, y), fill=color, width=5)
            draw.polygon([(bx + 370, y), (bx + 348, y - 14), (bx + 348, y + 14)], fill=color)

    rounded(draw, (160, 720, 1440, 780), 22, (32, 33, 30, 232))
    draw.text((205, 734), "稳定后，Codex 做的不只是一次操作，而是公司可复用的 SOP。", font=font(29, bold=True), fill="#fffaf0")

    footer(draw, "配图 04 / 浏览器自动化")
    return save(img, "04-automation-flow.png")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = [card_cover(), card_ladder(), card_content_chain(), card_automation()]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
