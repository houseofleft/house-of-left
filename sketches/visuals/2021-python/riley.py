import shades
import random

canvas = shades.Canvas(2400*2, 1500*2, (20, 20, 20))


class RandomFill(shades.Shade):
    def determine_shade(self, xy):
        if random.random() < self.chance:
            return (200, 200, 200)


tone = RandomFill(
    warp_size=500,
    warp_noise=[shades.NoiseField(scale=0), shades.NoiseField(scale=0.00125)],
)

for y in range(0, canvas.height + 500, 10 * 2):
    tone.chance = (y ** 2 / 10000) / 500 / 2
    for i in range(0, 3):
        tone.line(canvas, (-500, y+i), (canvas.width, y+i), 1)

canvas.show()
