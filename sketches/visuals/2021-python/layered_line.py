import shades
import random

canvas = shades.Canvas(700, 700)

shade = shades.NoiseGradient(
    color=(240,200,200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
    warp_size=100,
    warp_noise=(
      shades.NoiseField(scale=0.002),
      shades.NoiseField(scale=0.002),
      )
    )

for i in range(random.randint(250,350), random.randint(400,550), 100):
  shade.noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
  shade.rectangle(canvas, (-100, i), random.randint(500,700), 100)

canvas.show()
