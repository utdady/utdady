'''
Prompt: TASK: Write a program turtle_race.py that improves the Turtle Race game
        by adding features such as showing a time and the winner of the race and
        buttons to restart the race.
'''

# turtle race
from turtle import *
from random import randint
import turtle
import time

def set_turtles(colors):
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed(1)
        turtles.append(t)
    return turtles

def draw_track(start, finish):
    t = Turtle()
    t.speed(0)
    position, size, step = 100, 200, 40
    count = 0
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line,position+10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START")
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH")
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count)
        t.goto(line,position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)
    
def isfinish(t, finish):
    x, y = t.pos()
    if x < finish:
        return False
    else:
        return True

def race(turtles, start, finish):
    # y position
    position = 80
    distance = 40
    for t in turtles:
        t.penup()
        t.left(180)
        t.goto(start, position)
        position -= distance
        t.left(180)
        t.pendown()
    
    done = False
    times = turtle.Turtle()
    timer = turtle.Turtle()
    winner = turtle.Turtle()
    timer.hideturtle()
    times.hideturtle()
    winner.hideturtle()
    winner.penup()
    timer.penup()
    times.penup()
    winner.goto(-210,150)
    times.goto(0, -150)
    timer.goto(100, -150)
    timer.pendown()
    times.pendown()
    winner.pendown()
    times.write("Timer: ", font=("Courier", 20))
    start = time.time()
    while not done:
        timer.clear()
        timer.write(round((time.time() - start), 1), font=("Courier", 20))
        for t in turtles:
            t.forward(randint(1,10))
            if isfinish(t, finish):
                winner.write(f"{t.color()[0]} turtle is the winner!", font=('Courier', 20))
                done = True
    s.delay(10)

    button = turtle.Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('pink')
    button.penup()
    button.goto(-130, -130)
    button.write("Click here to restart!", align='center', font=('Courier', 8))
    button.sety(-140)
    button.onclick(restart)
    button.showturtle()
    s.delay(5)
    timer.clear()
    winner.clear()

def restart(x, y):
    race(turtles, start, finish)

if __name__ == '__main__':
    
    # main program
    s = Screen()  # make a canvas window
    s.setup(500, 400)
    s.bgcolor("white")
    s.title("Turtle Race")
    start = -200  # x position
    finish = 200  # x position

    draw_track(start, finish)
    turtles = set_turtles(["red", "yellow", "green", "cyan", "blue"])
    race(turtles, start, finish)
