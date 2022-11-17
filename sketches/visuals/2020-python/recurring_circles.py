import sketcher

canvas = sketcher.Canvas(700,700)
spacing = 12

canvas.fill(sketcher.Ink(color=(100,100,100)))

for i in range(spacing,int(canvas.width),spacing):
    canvas.circle((canvas.width/2, canvas.height/2), i, i-1, sketcher.Ink(warp_scale=0.008, warp_size=i*0.4))

canvas.show()
