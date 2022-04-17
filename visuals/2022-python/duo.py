import shades
import random

canvas = shades.Canvas(2000, 2000)

uno_shade = shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.001))
dos_shade = shades.NoiseGradient((180, 180, 180), color_fields=shades.noise_fields(scale=0.001))
uno_noise, dos_noise = shades.noise_fields(scale=0.005, channels=2)
uno_size, dos_size = shades.noise_fields(scale=0.005, channels=2)
uno = {'shade': uno_shade, 'noise': uno_noise, 'size': uno_size}
dos = {'shade': dos_shade, 'noise': dos_noise, 'size': dos_size}

for _ in range(10):
    tone = random.choice([uno, dos])
    start = random.randint(0, canvas.width)
    plus = random.randint(100, 300)
    space = random.randint(5, 20)
    for y in range(300, canvas.height-300, space):
        for x in range(start, start + plus):
            size = tone['size'].noise((x, y)) * 3
            size += 1
            size = int(size)
            warp = tone['noise'].noise((x, y*0.06))
            warp -= 0.5
            warp *= 200
            tone['shade'].weighted_point(canvas, (x, y + warp), size)

canvas.show()
