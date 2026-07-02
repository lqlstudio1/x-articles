from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "codex-x"
BG = Path(
    r"C:\Users\admin\.codex\generated_images\019efe49-b4ed-7961-840a-fe8e72f41de9"
    r"\ig_0a221e7092822e0b016a3d16cd67688198b1c9068d51428ced.png"
)
OUT = OUT_DIR / "title-codex-app-big-5x2.png"

W, H = 2500, 1000
FONT_REG = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
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
        top = (src_h - new_h) // 2
        img = img.crop((0, top, src_w, top + new_h))
    return img.resize(size, Image.Resampling.LANCZOS)


def center_text(draw, y, text, fnt, fill, stroke_fill=None, stroke_width=0):
    box = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke_width)
    tw = box[2] - box[0]
    th = box[3] - box[1]
    x = (W - tw) / 2
    draw.text(
        (x, y),
        text,
        font=fnt,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
    return y + th


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bg = cover_crop(Image.open(BG).convert("RGB"), (W, H)).convert("RGBA")

    # Strong central contrast, with the original generated background still visible.
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer, "RGBA")
    ld.rectangle((0, 0, W, H), fill=(0, 0, 0, 72))
    ld.rounded_rectangle((250, 185, 2250, 815), radius=40, fill=(0, 0, 0, 72), outline=(255, 255, 255, 24), width=2)
    ld.rectangle((360, 290, 2140, 705), fill=(0, 0, 0, 52))
    ld.rectangle((0, 0, W, 130), fill=(0, 0, 0, 44))
    ld.rectangle((0, H - 135, W, H), fill=(0, 0, 0, 48))
    layer = layer.filter(ImageFilter.GaussianBlur(0.2))
    img = Image.alpha_composite(bg, layer)

    draw = ImageDraw.Draw(img, "RGBA")

    # Small context, huge memory hook.
    center_text(draw, 214, "CODEX APP", font(50, bold=True), "#70fff2")
    center_text(
        draw,
        320,
        "AI执行环境",
        font(245, bold=True),
        "#fff8e7",
        stroke_fill=(0, 0, 0, 150),
        stroke_width=3,
    )

    # Keep the supporting line short and visually secondary.
    center_text(draw, 662, "不是聊天框，是能干活的系统", font(56, bold=True), "#ff8a4c")

    # Thin editorial rules.
    draw.line((430, 286, 2070, 286), fill=(112, 255, 242, 115), width=3)
    draw.line((570, 762, 1930, 762), fill=(255, 138, 76, 135), width=4)

    img.convert("RGB").save(OUT, quality=96)
    print(OUT)
    print(f"{W}x{H}")


if __name__ == "__main__":
    main()
