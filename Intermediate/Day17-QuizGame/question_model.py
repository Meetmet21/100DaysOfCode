### Definition
# Creat the appropriate structure for questions

class Question:
    # Initiate an object with a question text and the answer to the question
    def __init__(self, text, answer):
        # Formated text
        self.text = f"{text} (True/False)?: "
        # Correct answer
        self.answer = answer.lower()