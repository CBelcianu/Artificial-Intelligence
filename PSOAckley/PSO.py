from Swarm import Swarm
import matplotlib.pyplot as plt


class PSO:
    def __init__(self, swarmSize):
        self.s = Swarm(swarmSize, 5, 5)

    def runPSO(self):
        count = 0
        fitnesses = []

        while count < 1000:
            count += 1

            for particle in self.s.getParticles():
                particle.calculateFitness()
            bestParticle = self.s.getBestParticle()
            print("Iteration " + str(count) + "-> fitness: " + str(bestParticle))
            for particle in self.s.getParticles():
                particle.evaluate(self.s.getBestX(), self.s.getBestY(), self.s.getC1(), self.s.getC2())
            fitnesses.append(self.s.getBestGlobal())

        print('\nResult: The detected minimum point is (' + str(self.s.getBestX()) + ', ' + str(self.s.getBestY()) +
              ')\n with function\'s value ' + str(self.s.getBestGlobal()) + ' in ' + str(count) + ' \'swarm moves\'')
        plt.clf()
        plt.plot(fitnesses)
        plt.ylabel("fitness variation")
        plt.show()
