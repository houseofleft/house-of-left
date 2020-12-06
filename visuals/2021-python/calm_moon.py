import shades

canvas = shades.Canvas(700, 700)

line = shades.BlockColor((240,240,240))
top = shades.VerticalGradient([((255, 178, 0), 300), ((240, 240, 240), 50)])
bottom = shades.VerticalGradient([((145, 161, 219), 300), ((131, 104, 151), canvas.height)])

vertical_border = canvas.height * 1/10
horizontal_border = canvas.width / 5

shape_height = canvas.height - (vertical_border * 2)
shape_width = canvas.width - (horizontal_border * 2)

top.rectangle(canvas, (horizontal_border, vertical_border), shape_width, shape_width * 2/3)
bottom.rectangle(canvas, (horizontal_border, vertical_border + (shape_width * 2/3)), shape_width, shape_height - shape_width * 2/3)

line.circle_outline(canvas, (canvas.width/2, canvas.height - vertical_border*4), shape_width / 2 * 4/5)

canvas.show()
