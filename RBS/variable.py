from functions import *


class FuzzyVariable:
    def __init__(self, name, labels=None, interval=None, functions=None):
        self.__name = name
        self.__labels = labels
        self.__interval = interval
        self.__functions = functions

    def getName(self):
        return self.__name

    def getLabels(self):
        return self.__labels

    def getInterval(self):
        return self.__interval

    def getFunctions(self):
        return self.__functions

    def setName(self, name):
        self.__name = name

    def setLabels(self, labels):
        self.__labels = labels

    def setInterval(self, interval):
        self.__interval = interval

    def setFunctions(self, functions):
        self.__functions = functions

    def noOfLabels(self):
        return len(self.__labels)

    def getValues(self):
        values = []
        for func in self.__functions:
            values += func.getValues()
        result = set(values)
        result.remove(inf)
        return list(result)

    def __str__(self):
        s = "Name: " + self.__name + ", Labels: " + str(self.__labels) + ", Interval: " + str(self.__interval)
        for func in self.__functions:
            s += "\n" + str(func)
        return s
