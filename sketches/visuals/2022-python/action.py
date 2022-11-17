import shades
import random
from handy_stuff import palletes


MIN_SCALE = random.uniform(0, 0.5)
MAX_SCALE = MIN_SCALE + random.uniform(0, 0.5)
MAX_SIZE = random.randint(1, 5)
WALK_LENGTH = random.randint(400, 2000)
WALKERS = random.randint(300, 1500)

pallete = random.choice(palletes)
canvas = shades.Canvas(2000, 2000)
x_field, y_field = shades.noise_fields(scale=random.uniform(0.004, 0.008), channels=2)
ink = shades.NoiseGradient(color_variance=20)


class Walker():
    """
    Class to move based on noise of count, and mark point on grid
    Takes xy coord as sole initialisation argument
    """

    def __init__(self, xy, color=(60, 140, 180)):
        self.affect = 10
        self.xy = xy
        self.x_noise = random.randint(0, 999)
        self.y_noise = random.randint(0, 999)
        self.scale = random.uniform(0, 0.6)
        self.size = random.randint(1, MAX_SIZE)
        ink.color = color

    def draw(self):
        ink.weighted_point(canvas, self.xy, self.size)

    def move(self):
        new_x = self.xy[0] + (x_field.noise((self.x_noise, self.x_noise))-0.5)*2
        new_y = self.xy[1] + (y_field.noise((self.y_noise, self.y_noise))-0.5)*2
        self.xy = (new_x, new_y)
        self.x_noise += self.scale
        self.y_noise += self.scale

    def update(self):
        self.draw()
        self.move()


def random_start():
    x = random.randint(-500, canvas.width)
    y = random.randint(-500, canvas.height)
    return x, y


for i in range(0, WALKERS):
    walker = Walker(random_start(), random.choice(pallete))
    [walker.update() for i in range(1400)]


canvas.show()
