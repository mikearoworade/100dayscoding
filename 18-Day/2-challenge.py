from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('red')

for _ in range(14):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# To let the window start and only exit when clicked on
screen =  Screen()
screen.exitonclick()
