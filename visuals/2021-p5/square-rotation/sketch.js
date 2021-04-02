function setup() {
  createCanvas(windowWidth, windowHeight);
  // Sets origin mode to be the rectangle's center
  rectMode(CENTER);
}

function draw() {
  background(240);

  // Moves rectangle to center of canvas
  translate(width / 2, height / 2);

  // Creates multiple rotating rectangles
  for (let x = 500; x > 0; x -= 50) {
      // Makes height the same as width so it's a square
      let y = x;
      strokeWeight(0.5);
      rotate(radians(frameCount / 50));
      fill(255, x*0.75, 255);
      rect(0, 0, x, y);
      noFill();
      stroke(0, 100, 240);
      for (let i = 1; i < 10; i++) {
        rect(0 + i, 0 + i, x - i, x - i);
      }
  }
}
