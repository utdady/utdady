class SmartAI:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def S_ai_choose(self, board):
        Sign = SmartAI.get_sign(self)
        print("\nCPU's turn: ")
        if board.board[0] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[1] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[6] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[2] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(8):
                            board.set(8, Sign)
            elif board.board[3] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[5] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[1] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[6] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(8):
                            board.set(8, Sign)
            elif board.board[7] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[8] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
        
        if board.board[2] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(8):
                            board.set(8, Sign)
            elif board.board[1] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[3] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[3] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[1] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[5] == "X":
                if board.isempty(8):
                    board.set(8, Sign)
                if board.board[0] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[6] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[7] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[8] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
        if board.board[6] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(8):
                            board.set(8, Sign)
            elif board.board[1] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[2] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[3] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[1] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[5] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[7] == "X":
                if board.isempty(8):
                    board.set(8, Sign)
                if board.board[0] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[8] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[1] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)

        if board.board[8] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[1] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[2] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
            elif board.board[3] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[5] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[6] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[1] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[6] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[1] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
            elif board.board[7] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[3] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)

        if board.board[1] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[6] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[2] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[3] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[3] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[5] == "X":
                if board.isempty(8):
                    board.set(8, Sign)
                if board.board[0] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[6] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[7] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
                    elif board.board[3] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
            elif board.board[8] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[6] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)

        if board.board[3] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(1):
                        board.set(1, Sign)
                    if board.board[7] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[1] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[6] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[5] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[6] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[1] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
                    elif board.board[6] == "X":
                        if board.isempty(1):
                            board.set(6, Sign)
            elif board.board[6] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[1] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
            elif board.board[7] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[2] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[1] == "X":
                    if board.isempty(0):
                        board.set(0, Sign)
                    if board.board[8] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[8] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[7] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
        if board.board[7] == "X":
            if board.isempty(4):
                board.set(4, Sign)
            if board.board[0] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[3] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[2] == "X":
                if board.isempty(0):
                    board.set(0, Sign)
                if board.board[8] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[3] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
                    elif board.board[2] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[2] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[5] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[3] == "X":
                if board.isempty(8):
                    board.set(8, Sign)
                if board.board[0] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[2] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[5] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(8):
                        board.set(8, Sign)
                    if board.board[0] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[6] == "X":
                if board.isempty(8):
                    board.set(8, Sign)
                if board.board[0] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[5] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[8] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[2] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[3] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
                            
        if board.board[4] == "X":
            if board.isempty(0):
                board.set(0, Sign)
            if board.board[1] == "X":
                if board.isempty(7):
                    board.set(7, Sign)
                if board.board[2] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[8] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
                elif board.board[3] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[2] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
                    elif board.board[6] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
                elif board.board[5] == "X":
                    if board.isempty(3):
                        board.set(3, Sign)
                    if board.board[6] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
                elif board.board[6] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[3] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
                    elif board.board[5] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[2] == "X":
                if board.isempty(6):
                    board.set(6, Sign)
                if board.board[3] == "X":
                    if board.isempty(5):
                        board.set(5, Sign)
                    if board.board[1] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
                    elif board.board[7] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[3] == "X":
                if board.isempty(5):
                    board.set(5, Sign)
                if board.board[1] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[2] == "X":
                        if board.isempty(6):
                            board.set(6, Sign)
                    elif board.board[6] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(2):
                            board.set(2, Sign)
                elif board.board[2] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[1] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
                    elif board.board[7] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(1):
                            board.set(1, Sign)
            elif board.board[5] == "X":
                if board.isempty(3):
                    board.set(3, Sign)
                if board.board[6] == "X":
                    if board.isempty(2):
                        board.set(2, Sign)
                    if board.board[1] == "X":
                        if board.isempty(7):
                            board.set(7, Sign)
            elif board.board[6] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[1] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[3] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
                    elif board.board[5] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
                    elif board.board[8] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
            elif board.board[7] == "X":
                if board.isempty(1):
                    board.set(1, Sign)
                if board.board[2] == "X":
                    if board.isempty(6):
                        board.set(6, Sign)
                    if board.board[3] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
            elif board.board[8] == "X":
                if board.isempty(2):
                    board.set(2, Sign)
                if board.board[1] == "X":
                    if board.isempty(7):
                        board.set(7, Sign)
                    if board.board[3] == "X":
                        if board.isempty(5):
                            board.set(5, Sign)
                    elif board.board[5] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
                    elif board.board[6] == "X":
                        if board.isempty(3):
                            board.set(3, Sign)
        
