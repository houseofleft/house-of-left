void setup() {
  size(1000,1000);
  frameRate(0.2);
}

void draw() {

  background(240);

  float noiseStartX = random(7);
  float noiseStartY = random(7);

  float noiseScale = 0.001;


  float[] backgroundColour = {228, 220, 190};
  float[] highlightColour = {252, 207, 138};
  float[] navy = {100, 174, 193};
  float[] lightGrey = {200, 200, 200};
  float[] darkBlue = {150, 224, 243};
  float[] lightBlue = {215, 231, 250};
  float[] pink = {207, 44, 111};


  // contouring
  for (int i = 0; i < 10; i++) {
    contour(highlightColour, highlightColour, noiseScale, noiseStartX, noiseStartY, i*0.1, (i*0.1)+0.005, "outline");
  }


  contour(lightBlue, darkBlue, noiseScale, noiseStartX, noiseStartY, 0.45, 0.55, "stripes");
  contour(darkBlue, darkBlue, noiseScale, noiseStartX, noiseStartY, 0.45, 0.455, "outline");
  contour(darkBlue, darkBlue, noiseScale, noiseStartX, noiseStartY, 0.55, 0.555, "outline");

  contour(darkBlue, navy, noiseScale, noiseStartX, noiseStartY, 0.65, 1, "spots");
  contour(navy, navy, noiseScale, noiseStartX, noiseStartY, 0.65, 0.655, "outline");


  contour(pink, lightGrey, noiseScale, noiseStartX, noiseStartY, 0.25, 0.35, "spots");
  contour(lightGrey, lightGrey, noiseScale, noiseStartX, noiseStartY, 0.25, 0.255, "outline");
  contour(lightGrey, lightGrey, noiseScale, noiseStartX, noiseStartY, 0.35, 0.355, "outline");


}


void contour(float[] backgroundColour, float[] foregroundColour, float noiseScaleShape, float noiseStartX, float noiseStartY, float lowerEdge, float upperEdge, String vibe) {

  int xMulti = int(random(2));
  int yMulti = 1;

  for (float x = 0; x < width; x++) {
    for (float y = 0; y < height; y++) {
      float pointNoise = noise((x * noiseScaleShape) + noiseStartX, (y * noiseScaleShape) + noiseStartY);
      if ( (pointNoise > lowerEdge) && (pointNoise <= upperEdge)) {
        // first drawing the background
        stroke(backgroundColour[0], backgroundColour[1], backgroundColour[2]);
        point(x, y);
        // now the foreground
        if (vibe == "stripes") {
          if ( ((x * xMulti) + (y * yMulti)) % 11 == 0 ) {
            stroke(foregroundColour[0], foregroundColour[1], foregroundColour[2]);
            point(x, y);
          }
        }
        else if (vibe == "spots") {
          if ((x % 10 == 0) && (y % 10 == 0)) {
            noStroke();
            fill(foregroundColour[0], foregroundColour[1], foregroundColour[2]);
            circle(x, y, 5);
          }
        }
        else if (vibe == "outline") {
          fill(foregroundColour[0], foregroundColour[1], foregroundColour[2]);
          circle(x, y, 5);
        }
      }
    }
  }
}

