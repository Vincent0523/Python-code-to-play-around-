import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
spin = turtle.Turtle()
spin.speed(0)
spin.width(2)
spin.hideturtle()

# Function to draw a kaleidoscope spiral


def draw_kaleidoscope():
    num_shapes = 120      # Number of iterations
    sides = 6             # Number of symmetry sides
    hue = 0               # Initial color hue

    for i in range(num_shapes):
        spin.penup()
        spin.goto(0, 0)
        spin.pendown()

        # Set heading and color
        spin.setheading(i * 3)  # Spiral rotation
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        spin.pencolor(color)

        # Draw shape
        for _ in range(sides):
            spin.forward(100 + i)  # Increase distance each round
            spin.right(360 / sides)

        # Update color
        hue += 0.005
        if hue > 1:
            hue = 0


# Run it
draw_kaleidoscope()
screen.exitonclick()
