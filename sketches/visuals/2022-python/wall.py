import shades
import random
from handy_stuff import palletes

canvas = shades.Canvas()
if random.random() < 0.5:
    tones = [shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.002, channels=3)) for i in range(random.randint(2, 15))]
else:
    pallete = random.choice(palletes)
    tones = [shades.BlockColor(i) for i in pallete]

shift = random.randint(10, 40)
spacing = random.randint(2, 5)
grid_size_x = random.randint(20, 30)
grid_size_y = random.randint(30, 60)

for y in range(-grid_size_y, canvas.height + grid_size_y, grid_size_y):
    for i, x in enumerate(range(-grid_size_x, canvas.width + grid_size_x, grid_size_x)):
        tone = random.choice(tones)
        for plus_y in range(0, grid_size_y, spacing):
            if i % 2 == 0:
                tone.line(canvas, (x, y + plus_y), (x + grid_size_x, y + plus_y + shift), 1)
            else:
                tone.line(canvas, (x, y + plus_y + shift), (x + grid_size_x, y + plus_y), 1)

canvas.show()
