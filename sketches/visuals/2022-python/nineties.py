import shades
import random

GRID_SIZE = 40

canvas = shades.Canvas()
shadow = shades.BlockColor((40, 40, 40))
gradient = shades.NoiseGradient((200, 200, 200))

for i in range(10):
    # todo: add logic to check whether square already there
    #       add additional shapes
    x = random.choice(range(0, canvas.width, GRID_SIZE))
    y = random.choice(range(0, canvas.height, GRID_SIZE))
    width = GRID_SIZE * random.randint(1, 5)
    shadow.square(canvas, (x+5, y+5), width)
    gradient.square(canvas, (x, y), width)

canvas.show()
