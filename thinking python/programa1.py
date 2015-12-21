import turtle

bgcolor = input("informa a cor do fundo: ")
turtle_color = input("informe a cor da tartaruga: ")
pen_width = int(input('informe a espessura do traco: '))

altura = 50
largura = 120
angulo = 90
wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor(bgcolor)
t.color(turtle_color)
t.pensize(pen_width)

t.forward(largura)
t.left(angulo)
t.forward(altura)
t.left(angulo)
t.forward(largura)
t.left(angulo)
t.forward(altura)
wn.exitonclick()
