import shades

canvas = shades.Canvas()
shade = shades.SwirlOfShades(
  noise_field=shades.NoiseField(scale=0.005),
  shades=([
    (0.4, 0.6, shades.BlockColor((63, 151, 197)))
  ]),
)

shade.fill(canvas)
canvas.show()
