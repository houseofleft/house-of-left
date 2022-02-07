import shades
from random import randint

canvas = shades.Canvas(6000, 4000)

def random_point():
    x = randint(0, canvas.width)
    y = randint(0, canvas.height)
    return (x, y)

for i in range(6):
    ink = shades.NoiseGradient(
        color=(180,180,180),
        noise_fields=[shades.NoiseField(scale=0.0003) for i in range(3)],
        color_variance=80,
        warp_size=700,
        warp_noise=[shades.NoiseField(scale=0.0007) for i in range(2)],
    )

    centre = random_point()
    for i in range(1, int(canvas.height/2), 5):
        ink.circle_outline(
            canvas,
            centre,
            i,
            1,
        )

canvas.show() 
