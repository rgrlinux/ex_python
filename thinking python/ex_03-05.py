import turtle

line_size = 120
wn = turtle.Screen()
t = turtle.Turtle()
int_faces = 3
t.penup()
t.goto(-700,100)
t.pendown()

for l in (3,4,6,8):
    for i in range(l):
        t.forward(line_size)
        t.left(360/l)
    t.penup()
    t.forward(line_size * 2.5)
    t.pendown()        


wn.exitonclick()