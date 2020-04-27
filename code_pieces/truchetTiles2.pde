void setup() {
  size(1000, 1000);
}

void draw() {
  background(240);
  int gridSize = 80;
  float S11 = random(7);
  float S12 = random(7);
  float S13 = random(7);
  float S21 = random(7);
  float S22 = random(7);
  float S23 = random(7);
  for (int x = 0; x < width; x+=gridSize) {
    for (int y = 0; y < height; y+=gridSize) {
      truchetTile(x, y, gridSize, gridSize, S11, S12, S13, S21, S22, S23);
    }
  }
}

void gradientTriangle(float x1, float y1, float x2, float y2, float x3, float y3, float noiseScale, float red, float green, float blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  noStroke();
  // start by moving from 1 to 2
  float xStep, yStep, iStop;
  // first figure out which is biggest distance, that step will be one, so every pixel gets covered
  if (abs(x1-x2) > abs(y1-y2)) {
    if (x1 > x2) {xStep = -1;} else {xStep = 1;}
    if (y1 > y2) {yStep = -1 * (abs(y1-y2)/abs(x1-x2));} else {yStep = abs(y1-y2)/abs(x1-x2);}
    iStop = abs(x1-x2);
  } else {
    if (y1 > y2) {yStep = -1;} else {yStep = 1;}
    if (x1 > x2) {xStep = -1 * (abs(x1-x2)/abs(y1-y2));} else {xStep = abs(x1-x2)/abs(y1-y2);}
    iStop = abs(y1-y2);
  }
  // now we have our steps, we can draw a straight line between the two
  float x = x1;
  float y = y1;

  for (int i = 0; i < iStop; i++) {
    // this is running across the line between x1,y1 and x2,y2
    // at each point, we now need to draw ANOTHER line, between point x,y and x3,y3
    // basically repeating the exact code
    float xStep2, yStep2, iStop2;

    if (abs(x-x3) > abs(y-y3)) {
      if (x > x3) {xStep2 = -1;} else {xStep2 = 1;}
      if (y > y3) {yStep2 = -1 * (abs(y-y3)/abs(x-x3));} else {yStep2 = abs(y-y3)/abs(x-x3);}
      iStop2 = abs(x-x3);
    } else {
      if (y > y3) {yStep2 = -1;} else {yStep2 = 1;}
      if (x > x3) {xStep2 = -1 * (abs(x-x3)/abs(y-y3));} else {xStep2 = abs(x-x3)/abs(y-y3);}
      iStop2 = abs(y-y3);
    }

    float xAgain = x;
    float yAgain = y;

    for (int ii = 0; ii < iStop2; ii++) {
      // now affecting colour based on noise of x and y
      float rNoise = noise((xAgain*noiseScale)+noiseRStart, (yAgain*noiseScale)+noiseRStart);
      float gNoise = noise((xAgain*noiseScale)+noiseGStart, (yAgain*noiseScale)+noiseGStart);
      float bNoise = noise((xAgain*noiseScale)+noiseBStart, (yAgain*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      fill(rColour, gColour, bColour);
      // finally making point on canvas
      circle(xAgain, yAgain, 2);
      xAgain += xStep2;
      yAgain += yStep2;
    }

    x += xStep;
    y += yStep;
  }

}

void truchetTile(float x, float y, float height, float width, float S11, float S12, float S13, float S21, float S22, float S23) {

  float chance = random(1);

  if (chance > 0.75) {
    gradientTriangle(x, y, x+width, y, x+width, y+height, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S11, S12, S13);
    gradientTriangle(x, y, x, y+height, x+width, y+height, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S21, S22, S23);
   } else if (chance > 5) {
     gradientTriangle(x, y, x+width, y, x+width, y+height, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S21, S22, S23);
    gradientTriangle(x, y, x, y+height, x+width, y+height, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S11, S12, S13);
   } else if (chance > 0.25) {
    gradientTriangle(x, y+height, x+width, y+height, x+width, y, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S11, S12, S13);
    gradientTriangle(x, y+height, x, y, x+width, y, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S21, S22, S23);
   } else {
    gradientTriangle(x, y+height, x+width, y+height, x+width, y, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S21, S22, S23);
    gradientTriangle(x, y+height, x, y, x+width, y, 0.01, random(150, 250), random(150, 250), random(150, 250), 70, S11, S12, S13);
  }
}
