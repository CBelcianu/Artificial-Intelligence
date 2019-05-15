from variable import *


class Problem:
    def __init__(self, problemFile):
        self.__firstVar = None
        self.__secondVar = None
        self.__jointVar = None
        self.__probf = problemFile
        self.__rules = []
        self.readProblem()

    def solve(self, param1, param2):
        first, second = self.fuzzify(param1, param2)
        inferences = self.inference(first, second)
        aggregate = self.aggregate(inferences)
        centers = [func.center() for func in self.__jointVar.getFunctions()]
        result = self.defuzzify(aggregate, centers)
        self.printProgress([first, second], inferences, aggregate, result)

    def printProgress(self, fuzzified, inferences, aggregated, result):
        print("Fuzzified values:")
        s = str(self.__firstVar.getName()) + ": ["
        for val in fuzzified[0]:
            s += "{0:.2f}".format(val) + ", "
        print(s[:-2] + "]")
        s = str(self.__secondVar.getName()) + ": ["
        for val in fuzzified[1]:
            s += "{0:.2f}".format(val) + ", "
        print(s[:-2] + "]")
        print("\nInferred values for " + str(self.__jointVar.getName()) + " labels:")
        print(inferences)
        print("\nAggregated values for " + str(self.__jointVar.getName()) + " labels:")
        print(aggregated)
        print("\nDefuzzified result:")
        print(result)
        print("\nRecommended wash cycle")
        p = aggregated.index(max(aggregated))
        a = list(inferences)[p]
        print(a)

    def defuzzify(self, aggregate, centers):
        s1 = 0.0
        s2 = 0.0
        for i in range(len(aggregate)):
            s1 += aggregate[i] * centers[i]
            s2 += aggregate[i]
        return s1 / s2

    def aggregate(self, inferences):
        aggregated = [max(inferences[x]) for x in inferences]
        return aggregated

    def inference(self, firstValues, secondValues):
        inferences = {}
        for i in range(self.__firstVar.noOfLabels()):
            for j in range(self.__secondVar.noOfLabels()):
                label = self.__rules[i][j]
                if label in inferences.keys():
                    inferences[label].append(min(firstValues[i], secondValues[j]))
                else:
                    inferences[label] = [min(firstValues[i], secondValues[j])]
        return inferences

    def fuzzify(self, param1, param2):
        values1 = []
        for func in self.__firstVar.getFunctions():
            values1.append(func.compute(param1))
        values2 = []
        for func in self.__secondVar.getFunctions():
            values2.append(func.compute(param2))
        return values1, values2

    def readProblem(self):
        f = open(self.__probf, "r")
        variables = Problem.readVariables(f)
        self.__firstVar = variables[0]
        self.__secondVar = variables[1]
        self.__jointVar = variables[2]
        self.__rules = self.readFunctions(f)

    @staticmethod
    def readVariables(f):
        variables = []
        for var in range(3):
            line = f.readline().strip().split(',')
            name = line[0]
            nrFunctions = int(line[1])
            interval = [float(line[2]), float(line[3])]
            labels = [label for label in line[4:]]
            functions = []
            for func in range(nrFunctions):
                line = f.readline().strip().split(' ')
                line = [Problem.toNr(x) for x in line]
                functions.append(Problem.toFunction(line))
            variables.append(FuzzyVariable(name, labels, interval, functions))
        print("\n\nVARIABLES:\n")
        for k in variables:
            print(k)
            print('\n')
        return variables

    def readFunctions(self, f):
        rules = []
        for i in range(self.__firstVar.noOfLabels()):
            rules.append([])
            line = f.readline().strip().split(',')
            for j in range(self.__secondVar.noOfLabels()):
                rules[i].append(line[j])
        print("RULES:\n")
        for r in rules:
            print(r)
        print("\n\n")
        return rules

    @staticmethod
    def toNr(x):
        if x == 'inf':
            return inf
        return float(x)

    @staticmethod
    def toFunction(values):
        if len(values) == 3:
            return TriangularFunction(values[0], values[1], values[2])
        if len(values) == 4:
            return TrapezoidalFunction(values[0], values[1], values[2], values[3])
