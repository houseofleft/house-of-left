void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(240);

  float gridSize = int(random(5, 50));
  int offsetCount = 0;
  float offset;
  float rStarter = random(7);
  float gStarter = random(7);
  float bStarter = random(7);
  float density = random(1);

  for (float y = -gridSize; y <= height + gridSize; y += gridSize) {
    for (float x = -gridSize; x <= width + gridSize; x += gridSize) {
      // to offset every alternate row
      if (offsetCount % 2 == 0) {
        offset = gridSize/2;
      } else {
        offset = 0;
      }

      if (random(1)>density) {

      float red = random(150,250);
      float green = random(150,250);
      float blue = random(150,250);

      gradientTriangle(x + offset, y + gridSize, x + (gridSize/2) + offset, y, x + gridSize + offset, y + gridSize, 0.01, red, green, blue, 70, rStarter, gStarter, bStarter);
      gradientTriangle(x + (gridSize/2) + offset, y, x + gridSize + offset, y + gridSize, x + gridSize + (gridSize/2) + offset, y, 0.01, red, green, blue, 70, rStarter, gStarter, bStarter);
      }
    }
    offsetCount++;
  }

}
