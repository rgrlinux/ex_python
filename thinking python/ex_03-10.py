import turtle
import math

line_size = 150
wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()

t.speed(1)
t.shape('turtle')

t.color('blue')
t.penup()
t.left(90)
t.stamp()
t.right((360/12)/2)
t.forward((line_size * 2 * math.pi)/12)
#t.forward(line_size/2)
t.stamp()
for i in range(9):
    t.stamp()
    t.right(360/12)
    t.forward((line_size * 2 * math.pi)/12)
    
print(t.shapesize())
wn.exitonclick()