class State:
    def __init__(self):
        self.grid = self.readGrid()
        self.gridSize = len(self.grid)

    @staticmethod
    def readGrid():
        rez = []
        with open("in.txt", "r") as file:
            for line in file:
                line = line.split()
                a = [int(x) for x in line]
                rez.append(a)
        return rez

    def getGrid(self):
        return self.grid

    def getGridSize(self):
        return self.gridSize

    def __str__(self):
        printString = ""
        for row in self.grid:
            for col in row:
                if col != -1:
                    printString += str(col) + " "
                else:
                    printString += 'X' + " "
            printString += "\n"
        return printString
