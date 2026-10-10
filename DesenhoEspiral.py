import turtle
import random
turtle.Screen()
turtle.colormode(255)
Geoforma=turtle.Turtle()
Geoforma.speed(3)
Geoforma.hideturtle()
lados = random.randint(1, 10)

linhas = 1

for i in range(10000):
    Geoforma.forward(linhas)
    Geoforma.right(360/lados)
    linhas = linhas + 3
    Geoforma.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

turtle.exitonclick()