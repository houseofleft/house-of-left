import shades
import numpy as np

CANVAS = shades.Canvas(1000, 1000)

class Cloud(shades.Shade):

    def __init__(self, color, noise=shades.NoiseField(), air=0.3):
        super().__init__(color)
        self.cloud_noise = noise
        self.air = air

    def determine_shade(self, xy_coords):
        color = CANVAS.getpixel(xy_coords)
        noise = self.cloud_noise.noise(xy_coords)
        noise = max(noise, 0)
        return shades.color_clamp([np.average([color[i], self.color[i]], weights=[0.5, noise*self.air]) for i in range(3)])

colors = [(250, 0, 0), (0, 250, 0), (0, 0, 250)]
np.random.shuffle(colors)
for color in colors:
    tone = Cloud(color, shades.NoiseField(scale=0.001))
    tone.fill(CANVAS)

CANVAS.show()
