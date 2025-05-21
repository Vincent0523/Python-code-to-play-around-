import turtle
import colorsys
import numpy as np
import pyaudio

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Sound-Reactive Spiral Art")
artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.hideturtle()

# Audio stream setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Function to get microphone volume


def get_volume():
    data = np.frombuffer(stream.read(
        CHUNK, exception_on_overflow=False), dtype=np.int16)
    rms = np.sqrt(np.mean(np.square(data)))
    return min(rms / 1000, 1.0)  # Normalize to [0, 1]

# Draw spiral based on volume


def draw_spiral(volume):
    artist.clear()
    hue = 0
    spiral_scale = 80 + volume * 100  # Bigger if louder
    sides = int(5 + volume * 5)       # More sides if louder
    angle_step = 3 + volume * 5

    for i in range(120):
        artist.penup()
        artist.goto(0, 0)
        artist.pendown()
        artist.setheading(i * angle_step)

        color = colorsys.hsv_to_rgb(hue, 1, 1)
        artist.pencolor(color)

        for _ in range(sides):
            artist.forward(spiral_scale + i)
            artist.right(360 / sides)

        hue += 0.01
        if hue > 1:
            hue = 0


# Main loop
try:
    while True:
        vol = get_volume()
        draw_spiral(vol)

except KeyboardInterrupt:
    print("Exiting...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    turtle.bye()
