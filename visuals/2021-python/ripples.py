import shades

canvas = shades.Canvas()

colors = [(0, 255, 255), (255, 0, 255), (255, 255, 0)]

for color in colors:
  shade = shades.SwirlOfShades(
    noise_field=shades.NoiseField(scale=0.005),
    shades=([
      (0.4, 0.6, shades.BlockColor(color, transparency=0.6))
    ]),
  )
  shade.fill(canvas)

canvas.show()
