from PIL import Image
import itertools
import random
from opensimplex import OpenSimplex
import math
import glob

def mapped_noise(input_noise, xy, floor, ceiling, recursion=0, feedback=1):
    '''returns the simplex noise from xy coordinates.
    takes as arguments:
        input_noise: OpenSimplex noise object
        xy: x,y cordinates in form of tuple (x,y)
        floor: lowest possible return value
        ceiling: highest possible return value'''
    # base case - recursion is 0 or less
    if recursion <= 0:
        noise = (input_noise.noise2d(xy[0],xy[1])+1)/2
        noise *= abs(ceiling-floor)
        noise += floor
        return noise
    else:
        return mapped_noise(input_noise, (xy[0] + mapped_noise(input_noise, xy, floor, ceiling, recursion-1, feedback) * feedback, xy[1] + mapped_noise(input_noise, xy, floor, ceiling, recursion-1, feedback) * feedback), floor, ceiling, 0, feedback)

def adjust_point(xy, noise_seeds=[0,0], noise_scale=0.002, noise_size=30):
    x = mapped_noise(OpenSimplex(noise_seeds[0]), (xy[0]*noise_scale,xy[1]*noise_scale),xy[0]-noise_size,xy[0]+noise_size)
    y = mapped_noise(OpenSimplex(noise_seeds[1]), (xy[0]*noise_scale,xy[1]*noise_scale),xy[1]-noise_size,xy[1]+noise_size)
    return (x,y)

class Ink:
    
    def __init__(self, ink_type='block', color=(0,0,0), color_2 = (0,0,0), c_var=50, noise_scale=0.002, noise_seeds=[0,0,0], axis=0, warp_seeds=[0,0], warp_scale=0, warp_size=0, recursion=0, feedback=1, weight=1, transparency=0):
        # to do: put in assert for ink_types ['block', 'simplex_gradient', 'linear_gradient']
        self.ink_type = ink_type
        self.color = color
        self.color_2 = color_2
        self.weight = weight
        self.c_var = c_var
        self.noise_scale = noise_scale
        self.noise = [OpenSimplex(n) for n in noise_seeds]
        self.axis = axis
        self.warp_noise = [OpenSimplex(w) for w in warp_seeds]
        self.warp_scale = warp_scale
        self.warp_size = warp_size
        self.recursion = recursion
        self.feedback = feedback
        self.transparency = transparency

    def decide_color(self, xy, canvas):
        '''determines the color for xy coordinates based on ink type.
        takes as arguments:
            xy: xy coordinates in the form of a tuple (x,y)'''
        if self.ink_type == 'block':
            return self.color
        elif self.ink_type == 'simplex_gradient':
            color = [0,0,0]
            for i in range(0,3):
                affected_color = mapped_noise(self.noise[i], (xy[0]*self.noise_scale,xy[1]*self.noise_scale), self.color[i] - self.c_var, self.color[i] + self.c_var, self.recursion, self.feedback)
                color[i] = max(min(int(affected_color),255),0)
            return tuple(color)
        elif self.ink_type == 'linear_gradient':
            through = xy[self.axis] / [canvas.width, canvas.height][self.axis]
            color = [0,0,0]
            for i in range(0,3):
                color[i] = int(self.color[i] + ((self.color_2[i] - self.color[i]) * through))
                color[i] = max(min(int(color[i]),255),0)
            return tuple(color)

    def apply_transparency(self, xy, color, canvas):
        initial_color = canvas.img.getpixel((int(xy[0]),int(xy[1])))
        new_color = [0,0,0]
        for i in range(0,3):
            new_color[i] = initial_color[i] + ((color[i] - initial_color[i]) * (1-self.transparency))
            new_color[i] = int(new_color[i])
        return tuple(new_color)

    def adjust_point(self, xy):
        if self.warp_scale == 0 or self.warp_size == 0:
            return xy
        else:
            x = mapped_noise(self.warp_noise[0], (xy[0]*self.warp_scale,xy[1]*self.noise_scale), xy[0]-self.warp_size, xy[0]+self.warp_size)
            y = mapped_noise(self.warp_noise[1], (xy[0]*self.warp_scale,xy[1]*self.noise_scale), xy[1]-self.warp_size, xy[1]+self.warp_size)
            return ((x,y))


    def point(self, canvas, xy):
        '''makes a point on a Canvas object.
        takes as arguments:
            canvas: a sketcher.Canvas object
            xy: xy coordinates in the form of a tuple (x,y)'''
        color = self.decide_color(xy, canvas)
        xy = self.adjust_point(xy)
        for x in range(int(xy[0]),int(xy[0]+self.weight)):
            for y in range(int(xy[1]),int(xy[1]+self.weight)):
                if canvas.point_in_canvas((x,y)):
                    if self.transparency != 0:
                        color = self.apply_transparency((x,y), color, canvas)
                    canvas.img.putpixel((int(x),int(y)),color)


