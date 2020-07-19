class Genome{
  constructor(name, min, max, value){
    this.name = name;
    this.min = min;
    this.max = max;
    if(value){
      this.value = value;
    } else {
      this.value = random(min, max);
    }

  }
}
