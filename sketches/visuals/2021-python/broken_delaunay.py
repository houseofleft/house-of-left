import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas(1000, 1000)
ink = shades.NoiseGradient(
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)

points = [
 (randint(-canvas.width, canvas.width*2),
     randint(-canvas.height, canvas.height*2)) for i in range(70)]

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
