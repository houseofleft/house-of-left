import shades
from random import randint

def random_point():
    x = randint(0, canvas.width)
    y = randint(0, canvas.height)
    return (x, y)

def nearby_point(point):
    x = point[0] + randint(-300, 300)
    y = point[1] + randint(-300, 300)
    return (x, y)

canvas = shades.Canvas(1000, 1000)
shade = shades.BlockColor()
gradient = shades.NoiseGradient(
    color=(200,200,200),
    color_variance=70,
)

for i in range(2):
    x_offset = randint(-50, 50)
    y_offset = randint(-50, 50)
    gradient.noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)]
    points = [random_point() for i in range(500000)]
    for point in points:
        color = gradient.determine_shade(nearby_point(point))
        shade.color = color
        shade.point(canvas, (point[0] + x_offset, point[1] + y_offset))

canvas.show()
