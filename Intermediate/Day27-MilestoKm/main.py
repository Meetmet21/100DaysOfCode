import tkinter as tk
from tkinter import ttk

class MileToKm:
    def __init__(self, root):
        # Minsize
        self.width = 300
        self.height = 100
        self.font = ("Arial", 18, "bold")
        self.pad = 5
        self.Kilometers = tk.StringVar()
        self.miles = tk.StringVar()

        # Root
        root.title("Miles to Km Converter")
        root.minsize(width=self.width, height=self.height)
        root.config(padx=20, pady=20)

        # Main content frame
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky="nwes")

        # Text widgets
        ttk.Label(mainframe, text="is equal to", font=self.font, ).grid(column=1, row=2, padx=self.pad, pady=self.pad,)
        ttk.Label(mainframe, text="Miles", font=self.font).grid(column=3, row=1, padx=self.pad, pady=self.pad)
        ttk.Label(mainframe, font=self.font, textvariable=self.Kilometers).grid(column=2, row=2, padx=self.pad, pady=self.pad)
        ttk.Label(mainframe, font=self.font, text="Km").grid(column=3, row=2, padx=self.pad, pady=self.pad)

        # Entry widgets
        ttk.Entry(mainframe, textvariable=self.miles, width=8).grid(column=2, row=1, padx=self.pad, pady=self.pad)

        # Button widgets
        ttk.Button(mainframe, text="Calculate", command=self.miles_to_km,).grid(column=2, row=3, padx=self.pad, pady=self.pad)

    def miles_to_km(self, *args):
        try:
            value = float(self.miles.get())
            self.Kilometers.set(str(value * 1.61))
        except ValueError:
            root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    MileToKm(root)
    root.mainloop()
