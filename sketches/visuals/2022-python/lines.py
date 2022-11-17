import shades
import random
from handy_stuff import palletes

canvas = shades.Canvas(height=2000, width=2000)
transparency = random.uniform(0.4, 0.9)
pallete = random.choice(palletes)
inks = [shades.BlockColor(i, transparency=0.6) for i in pallete]


def draw_rect_with_lines(shade, canvas, topcorner, height, width):
    offset_1 = random.randint(0, 500)
    offset_2 = random.randint(0, 500)
    if random.random() < 0.5:
        for x in range(topcorner[0], topcorner[0] + width, 5):
            shade.line(
                canvas,
                (x + offset_1, topcorner[1]),
                (x + offset_2, topcorner[1] + height),
                1,
            )
    else:
        for y in range(topcorner[1], topcorner[1] + height, 5):
            shade.line(
                canvas,
                (topcorner[0], y + offset_1),
                (topcorner[0] + width, y + offset_2),
                1,
            )


def random_point(canvas, buffer):
    x = random.randint(-buffer, canvas.width)
    y = random.randint(-buffer, canvas.height)
    return (x, y)


for i in range(100):
    draw_rect_with_lines(
        random.choice(inks),
        canvas,
        random_point(canvas, canvas.width),
        random.randint(1000, canvas.width),
        random.randint(1000, canvas.height),
    )

canvas.show()
