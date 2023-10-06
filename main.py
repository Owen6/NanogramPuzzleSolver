gridSize = 10

class Board:
    boardValues = []

    def loadBoard(self, boardSize):
        self.boardSize = boardSize
        for i in range(boardSize):
            self.boardValues.append([])
            for j in range(boardSize):
                self.boardValues[i].append('O')

    def printBoard(self):
        for i in range(self.boardSize):
            print('[',*self.boardValues[i],']')
        print('\n')

    def setValue(self, xVal, yVal, val):
        if val != '-':
            self.boardValues[xVal][yVal] = val


def main():
    #Vertices
    vertices = [
                ['X','X','X','X','X','-','-','-','-','X'],
                ['X','-','-','-','X','-','-','-','-','-'],
                ['-','X','X','X','-','X','-','-','-','-'],
                ['X','-','X','X','-','-','X','-','X','-'],
                ['X','-','-','-','-','-','-','X','-','X'],
                ['X','X','-','-','-','-','-','-','-','X'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-']
                ]


    newBoard = Board()
    newBoard.loadBoard(gridSize)
    #newBoard.setValue(1,1)
    newBoard.printBoard()
    newBoard = loadExampleBoard(newBoard,vertices)
    newBoard.printBoard()

def loadExampleBoard(tempBoard, vertices):
    for i in range(gridSize):
        for j in range(gridSize):
            tempBoard.setValue(i,j,vertices[i][j])
    return tempBoard

if __name__ == "__main__":
    main()
