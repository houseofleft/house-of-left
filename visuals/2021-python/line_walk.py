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
foreground = shades.BlockColor(
    color=(41,104,136),
    warp_size=50,
    warp_noise=[shades.NoiseField(scale=0.02), shades.NoiseField(scale=0.001)],
)
steps = 25
walk_distance = 10
wackiness = 50


for i in range(1, steps):
    y = i / steps * canvas.height
    start = (0, y)
    end = (canvas.width, y)
    last_point = start
    while last_point[0] < end[0]:
        point = (last_point[0] + walk_distance, y)
        point = nearby_point(point, wackiness)
        while shades.distance_between_points(point, last_point) < 1:
            point = nearby_point(point, wackiness)
        foreground.line(canvas, last_point, point)
        last_point = point
    if shades.distance_between_points(last_point, end) > 1:
        foreground.line(canvas, last_point, end, 4)

background_shade.rectangle(canvas, (0, 0), 100, canvas.height)
background_shade.rectangle(canvas, (canvas.width-100, 0), 100, canvas.height)

canvas.show()
