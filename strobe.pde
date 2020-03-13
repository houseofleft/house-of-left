float red = random(10);
float blue = random(10);
float green = random(10);
float alpha = random(10);
float noiseScale = 0.01;

void setup() {
  size(600,600);
}

void draw() {
  background(240);
  float rNoise = map(noise(red), 0, 1, 150, 255);
  float bNoise = map(noise(blue), 0, 1, 150, 255);
  float gNoise = map(noise(green), 0, 1, 150, 255);
  float aNoise = map(noise(alpha), 0, 1, 50, 150);
  noStroke();
  fill(rNoise, bNoise, gNoise, aNoise);
  rect(width/2 - 250, height/2 - 250, 500, 500);
  red += noiseScale;
  blue += noiseScale;
  green += noiseScale;
  alpha += noiseScale;
}
