void setup() {
  size(600, 600);
  frameRate(2);
}

void draw() {

  drawNoiseRect(0, 0, width, height, 0.002, 5, 122, 170, 70);

  int gridSize = int(random(20, 70));
  int glyphSize = int(random(5, 12));

  for (int x = -gridSize; x < width + gridSize; x += gridSize) {
    for (int y = -gridSize; y < height + gridSize; y += gridSize) {
      squareGlyph(x, y, glyphSize);
    }
  }
}

void drawNoiseRect(int xLocation, int yLocation, int rectWidth, int rectHeight, float noiseScale, int red, int green, int blue, float cVar) {
  float noiseRStart = random(7);
  float noiseGStart = random(7);
  float noiseBStart = random(7);
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

void squareGlyph(int xLocation, int yLocation, int squareWidth) {
  //left
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation, yLocation + squareWidth);
  }
  //right
  if (random(1) > 0.6) {
  line(xLocation + squareWidth, yLocation, xLocation + squareWidth, yLocation + squareWidth);
  }
  //bottom
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation + squareWidth, yLocation);
  }
  //top
  if (random(1) > 0.6) {
  line(xLocation + squareWidth, yLocation + squareWidth, xLocation, yLocation + squareWidth);
  }
  //diagonal1
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation + squareWidth, yLocation + squareWidth);
  }
  //diagonal2
  if (random(1) > 0.6) {
  line(xLocation, yLocation + squareWidth, xLocation + squareWidth, yLocation);
  }
}
