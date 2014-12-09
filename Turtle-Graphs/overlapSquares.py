import turtle

def drawSquare(t, sz):
    """Get a turtle 't' to draw a square with size 'sz'"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
def drawMultipleSquare(t, num):
    """Get a turtle to draw multiple squares with the same center"""
    size = 20
    
    for i in range(num):
        drawSquare(t, size)
        t.up()
        xNew = t.xcor() - 10
        yNew = t.ycor() - 10
        t.goto(xNew, yNew)
        t.down()
        size += 20
        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    alex = turtle.Turtle()
    alex.color("red")

    drawMultipleSquare(alex,5)

    wn.exitonclick()
    
main()
