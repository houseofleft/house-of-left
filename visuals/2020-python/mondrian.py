import sketcher
import random

canvas = sketcher.Canvas(500, 500)
colors = [(59,78,148),(185,63,34),(210,180,10)]

num_x = random.randint(2,4)
num_y = random.randint(2,4)


x_points = [random.randint(0,canvas.width) for i in range(num_x)]
y_points = [random.randint(0,canvas.height) for i in range(num_y)]

x_points.append(-10)
x_points.append(canvas.width+10)
y_points.append(-10)
y_points.append(canvas.height+10)

for x in x_points:
    for y in y_points:
        # first find the nearest x point, and use to decide width
        try:
            canvas.line((0,y),(canvas.width,y), ink=sketcher.Ink(color=(40,40,40),weight=4))
            next_x = [p for p in x_points if x < p]
            next_x.sort()
            next_x = next_x[0]
            next_y = [p for p in y_points if y < p]
            next_y.sort()
            next_y = next_y[0]
            width = next_x - x
            height = next_y - y
            if random.randint(0,3) == 0:
                color = random.choice(colors)
            else:
                color = (240,240,240)
            canvas.rect((x,y),width,height,sketcher.Ink(color=color))
        except:
            pass

    canvas.line((x,0),(x,canvas.height), ink=sketcher.Ink(color=(40,40,40),weight=4))
canvas.show()
