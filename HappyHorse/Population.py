from random import randint

from Chromosome import Chromosome


class Population:
    def __init__(self, popSize, grid):
        self.grid = grid
        self.popSize = popSize
        self.pop = []
        for i in range(0, popSize):
            c = Chromosome(self.grid)
            self.pop.append(c)

    def setPop(self, pop):
        self.pop = pop

    def averageFitness(self):
        x = 0
        for i in self.pop:
            x += i.fitness();
        x = x/self.popSize
        return x;

    def selection(self):
        c1 = self.pop[randint(1, self.popSize - 1)]
        c2 = self.pop[randint(1, self.popSize - 1)]
        if c1.fitness() < c2.fitness():
            return c1
        else:
            return c2

    def best(self):
        min = self.pop[0]
        for i in self.pop:
            if i.fitness() < min.fitness():
                min = i
        return min

