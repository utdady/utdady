import turtle

def tree(l):
    if l > 0:
        t.forward(l)
        t.right(20)
        tree(l - 15)    # recursive call
        t.left(40)
        tree(l - 15)    # recursive call
        t.right(20)
        t.backward(l)

if __name__ == '__main__':
    # turtle setup
    s = turtle.Screen()
    s.setup(500, 500)
    s.bgcolor("ivory4")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("classic")
    t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=1)

    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(100)   # calling tree
