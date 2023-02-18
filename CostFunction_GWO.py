"""

@authors: Sahar Babaei, Mohammad Reza Rastegaran

"""

import numpy
import math


# define the function blocks
def prod(items):
    product = 1
    for number in items:
        product *= number
    return product


def fitness_1(x):
    s = numpy.sum(x ** 2)
    return s


def fitness_2(x):
    o = sum(abs(x)) + prod(abs(x))
    return o


def fitness_3(x):
    dim = len(x) + 1
    o = 0
    for i in range(1, dim):
        o = o + (numpy.sum(x[0:i])) ** 2
    return o


def fitness_4(x):
    o = max(abs(x))
    return o


def fitness_5(x):
    dim = len(x)
    o = numpy.sum(100 * (x[1:dim] - (x[0:dim - 1] ** 2)) ** 2 + (x[0:dim - 1] - 1) ** 2)
    return o


def fitness_6(x):
    o = numpy.sum(abs((x + .5)) ** 2)
    return o


def fitness_7(x):
    dim = len(x)
    w = [i for i in range(len(x))]
    for i in range(0, dim):
        w[i] = i + 1
    o = numpy.sum(w * (x ** 4)) + numpy.random.uniform(0, 1)
    return o


def fitness_8(x):
    o = sum(-x * (numpy.sin(numpy.sqrt(abs(x)))))
    return o


def fitness_9(x):
    dim = len(x)
    o = numpy.sum(x ** 2 - 10 * numpy.cos(2 * math.pi * x)) + 10 * dim
    return o


def fitness_10(x):
    dim = len(x)
    o = -20 * numpy.exp(-.2 * numpy.sqrt(numpy.sum(x ** 2) / dim)) - numpy.exp(
        numpy.sum(numpy.cos(2 * math.pi * x)) / dim) + 20 + numpy.exp(1)
    return o
