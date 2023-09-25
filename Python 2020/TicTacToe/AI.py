import random 
class AI:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def ai_choose(self, board):
        flag = True
        print("\nCPU's turn: ")
        while flag:
            cell = random.randint(0,8)
            if board.isempty(cell):
                SIGN = AI.get_sign(self)
                board.set(cell, SIGN)
                flag = False
            else:
                flag = True
          
        
