import turtle

def draw_star(t, size):
    t.pendown()
    t.begin_fill()
    angle = 360
    while angle > 0:
        for i in range(5):
            t.forward(size);
            t.left(angle);
        t.end_fill()
        angle -= 5

def draw_star_rec(t, size):
    t.pendown()
    return draw_star_rec()

s = turtle.Screen()
s.setup(500, 500)
s.bgcolor("ivory4")
s.title("Turtle Program")

t = turtle.Turtle()
t.shape("classic")
t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=1)

t.penup()
t.goto(0,0)
t.color('red')
draw_star(t, 50)
