# Poker GUI (ver2/Work in Progress)

A simple Texas Hold'em poker GUI built with Python and Tkinter.
This version focuses on visualizing cards using image files.

## Features
- Tkinter-based GUI
- Card images displayed using Pillow (PIL)
- Automatically shuffled 52-card deck
- Displays:
  - Your hand (2 cards)
  - Community cards (5 cards)
  - Bot hand (2 cards, currently shown for debugging)
- Simple structure for future expansion

## Requirements
- Python 3.x
- Pillow (PIL)

Install Pillow:
```
pip install pillow
```

## Folder Structure
The program expects the following files inside the `ver2_vis` directory:

- PokerGUI.py
- game.py
- deck.py
- player.py
- hand_eval.py
- makecards.py
- cards/  
  - AS.png  
  - 10H.png  
  - QD.png  
  - ...  

## Card Image Naming Rule
Card images must be placed in the `cards/` directory and named as follows:

- AS.png  → Ace of Spades (A♠)
- 10H.png → Ten of Hearts (10♥)
- QD.png  → Queen of Diamonds (Q♦)
- 7C.png  → Seven of Clubs (7♣)

Suit codes:
- ♠ → S
- ♥ → H
- ♦ → D
- ♣ → C

## How to Run
Move into the `ver2_vis` directory and run:

```
python PokerGUI.py
```

## Notes
- The bot's hand is currently visible for development and debugging.
- This version is a GUI prototype and will be extended in future versions.
- This project was developed with the assistance of generative AI tools.

## Motivation
Originally, I had only worked with Python in a procedural style. Through my research, I was introduced to object-oriented languages. To better understand how classes are used in practice, I created this project using a class-based design in Python.
