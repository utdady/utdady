done= False

while not done:
    word= input("Please, enter a palindrome:")
    drow= word[::-1]

    if drow==word:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")
    yesno=input("Would you like to play again[Y/N]?")
    if yesno=='Y' or yesno=='y':
        done= False
    else:
        done= True
        print("Goodbye!")