class Canvas:

  def __init__(self, width, height):
    self.height = height
    self.width = width
    self.img = Image.new('RGB', (self.width, self.height), color=(255,255,255))

  def fill(self, ink=Ink()):
    for x in range(0, int(self.width)):
      for y in range(0, int(self.height)):
        ink.point(self, (x,y))

  def rect(self, xy, width, height, ink=Ink()):
    for x in range(int(xy[0]), int(xy[0] + width)):
      for y in range(int(xy[1]), int(xy[1] + height)):
        if self.point_in_canvas((x,y)):
          ink.point(self, (x,y))

  def circle(self, x_y, radius, start_radius=0, ink=Ink()):
    for h in range(int(start_radius), int(radius)):
      circumference = radius * 2 * math.pi
      for c in [x for x in range(0, (int(circumference)+1))]:
        angle = (c/circumference) * 360
        opposite = math.sin(math.radians(angle)) * h
        adjacent = math.cos(math.radians(angle)) * h
        ink.point(self, (x_y[0] + adjacent, x_y[1] + opposite))

  def line(self, xy1, xy2, ink=Ink()):
  # start by moving from 1 to 2
    # first figuring out which is biggest distance, that step will be one, so every pixel gets covered
    if abs(xy1[0] - xy2[0]) > abs(xy1[1] - xy2[1]):
      if xy1[0] > xy2[0]:
        x_step = -1
      else:
        x_step = 1
      if xy1[1] > xy2[1]:
        y_step = -1 * (abs(xy1[1]-xy2[1])/abs(xy1[0]-xy2[0]))
      else:
        y_step = abs(xy1[1]-xy2[1])/abs(xy1[0]-xy2[0])
      istop = abs(xy1[0] - xy2[0])
    else:
      if xy1[1] > xy2[1]:
        y_step = -1
      else:
        y_step = 1
      if xy1[0] > xy2[0]:
        x_step = -1 * (abs(xy1[0]-xy2[0])/abs(xy1[1]-xy2[1]))
      else:
        x_step = (abs(xy1[0]-xy2[0])/abs(xy1[1]-xy2[1]))
      istop = abs(xy1[1]-xy2[1])
    x = xy1[0]
    y = xy1[1]
    for i in range(0,int(istop)):
        ink.point(self, (x,y))
        x += x_step
        y += y_step
   
  def triangle(self, xy1, xy2, xy3, ink=Ink()):
    # start by moving from 1 to 2
    # first figuring out which is biggest distance, that step will be one, so every pixel gets covered
    if abs(xy1[0] - xy2[0]) > abs(xy1[1] - xy2[1]):
      if xy1[0] > xy2[0]:
        x_step = -1
      else:
        x_step = 1
      if xy1[1] > xy2[1]:
        y_step = -1 * (abs(xy1[1]-xy2[1])/abs(xy1[0]-xy2[0]))
      else:
        y_step = abs(xy1[1]-xy2[1])/abs(xy1[0]-xy2[0])
      istop = abs(xy1[0] - xy2[0])
    else:
      if xy1[1] > xy2[1]:
        y_step = -1
      else:
        y_step = 1
      if xy1[0] > xy2[0]:
        x_step = -1 * (abs(xy1[0]-xy2[0])/abs(xy1[1]-xy2[1]))
      else:
        x_step = (abs(xy1[0]-xy2[0])/abs(xy1[1]-xy2[1]))
      istop = abs(xy1[1]-xy2[1])
    # now we have our steps, we can draw a straight line between the two
    x = xy1[0]
    y = xy1[1]
    for i in range(0,int(istop)):
      # this is running across the line between xy1 and xy2
      # at each opint, we need to draw another line, between point xy and xy3
      if abs(x-xy3[0]) > abs(y-xy3[1]):
        if x > xy3[0]:
          x_step_2 = -1
        else:
          x_step_2 = 1
        if y > xy3[1]:
          y_step_2 = -1 * (abs(y-xy3[1])/abs(x-xy3[0]))
        else:
          y_step_2 = (abs(y-xy3[1])/abs(x-xy3[0]))
        istop2 = abs(x-xy3[0])
      else:
        if y > xy3[1]:
          y_step_2 = -1
        else:
          y_step_2 = 1
        if x > xy3[0]:
          x_step_2 = -1 * (abs(x-xy3[0])/abs(y-xy3[1]))
        else:
          x_step_2 = (abs(x-xy3[0])/abs(y-xy3[1]))
        istop2 = abs(y-xy3[1])
      
      x2 = x
      y2 = y

      for j in range(0,int(istop2)):
        self.rect((x2,y2),2,2,ink)
        x2 += x_step_2
        y2 += y_step_2
      
      x += x_step
      y += y_step

  def point_in_canvas(self, xy):
    return (xy[0] < self.width and xy[0] >= 0 and xy[1] < self.height and xy[1] >= 0)

  def point(self, canvas, xy):
    canvas.img.putpixel((int(xy[0]),int(xy[1])), self.img.getpixel((int(xy[0]), int(xy[1]))))

  def show(self):
    self.img.show()

  def save(self, file_name):
    self.img.save(file_name)

def shuffle_image(img, horizontal_pieces=5, vertical_pieces=5):
    copy = img
    x_coordinates = [x for x in range(0, img.width, int(img.width/horizontal_pieces))]
    y_coordinates = [y for y in range(0, img.height, int(img.height/vertical_pieces))]
    coordinates = [i for i in itertools.product(x_coordinates, y_coordinates)]
    shuffled_coordinates = coordinates.copy()
    random.shuffle(shuffled_coordinates)
    coordinate_pairs = [i for i in zip(coordinates, shuffled_coordinates)]
    for pair in coordinate_pairs:
        first = pair[0]
        second = pair[1]
        for x in range(0, int(img.width/horizontal_pieces)):
            for y in range(0, int(img.height/vertical_pieces)):
                try:
                    color = copy.getpixel((second[0]+x,second[1]+y))
                    img.putpixel((first[0]+x,first[1]+y),color)
                except:
                    pass
    return img
