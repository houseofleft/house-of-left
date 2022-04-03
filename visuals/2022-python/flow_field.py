import shades
import random

canvas = shades.Canvas(1000, 1000)
x_field = shades.NoiseField(
    scale=random.uniform(0.3, 0.8),
    buffer=1500,
    limit=3000,
)
y_field = shades.NoiseField(
    scale=random.uniform(0.3, 0.8),
    buffer=1500,
    limit=3000,
)
gradient = shades.NoiseGradient(
    color=(200, 200, 200),
    noise_fields=shades.noise_fields(
        scale=random.uniform(0.1, 0.4),
        buffer=1500,
        limit=3000,
        channels=3,
    ),
)
ink = shades.BlockColor(
    warp_noise=shades.noise_fields(
        scale=0,
        buffer=1500,
        limit=3000,
        channels=2,
    ),
)


class Walker():
    """
    Class to move based on flow field, and mark point on grid
    Takes xy coord as sole initialisation argument
    """

    def __init__(self, xy):
        self.affect = 10
        self.xy = xy
        ink.color = gradient.determine_shade((
            int(self.xy[0]),
            int(self.xy[1]),
        ))

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
    x = random.randint(-1500, canvas.width)
    y = random.randint(-1500, canvas.height)
    return x, y


ink.color = gradient.determine_shade(canvas.random_point())
ink.fill(canvas)

for i in range(0, 7000):
    walker = Walker(random_start())
    [walker.update() for i in range(700)]

canvas.show()
