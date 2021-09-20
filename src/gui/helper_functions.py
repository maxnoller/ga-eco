import numpy as np

class GuiHelperFunctions:
    @staticmethod
    def convert_rel_to_abs_cords(relative_coordinates, center_point):
        return_coordinates = []
        for (x,y) in relative_coordinates:
            return_coordinates.append((center_point[0]+x, center_point[1]+y))
        return return_coordinates


    @staticmethod
    def convert_creature_cords(coordinates, alpha):
        return_coordinates = []
        for (x,y) in coordinates:
            (rho, phi) = GuiHelperFunctions.cart2pol(x,y)
            return_coordinates.append(GuiHelperFunctions.pol2cart(rho,phi+np.deg2rad(alpha)))
        return return_coordinates

    @staticmethod
    def cart2pol(x, y):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        return(rho, phi)

    @staticmethod
    def pol2cart(rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        return(x, y)