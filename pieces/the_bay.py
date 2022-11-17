"""
The Bay 2022

Expected arguments: output-file, width (px), height (px)

"""
import sys
import random

from shades import *

output_file, width, height = sys.argv[1:]

canvas = Canvas(height, width)

class NoiseyGradient(Shade):
    def __init__(
        self,
        color: Tuple[int, int, int] = (0, 0, 0),
        warp_noise: Tuple[NoiseField, NoiseField, NoiseField] = noise_fields(channels=3),
        warp_size: int = 0,
        color_variance: int = 70,
        color_fields: Tuple[NoiseField, NoiseField] = noise_fields(channels=3),
        fuzz: int = 90,
    ):
        super().__init__(color, warp_noise, warp_size)
        self.color_variance = color_variance
        self.color_fields = tuple(color_fields)
        self.fuzz = fuzz

    def determine_shade(self, xy_coords: Tuple[int, int]) -> Tuple[int, int, int]:
        def apply_noise(i):
            noise = self.color_fields[i].noise(xy_coords) - 0.5
            color_affect = noise * (2*self.color_variance)
            return self.color[i] + color_affect + random.randint(-self.fuzz, self.fuzz)
        return color_clamp([apply_noise(i) for i in range(len(self.color))])


noisey_gradient = NoiseyGradient(
    [random.randint(150, 255) for i in range(3)],
    color_fields=noise_fields(channels=3, scale=0.001),
    fuzz=70,
)
noisey_gradient.fill(canvas)

canvas.save(output_file)
