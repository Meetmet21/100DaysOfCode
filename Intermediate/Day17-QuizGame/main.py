### Description
# In this project, I implemented a simple quiz game

### Modules
from data import question_data # Quiz questions
from question_model import Question # Question class to build question formated
from quiz_brain import QuizBrain # Handle the questioning process and I/O

### Variables
# list of formated questions
question_bank = []

### Main program
# Build question bank
for f_question in question_data:
    question_bank.append(Question(f_question['question'], f_question['correct_answer']))

# Iniate the questioning process
master = QuizBrain(question_bank)

while master.end():
    # Ask a question
    player_answer = master.ask_question()
    # Check the answer nad if right
    if master.check_answer(player_answer):
        master.display_win()
    # If wrong
    else:
        master.display_loose()


 