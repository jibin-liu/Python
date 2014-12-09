import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawMultipleSquare(t, sz, num):
    """Get turtle t to draw multiple squares"""
    
    for i in range(num):
        drawSquare(t, sz)
        t.up()
        t.forward(sz + 20)
        t.down()

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")

    drawMultipleSquare(alex,20, 4)

    wn.exitonclick()
    
main()
