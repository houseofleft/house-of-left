void setup() {
    size(700, 700);
}

void draw() {
    lines();
}

void lines() {
    // first off pick a random point
    float randomX = random(width);
    float xlength = random(-200,200);
    float ylength = random(-200,200);
    float randomY = random(height);
    // pick a random shift
    float shiftX = random(-2,2);
    float shiftY = random(-2,2);
    // pick a number of lines
    float lines = random(200);
    // pick a noise start
    float starter = random(7);
    for (int i = 0; i < lines; i++) {
        if (i % 2 == 0) {fill(240);} else {fill(200);}
        fill(random(230,250));
        squiggle(randomX,randomY,randomX+xlength,randomY+ylength,2,1,40,0.002,0.01,starter,starter);
        randomX += shiftX;
        randomY += shiftY;
    }


}
