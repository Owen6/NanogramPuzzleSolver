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
    #newBoard.printBoard()
    newBoard = loadExampleBoard(newBoard,vertices)
    #newBoard.printBoard()
    possibleSolutions()

def loadExampleBoard(tempBoard, vertices):
    for i in range(gridSize):
        for j in range(gridSize):
            tempBoard.setValue(i,j,vertices[i][j])
    return tempBoard

def possibleSolutions():

    rule = [2,3]
    if(listSum(rule) > gridSize):
        print('Not a valid rule')
        return
    initialState = initialize(rule)

    possibleSol = []
    possibleSol.append(initialState)

    final = False
    temp = []
    for i in range(len(rule)):
        while final == False:
            temp = possibleSol[-1].copy()
            tempTwo = []
            tempTwo = temp.copy()
            for j in range(len(possibleSol[i])):
                if temp[-1*(j+1)] != 'X':
                    #print(possibleSol)
                    temp[-1*(j+1)] = tempTwo[-1*(j)]
                    temp[-1*(j)] = tempTwo[-1*(j+1)]
                    break
            if possibleSol[-1][-1] != 'X':
                final = True
            else:
                possibleSol.append(temp)
            #final = True
    for k in range(len(possibleSol)):
        print(possibleSol[k])


def initialize(rule):
    filled = listSum(rule)+len(rule)-1
    xNum = gridSize - filled
    index = 0
    itemAdded = False
    initialState = []
    for i in range(gridSize - len(rule)):
        if(index < len(rule) and itemAdded == False):
            initialState.append(rule[index])
            index = index + 1
            itemAdded = True
        else:
            initialState.append('X')
            itemAdded = False
    return initialState

def listSum(l):
    sum = 0
    index = 0
    while index < len(l):
        sum = sum + l[index]
        index = index + 1
    return int(sum)

if __name__ == "__main__":
    main()
