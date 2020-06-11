void haze(float noiseScaleX, float noiseScaleY, float noiseStart, float red, float green, float blue) {
  // this function runs covers the entire draw area with a single colour of varying opacity (based on perlin noise)
  // looping through x and y
  for (float x = 0; x < width; x++) {
    for (float y = 0; y < height; y++) {
      // now affecting colour based on noise of x and y
      float monoNoise = noise((x*noiseScaleX)+noiseStart, (y*noiseScaleY)+noiseStart);
      float monoColour = map(monoNoise, 0, 1, 0, 255);
      monoColour = max(0, monoColour);
      monoColour = min(255, monoColour);
      stroke(red, green, blue, monoColour);
      // finally making point on canvas
      point(x, y);
    }
  }
}
