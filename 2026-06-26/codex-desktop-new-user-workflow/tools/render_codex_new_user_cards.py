from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "codex-new-user"
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size=size)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center(draw, y, text, fnt, fill, w, stroke_width=0, stroke_fill=None):
    tw, _ = text_size(draw, text, fnt)
    draw.text(
        ((w - tw) / 2, y),
        text,
        font=fnt,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )


def bg(size):
    w, h = size
    img = Image.new("RGB", size, "#080c0e")
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(255, 255, 255, 9), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(255, 255, 255, 7), width=1)
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.ellipse((-260, -260, 760, 760), fill=(0, 190, 180, 44))
    d.ellipse((w - 650, h - 520, w + 220, h + 260), fill=(230, 94, 44, 44))
    d.rounded_rectangle((80, 80, w - 80, h - 80), radius=44, outline=(255, 255, 255, 28), width=2)
    layer = layer.filter(ImageFilter.GaussianBlur(2))
    return Image.alpha_composite(img.convert("RGBA"), layer)


def title_card():
    w, h = 2500, 1000
    img = bg((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    center(draw, 185, "CODEX 桌面版入门", font(54, True), "#64fff0", w)
    center(draw, 340, "别先学按钮", font(210, True), "#fff8e8", w, 4, "#000000")
    center(draw, 610, "先学工作流", font(132, True), "#ff8a4c", w, 2, "#000000")
    center(draw, 810, "读项目 / 做计划 / 小步改 / 自验证 / 看 diff / 沉淀规则", font(42, True), "#d9e4df", w)
    out = OUT_DIR / "01-title-5x2.png"
    img.convert("RGB").save(out, quality=96)
    return out


def workflow_card():
    w, h = 1600, 900
    img = bg((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((92, 78), "新手最稳工作流", font=font(48, True), fill="#64fff0")
    draw.text((92, 140), "不是一次性许愿，而是多轮协作", font=font(72, True), fill="#fff8e8")
    steps = ["读项目", "做计划", "小步改", "自验证", "Review", "沉淀"]
    colors = ["#0f8f86", "#2f5f91", "#d85a2f", "#8b7425", "#222726", "#0f8f86"]
    x0, y = 132, 430
    for i, step in enumerate(steps):
        x = x0 + i * 236
        draw.rounded_rectangle((x, y, x + 168, y + 120), radius=24, fill=colors[i], outline=(255, 255, 255, 45), width=2)
        tw, th = text_size(draw, step, font(34, True))
        draw.text((x + (168 - tw) / 2, y + 39), step, font=font(34, True), fill="#fff8e8")
        if i < len(steps) - 1:
            draw.line((x + 180, y + 60, x + 222, y + 60), fill="#d9e4df", width=4)
            draw.polygon([(x + 226, y + 60), (x + 206, y + 46), (x + 206, y + 74)], fill="#d9e4df")
    draw.rounded_rectangle((160, 690, 1440, 760), radius=28, fill=(255, 248, 232, 230))
    draw.text((210, 706), "关键：每一步都要有上下文、约束和完成标准。", font=font(36, True), fill="#111614")
    out = OUT_DIR / "02-workflow.png"
    img.convert("RGB").save(out, quality=95)
    return out


def compare_card():
    w, h = 1600, 900
    img = bg((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((92, 78), "两种用法", font=font(48, True), fill="#64fff0")
    draw.text((92, 140), "聊天框思维 vs 工作流思维", font=font(72, True), fill="#fff8e8")
    panels = [
        (120, 300, 740, 720, "#2b2f31", "聊天框思维", ["一句话许愿", "等 AI 自由发挥", "不验证结果", "改坏了才发现"]),
        (860, 300, 1480, 720, "#0f4f4b", "工作流思维", ["给上下文", "先计划再实现", "跑测试看页面", "Review 后再沉淀"]),
    ]
    for x1, y1, x2, y2, color, title, items in panels:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=34, fill=color, outline=(255, 255, 255, 42), width=2)
        draw.text((x1 + 48, y1 + 44), title, font=font(46, True), fill="#fff8e8")
        for i, item in enumerate(items):
            y = y1 + 130 + i * 68
            draw.ellipse((x1 + 52, y + 10, x1 + 74, y + 32), fill="#ff8a4c")
            draw.text((x1 + 94, y), item, font=font(34, True), fill="#e6eee9")
    center(draw, 785, "Codex 不是许愿机，是需要你会管理的 AI 同事", font(40, True), "#ff8a4c", w)
    out = OUT_DIR / "03-compare.png"
    img.convert("RGB").save(out, quality=95)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [title_card(), workflow_card(), compare_card()]:
        print(path)


if __name__ == "__main__":
    main()
