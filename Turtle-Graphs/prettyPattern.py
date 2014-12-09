import turtle

def drawSquare(t):
    # Get a turtle to draw a square with size 100
    for i in range(4):
        t.forward(100)
        t.left(90)
        
def draw4Square(t):
    # Get a turtle to draw 4 small squares
    for i in range(4):
        drawSquare(t)
        t.right(90)
        
def drawMultipleSquare(t):
    # Get a turtle to draw many squares
    for i in range(5):
        draw4Square(t)
        t.left(18)
               
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    alex = turtle.Turtle()
    alex.color("red")
    
    drawMultipleSquare(alex)
    
    wn.exitonclick()
    
main()
