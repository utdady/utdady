# assignment: programming assignment 3
# author: (Aditya Bhaskar)
# date: (8th November 2020)
# file: calculator.py is a program that (type the description of the program)
# input: (numbers as string)
# output: (numbers in float)

def add (x, y):
    a= float(x)
    b= float(y)
    num= a+b
    k= format_num(num)
    return k

    
def subtract (x, y):
    a= float(x)
    b= float(y)
    num= a-b
    k= format_num(num)
    return k
    
def multiply (x, y):
    a= float(x)
    b= float(y)
    num= a*b
    k= format_num(num)
    return k
    
def divide (x, y):
    a= float(x)
    b= float(y)
    num= a/b
    k= format_num(num)
    return k

def format_num (num, precision= 2):
    a= round(num, precision)
    return a

def isfloat (token) :
    dot = False
    minus = False
    for char in token :
        if char.isdigit() :  # allow many digits in a string
            continue
        elif char == "." :   # allow only one dot in a string
            if not dot :
                dot = True
            else :                                   
                return False
        elif char == "-" and token[0] == "-": # allow one minus in front
            if not minus :
                minus = True
            else :
                return False
        else :               # do not allow any other characters in a string
            return False
    return True


def main():
    pts= False
    print("Welcome to the Calculator Program!")

    while not pts:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Please choose one of the following operations:\nAddition - A\nSubtraction - S\nDivision - D\nMultiplication - M")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        op= input("Enter your choice: ")
        if op=="A" or op=="a":
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("You chose addition.")
            num1= input("\nPlease enter the first number: ")
            NUM1= isfloat(num1)
            if not NUM1:
                pt= False
                while not pt:
                    num1= input("You did not choose a number.\nPlease enter the first number: ")
                    nums= isfloat(num1)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The first number is {num1}.")
            num2= input("\nPlease enter the second number: ")
            NUM2= isfloat(num2)
            if not NUM2:
                pt= False
                while not pt:
                    num2= input("You did not choose a number.\nPlease enter the second number: ")
                    nums= isfloat(num2)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The second number is {num2}.")
            ab=add (num1, num2)
            print(f"\n{num1} + {num2} = {ab}")
            print("++++++++++++++++++++++++++++++++++++++++++++++")
        elif op=="S" or op=="s":
            print("----------------------------------------------")
            print("You chose subtraction.")
            num1= input("\nPlease enter the first number: ")
            NUM1= isfloat(num1)
            if not NUM1:
                pt= False
                while not pt:
                    num1= input("You did not choose a number.\nPlease enter the first number: ")
                    nums= isfloat(num1)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The first number is {num1}.")
            num2= input("\nPlease enter the second number: ")
            NUM2= isfloat(num2)
            if not NUM2:
                pt= False
                while not pt:
                    num2= input("You did not choose a number.\nPlease enter the second number: ")
                    nums= isfloat(num2)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The second number is {num2}.")
            ab=subtract(num1, num2)
            print(f"\n{num1} - {num2} = {ab}")
            print("----------------------------------------------")
        elif op=="D" or op=="d":
            print("//////////////////////////////////////////////")
            print("You chose division.")
            num1= input("\nPlease enter the first number: ")
            NUM1= isfloat(num1)
            if not NUM1:
                pt= False
                while not pt:
                    num1= input("You did not choose a number.\nPlease enter the first number: ")
                    nums= isfloat(num1)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The first number is {num1}.")
            num2= input("\nPlease enter the second number: ")
            if num2=="0":
                done= False
                while not done:
                    print("The division by zero is prohibited!") 
                    num2= input("Please enter the second number: ")
                    if num2=="0":
                        done= False
                    else:
                        done= True
            NUM2= isfloat(num2)
            if not NUM2:
                pt= False
                while not pt:
                    num2= input("You did not choose a number.\nPlease enter the second number: ")
                    nums= isfloat(num2)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The second number is {num2}.")            
            ab=divide(num1, num2)
            print(f"\n{num1} / {num2} = {ab}")
            print("//////////////////////////////////////////////")
        elif op=="M" or op=="m":
            print("**********************************************")
            print("You chose multiplication.")
            num1= input("\nPlease enter the first number: ")
            NUM1= isfloat(num1)
            if not NUM1:
                pt= False
                while not pt:
                    num1= input("You did not choose a number.\nPlease enter the first number: ")
                    nums= isfloat(num1)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The first number is {num1}.")
            num2= input("\nPlease enter the second number: ")
            NUM2= isfloat(num2)
            if not NUM2:
                pt= False
                while not pt:
                    num2= input("You did not choose a number.\nPlease enter the second number: ")
                    nums= isfloat(num2)
                    if not nums:
                        pt= False
                    else:
                        pt= True
            print(f"The second number is {num2}.")
            ab=multiply(num1, num2)
            print(f"\n{num1} x {num2} = {ab}")
            print("**********************************************")
        else:
            print("\nWrong Input!")
        yes= input("Do you want to continue [Y/N]: ")
        if yes=="Y" or yes=="y":
            pts= False
        else:
            print("\nGoodbye!")
            pts= True
main()
