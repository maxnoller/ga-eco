class DNA:
    def __init__(self, max_health, max_food, hunger_loss, hunger_damage):
        self.max_health = max_health
        self.max_food = max_food
        self.hunger = hunger_loss
        self.hunger_damage = hunger_damage
        self.speed_modifier = 0.7
        self.reproduce_cooldown = 30
        self.color = (0, 0, 255)

    