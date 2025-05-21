import turtle
import math
import colorsys
import numpy as np
import pyaudio

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("💖 Romantic Heart - Music Reactive 💖")

# Setup turtle
heart = turtle.Turtle()
heart.speed(0)
heart.hideturtle()
heart.pensize(2)

# Setup audio input
CHUNK = 1024
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Get microphone volume


def get_volume():
    data = np.frombuffer(stream.read(
        CHUNK, exception_on_overflow=False), dtype=np.int16)
    rms = np.sqrt(np.mean(np.square(data)))
    return min(rms / 800, 1.0)  # Normalize volume

# Draw romantic heart shape with glowing effect


def draw_heart(size, glow_intensity):
    heart.clear()
    heart.penup()
    heart.goto(0, -size * 1.5)
    heart.pendown()

    hue = glow_intensity * 0.8
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    heart.pencolor((r, g, b))
    heart.fillcolor((r * 0.5 + 0.5, g * 0.2, b * 0.5 + 0.5))
    heart.begin_fill()

    for t in range(0, 360, 1):
        angle = math.radians(t)
        x = size * 16 * math.sin(angle)**3
        y = size * (13 * math.cos(angle) - 5 * math.cos(2 * angle) -
                    2 * math.cos(3 * angle) - math.cos(4 * angle))
        if t == 0:
            heart.penup()
        else:
            heart.pendown()
        heart.goto(x, y)

    heart.end_fill()


# Main loop: React to romantic music
try:
    while True:
        volume = get_volume()
        size = 10 + volume * 10         # Heart grows with sound
        glow = volume                   # Controls color glow
        draw_heart(size, glow)

except KeyboardInterrupt:
    print("Stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    turtle.bye()
