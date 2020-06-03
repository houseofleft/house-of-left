float thick = random(7);
float movement = random(7);
float r = random(7);
float g = random(7);
float b = random(7);

void setup() {
  size(600, 600);
}

void draw() {

  background(253, 220, 0);

  fill(0);

  for (float y = ((height * 3)/5); y < ((height * 4) / 5); y += 10) {
    anotherSquiggle(0, y, width, y, 1.5, 0, 100, 0.02, 0.005, thick, movement);
  }

  thick += 0.05;
  movement += 0.05;

}
