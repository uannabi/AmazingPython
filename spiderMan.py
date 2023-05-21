
import turtle

def draw_spiderman():
    turtle.bgcolor("black")
    turtle.speed(2)  # Set the speed to a moderate value
    turtle.color("red")
    turtle.begin_fill()

    # Draw Spider-Man's head
    turtle.circle(100)

    turtle.end_fill()

    # Draw Spider-Man's eyes
    turtle.color("white")
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(-40, 120)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(40, 120)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw Spider-Man's web pattern on the head
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.setheading(60)

    for _ in range(6):
        turtle.forward(200)
        turtle.backward(200)
        turtle.right(60)

    turtle.hideturtle()

# Create a turtle screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=800, height=600)
screen.title("Spider-Man")

# Draw Spider-Man
draw_spiderman()

# Exit on click
turtle.exitonclick()

