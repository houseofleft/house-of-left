import shades
import random
from handy_stuff import palletes

canvas = shades.Canvas(2000, 2000)
pallete = random.choice(palletes)

shade = shades.BlockColor(random.choice(pallete))
shade.fill(canvas)
noise = shades.NoiseField(scale=0.005)

shift = random.uniform(0.4, 0.6)
start = random.randint(0, canvas.width*0.3)
keep = False
for y in range(-canvas.height, canvas.height+400, 3):
    shade.color = random.choice(pallete)
    for i, x in enumerate(range(-400, canvas.width+400)):
        if not keep:
            keep = random.random() > 0.99
            if keep:
                shade.color = random.choice(pallete)
        else:
            keep = random.random() > 0.01
        if keep:
            warp = noise.noise((x, y*0.06))
            warp -= 0.5
            warp *= 200
            shade.point(canvas, (x, y + warp + (shift * i)))

canvas.show()
