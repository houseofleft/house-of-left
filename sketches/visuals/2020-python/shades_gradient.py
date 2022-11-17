import sketcher
import opensimplex
import random

canvas = sketcher.Canvas(600,600)
noise_scale = 0.004

for c in [(137,143,167),(224,173,89),(209,192,181)]:
    noise = opensimplex.OpenSimplex(random.randint(0,9999))
    ink = sketcher.Ink(color=c)
    for x in range(canvas.width):
        for y in range(canvas.width):
            ink.transparency = sketcher.mapped_noise(noise, (x*noise_scale, y*noise_scale), 0.4, 1)
            ink.point(canvas, (x,y))

canvas.save('grad{}.png'.format(random.randint(0,9999)))
canvas.show()
