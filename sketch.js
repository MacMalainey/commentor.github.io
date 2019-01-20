var titleTransition = 0;
var titleTransitionWhite = 100;
var writing = 0

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

function printBox(fraction) {
    var barHeight = 20;

}
