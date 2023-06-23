'''
Prompt: TASK: Write a program snowflake.py that generates the famous fractal
        Koch snowflake Koch snowflake - Wikipedia. (Links to an external site.)
        You need to use recursion and the turtle.
'''

import turtle

def snowflake(a, order):
    if order > 0:
        for i in [60, -120, 60, 0]:
            #recursive call
            snowflake(a / 3, order - 1)
            t.left(i)
    else:
        t.forward(a)

if __name__ == '__main__':
    
    # turtle setup
    s = turtle.Screen()
    s.setup(500, 500)
    s.bgcolor("ivory4")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("classic")
    t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=1, speed=0)

    # loop to make snowflake
    for j in range(3):
        # function : snowflake(size of side = a, order)
        snowflake(100, 6)
        t.right(120)
