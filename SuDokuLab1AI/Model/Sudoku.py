from Model.State import State
from math import sqrt
from operator import itemgetter


class Sudoku:
    def __init__(self):
        self.state = State()

    def getState(self):
        return self.state

    @staticmethod
    def lookForDuplicates(someGrid):
        frq = []
        for i in range(100):
            frq.append(0)
        for elem in someGrid:
            if elem != -1:
                frq[elem] += 1
        for freq in frq:
            if freq == 2:
                return True
        return False

    def isPartiallyCorrect(self):
        for row in self.state.getGrid():
            if self.lookForDuplicates(row) is True:
                return False
        for i in range(0, len(self.state.getGrid())):
            currentColumn = []
            for j in range(0, len(self.state.getGrid())):
                currentColumn.append(self.state.getGrid()[j][i])
            if self.lookForDuplicates(currentColumn) is True:
                return False
        return True

    def getFirstFreePos(self):
        for row in self.state.getGrid():
            for col in row:
                if col == -1:
                    return self.state.getGrid().index(row), row.index(col)
        return [0, 0]

    def getAllFreePos(self):
        result = []
        for row in range(0, len(self.state.getGrid())):
            for col in range(0, len(self.state.getGrid())):
                if self.state.getGrid()[row][col] == -1:
                    result.append([row, col])
        return result

    def isInRow(self, row, number):
        flag = False
        for value in self.state.getGrid()[row]:
            flag = True if number == value else False
        return flag

    def isInColumn(self, col, value):
        flag = False
        for row in self.state.getGrid():
            flag = True if value == row[col] else False
        return flag

    def isInSquare(self, row, col, value):
        squareSide = int(sqrt(self.state.getGridSize()))
        isDown = True if row < squareSide else False
        isLeft = True if col < squareSide else False
        if isLeft == isDown:
            params = [0, 0] if (isDown and isLeft) else [squareSide, squareSide]
        else:
            params = [0, squareSide] if (isDown and not isLeft) else [squareSide, 0]

        flag = False
        for row in range(params[0], params[0] + squareSide):
            for col in range(params[1], params[1] + squareSide):
                flag = True if self.state.getGrid()[row][col] == value else False
        return flag

    def isSafe(self, row, col, value):
        if self.isInColumn(col, value) is True:
            return False
        if self.isInRow(row, value) is True:
            return False
        if self.isInSquare(row, col, value) is True:
            return False
        return True

    def calculateHeuristic(self, row, col, value):
        """
        calculate the heuristic based on the number of restriction the cell has
        """
        result = []
        for someRow in self.state.getGrid():
            if value != someRow[col] and (someRow[col] not in result):
                result.append(someRow[col])
        for number in self.state.getGrid()[row]:
            if number != value and (number not in result):
                result.append(number)
        squareSide = int(sqrt(self.state.getGridSize()))
        isDown = True if row < squareSide else False
        isLeft = True if col < squareSide else False
        if isLeft == isDown:
            params = [0, 0] if (isDown and isLeft) else [squareSide, squareSide]
        else:
            params = [0, squareSide] if (isDown and not isLeft) else [squareSide, 0]

        for row in range(params[0], params[0] + squareSide):
            for col in range(params[1], params[1] + squareSide):
                if self.state.getGrid()[row][col] != value and (self.state.getGrid()[row][col] not in result):
                    result.append(self.state.getGrid()[row][col])
        return len(result)

    def bestHeuristicPos(self):
        """
        returns the sorted list with possible candidates
        """
        possiblePos = self.getAllFreePos()
        rez = []
        for pos in possiblePos:
            rez.append([self.calculateHeuristic(pos[0], pos[1],
                                                self.state.getGrid()[pos[0]][pos[1]]), pos])
        rez = sorted(rez, key=itemgetter(0))
        return rez[::-1]

    def firstHeuristicsPos(self):
        if len(self.bestHeuristicPos()) != 0:
            return self.bestHeuristicPos()[0][1]
        else:
            return self.getFirstFreePos()

    def __eq__(self, other):
        if not (isinstance(other, Sudoku)):
            return False
        if self.state.getGridSize() != other.getState().getGridSize():
            return False
        for i in range(self.state.getGridSize()):
            for j in range(self.state.getGridSize()):
                if self.state.getGrid()[i][j] != other.getState().getGrid()[i][j]:
                    return False
        return True
