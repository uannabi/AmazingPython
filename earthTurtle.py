import turtle

def draw_earth():
    turtle.bgcolor("black")
    turtle.speed(0)  # Set the speed to the fastest
    turtle.color("green")
    turtle.begin_fill()

    for _ in range(180):
        turtle.forward(1)
        turtle.left(1)

    turtle.end_fill()

    turtle.color("blue")
    turtle.begin_fill()

    for _ in range(180):
        turtle.forward(1)
        turtle.right(1)

    turtle.end_fill()

    turtle.hideturtle()

# Create a turtle screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=800, height=600)
screen.title("Earth")

# Draw the Earth
draw_earth()

# Exit on click
turtle.exitonclick()

