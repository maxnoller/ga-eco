import unittest

from world import FoodTile

class TestFoodTile(unittest.TestCase):
    def test_eat(self):
        full_food_tile = FoodTile(100, 1)
        self.assertTrue(full_food_tile.eat())
        empty_food_tile = FoodTile(0,1)
        self.assertFalse(empty_food_tile.eat())

    def test_update(self):
        tile = FoodTile(100,1)
        tile.change_food(-100)
        tile.update(5000)
        self.assertEqual(tile.food, 5)
    
    def test_change_food(self):
        tile = FoodTile(100,1)
        tile.change_food(-50)
        self.assertEqual(tile.food, 50)
        tile.change_food(50)
        self.assertEqual(tile.food, 100)