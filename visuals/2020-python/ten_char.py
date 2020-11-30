import sketcher
import random

canvas = sketcher.Canvas(1200,1200)


for y in range(0, canvas.height, 25):
    for x in range(0, canvas.width, 25):
        if random.randint(0,1) == 0:
            canvas.line((x,y),(x+25,y+25))
        else:
            canvas.line((x,y+25),(x+25,y))

canvas.show()
