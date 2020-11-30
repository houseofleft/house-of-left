void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(240);

  gradientRectMessed2(0, 0, width, height, 0.003, 0.003, -100, 250, random(7), 0, 255, 255);
  gradientRectMessed2(0, 0, width, height, 0.003, 0.003, -100, 250, random(7), 255, 0, 255);
  gradientRectMessed2(0, 0, width, height, 0.003, 0.003, -100, 250, random(7), 255, 255, 0);

}


void gradientRectMessed2(float xLocation, float yLocation, float rectWidth, float rectHeight, float noiseScaleX, float noiseScaleY, float mono, float cVar, float noiseStart, float red, float green, float blue) {
  // looping through x and y
  for (float x = xLocation; x < (xLocation + rectWidth); x++) {
    for (float y = yLocation; y < (yLocation + rectHeight); y++) {
      // now affecting colour based on noise of x and y
      float monoNoise = noise((x*noiseScaleX)+noiseStart, (y*noiseScaleY)+noiseStart);
      float monoColour = map(monoNoise, 0, 1, max(0, mono-cVar), min(255, mono+cVar));
      stroke(red, green, blue, monoColour);
      // finally making point on canvas
      point(x, y);
    }
  }
}
