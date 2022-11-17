import shades
from random import randint, choice, choices

def random_point(margin):
    x = randint(margin, canvas.width-margin)
    y = randint(margin, canvas.height-margin)
    return (x, y)

def nearby_point(point, distance):
    x = point[0] + randint(-distance, distance)
    y = point[1] + randint(-distance, distance)
    return (x, y)

canvas = shades.Canvas()
circles = []
shade = shades.BlockColor()
gradient = shades.NoiseGradient(
    color_variance=50,
    noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)],
)
colors = [(254, 208, 16), (21, 157, 73), (68, 76, 159)]
color_weights = [10, 4, 1]

for i in range(50000):
    radius = randint(5, 7)
    point = random_point(radius)
    if not any([c for c in circles if shades.distance_between_points(c[0], point) <= radius + c[1] + 3]):
        gradient.color = choices(colors, weights=color_weights)[0]
        color = gradient.determine_shade(nearby_point(point, 300))
        shade.color = color
        shade.circle(canvas, point, radius)
        circles.append((point, radius))

canvas.show()
