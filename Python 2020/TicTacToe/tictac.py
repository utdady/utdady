# author: Aditya Bhaskar
# date: December 15, 2020
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from os import system
from board import Board
from player import Player
from AI import AI
from SmartAI import SmartAI

# main program

print("Welcome to TIC-TAC-TOE Game!")
while True:
    gamer = input("\nPlayer v Player [PVP] or CPU [CPU]: ").upper()
    if gamer == "PVP":
        P1 = input("\nPlayer One, Enter Name: ")
        P2 = input("\nPlayer Two, Enter Name: ")
        board = Board()
        player1 = Player(P1, "X")
        player2 = Player(P2, "O")
        turn = True
        board.show()
        while True:
            if turn:
                player1.choose(board)
                turn = False
            else:
                player2.choose(board)
                turn = True
            SiGn = player1.get_sign()
            sIgN = player2.get_sign()
            if board.mtcheck():
                break
            if board.isdone(SiGn):
                break
            if board.isdone(sIgN):
                break
            board.show()
        if board.isdone(SiGn):   
            if board.get_winner() == player1.get_sign():
                board.show()
                print(f"\n{player1.get_name()} is a winner!")
        elif board.isdone(sIgN):
            if board.get_winner() == player2.get_sign():
                board.show()
                print(f"\n{player2.get_name()} is a winner!")
        else:
                board.show()
                print("\nIt is a tie!")
    elif gamer == "CPU":
        lvl = input("\nEasy [e] or Normal [n]: ").upper()
        if lvl == "E":
            P1 = input("\nPlayer, Enter Name: ")
            board = Board()
            player1 = Player(P1, "X")
            player2 = AI("CPU", "O")
            turn = True
            board.show()
            while True:
                if turn:
                    player1.choose(board)
                    turn = False
                else:
                    player2.ai_choose(board)
                    turn = True
                SiGn = player1.get_sign()
                sIgN = player2.get_sign()
                if board.mtcheck():
                    break
                if board.isdone(SiGn):
                    break
                if board.isdone(sIgN):
                    break
                board.show()
            if board.isdone(SiGn):   
                if board.get_winner() == player1.get_sign():
                    board.show()
                    print(f"\n{player1.get_name()} is a winner!")
            elif board.isdone(sIgN):
                if board.get_winner() == player2.get_sign():
                    board.show()
                    print(f"\n{player2.get_name()} is a winner!")
            else:
                board.show()
                print("\nIt is a tie!")
        elif lvl == "N":
            P1 = input("\nPlayer, Enter Name: ")
            board = Board()
            player1 = Player(P1, "X")
            player2 = SmartAI("CPU", "O")
            turn = True
            board.show()
            while True:
                if turn:
                    player1.choose(board)
                    turn = False 
                else:
                    player2.S_ai_choose(board)
                    turn = True
                SiGn = player1.get_sign()
                sIgN = player2.get_sign()
                if board.mtcheck():
                    break
                if board.isdone(SiGn):
                    break
                if board.isdone(sIgN):
                    break
                board.show()
            if board.isdone(SiGn):   
                if board.get_winner() == player1.get_sign():
                    board.show()
                    print(f"\n{player1.get_name()} is a winner!")
            elif board.isdone(sIgN):
                if board.get_winner() == player2.get_sign():
                    board.show()
                    print(f"\n{player2.get_name()} is a winner!")
            else:
                board.show()
                print("\nIt is a tie!")
    else:
        print("\nWrong Input!")
    ans = input("\nWould you like to play again? [Y/N] ").upper()
    if (ans != "Y"):
        break
print("\nGoodbye!")
