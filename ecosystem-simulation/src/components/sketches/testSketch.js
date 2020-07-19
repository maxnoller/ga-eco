export default function testSketch (p) {
  let width = 0;

  p.setup = function ( ) {
    p.createCanvas(width, width/2);
  };

  p.myCustomRedrawAccordingToNewPropsHandler = function (props) {
    if (props.width){
      width = props.width;
    }
  };

  p.draw = function () {
    p.background(100);
    p.noStroke();
  };
  p.windowResized = function () {
    p.resizeCanvas(width, width/2);
  };

};
