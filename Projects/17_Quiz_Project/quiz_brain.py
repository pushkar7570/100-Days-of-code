class QuizBrain:

    def __init__(self, q_list):
        self.answer = ""
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_ques(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_ques.text} (True/False): ").lower()
        correct_answer = current_ques.answer.lower()
        self.check_answer(user_answer, correct_answer)

    def still_has_ques(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, u_ans, corr_ans):
        if u_ans == corr_ans:
            self.score += 1
            print("You got it right!!")
        else:
            print("You got it  wrong.")

        print(f"The correct answer was: {corr_ans}")
        print(f"Your current score is {self.score}/{self.question_number}\n ")


        
