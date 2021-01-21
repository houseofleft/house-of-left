import shades

canvas = shades.Canvas(1500, 1500)

noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)]

block = shades.NoiseGradient((200,200,200), noise_fields=noise_fields)
fade = shades.NoiseGradient((220,220,220), noise_fields=noise_fields)

swirl = shades.SwirlOfShades(
  noise_field=shades.NoiseField(scale=0.005),
  depth=1,
  feedback=3,
  shades=[
    (0.8, 0.1, fade),
    (0.1, 0.15, block),
    (0.15, 0.17, fade),
    (0.28, 0.3, fade),
    (0.3, 0.35, block),
    (0.35, 0.37, fade),
    (0.48, 0.5, fade),
    (0.5, 0.55, block),
    (0.55, 0.57, fade),
    (0.68, 0.7, fade),
    (0.7, 0.75, block),
    (0.75, 0.77, fade),
    (0.88, 0.9, fade),
    (0.9, 0.95, block),
    (0.95, 0.97, fade),
  ]
)

swirl.fill(canvas)

canvas.show()
