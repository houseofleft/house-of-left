import shades
import math
import random

canvas = shades.Canvas(800,800)

def draw_parametric(color):
    div1 = random.randint(8,16)
    div2 = random.randint(8,16)
    div3 = random.randint(8,16)
    div4 = random.randint(8,16)
    mul1 = random.randint(100, 250)
    mul2 = random.randint(100, 250)
    mul3 = random.randint(100, 250)
    mul4 = random.randint(100, 250)

    def x(t):
        return math.sin(t / div1) * mul1 + math.sin(t / div2) * mul2

    def y(t):
        return math.cos(t / div3) * mul3 + math.cos(t / div4) * mul4

    start = random.randint(0,9999999)
    end = random.randint(1, 2000)
    ink = shades.BlockColor(color)
    go = True

    for i in range(0, end, 1):
        if go:
            t = start + i
            ink.circle(canvas, (canvas.width/2 + x(t/15), canvas.height/2 + y(t/15)), 1)
        if random.randint(0,200) == 77:
            go = not go

for i in range(10):
    draw_parametric((127, 160, 251))
    draw_parametric((255,51,82))
    draw_parametric((249,216,20))
canvas.show()
