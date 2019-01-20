
var fade = 0;
var page = 0;
function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
  background('#a5c7ff');
  triangles();
}

function draw() {
  if (start > 0) {
    fill(color(255, 255, 255));
    rect(0 , 0, windowWidth, windowHeight, 5, 5, 5, 5);
  }
  titleScreen();
  fill(color(162, 188, 229, titleTransition));
   rect(610, 450, 300, 100, 5, 5, 5, 5);
 fill(color(255, 255, 255, titleTransitionWhite));
  rect(610 - 10, 440, 300, 100, 5, 5, 5, 5);
   start = 0;

  if (page) {
    richGame(page);
  }
  }



function mousePressed() {
  page++;
}
