class WorldTile:
    def __init__(self, x, y):
        self.position = (x,y)

class FoodTile(WorldTile):
    def __init__(self, max_food, regenration_rate):
        self.food = max_food
        self.food_portion = 1

    def eat(self):
        if(self.food >= self.food_portion):
            self.food - self.food_portion
            return True
        return False