import shades
from random import randint

canvas = shades.Canvas()


mono_noise = shades.NoiseField(scale=0.005)
mono = shades.NoiseGradient(color=(200,200,200), color_variance=50, noise_fields=[mono_noise for i in range(3)])
flecks = shades.SwirlOfShades(
  noise_field=shades.NoiseField(scale=0.05),
  shades=([
    (0.7, 1, shades.BlockColor((200, 200, 200)))
  ]),
)

shades.SwirlOfShades
#mono.fill(canvas)
flecks.fill(canvas)

canvas.show()
