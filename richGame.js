// xCor, yCor
// R G B opacity
// fill(color(255, 255, 255, titleTransitionWhite));

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

  for (i=1; i<height;i++) {
    fill((color(R-10,G-10,B-20)));
    rect(xCor+3, yCor+3, 55, i, boxRadius);
    fill((color(R,G,B)));
    rect(xCor, yCor, 55, i, boxRadius);
  }
}

function richGame(page) {
  // console.log(page);
  var barHeight = 300;
  var barWidth = 50;
  var barSpace = 50;
  var baseX = 50;
  var baseY = 500;
  var xCor = 90;

  var diccionario = {
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
  // returns a list of keys to the dictionary
  const keys = Object.keys(diccionario);
  for (i=0;i<(keys.length);i++) {
    // console.log(keys[i]);
    xCor = baseX + i*(barSpace+barWidth);
    drawBox(255,179,98,xCor,diccionario[keys[i]]);
  }
  var xAxisLength = i*(barSpace+barWidth);

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
