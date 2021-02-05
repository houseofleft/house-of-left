import shades
import random

canvas = shades.Canvas()
shade = shades.NoiseGradient(
  color=(200,200,200),
  color_variance=40,
  noise_fields=[shades.NoiseField(scale=0.002) for i in range(3)]
  )

points = [(random.randint(0, canvas.width), random.randint(0, canvas.height)) for i in range(200)]

def distance_between(p1, p2):
  return (((p1[0] - p2[0]) ** 2) + ((p1[1]-p2[1]) ** 2)) ** 0.5

for point in points:
  points.sort(key=lambda x: distance_between(x, point))
  for i in range(1, 20):
    shade.line(canvas, point, points[i], 1)

canvas.show()
