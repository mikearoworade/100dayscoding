from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('red')

for _ in range(4):
    tim.forward(100)
    tim.left(90)


# To let the window start and only exit when clicked on
screen =  Screen()
screen.exitonclick()
