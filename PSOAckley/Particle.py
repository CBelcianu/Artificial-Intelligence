import math
import random


class Particle:
    def __init__(self):
        self.x = random.uniform(-5, 5)
        self.y = random.uniform(-5, 5)
        self.velocityX = 0
        self.velocityY = 0
        self.fitness = 0
        self.bestX = math.inf
        self.bestY = math.inf
        self.bestFitness = math.inf

    def getX(self): return self.x

    def getY(self): return self.y

    def getFitness(self): return self.fitness

    def getBestFitness(self): return self.bestFitness

    def calculateFitness(self):
        self.fitness = -20 * math.exp(1) ** (-0.2 * math.sqrt(0.5 * (self.x ** 2 + self.y ** 2))) - math.exp(1) ** (
                    0.5 * (math.cos(2 * math.pi * self.x) + math.cos(2 * math.pi * self.y))) + math.exp(1) + 20
        if self.fitness < self.bestFitness:
            self.bestFitness = self.fitness
            self.bestX = self.x
            self.bestY = self.y

    def evaluate(self, bestGlobalX, bestGlobalY, c1, c2):
        self.velocityX = self.velocityX + c1 * random.random() * (self.bestX - self.x) + c2 * random.random() * (
                    bestGlobalX - self.x)

        if self.velocityX > 5 or self.velocityX < -5:
            self.velocityX = random.uniform(-5, 5)
        '''
        if self.velocityX > 5:
            self.velocityX -= 5
        elif self.velocityX < -5:
            self.velocityX += 5
         '''

        self.velocityY = self.velocityY + c1 * random.random() * (self.bestY - self.y) + c2 * random.random() * (
                    bestGlobalY - self.y)

        if self.velocityY > 5 or self.velocityY < -5:
            self.velocityY = random.uniform(-5, 5)
        '''
        if self.velocityY > 5:
            self.velocityY -= 5
        elif self.velocityY < -5:
            self.velocityY += 5
         '''

        if self.x + self.velocityX > 5:
            self.x = 5
        elif self.x + self.velocityX < -5:
            self.x = -5
        else:
            self.x += self.velocityX

        if self.y + self.velocityY > 5:
            self.y = 5
        elif self.y + self.velocityY < -5:
            self.y = -5
        else:
            self.y += self.velocityY
