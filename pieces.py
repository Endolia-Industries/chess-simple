import numpy as np

# print functions are temporary for debugging
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
    board = np.full((8, 8), '.', dtype=np.str_)

    def __init__(self, coords, piece):  # p = Piece([1, 1], 'P')
        xCoord = coords[0]
        yCoord = coords[1]
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.piece = piece
        # choose color based upon capitalization

        if piece.upper() == 'P':
            self.steps = [[0, 1]]
            self.maxStep = 2

        if piece.upper() == 'K':
            self.steps = [[1, 2], [2, 1], [2, -1], [1, -2], [-1,-2],[-2, -1], [-2, 1], [-1, 2]]
            self.maxStep = 1
        
        if piece.upper() == 'R':
            self.steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            self.maxStep = 7
        
        if piece.upper() == 'B':
            self.steps = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            self.maxStep = 7

        if piece.upper() == 'Q':
            self.steps = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            self.maxStep = 7

        if piece.upper() == 'K':
            self.steps = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            self.maxStep = 7

        self.__class__.board[self.xCoord][self.yCoord] = self.piece

    def setup():
        # White pieces
        P1 = Piece([1, 0], 'P')
        P2 = Piece([1, 1], 'P')
        P3 = Piece([1, 2], 'P')
        P4 = Piece([1, 3], 'P')
        P5 = Piece([1, 4], 'P')
        P6 = Piece([1, 5], 'P')
        P7 = Piece([1, 6], 'P')
        P8 = Piece([1, 7], 'P')

        R1 = Piece([0, 0], 'R')
        R2 = Piece([0, 7], 'R')

        N1 = Piece([0, 1], 'N')
        N2 = Piece([0, 6], 'N')

        B1 = Piece([0, 2], 'B')
        B2 = Piece([0, 5], 'B')

        Q = Piece([0, 4], 'Q')

        K = Piece([0, 3], 'K')

        # Black Pieces
        p1 = Piece([6, 0], 'p')
        p2 = Piece([6, 1], 'p')
        p3 = Piece([6, 2], 'p')
        p4 = Piece([6, 3], 'p')
        p5 = Piece([6, 4], 'p')
        p6 = Piece([6, 5], 'p')
        p7 = Piece([6, 6], 'p')
        p8 = Piece([6, 7], 'p')

        r1 = Piece([7, 0], 'r')
        r2 = Piece([7, 7], 'r')

        n1 = Piece([7, 1], 'n')
        n2 = Piece([7, 6], 'n')

        b1 = Piece([7, 2], 'b')
        b2 = Piece([7, 5], 'b')

        q = Piece([7, 4], 'q')

        k = Piece([7, 3], 'k')


    def ray_casting(self, coords):
        possible = 0
        xCoord = coords[0]
        yCoord = coords[1]

        for step in self.steps:
            xStepPos = xCoord
            yStepPos = yCoord
            for n in range(self.maxStep):
                xStepPos -= step[0]
                yStepPos -= step[1]
                if xStepPos < 0 or yStepPos < 0:
                    break
                if xStepPos > 7 or yStepPos > 7:
                    break
                if self.__class__.board[xStepPos][yStepPos] != '.':
                    if self.__class__.board[xStepPos][yStepPos] == self.piece:
                        # need to add ability to specify original coords
                        possible += 1
                    else:
                        pass
                    break
        return possible
        
    
    def check_pawn(self, coords, take):
        xCoord = coords[0]
        yCoord = coords[1]

        if(self.piece.upper() == 'P'):
            if take is True:
                self.maxStep = 1
                if self.piece == 'P':
                    self.steps = [[1, 1], [-1, 1]]
                else:
                    self.steps = [[1, -1], [-1, -1]]
            else:
                if self.piece == 'P':
                    self.steps = [[0, 1]]
                else:
                    self.steps = [[0, -1]]
                
                if self.piece == 'P':
                    if self.yCoord != 1:
                        self.maxStep = 1
                else:
                    if self.yCoord != 6:
                        self.maxStep = 1
        return self.ray_casting(coords)



                   
        
    def move(self, coords, take = False):
        possible = self.check_pawn(coords, take)
        if possible == 1:
            self.__class__.board[self.xCoord][self.yCoord] = "."
            self.xCoord = coords[0]
            self.yCoord = coords[1]
            self.__class__.board[self.xCoord][self.yCoord] = self.piece
        elif possible > 1:
            raise ValueError("Notation is ambiguous")
        else:
            raise ValueError("invalid move")
        
        #don't forget pawn promotions or else ur a nerd - Big Wise cheese grater man



# R = Piece([4, 4], 'R')
# b = Piece([6, 4], 'b')

# printCoordMatrix(Piece.board)

# R.move([6, 4])

# printCoordMatrix(Piece.board)
