import shades
import random

canvas = shades.Canvas()
max_shape_height = random.randint(0, int(canvas.height/4))

for i in range(50):
    height = random.randint(0, max_shape_height)
    width = height / 3
    color = random.choice([(0, 200, 200), (200, 0, 200), (200, 200, 0)])
    shade = shades.NoiseGradient(
        color=color,
        color_variance=70,
        noise_fields=[shades.NoiseField(scale=random.uniform(0, 0.01)) for i in range(3)],
        transparency=random.uniform(0.2, 0.6),
    )
    shade.rectangle(
        canvas=canvas,
        xy=(random.randint(0, canvas.width), random.randint(0, canvas.height)),
        width=width,
        height=height,
    )

canvas.show()
