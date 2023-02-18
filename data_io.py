import random
from City import *

FILE_NAME = "cities.txt"

MIN = 0
MAX = 50
DEFAULT = 50


def generate(number=50, min=MIN, max=MAX):
    """
    Create random points (x,y) and save them to a .txt file

    :param number: number of cities to create
    :param min: minimum value a city coordinate can have
    :param max: maximum value a city coordinate can have

    """
    file = open(FILE_NAME, "w")
    for i in range(number):
        x, y = [random.randint(min, max), random.randint(min, max)]
        file.write(" ".join(str(v) for v in [i, x, y]))
        file.write("\n")
    file.close()


def read():
    """
    Return list of City samples from file
    :rtype: list<City>
    """
    cities_list = []
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            line = line.rstrip("\n") # exclude line-break
            index, x, y = line.split(" ") # extract coordinates
            cities_list.append(City(index,x, y)) # create and then append instance
    return cities_list
