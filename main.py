import another_module

print(another_module.another_variable)

# import turtle
# Instead write
from turtle import Turtle, Screen
# Read the documentation 'turtle graphics documentation' to see all the methods, attributes etc.

# turtleOne = turtle.Turtle()
# We've used a class Turtle from turtle.
# Instead write
turtleOne = Turtle()
print(turtleOne)
turtleOne.shape("turtle")
turtleOne.color("green")
# the methods will have a 'M' next to it on the dropdown menu when you're typing

my_screen = Screen()
print(my_screen.canvheight)
# The same as JS^, you're selecting a specific attribute from the object.

# We can call a function that an object has. e.g. car.stop()
my_screen.exitonclick()