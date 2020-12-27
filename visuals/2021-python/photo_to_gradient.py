import random
import shades
from PIL import Image

image = Image.open('image.jpg')
canvas = shades.Canvas(width=image.width, height=image.height)

num_points = random.randint(3,5)
points = []

for i in range(num_points):
    x = random.randint(0, image.width)
    y = random.randint(0, image.height)
    color = image.getpixel((x, y))
    points.append((color, (x,y)))

gradient = shades.PointGradient(points)

gradient.fill(canvas)
canvas.show()
