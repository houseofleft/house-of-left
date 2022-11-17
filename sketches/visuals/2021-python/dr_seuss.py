import shades

canvas = shades.Canvas()

black = shades.BlockColor((20, 20, 20))
red = shades.BlockColor((255, 20, 0))
blue = shades.BlockColor((0, 139, 200))

swirl = shades.SwirlOfShades(
    shades = [
        (0.25, 0.3, black),
        (0.3, 0.4, red),
        (0.4, 0.45, black),
        (0.55, 0.6, black),
        (0.6, 0.8, blue),
        (0.8, 0.85, red),
        (0.85, 0.9, black)
    ],
    noise_field = shades.NoiseField(scale=0.006),
    feedback = 2
)

swirl.fill(canvas)

canvas.show()
