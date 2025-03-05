from turtle import Turtle, Screen, colormode
import random

tim = Turtle()


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    r_color = (r, g, b)
    return r_color


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()

