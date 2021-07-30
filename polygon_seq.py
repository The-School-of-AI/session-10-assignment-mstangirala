
from functools import lru_cache
from session10 import Polygon

class Polygon_Sequence:

    def __init__(self,vertices,circumradius):
        self.vertices = vertices
        self.circumradius = circumradius
        self.ratios = dict()

    def __len__(self):
        return self.vertices
    
    def __repr__(self)->str:
        return f"Polygon with {self.vertices} sides and {self.circumradius} as circumradius"

    def __getitem__(self,vertex):
        if isinstance(vertex, int):
            if vertex < 0:
                vertex = self.vertices + vertex
            if vertex < 0 or vertex >= self.vertices:
                raise IndexError
            else:
                if vertex>1:
                    return Polygon_Sequence._ratio(vertex,self.circumradius)
                else:
                    return 'it is not a polygon'
        else:
            raise IndexError
            
    @staticmethod
    @lru_cache(2 ** 10)
    def _ratio(vertices:int,circumradius:int)->float:
        if vertices < 2:
            return 1
        else:
            p1 = Polygon(vertices,circumradius)
            return p1.area/p1.perimeter
    
    @property
    def max_efficieny(self)->str:
        for i in range(self.vertices):
            if i> 1:
                self.ratios[i+1] = self.__getitem__(i)
        key = max(self.ratios,key = self.ratios.get)
        return f"Max Ratio is {self.ratios[key]} at vertex {key}"
