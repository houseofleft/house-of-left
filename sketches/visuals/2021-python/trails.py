import shades
import random

warp_start = random.randint(30, 80)
warp_step = random.uniform(0.5, 5)
circle_step = random.randint(3, 6)


canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    color=(200, 200, 200),
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)],
    color_variance=70,
    warp_size=warp_start,
    warp_noise=[shades.NoiseField(scale=0.003) for i in range(3)],
)

for i in range(1, canvas.width, circle_step):
    ink.warp_size += warp_step
    ink.circle_outline(canvas, (canvas.width/2, canvas.height/2), i, 1)


canvas.show()
