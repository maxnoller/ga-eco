import p5 from "p5";

export default class Genome{
  constructor(p, name, min, max, value){
    this.name = name;
    this.min = min;
    this.max = max;
    if(value){
      this.value = value;
    } else {
      this.value = p.random(min, max);
    }

  }
}
