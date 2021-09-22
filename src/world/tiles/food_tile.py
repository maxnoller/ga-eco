from .world_tile import WorldTile

class FoodTile(WorldTile):
    """A tile which contains food and can be eaten"""    
    def __init__(self, max_food: int, regeneration_rate: float):
        self.max_food = max_food
        self.food = max_food
        self.food_portion = 50
        self.regeneration_rate = regeneration_rate
        self.update_color()

    def update(self, delta_time: float):
        if(self.food == 100): return
        self.change_food(delta_time/1000 * self.regeneration_rate)
        
    def get_color(self):
        return self.color

    def change_food(self, food: int):
        """Change the food by the given value. Food will always stay between 0 and the specified maximum"""
        self.food += food
        if(self.food < 0):
            self.food = 0
        elif(self.food > self.max_food):
            self.food = self.max_food
        self.update_color()

    def update_color(self):
        self.color = (0, self.food * 250 // 100 + 5, 0)

    def eat(self) -> bool:
        if(self.food >= self.food_portion):
            self.change_food(-self.food_portion)
            return True
        return False

    def __str__(self) -> str:
        return "FT"

