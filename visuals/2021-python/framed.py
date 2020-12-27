import shades

canvas = shades.Canvas(1400, 1400)

shade = shades.NoiseGradient(
    color = (200, 200, 200),
    noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)],
    warp_size = 300,
    warp_noise = (shades.NoiseField(scale=0.002),shades.NoiseField(scale=0.002))
)

for x in range(-300, canvas.width+300, 10):
    shade.line(canvas, (x,-300), (x,canvas.height+300), 1)

for y in range(-300, canvas.height+300, 10):
    shade.line(canvas, (-300,y), (canvas.height+300,y), 1)

white = shades.BlockColor((240,240,240))
border_size = 300

white.rectangle(canvas, (0, 0), border_size, canvas.height)
white.rectangle(canvas, (0, 0), canvas.width, border_size)
white.rectangle(canvas, (0, canvas.height - border_size), canvas.width, border_size)
white.rectangle(canvas, (canvas.width - border_size, 0), border_size, canvas.height)

canvas.show()
