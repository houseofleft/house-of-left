def asciify(image, ascii_width = 100, ascii_code = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "):

  '''
  asciify function to input image and output ascii text of image.
  width and ascii characters used are editable
  '''

  # modules
  from PIL import Image
  import re

  # importing image
  img = Image.open(image)

  # resizing and greyscaling
  width, height = img.size
  ascii_height = height * (ascii_width / width) * 0.66
  img = img.resize((ascii_width, int(ascii_height)))
  img = img.convert('L')

  # characters to be used in ascii
  characters = [i for i in ascii_code]
  pixels = img.getdata()

  # method is to put all pixels into scale between lightest and darkest, then pick out the corresponding on from the list on that basis
  lightest_pixel = min(pixels)
  pixels = [i - lightest_pixel for i in pixels]
  darkest_pixel = max(pixels)
  ascii = [characters[int(i/darkest_pixel*len(characters))-1] for i in pixels]
  import re
  ascii = re.sub("(.{" + str(ascii_width) + "})", "\\1\n", "".join(ascii), 0, re.DOTALL)

  return ascii
