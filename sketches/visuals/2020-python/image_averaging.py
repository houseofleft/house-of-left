from PIL import Image
import glob
import numpy as np

files = [f for f in glob.glob('*.jpg')]
pic_h = 700
pic_w = 300

images = [Image.open(f) for f in files]
average = Image.new('RGB', (pic_w,pic_h))

for x in range(0,pic_w):
    for y in range(0,pic_h):
        x_through = x/pic_w
        y_through = y/pic_h
        colours = []
        for i in images:
            width = i.width
            height = i.height
            colour = i.getpixel((width*x_through,height*y_through))
            colours.append(colour)
        average_colour = [0,0,0]
        for i in range(len(average_colour)):
            average_colour[i] = int(np.mean([c[i] for c in colours]))
        average.putpixel((x,y),tuple(average_colour)) 

average.show()
