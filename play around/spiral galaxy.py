import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
galaxy = turtle.Turtle()
galaxy.speed(0)
galaxy.pensize(2)
galaxy.hideturtle()

# Function to draw a colorful spiral pattern


def draw_spiral_galaxy(arms=5, turns=360):
    num_colors = 100
    hue = 0

    for j in range(arms):  # Multiple spirals
        galaxy.penup()
        galaxy.goto(0, 0)
        galaxy.setheading(j * (360 / arms))  # Spread out arms

        for i in range(turns):
            galaxy.pendown()
            rgb = colorsys.hsv_to_rgb(hue, 1, 1)
            galaxy.pencolor(rgb)
            galaxy.forward(i * 0.3)
            galaxy.right(59)
            hue += 1 / num_colors
            if hue > 1:
                hue = 0


draw_spiral_galaxy(arms=7, turns=180)

# Exit on click
screen.exitonclick()
