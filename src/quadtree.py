from dataclasses import dataclass
import math
from typing import List
from numba import jit
from creature import Creature

class Node:
    pass

@dataclass
class Leaf(Node):
    instance: Creature
    x: int
    y: int

class QuadTree:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root = Box(0, 0, width, height)

    def insert(self, creature: Creature, x: int, y: int):
        leaf = Leaf(instance=creature, x=x, y=y)
        self.root.insert(leaf)

    def remove(self, creature: Creature):
        self.root.remove(self.root.find_creature(creature))

    def find_by_creature(self, creature: Creature) -> Leaf:
        return self.root.find(creature)

    def find(self, x: int, y: int) -> Creature:
        return self.root.find(x, y).instance

    def get_neighbors(self, x: int, y:int, r: int):
        return self.root.all_within(x, y, r)

    def all(self):
        return [a.instance for a in self.root.all()]

class Box(Node):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.childs = []

    #@jit(nopython=True)
    def within_bounds(self, x: int, y: int) -> bool:
        if (x < self.x or y < self.y or x > self.x+self.width or y > self.y+self.height):
            return False
        return True

    def split_up(self):
        temp_childs = self.childs.copy()
        width = self.width
        height = self.height
        self.childs = [Box(self.x, self.y, int(width/2), int(height/2)),
                       Box(int(width/2), self.y, int(width/2), int(height/2)),
                       Box(self.x, int(height/2), int(width/2), int(height/2)),
                       Box(int(width/2), int(height/2), int(width/2), int(height/2))]
        for child in temp_childs:
            self.insert(child)

    def remove(self, leaf: Leaf) -> bool:
        if self.within_bounds(leaf.x, leaf.y) and leaf in self.childs: 
            self.childs.remove(leaf)
            return True
        for child in self.childs:
            if(isinstance(child, Box) and child.within_bounds(leaf.x, leaf.y)):
                return child.remove(leaf)


    def find_creature(self, creature: Creature) -> Leaf:
        #TODO: Multiproccessing
        if(len(self.childs) != 0):
            for child in self.childs:
                if(isinstance(child, Leaf)):
                    if(child.instance == creature):
                        return child
                elif(isinstance(child, Box)):
                    result = child.find_creature(creature)
                    if(result is not None):
                        return result
        return None

    def find(self, x: int, y: int) -> Leaf:
        if(self.within_bounds(x,y)):
            for child in self.childs:
                if(isinstance(child, Leaf)):
                    if(child.x == x and child.y == y):
                        return child
                else:
                    if(child.within_bounds(x,y)):
                        return self.child.find(x,y)
        return None

    def all(self) -> List[Leaf]:
        childs = []
        for child in self.childs:
            if(isinstance(child, Leaf)):
                childs.append(child)
            else:
                childs.extend(child.all())
        return childs

    def all_within(self, x: int, y:int, r:int) -> List[Leaf]:
        childs_within = []
        if(self.intersects_circle(x,y,r)):
            for child in self.childs:
                if(isinstance(child, Leaf)):
                    distance_x = abs(child.x - x)
                    distance_y = abs(child.y-y)
                    if(distance_x <= r and distance_y <= r):
                        if math.sqrt(distance_x**2 + distance_y**2 ) <= r:
                            childs_within.append(child)
                else:
                    if(child.intersects_circle(x,y,r)):
                        childs_within.extend(child.all_within(x,y,r))
        return childs_within

    #@jit(nopython=True)
    def intersects_circle(self, x: int, y:int, r: int) -> bool:
        distanceX = abs(x-self.x)
        distanceY = abs(y-self.y)

        if(distanceX > (self.width/2+r)): return False
        if(distanceY > (self.height/2+r)): return False
        if(distanceX <= (self.width/2)): return True
        if(distanceY <= (self.height/2)): return True

        corner_distance_squared = (distanceX - self.width/2)**2 + (distanceY-self.height/2)**2

        return corner_distance_squared <= (r**2)



    def insert(self, leaf: Leaf) -> bool:
        if(not self.within_bounds(leaf.x, leaf.y)):
            return False

        for child in self.childs:
            if(isinstance(child, Box)):
                if(child.within_bounds(leaf.x, leaf.y)):
                    return child.insert(leaf)
        
        if(len(self.childs) < 4):
            self.childs.append(leaf)
            #print(f"Adding leaf with coordinates: x:{leaf.x} y:{leaf.y}")
            return True

        if(any(isinstance(temp, Leaf) for temp in self.childs)):
            self.split_up()
            return self.insert(leaf)
        return False

        


        
