from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size=size)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center(draw, w, y, text, fnt, fill, stroke=0):
    tw, _ = text_size(draw, text, fnt)
    draw.text(((w - tw) / 2, y), text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill="#000000")


def base(size):
    w, h = size
    img = Image.new("RGB", size, "#090d0f").convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(255, 255, 255, 9), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(255, 255, 255, 7), width=1)
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.ellipse((-260, -220, 760, 720), fill=(0, 185, 174, 42))
    d.ellipse((w - 610, h - 520, w + 240, h + 260), fill=(237, 94, 45, 43))
    d.rounded_rectangle((76, 76, w - 76, h - 76), radius=44, outline=(255, 255, 255, 28), width=2)
    layer = layer.filter(ImageFilter.GaussianBlur(2))
    return Image.alpha_composite(img, layer)


def title_card():
    w, h = 2500, 1000
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    center(draw, w, 185, "AI 写作质检", font(56, True), "#64fff0")
    center(draw, w, 342, "去 AI 味", font(245, True), "#fff8e8", 4)
    center(draw, w, 638, "不是口语化，是补细节", font(92, True), "#ff8a4c", 2)
    center(draw, w, 820, "检测 / 删套话 / 改人话 / 补经验 / 沉淀风格", font(44, True), "#d9e4df")
    out = OUT_DIR / "01-title-5x2.png"
    img.convert("RGB").save(out, quality=96)
    return out


def workflow_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((90, 80), "去 AI 味工作流", font=font(50, True), fill="#64fff0")
    draw.text((90, 148), "先定位问题，再重写表达", font=font(72, True), fill="#fff8e8")
    steps = ["检测", "删套话", "人话", "补细节", "审美", "风格"]
    colors = ["#0d8f85", "#315f91", "#d95a2e", "#8b7425", "#242928", "#0d8f85"]
    x0, y = 122, 428
    for i, step in enumerate(steps):
        x = x0 + i * 238
        draw.rounded_rectangle((x, y, x + 168, y + 118), radius=24, fill=colors[i], outline=(255, 255, 255, 50), width=2)
        tw, _ = text_size(draw, step, font(36, True))
        draw.text((x + (168 - tw) / 2, y + 38), step, font=font(36, True), fill="#fff8e8")
        if i < len(steps) - 1:
            draw.line((x + 180, y + 59, x + 224, y + 59), fill="#d9e4df", width=4)
            draw.polygon([(x + 228, y + 59), (x + 207, y + 45), (x + 207, y + 73)], fill="#d9e4df")
    draw.rounded_rectangle((160, 690, 1440, 762), radius=30, fill=(255, 248, 232, 230))
    draw.text((210, 707), "关键：不是把句子写乱，而是加入真实判断和现场细节。", font=font(35, True), fill="#111614")
    out = OUT_DIR / "02-workflow.png"
    img.convert("RGB").save(out, quality=95)
    return out


def compare_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((90, 80), "两种文字", font=font(50, True), fill="#64fff0")
    draw.text((90, 148), "AI 味 vs 真人感", font=font(76, True), fill="#fff8e8")
    panels = [
        (120, 300, 740, 720, "#2b3031", "AI 味", ["开头宏大", "句子很顺", "没有细节", "强行升华"]),
        (860, 300, 1480, 720, "#0f514d", "真人感", ["有判断", "有边界", "有案例", "有踩坑"]),
    ]
    for x1, y1, x2, y2, color, title, items in panels:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=34, fill=color, outline=(255, 255, 255, 42), width=2)
        draw.text((x1 + 48, y1 + 44), title, font=font(50, True), fill="#fff8e8")
        for i, item in enumerate(items):
            y = y1 + 138 + i * 68
            draw.ellipse((x1 + 54, y + 11, x1 + 76, y + 33), fill="#ff8a4c")
            draw.text((x1 + 96, y), item, font=font(36, True), fill="#e6eee9")
    center(draw, w, 786, "真正的人味来自经历、取舍和细节", font(42, True), "#ff8a4c")
    out = OUT_DIR / "03-compare.png"
    img.convert("RGB").save(out, quality=95)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [title_card(), workflow_card(), compare_card()]:
        print(path)


if __name__ == "__main__":
    main()
