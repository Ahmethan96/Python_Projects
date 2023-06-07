from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for i in ((question_data)):
        (question_bank.append(Question(i["text"], i["answer"])))

quiz = Quiz(question_bank)

while quiz.ask_user():
        quiz.ask_user()
