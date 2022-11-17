let noiseScale, tNoiseScale, noiseVal, resolution, t, rN, gN, bN;

function setup() {
  createCanvas(windowWidth, windowHeight);
  noiseScale = 0.0005;
  noiseVal = random(100);
  tNoiseScale = 0.01;
  resolution = 15;
  t = random(1000);
  t2 = random(1000);
  rN = random(1000);
  gN = random(1000);
  bN = random(1000);
  noiseRStart = int(random(0, 1000));
  noiseGStart = int(random(0, 1000));
  noiseBStart = int(random(0, 1000));
}

function draw() {
  background(240);
  noStroke();
  for (let x = 0; x < width; x += resolution) {
    for (let y = 0; y < height; y += resolution) {
      let r = noise(x * noiseScale + rN, y * noiseScale + rN, t) * 255;
      let g = noise(x * noiseScale + gN, y * noiseScale + gN, t) * 255;
      let b = noise(x * noiseScale + bN, y * noiseScale + bN, t) * 255;
      fill(r, g, b);
      rect(x, y, resolution, resolution);
  }
  }
  t += tNoiseScale;
}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}
