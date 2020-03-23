float pNoise = random(10);

void setup() {
  size(1500, 500);
  noStroke();
  frameRate(1);
}

void draw() {

  background(240);
  int padding = 5;

  for (int xPoint = 0; xPoint <= width; xPoint += 250) {
    cutBarSquare(xPoint + padding, 0, 250 - (padding * 2), height, 12);
  }

  for (int x = 0; x <= width; x++) {
    for (int y = 0; y <= height; y++) {
      if (random(1) > 0.1) {point(x,y);}
    }
  }

}

void cutBarSquare(int sX, int sY, int sWidth, int sHeight, int numStripes) {

  int sectionWidth = int(sWidth / numStripes);
  int padding = int(0.2 * sectionWidth);
  int stripeWidth = int(sectionWidth * 0.8);
  float pNoise = random(10);
  float direction = random(1);

  for (int x = sX + int(padding/2); x <= sX + sWidth; x += sectionWidth) {

    cutBar(x, sY, stripeWidth, sHeight, noise(pNoise), direction);

    pNoise += 0.2;

  }

}

void cutBar(int cX, int cY, int cWidth, int cHeight, float ratio, float direction) {

  int r1, g1, b1, r2, g2, b2;

  if (direction > 0.5) {
    r1 = 156;
    g1 = 247;
    b1 = 212;
    r2 = 97;
    g2 = 247;
    b2 = 237;
  } else {
    r1 = 97;
    g1 = 247;
    b1 = 237;
    r2 = 156;
    g2 = 247;
    b2 = 212;
  }

  fill(r1, g1, b1);
  rect(cX, cY, cWidth, cHeight);

  fill(r2, g2, b2);

  float fillHeight = cHeight;
  float rectHeight = fillHeight * ratio;
  float triangleHeight = fillHeight * (ratio * (1-ratio));

  rect(cX, cY, cWidth, rectHeight);
  triangle(cX, cY + rectHeight, cX + cWidth, cY + rectHeight, cX, cY + fillHeight);

}
