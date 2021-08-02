import shades
import random

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    color=(200,200,200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
    warp_size=500,
    warp_noise=[shades.NoiseField(scale=0.01), shades.NoiseField(scale=0.01)])

def random_point():
    x = random.randint(0, canvas.width)
    y = random.randint(0, canvas.height)
    return (x, y)

points = [random_point() for i in range(1000)]
for i in range(len(points)-1):
    ink.line(canvas, points[i], points[i+1], 1)

canvas.show()
