import turtle

line_size = 100
wn = turtle.Screen()
t = turtle.Turtle()

for i in (160,-43,270,-97,-43,200,-940,17,86):
    t.forward(line_size)
    t.left(i)
print('Direção atual', t.heading(),'º')
wn.exitonclick()
