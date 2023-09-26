import turtle

# Create a Turtle screen and set up its properties
screen = turtle.Screen()
screen.title("Square Drawing")
screen.bgcolor("white")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the speed of the turtle (1 is the slowest)

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move the turtle forward by 100 units
    pen.right(90)  # Turn the turtle 90 degrees to the right

# Exit the program when the user clicks on the screen
screen.exitonclick()