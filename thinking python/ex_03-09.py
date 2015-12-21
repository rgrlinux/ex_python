import turtle

line_size = 100
wn = turtle.Screen()
t = turtle.Turtle()

for i in range(5):
    t.forward(line_size)
    t.left(-144)

wn.exitonclick()
