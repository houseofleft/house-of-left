import shades
import random

canvas = shades.Canvas(600, 600)
ink = shades.BlockColor()

colors = [
    (172, 205, 213),
    (70, 70, 70),
    (44, 39, 0),
    (188, 61, 17),
    (250, 233, 122),
]

segments_x = 6
segments_y = 6

x_step = int(canvas.width / segments_x)
y_step = int(canvas.height / segments_y)


# what if we iterate through, placing a bunch of rectangles around?
ink.color = random.choice(colors)
ink.rectangle(
    canvas,
    (x_step, y_step),
    canvas.width - x_step * 2,
    canvas.height - y_step * 2,
)

for i in range(12):
    y = random.choice(range(y_step, canvas.height - y_step * 2, y_step))
    x = random.choice(range(x_step, canvas.width - x_step * 2, x_step))

    # width between x_step, and however many x_steps to get to end
    max_width = (canvas.width - x_step - x)
    width = random.choice(range(x_step, max_width, x_step))

    max_height = (canvas.width - y_step - y)
    height = random.choice(range(y_step, max_height, y_step))

    ink.color = random.choice(colors)
    ink.rectangle(canvas, (x, y), width, height)


canvas.show()

