void setup() {
  size(600, 600);
  frameRate(0.2);
}

void draw() {

  background(240);


  // background
  gradientRect(0, 0, width, height, 0.002, random(150, 250), random(150, 250), random(150, 250), 70, random(7), random(7), random(7));

  // noise waves

  float thick = random(7);
  float movement = random(7);

  fill(240);

  for (int y = 250; y < height - 70; y += 10) {
    anotherSquiggle(50, y, width-50, y, 1.5, 0, 100, 0.02, 0.005, thick, movement);
  }

  // glyphs

  int glyphSize = 10;
  int padding = 5;

  stroke(240);
  strokeWeight(1.5);

  for (int i = 0; i <= 7; i++) {
    for (int x = 50; (random(1) < 0.95) && (x < width * 0.8); x += glyphSize + padding) {
      squareGlyph(x, ((glyphSize + padding) * i) + 50, glyphSize);
    }
  }

}

