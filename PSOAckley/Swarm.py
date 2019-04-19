import math

from Particle import Particle


class Swarm:
    def __init__(self, noParticles, c1, c2):
        self.particles = []
        self.bestGlobal = math.inf
        self.bestGlobalX = math.inf
        self.bestGlobalY = math.inf
        self.c1 = c1
        self.c2 = c2
        self.noParticles = noParticles
        for x in range(noParticles):
            p = Particle()
            self.particles.append(p)

    def getBestParticle(self):
        for x in self.particles:
            if x.getFitness() < self.bestGlobal:
                self.bestGlobal = x.getFitness()
                self.bestGlobalX = x.getX()
                self.bestGlobalY = x.getY()
        return self.bestGlobal

    def getBestGlobal(self): return self.bestGlobal

    def getBestX(self): return float(self.bestGlobalX)

    def getBestY(self): return float(self.bestGlobalY)

    def getParticles(self): return self.particles

    def getC1(self): return self.c1

    def getC2(self): return self.c2

    def getNoParticles(self): return self.noParticles


