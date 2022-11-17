import random
import shades

canvas = shades.Canvas()

ink = shades.BlockColor()
toner = shades.NoiseGradient((200, 100, 100))

initial_color = [0, 0, 0]
color_add = random.randint(1, 4)
lines = random.randint(2, 4)
gap = random.randint(3, 70)

for y in range(-canvas.height, canvas.height, gap):
    onoff = True
    for i in range(0, canvas.height, gap):
        initial_color = list(toner.determine_shade((y+i, y+i)))
        if onoff:
            for j in range(0, gap, lines):
                ink.color = shades.color_clamp([i+(j*color_add) for i in initial_color])
                ink.line(canvas, (i, y+i+j), (i+gap, y+i+j+gap), 1)
        onoff = not onoff
    onoff = False
    for i in range(0, canvas.height, gap):
        initial_color = list(toner.determine_shade((y+i, y+i)))
        if onoff:
            for j in range(0, gap, lines):
                ink.color = shades.color_clamp([i+(j*color_add) for i in initial_color])
                ink.line(canvas, (i+gap, y+i+j), (i, y+i+j+gap), 1)
        onoff = not onoff


canvas.show()
