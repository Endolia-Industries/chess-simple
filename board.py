import numpy as np
from pieces import Piece
# board = np.zeros((8,8))

class Board: 
    @classmethod
    def setup(cls):
        # White pieces
        cls.P1 = Piece([0, 1], 'P')
        cls.P2 = Piece([1, 1], 'P')
        cls.P3 = Piece([2, 1], 'P')
        cls.P4 = Piece([3, 1], 'P')
        cls.P5 = Piece([4, 1], 'P')
        cls.P6 = Piece([5, 1], 'P')
        cls.P7 = Piece([6, 1], 'P')
        cls.P8 = Piece([7, 1], 'P')

        cls.R1 = Piece([0, 0], 'R')
        cls.R2 = Piece([7, 0], 'R')

        cls.N1 = Piece([1, 0], 'N')
        cls.N2 = Piece([6, 0], 'N')

        cls.B1 = Piece([2, 0], 'B')
        cls.B2 = Piece([5, 0], 'B')

        cls.Q = Piece([4, 0], 'Q')

        cls.K = Piece([3, 0], 'K')

        # Black Pieces
        cls.p1 = Piece([0, 6], 'p')
        cls.p2 = Piece([1, 6], 'p')
        cls.p3 = Piece([2, 6], 'p')
        cls.p4 = Piece([3, 6], 'p')
        cls.p5 = Piece([4, 6], 'p')
        cls.p6 = Piece([5, 6], 'p')
        cls.p7 = Piece([6, 6], 'p')
        cls.p8 = Piece([7, 6], 'p')

        cls.r1 = Piece([0, 7], 'r')
        cls.r2 = Piece([7, 7], 'r')

        cls.n1 = Piece([1, 7], 'n')
        cls.n2 = Piece([6, 7], 'n')

        cls.b1 = Piece([2, 7], 'b')
        cls.b2 = Piece([5, 7], 'b')

        cls.q = Piece([4, 7], 'q')

        cls.k = Piece([3, 7], 'k')

    # def move()

