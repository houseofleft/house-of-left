import shades
from handy_stuff import palletes
import random

pallete = random.choice(palletes)

canvas = shades.Canvas()
tones = []
i = 0
while i < 1:
    add_to = random.uniform(0.0001, 0.0005)
    tones.append((
        i, i + add_to, shades.BlockColor(random.choice(pallete)),
    ))
    i += add_to

swirl = shades.SwirlOfShades(
    shades=tones,
    swirl_field=shades.NoiseField(scale=0.002),
    depth=1,
)

swirl.fill(canvas)
canvas.show()
