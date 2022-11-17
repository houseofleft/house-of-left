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
    end = random.randint(1, 1500)
    ink = shades.BlockColor(color)

    for i in range(0, end, 2):
        t = start + i
        ink.line(canvas, (canvas.width/2 + x(t/15), canvas.height/2 + y(t/15)), (canvas.width/2 + x(t/12), canvas.height/2 + y(t/12)), 1)


draw_parametric((127, 160, 251))
draw_parametric((255,51,82))
draw_parametric((249,216,20))
canvas.show()
