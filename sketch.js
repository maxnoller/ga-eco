
// Evolution EcoSystem
// Daniel Shiffman <http://www.shiffman.net>
// The Nature of Code

// A World of creatures that eat food
// The more they eat, the longer they survive
// The longer they survive, the more likely they are to reproduce
// The bigger they are, the easier it is to land on food
// The bigger they are, the slower they are to find food
// When the creatures die, food is left behind


let vehicles = [];
let food = [];
let poison = [];
let show_debug_information = true;

function setup() {
  createCanvas(640, 360);
  checkbox = createCheckbox('Debug Information', true);
  checkbox.changed(debugInformationChanged);
  for (var i = 0; i<10; i++){
    var x = random(width);
    var y = random(height);
    vehicles[i] = new Vehicle(x, y);
  }
  for (var i = 0; i < 20; i++){
    var x = random(width);
    var y = random(height);
    food.push(createVector(x, y));
  }
  for (var i = 0; i < 10; i++){
    var x = random(width);
    var y = random(height);
    poison.push(createVector(x, y));
  }
}

function draw() {
  background(51);

  if (random(1) < 0.1){
    var x = random(width);
    var y = random(height);
    food.push(createVector(x, y));
  }
  if (random(1) < 0.01){
    var x = random(width);
    var y = random(height);
    poison.push(createVector(x, y));
  }

  let target = createVector(mouseX, mouseY)

  for (var i = 0; i < food.length; i++){
    fill(0,255,0);
    noStroke();
    ellipse(food[i].x, food[i].y, 4, 4);
  }
  for (var i = 0; i < poison.length; i++){
    fill(255,0,0);
    noStroke();
    ellipse(poison[i].x, poison[i].y, 4, 4);
  }
  for (var i = vehicles.length-1; i>=0;i--){
    vehicles[i].boundaries();
    vehicles[i].behaviors(food, poison);
    vehicles[i].update();
    vehicles[i].display();

    var newVehicle = vehicles[i].clone();
    if(newVehicle != null){
      vehicles.push(newVehicle);
    }

    if (vehicles[i].dead()){
      var x = vehicles[i].position.x;
      var y = vehicles[i].position.y;
      food.push(createVector(x,y));

      vehicles.splice(i,1);
    }


  }
}
function debugInformationChanged(){
  show_debug_information = this.checked();
}
