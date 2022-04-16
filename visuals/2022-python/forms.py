import shades
from random import randint

canvas = shades.Canvas(1000, 1000)

for i in range(2):
    ink = shades.NoiseGradient(
        color=(180,180,180),
        color_fields=shades.noise_fields(scale=0.001, channels=3),
        color_variance=80,
        warp_size=30,
        #warp_noise=[shades.NoiseField(scale=0.0002) for i in range(2)],
    )

    centre = canvas.random_point()
    for i in range(1, int(canvas.height/2), 5):
        ink.circle(
            canvas,
            centre,
            i,
        )

canvas.show() 

