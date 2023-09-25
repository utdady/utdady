import random

def check(matrix, sign):

    '''Function to check all the winning conditions.'''
    
    if matrix[0][0] == sign and matrix[0][1] == sign and matrix[0][2] == sign:
        return True
    if matrix[1][0] == sign and matrix[1][1] == sign and matrix[1][2] == sign:
        return True
    if matrix[2][0] == sign and matrix[2][1] == sign and matrix[2][2] == sign:
        return True
    if matrix[0][0] == sign and matrix[1][0] == sign and matrix[2][0] == sign:
        return True
    if matrix[0][1] == sign and matrix[1][1] == sign and matrix[2][1] == sign:
        return True
    if matrix[0][2] == sign and matrix[1][2] == sign and matrix[2][2] == sign:
        return True
    if matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign:
        return True
    if matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign:
        return True


def is_empty(pos, matrix, assign):

    '''Function to check if a space is empty or not.'''
     
    m, n = assign[pos][0], assign[pos][1]
    if matrix[m][n] == " ":
        return True
    else:
        return False


def board(matrix):

    '''Playing Board.'''
    
    return f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}\n-----------\n {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}\n-----------\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} "


def main():
    assign = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    symbol = ['X', 'O']

    input("Press ENTER key to start.....")
    
    print("\n1. Player versus Player [PVP]\n2. CPU [Easy]\n3. CPU [Hard]\n")
    gameMode = input("Select the game mode: ")

    if gameMode == '1' or gameMode.upper() in ("PVP", "P"):
        P1 = input("\nPlayer 1, Name: ")
        P2 = input("Player 2, Name: ")
        win = False

        P1sym = random.choice(symbol)
        if P1sym == 'X':
            P2sym = 'O'
        else:
            P2sym = 'X'

        print(f"\n{P1} has symbol {P1sym}.\n{P2} has symbol {P2sym}.\n")
        print(board(matrix))
        
        if P1sym == 'X':
            cond = False
            while not cond:
                pos = int(input(f"\n{P1sym}, {P1} choose a valid space [1-9]: "))
                if 0 < pos < 10:
                    p, q = assign[pos][0], assign[pos][1]
                    matrix[p][q] = P1sym
                    cond = True
                else:
                    print("!Please select a valid space!\n")
                    cond = False
            print("\n", board(matrix))
            for i in range(0,4):
                cond = False
                while not cond:
                    pos = int(input(f"\n{P2sym}, {P2} choose a valid space [1-9]: "))
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = P2sym
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, P2sym):
                    print(f"\n{P2sym}, {P2} gets the W!")
                    win = True
                    break
                cond = False
                while not cond:
                    pos = int(input(f"\n{P1sym}, {P1} choose a valid space [1-9]: "))
                    p, q = assign[pos][0], assign[pos][1]
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = P1sym
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, P1sym):
                    print(f"\n{P1sym}, {P1} gets the W!")
                    win = True
                    break
                i += 1
            
        if P1sym == 'O':
            cond = False
            while not cond:
                pos = int(input(f"\n{P2sym}, {P2} choose a valid space [1-9]: "))
                if 0 < pos < 10:
                    p, q = assign[pos][0], assign[pos][1]
                    matrix[p][q] = P2sym
                    cond = True
                else:
                    print("!Please select a valid space!\n")
                    cond = False
            print("\n", board(matrix))
            for i in range(0,4):
                cond = False
                while not cond:
                    pos = int(input(f"\n{P1sym}, {P1} choose a valid space [1-9]: "))
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = P1sym
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, P1sym):
                    print(f"\n{P1sym}, {P1} gets the W!")
                    win = True
                    break
                cond = False
                while not cond:
                    pos = int(input(f"\n{P2sym}, {P2} choose a valid space [1-9]: "))
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = P2sym
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, P2sym):
                    print(f"\n{P2sym}, {P2} gets the W!")
                    win = True
                    break
                i += 1

        if win == False:
            print("\nIt's a tie!")
            
    elif gameMode == '2' or gameMode.upper() in ("EASY","E"):
        P = input("\nEnter player name: ")
        win = False
        space = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        Psym = random.choice(symbol)
        if Psym == 'X':
            Csym = 'O'
        else:
            Csym = 'X'
            
        print(f"\n{P} has symbol {Psym}.\nComputer has symbol {Csym}.\n")
        print(board(matrix))

        if Psym == 'X':
            cond = False
            while not cond:
                pos = int(input(f"\n{Psym}, {P} choose a valid space [1-9]: "))
                if 0 < pos < 10:
                    p, q = assign[pos][0], assign[pos][1]
                    matrix[p][q] = Psym
                    space.remove(pos)
                    cond = True
                else:
                    print("!Please select a valid space!\n")
                    cond = False
            print("\n", board(matrix))
            for i in range(0,4):
                print("\nComputer's Turn:")
                pos = random.choice(space)
                matrix[assign[pos][0]][assign[pos][1]] = Csym
                space.remove(pos)
                print("\n", board(matrix))
                if check(matrix, Csym):
                    print(f"\nComputer gets the W!")
                    win = True
                    break
                cond = False
                while not cond:
                    pos = int(input(f"\n{Psym}, {P} choose a valid space [1-9]: "))
                    p, q = assign[pos][0], assign[pos][1]
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = Psym
                            space.remove(pos)
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, Psym):
                    print(f"\n{Psym}, {P} gets the W!")
                    win = True
                    break
                i += 1

        if Psym == 'O':
            print("\nComputer's Turn:")
            pos = random.choice(space)
            matrix[assign[pos][0]][assign[pos][1]] = Csym
            space.remove(pos)
            print("\n", board(matrix))
            for i in range(0,4):
                cond = False
                while not cond:
                    pos = int(input(f"\n{Psym}, {P} choose a valid space [1-9]: "))
                    if 0 < pos < 10:
                        p, q = assign[pos][0], assign[pos][1]
                        if is_empty(pos, matrix, assign):
                            matrix[p][q] = Psym
                            space.remove(pos)
                            cond = True
                    else:
                        print("!Please select a valid space!\n")
                        cond = False
                print("\n", board(matrix))
                if check(matrix, Psym):
                    print(f"\n{Psym}, {P} gets the W!")
                    win = True
                    break
                print("\nComputer's Turn:")
                pos = random.choice(space)
                matrix[assign[pos][0]][assign[pos][1]] = Csym
                space.remove(pos)
                print("\n", board(matrix))
                if check(matrix, Csym):
                    print(f"\nComputer gets the W!")
                    win = True
                    break
                i += 1

        if win == False:
            ("\nIt's a tie!")

            

main()
