import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas()
ink = shades.NoiseGradient(
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)

points = [(randint(100, canvas.width-100), randint(100, canvas.height-100)) for i in range(randint(10, 30))]

# drawing triangles between points
space_factor = randint(2, 5)
for tri in Delaunay(points).simplices:
    if randint(1, space_factor) == 1:
        ink.color = [randint(180, 255) for i in range(3)]
        ink.triangle(
            canvas,
            points[tri[0]],
            points[tri[1]],
            points[tri[2]],
        )

canvas.show()
