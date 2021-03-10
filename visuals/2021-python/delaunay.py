import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas(1920, 1200)
ink = shades.NoiseGradient(
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)

points = [(randint(0, canvas.width), randint(0, canvas.height)) for i in range(90)]
# plus some edge points to make sure the whole canvas is coloured
points.append((0, 0))
points.append((0, canvas.height))
points.append((canvas.width, 0))
points.append((canvas.width, canvas.height))
points.append((0, canvas.height/2))
points.append((canvas.width, canvas.height/2))
points.append((canvas.width/2, 0))
points.append((canvas.width/2, canvas.height))

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
