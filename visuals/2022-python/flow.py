import shades
import random

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    color=(150, 150, 150),
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)],
    color_variance=70,
    warp_size=800,
    warp_noise=[shades.NoiseField(scale=0.005), shades.NoiseField(scale=0.005)],
)


def random_point():
    x = random.randint(-800, canvas.width+800)
    y = random.randint(-800, canvas.height+800)
    return (x, y)


points = [random_point() for i in range(5000)]
for i in range(len(points)-1):
    ink.line(canvas, points[i], points[i+1], 1)

canvas.show()
