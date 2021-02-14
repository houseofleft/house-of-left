import shades
import random

canvas = shades.Canvas(2000, 2000)

size_noise = shades.NoiseField(scale=0.003)

block_shade = shades.BlockColor()

gradient_shade = shades.NoiseGradient(
    color = (253, 208, 41),
    noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)]
    )

start_x = 150
start_y = 200
gap = 90
tilt = 300
width = canvas.width - (start_x * 2)
height = canvas.height - (start_y * 2) - tilt

def circle_line(xy, width, tilt, shade):
    i_count = 0
    for x in range(int(xy[0]), int(xy[0] + width)):
        y = xy[1] + ((i_count / width) * tilt)
        size = size_noise.noise((x,y)) * 7
        shade.circle(canvas, (x,y), size)
        i_count += 1

for y in range(start_y, start_y + height, gap):
    inset = 0
    circle_line((start_x + 4, y + 4), width, tilt, gradient_shade)
    circle_line((start_x, y), width, tilt, block_shade)

canvas.show()

