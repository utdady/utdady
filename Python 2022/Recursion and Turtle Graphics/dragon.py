'''
Prompt: TASK: Write a program dragon.py that generates the famous fractal
        Dragon curve Dragon curve - Wikipedia (Links to an external site.).
        You need to use recursion and the turtle.
'''

import turtle

# L-system set up
START = "fx"
RULES = {'x':'x+yf+', 'y':'-fx-y', 'f':'f', '+':'+', '-':'-'}

LEVEL = 13

# turtle setup
s = turtle.Screen()
s.setup(500, 500)
s.bgcolor("ivory4")
t = turtle.Turtle()
t.pen(pencolor='blue', speed=0)

sub_string = string = START

for _ in range(LEVEL):

    # apply the RULES from text to graphics
    for character in sub_string:
        if character == '+':
            t.right(90)
        elif character == '-':
            t.left(90)
        elif character == 'f':
            t.forward(5)

    # make a new generation of the L-system
    full_string = "".join(RULES[character] for character in string)
    sub_string = full_string[len(string):]  # only the new information
    string = full_string  # the complete string for the next generation

