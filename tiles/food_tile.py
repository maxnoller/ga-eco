from .world_tile import WorldTile

class FoodTile(WorldTile):
    def __init__(self, max_food, regeneration_rate):
        self.food = max_food
        self.food_portion = 50
        self.regeneration_rate = regeneration_rate
        self.update_color()

    def update(self, delta_time):
        if(self.food == 100): return
        self.change_food(delta_time/1000 * self.regeneration_rate)
        
    def get_color(self):
        return self.color

    def change_food(self, food):
        self.food += food
        if(self.food < 0):
            self.food = 0
        elif(self.food > 100):
            self.food = 100
        self.update_color()

    def update_color(self):
        self.color = (0, self.food * 250 // 100 + 5, 0)

    def eat(self):
        if(self.food >= self.food_portion):
            self.change_food(-self.food_portion)
            return True
        return False

    def __str__(self):
        return "FT"

