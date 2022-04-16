import shades
import random
from handy_stuff import palletes

canvas = shades.Canvas(2000, 2000)
pallete = random.choice(palletes)
random.shuffle(pallete)

canvas = shades.Canvas(2000, 2000, pallete[0])

tone = shades.BlockColor(warp_noise=shades.noise_fields(scale=[0, random.uniform(0, 0.002)], channels=2), warp_size=random.randint(300, 900))
shift = random.randint(3, 9)

for y in range(-tone.warp_size, canvas.height+tone.warp_size, 30):
    for x in range(-50, canvas.width):
        for i in range(30):
            tone.color = pallete[i % len(pallete)]
            tone.weighted_point(canvas, (x+i*shift, y+i*shift), 2)

canvas.show()
