"""
Take the A Train 2021

Expected arguments: output_file, width, height

"""
import sys
from random import choice, randint

import shades

output_file, width, height = sys.argv[1:]

canvas = shades.Canvas(height, width, color=(249, 241, 228))
ink = shades.BlockColor()
units = 50

palletes = [
    [(27, 26, 23), (240, 165, 0), (228, 88, 38), (230, 213, 183)],
    [(84, 99, 255), (236, 236, 236), (255, 195, 0), (255, 24, 24)],
    [(255, 211, 45), (0, 142, 137), (8, 94, 125), (8, 69, 148)],
    [(21, 114, 161), (154, 208, 236), (239, 218, 215), (227, 190, 198)],
    [(150, 206, 180), (255, 238, 173), (217, 83, 79), (255, 173, 96)],
    [(0, 255, 255), (255, 0, 255), (255, 255, 0)],
    [(250, 0, 0), (0, 255, 0), (0, 0, 255)],
]
pallete = choice(palletes)

def pick_colour():
  var = 10
  colour = choice(pallete)
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

canvas.save(output_file)
