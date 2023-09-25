# assignment: programming assignment 2
# author: (Aditya Bhaskar)
# date: (25th October 2020)
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import randint

done= False
print("Play a game: Guess My Number")

while not done:
    mynum= randint(1,10)
    #print(mynum)
    print("You have three attempts to guess my number.")
    yournum=int(input("Please enter a number from 1 to 10:"))
    for x in range(0,2):
        if yournum==mynum:
            break
        if yournum<mynum:
            print("You guessed wrong. Your number is smaller than mine.")
            yournum=int(input("Guess again. Please enter a number:"))
        elif yournum>mynum:
            print("You guessed wrong. Your number is bigger than mine.")
            yournum=int(input("Guess again. Please enter a number:"))
        else:
            print("Wrong Input!!!")
    if yournum!=mynum:
         print(f"Sorry you lost. My number is {mynum}.")
    else:
        print(f"You guessed right. My number is {mynum}. Congratulations you won!")
    yesno=input("Would you like to play again[Y/N]?")
    if yesno=='Y' or yesno=='y':
        done= False
    else:
        done= True
        print("Goodbye!")
