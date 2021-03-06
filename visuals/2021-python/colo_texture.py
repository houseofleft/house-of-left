import shades
from random import randint, choice

canvas = shades.Canvas()
fill = shades.BlockColor(warp_size=10)

colors = [[randint(230, 250) for i in range(3)] for i in range(9)]

for i in range(20000):
    fill.warp_noise = ([shades.NoiseField(), shades.NoiseField()])
    fill.color = choice(colors)
    xy = (randint(-50, canvas.width), randint(-50, canvas.height))
    if randint(1, 2) == 1:
        xy2 = (xy[0], xy[1] + randint(1,100))
    else:
        xy2 = (xy[0] + randint(1,100), xy[1])
    fill.line(canvas, xy, xy2, 1)


canvas.show()
