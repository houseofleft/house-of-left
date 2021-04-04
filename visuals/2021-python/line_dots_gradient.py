import shades
from random import randint, uniform

rs = randint(1, 9999)
gs = randint(1, 9999)
bs = randint(1, 9999)

canvas = shades.Canvas(1000, 1000)
gradient = shades.NoiseGradient(
    color=(102, 150, 200),
    color_variance=60,
    noise_fields=[shades.NoiseField(scale=uniform(0.0001, 0.001)) for i in range(3)],
)

gradient.fill(canvas)

size_noise = shades.NoiseField(scale=0.02)
x_space_noise = shades.NoiseField(scale=0.02)
y_space_noise = shades.NoiseField(scale=0.002)
color_noise = shades.NoiseField(scale=0.02)
color_scales = [[uniform(0.0001, 0.001) for i in range(3)] for j in range(6)]

x = 0
y = 0
t = randint(1, 9999)
scale = randint(3,5)
scale_change_x = randint(2,4)
scale_change_y = randint(2, 4)

while y < canvas.height:
    x = 0
    while x < canvas.width:
        c_val = color_noise.noise((t,1))
        color_scale = color_scales[int(c_val*len(color_scales))]
        rn = shades.NoiseField(scale=color_scale[0], seed=rs)
        gn = shades.NoiseField(scale=color_scale[1], seed=gs)
        bn = shades.NoiseField(scale=color_scale[2], seed=bs)
        gradient.noise_fields = [rn, gn, bn]
        gradient.circle(canvas, (x, y), size_noise.noise((t,1))*scale)
        x += x_space_noise.noise((t,1))*scale*scale_change_x
        t += 1


    y += y_space_noise.noise((t,1))*scale*scale_change_y

canvas.show()
