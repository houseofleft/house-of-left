// this function creates a colour gradient in a circle shape (can be used to draw a semi circle)
// it takes as arguments:
// cX : x location of centre of circle
// cY : y location of centre of circle
// radius : radius of circle
// startAngle : the angle from which the circle will start being drawn (clockwise)
// endAngle : the angle to which the circle will be drawn
// cStep : how disbursed the circle will be (theoretically, 1 should mean pixels are "1" apart and the circle is therefore solid, however in practice, make it around 0.3 - 0.5 to achieve this for a larger circle
// noiseScale : scale of perlin noise (0.002 will create a smooth gradient, 5 will effectively be random)
// red, green, blue : colour values for "central" colour around which the gradient will vary
// cVar : how much red, green and blue values are allowed to vary from "central" colour
// noiseRStart, noiseGStart, noiseBStart : starting values for perlin noise
void gradientCircle(float cX, float cY, float radius, float startAngle, float endAngle, float cStep, float noiseScale, float red, float green, float blue, float cVar, float noiseRStart, float noiseGStart, float noiseBStart) {
  //looping through distances from the centre
  for (float h = 0; h <= radius; h++) {
  // now figure out the circumference at this point
  // so we can draw the right amount of pixels
  // (this still doesn't quite work, can be levelled out with the cStep argument)
  float circumference = (radius * 2) * PI;
  // figuring out which points we want to start on
  float startC = map(startAngle, 0, 360, 0, circumference);
  float endC = map(endAngle, 0, 360, 0, circumference);
    for (float c = startC; c <= endC; c+= cStep) {
      // but we need to convert point in the circumference to an angle now
      // which we can do pretty quickly with mapping
      float angle = map(c, 0, circumference, 0, 360);
      float opposite = sin(radians(angle)) * h;
      float adjacent = cos(radians(angle)) * h;
      // now affecting colour based on noise of x and y
      float rNoise = noise(((cX + adjacent)*noiseScale)+noiseRStart, ((cY+opposite)*noiseScale)+noiseRStart);
      float gNoise = noise(((cX + adjacent)*noiseScale)+noiseGStart, ((cY+opposite)*noiseScale)+noiseGStart);
      float bNoise = noise(((cX + adjacent)*noiseScale)+noiseBStart, ((cY+opposite)*noiseScale)+noiseBStart);
      float rColour = map(rNoise, 0, 1, max(0, red-cVar), min(255, red+cVar));
      float gColour = map(gNoise, 0, 1, max(0, green-cVar), min(255, green+cVar));
      float bColour = map(bNoise, 0, 1, max(0, blue-cVar), min(255, blue+cVar));
      stroke(rColour, gColour, bColour);
      // finalling making point on canvas
      point(cX + adjacent, cY + opposite);
    }
  }
}
