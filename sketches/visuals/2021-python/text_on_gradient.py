import shades
from PIL import ImageDraw
from PIL import ImageFont

canvas = shades.Canvas()
gradient = gradient = shades.NoiseGradient(
    color=(50,150,250),
    noise_fields = [shades.NoiseField(scale=0.002) for i in range(3)],
    color_variance=70,
)
margin = 10
gradient.rectangle(
    canvas,
    (margin, margin),
    canvas.width - margin*2,
    canvas.height - margin*2,
)

draw = ImageDraw.Draw(canvas)
font_size = 90
free_sans = ImageFont.truetype('FreeSansBold.ttf', font_size)
haiku = [
    "A logical",
    "place, upon",
    "this point",
    "of time and",
    "thus, the",
    "conception",
]
haiku.reverse()

total_height = 0
for i in range(len(haiku)):
    line = haiku[i]
    width, height = free_sans.getsize(line)
    x = canvas.width - width - 20
    y = canvas.width - font_size*(i+1) - 10
    draw.text((x, y), line, font=free_sans, fill=(240,240,240))

canvas.show()
