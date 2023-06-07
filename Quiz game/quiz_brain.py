# from main import question_bank

class Quiz:

    def __init__(self, list):
        self.q_number = 0
        self.bank = list
        # self.ask = input("Q {}. {} True/False: ".format(self.q_number, self.bank[self.q_number]["text"]))

    def next_question(self):
        if self.q_number <= len(self.bank):
            self.q_number += 1
            return self.q_number

    def ask_user(self):
        ask = input("Q.{} {} (True/False)?: ".format(self.q_number + 1,self.bank[self.q_number].text))


        if ask == self.bank[self.q_number].answer:
            self.next_question()
            print("nice")
            return True
        else:
            print("wrong")
            return False





# print(Quiz(question_bank[0].text))
# print(Quiz(question_bank[0]))
# print(Quiz(question_bank).next_question())
