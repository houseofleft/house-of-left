import shades
from random import randint

def random_point():
    x = randint(0, canvas.width)
    y = randint(0, canvas.height)
    return (x, y)

def nearby_point(point, distance):
    x = point[0] + randint(-distance, distance)
    y = point[1] + randint(-distance, distance)
    while shades.distance_between_points(point, (x, y)) > distance:
        x = point[0] + randint(-distance, distance)
        y = point[1] + randint(-distance, distance)
    return (x, y)

def blueish():
    blue = (87, 141, 209)
    blueish = [i + randint(-20, 20) for i in blue]
    return tuple(blueish)

canvas = shades.Canvas(1000, 1000)
shade = shades.BlockColor(
    color=(87, 141, 209),
    transparency=0.95,
    warp_size=20,
    warp_noise=[shades.NoiseField(scale=0.002) for i in range(2)]
)
center = (int(canvas.width/2), int(canvas.height/2))

for i in range(15):
    off_center = nearby_point(center, 100)
    shade.circle(canvas, off_center, 300)

canvas.show()
