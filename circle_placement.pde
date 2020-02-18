void setup() {
  size(1200, 600);
  noStroke();
  frameRate(0.2);
}

void draw() {
  background(240);
  float gridSize = random(10, 100);
  float shapeSize;
  float chanceOne = random(0.66);
  float chanceTwo = random(0.5);
  float chanceThree = random(0.66);
  if (random(1) > 0.5) {shapeSize = gridSize / 3;}
  else {shapeSize = (gridSize / 3) * 2;}
  for (int x = 0; x + (shapeSize/2) < width; x += gridSize) {
    for (int y = 0; y + (shapeSize/2) < height; y += gridSize) {
      if (random(1) < chanceOne) {fill(230, 180, 0);}
      else if (random(1) < chanceTwo) {fill(240, 60, 0);}
      else {fill(100);}
      if (random(1)<chanceThree) {circle(x + (shapeSize/2), y + (shapeSize/2), shapeSize);}
    }
  }
}

void keyPressed() {
  if (keyCode == ENTER) {saveFrame("cirlces-####.jpg");}
}
