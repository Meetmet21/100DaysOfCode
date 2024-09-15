import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import json

import pyperclip

class PasswordManager:
    def __init__(self, root):
        # Password
        self.password_length = 12
        # Data recors
        self.database = "data.json"

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
        self.entry_password = ttk.Entry(self.mainframe, font=("Arial", 12), textvariable=self.password, show="*").grid(column=2, row=4, sticky="we")

        # Buttons
        ttk.Button(self.mainframe, text="Generate Password", command=self.generate_password).grid(column=3, row=4, padx=(20,0))
        ttk.Button(self.mainframe, text="Add", command=self.save).grid(column=2, row=5, sticky="EW")
        ttk.Button(self.mainframe, text="Search", command=self.search).grid(column=3, row=2, stick="ew", padx=(20,0))

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
                new_data = {
                    self.website.get().capitalize(): {
                        "email": self.email.get(),
                        "password": self.password.get()
                    }
                }
                # Check if data file exists
                try:
                    with open(file=self.database, mode="r") as database:
                        # Read the old data
                        data = json.load(fp=database)

                except FileNotFoundError:
                    # Write the new data
                    with open(file=self.database, mode="w") as database:
                        json.dump(obj=new_data, fp=database, indent=4, sort_keys=True)
                else:
                    # Update old data
                    data.update(new_data)
                    # Write new data
                    with open(file=self.database, mode="w") as database:
                        json.dump(obj=data, fp=database, indent=4, sort_keys=True)

                # Erase previous entries
                self.password.set("")
                self.email.set("")
                self.website.set("")

    def search(self):
        try:
            with open(self.database, "r") as database:
                data = json.load(fp=database)

                # Message
                messagebox.showinfo(title=self.website.get(),
                                    message=f"Email: {data[self.website.get().capitalize()]["email"]}\n"
                                            f"Password: {data[self.website.get().capitalize()]["password"]}")
        # Catch no file or keyerror
        except:
            messagebox.showinfo(title="No data yet.", message="There is no data registered in the database!")


if __name__ == '__main__':
    root = tk.Tk()
    PasswordManager(root)
    root.mainloop()