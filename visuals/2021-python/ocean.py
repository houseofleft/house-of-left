import shades

canvas = shades.Canvas()

warp_size = 50
warp = shades.BlockColor(
    warp_size=warp_size,
    warp_noise=[shades.NoiseField(scale=0.1), shades.NoiseField(scale=0)],
)
ink = shades.BlockColor()
noise = shades.NoiseField()

for y in range(-warp_size, canvas.height + warp_size, 10):
    for x in range(-warp_size, canvas.width + warp_size):
        size = noise.noise((x, y)) * 3
        if size > 0:
            xy = warp.adjust_point((x, y))
            ink.circle(canvas, xy, size)


canvas.show()
