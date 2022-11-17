import sketcher
import random
from opensimplex import OpenSimplex

canvas = sketcher.Canvas(700,700)
grid_w = 10
grid_h = 10
noise = OpenSimplex(random.randint(0,999999))

for x in range(200, canvas.width-200, grid_w*2):
    for y in range(10, canvas.height-10, grid_h*2):
        xy_noise = sketcher.mapped_noise(noise, (x*0.02,y*0.02), 0, 1)
        canvas.line((x+grid_w*xy_noise,y),(x+grid_w*(1-xy_noise),y+grid_h))

canvas.save('flow_field.png')
canvas.show()
