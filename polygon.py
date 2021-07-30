from functools import lru_cache
import math

class Polygon:
    def __init__(self, vertices, circumradius):
        self.vertices = vertices
        self.circumradius = circumradius

    def __repr__(self)->str:
        return f"Polygon with {self.vertices} sides and {self.circumradius} as circumradius"
    
    def __eq__(self,other):
        if isinstance(other, Polygon):
            return ((self.vertices == other.vertices) and (self.circumradius == other.circumradius))
        return  False

    def get_number_of_vertices(self):
        return (self.vertices)

    def circum_radius(self):
        return (self.circumradius)
    
    def interior_angle(self):
        if self.vertices < 3 or self.circumradius <= 0:
            raise ValueError("Number of vertices should not be less than 3 and circumradius should be greater than 0")
        else:
            return (self.vertices - 2) * 180/self.vertices

    def edge_length(self):
        if self.vertices < 3 or self.circumradius <= 0:
            raise ValueError("Number of vertices should not be less than 3 and circumradius should be greater than 0")
        else:
            return 2 * self.circumradius * math.sin(math.pi/self.vertices)

    def apothem(self):
        if self.vertices < 3 or self.circumradius <= 0:
            raise ValueError("Number of vertices should not be less than 3 and circumradius should be greater than 0")
        else:
            return self.circumradius * math.cos(math.pi/self.vertices)
        
    def area(self):
        return 1/2 * self.edge_length() * self.apothem() * self.get_number_of_vertices()

    def perimeter(self):
        return self.get_number_of_vertices() * self.edge_length()
    
    def __repr__(self):
        return f'Polygon has {self.vertices} number of sides and {self.circumradius} as circumradius'
    
    def __len__(self):
        return len((self.vertices, self.circumradius))