import shades
from random import randint

def nearby_point(point, distance):
    x = point[0] + randint(-distance, distance)
    y = point[1] + randint(-distance, distance)
    while shades.distance_between_points(point, (x, y)) > distance:
        x = point[0] + randint(-distance, distance)
        y = point[1] + randint(-distance, distance)
    return (x, y)

canvas = shades.Canvas(4000, 4000)
background_shade = shades.BlockColor((240,240,240))
foreground = shades.BlockColor()
gradient = shades.NoiseGradient(
    color=(200,200,200),
    color_variance=70,
    noise_fields = [shades.NoiseField(scale=0.0002) for i in range(3)],
)

steps = 20
walk_distance = 50
wackiness = 300
color_distance = 1000

for i in range(15):
    foreground.noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)]
    for i in range(1+4, steps-1):
        y = i / steps * canvas.height
        start = (0, y)
        end = (canvas.width, y)
        last_point = start
        foreground.color = gradient.determine_shade(nearby_point(start, color_distance))
        while last_point[0] < end[0]:
            point = (last_point[0] + walk_distance, y)
            point = nearby_point(point, wackiness)
            while shades.distance_between_points(point, last_point) < 1:
                point = nearby_point(point, wackiness)
            foreground.line(canvas, last_point, point)
            last_point = point
        if shades.distance_between_points(last_point, end) > 1:
            foreground.line(canvas, last_point, end, 6)

background_shade.rectangle(canvas, (0, 0), 100, canvas.height)
background_shade.rectangle(canvas, (canvas.width-100, 0), 100, canvas.height)

canvas.show()
