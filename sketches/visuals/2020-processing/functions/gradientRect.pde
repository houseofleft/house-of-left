// this function draws a rectangular colour gradient
// it takes as arguments:
// xLocation: location of top left corner of rectangle on x axis
// yLocation: location of top left corner of rectangle on y axis
// rectWidth: width of the rectangle
// rectHeight: height of the rectangle
// noiseScale: the scale of perlin noise (0.002 will give smooth gradient, 0.01 will look patterned)
// red, green, blue: "central" colour around which the gradient will be based
// cVar: how much the red, green and blue colours are allowed to vary from the "central" colour
// noiseRStart, noiseGStart, noiseBStart: starting points of perlin noise
void gradientRect(float xLocation, float yLocation, float rectWidth, float rectHeight, float noiseScale, float red, float green, float blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  // looping through x and y
  for (float x = xLocation; x < (xLocation + rectWidth); x += 1) {
    for (float y = yLocation; y < (yLocation + rectHeight); y += 1) {
      // now affecting colour based on noise of x and y
      float rNoise = noise((x*noiseScale)+noiseRStart, (y*noiseScale)+noiseRStart);
      float gNoise = noise((x*noiseScale)+noiseGStart, (y*noiseScale)+noiseGStart);
      float bNoise = noise((x*noiseScale)+noiseBStart, (y*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      stroke(rColour, gColour, bColour);
      // finally making point on canvas
      point(x, y);
    }
  }
}
