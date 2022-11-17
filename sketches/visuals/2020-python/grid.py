from sketcher import *
import random

canvas = Canvas(1004, 1475)
colours = [(6,82,158),(6,82,158),(0,111,166),(0,176,212),(0,184,219),(0,111,166),(0,176,212),(222,208,173),(229,187,172)]
colours = [(252, 277, 67),(74,140,167),(109,181,197),(109,181,197),(0,155,202),(0,155,202),(0,155,202),(230,243,247),(17,92,112),(17,92,112)]


# goal is to draw an angled grid (we'll do this with triangles)
# first though, we'll just do a straight grid
grid_width = 100
grid_height = 150
offset = 100
i = 0

for x in range(0, canvas.width+grid_width, grid_width):
    for y in range((i%grid_height)-grid_height, canvas.height+grid_height, grid_height):
        fill = Ink(color=random.choice(colours))
        canvas.triangle((x,y), (x,y+grid_height), (x+grid_width,y+offset), fill)
        canvas.triangle((x,y+grid_height), (x+grid_width,y+offset), (x+grid_width,y+grid_height+offset), fill)
    i += offset

canvas.show()
