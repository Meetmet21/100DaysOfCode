import tkinter as tk
from tkinter import ttk
import math

class Pomodoro:
    def __init__(self, root):

        #### Atributes ####
        # Palet color
        self.yellow = "#f7f5dd"
        self.green = "#9bdeac"
        # Timer (seconds)
        self.work = 5
        self.rest = 3
        self.big_rest = 10
        self.repetitions = 5
        self.timerobj = None
        # Geometry
        self.width = 200
        self.height = 200
        self.font = ("Arial", 23, "bold")
        self.pad = 2
        # Img
        root.tomato_img = self.tomato_img = tk.PhotoImage(file="tomato.png")

        #### GUI ####
        # Root
        root.title("Pomodoro Technique")
        root.minsize(width=self.width, height=self.height)
        root.config(padx=20, pady=20, bg=self.yellow)
        root.resizable(1, 1)

        # Main content frame
        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky="NSEW")

        # Canvas widgets
        self.canvas = tk.Canvas(self.mainframe, width=220, height=240, bg=self.yellow)
        self.canvas.create_image(106,112, image=root.tomato_img)
        self.timer = self.canvas.create_text(108, 140, text="00:00", fill="white", font=self.font)
        self.canvas.grid(column=2, row=2)

        # Text widgets
        ttk.Label(self.mainframe, text="Timer", font=self.font, foreground=self.green, background=self.yellow).grid(column=2, row=1)
        ttk.Label(self.mainframe, text="✓", foreground=self.green, background=self.yellow).grid(column=2, row=4)
        # Button widhets
        ttk.Button(self.mainframe, text="Start", command=self.start_count).grid(column=1, row=3, padx= self.pad, pady=self.pad)
        ttk.Button(self.mainframe, text="Reset", command=self.reset_count).grid(column=3, row=3, padx=self.pad, pady=self.pad)

        #### Modules ####
    def countdown(self, count):
        # Compute time
        minutes = math.floor(count / 60)
        seconds = count % 60
        # Update canvas
        self.canvas.itemconfig(self.timer, text=f"{minutes:02}:{seconds:02}")
        # Check for timer end
        if count > 0:
            # Wait 1 sec and call countdown with count - 1
            self.timerobj = root.after(1000, self.countdown, count - 1)
        elif self.repetitions >= 0:
            self.start_count()
    def start_count(self):
        if self.repetitions % 2 == 1:
            self.countdown(self.work)
            self.repetitions -= 1
        elif self.repetitions == 0:
            self.countdown(self.big_rest)
            self.repetitions -= 1
        else:
            self.countdown(self.rest)
            self.repetitions -= 1

    def reset_count(self):
        root.after_cancel(self.timerobj)
        self.canvas.itemconfig(self.timer, text="00:00")

if __name__ == '__main__':
    root = tk.Tk()
    Pomodoro(root)
    root.mainloop()