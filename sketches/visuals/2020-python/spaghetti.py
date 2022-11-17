import sketcher
import random
from opensimplex import OpenSimplex
canvas = sketcher.Canvas(1000,1000)

ink = sketcher.Ink('simplex_gradient', (200,200,200), c_var=70, noise_seeds=[random.randint(0,999) for i in range(3)], warp_scale=0.004, warp_size=300)

for i in range(3):
    ink.warp_noise = [OpenSimplex(random.randint(0,999)) for i in range(2)]
    for y in range(0-ink.warp_size,canvas.height+ink.warp_size,10):
        canvas.line((0-ink.warp_size,y),(canvas.width+ink.warp_size,y),ink)

canvas.save('overlapping_grids_{}.png'.format(random.randint(1,9999)))
canvas.show()
