import turtle

def drawSpiral(t, angle):
    # Get a turtle to draw spiral using given angle
    size = 2
    t.right(90)
    
    for i in range(100):
        t.forward(size)
        t.right(angle)
        size += 2
        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    alex = turtle.Turtle()
    alex.color("blue")
    
    drawSpiral(alex, 89)
    
    wn.exitonclick()
    
main()
