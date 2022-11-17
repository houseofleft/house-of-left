import shades

canvas = shades.Canvas(1000, 907)

def units(n):
    return n * (canvas.width / 205)

central_color = (200, 200, 200)

one = shades.NoiseGradient(
    color=central_color,
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)]
)

two = shades.NoiseGradient(
    color=central_color,
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)]
)

three = shades.NoiseGradient(
    color=central_color,
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)]
)

fill = shades.NoiseGradient(
    color=central_color,
    noise_fields=[shades.NoiseField(scale=0.001) for i in range(3)]
)

fill.fill(canvas)

one.shape(
    canvas,
    [
        (units(87), units(1)),
        (units(116), units(1)),
        (units(204), units(156)),
        (units(157), units(129)),
    ]
)

one.shape(
    canvas,
    [
        (units(63), units(156)),
        (units(78), units(129)),
        (units(157), units(129)),
        (units(204), units(156)),
    ]
)

two.shape(
    canvas,
    [
        (units(103), units(85)),
        (units(87), units(56)),
        (units(16), units(185)),
        (units(63), units(156)),
    ]
)

two.shape(
    canvas,
    [
        (units(16), units(185)),
        (units(190), units(185)),
        (units(204), units(156)),
        (units(63), units(156)),
    ]
)

three.shape(
    canvas,
    [
        (units(16), units(185)),
        (units(1), units(156)),
        (units(87), units(1)),
        (units(87), units(56)),
    ]
)

three.shape(
    canvas,
    [
        (units(87), units(1)),
        (units(158), units(129)),
        (units(126), units(129)),
        (units(87), units(56)),
    ]
)

canvas.show()
