from  sketcher import *
import random

canvas = Canvas(600, 600)

noise_seeds = [random.randint(0,999) for i in range(0,3)]
color = [random.randint(150,250) for i in range(3)]

warp = Ink('simplex_gradient',color=color, c_var=70, noise_seeds=noise_seeds, noise_scale=0.001)

canvas.fill(warp)

img = shuffle_image(canvas.img, 10, 10)

img.show()
img.save('cool{}.png'.format(random.randint(1,99999)))
