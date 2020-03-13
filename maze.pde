void setup() {
  size(700, 700);
  strokeWeight(5);
  frameRate(0.2);
}

void draw() {

  float xrNoise = random(10);
  float yrNoise = random(10);
  float xbNoise = random(10);
  float ybNoise = random(10);
  float xgNoise = random(10);
  float ygNoise = random(10);
  float xaNoise = random(10);
  float yaNoise = random(10);

  float noiseScale = 0.1;

  int gridSize = int(random(5, 30));
  int strokeDiv = int(random(2, 4));

  background(240);
  for (int x = 0; x <= width + gridSize; x += gridSize) {

    float yrNoiseStart = yrNoise;
    float ybNoiseStart = ybNoise;
    float ygNoiseStart = ygNoise;

    for (int y = 0; y <= height + gridSize; y += gridSize) {

      float red = map(noise(yrNoise, xrNoise), 0, 1, 150, 250);
      float blue = map(noise(ybNoise, xbNoise), 0, 1, 150, 250);
      float green = map(noise(ygNoise, xgNoise), 0, 1, 150, 250);

      strokeWeight(max(1, gridSize/strokeDiv));
      stroke(red, blue, green);

      if (random(1) > 0.5) {
        line(x, y, x + gridSize, y + gridSize);
      } else {
        line(x, y + gridSize, x + gridSize, y);
      }

      yrNoise += noiseScale;
      ybNoise += noiseScale;
      ygNoise += noiseScale;

    }

    yrNoise = yrNoiseStart;
    ybNoise = ybNoiseStart;
    ygNoise = ygNoiseStart;

    xrNoise += noiseScale;
    xbNoise += noiseScale;
    xgNoise += noiseScale;

  }
}
