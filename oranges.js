var fade = 0;
function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
  background('#a5c7ff');
  triangles();
}

function draw() {
  if (start == true) {
    for (i=1; i<255; i++){
    fade = fade++;
    fill(color(255, 255, 255, fade));
    rect(0 , 0, windowWidth, windowHeight, 5, 5, 5, 5);
  }
  }
  titleScreen();
  begin();


}
