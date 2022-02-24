import shades
import random

canvas = shades.Canvas(1000, 1000)
ink = shades.BlockColor()

margin = 0
grid_size = 200

colors = [
    (13, 59, 102),
    (250, 240, 202),
    (244, 211, 94),
    (238, 150, 75),
    (249, 87, 56),
]

def quarter_circle(x, y):
    # draw background
    ink.color = random.choice(colors)
    ink.rectangle(canvas, (x, y), grid_size, grid_size)
    ink.color = random.choice(colors)
    placement = random.choice(['top_left', 'bottom_left', 'top_right', 'bottom_left'])
    if placement == 'top_left':
        ink.pizza_slice(canvas, (x, y), grid_size, 90, 90)
    elif placement == 'bottom_left':
        ink.pizza_slice(canvas, (x, y + grid_size), grid_size, 0, 90)
    elif placement == 'top_right':
        ink.pizza_slice(canvas, (x + grid_size, y), grid_size, 180, 90)
    elif placement == 'bottom_left':
        ink.pizza_slice(canvas, (x + grid_size, y + grid_size), grid_size, 270, 90)


def triangle(x, y):
    # draw background
    ink.color = random.choice(colors)
    ink.rectangle(canvas, (x, y), grid_size, grid_size)
    ink.color = random.choice(colors)
    placement = random.choice(['left', 'right'])
    if placement == 'left':
        ink.triangle(canvas, (x, y), (x + grid_size, y + grid_size), (x, y + grid_size))
    elif placement == 'right':
        ink.triangle(canvas, (x + grid_size, y), (x + grid_size, y + grid_size), (x, y + grid_size))


def tile(x, y):
    shape = random.choice(['half_circle', 'triangle'])
    if shape == 'half_circle':
        quarter_circle(x, y)
    elif shape == 'triangle':
        triangle(x, y)


for x in range(margin, canvas.width - margin, grid_size):
    for y in range(margin, canvas.height - margin, grid_size):
        tile(x, y)

canvas.show()
