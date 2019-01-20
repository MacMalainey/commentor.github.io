var page = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
  background('#a5c7ff');

}

function draw() {
  titleScreen();
  if (page) {
    richGame(page);
  }
}

function mousePressed() {
  page++;
}
