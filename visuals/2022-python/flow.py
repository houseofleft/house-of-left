import shades
import random

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    color=(200, 200, 200),
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)],
    noise_fields=noise_fields(scale=0.06, limit=2000, buffer=1000, channels=3),
    color_variance=70,
    warp_size=800,
    warp_noise=noise_fields(scale=0.5, limit=2000, buffer=1000, channels=2),
)


def random_point():
    x = random.randint(-800, canvas.width+800)
    y = random.randint(-800, canvas.height+800)
    return (x, y)


points = [random_point() for i in range(5000)]
for i in range(len(points)-1):
    ink.line(canvas, points[i], points[i+1], 1)

canvas.show()
