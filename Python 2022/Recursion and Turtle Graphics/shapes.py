'''
Prompt: TASK: Write a program named shapes.py that has two functions for
        generating convex and star regular polygons. Each function should be
        implemented by using iteration (a for loop) and recursion. It is
        optional to fill in your shapes. The function for generating polygons
        can be named polygon(size, n) and the function that generates stars can
        be named star(size, n), where size is the size of the polygon side (edge
        and n is the number of sides (or angles).
'''

import turtle
from turtle import mainloop

# polygon recursive
def polygonREC(size, n):
    t.pendown()
    if n > 0:
        angle = 360 / n
        t.forward(size)
        t.left(angle)
        n += 1
        polygon(size, n - 1)

# polygon iterative
def polygon(size, n):
    t.pendown()
    angle = 360 / n
    for i in range(n):
        t.forward(size)
        t.left(angle)

# star recursive
def starREC(size, n):
    t.pendown()
    if n > 0:
        l = 360 / n
        r = l * 2
        t.forward(size)
        t.left(l)
        t.forward(size)
        t.right(r)
        n += 1
        starREC(size, n - 1)

# star iterative
def star(size, n):
    l = 360/ n
    r = l * 2
    t.pendown()
    for i in range(n):
        t.forward(size)
        t.right(r)
        t.forward(size)
        t.left(l)


if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(750, 750)
    s.bgcolor("ivory4")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("classic")
    t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=1)
    t.hideturtle()
    
    t.penup()
    t.goto(-220,250)
    star(50, 7)

    t.penup()
    t.goto(-220, -250)
    polygonREC(50, 7)

    t.penup()
    t.goto(220,-250)
    polygon(50, 7)

    t.penup()
    t.goto(150,168)
    starREC(50, 7)
