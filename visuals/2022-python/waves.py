import shades
import random

canvas = shades.Canvas(2000, 2000)

shade = shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.001))
noise = shades.NoiseField(scale=0.005)

shift = random.uniform(0.4, 0.6)
start = random.randint(0, canvas.width*0.3)
plus = random.randint(canvas.width*0.33, canvas.width*0.75)
space = random.randint(2, 7)
keep = False
for y in range(-canvas.height, canvas.height+400, space):
    for i, x in enumerate(range(-400, canvas.width+400)):
        if not keep:
            keep = random.random() > 0.99
        else:
            keep = random.random() > 0.01
        if keep:
            warp = noise.noise((x, y*0.06))
            warp -= 0.5
            warp *= 200
            shade.point(canvas, (x, y + warp + (shift * i)))

canvas.show()
