from PIL import Image, ImageDraw, ImageFont
import os

# 保存先ディレクトリ
output_dir = "cards"
os.makedirs(output_dir, exist_ok=True)

# カードのサイズ
width, height = 150, 220

# スート記号と色
suits = {
    "S": ("♠", "black"),
    "H": ("♥", "red"),
    "D": ("♦", "red"),
    "C": ("♣", "black")
}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# フォントの設定（適宜パスを変更）
font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # Macの場合
font = ImageFont.truetype(font_path, 48)

for suit_code, (symbol, color) in suits.items():
    for rank in ranks:
        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)

        # マークとランクを左上と中央に描画
        draw.text((10, 10), rank + symbol, font=font, fill=color)
        draw.text((width // 2 - 20, height // 2 - 30), symbol, font=font, fill=color)

        # 保存
        filename = f"{rank}{suit_code}.png"  # 例: "AS.png"
        img.save(os.path.join(output_dir, filename))

print("52枚のカード画像を生成しました。")
