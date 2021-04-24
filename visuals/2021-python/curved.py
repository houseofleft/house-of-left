import shades
import random

class noise(shades.Shade):
    def determine_shade(self, xy):
        if self.warp_noise[0].noise(xy) < random.uniform(*self.rand_range):
            self.transparency = 1
        else:
            self.transparency = 0
        return self.color


canvas = shades.Canvas(1200, 1200)
colors = [(0, 43, 89), (249, 223, 29), (84, 145, 150), (173, 176, 163), (72, 172, 157), (50, 111, 164), (171, 190, 208), (159, 132, 63), (83, 127, 177)]
inks = []

for c in colors:
    ink = noise(c, warp_noise=[shades.NoiseField(scale=0.001) for i in range(2)])
    ink.rand_range = [random.uniform(0, 0.8), 1]
    inks.append(ink)

random.shuffle(inks)

margin = canvas.width/3

for ink in inks:
    ink.rectangle(canvas, (margin, 0), canvas.width-margin, margin)
    ink.rectangle(canvas, (0, margin), canvas.width, canvas.height-margin*2)
    ink.rectangle(canvas, (0, canvas.width-margin), canvas.width-margin, margin)
    ink.pizza_slice(canvas, (margin, margin), margin, 270, 90)
    ink.pizza_slice(canvas, (canvas.width-margin, canvas.height-margin), margin, 90, 90)

canvas.show()
