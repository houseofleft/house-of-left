import shades
import random

canvas = shades.Canvas()
block = shades.BlockColor()

red = shades.NoiseGradient(
    color = (241, 0, 0),
    noise_fields = [shades.NoiseField(scale=0.005) for i in range(3)]
)

blue = shades.NoiseGradient(
    color = (40, 13, 144),
    noise_fields = [shades.NoiseField(scale=0.005) for i in range(3)]
)

yellow = shades.NoiseGradient(
    color = (246, 225, 0),
    noise_fields = [shades.NoiseField(scale=0.005) for i in range(3)]
)

mono_noise = shades.NoiseField(scale=0.005)
white = shades.NoiseGradient(
    color = (240, 240, 240),
    noise_fields = [mono_noise for i in range(3)]
)

gradient = shades.SwirlOfShades(
    shades = [
        (0, 0.2, white),
        (0.2, 0.3, red),
        (0.3, 0.4, yellow),
        (0.4, 0.6, white),
        (0.6, 0.7, blue),
        (0.7, 0.8, red),
        (0.8, 1, white)
    ],
    noise_field = shades.NoiseField(scale=0.006),
)

grid_size = 50

for x in range(0, canvas.width, grid_size):
    for y in range(0, canvas.height, grid_size):
        block.color = gradient.determine_shade((x,y))
        block.rectangle(canvas, (x,y), grid_size, grid_size)

canvas.show()
