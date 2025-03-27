from PIL import Image, ImageDraw, ImageFont
import os

# 用語リスト
terms = ["Python", "Java", "C++", "JavaScript", "Ruby",
         "Swift", "Go", "Kotlin", "PHP", "R"]

# 画像サイズとフォント設定
width, height = 400, 200
font_size = 40

# フォント設定
font_path = "arial.ttf"  # Windows環境
font = ImageFont.truetype(font_path, font_size)

# GIFの保存先をプロジェクトフォルダに固定
output_path = os.path.join(os.path.dirname(__file__), "terms_animation.gif")

# フレーム作成
frames = []
for term in terms:
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # テキストのサイズを取得
    bbox = draw.textbbox((0, 0), term, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 中央配置
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), term, font=font, fill="black")

    frames.append(img)

# GIF保存
frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=3000, loop=0)

print(f"✅ GIFが保存されました: {output_path}")
