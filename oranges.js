<<<<<<< HEAD
var fade = 0;
=======
var page = 0;

>>>>>>> 04d4a3ae09f09f04fd90c283a873a0180f3190b4
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
<<<<<<< HEAD
  begin();


=======
  if (page) {
    richGame(page);
  }
}

function mousePressed() {
  page++;
>>>>>>> 04d4a3ae09f09f04fd90c283a873a0180f3190b4
}
