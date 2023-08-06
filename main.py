import random

class UserInput:

    def __init__(self):
        self.min = int(input('最小値を教えてください\n'))
        self.max = int(input('最大値を教えてください\n'))
        self.user_answer = int(input('答えをどうぞ！'))

class Game:
    def __init__(self,min,max):
        self.answer = random.randint(min, max)
    
    def hint1_even_or_not(self):
        return "偶数です" if self.answer % 2 == 0 else "奇数です"

    def hint2_is_multiple_of_3(self):
        return "3の倍数です" if self.answer % 3 == 0 else "3の倍数ではありません"
    
    def hint3_is_multiple_of_5(self):
        return "5の倍数です" if self.answer % 5 == 0 else "5の倍数ではありません"

    def hint4_is_multiple_of_7(self):
        return "7の倍数です" if self.answer % 7 == 0 else "7の倍数ではありません"
    
    def hint5_is_multiple_of_9(self):
        return "9の倍数です" if self.answer % 9 == 0 else "9の倍数ではありません"

    def is_user_answer_correct(self,user_answer):
        return "正解です！" if self.answer == user_answer else "不正解です..."
    
class main:

    def __init__(self):
        self.user_input = UserInput()
        self.game = Game(self.user_input.min,self.user_input.max)
        self.loop()
    def loop(self):
        while self.game.is_user_answer_correct(self.user_input.user_answer) != "正解です！":
            print(self.game.is_user_answer_correct(self.user_input.user_answer))
            print("-----ヒント-----")
            print(self.game.hint1_even_or_not())
            print(self.game.hint2_is_multiple_of_3())
            print(self.game.hint3_is_multiple_of_5())
            print(self.game.hint4_is_multiple_of_7())
            print(self.game.hint5_is_multiple_of_9())
            self.user_input.user_answer = int(input('答えをどうぞ！'))
        print(self.game.is_user_answer_correct(self.user_input.user_answer))

main()