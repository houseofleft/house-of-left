void setup() {
  size(600, 600);
  frameRate(1);
}

void draw() {
  background(240);

  haze(0.006, 0.004, random(7), 77, 177, 176);
  haze(0.006, 0.003, random(7), 88, 185, 184);

  float point1 = random(height);
  float point2 = random(height);
  float noiseStarter = random(7);
  float shift = 0;

  for (int i = 0; random(1) < 0.7; i++) {
    fill(221 + random(-20, 20), 0 + random(-20, 20), 0 + random(-20, 20));
    squiggle(random(-300, -310), point1 + shift, width+300, point2 + shift, random(2, 6), random(1, 3), 300, 0.05, 0.003, random(7), noiseStarter);
    shift += random(-200, 200);
  }



}

