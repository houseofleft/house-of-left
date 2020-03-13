// setup
void setup() {
  size(400, 700);
  frameRate(0.2);
  noStroke();
}

// draw
void draw() {
  background(240);
  int rec_depth = int(random(5, 10));
  makeTotem(120, 15, width-240, height - 30, rec_depth);
}

// central makeTotem function (to draw a rectangle divided into coloured sections)
void makeTotem(int x, int y, int totemWidth, int totemHeight, int depth) {
  // first off, decide colour of rectangle
  fill(random(100, 200));
  if (random(1) < 0.3) {if (random(1) < 0.66) {fill(230, 180, 0);} else {fill(240, 60, 0);}}
  // base case: depth is one - draw rectangle in remaining space
  if (depth <= 0) {
    rect(x, y, totemWidth, totemHeight, random(totemWidth), random(totemWidth), random(totemWidth), random(totemWidth));
  }
  // recursive step: draw a rectangle in some of it then call function again in remaining space
  else {
    float ratio = 1.0/depth;
    ratio = random(ratio*0.2, ratio*0.8);
    int newTotemHeight = int(totemHeight * ratio);
    rect(x, y, totemWidth, newTotemHeight, random(totemWidth), random(totemWidth), random(totemWidth), random(totemWidth));
    makeTotem(x, y+newTotemHeight, totemWidth, totemHeight - newTotemHeight, depth - 1);
  }
}
