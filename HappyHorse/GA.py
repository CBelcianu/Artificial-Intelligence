from Population import Population
import matplotlib.pyplot as plt

class GA:
    def __init__(self, popSize):
        self.popSize = popSize
        self.dict = self.generateDict()

    def generateDict(self):
        tabla = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23],
                 [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]]
        mutari = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]

        dict1 = dict()

        for i in range(0, 36):
            dict1[i] = []

        for i in range(0, 6):
            for j in range(0, 6):
                for mutare in mutari:
                    if i + mutare[0] >= 0 and i + mutare[0] <= 5 and j + mutare[1] >= 0 and j + mutare[1] <= 5:
                        dict1[tabla[i][j]].append(tabla[i + mutare[0]][j + mutare[1]])

        return dict1

    def resolver(self):
        pop = Population(self.popSize, self.dict)
        gennr=0
        fitnesses = []
        while pop.best().fitness() != 0:
            if gennr < 250:
                newpop = [pop.best()]
                for i in range(1, self.popSize):
                    M = pop.selection()
                    F = pop.selection()
                    off = M.xover(F)
                    off.mutate()
                    newpop.append(off)
            pop.setPop(newpop)
            print("fitness:", pop.best().fitness(), "generetion: ", gennr)
            gennr +=1
            fitnesses.append(pop.averageFitness())
            if gennr > 1000:
                plt.clf()
                plt.plot(fitnesses)
                plt.ylabel("fitness variation")
                plt.show()

                break
        #print(pop.best())
        return pop.best()