import p5 from 'p5';
import DNA from "./dna";

export default class Vehicle {
  constructor(p, x, y, width, height, dna) {
    var mutation_rate = 0.01;
    this.p = p;
    this.acceleration = this.p.createVector(0, 0);
    this.velocity = this.p.createVector(0, -2);
    this.position = this.p.createVector(x, y);
    this.r = 4;
    this.width = width;
    this.height = height;
    this.maxspeed = 5;
    this.maxforce = 0.3;
    this.show_debug_information = true;

    this.health = 1;

    if(dna){
      this.dna = new DNA(p, 0.01, dna);
      this.dna.mutate();
    } else {
      this.dna = new DNA(p, 0.01);
    }
  }
  this.p.update = function(){
    let food_consumption = 0.002;
    this.health -= food_consumption*this.dna.max_speed.value;
    // Update velocity
    this.velocity.add(this.acceleration);
    // Limit speed
    this.velocity.limit(this.dna.max_speed.value);
    this.position.add(this.velocity);
    // Reset accelerationelertion to 0 each cycle
    this.acceleration.mult(0);
  }

  applyForce(force) {
    // We could add mass here if we want A = F / M
    this.acceleration.add(force);
  }

  // A method that calculates a steering force towards a target
  // STEER = DESIRED MINUS VELOCITY
  seek(target) {

    var desired = this.p.Vector.sub(target, this.position); // A vector pointing from the location to the target

    // Scale to maximum speed
    desired.setMag(this.dna.max_speed.value);

    // Steering = Desired minus velocity
    var steer = this.p.Vector.sub(desired, this.velocity);
    steer.limit(this.maxforce); // Limit to maximum steering force

    return steer;
  }

  behaviors(good, bad){
    var steerG = this.eat(good, 0.3, this.dna.food_perception.value);
    var steerB = this.eat(bad, -0.75, this.dna.poison_perception.value);

    steerG.mult(this.dna.food_weight.value);
    steerB.mult(this.dna.poison_weight.value);

    this.applyForce(steerG);
    this.applyForce(steerB);
  }

  clone(){
    if(this.p.random(1) < 0.001){
      return new Vehicle(this.position.x, this.position.y, this.dna);
    } else {
      return null;
    }
  }

  eat(list, nutrition, perception) {
    var record = Infinity;
    var closest = null;
    for (var i = list.length-1; i>=0 ; i--){
      var d = this.position.dist(list[i]);

      if (d < this.dna.max_speed.value){
        list.splice(i,1);
        this.health += nutrition;
      } else {

      if (d < record && d < perception){
        record = d;
        closest = list[i];
      }
    }
    }
    if (closest != null){
      return this.seek(closest);
    }

    return this.p.createVector(0,0);
  }

  dead(){
    return (this.health < 0);
  }

  boundaries() {
    var d = 25;
    let desired = null;

    if (this.position.x < d) {
      desired = this.p.createVector(this.maxspeed, this.velocity.y);
    } else if (this.position.x > this.width - d) {
      desired = this.p.createVector(-this.maxspeed, this.velocity.y);
    }

    if (this.position.y < d) {
      desired = this.p.createVector(this.velocity.x, this.maxspeed);
    } else if (this.position.y > this.height - d) {
      desired = this.p.createVector(this.velocity.x, -this.maxspeed);
    }

    if (desired !== null) {
      desired.normalize();
      desired.mult(this.maxspeed);
      let steer = this.p.Vector.sub(desired, this.velocity);
      steer.limit(this.maxforce);
      this.applyForce(steer);
    }
}

generate_debug_visuals(){
  if(this.show_debug_information){
    this.p.stroke(0,255,0);
    this.p.noFill();
    this.p.line(0,0,0,-this.dna.food_weight.value*20);
    this.p.ellipse(0,0,this.dna.food_perception.value*2);
    this.p.stroke(255,0,0);
    this.p.line(0,0,0,-this.dna.poison_weight.value*20);
    this.p.ellipse(0,0,this.dna.poison_perception.value*2);
  }
}

  this.p.display() {
    // Draw a triangle rotated in the direction of velocity
    var angle = this.velocity.heading() + this.p.PI / 2;
    this.p.push();
    this.p.translate(this.position.x, this.position.y);
    this.p.rotate(angle);

    this.generate_debug_visuals();

    var green = this.p.color(0,255,0);
    var red = this.p.color(255,0,0);
    var col = this.p.lerpColor(red, green, this.health);

    this.p.fill(col);
    this.p.stroke(col);
    this.p.strokeWeight(1);
    this.p.beginShape();
    this.p.vertex(0, -this.r * 2);
    this.p.vertex(-this.r, this.r * 2);
    this.p.vertex(this.r, this.r * 2);
    this.p.endShape(this.p.CLOSE);
    this.p.pop();
  }
}
