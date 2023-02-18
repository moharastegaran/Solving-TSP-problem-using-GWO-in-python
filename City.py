from math import sqrt, pow

"""
This class is the modular presentation of cities in TSP problem

Each city consists of a pair of (x,y) coordinates
"""


class City:
    def __init__(self,index, x, y):
        self.x = int(x)
        self.y = int(y)
        self.i = int(index)

    def distance_from(self, city: "City") -> float:
        """
        :param city: the city to calc the distance to.
        :return: Euclidean distance between two cities
        """
        return sqrt(pow(self.x - city.x, 2) + pow(self.y - city.y, 2))

    def __str__(self) -> str:
        """
        :return: String representation of current instance
        """
        return '{{{},{}}}'.format(self.x, self.y)
