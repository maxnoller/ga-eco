class Vehicle {
  constructor(x, y, dna) {
    var mutation_rate = 0.01;
    this.acceleration = createVector(0, 0);
    this.velocity = createVector(0, -2);
    this.position = createVector(x, y);
    this.r = 4;
    this.maxspeed = 5;
    this.maxforce = 0.3;

    this.health = 1;

    this.dna = [];
    if(dna === undefined){
    //Food Weight
    this.dna[0] = random(-5, 5);
    //Poison weight
    this.dna[1] = random(-5, 5);
    //Food perception
    this.dna[2] = random(0, 100);
    //Poison perception
    this.dna[3] = random(0, 100);
    //low hp poison evasion
    this.dna[4] = random(-5,5)
  } else {
    this.dna[0] = dna[0];
    if(random(1) < mutation_rate){
      this.dna[0] += random(-0.1, 0.1);
    }
    this.dna[1] = dna[1];
    if(random(1) < mutation_rate){
      this.dna[1] += random(-0.1, 0.1);
    }
    this.dna[2] = dna[2];
    if(random(1) < mutation_rate){
      this.dna[2] += random(-10, 10);
    }
    this.dna[3] = dna[3];
    if(random(1) < mutation_rate){
      this.dna[3] += random(-10, 10);
    }
    this.dna[4] = dna[4];
  }
  }
  update() {
    this.health -= 0.005;
    // Update velocity
    this.velocity.add(this.acceleration);
    // Limit speed
    this.velocity.limit(this.maxspeed);
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

    var desired = p5.Vector.sub(target, this.position); // A vector pointing from the location to the target

    // Scale to maximum speed
    desired.setMag(this.maxspeed);

    // Steering = Desired minus velocity
    var steer = p5.Vector.sub(desired, this.velocity);
    steer.limit(this.maxforce); // Limit to maximum steering force

    return steer;
  }

  behaviors(good, bad){
    var steerG = this.eat(good, 0.3, this.dna[2]);
    var steerB = this.eat(bad, -0.75, this.dna[3]);

    steerG.mult(this.dna[0]);
    steerB.mult(this.dna[1]*((1-this.hp)*this.dna[4]));

    this.applyForce(steerG);
    this.applyForce(steerB);
  }

  clone(){
    if(random(1) < 0.001){
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

      if (d < this.maxspeed){
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

    return createVector(0,0);
  }

  dead(){
    return (this.health < 0);
  }

  boundaries() {
    var d = 25;
    let desired = null;

    if (this.position.x < d) {
      desired = createVector(this.maxspeed, this.velocity.y);
    } else if (this.position.x > width - d) {
      desired = createVector(-this.maxspeed, this.velocity.y);
    }

    if (this.position.y < d) {
      desired = createVector(this.velocity.x, this.maxspeed);
    } else if (this.position.y > height - d) {
      desired = createVector(this.velocity.x, -this.maxspeed);
    }

    if (desired !== null) {
      desired.normalize();
      desired.mult(this.maxspeed);
      let steer = p5.Vector.sub(desired, this.velocity);
      steer.limit(this.maxforce);
      this.applyForce(steer);
    }
}

generate_debug_visuals(){
  if(show_debug_information){
    stroke(0,255,0);
    noFill();
    line(0,0,0,-this.dna[0]*20);
    ellipse(0,0,this.dna[2]*2)
    stroke(255,0,0)
    line(0,0,0,-this.dna[1]*20)
    ellipse(0,0,this.dna[3]*2)
  }
}

  display() {
    // Draw a triangle rotated in the direction of velocity
    var angle = this.velocity.heading() + PI / 2;
    push();
    translate(this.position.x, this.position.y);
    rotate(angle);

    this.generate_debug_visuals();

    var green = color(0,255,0);
    var red = color(255,0,0);
    var col = lerpColor(red, green, this.health);

    fill(col);
    stroke(col);
    strokeWeight(1);
    beginShape();
    vertex(0, -this.r * 2);
    vertex(-this.r, this.r * 2);
    vertex(this.r, this.r * 2);
    endShape(CLOSE);
    pop();
  }
}