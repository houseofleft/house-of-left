import shades

canvas = shades.Canvas()

shade = shades.NoiseGradient(
    color = (253, 208, 41),
    noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)],
    warp_size = 300,
    warp_noise = (shades.NoiseField(scale=0.002),shades.NoiseField(scale=0.002))
)

for x in range(-300, canvas.width+300, 4):
    shade.line(canvas, (x,-300), (x,canvas.height+300), 1)

for y in range(-300, canvas.height+300, 4):
    shade.line(canvas, (-300,y), (canvas.height+300,y), 1)

canvas.show()
