from .world_tile import WorldTile

class FoodTile(WorldTile):
    def __init__(self, x, y, max_food):
        self.food = max_food
        self.food_portion = 50
        self.position = (x,y)
        
    def get_color(self):
        return (0, self.food * 255 // 100, 0)

    def eat(self):
        if(self.food >= self.food_portion):
            self.food -= self.food_portion
            return True
        return False

