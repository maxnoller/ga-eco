
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
let mutation_chance = 0.05;
let vehicle_count = 1;

let food_generation_chance = 0.1;
let poison_generation_chance = 0.01;

function setup() {
  createCanvas(640, 360);
  debug_information_checkbox = createCheckbox('Debug Information', true);
  debug_information_checkbox.changed(debugInformationChanged);

  generate_vehicle_input = createInput("1");
  generate_vehicle_input.input(vehicle_count_changed);
  generate_button = createButton("Generate new Vehicles");
  generate_button.mousePressed(generate_vehicles)

  food_generation_chance_input = createInput(food_generation_chance);
  food_generation_chance_input.input(food_generation_chance_changed);
  poison_generation_chance_input = createInput(poison_generation_chance);
  poison_generation_chance_input.input(poison_generation_chance_changed);

  generate_vehicles(10);
  generate_resources(food, 30);
  generate_resources(poison, 10);
}

function draw() {
  background(51);

  if (random(1) < food_generation_chance){
    generate_resources(food, 1)
  }
  if (random(1) < poison_generation_chance){
    generate_resources(poison, 1)
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
function generate_resources(list, count){
  for (var i = 0; i < count; i++){
    var x = random(width);
    var y = random(height);
    list.push(createVector(x, y));
  }
}

function generate_vehicles(count){
  if(!count){
    count = vehicle_count
  }
  for (var i = 0; i<count; i++){
    var x = random(width);
    var y = random(height);
    vehicles.push(new Vehicle(x, y));
  }
}

function debugInformationChanged(){
  show_debug_information = this.checked();
}

function vehicle_count_changed(){
  vehicle_count = this.value();
}

function food_generation_chance_changed(){
  food_generation_chance = this.value();
}

function poison_generation_chance_changed(){
  poison_generation_chance = this.value();
}
