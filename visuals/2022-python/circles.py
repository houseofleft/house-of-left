import shades
import random

canvas = shades.Canvas(1500, 1500)
noise = shades.NoiseField(scale=0.02)
ink = shades.BlockColor()

colors = [
    (249, 65, 68),
    (243, 114, 44),
    (248, 150, 30),
    (249, 132, 74),
    (249, 199, 79),
    (144, 190, 109),
    (67, 170, 139),
    (77, 144, 142),
    (87, 117, 144),
    (39, 125, 161),
]

for y in range(0, canvas.height, 5):
    segments = 15
    for i in range(segments):
        x = (canvas.width/segments) * i
        if i % 2:
            size = canvas.width/segments/2 * noise.noise((x, y))
        else:
            size = canvas.width/segments/2 * (1 - noise.noise((x, y)))
        ink.color = random.choice(colors)
        ink.circle_outline(canvas, (x, y), size, 1)

canvas.show()
