import shades

canvas = shades.Canvas()

shade = shades.DomainWarpGradient(
    color=(260, 260, 260),
    color_variance=60,
    noise_fields=[shades.NoiseField(scale=0.002), shades.NoiseField(scale=0.003), shades.NoiseField(scale=0.005)],
    depth=2,
    feedback=2.4,
)

shade.fill(canvas)

canvas.show()
