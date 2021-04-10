// majority of algorithm from Daniel Shiffman's Nature of Code script
// https://natureofcode.com

let flock;

function setup() {
  createCanvas(windowWidth, windowHeight);
  flock = new Flock(250);
}

function draw() {
  background(240);
  flock.run();
}

class Flock {

  constructor(size) {
    this.boids = []
    for (let i = 0; i < size; i++) {
      let boid = new Boid(random(width), random(height));;
      this.boids.push(boid)
    }
  }

  run() {
    for (let i = 0; i < this.boids.length; i++) {
      this.boids[i].run(this.boids);
    }
  }
}

class Boid {

  constructor(x, y) {
    this.color = this.generateColor();
    this.acceleration = createVector(0, 0);
    this.velocity = createVector(random(-1, 1), random(-1, 1));
    this.position = createVector(x, y);
    this.berth = int(random(3, 10));
    this.maxspeed = 13;
    this.maxforce = 0.2;
  }

  generateColor() {
    let pallete = [
      [100, 150, 200],
      [200, 200, 200],
    ];
    let selection = pallete[int(random(pallete.length))];
    //vary color slightly
    let color = [
      selection[0] + random(-20, 20),
      selection[1] + random(-20, 20),
      selection[2] + random(-20, 20),
    ];
    return color;
  }

  run(boids) {
    this.flock(boids);
    this.update();
    this.border();
    this.render();
  }

  applyForce(force) {
    this.acceleration.add(force);
  }

  flock(boids) {
    let seperated = this.seperate(boids);
    let aligned = this.align(boids);
    let cohesed = this.cohesion(boids);
    seperated.mult(1.5);
    aligned.mult(1.0);
    cohesed.mult(1.3);
    this.applyForce(seperated);
    this.applyForce(aligned);
    this.applyForce(cohesed);
  }

  update() {
    this.velocity.add(this.acceleration);
    this.velocity.limit(this.maxspeed);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }

  seek(target) {
    // desired vector pointing from the location to the target
    let desired = p5.Vector.sub(target,this.position);
    desired.normalize();
    desired.mult(this.maxspeed);
    // Steering = Desired minus Velocity
    let steer = p5.Vector.sub(desired, this.velocity);
    steer.limit(this.maxforce);
    return steer;
  }

  render() {
    // Draw a triangle rotated in the direction of velocity
    let theta = this.velocity.heading() + radians(90);
    fill(this.color[0], this.color[1], this.color[2]);
    noStroke();
    push();
    translate(this.position.x, this.position.y);
    rotate(theta);
    rect(0, 0, this.berth, this.berth * 1.618);
    pop();
  }

  border() {
     if (this.position.x < -this.berth) {
       this.position.x = width + this.berth;
     } else if (this.position.y < -this.berth) {
       this.position.y = height + this.berth;
     } else if (this.position.x > width + this.berth) {
       this.position.x = -this.berth;
     } else if (this.position.y > height + this.berth) {
       this.position.y = -this.berth;
    }
  }

  seperate(boids) {
    let desiredseparation = 25.0;
    let steer = createVector(0, 0);
    let count = 0;
    // For every boid in the system, check if it's too close
    for (let i = 0; i < boids.length; i++) {
      let d = p5.Vector.dist(this.position,boids[i].position);
      // If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
      if ((d > 0) && (d < desiredseparation)) {
        // Calculate vector pointing away from neighbor
        let diff = p5.Vector.sub(this.position, boids[i].position);
        diff.normalize();
        diff.div(d);        // Weight by distance
        steer.add(diff);
        count++;            // Keep track of how many
      }
    }
    // Average -- divide by how many
    if (count > 0) {
      steer.div(count);
    }

    // As long as the vector is greater than 0
    if (steer.mag() > 0) {
      // Implement Reynolds: Steering = Desired - Velocity
      steer.normalize();
      steer.mult(this.maxspeed);
      steer.sub(this.velocity);
      steer.limit(this.maxforce);
    }
    return steer;
  }

  align(boids) {
    let neighbordist = 25;
    let sum = createVector(0,0);
    let count = 0;
    for (let i = 0; i < boids.length; i++) {
      let d = p5.Vector.dist(this.position,boids[i].position);
      if ((d > 0) && (d < neighbordist)) {
        sum.add(boids[i].velocity);
        count++;
      }
    }
    if (count > 0) {
      sum.div(count);
      sum.normalize();
      sum.mult(this.maxspeed);
      let steer = p5.Vector.sub(sum, this.velocity);
      steer.limit(this.maxforce);
      return steer;
    } else {
      return createVector(0, 0);
    }
  }

  cohesion(boids) {
    let neighbordist = 50;
    let sum = createVector(0, 0);
    let count = 0;
    for (let i = 0; i < boids.length; i++) {
      let d = p5.Vector.dist(this.position,boids[i].position);
      if ((d > 0) && (d < neighbordist)) {
        sum.add(boids[i].position);
        count++;
      }
    }
    if (count > 0) {
      sum.div(count);
      return this.seek(sum);
    } else {
      return createVector(0, 0);
    }
  }

}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}
