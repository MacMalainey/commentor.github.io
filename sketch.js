var titleTransition = 0;
var titleTransitionWhite = 100;
var writing = 0;
var buttonPressed = 5;
var buttonX = 300;
var buttonY = 100;
var coordinateX = 600;
var coordinateY = 440;


function titleScreen(){
  writing = writing + 8;
  titleTransition=titleTransition+2;
  titleTransitionWhite= titleTransitionWhite+2;

  //Title box and screen
  fill(color(162, 188, 229, titleTransition));
  rect(370, 110, 800, 150, 5, 5, 5, 5);
  fill(color(255, 255, 255, titleTransitionWhite));
  rect(360, 100, 800, 150, 5, 5, 5, 5);
  fill(color(165, 199, 255, writing));
  textFont('monospace', 50);
  textSize(50);
  text('GitHub Statistics',530 , 150, 600, 100);

  //Subtitle
  fill(color(162, 188, 229, titleTransition));
  rect(610, 275, 560 , 40, 5, 5, 5, 5);
  fill(color(255, 255, 255, titleTransitionWhite));
  rect(600, 265, 560 , 40, 5, 5, 5, 5);

  fill(color(165, 199, 255, writing));
  textFont('monospace', 50);
  textSize(17);
  text('Mac Malainey, Hudson Shykowski, Richmond Naviza, Lora Ma', 618 , 278, 600, 50);


}

function triangles(){
  //background triangles
  fill(color(212, 225, 247, 180));
  triangle(800,10 , 100, 625, 200, 200);
  fill(color(127, 173, 249, 255));
  triangle(30, 700, 580, 100, 860, 750);
  fill(color(151, 188, 252, 180));
  triangle(1100, 0, 1500, 0, 1000, 300);
  fill(color(191, 209, 239, 150));
  triangle(900, 100, 900, 800, 1500, 800);
}

function begoneTHOT(){
    rect(0,0,windowWidth,windowHeight);
}
