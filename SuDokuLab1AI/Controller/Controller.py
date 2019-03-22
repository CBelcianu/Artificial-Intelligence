from copy import deepcopy


class Controller:
    def __init__(self, sudo):
        self.sudo = sudo

    def getSudo(self):
        return self.sudo

    @staticmethod
    def isSolved(someSudo):
        return someSudo.isPartiallyCorrect() and someSudo.getFirstFreePos() == [0, 0]

    @staticmethod
    def expand(someSudo):
        row, col = someSudo.getFirstFreePos()
        gridSize = someSudo.getState().getGridSize()
        partialCalculate = []
        for number in range(1, gridSize + 1):
            if someSudo.isSafe(row, col, number):
                newSudo = deepcopy(someSudo)
                newSudo.getState().getGrid()[row][col] = number
                partialCalculate.append(newSudo)
        return partialCalculate

    @staticmethod
    def heuristicsExpand(someSudo):
        row, col = someSudo.firstHeuristicsPos()
        gridSize = someSudo.getState().getGridSize()
        partialCalculate = []
        for number in range(1, gridSize + 1):
            if someSudo.isSafe(row, col, number):
                newSudo = deepcopy(someSudo)
                newSudo.getState().getGrid()[row][col] = number
                partialCalculate.append(newSudo)
        return partialCalculate

    def bfs(self):
        visited = [self.sudo]
        queue = [[self.sudo]]
        while len(queue) > 0:
            partialResult = queue.pop(0)
            if self.isSolved(partialResult[-1]):
                return partialResult
            for table in self.expand(partialResult[-1]):
                if table not in visited:
                    partialResult += [table]
                    visited.append(partialResult[-1])
                queue.append(partialResult)
                partialResult = partialResult[:-1]
        return None

    def greedyBfs(self):
        visited = [self.sudo]
        queue = [[self.sudo]]
        while len(queue) > 0:
            partialResult = queue.pop(0)
            if self.isSolved(partialResult[-1]):
                return partialResult
            for table in self.heuristicsExpand(partialResult[-1]):
                if table not in visited:
                    partialResult += [table]
                    visited.append(partialResult[-1])
                queue.append(partialResult)
                partialResult = partialResult[:-1]
        return None
