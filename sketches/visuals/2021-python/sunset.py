from shades import *

canvas = Canvas(700, 700)
points = [
    ( (114, 17, 221), 0 ),
    ( (129, 121, 211), 100 ),
    ( (222, 108, 160), 400 ),
    ( (255, 209, 90), 500 ),
    ( (255, 178, 0), 650 )
]
reversed = [
    ( (114, 17, 221), 650 ),
    ( (129, 121, 211), 500 ),
    ( (222, 108, 160), 400 ),
    ( (255, 209, 90), 100 ),
    ( (255, 178, 0), 0 )
]
vertical = VerticalGradient(points)
flipped = VerticalGradient(reversed)

vertical.fill(canvas)
flipped.circle(canvas, (350, 350), 300)

canvas.show()
