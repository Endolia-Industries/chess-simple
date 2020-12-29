from typing import NoReturn


pieceNotation = {
    "P" : "Pawn",
    "N" : "Knight",
    "B" : "Bishop",
    "R" : "Rook",
    "Q" : "Queen",
    "K" : "King"
}


class Notation:
    def __init__(self, notation):
        self.notation = notation
        self.check = False
        self.mate = False
        self.kCastle = False
        self.qCastle = False
        self.take = False
        self.specifics = ""
        
    def compile(self):
        notation = self.notation
        
        if len(notation) < 2:
            raise ValueError("improper notation")
        if notation[-1] == "+":
            check = True
            notation = notation[:-1]
        elif notation[-1] == "#":
            mate = True
            notation = notation[:-1]

        if notation == "0-0":
            kCastle = True
            return kCastle  # need better way to store this info
        elif notation == "0-0-0":
            qCastle = True
            return qCastle  # ^

        try:
            promotion = pieceNotation[notation[-1]]
            notation = notation[:-2]
        except KeyError:
            pass

        xCoord = notation[-2:-1] # needs protection from bad notation
        yCoord = notation[-1:]
        notation = notation[:-2]

        xCoord = notation[-2:-1] # needs protection from bad notation
        yCoord = notation[-1:]
        notation = notation[:-2]

        try:
            if notation[-1] == "x":
                take = True
                notation = notation[:-1]
        except IndexError:
            pass

        try:
            piece = pieceNotation[notation[0]]
            notation = notation[1:]
        except IndexError:
            self.piece = pieceNotation[""]
        except KeyError:
            piece = pieceNotation[""]
        
        if len(notation) > 0:
            specifics = notation

        # print(f"castle: K({self.kCastle}) Q({self.qCastle}), ({self.xCoord, self.yCoord}), {self.piece}, promotion: {self.promotion} take: {self.take}, check: {self.check}, mate: {self.mate}, etc: {self.specifics}")
        # needs output

        return 

        # def verify(notationList):

Notation("e3")
