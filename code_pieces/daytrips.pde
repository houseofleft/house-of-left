void setup() {
  size(600, 600);
}

void draw() {

  //background

  background(240);

  float starterBack = random(7);
  gradientRectMessed(0, 0, width, height, 0.008, 0.004, 240, 40, starterBack);
  gradientRectMessed2(0, 0, width, height, 0.008, 0.004, -100, 250, starterBack);


  // main line

  float starterOne = random(7);
  float starterTwo = random(7);
  float pointOne = random(height);
  float pointTwo = random(height);

  for (int i = 0; i < 5; i++) {
    fill(95, 160, 207, random(100));
    squiggle(-width, pointOne, width*2, pointTwo, 4, 2, 300, 0.02, 0.002, starterOne + random(-0.02, 0.002), starterTwo + random(-0.02, 0.002));
  }

  fill(95, 160, 207);
  squiggle(-width, pointOne, width*2, pointTwo, 3, 0, 300, 0.02, 0.002, starterOne, starterTwo);

}

void gradientRectMessed(float xLocation, float yLocation, float rectWidth, float rectHeight, float noiseScaleX, float noiseScaleY, float mono, float cVar, float noiseStart) {
  // looping through x and y
  for (float x = xLocation; x < (xLocation + rectWidth); x += 1) {
    for (float y = yLocation; y < (yLocation + rectHeight); y += 1) {
      // now affecting colour based on noise of x and y
      float monoNoise = noise((x*noiseScaleX)+noiseStart, (y*noiseScaleY)+noiseStart);
      float monoColour = map(monoNoise, 0, 1, max(0, mono-cVar), min(255, mono+cVar));
      stroke(monoColour);
      // finally making point on canvas
      point(x, y);
    }
  }
}

void gradientRectMessed2(float xLocation, float yLocation, float rectWidth, float rectHeight, float noiseScaleX, float noiseScaleY, float mono, float cVar, float noiseStart) {
  // looping through x and y
  for (float x = xLocation; x < (xLocation + rectWidth); x += 1) {
    for (float y = yLocation; y < (yLocation + rectHeight); y += 1) {
      // now affecting colour based on noise of x and y
      float monoNoise = noise((x*noiseScaleX)+noiseStart, (y*noiseScaleY)+noiseStart);
      float monoColour = map(monoNoise, 0, 1, max(0, mono-cVar), min(255, mono+cVar));
      stroke(255, 0, 0, monoColour);
      // finally making point on canvas
      point(x, y);
    }
  }
}
