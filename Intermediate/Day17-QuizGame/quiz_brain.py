### Modules
from random import shuffle
from copy import deepcopy 

### Class
class QuizBrain:
    def __init__(self, q_list):
        # Current question number
        self.number = 0
        # Randomize the provided list
        self.list = deepcopy(q_list)
        shuffle(self.list)
        # Score of current game
        self.score = 0
    
    # List index for the next question
    def ask_question(self):
        # Current question
        self.current_question = self.list[self.number]
        # Next question
        self.number += 1
        # Ask the current question to player and get answer
        player_answer = input(f"Q.{self.number}: {self.current_question.text}").lower()

        return player_answer
    
    # Check if player answered the right question
    def check_answer(self, player_answer):
        if player_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False

    def display_win(self):
        print(f"You got it right!")
        print(f"The current score is {self.score}/{self.number}.\n")

    def display_loose(self):
        print(f"Wrong, the right answer was {self.current_question.answer}.")
        print(f"The current score is {self.score}/{self.number}.\n")

    # Check if all question asked
    def end(self):
        return self.number < len(self.list)

    
