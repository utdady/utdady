# Assignment: Programming Assignment 1 (PA1)
# Author: Aditya Bhaskar
# Date: 11th October 2020
# File: finalhello.py is a program that asks the user to enter user’s name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user.
# input: string data
# output: string data

x=int()                                                                      # Use of Integer casting

y=str("Hello! What is your name?")                                           # Use of String Casing.

name=input(y)                                                                # Variable Declaration and Input Function for Name of the user.

x=input("What is your age?")                                                 # Variable Declaration and Input Function for Age of the user.

movie=input("What is your favourite movie?")                                 # Variable Declaration and Input Function for favourite movie of user.

print("Nice to meet you, %s." % name)                                         # Use of String Formatting.

var="You are %s years old and your favourite movie is %s." % (x, movie)      # Use of String Formatting and Variable Declaration.

print(var)                                                                   # Use of String Concatenation.
