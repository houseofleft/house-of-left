import shades
from random import uniform, randint

noise_scale = uniform(0, 0.02)
spacing = randint(2, 6)

canvas = shades.Canvas()

mono_field = shades.NoiseField(scale=0.002)
background = shades.NoiseGradient(
    color=(10, 10, 10),
    noise_fields=[mono_field for i in range(3)],
    color_variance=40,
)
outline = shades.BlockColor((100, 100, 100))

tunnel_noise_x = shades.NoiseField(scale=noise_scale)
tunnel_noise_y = shades.NoiseField(scale=noise_scale)

background.fill(canvas)

def circle_and_fill(xy, radius):
    for i in range(1, 50):
        background.circle_outline(canvas, xy, radius+i, 1)
    outline.circle_outline(canvas, xy, radius, 1)

for i in range(1, int(canvas.width*2/5), spacing):
    x_shift = tunnel_noise_x.noise((i, i)) * 200 - 100
    y_shift = tunnel_noise_y.noise((i, i)) * 200 - 100
    circle_and_fill((canvas.width/2 + x_shift, canvas.height/2 + y_shift), i)

canvas.show()
