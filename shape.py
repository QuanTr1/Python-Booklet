import turtle
wn = turtle. Screen()
tom = turtle. Turtle()
def square(length):
    for a in range (4):
        tom. forward (length)
        tom. right (90)
    wn . exitonclick()
    
def triangle(length):
    for a in range(3):
        tom.forward(length)
        tom.right(180-60)
    wn . exitonclick()
def hexagon(length):
    for a in range(6):
        tom.forward(length)
        tom.right(180-120)
    wn . exitonclick()
    
def octagon(length):
    for a in range(8):
        tom.forward(length)
        tom.right(180-135)
    wn . exitonclick()
        
size = int(input("Enter the length of the shape "))
#octagon(size)
hexagon(size)