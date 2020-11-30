import sketcher
from PIL import Image
import random

pic = Image.open('c.jpg')

pic = sketcher.shuffle_image(pic, 20, 20)

pic.show()
pic.save('pic{}.png'.format(random.randint(1,9999)))
