import sketcher
import random

canvas = sketcher.Canvas(800, 800)
ink = sketcher.Ink(color=(100,100,100), warp_seeds=[random.randint(0,999) for i in [1,2]], warp_scale=0.01, warp_size=0)

canvas.fill(sketcher.Ink('simplex_gradient', color=(60,60,60)))

y = 300

while y < canvas.height - 200:

    canvas.circle((canvas.width/2,y),300, 299, ink)
    ink.warp_size += 4
    y += 7

canvas.show()
canvas.save('cool'+str(random.randint(0,99999999))+'.png')
