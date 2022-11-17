import shades

canvas = shades.Canvas()
ink = shades.BlockColor(color=(0,255, 255), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)
ink2 = shades.BlockColor(color=(255, 0, 255), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)
ink3 = shades.BlockColor(color=(255, 255, 0), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)
ink4 = shades.BlockColor(color=(0,255, 255), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)
ink5 = shades.BlockColor(color=(255, 0, 255), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)
ink6 = shades.BlockColor(color=(255, 255, 0), transparency=0.6, warp_noise=[shades.NoiseField(0.002) for i in range(2)], warp_size=30)

for x in range(-30, canvas.width+30, 5):
    for y in range(-30, canvas.height+30, 5):
        ink.line(canvas, (x,y), (x, y+3))
        ink2.line(canvas, (x,y), (x, y+3))
        ink3.line(canvas, (x,y), (x, y+3))
        ink4.line(canvas, (x,y), (x, y+3))
        ink5.line(canvas, (x,y), (x, y+3))
        ink6.line(canvas, (x,y), (x, y+3))

canvas.show()
