import shades

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    color=(200, 200, 200),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
    color_variance=70,
    warp_size=50,
    warp_noise=[shades.NoiseField(scale=0.003) for i in range(3)],
)

for i in range(1, canvas.width, 4):
    ink.warp_size += 5
    ink.circle_outline(canvas, (canvas.width/2, canvas.height/2), i, 1)


canvas.show()
