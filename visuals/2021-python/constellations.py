import shades
from random import randint
from scipy.spatial import Delaunay

canvas = shades.Canvas(700, 700)
background = shades.NoiseGradient(
    color=(0, 0, 50),
    noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
)
white = shades.BlockColor((255, 255, 255))

background.fill(canvas)

points = [(randint(0, canvas.width), randint(0, canvas.height)) for i in range(200)]

for point in points:
    white.circle(canvas, point, randint(1,1))

# drawing triangles between points
for tri in Delaunay(points).simplices:
    if randint(1, 30) == 1:
        white.triangle_outline(
            canvas,
            points[tri[0]],
            points[tri[1]],
            points[tri[2]],
            1
        )

canvas.show()
