# turtle code 

import turtle


# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
my_turtle = turtle.Turtle()

# Define the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set the turtle properties
my_turtle.width(3)
my_turtle.speed(2)

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-200, 0)
my_turtle.pendown()

# Draw "Hello World" with multiple colors
for char in "Hello World":
    # Set the color
    color = colors.pop(0)
    my_turtle.color(color)

    # Write the character
    my_turtle.write(char, font=("Arial", 24, "bold"))

    # Move the turtle forward
    my_turtle.forward(50)

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()

