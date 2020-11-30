from  sketcher import *
import random

def shift(color, shift):
    return tuple([int(c + random.uniform(-shift,shift)) for c in color])

canvas = Canvas(1200, 1200)

noise_seeds = [random.randint(0,999) for i in range(0,3)]
color = (240, 240, 240)

warp = Ink('simplex_gradient',color=color, c_var=50, noise_seeds=noise_seeds, noise_scale=0.01, recursion=1, feedback=0.5)

canvas.fill(warp)
canvas.show()
