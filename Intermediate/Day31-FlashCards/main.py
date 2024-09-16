import tkinter as tk
from tkinter import ttk

import pandas as pd


class FlashCard:
    def __init__(self, root):
        ### Paramters ###
        # Database French/English
        try:
            self.db = pd.read_csv(filepath_or_buffer="data/words_to_learn.csv")
        except FileNotFoundError:
            self.db = pd.read_csv(filepath_or_buffer="data/french_words.csv")

        # Geometry for widgets
        # Canvas
        self.width_card = 800
        self.height_card = 526
        self.font_language = ("Arial", 40, "italic")
        self.font_word = ("Arial", 60, "bold")
        # Position text on canvas
        self.pos_language = (400, 150)
        self.pos_word = (400, 263)
        self.pad_main = 50
        # Background color for main frame
        self.color = "#B1DDC6"

        # Config
        root.title("FlashCards")
        root.config(padx=self.pad_main, pady=self.pad_main, bg=self.color)
        # Images init
        try:
            root.card_front = tk.PhotoImage(file="images/card_front.png")
            root.card_back = tk.PhotoImage(file="images/card_back.png")
            root.right = tk.PhotoImage(file="images/right.png")
            root.wrong = tk.PhotoImage(file="images/wrong.png")
        except:
            raise FileNotFoundError("Check paths of images to be loaded.")

        ### Widgets ###
        # Nain Frame
        self.main = ttk.Frame(root)
        self.main.grid(column=0, row=0, sticky="nwes")

        # Canvas for flash cards
        self.canvas = tk.Canvas(self.main, width=self.width_card, height=self.height_card)
        self.canvas.grid(column=1, row=1,columnspan=2, sticky="nwes")
        self.card = self.canvas.create_image(400, 263,  image=root.card_front)
        self.title = self.canvas.create_text(self.pos_language, text="French", font=self.font_language)
        self.word = self.canvas.create_text(self.pos_word, text="Word", font=self.font_word)
        self.canvas.config(bg=self.color, highlightthickness=0)

        # Buttons
        self.wrong = ttk.Button(self.main, image=root.wrong, command=self.random_card)
        self.wrong.grid(column=1, row=2)
        self.right = ttk.Button(self.main, image=root.right, command=self.random_card)
        self.right.grid(column=2, row=2)

        # First card
        self.random_card()


    # Turn english side
    def turn(self, random_word):
        self.canvas.itemconfig(self.title, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=f"{random_word['English'].values[0]}", fill="white")
        self.canvas.itemconfig(self.card, image=root.card_back)


    # Generate random french words
    def random_card(self):
        # Select 1 random row in db
        random_word = self.db.sample(n=1)
        # Modify Canvas word text
        self.canvas.itemconfig(self.title, text="French", fill="black")
        self.canvas.itemconfig(self.word, text=f"{random_word['French'].values[0]}", fill="black")
        self.canvas.itemconfig(self.card, image=root.card_front)

        # Wait 3s and change the card
        root.after(3000, self.turn, random_word)


if __name__ == '__main__':
    root = tk.Tk()
    FlashCard(root)
    root.mainloop()
