"""
Riley 2023

Expected arguments: output-file, width (px), height (px)
"""
import sys
import random

import shades

output_file, width, height = sys.argv[1:]

# messing with the variables, and weighting colors
pallete = [
    (33, 80, 169), # blue
    (90, 126, 165), # light blue
    (68, 163, 81), # green
    (255, 199, 52), # yellow
    (219, 207, 177), # beige
    (189, 189, 186), # grey
    (232, 99, 98), # pink
]
pallete_weights = [random.random() for i in range(len(pallete))]

canvas = shades.Canvas(height, width)
ink = shades.BlockColor()

grid_width = random.randint(1, 100)
grid_height = random.randint(1, 50)
grid_offset = int(grid_height/random.choice([1, 2, 4]))
grid_height = grid_offset * 2 # ensuring exact division
                  
def pick_two_colors():
    # lets make sure we return a single block fairly often
    if random.random() < 0.25:
        color = random.choices(pallete, weights=pallete_weights)[0]
        return [color, color]
    return random.choices(pallete, weights=pallete_weights, k=2)

block_size = 6


for j, x in enumerate(range(-grid_width, canvas.width+grid_width, grid_width)):
    for i, y in enumerate(range(-grid_height-grid_offset, canvas.height+grid_height+grid_offset, grid_height)):
        if (i + j) % block_size == 0:
            two_colors = pick_two_colors()
        ink.color = two_colors[i % 2]
        ink.shape(
            canvas,
            [(x, y + grid_offset),
            (x + grid_width, y - grid_offset),
            (x + grid_width, y + grid_height - grid_offset),
            (x, y + grid_height + grid_offset)],
        )

canvas.save(output_file)
