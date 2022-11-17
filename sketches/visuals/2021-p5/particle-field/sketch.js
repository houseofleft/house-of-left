let noiseScale, colorNoiseScale, t, tStep, rN, gN, bN;


function setup() {
  createCanvas(windowWidth, windowHeight);
  field = new ParticleField(50000, random(10, 30), random(30));
  noiseScale = 0.002;
  colorNoiseScale = 0.0005;
  t = Math.random(10000);
  tStep = 0.01;
  rN = random(1000);
  gN = random(1000);
  bN = random(1000);
}


function draw() {
  background(240);
  field.run();
  t += tStep;
}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}

class Particle {
  constructor(maxSpeed, noiseAffect) {
    this.x = random(0, width);
    this.y = random(0, height);
    this.xd = 0;
    this.yd = 0;
    this.maxSpeed = maxSpeed;
    this.noiseAffect = noiseAffect;
  }

  updateVector() {
    this.xd += this.noiseAffect * (noise(this.x * noiseScale, this.y * noiseScale, t) - 0.5)
    this.yd += this.noiseAffect * (noise(this.y * noiseScale, this.x * noiseScale, t) - 0.5)
    this.xd = max(min(this.xd, this.maxSpeed), -this.noiseAffect);
    this.yd = max(min(this.yd, this.maxSpeed), -this.noiseAffect);
  }

  move() {
    this.x += this.xd;
    this.y += this.yd;
    if (this.x < 0) {
      this.x = width;
    } else if (this.x > width) {
      this.x = 0;
    } if (this.y < 0) {
      this.y = height;
    } else if (this.y > height) {
      this.y = 0;
    }
  }

  render() {
    strokeWeight(1.5);

    let r = noise(this.x * colorNoiseScale + rN, this.y * colorNoiseScale + rN, t) * 255;
    let g = noise(this.x * colorNoiseScale + gN, this.y * colorNoiseScale + gN, t) * 255;
    let b = noise(this.x * colorNoiseScale + bN, this.y * colorNoiseScale + bN, t) * 255;
    stroke(r, g, b);

    point(this.x, this.y);
  }

}

class ParticleField {
  constructor(n, maxSpeed, noiseAffect) {
    this.particles = [];
    for (let i = 0; i < n; i++) {
      let p = new Particle(maxSpeed, noiseAffect);
      this.particles.push(p);
    }
  }

  run() {
    for (let i = 0; i < this.particles.length; i++) {
      let p = this.particles[i];
      p.updateVector();
      p.move();
      p.render();
    }
  }
}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}
