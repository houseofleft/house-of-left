void gradientTriangle(float x1, float y1, float x2, float y2, float x3, float y3, float noiseScale, float red, float green, float blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  noStroke();
  // start by moving from 1 to 2
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

  for (int i = 0; i < iStop; i++) {
    // this is running across the line between x1,y1 and x2,y2
    // at each point, we now need to draw ANOTHER line, between point x,y and x3,y3
    // basically repeating the exact code
    float xStep2, yStep2, iStop2;

    if (abs(x-x3) > abs(y-y3)) {
      if (x > x3) {xStep2 = -1;} else {xStep2 = 1;}
      if (y > y3) {yStep2 = -1 * (abs(y-y3)/abs(x-x3));} else {yStep2 = abs(y-y3)/abs(x-x3);}
      iStop2 = abs(x-x3);
    } else {
      if (y > y3) {yStep2 = -1;} else {yStep2 = 1;}
      if (x > x3) {xStep2 = -1 * (abs(x-x3)/abs(y-y3));} else {xStep2 = abs(x-x3)/abs(y-y3);}
      iStop2 = abs(y-y3);
    }

    float xAgain = x;
    float yAgain = y;

    for (int ii = 0; ii < iStop2; ii++) {
      // now affecting colour based on noise of x and y
      float rNoise = noise((xAgain*noiseScale)+noiseRStart, (yAgain*noiseScale)+noiseRStart);
      float gNoise = noise((xAgain*noiseScale)+noiseGStart, (yAgain*noiseScale)+noiseGStart);
      float bNoise = noise((xAgain*noiseScale)+noiseBStart, (yAgain*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      fill(rColour, gColour, bColour);
      // finally making point on canvas
      circle(xAgain, yAgain, 2);
      xAgain += xStep2;
      yAgain += yStep2;
    }

    x += xStep;
    y += yStep;
  }

}

