

from random import randint

done= False
print("Play a game: Guess My Number")

while not done :
    mynum= randint(1, 10)
    print(mynum)
    print("You have three attempts to guess my number.")
    yournum=int(input("Please enter a number from 1 to 10:"))
    if yournum==mynum:
        print("You won")
        break
    else:
        for x in range(0,3):
            if yournum<mynum:
                print("smol")
                yournum=int(input("guess"))
            elif yournum>mynum:
                print("big")
                yournum=int(input("guess"))
    yesno=input("Would you like to play again[Y/N]?")
    if yesno=='Y' or yesno=='y':
        done= False
    else:
        done= True
