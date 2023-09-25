# assignment: programming assignment 1
# author: (Aditya Bhaskar)
# date: (15th October 2020)
# file: hello.py is a program that asks the user to enter user's name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data


y="Hello!"

b=str(y)

x=b+" What is your name? "

name=input(x)

age=input("What is your age? ")

a=int(age)

movie=input("What is your favorite movie? ")                                  

print("Nice to meet you, %s. " % name)                                        

var=f"You are {a} years old and your favorite movie is {movie}."       

print(var)                                                                   
