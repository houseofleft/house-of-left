import shades
import random

canvas = shades.Canvas(1300, 1300)
ink = shades.BlockColor(
    warp_size=500,
    warp_noise=[shades.NoiseField(scale=0.01) for i in range(2)],
)
colors = [
    (193, 246, 218),
    (249, 220, 220),
    (242, 250, 251),
    (207, 229, 244),
    (249, 222, 238),
]


def random_point():
    x = random.randint(0, canvas.width)
    y = random.randint(0, canvas.height)
    return (x, y)


for i in range(9000):
    ink.color = random.choice(colors)
    point = random_point()
    shift = (
        point[0] + random.randint(-1000, 1000),
        point[1] + random.randint(-1000, 1000),
    )
    ink.line(canvas, point, shift, 3)


canvas.show()
