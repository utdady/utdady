import random

assign = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
win = False

def check(matrix, sign):

    ''' Function to check all of the winning conditions. '''

    # First Row
    if matrix[0][0] == sign and matrix[0][1] == sign and matrix[0][2] == sign:
        return True

    # Second Row
    if matrix[1][0] == sign and matrix[1][1] == sign and matrix[1][2] == sign:
        return True

    # Third Row
    if matrix[2][0] == sign and matrix[2][1] == sign and matrix[2][2] == sign:
        return True
    
    # First Column
    if matrix[0][0] == sign and matrix[1][0] == sign and matrix[2][0] == sign:
        return True

    # Second Column
    if matrix[0][1] == sign and matrix[1][1] == sign and matrix[2][1] == sign:
        return True

    # Third Column
    if matrix[0][2] == sign and matrix[1][2] == sign and matrix[2][2] == sign:
        return True

    # Principal Diagonal
    if matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign:
        return True

    # Secondary Diagonal 
    if matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign:
        return True

def is_empty(pos, matrix, assign):

    ''' Function to check if a space is empty or not. '''
    
    m, n = assign[pos][0], assign[pos][1]
    
    if matrix[m][n] == " ":
        return True
    else:
        return False

def board(matrix):

    ''' Playing Board. '''
    
    return f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}\n-----------\n {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}\n-----------\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} "

def playerMove(P, S):

    ''' A function that allows the player to take his turn. '''
    
    cond = False
    while not cond:

        # Player chooses their space.
        pos = int(input(f"\n{S}, {P} choose a valid space [1-9]: "))

        # To check if the player chooses a valid space.
        if 0 < pos < 10:
            if is_empty(pos, matrix, assign):
                matrix[assign[pos][0]][assign[pos][1]] = S
                cond = True
            else:
                print("!Please select an empty space!")
                cond = False
        else:
            print("!Please select a valid space!")
            cond = False

    # Displays the board.
    print("\n", board(matrix))

    # To check if the player has won, after each turn.
    if check(matrix, S):
        print(f"\n{S}, {P} gets the W!")
        return True
    else:
        return False

def compMoveE(S):

    ''' A function that allows the computer to move on random. '''
    
    print("\nComputer's Turn:")

    cond = False
    while not cond:

        # Computer takes its turn.
        pos = random.randint(1,9)

        # Checks if space is empty.
        if is_empty(pos, matrix, assign):
            matrix[assign[pos][0]][assign[pos][1]] = S
            cond = True
        else:
            cond = False
            
    # Displays the board.
    print("\n", board(matrix))

    # Checks the winning condition after each turn.
    if check(matrix, S):
        print(f"\nComputer gets the W!")
        return True
    else:
        return False
    
def main():

    # Symbols
    symbol = ['X', 'O']

    input("Press ENTER key to start.....")
    
    print("\n1. Player versus Player [PVP]\n2. CPU [Easy]\n3. CPU [Hard]\n")
    gameMode = input("Select the game mode: ")

    # Player versus player mode.
    if gameMode == '1' or gameMode.upper() in ("PVP", "P"):

        # Players enter their names.
        P1 = input("\nPlayer 1, Name: ")
        P2 = input("Player 2, Name: ")
        
        matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        win = False

        # Random allotment of symbol
        P1S = random.choice(symbol)
        if P1S == 'X':
            P2S = 'O'
        else:
            P2S = 'X'

        print(f"\n{P1} has symbol {P1S}.\n{P2} has symbol {P2S}.\n")

        # Displays the board.
        print(board(matrix))

        # If Player 1 has X.
        if P1S == 'X':

            # First move.
            if playerMove(P1, P1S):
                pass

            # Subsequent moves.
            for i in range(0,4):
                if playerMove(P2, P2S):
                    win = True
                    break
                elif playerMove(P1, P1S):
                    win = True
                    break
                i += 1

        # If Player 1 has O.
        elif P1S == 'O':

            # First move.
            if playerMove(P2, P2S):
                pass

            # Subsequent moves.
            for i in range(0,4):
                if playerMove(P1, P1S):
                    win = True
                    break
                elif playerMove(P2, P2S):
                    win = True
                    break
                i += 1

        if win == False:
            print("\nIt's a tie!")

    elif gameMode == '2' or gameMode.upper() in ("EASY","E"):

        P = input("\nEnter player name: ")
        matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        win = False
        
        PS = random.choice(symbol)
        if PS == 'X':
            CS = 'O'
        else:
            CS = 'X'

        print(f"\n{P} has symbol {PS}.\nComputer has symbol {CS}.\n")
        print(board(matrix))

        if PS == 'X':
            if playerMove(P, PS):
                pass
            for i in range(0,4):
                if compMoveE(CS):
                    win = True
                    break
                if playerMove(P, PS):
                    win = True
                    break
                i += 1

        elif PS == 'O':
            if compMoveE(CS):
                pass
            for i in range(0,4):
                if playerMove(P, S):
                    win = True
                    break
                if compMoveE(CS):
                    win = True
                    break
                i += 1

        if win == False:
            ("\nIt's a tie!")

main()

