import shades

canvas = shades.Canvas(1024, 929)

one = shades.BlockColor((200, 200, 200))
two = shades.BlockColor((100, 100, 100))
three = shades.BlockColor((150, 150, 150))

unit = canvas.width / 10

one.shape()
    canvas,
    [
        (425, 0),
        (580, 0),
        (1020, 780),
        (315, 780),
        (390, 645),
        (785, 650)
    ]
)

canvas.show()
