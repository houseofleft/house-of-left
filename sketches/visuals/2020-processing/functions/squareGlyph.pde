// this function draws a glyph made up of fragments of a square
// it takes as arguments:
// xLocation : location of top left corner of glyph on x axis
// yLocation : location of top left corner of glyph on y axis
// squareWidth : width (and also height) of the glyph
void squareGlyph(int xLocation, int yLocation, int squareWidth) {
  //left
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation, yLocation + squareWidth);
  }
  //right
  if (random(1) > 0.6) {
  line(xLocation + squareWidth, yLocation, xLocation + squareWidth, yLocation + squareWidth);
  }
  //bottom
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation + squareWidth, yLocation);
  }
  //top
  if (random(1) > 0.6) {
  line(xLocation + squareWidth, yLocation + squareWidth, xLocation, yLocation + squareWidth);
  }
  //diagonal1
  if (random(1) > 0.6) {
  line(xLocation, yLocation, xLocation + squareWidth, yLocation + squareWidth);
  }
  //diagonal2
  if (random(1) > 0.6) {
  line(xLocation, yLocation + squareWidth, xLocation + squareWidth, yLocation);
  }
}
