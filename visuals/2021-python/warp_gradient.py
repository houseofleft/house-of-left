import shades

canvas = shades.Canvas()

shade = shades.DomainWarpGradient(
    color=(200,200,200),
    color_variance=70,
    noise_fields=[shades.NoiseField(scale=0.006) for i in range(3)],
    depth=2,
)

shade.fill(canvas)

canvas.show()
