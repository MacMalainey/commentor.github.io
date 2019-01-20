
var fade = 0;
var page = 0;
var initDimensions = (0,0);

var dicc0 = {
"00-10": 0.8,
"10-20": 0.54,
"20-30": 0.12,
"30-40": 0.65,
"40-50": 0.76,
"50-60": 0.98,
"60-70": 0.12,
"70-80": 0.13
};
var dicc1 = {
"00-10": 0.8,
"10-20": 0.5,
"20-30": 0.23,
"30-40": 0.25,
"70-80": 0.72,
"80-90": 0.65,
"90-100": 0.78
};
var dicc2 = {
  "00-10": 0.8,
  "10-20": 0.54,
  "20-30": 0.12,
  "30-40": 0.65,
  "40-50": 0.76,
  "50-60": 0.98,
  "60-70": 0.12,
  "70-80": 0.13,
  "80-90": 0.23,
  "90-100": 0.57
};
var dicc3 = {
  "00-10": 0.8,
  "10-20": 0.5,
  "20-30": 0.23,
  "30-40": 0.25,
  "40-50": 0.90,
  "50-60": 0.98,
  "60-70": 0.13,
  "70-80": 0.72,
  "80-90": 0.65,
  "90-100": 0.78
};
var diccList = [dicc0, dicc1, dicc2, dicc3];
function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
  background('#a5c7ff');
  triangles();
  initDimensions = (windowWidth, windowHeight);
}

function draw() {
  if (page) {
    console.log(page);
    richGame(diccList[page]);
  } if (page == 0) {
    if (start == true) {
      for (i=1; i<255; i++){
      fade = fade++;
      fill(color(255, 255, 255, fade));
      rect(0 , 0, windowWidth, windowHeight, 5, 5, 5, 5);
    }
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
    }
    titleScreen();
    begin();
  } else if (page >= diccList.length) {
    endGame();
  }
}
  if (page) {
    console.log(page);
    richGame(diccList[page]);
  } else {
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
  }




function mousePressed() {
  page++;
  clearPage(initDimensions);
  if (page >= diccList.length) {
    endGame();
  }
}
