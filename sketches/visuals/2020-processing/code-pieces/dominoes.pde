void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(240);

  float redChance = random(7);
  float greenChance = random(7);
  float blueChance = random(7);

  int[] possibleGrids = {30, 40, 50};
  float gridSize = possibleGrids[int(random(3))];
  float margin = gridSize * int(random(2,5));

  float thickness = 0.4;
  float thicknessWack = 0.4;
  float movementWack = 0.1;
  thickness = 1;
  thicknessWack = 0;
  movementWack = 0;
  float thicknessScale = random(0.04);
  float movementScale = 0.02;


  float[] colour1 = {137, 183, 145};
  float[] colour2 = {189, 172, 175};
  float cVar = 15;

  for (float x = 0; x <= width; x += gridSize) {
    for (float y = 0; y <= height; y += gridSize) {
      gradientRect(x, y, gridSize, gridSize, 0.004, random(220, 250), random(220, 250), random(220, 250), 100, redChance, greenChance, blueChance);
    }
  }

  fill(random(220, 250), random(220, 250), random(220, 250));

  for (float x = margin; x <= width - margin; x += gridSize) {
    squiggle(x, margin, x, height-margin, thickness, thicknessWack, movementWack, thicknessScale, movementScale, random(7), random(7));
  }
  for (float y = margin; y <= width - margin; y += gridSize) {
    squiggle(margin, y, width-margin, y, thickness, thicknessWack, movementWack, thicknessScale, movementScale, random(7), random(7));
  }

  for (float x = margin; x < width - margin; x += gridSize) {
    for (float y = margin; y < width - margin; y += gridSize) {
      float coinToss = random(1);
      if (coinToss > 0.75) {
       circle(x + gridSize/2, y + gridSize/2, 3);
      } else if (coinToss > 0.5) {
        circle(x + (gridSize/4), y + (gridSize/4), 3);
        circle(x + ((gridSize*3)/4), y + (gridSize/4), 3);
        circle(x + (gridSize/4), y + ((gridSize*3)/4), 3);
        circle(x + ((gridSize*3)/4), y + ((gridSize*3)/4), 3);
      } else if (coinToss > 0.25) {
        circle(x + (gridSize/4), y + (gridSize/4), 3);
        circle(x + ((gridSize*3)/4), y + ((gridSize*3)/4), 3);
      } else {
        circle(x + ((gridSize*3)/4), y + (gridSize/4), 3);
        circle(x + (gridSize/4), y + ((gridSize*3)/4), 3);
      }
    }
  }

}
