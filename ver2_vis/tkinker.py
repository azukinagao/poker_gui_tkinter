import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Poker Card Display")

card_codes = ["AS", "KD", "7H", "2C", "JC"]
images = []

for code in card_codes:
    img = Image.open(f"cards/{code}.png")
    photo = ImageTk.PhotoImage(img)
    images.append(photo)  # 参照を保持しないと表示されない

    label = tk.Label(root, image=photo)
    label.pack(side=tk.LEFT, padx=5)

root.mainloop()