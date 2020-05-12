void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(240);
  gradientRect(0, 0, width, height, 0.005, 240, 240, 240, 30, random(7), random(7), random(7));

  float steps1 = 100;
  float steps2 = 122;

  float margin = int(random(4, 12)) * 10;
  float iconSize = height - (margin * 2);

  float thickness = 1;
  float thicknessWack = random(0.3, 0.6);
  float movementWack = random(10, 40);
  float thicknessScale = random(0.04);
  float movementScale = 0.02;
  float start1 = random(7);
  float start2 = random(7);
  float start3 = random(7);
  float start4 = random(7);

  float[] colour1 = {137, 183, 145};
  float[] colour2 = {189, 172, 175};
  float cVar = 15;

  fill(0);

  // covering the left diagonal
  for (int i = 1; i <= steps1; i++) {
    // x1 is always gonna be 0
    // y2 is always gonna be 0
    // x2 and y1 are always going to be the same in a square grid
    float x1 = margin;
    float y1 = margin + ((i/steps1) * iconSize);
    float x2 = margin + ((i/steps1) * iconSize);
    float y2 = margin;
    fill(colour1[0]+random(-cVar,cVar),colour1[1]+random(-cVar,cVar),colour1[2]+random(-cVar,cVar));
    squiggle(x1, y1, x2, y2, thickness, thicknessWack, movementWack, thicknessScale, movementScale, start1, start2);
  }

  // covering the right diagonal
  for (int i = 0; i <= steps2; i++) {
    float x1 = margin + ((i/steps2) * iconSize);
    float y1 = margin + ((1 - (i/steps2)) * iconSize);
    float x2, y2;
    if ((i/(steps2-1)) < 0.5) {
      x2 = margin + ((i/(steps2/2)) * iconSize);
      y2 = margin + iconSize;
    } else {
      x2 = margin + iconSize;
      y2 = map(i, steps2/2, steps2, margin + iconSize, margin);
    }
    fill(colour2[0]+random(-cVar,cVar),colour2[1]+random(-cVar,cVar),colour2[2]+random(-cVar,cVar));
    squiggle(x1, y1, x2, y2, thickness, thicknessWack, movementWack, thicknessScale, movementScale, start3, start4);
  }

}
