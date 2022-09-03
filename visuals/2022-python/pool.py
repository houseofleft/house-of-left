import shades
import random

warp = 200
gap = 10
tilt = 50

canvas = shades.Canvas(2000, 2000)
ink = shades.NoiseGradient(
    color=(150, 150, 150),
    color_fields=shades.noise_fields(scale=[random.uniform(0, 0.001) for i in range(3)]),
    color_variance=150,
    warp_size=warp,
    warp_noise=shades.noise_fields(scale=0.002, channels=2),
)

switch = True
for y in range(-warp-tilt, canvas.height+warp, gap):
    if switch:
        ink.line(canvas, (-warp, y), (canvas.width+warp, y+tilt), 1)
        ink.line(canvas, (canvas.width+warp, y), (0-warp, y+tilt), 1)
    if random.random() < 0.01:
        switch = not switch

canvas.show()