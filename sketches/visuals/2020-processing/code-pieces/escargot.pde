void setup() {
  size(600, 600);
}

void draw() {
  background(240);
  fill(240);
  noFill();

  int[] reds = {85, 201};
  int[] greens = {118, 204};
  int[] blues = {153, 230};

  float c1x = width/2;
  float c1y = height/2;
  float c1c = 500;
  float c1s = 10;

  float c2x = width/2 + 100;
  float c2y = height/2 - 50;
  float c2c = 200;
  float c2s = 6;

  float c3x = width/2 + 80;
  float c3y = width/2 - 40;
  float c3c = 35;

  float noiseStartR = random(7);
  float noiseStartG = random(7);
  float noiseStartB = random(7);

  drawNoiseRect(0, 0, width, height, 0.002, 201, 204, 230, 70, noiseStartR, noiseStartG, noiseStartB);

  for (int i = 0; i < c1s; i++) {
    float x = map(i, 0, c1s, c1x, c2x);
    float y = map(i, 0, c1s, c1y, c2y);
    float c = map(i, 0, c1s, c1c, c2c);
    int pick = i % 2;
    drawCircle(x, y, 0, c/2, 0, 360, 0.3, 0.002, reds[pick], greens[pick], blues[pick], 70, noiseStartR, noiseStartG, noiseStartB);
  }

  for (int i = 0; i < c2s; i++) {
    float x = map(i, 0, c2s, c2x, c3x);
    float y = map(i, 0, c2s, c2y, c3y);
    float c = map(i, 0, c2s, c2c, c3c);
    int pick = i % 2;
    drawCircle(x, y, 0, c/2, 0, 360, 0.3, 0.002, reds[pick], greens[pick], blues[pick], 70, noiseStartR, noiseStartG, noiseStartB);
  }

}

void drawCircle(float cX, float cY, float startRadius, float endRadius, float startAngle, float endAngle, float cStep, float noiseScale, int red, int green, int blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  //looping through distances from the centre
  for (float h = startRadius; h <= endRadius; h++) {
  // now figure out the circumference at this point
  // so we can draw the right amount of pixels
  // (this still doesn't quite work, can be levelled out with the cStep argument)
  float circumference = (endRadius * 2) * PI;
  // figuring out which points we want to start on
  float startC = map(startAngle, 0, 360, 0, circumference);
  float endC = map(endAngle, 0, 360, 0, circumference);
    for (float c = startC; c <= endC; c+= cStep) {
      // but we need to convert point in the circumference to an angle now
      // which we can do pretty quickly with mapping
      float angle = map(c, 0, circumference, 0, 360);
      float opposite = sin(radians(angle)) * h;
      float adjacent = cos(radians(angle)) * h;
      // now affecting colour based on noise of x and y
      float rNoise = noise(((cX + adjacent)*noiseScale)+noiseRStart, ((cY+opposite)*noiseScale)+noiseRStart);
      float gNoise = noise(((cX + adjacent)*noiseScale)+noiseGStart, ((cY+opposite)*noiseScale)+noiseGStart);
      float bNoise = noise(((cX + adjacent)*noiseScale)+noiseBStart, ((cY+opposite)*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      stroke(rColour, gColour, bColour);
      point(cX + adjacent, cY + opposite);
    }
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
