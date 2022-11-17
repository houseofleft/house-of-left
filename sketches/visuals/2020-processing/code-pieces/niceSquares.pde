void setup() {
  size(600, 600);
}

void draw() {
  background(240);
  float r = random(7);
  float g = random(7);
  float b = random(7);
  //drawNoiseRect(0, 0, width/2, height/2, 0.002, 100, 210, 270, 200, r, g, b);
  //drawNoiseRect(width/2, 0, width/2, height/2, 0.002, 143, 13, 134, 200, r, g, b);
  //drawNoiseRect(0, height/2, width/2, height/2, 0.002, 231, 213, 43, 200, r, g, b);
  //drawNoiseRect(width/2, height/2, width/2, height/2, 0.002, 243, 21, 43, 200, r, g, b);
  int splits = int(random(10));
  for (int i = 0; i < splits; i++) {
    for (int ii = 0; ii < splits; ii++) {
      drawNoiseRect(int(width/splits * i), int(width/splits * ii), int(width/splits), int(width/splits), 0.002, int(random(256)), int(random(256)), int(random(256)), 200, r, g, b);
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
