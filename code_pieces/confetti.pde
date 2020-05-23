void setup() {
  size(1200, 1200);
  frameRate(0.2);
}

void draw() {

  background(240);
  float gridSize = 100;
  float iconSize = 60;
  float margin = 200;
  float gridMargin = (gridSize - iconSize) / 2;

  float rStart = random(7);
  float gStart = random(7);
  float bStart = random(7);

  for (float x = margin; x < width - margin; x += gridSize) {
    for (float y = margin; y < height - margin; y += gridSize) {
      crane(x + gridMargin, y + gridMargin, iconSize, rStart, gStart, bStart);
    }
  }

}

void crane(float x, float y, float size, float rStart, float gStart, float bStart) {

  float red = random(150, 250);
  float green = random(150, 250);
  float blue = random(150, 250);

  if (random(1) > 0.1) {
    float mono = random(250);
    red = mono;
    green = mono;
    blue = mono;
  }

  //pick random point 1
  float point1x = int(random(x + (size/3), x + ((size/3)*2)));
  float point1y = int(random(y, y + (size/2)));

  //pick random point 2
  float point2x = int(random(x + size/3, x + ((size/3)*2)));
  float point2y = int(random(y + size/2,y + size));

  //picking random point 3 for now
  float point3x = random(x, x + size);
  float point3y = random(y, y + size);

  gradientTriangle(point1x, point1y, point2x, point2y, point3x, point3y, 0.02, red, green, blue, 20, rStart, gStart, bStart);

  //half way to 2 from 1
  float halfx = (point1x + point2x) / 2;
  float halfy = (point1y + point2y) / 2;

  //distance to half from 3
  float x3tohalf = point3x - halfx;
  float y3tohalf = point3y - halfy;

  //point 4
  float point4x = halfx + (x3tohalf * -1);
  float point4y = halfy + (y3tohalf * -1);

  gradientTriangle(point1x, point1y, point2x, point2y, point4x, point4y, 0.02, red, green, blue, 20, rStart, gStart, bStart);
}
