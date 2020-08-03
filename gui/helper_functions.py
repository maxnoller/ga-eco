import numpy as np
from numba import jit

class GuiHelperFunctions:
    @staticmethod
    def convert_rel_to_abs_cords(relative_coordinates, center_point):
        return_coordinates = []
        for (x,y) in relative_coordinates:
            return_coordinates.append((center_point[0]+x, center_point[1]+y))
        return return_coordinates


    @staticmethod
    def convert_creature_cords(coordinates, alpha):
        return [GuiHelperFunctions.convert_creature_cord(x, y, alpha) for (x, y) in coordinates]

    @staticmethod
    def convert_creature_cord(x, y, alpha):
        (rho, phi) = GuiHelperFunctions.cart2pol(x, y)
        return GuiHelperFunctions.pol2cart(rho, phi+np.deg2rad(alpha))


    @staticmethod
    @jit(nopython=True)
    def cart2pol(x, y):
        rho = np.sqrt(np.square(x) + np.square(y))
        phi = np.arctan2(y, x)
        return (rho, phi)

    @staticmethod
    @jit(nopython=True)
    def pol2cart(rho, phi):
        x = np.multiply(rho, np.cos(phi))
        y = rho * np.sin(phi)
        return(x, y)