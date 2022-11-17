import shades
import random

canvas = shades.Canvas(2000, 2000)
ink = shades.NoiseGradient(
    color=(200, 200, 200),
    color_fields=shades.noise_fields(scale=0.0002, channels=3),
    color_variance=70,
    warp_size=800,
    warp_noise=shades.noise_fields(scale=0.002, channels=2),
)


def random_point():
    x = random.randint(-800, canvas.width+800)
    y = random.randint(-800, canvas.height+800)
    return (x, y)

'''
points = [random_point() for i in range(5500)]
for i in range(len(points)-1):
    ink.line(canvas, points[i], points[i+1], 1)
'''
for i in range(5000000):
    ink.point(canvas, random_point())

canvas.show()
