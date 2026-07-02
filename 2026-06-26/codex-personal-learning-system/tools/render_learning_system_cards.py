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
    img = Image.new("RGB", size, "#080c0e").convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    for x in range(0, w, 80):
        draw.line((x, 0, x, h), fill=(255, 255, 255, 9), width=1)
    for y in range(0, h, 80):
        draw.line((0, y, w, y), fill=(255, 255, 255, 7), width=1)
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.ellipse((-260, -220, 780, 740), fill=(0, 185, 174, 42))
    d.ellipse((w - 680, h - 540, w + 230, h + 260), fill=(237, 94, 45, 42))
    d.rounded_rectangle((76, 76, w - 76, h - 76), radius=44, outline=(255, 255, 255, 28), width=2)
    layer = layer.filter(ImageFilter.GaussianBlur(2))
    return Image.alpha_composite(img, layer)


def title_card():
    w, h = 2500, 1000
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    center(draw, w, 178, "CODEX 学习系统", font(56, True), "#64fff0")
    center(draw, w, 338, "答案不等于能力", font(210, True), "#fff8e8", 4)
    center(draw, w, 625, "把学习当项目来跑", font(104, True), "#ff8a4c", 2)
    center(draw, w, 820, "目标 / 任务 / 练习 / 错误 / 复测 / 项目", font(46, True), "#d9e4df")
    out = OUT_DIR / "01-title-5x2.png"
    img.convert("RGB").save(out, quality=96)
    return out


def loop_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((90, 78), "学习闭环", font=font(52, True), fill="#64fff0")
    draw.text((90, 148), "从问答案，到练能力", font=font(76, True), fill="#fff8e8")
    steps = ["目标", "地图", "任务", "练习", "错误", "复测", "项目"]
    colors = ["#0d8f85", "#315f91", "#d95a2e", "#8b7425", "#242928", "#0d8f85", "#315f91"]
    x0, y = 92, 430
    for i, step in enumerate(steps):
        x = x0 + i * 205
        draw.rounded_rectangle((x, y, x + 142, y + 110), radius=22, fill=colors[i], outline=(255, 255, 255, 50), width=2)
        tw, _ = text_size(draw, step, font(34, True))
        draw.text((x + (142 - tw) / 2, y + 36), step, font=font(34, True), fill="#fff8e8")
        if i < len(steps) - 1:
            draw.line((x + 152, y + 55, x + 190, y + 55), fill="#d9e4df", width=4)
            draw.polygon([(x + 194, y + 55), (x + 174, y + 42), (x + 174, y + 68)], fill="#d9e4df")
    draw.rounded_rectangle((150, 690, 1450, 764), radius=30, fill=(255, 248, 232, 230))
    draw.text((200, 708), "关键：没有练习、错误和复测，学习计划只是漂亮目录。", font=font(35, True), fill="#111614")
    out = OUT_DIR / "02-learning-loop.png"
    img.convert("RGB").save(out, quality=95)
    return out


def repo_card():
    w, h = 1600, 900
    img = base((w, h))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((90, 78), "最小学习仓库", font=font(52, True), fill="#64fff0")
    draw.text((90, 148), "先建 5 个文件就够了", font=font(76, True), fill="#fff8e8")
    files = [
        ("AGENTS.md", "学习规则"),
        ("progress.md", "当前进度"),
        ("knowledge_map.md", "知识地图"),
        ("daily_task.md", "今日任务"),
        ("mistakes.md", "错误复测"),
    ]
    x1, y1 = 210, 315
    for i, (name, desc) in enumerate(files):
        y = y1 + i * 88
        draw.rounded_rectangle((x1, y, 1390, y + 62), radius=18, fill=(255, 248, 232, 224), outline=(255, 255, 255, 42), width=1)
        draw.text((x1 + 34, y + 13), name, font=font(28, True), fill="#111614")
        draw.text((x1 + 550, y + 13), desc, font=font(28, True), fill="#0d625d")
    center(draw, w, 790, "不用每次重新介绍背景，让 Codex 从真实状态继续推进", font(38, True), "#ff8a4c")
    out = OUT_DIR / "03-minimal-repo.png"
    img.convert("RGB").save(out, quality=95)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in [title_card(), loop_card(), repo_card()]:
        print(path)


if __name__ == "__main__":
    main()
