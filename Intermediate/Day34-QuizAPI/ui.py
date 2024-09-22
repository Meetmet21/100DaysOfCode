import tkinter as tk
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Tk instance
        self.root = tk.Tk()
        self.quiz = quiz_brain

        # Widget parameters
        self.font = ("Arial", 20, "italic")
        self.pad = 20
        self.theme_color = "#375362"
        self.canvas_height = 250
        self.canvas_width = 400

        # Variables
        self.current_score = tk.StringVar(value=f"Score: 0")
        self.button_pressed = tk.BooleanVar(value=False)

        # Main window
        self.root.title("Quizzler")
        self.root.config(pady=self.pad, padx=self.pad, bg=self.theme_color)

        # Images
        try:
            self.root.false = tk.PhotoImage(file="images/false.png")
            self.root.true = tk.PhotoImage(file="images/true.png")
        except FileNotFoundError:
            raise FileNotFoundError("Check paths of images to be loaded.")

        ### Widgets ###
        # Nain Frame
        self.main = tk.Frame(self.root, bg=self.theme_color)
        self.main.grid(column=0, row=0, sticky="nwes")

        # Buttons
        self.true = tk.Button(self.main, image=self.root.true, command=self.right_pressed)
        self.true.grid(column=1, row=3)
        self.wrong = tk.Button(self.main, image=self.root.false, command=self.wrong_pressed)
        self.wrong.grid(column=2, row=3)

        # Label
        self.score = tk.Label(self.main, textvariable=self.current_score, anchor="center", fg="white",
                              bg=self.theme_color)
        self.score.grid(column=2, row=1)

        # Canvas for flash cards
        self.canvas = tk.Canvas(self.main, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(column=1, row=2,columnspan=2, pady=(50,50))
        self.q_text = self.canvas.create_text(200, 125, text="French",
                                              font=self.font, fill=self.theme_color,
                                              width=250)
        # Generate first question
        self.next_question()

        self.root.mainloop()

    def next_question(self):
        if self.quiz.question_number >= len(self.quiz.question_list):
            self.canvas.itemconfig(self.q_text, text=self.current_score.get())
            self.current_score.set("")
            self.wrong.config(state="disabled")
            self.true.config(state="disabled")
        else:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.current_score.set(f"Score: {self.quiz.score}")

    def right_pressed(self):
        self.quiz.check_answer("True")
        self.next_question()

    def wrong_pressed(self):
        self.quiz.check_answer("False")
        self.next_question()
