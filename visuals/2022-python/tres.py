import shades
import random

canvas = shades.Canvas()

uno_shade = shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.001))
dos_shade = shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.001))
uno_noise, dos_noise = shades.noise_fields(scale=0.005, channels=2)
uno_size, dos_size = shades.noise_fields(scale=0.005, channels=2)
uno = {'shade': uno_shade, 'noise': uno_noise, 'size': uno_size}
dos = {'shade': dos_shade, 'noise': dos_noise, 'size': dos_size}

shift = random.uniform(0.4, 0.6)
tone = random.choice([uno, dos])
start = random.randint(0, canvas.width*0.3)
plus = random.randint(canvas.width*0.33, canvas.width*0.75)
space = random.randint(2, 7)
keep = False
for y in range(-canvas.height, canvas.height+400, space):
    for i, x in enumerate(range(-400, canvas.width+400)):
        if not keep:
            keep = random.random() > 0.99
        else:
            keep = random.random() > 0.01
        if keep:
            warp = tone['noise'].noise((x, y*0.06))
            warp -= 0.5
            warp *= 200
            tone['shade'].point(canvas, (x, y + warp + (shift * i)))

canvas.show()
