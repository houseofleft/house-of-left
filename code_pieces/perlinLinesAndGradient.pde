void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(255);
  drawNoiseRect(0, 0, width, height, 0.002, 124, 224, 219, 100, random(7), random(7), random(7));

  int thickness = 1;
  float thicknessWack = 0.9;
  float movementWack = 200;
  float thicknessScale = 0.004;
  float movementScale = 0.002;
  float firstStarter1 = random(7);
  float firstStarter2 = random(7);
  float secondStarter1 = random(7);
  float secondStarter2 = random(7);
  float thirdStarter1 = random(7);
  float thirdStarter2 = random(7);
  float yStartPosition = random((height*3)/5, (height*4)/5);

  for (float y = yStartPosition; y < height*2; y += random(1, 5)) {

    int cV = 60;
    fill(max(0, 218+random(-cV, cV)), max(0, 80+random(-cV, cV)), max(0, 170+random(-cV, cV)));

    squiggle(
               int(y),
               thickness,
               thicknessWack+random(-0.3, 0.3),
               movementWack,
               thicknessScale,
               movementScale,
               firstStarter1,
               firstStarter2
    );

  }
}

void squiggle(
  int y,
  float thickness,
  float thicknessWack,
  float movementWack,
  float thicknessScale,
  float movementScale,
  float thicknessStart,
  float movementStart) {

  // drawing line through x iterations

  float positionNoiseCount = movementStart;
  float thicknessNoiseCount = thicknessStart;

  for (int x = 0; x <= width; x ++) {
    noStroke();

    float noiseMovement = map(noise(positionNoiseCount), 0, 1, -movementWack, movementWack);
    float noiseSize = map(noise(thicknessNoiseCount), 0, 1, 1 - thicknessWack, 1 + thicknessWack);

    circle(x,y+noiseMovement, thickness*noiseSize);

    positionNoiseCount += movementScale;
    thicknessNoiseCount += thicknessScale;
  }

}

void drawNoiseRect(int xLocation, int yLocation, int rectWidth, int rectHeight, float noiseScale, int red, int green, int blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  for (int x = xLocation; x < (xLocation + rectWidth); x += 1) {
    for (int y = yLocation; y < (yLocation + rectHeight); y += 1) {
      // now affecting colour based on noise of x and y
      float rNoise = noise((x*noiseScale)+noiseRStart, (y*noiseScale)+noiseRStart);
      float gNoise = noise((x*noiseScale)+noiseGStart, (y*noiseScale)+noiseGStart);
      float bNoise = noise((x*noiseScale)+noiseBStart, (y*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      stroke(rColour, gColour, bColour);
      point(x, y);
    }
  }
}
