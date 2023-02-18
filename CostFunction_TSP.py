import array

import numpy

import City


class CostFunction:
    def __init__(self, route):
        self.route = route
        self.fitness = 0.0

    def route_distance(self) -> int:
        """
        Given a list of cities to traverse, traverse from the first city,
        reach every other city in the route list,
        at Last, return to the starting city
        ====>> [route..., route[0]]

        :return: calculated weight of the route of cities passed in to the constructor
        :rtype: int
        """
        route_len = len(self.route)
        overall_distance = 0
        if self.fitness == 0:
            for i in range(route_len):
                from_city = self.route[i]
                if i < route_len - 1:
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                overall_distance += from_city.distance_from(to_city)

        if self.fitness == 0:
            self.fitness = overall_distance

        return self.fitness
