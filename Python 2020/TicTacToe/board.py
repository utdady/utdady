class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""

    def get_size(self):
        # optional, return the board size (an instance size)
        return self.size**2

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with sign X or O
        self.board[cell] = sign

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        if self.board[cell] == " ":
            return True

    def isdone(self, sign):
        done = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        if self.board[0] == sign and self.board[1] == sign and self.board[2] == sign:
            done = True
        if self.board[3] == sign and self.board[4] == sign and self.board[5] == sign:
            done = True
        if self.board[6] == sign and self.board[7] == sign and self.board[8] == sign:
            done = True
        if self.board[0] == sign and self.board[3] == sign and self.board[6] == sign:
            done = True
        if self.board[1] == sign and self.board[4] == sign and self.board[7] == sign:
            done = True
        if self.board[2] == sign and self.board[5] == sign and self.board[8] == sign:
            done = True
        if self.board[0] == sign and self.board[4] == sign and self.board[8] == sign:
            done = True
        if self.board[2] == sign and self.board[4] == sign and self.board[6] == sign:
            done = True
        self.winner = sign
        return done
    
    def mtcheck(self):
        dumb = False
        if self.board[0] != " " and self.board[1] != " " and self.board[2] != " " and self.board[3] != " " and self.board[4] != " " and self.board[5] != " " and self.board[6] != " " and self.board[7] != " " and self.board[8] != " ":
            dumb = True
        return dumb

    def show(self):
        # draw the board
        print("\n   A   B   C  ")
        print(" +---+---+---+")
        print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(" +---+---+---+")
        print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(" +---+---+---+")
        print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
        print(" +---+---+---+")
        
