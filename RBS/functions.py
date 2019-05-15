from math import inf


class TriangularFunction:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def compute(self, x):
        first = (x - self.__a) / (self.__b - self.__a)
        second = (self.__c - x) / (self.__c - self.__b)
        return max(0, min(first, 1, second))

    def getValues(self):
        return [self.__a, self.__b, self.__c]

    def center(self):
        return self.__b

    def __str__(self):
        return "Triangular function with values = [" + str(self.__a) + ", " + str(self.__b) + ", " + str(self.__c) + "]"


class TrapezoidalFunction:
    def __init__(self, a,  b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def compute(self, x):
        if self.__b == self.__a == inf:
            if self.__d == self.__c:
                return 1
            return max(0, min(1, (self.__d - x) / (self.__d - self.__c)))
        if self.__c == self.__d == inf:
            if self.__b == self.__a:
                return 1
            return max(0, min((x - self.__a) / (self.__b - self.__a), 1))

    def getValues(self):
        return [self.__a, self.__b, self.__c, self.__d]

    def center(self):
        if self.__b == inf:
            return self.__c
        if self.__c == inf:
            return self.__b

    def __str__(self):
        return "Trapezoidal function with values = [" + str(self.__a) + ", " + str(self.__b) + ", " + \
               str(self.__c) + ", " + str(self.__d) + "]"
