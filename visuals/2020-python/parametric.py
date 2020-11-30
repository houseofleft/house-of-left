import sketcher
import math
import random

canvas = sketcher.Canvas(800,800)

def x(t):
    return math.sin(t/12) * 220 + math.sin(t/15) * 100

def y(t):
    return math.cos(t / 10) * 130 + math.cos(t / 13) * 200

start = random.randint(0,9999999)

canvas.fill(sketcher.Ink('simplex_gradient', color=(200,200,200)))
ink = sketcher.Ink(color=(200,200,200))

for i in range(3000):
    t = start + i
    canvas.rect((canvas.width/2+x(t/15),canvas.height/2+y(t/15)), 2, 2, ink)

canvas.show()
