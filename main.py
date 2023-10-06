

class Board:
    boardValues = []

    def loadBoard(self, boardSize):
        self.boardSize = boardSize
        for i in range(boardSize):
            self.boardValues.append([])
            for j in range(boardSize):
                self.boardValues[i].append([])

    def printBoard(self):
        for i in range(self.boardSize):
            print(self.boardValues[i])

    def setValue(self, xVal, yVal):
        self.boardValues[xVal-1][yVal-1] = 'X'


def main():
    newBoard = Board()
    newBoard.loadBoard(10)
    newBoard.setValue(1,1)
    newBoard.printBoard()


if __name__ == "__main__":
    main()
