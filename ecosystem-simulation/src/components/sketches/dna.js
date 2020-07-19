import p5 from "p5";
import Genome from "./genome.js";

export default class DNA {
  constructor(p, mutation_chance, dna_){
    this.mutation_chance = mutation_chance;
    if(dna_){
      this.food_weight = new Genome(p, "food_weight", -5, 5, dna_.food_weight.value);
      this.poison_weight = new Genome(p, "poison_weight", -5, 5, dna_.poison_weight.value);
      this.food_perception = new Genome(p, "food_perception", 0, 100, dna_.food_perception.value);
      this.poison_perception = new Genome(p, "poison_perception", 0, 100, dna_.poison_perception.value);
      this.max_speed = new Genome(p, "max_speed", 0.1, 10, dna_.max_speed.value);
    } else {
      this.food_weight = new Genome(p, "food_weight", -5, 5);
      this.poison_weight = new Genome(p, "poison_weight", -5, 5);
      this.food_perception = new Genome(p, "food_perception", 0, 100);
      this.poison_perception = new Genome(p, "poison_perception", 0, 100);
      this.max_speed = new Genome(p, "max_speed", 1, 10)
    }
  }
  mutate(){
    for (var property in this) {
      if (this.hasOwnProperty(property)) {
        if(p5.random(1) < this.mutation_chance){
          this[property].value += p5.random(this[property].min*0.1, this[property].max*0.1);
        }
      }
    }
  }
}
