import shades
from random import choice, randint

canvas = shades.Canvas(color=(249, 241, 228))
ink = shades.BlockColor()
units = randint(1,6) * 25

def pick_colour():
  colours = [
    (233, 80, 62),
    (76, 111, 190),
    (252, 218, 0),
    (0, 142, 41),
    (249, 241, 228),
    (204, 195, 175),
  ]
  var = 0
  colour = choice(colours)
  return shades.color_clamp((colour[0] + randint(-var,var),colour[1] + randint(-var,var),colour[2] + randint(-var,var)))

def rythm(y):
  height = units * randint(1,3)
  width = units * randint(1,4)
  spacing = width * randint(0,5)
  placement = spacing
  ink.color = pick_colour()

  while placement < canvas.width:
    ink.rectangle(canvas, (placement, y), width, height)
    placement += width + spacing

for i in range(200):
    rythm(units * randint(0,canvas.height/units))

canvas.show()
