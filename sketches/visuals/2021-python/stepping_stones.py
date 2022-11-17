import shades
import random

canvas = shades.Canvas(2000, 2000, (240, 240, 240))
underlay = shades.BlockColor((230, 230, 230))
highlight = shades.BlockColor()
highlight_colors = [(244, 131, 166), (128, 199, 242), (213, 205, 209)]
highlight_weights = [1, 10, 10]
underlay = shades.BlockColor((220, 220, 220))
line = shades.BlockColor((220, 220, 220), transparency=1)

grid_size = 100
grid_points = []

for x in range(0, canvas.width, int(grid_size)):
    for y in range(0, canvas.height, int(grid_size)):
        if random.random() > 0.5:
            underlay.circle(canvas, (x, y), 3)
        else:
            underlay.line(canvas, (x - 5, y - 5), (x + 5, y + 5), 2)
            underlay.line(canvas, (x - 5, y + 5), (x + 5, y - 5), 2)


def random_point():
    x_grid_lr = int(canvas.width / grid_size / 4)
    x_grid_ur = x_grid_lr * 2
    y_grid_lr = int(canvas.height / grid_size / 4)
    y_grid_ur = y_grid_lr * 2
    x = grid_size * random.randint(x_grid_lr, x_grid_ur)
    y = grid_size * random.randint(y_grid_lr, y_grid_ur)
    return [x, y]


for i in range(10):

    point = random_point()

    while (point[0] < canvas.width) and (point[0] > 0) and (point[1] < canvas.height) and (point[1] > 0):

        last_point = point.copy()
        movement = random.randint(-int((canvas.width / grid_size / 2)),
                                  int((canvas.width / grid_size / 2)))
        axis = random.choice([0, 1])

        point[axis] += movement * grid_size

        if movement != 0:
            line.line(canvas, last_point, point, 2)
            highlight.color = random.choices(
                highlight_colors, weights=highlight_weights, k=1
            )[0]
            highlight.circle(canvas, point, 10)
            highlight.color = random.choices(
                highlight_colors, weights=highlight_weights, k=1
            )[0]
            highlight.circle(canvas, last_point, 10)


canvas.show()
