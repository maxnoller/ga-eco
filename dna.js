class DNA {
  constructor(dna_){
    if(dna_){
      this.food_weight = new Genome("food_weight", -5, 5, dna_.food_weight.value);
      this.poison_weight = new Genome("poison_weight", -5, 5, dna_.poison_weight.value);
      this.food_perception = new Genome("food_perception", 0, 100, dna_.food_perception.value);
      this.poison_perception = new Genome("poison_perception", 0, 100, dna_.poison_perception.value);
      this.max_speed = new Genome("max_speed", 0.1, 10, dna_.max_speed.value);
    } else {
      this.food_weight = new Genome("food_weight", -5, 5);
      this.poison_weight = new Genome("poison_weight", -5, 5);
      this.food_perception = new Genome("food_perception", 0, 100);
      this.poison_perception = new Genome("poison_perception", 0, 100);
      this.max_speed = new Genome("max_speed", 1, 10)
    }
  }
  mutate(){
    for (var property in this) {
      if (this.hasOwnProperty(property)) {
        if(random(1) < mutation_chance){
          this[property].value += random(this[property].min*0.1, this[property].max*0.1);
        }
      }
    }
  }
}
