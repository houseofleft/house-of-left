function setup() {
  createCanvas(500, 500);
}

function draw() {

  //vertical lines
  stroke(127);
  strokeWeight(10);

  for (posX = 0; posX <= width/2; posX += 25) {
    line(posX, 0, posX, height/2);
  }

  //polkadot
  noStroke();
  fill('#ffd700');

  for (posX = width/2; posX <= width; posX += 25) {
    for (posY = 0; posY <= height/2; posY += 25) {
      if (posX % 2 === 0) {
        circle(posX, posY - 10, 10);
      } else {
        circle(posX, posY, 10);
      }
    }
  }

  //checker board
  fill('red')
  for (posX = 0; posX < width/2; posX += 25) {
    for (posY = height/2; posY <= height; posY += 50) {
      if (posX % 2 === 0) {
        square(posX, posY+25, 25);
      } else {
        square(posX, posY, 25);
      }
    }
  }

  //diagonal lines
  strokeWeight(10);
  stroke(0, 0, 255);
  for (i = 0; i < 10; i++) {
    line(width/2, height - (i * 25), width/2 + (i *25), height);
    line(width/2 + (i*25), height/2, width, height - (i*25));
  }


  //dividers
  stroke(0);
  strokeWeight(10);

  line(width/2, 0, width/2, height);
  line(0, height/2, width, height/2);
  strokeWeight(20);
  line(width, 0, width, height);
  line(0, 0, 0, height);
  line(width, height, 0, height);
  line(0, 0, width, 0);

}
