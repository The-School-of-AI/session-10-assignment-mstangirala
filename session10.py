import math

class Polygon:
    def __init__(self, vertices, circumradius):
        if vertices < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.vertices = vertices
        self.circumradius = circumradius

    def __repr__(self)->str:
        return f"Polygon with {self.vertices} sides and {self.circumradius} as circumradius"
    @property
    def get_number_of_vertices(self):
        return (self.vertices)
    @property
    def circum_radius(self):
        return (self.circumradius)

    @property
    def interior_angle(self):
        return (self.vertices - 2) * 180/self.vertices

    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin(math.pi/self.vertices)

    @property
    def apothem(self):
        return self.circumradius * math.cos(math.pi/self.vertices)

    @property
    def area(self):
        return 0.5*self.apothem*self.edge_length * self.vertices

    @property
    def perimeter(self):
        return self.vertices * self.edge_length

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return ((self.get_number_of_vertices == other.get_number_of_vertices) and (self.circum_radius == other.circum_radius))
        return  False

    def __gt__(self,other):
        if isinstance(other,self.__class__):
            return ((self.get_number_of_vertices > other.get_number_of_vertices) or (self.circum_radius > other.circum_radius))
        else:
            raise ValueError('incorrect polygon type')
