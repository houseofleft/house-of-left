from sketcher import *
import random

canvas = Canvas(800, 800)

fill1 = Ink('simplex_gradient',(241,198,183), noise_scale=0.004, noise_seeds=[random.randint(0,999) for i in range(3)])
fill2 = Ink('simplex_gradient',(152,157,186), noise_scale=0.004,noise_seeds=[random.randint(0,999) for i in range(3)])
fill3 = Ink('simplex_gradient',(107,127,161), noise_scale=0.004,noise_seeds=[random.randint(0,999) for i in range(3)])

fills = [fill1,fill2,fill3]

margin = 50
size = 20

x = margin
while x <= canvas.width:
    y = margin
    while y <= canvas.height:
        if random.randint(0,99) < 70:
            canvas.circle((x+size/2,y+size/2),size/2, random.choice(fills))
        y += margin + size
    x += margin + size

canvas.show()
