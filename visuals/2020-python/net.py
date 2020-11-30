import sketcher
import random

canvas = sketcher.Canvas(700, 700)

toner = sketcher.Ink(color=(240,240,240))

seeds = [random.randint(0,999),random.randint(0,999)]
scale = 0.002
size = random.randint(40,150)

background = sketcher.Ink('simplex_gradient', (33,136,254), c_var=70, noise_scale=0.002, noise_seeds=[random.randint(0,999) for x in range(3)])

canvas.fill(background)

x = -size

while x < canvas.width + size:
    y = -size
    while y < canvas.height + size:
        canvas.circle(sketcher.adjust_point((x,y), seeds, scale, size), 3, ink=toner)
        y += 20
    x += 20

canvas.show()
