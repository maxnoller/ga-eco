from .world_tile import WorldTile

class FoodTile(WorldTile):
    def __init__(self, x, y, max_food):
        self.food = max_food
        self.food_portion = 50
        self.position = (x,y)
        self.update_color()
        
    def get_color(self):
        return self.color

    def change_food(self, food):
        self.food += food
        self.update_color()

    def update_color(self):
        self.color = (0, self.food * 255 // 100, 0)

    def eat(self):
        if(self.food >= self.food_portion):
            self.change_food(-self.food_portion)
            return True
        return False

    def __str__(self):
        return "FT"

