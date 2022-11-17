import shades
import numpy as np

canvas = shades.Canvas(400, 400)

class Cloud(shades.Shade):

    def __init__(self, color, noise=shades.NoiseField(), air=0.3):
        super().__init__(color)
        self.cloud_noise = noise
        self.air = air

    def determine_shade(self, xy_coords):
        color = canvas.getpixel(xy_coords)
        noise = self.cloud_noise.noise(xy_coords) - 0.4
        noise = max(noise, 0)
        return shades.color_clamp([np.average([color[i], self.color[i]], weights=[0.5, noise*self.air]) for i in range(3)])

colors = [(250, 250, 0), (250, 0, 250), (0, 250, 250)]

np.random.shuffle(colors)
for color in colors:
    tone = Cloud(color, shades.NoiseField(scale=0.006))
    for x in range(0, canvas.width, 50):
        for y in range(0, canvas.height, 50):
            if np.random.random() > 0.1:
                tone.square(canvas, (x, y), 50)

canvas.show()
