import tkinter as tk
from PIL import Image, ImageTk
from deck import Deck
from player import Player
from hand_eval import evaluate_hand
import os

# 記号からスートコードに変換する辞書
suit_symbol_to_code = {
    '♠': 'S',
    '♥': 'H',
    '♦': 'D',
    '♣': 'C'
}

def card_to_filename(card):
    """
    Cardオブジェクトからファイル名を生成
    """
    suit_symbol_to_code = {
        '♠': 'S',
        '♥': 'H',
        '♦': 'D',
        '♣': 'C'
    }
    suit_code = suit_symbol_to_code[card.suit]
    return f"{card.rank}{suit_code}.png"


class PokerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker GUI")
        self.deck = Deck()
        self.player = Player("You")
        self.opponent = Player("Bot")

        # 各Frameを作成
        self.frame_player = tk.Frame(root)
        self.frame_player.pack(pady=10)

        self.frame_community = tk.Frame(root)
        self.frame_community.pack(pady=10)

        self.frame_opponent = tk.Frame(root)
        self.frame_opponent.pack(pady=10)

        self.button = tk.Button(root, text="Start New Hand", command=self.start_hand)
        self.button.pack(pady=20)

        # イメージ保持リスト（破棄防止）
        self.images = []

    def start_hand(self):
        # リセット
        for widget in self.frame_player.winfo_children():
            widget.destroy()
        for widget in self.frame_opponent.winfo_children():
            widget.destroy()
        for widget in self.frame_community.winfo_children():
            widget.destroy()
        self.images.clear()

        self.deck = Deck()
        self.player.hand = self.deck.deal(2)
        self.opponent.hand = self.deck.deal(2)
        community = self.deck.deal(5)

        # 表示
        self.display_cards(self.frame_player, self.player.hand, "Your Hand")
        self.display_cards(self.frame_community, community, "Community Cards")
        self.display_cards(self.frame_opponent, self.opponent.hand, "Bot Hand")

    def display_cards(self, frame, cards, label_text):
        label = tk.Label(frame, text=label_text, font=("Arial", 14, "bold"))
        label.pack()

        row = tk.Frame(frame)
        row.pack()

        for card in cards:
            filename = card_to_filename(card)
            path = os.path.join("cards", filename)
            img = Image.open(path)
            photo = ImageTk.PhotoImage(img)
            self.images.append(photo)  # 保持しておく

            label = tk.Label(row, image=photo)
            label.pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    gui = PokerGUI(root)
    root.mainloop()
