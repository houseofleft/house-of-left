import shades
from random import randint

canvas = shades.Canvas(1000, 1000, (220, 230, 229))
block = shades.BlockColor((229, 211, 96))
size_noise = shades.NoiseField(scale=0.02)
x_space_noise = shades.NoiseField(scale=0.02)
y_space_noise = shades.NoiseField(scale=0.002)
color_noise = shades.NoiseField(scale=0.02)
colors = [
    (189, 213, 215),
    (67, 99, 110),
    (253, 243, 218),
    (103, 151, 165),
    (255, 193, 178),
]

x = 0
y = 0
t = randint(1, 9999)
scale = randint(3,5)
scale_change_x = randint(2,4)
scale_change_y = randint(2, 4)


while y < canvas.height:
    x = 0
    while x < canvas.width:
        block.circle(canvas, (x, y), size_noise.noise((t,1))*scale)
        x += x_space_noise.noise((t,1))*scale*scale_change_x
        t += 1
        c_val = color_noise.noise((t,1))
        block.color = colors[int(c_val * len(colors))]

    y += y_space_noise.noise((t,1))*scale*scale_change_y

canvas.show()
