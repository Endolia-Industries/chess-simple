import numpy as np
from board import Board
from pieces import Piece
# from notation import Notation


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

def setup():
    # White pieces
    P1 = Piece([0, 1], 'P')
    P2 = Piece([1, 1], 'P')
    P3 = Piece([2, 1], 'P')
    P4 = Piece([3, 1], 'P')
    P5 = Piece([4, 1], 'P')
    P6 = Piece([5, 1], 'P')
    P7 = Piece([6, 1], 'P')
    P8 = Piece([7, 1], 'P')

    R1 = Piece([0, 0], 'R')
    R2 = Piece([7, 0], 'R')

    N1 = Piece([1, 0], 'N')
    N2 = Piece([6, 0], 'N')

    B1 = Piece([2, 0], 'B')
    B2 = Piece([5, 0], 'B')

    Q = Piece([4, 0], 'Q')

    K = Piece([3, 0], 'K')

    # Black Pieces
    p1 = Piece([0, 6], 'p')
    p2 = Piece([1, 6], 'p')
    p3 = Piece([2, 6], 'p')
    p4 = Piece([3, 6], 'p')
    p5 = Piece([4, 6], 'p')
    p6 = Piece([5, 6], 'p')
    p7 = Piece([6, 6], 'p')
    p8 = Piece([7, 6], 'p')

    r1 = Piece([0, 7], 'r')
    r2 = Piece([7, 7], 'r')

    n1 = Piece([1, 7], 'n')
    n2 = Piece([6, 7], 'n')

    b1 = Piece([2, 7], 'b')
    b2 = Piece([5, 7], 'b')

    q = Piece([4, 7], 'q')

    k = Piece([3, 7], 'k')


Board.setup()

printCoordMatrix(Piece.board)

Board.P4.move([4, 3])

printCoordMatrix(Piece.board)
