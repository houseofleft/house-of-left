void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {
  background(240);
  float thicknessStarter = random(7);
  float movementStarter = random(7);

  int steps = int(random(3, 20));
  float movementWack = random(steps, steps+30);
  int iSteps = int(random(steps));
  float dynamism = random(0.5);

  int[] redArray = {248, 151, 255, 251};
  int[] greenArray = {231, 227, 91, 158};
  int[] blueArray = {188, 219, 109, 205};

  int colourOne = int(random(4));
  int colourTwo = int(random(4));
  while (colourOne == colourTwo) {colourTwo = int(random(4));}

  for (float y = -movementWack; y <= height+movementWack; y += steps) {

    for (int i = 0; i <= steps+movementWack; i++) {

      float red = map(i, 0, iSteps, redArray[colourOne], redArray[colourTwo]);
      float green = map(i, 0, iSteps, greenArray[colourOne], greenArray[colourTwo]);
      float blue = map(i, 0, iSteps, blueArray[colourOne], blueArray[colourTwo]);

      fill(red, green, blue);

      squiggleMod(-movementWack, y+i, width+movementWack, y+i, 2, 1, movementWack, 0.02, 0.002, thicknessStarter, movementStarter);
    }

    movementStarter += random(-dynamism, dynamism);
  }

}

void squiggleMod(
  float x1,
  float y1,
  float x2,
  float y2,
  float thickness,
  float thicknessWack,
  float movementWack,
  float thicknessScale,
  float movementScale,
  float thicknessStart,
  float movementStart) {

  // moving from 1 to 2
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
  float positionNoiseCount = movementStart;
  float thicknessNoiseCount = thicknessStart;
  noStroke();

  for (int i = 0; i < iStop; i++) {

    float noiseMovement = map(noise(x*movementScale+positionNoiseCount,y*movementScale+positionNoiseCount), 0, 1, -movementWack, movementWack);
    float noiseSize = map(noise(thicknessNoiseCount), 0, 1, -thicknessWack, +thicknessWack);

    circle(x+noiseMovement,y+noiseMovement, thickness+noiseSize);

    positionNoiseCount += movementScale;
    thicknessNoiseCount += thicknessScale;

    x += xStep;
    y += yStep;
  }

}
