import random
from shades import *

canvas = Canvas(700, 700)

noise_fields = [NoiseField(scale = 0.003) for i in range(3)]
blue = NoiseGradient(color = (162, 188, 156), noise_fields = noise_fields)
purple = NoiseGradient(color = (234, 215, 166), noise_fields = noise_fields)

grid_size = 100

for x in range(0, canvas.width, grid_size):
    for y in range(0, canvas.height, grid_size):
        shades = [blue, purple]
        shade_one = random.choice(shades)
        shade_two = random.choice(shades)
        shade_one.rectangle(canvas, (x,y), grid_size, grid_size)
        option = random.choice(['tl', 'bl', 'tr', 'br'])
        if option == 'tl':
            shade_two.diet_pizza_slice(canvas, (x,y), grid_size, 90, 90)
        elif option == 'bl':
            shade_two.pizza_slice(canvas, (x,y+grid_size), grid_size, 0, 90)
        elif option == 'tr':
            shade_two.pizza_slice(canvas, (x+grid_size,y), grid_size, 180, 90)
        elif option == 'br':
            shade_two.pizza_slice(canvas, (x+grid_size, y+grid_size), grid_size, 270, 90)


canvas.show()
