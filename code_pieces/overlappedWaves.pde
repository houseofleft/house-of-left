void setup() {
    size(700, 700);
    frameRate(0.2);
}

void draw() {
    background(240);
    fill(random(150,250),random(150,250),random(150,250));
    float starter = random(7);
    for (float y = 50; y < height - 50; y+= 10) {
        anotherSquiggle(60,y,width-60,y,2,2,50,0.02,0.02,starter,starter);
    }
    fill(random(150,250),random(150,250),random(150,250));
    float starter2 = random(7);
    for (float y = 50; y < height - 50; y+= 10) {
        anotherSquiggle(60,y,width-60,y,2,2,50,0.02,0.02,starter2,starter2);
    }
}

