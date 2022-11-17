"""
Swimming Pools 2022

Expected arguments: output-file, width (px), height (px)

"""
import sys
import random

import shades

output_file, width, height = sys.argv[1:]

palletes = [
    [(27, 26, 23), (240, 165, 0), (228, 88, 38), (230, 213, 183)],
    [(84, 99, 255), (236, 236, 236), (255, 195, 0), (255, 24, 24)],
    [(255, 211, 45), (0, 142, 137), (8, 94, 125), (8, 69, 148)],
    [(21, 114, 161), (154, 208, 236), (239, 218, 215), (227, 190, 198)],
    [(150, 206, 180), (255, 238, 173), (217, 83, 79), (255, 173, 96)],
    [(0, 255, 255), (255, 0, 255), (255, 255, 0)],
    [(250, 0, 0), (0, 255, 0), (0, 0, 255)],
]
pallete = random.choice(palletes)
canvas = shades.Canvas(height, width, random.choice(pallete))
x_field = shades.NoiseField(
    scale=random.uniform(0.003, 0.008),
)
y_field = shades.NoiseField(
    scale=random.uniform(0.003, 0.008),
)
ink = shades.BlockColor()


class Walker():
    """
    Class to move based on flow field, and mark point on grid
    Takes xy coord as sole initialisation argument
    """

    def __init__(self, xy, color=(60, 140, 180)):
        self.affect = 10
        self.xy = xy
        ink.color = color

    def draw(self):
        ink.point(canvas, (int(self.xy[0]), int(self.xy[1])))

    def move(self):
        x_vect = x_field.noise((
                int(self.xy[0]),
                int(self.xy[1]),
            ))
        y_vect = y_field.noise((
                int(self.xy[0]),
                int(self.xy[1]),
            ))
        new_x = self.xy[0] + x_vect
        new_y = self.xy[1] + y_vect
        self.xy = (new_x, new_y)

    def update(self):
        self.draw()
        self.move()


def random_start():
    x = random.randint(-500, canvas.width)
    y = random.randint(-500, canvas.height)
    return x, y


for i in range(0, 9000):
    walker = Walker(random_start(), random.choice(pallete))
    [walker.update() for i in range(400)]


canvas.save(output_file)
