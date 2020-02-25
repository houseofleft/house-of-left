void setup() {
  size(500, 500);
  noStroke();
  frameRate(0.2);
}

void draw() {
 background(255);
 drawNoiseRect(0, 0, width, height, 0.002, int(random(0, 255)));

}

void drawNoiseRect(int xLocation, int yLocation, int rectWidth, int rectHeight, float noiseScale, int colourDensity) {
  float countRx = random(10);
  float countGx = random(10);
  float countBx = random(10);
  float countRy = random(10);
  float countGy = random(10);
  float countBy = random(10);
  for (int x = xLocation; x < (xLocation + rectWidth); x += 1) {
    float countStartRy = countRy;
    float countStartGy = countGy;
    float countStartBy = countBy;
    for (int y = yLocation; y < (yLocation + rectHeight); y += 1) {
      stroke(map(noise(countRx, countRy), 0, 1, 0, 255), map(noise(countGx, countGy), 0, 1, 0, 255), map(noise(countBx, countBy), 0, 1, 0, 255), colourDensity);
      point(x, y);
      countRy += noiseScale;
      countGy += noiseScale;
      countBy += noiseScale;
    }
    countRx += noiseScale;
    countGx += noiseScale;
    countBx += noiseScale;
    countRy = countStartRy;
    countGy = countStartGy;
    countBy = countStartBy;
  }
}


void keyPressed() {  if (keyCode == ENTER) {saveFrame("gradient-####.jpg");}}
