float wack = random(2);

void setup() {
  size(700, 500);
  frameRate(1);
}

void draw() {
  background(240);
  noStroke();
  fill(0);
  for (int x = 0; x < width; x+=int(random(1, 100))) {
    toothUp(x);
    toothDown(x);
  }
}

void toothUp(float x) {
  int size = int(random(1, 2));
  for (int y = 0; y < height; y++) {
    x += random(wack*-1, wack);
    circle(x, y, size);
  }
}


void toothDown(float x) {
  int size = int(random(1, 2));
  for (int y = height; y > 0; y--) {
    x += random(wack*-1, wack);
    circle(x, y, size);
  }
}
