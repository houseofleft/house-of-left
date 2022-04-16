import shades
import random
from handy_stuff import palletes

pallete = random.choice(palletes)
canvas = shades.Canvas(2000, 2000, random.choice(pallete))
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


for i in range(0, 5000):
    walker = Walker(random_start(), random.choice(pallete))
    [walker.update() for i in range(400)]


canvas.show()
