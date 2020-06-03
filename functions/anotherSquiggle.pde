void anotherSquiggle(
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

    float noiseMovement = map(noise((x*movementScale)+movementStart, (y*movementScale)+movementStart), 0, 1, -movementWack, movementWack);
    float noiseSize = map(noise((x*thicknessScale)+thicknessStart, (y*thicknessScale)+thicknessStart), 0, 1, -thicknessWack, thicknessWack);

    circle(x,y+noiseMovement, thickness+noiseSize);

    positionNoiseCount += movementScale;
    thicknessNoiseCount += thicknessScale;
    x += xStep;
    y += yStep;
  }

}
