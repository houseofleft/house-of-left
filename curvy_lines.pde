//== setup

void setup() {
  
 frameRate(0.2);
 size(1000, 600);
 noFill();
 strokeWeight(60);
 
}


//== draw

void draw() {
  
  background(240);
  
  stroke(230, 180, 0);
  curvyLine();
  
  stroke(100);
  curvyLine();
  
  stroke(240, 60, 0);
  curvyLine();
  
  
}


//=== central function for drawing line

void curvyLine() {
  
  float xStart, yStart, xEnd, yEnd;
  
  // select start points (either x or y must be max/min value so that is on border)
  float coinToss1 = random(2);
  float coinToss2 = random(2);
  
  if (coinToss1 < 1) {
    if (coinToss2 < 1) {xStart = -50; yStart = random(height);}
    else {xStart = width+50; yStart = random(height);}
  }
  else {
    if (coinToss2 < 1) {xStart = random(width); yStart = 0-50;}
    else {xStart = random(width); yStart = height+50;}
  }
  
  // select end points (either x or y must be max/min value so that is on border)
  coinToss1 = random(2);
  coinToss2 = random(2);
  
  if (coinToss1 < 1) {
    if (xStart == height+50) {xEnd = -50; yEnd = random(height);}
    else {xEnd = width+50; yEnd = random(height);}
  }
  else {
    if (yStart == height+50) {xEnd = random(width); yEnd = -50;}
    else {xEnd = random(width); yEnd = height+50;}
  }
  
  // now drawing line
  bezier(xStart, yStart, random(width), random(height), random(width), random(height), xEnd, yEnd);

}


//=== option to save if enter is pressed

void keyPressed() {
  if (keyCode == ENTER) {saveFrame("lines-####.jpg");}
}
