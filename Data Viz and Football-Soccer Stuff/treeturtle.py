# draws a tree
import turtle

# set the canvas window
def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

# set a turtle (a pen)
def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=10)
    return t

# draw a tree fractal using recursion
def draw_tree(t, branch, angle, n):
  if n > 0: # recursive step
        t.color('brown')
        t.pensize(n)
        t.forward(branch)
        length = branch * 9/10
        t.left(angle)
        draw_tree(t, length, angle, n-1) # recursive call (left branch of the tree)
        t.color('brown')
        t.right(angle * 2)
        t.pensize(n)
        t.forward(branch/10)
        draw_tree(t, length, angle, n-1) # recursive call (right branch of the tree)
        t.color('brown')
        t.left(angle)
        t.backward(branch*11/10)
  else: # base case
        t.color('green')
        t.pendown()
        t.dot(15)

# main program
s = set_canvas()
t = set_pen('brown')
t.penup()
t.goto(-45, -150)
t.left(90)
t.pendown()
draw_tree(t, 60, 20, 6)
