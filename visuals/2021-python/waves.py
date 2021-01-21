import shades

canvas = shades.Canvas()

shade = shades.NoiseGradient(
    color=(200, 200, 200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
    )

block = shades.BlockColor(
    color=(240, 240, 240),
    warp_size=150,
    warp_noise=(shades.NoiseField(scale=0),shades.NoiseField(scale=0.008)),
    )

shade.fill(canvas)

for y in range(-150, canvas.height+150, 4):
    block.line(canvas, (-150, y), (canvas.width + 150, y), 1)

canvas.show()
