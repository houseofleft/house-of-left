import sketcher
import random

for i in range(8):
    canvas = sketcher.Canvas(1004,1475)

    ink = sketcher.Ink('simplex_gradient', (200,200,200), c_var=70, noise_seeds=[random.randint(0,999) for i in range(3)], warp_seeds=[random.randint(0,999) for i in range(2)], warp_scale=0.001, warp_size=400)

    for y in range(0-ink.warp_size,canvas.height+ink.warp_size,10):
        canvas.line((0-ink.warp_size,y),(canvas.width+ink.warp_size,y),ink)

    for x in range(0-ink.warp_size,canvas.width+ink.warp_size,10):
        canvas.line((x,0-ink.warp_size),(x,canvas.height+ink.warp_size),ink)

    canvas.save('lines'+str(random.randint(0,99999))+'.png')
    canvas.show()
