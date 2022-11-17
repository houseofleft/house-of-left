import sketcher
import random

canvas = sketcher.Canvas(700, 700)
colors = [(12,11,6),(240,203,71),(58,135,163),(235,177,176),(244,238,224),(200,38,49)]

num_x = random.randint(2,15)
num_y = random.randint(2,15)


x_points = [random.randint(0,canvas.width/20)*20 for i in range(num_x)]
y_points = [random.randint(0,canvas.height/20)*20 for i in range(num_y)]


noise_seeds = [random.randint(0,999) for i in range(3)]

for x in x_points:
    last_y = 0
    while last_y <= canvas.height:
        next_y = last_y + (random.randint(1,5) * 20)
        color = random.choice(colors)
        line_tone = sketcher.Ink(color=color,weight=20)
        canvas.line((x,last_y),(x,next_y), ink=line_tone)
        last_y = next_y

for y in y_points:
    last_x = 0
    while last_x <= canvas.height:
        next_x = last_x + (random.randint(1,5) * 20)
        color = random.choice(colors)
        line_tone = sketcher.Ink(color=color,weight=20)
        canvas.line((last_x,y),(next_x,y), ink=line_tone)
        last_x = next_x

for x in x_points:
    for y in y_points:
        color = random.choice(colors)
        canvas.line((x,y),(x+1,y),ink=sketcher.Ink(color=color,weight=20))



canvas.save('carousel-{}.png'.format(str(random.randint(1,999999))))
canvas.show()

