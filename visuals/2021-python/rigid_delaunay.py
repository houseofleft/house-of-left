import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas()
ink = shades.NoiseGradient(
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)

points = []
for x in range(0, canvas.width+50, 20):
    for y in range(0, canvas.height+50, 20):
        if randint(1,3) == 1:
            points.append((x,y))

# drawing triangles between points
for tri in Delaunay(points).simplices:
    ink.color = [randint(180, 255) for i in range(3)]
    ink.triangle(
        canvas,
        points[tri[0]],
        points[tri[1]],
        points[tri[2]],
    )

canvas.show()
