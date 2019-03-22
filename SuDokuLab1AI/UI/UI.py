from Model.Sudoku import Sudoku
from Controller.Controller import Controller
from time import time


class UI:
    def __init__(self):
        sudo = Sudoku()
        self.ctrl = Controller(sudo)

    @staticmethod
    def printMainMenu():
        s = '\n'
        s += "0 - exit \n"
        s += "1 - solve Sudoku with BFS \n"
        s += "2 - solve Sudoku with GreedyBFS\n"
        print(s)

    def runBFS(self):
        startClock = time()
        [print(x.getState()) for x in self.ctrl.bfs()]
        print('execution time = ', time() - startClock, " seconds")

    def runGreedyBFS(self):
        startClock = time()
        [print(x.getState()) for x in self.ctrl.greedyBfs()]
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        print('\n Sudoku Solver - BFS & GreedyBFS')
        runApp = True
        self.printMainMenu()
        while runApp:
            try:
                command = int(input(">>"))
                if command == 0:
                    runApp = False
                    print('terminating ...')
                elif command == 1:
                    self.runBFS()
                    self.printMainMenu()
                elif command == 2:
                    self.runGreedyBFS()
                    self.printMainMenu()
                else:
                    print('unknown command')
            except ValueError:
                print('invalid command')
