from sketcher import *
import random


def pick_colour():
  colours = [(24,16,27),(14,164,177),(14,164,177),(247,204,135),(254,233,0),(249,180,183),(249,180,183),(249,180,183),(1,35,116)]
  var = 0
  colour = random.choice(colours)
  return (colour[0] + random.randint(-var,var),colour[1] + random.randint(-var,var),colour[2] + random.randint(-var,var))


def rythm(y):
  height = units * random.randint(1,3)
  width = units * random.randint(1,4)
  spacing = width * random.randint(0,5)
  placement = spacing
  fill = Ink(color=pick_colour())

  while placement < canvas.width:
    canvas.rect((placement, y), width, height, fill)
    placement += width + spacing

canvas = Canvas(500, 500)
units = 50

for i in range(10):
    canvas.fill(Ink(color=(241, 225, 206)))

    for i in range(150):
        rythm(units * random.randint(0,canvas.height/units))
    
    canvas.save('modular-{}.png'.format(str(random.randint(1,9999999))))
