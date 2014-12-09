import turtle

def drawPoly(turtle, sides, size):
    """Get a turtle to draw a polygon with given sides and size"""
    angle = 360 / sides
    
    for i in range(sides):
        turtle.forward(size)
        turtle.left(angle)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    tess = turtle.Turtle()
    tess.color("red")
    
    drawPoly(tess, 8, 50)
    
    wn.exitonclick()
    
main()
