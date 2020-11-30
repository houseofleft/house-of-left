import sketcher
import random

canvas = sketcher.Canvas(800, 800)
ink = sketcher.Ink('simplex_gradient', color=(200,200,200), c_var=70, noise_seeds=[random.randint(0,9999) for i in range(3)], warp_seeds=[random.randint(0,999) for i in [1,2]], warp_scale=0.01, warp_size=50)

#canvas.fill(sketcher.Ink('simplex_gradient', color=(60,60,60)))


for i in range(1):
    x_offset = random.uniform(-1,1) * 200
    y_offset = random.uniform(-1,1) * 200

    size = 5
    while size < canvas.height:
        canvas.circle((canvas.width/2 + x_offset, canvas.height/2 + y_offset), size, size-2, ink)
        size += 5

canvas.show()
canvas.save('circles{}.png'.format(random.randint(1,999999)))
