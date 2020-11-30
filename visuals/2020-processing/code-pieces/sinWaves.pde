void setup() {
  size(600,600);
  frameRate(0.2);
}

void draw() {

  background(240);
  float noiseStart = random(7);

  float r = random(7);
  float g = random(7);
  float b = random(7);

  float red = random(150, 250);
  float green = random(150, 250);
  float blue = random(150, 250);

  //gradientRect(0, 0, width, height, 0.002, red, green, blue, 70, random(7), random(7), random(7));

  fill(240);
  for (float y = 0; y <= height; y += 30) {
    sinSquiggle(-100, y, width+100, y, 5, 1, 5, 0.04, 0.04, noiseStart, noiseStart, red, green, blue, 70, 0.002, r, g, b);
    noiseStart += 0.05;
  }

}


// this function draws an imperfect line
// it takes as arguments:
// x1: x coordinate of 1st point
// y1: y coordinate of 1st point
// x2: x coordinate of 2nd point
// y2: y coordinate of 2nd point
// thickness: thickness of line in pixels
// thicknessWack: how strongly the line thickness varies
// movementWack: how strongly the line veers off
// thicknessScale: how fast the line thickness varies (e.g. 1 would seem random fluctuation, 0.002 would be very smooth)
// movementScale: how fast the line veers off (e.g. 1 would seem almost random points, 0.002 would be very smooth)
// thicknessStart: the perlin noise start point for thickness (use random number if unsure)
// movementStart: the perlin noise start point for movement (use random number if unsure)
void sinSquiggle(
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
  float movementStart,
  float red, float green, float blue, float cVar, float noiseScale, float noiseRStart, float noiseGStart, float noiseBStart) {

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

    float noiseMovement = map(sin(positionNoiseCount), 0, 1, -movementWack, movementWack);
    float noiseSize = map(sin(thicknessNoiseCount), 0, 1, -thicknessWack, thicknessWack);

    float rNoise = noise((x*noiseScale)+noiseRStart, (y*noiseScale)+noiseRStart);
    float gNoise = noise((x*noiseScale)+noiseGStart, (y*noiseScale)+noiseGStart);
    float bNoise = noise((x*noiseScale)+noiseBStart, (y*noiseScale)+noiseBStart);
    float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
    float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
    float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
    fill(rColour, gColour, bColour);

    circle(x+noiseMovement,y+noiseMovement, thickness+noiseSize);

    positionNoiseCount += movementScale;
    thicknessNoiseCount += thicknessScale;
    x += xStep;
    y += yStep;
  }

}
