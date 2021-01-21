import shades
import random

canvas = shades.Canvas()
shade_one = shades.BlockColor((102, 169, 193))
shade_two = shades.BlockColor((30, 86, 165))
shade_three = shades.BlockColor((236, 147, 155))
shade_four = shades.BlockColor((127, 89, 155))

def stack(start_coords, width, height, offset):
  perc = height/100
  shade_dict = {
    0: shade_one,
    random.randint(perc*33,perc*40): shade_two,
    random.randint(perc*46, perc*50): shade_three,
    random.randint(perc*75, perc*85): shade_four,
    perc*200: shade_one,
    }
  for y in range(int(start_coords[1]), int(start_coords[1]+height), 5):
    filtered_dict = {k: shade_dict[k] for k in shade_dict if k > y}
    color = filtered_dict[list(filtered_dict.keys())[0]]
    color.line(canvas, (start_coords[0], y), (start_coords[0] + width, y + offset), 1)

margin = 50
width = 20
gap = 5
tilt = random.randint(0,20)

for x in range(margin, canvas.width - margin - width, width + gap):
  stack((x, margin), width, canvas.height - (2 * margin), tilt)


canvas.show()
