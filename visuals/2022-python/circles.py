import shades
from random import randint

canvas = shades.Canvas()

ink = shades.NoiseGradient(
    warp_size=250,
    color=(200, 200, 200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
)
for i in range(100):
    ink.warp_noise = [shades.NoiseField(scale=0.002), shades.NoiseField(scale=0.02)] 
    width = randint(25, 100)
    x = randint(0, canvas.width)
    for y in range(-500, canvas.height+500, 15):
        ink.circle_outline(canvas, (x, y), width, 1)

canvas.show()
