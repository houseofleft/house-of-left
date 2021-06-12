import shades
from random import randint

canvas = shades.Canvas()
g_noise = [shades.NoiseField(scale=0.002) for i in range(3)]

def random_color():
    r = randint(150, 250)
    g = randint(150, 250)
    b = randint(150, 250)
    return (r, g, b)

shade_one = shades.NoiseGradient(color=random_color(), noise_fields=g_noise)
shade_two = shades.NoiseGradient(color=random_color(), noise_fields=g_noise)

shade_one.triangle(canvas, (0, 0), (0, canvas.height), (canvas.width, 0))
shade_two.triangle(canvas, (canvas.width, 0), (canvas.width, canvas.height), (0, canvas.height))

canvas.show()
