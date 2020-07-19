import Vehicle from "./vehicle";

export default function environmentSketch (p) {
  let width = 0;
  let height = 0;
  let vehicles = [];
  let food = [];
  let poison = [];
  var show_debug_information = true;
  let mutation_chance = 0.05;
  let vehicle_count = 1;

  let food_generation_chance = 0.1;
  let poison_generation_chance = 0.01;

  p.setup = function ( ) {
    p.createCanvas(width, width/2);

    generate_vehicles(10);
    generate_resources(food, 30);
    generate_resources(poison, 10);
  };

  p.myCustomRedrawAccordingToNewPropsHandler = function (props) {
    if (props.width){
      width = props.width;
      height = props.height;
    }
  };

  p.draw = function () {
    p.background(100);
    p.noStroke();
  };
  p.windowResized = function () {
    p.resizeCanvas(width, width/2);
  };

  function generate_resources(list, count){
    for (var i = 0; i < count; i++){
      var x = p.random(width);
      var y = p.random(height);
      list.push(p.createVector(x, y));
    }
  }

  function generate_vehicles(count){
    if(!count){
      count = vehicle_count
    }
    for (var i = 0; i<count; i++){
      var x = p.random(width);
      var y = p.random(height);
      vehicles.push(new Vehicle(p, x, y, width, height));
    }
  }
};
