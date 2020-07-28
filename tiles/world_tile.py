class WorldTile:
    def __init__(self, x, y):
        self.position = (x,y)

    def get_color(self):
        return (255, 255, 255)
    
    def __str__(self):
        return "WorldTile({},{})".format(self.position[0],
                                         self.position[1])