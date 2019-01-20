// xCor, yCor
// R G B opacity
// fill(color(255, 255, 255, titleTransitionWhite));
function printXlabel(xCor, yCor, key) {
  console.log("we really here");
  fill(0, 102, 153);
  textSize(32);
  text('word',xCor, yCor);
}

// colour is a string of the hex value of the colour with # infront
// this function draws with shadows
function drawBox(R,G,B,xCor, fraction) {
  // console.log(fraction);
  var barHeight = 300;
  var boxRadius = 5;
  var baseY = 500;

  var height =  barHeight*fraction;
  var yCor = baseY - height;

  // (x,y) coordinate ; // width and height
  fill((color(R-10,G-10,B-20)));
  rect(xCor+3, yCor+3, 55, height, boxRadius);
  fill((color(R,G,B)));
  rect(xCor, yCor, 55, height, boxRadius);
  printXlabel(xCor, baseY + 30, key)
}

function richGame(diccionario) {
  // console.log(page);
  var barHeight = 300;
  var barWidth = 50;
  var barSpace = 30;
  var baseX = 350;
  var baseY = 500;
  var xCor = 90;
  var firstBarSpace = 20;

  // returns a list of keys to the dictionary
  const keys = Object.keys(diccionario);

  // iterate over the keys to print the values
  for (i=0;i<(keys.length);i++) {
    // console.log(keys[i]);
    xCor = baseX + i*(barSpace+barWidth);
    drawBox(255,179,98,xCor + firstBarSpace,diccionario[keys[i]]);
  }
  var xAxisLength = i*(barSpace+barWidth) + firstBarSpace;

  //print the box starting from the base to the top
  fill('#000000');

  // this is the horizontal line
  rect(baseX, baseY + 3,xAxisLength,3);
  var height =  30 + barHeight;
  var yCor = baseY - height + 6;
  // Draw a rectangle at location (30, 20) with a width and height
  // this is the horizontal
  rect(baseX - 3, yCor,3,height);

}


function endGame(initDimensions) {
  console.log("End Game");
  background('#000000');
  drawBox(0,0,initDimensions[0], initDimensions[1]);
}
