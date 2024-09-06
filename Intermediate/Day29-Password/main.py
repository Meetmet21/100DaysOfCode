import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets

import pyperclip

class PasswordManager:
    def __init__(self, root):
        # Password
        self.password_length = 12
        # Data recors
        self.datanase = "data.txt"

        # Geometry
        self.width = 600
        self.height = 400
        self.font = ("Arial", 16, "bold")
        self.pad = 50

        # Text variables
        self.email = tk.StringVar()
        self.website = tk.StringVar()
        self.password = tk.StringVar()

        # Root
        root.title("Password Manager", )
        root.minsize(width=self.width, height=self.height)
        root.config(padx=self.pad, pady=self.pad)
        root.logo = self.logo =tk.PhotoImage(file="logo.png")

        #Frame
        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky="nwes")

        self.password_frame = ttk.Frame(self.mainframe)
        self.password_frame.grid(column=2, row=4)

        # Canvas
        self.canvas = tk.Canvas(self.mainframe, width=400, height=200)
        self.canvas.create_image(100, 100, image=root.logo)
        self.canvas.grid(column=2, row=1)

        # Text
        ttk.Label(self.mainframe, text="Website:", font=self.font, anchor=tk.CENTER).grid(column=1, row=2)
        ttk.Label(self.mainframe, text="Email/Username:", font=self.font, anchor=tk.CENTER).grid(column=1, row=3)
        ttk.Label(self.mainframe, text="Password:", font=self.font, anchor=tk.CENTER).grid(column=1, row=4)

        # Entry
        self.entry_website = ttk.Entry(self.mainframe, font=("Arial", 12), textvariable=self.website)
        self.entry_website.grid(column=2, row=2, sticky="EW")
        self.entry_website.focus()
        self.entry_email = ttk.Entry(self.mainframe, font=("Arial", 12), textvariable=self.email).grid(column=2, row=3, sticky="EW")
        self.entry_password = ttk.Entry(self.password_frame, font=("Arial", 12), textvariable=self.password, show="*").grid(column=1, row=1, padx=(0,20))

        # Buttons
        ttk.Button(self.password_frame, text="Generate Password", command=self.generate_password).grid(column=2, row=1, padx=(20,0))
        ttk.Button(self.mainframe, text="Add", command=self.save).grid(column=2, row=5, sticky="EW")

    def generate_password(self):
        self.password.set(secrets.token_urlsafe(self.password_length))
        # Copy to clipboard
        pyperclip.copy(self.password.get())

    def save(self):
        if (len(self.email.get()) == 0
                or len(self.password.get()) == 0
                or len(self.website.get()) == 0):
            messagebox.showinfo(title="Oops..", message="Fill all the information fields!")
        else:
            is_ok = messagebox.askokcancel(title="Validation requested", message=f"Do you want to save current entries:"
                                                                         f"\nwebsite: {self.website.get()}"
                                                                         f"\nemail: {self.email.get()}"
                                                                         f"\nPassword:" )
            if is_ok:
                with open(file=self.datanase, mode="a") as database:
                    database.write(f"{self.website.get()} | {self.email.get()} | {self.password.get()}\n")

                # Erase previous entries
                self.password.set("")
                self.email.set("")
                self.website.set("")



if __name__ == '__main__':
    root = tk.Tk()
    PasswordManager(root)
    root.mainloop()