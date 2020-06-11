void setup() {
  size(600, 600);
  frameRate(1);
}

void draw() {
  background(240);

  haze(0.002, 0.002, random(7), 64, 168, 159);
  haze(0.002, 0.002, random(7), 79, 186, 173);
  haze(0.002, 0.002, random(7), 183, 226, 220);

  float thick = random(7);
  float movement = random(7);
  float wack = 100;
  noStroke();

  for (float y = -wack; y < height + wack; y += 4) {
    fill(94 + random(-50, 50), 73 + random(-50, 50), 49 + random(-50, 50));
    anotherSquiggle(0, y, width, y, 1, 2, wack, 0.02, 0.005, thick, movement);
  }

}



