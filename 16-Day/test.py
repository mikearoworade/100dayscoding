from turtle import Turtle, Screen

# Object timmy created with Turtle class
timmy = Turtle()

print(timmy)
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)

my_screen = Screen()

# Accessing Object attribute
print(my_screen.canvheight)

# Object method - Keep screen running until clicked on screen
my_screen.exitonclick()
