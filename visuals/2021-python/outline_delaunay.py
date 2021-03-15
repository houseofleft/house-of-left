import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)],
    color=(100,150,200)
)

points = [(randint(50, canvas.width-50), randint(50, canvas.height-50)) for i in range(2000)]
# plus some edge points to make sure the whole canvas is coloured
points += [(randint(50, canvas.width-50), 50) for i in range(10)]
points += [(50, randint(50, canvas.height-50)) for i in range(10)]
points += [(randint(50, canvas.width-50), canvas.height-50) for i in range(10)]
points += [(canvas.width-50, randint(50, canvas.height-50)) for i in range(10)]
points += [(50, 50), (50, canvas.height-50), (canvas.width-50, 50), (canvas.width-50, canvas.height-50)]

# drawing triangles between points
for tri in Delaunay(points).simplices:
    ink.triangle_outline(
        canvas,
        points[tri[0]],
        points[tri[1]],
        points[tri[2]],
        1
    )

canvas.show()
