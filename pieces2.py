import numpy as np
from numpy.core.defchararray import isupper

def printMatrix(mat):
    out = ""
    for idxi, i in enumerate(mat):
        for idxj, j in enumerate(i):
            out += f"{mat[idxi][idxj]} "
        out += "\n"
    print(out)

def printCoordMatrix(mat):
    mat = np.flip(mat, 1)
    out = ""
    for idxi, i in enumerate(mat):
        for idxj, j in enumerate(i):
            out += f"{mat[idxj][idxi]} "
        out += "\n"
    print(out)


class Piece:
    pieceSteps = {
        'p' : "special", # come back to later
        'r' : [[1, 0], [0, 1], [-1, 0], [0, -1]],
        'n' : [[1, 2], [2, 1], [2, -1], [1, -2], [-1,-2],[-2, -1], [-2, 1], [-1, 2]],
        'b' : [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        'q' : [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]],
        'k' : [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    }
    pieceMax = {
    'p' : "special", # come back to later
    'k' : 1
    }

    board = np.full((8, 8), '.')

    def __init__(self, type): #sets up all the piece types
        self.type = type

        self.steps = self.__class__.pieceSteps.get(self.type.lower())
        self.stepMax = self.__class__.pieceMax.get(self.type.lower(), 7)

    @classmethod
    def setup(cls):
        cls.initialize_pieces()

        # White Pieces
        cls.board[0][0] = 'R'
        cls.board[7][0] = 'R'

        cls.board[1][0] = 'N'
        cls.board[6][0] = 'N'

        cls.board[2][0] = 'B'
        cls.board[5][0] = 'B'

        cls.board[3][0] = 'Q'
        cls.board[4][0] = 'K'

        cls.board[0][1] = 'P'
        cls.board[1][1] = 'P'
        cls.board[2][1] = 'P'
        cls.board[3][1] = 'P'
        cls.board[4][1] = 'P'
        cls.board[5][1] = 'P'
        cls.board[6][1] = 'P'
        cls.board[7][1] = 'P'


        cls.board[0][7] = 'r'
        cls.board[7][7] = 'r'

        cls.board[1][7] = 'n'
        cls.board[6][7] = 'n'

        cls.board[2][7] = 'b'
        cls.board[5][7] = 'b'

        cls.board[3][7] = 'q'
        cls.board[4][7] = 'k'

        cls.board[0][6] = 'p'
        cls.board[1][6] = 'p'
        cls.board[2][6] = 'p'
        cls.board[3][6] = 'p'
        cls.board[4][6] = 'p'
        cls.board[5][6] = 'p'
        cls.board[6][6] = 'p'
        cls.board[7][6] = 'p'

    @classmethod
    def custom_setup(cls):
        cls.initialize_pieces()

        cls.board[0][0] = 'R'
        cls.board[0][7] = 'r'

    @classmethod
    def initialize_pieces(cls):
        cls.P = Piece('P')
        cls.R = Piece('R')
        cls.N = Piece('N')
        cls.B = Piece('B')
        cls.Q = Piece('Q')
        cls.K = Piece('K')

        cls.p = Piece('p')
        cls.r = Piece('r')
        cls.n = Piece('n')
        cls.b = Piece('b')
        cls.q = Piece('q')
        cls.k = Piece('k')



    def find_move(self, xCoord, yCoord): # needs to be able to intake disambiguating info
        possibilities = []

        for step in self.steps:
            xStepPos = xCoord
            yStepPos = yCoord
            for n in range(self.stepMax):
                xStepPos -= step[0]
                yStepPos -= step[1]
                if xStepPos < 0 or yStepPos < 0:
                    break
                if xStepPos > 7 or yStepPos > 7:
                    break
                if self.__class__.board[xStepPos][yStepPos] != '.':
                    if self.__class__.board[xStepPos][yStepPos] == self.type:
                        # need to add ability to specify original coords
                        possibilities.append([xStepPos, yStepPos])
                    break
        return possibilities
    
    def move(self, xCoord, yCoord):
        possibilities = self.find_move(xCoord, yCoord)
        if len(possibilities) > 1:
            print(possibilities)
            raise ValueError("move is ambiguous")
        elif len(possibilities) < 1:
            print(possibilities)
            raise ValueError("move is invalid")
        fromX = possibilities[0][0]
        fromY = possibilities[0][1]
        self.__class__.board[fromX][fromY] = '.'
        self.__class__.board[xCoord][yCoord] = self.type





Piece.custom_setup()

# P = Piece('P')
# R = Piece('R')
# N = Piece('N')
# B = Piece('B')
# Q = Piece('Q')
# K = Piece('K')

# p = Piece('p')
# r = Piece('r')
# n = Piece('n')
# b = Piece('b')
# q = Piece('q')
# k = Piece('k')


printCoordMatrix(Piece.board)

Piece.R.move(0, 5)

printCoordMatrix(Piece.board)
