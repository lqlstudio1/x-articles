from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "codex-x"
BG = Path(
    r"C:\Users\admin\.codex\generated_images\019efe49-b4ed-7961-840a-fe8e72f41de9"
    r"\ig_0564c12bef36bb09016a3d14554cc88199adf9e4531996b0da.png"
)
OUT = OUT_DIR / "title-codex-app-ai-execution-env-5x2.png"

W, H = 2500, 1000
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_SERIF = Path(r"C:\Windows\Fonts\NotoSerifSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")


def font(size, bold=False, serif=False):
    path = FONT_SERIF if serif else (FONT_BOLD if bold else FONT_REG)
    return ImageFont.truetype(str(path), size=size)


def cover_crop(img, size):
    target_w, target_h = size
    src_w, src_h = img.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h
    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, src_h))
    else:
        new_h = int(src_w / target_ratio)
        top = max(0, (src_h - new_h) // 2 - 20)
        img = img.crop((0, top, src_w, top + new_h))
    return img.resize(size, Image.Resampling.LANCZOS)


def draw_text_shadow(draw, xy, text, fnt, fill, shadow=(255, 250, 235, 210), offset=4):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=fnt, fill=shadow)
    draw.text((x, y), text, font=fnt, fill=fill)


def text_width(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bg = cover_crop(Image.open(BG).convert("RGB"), (W, H)).convert("RGBA")

    # Improve readability while preserving the generated editorial background.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay, "RGBA")
    od.rounded_rectangle((390, 170, 1830, 810), radius=44, fill=(248, 241, 225, 214), outline=(25, 28, 26, 80), width=3)
    od.rectangle((0, 0, W, H), fill=(0, 0, 0, 16))
    od.rectangle((0, 0, W, H), fill=(255, 244, 225, 22))
    overlay = overlay.filter(ImageFilter.GaussianBlur(0.3))
    img = Image.alpha_composite(bg, overlay)

    draw = ImageDraw.Draw(img, "RGBA")

    teal = "#0b7470"
    orange = "#d95a2e"
    ink = "#1d211f"
    muted = "#555a54"

    x0 = 450
    draw.rounded_rectangle((x0, 220, x0 + 315, 280), radius=30, fill=(11, 116, 112, 238))
    draw.text((x0 + 32, 233), "CODEX APP 实战", font=font(32, bold=True), fill="#fff8ea")

    draw_text_shadow(draw, (x0, 335), "Codex App 不是聊天框", font(106, bold=True, serif=True), ink)
    draw_text_shadow(draw, (x0, 476), "而是一个能帮你干活的", font(88, bold=True, serif=True), ink)
    draw_text_shadow(draw, (x0, 596), "AI 执行环境", font(126, bold=True, serif=True), orange)

    subtitle = "写文件 · 跑代码 · 控浏览器 · 做内容 · 搭自动化"
    draw.text((x0 + 6, 756), subtitle, font=font(40, bold=True), fill=teal)

    footer = "AI 编程 / 自媒体创作 / 自动化工作流"
    fw = text_width(draw, footer, font(30))
    draw.rounded_rectangle((W - fw - 190, H - 110, W - 85, H - 58), radius=26, fill=(29, 33, 30, 210))
    draw.text((W - fw - 138, H - 96), footer, font=font(30), fill="#fff8ea")

    img.convert("RGB").save(OUT, quality=96)
    print(OUT)
    print(f"{W}x{H}")


if __name__ == "__main__":
    main()
