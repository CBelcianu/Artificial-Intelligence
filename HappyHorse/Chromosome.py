from random import randint


class Chromosome:
    def __init__(self, grid):
        self.grid = grid
        self.genes = []
        self.genes.append(0)
        for i in range(1, 36):
            rand = randint(1, 35)
            while self.genes.__contains__(rand):
                rand = randint(1, 35)
            self.genes.append(rand)

    def setGenes(self, genes):
        self.genes = genes

    def fitness(self):
        fit = 0
        for i in range(0, 35):
            if not self.grid[self.genes[i]].__contains__(self.genes[i+1]):
                fit += 1
        return fit

    def xover(self, partener):
        newgene = []
        for i in range(0, 36):
            if i % 2 == 0 and not newgene.__contains__(self.genes[i]):
                newgene.append(self.genes[i])
            elif i % 2 == 1 and not newgene.__contains__(partener.genes[i]):
                newgene.append(partener.genes[i])
            else:
                rand = randint(0, 35)
                while newgene.__contains__(rand):
                    rand = randint(0, 35)
                newgene.append(rand)
        off = Chromosome(self.grid)
        off.setGenes(newgene)
        return off

    def mutate(self):
        rand = randint(1, 35)
        if not self.grid[self.genes[rand-1]].__contains__(self.genes[rand]):
            lengr = len(self.grid[self.genes[rand-1]])
            ranpos = randint(0, lengr-1)
            val = self.grid[self.genes[rand-1]][ranpos]
            oldval = self.genes[rand]
            idx = self.genes.index(val)
            self.genes[rand] = val
            self.genes[idx] = oldval

    def __str__(self):
        v = ""
        for i in self.genes:
            v = v + " " + i.__str__()
        return v
