from enum import Enum
from position import Position
from board.side import Side

class PieceType(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class Piece:
    position: Position
    pieceType: PieceType
    side: Side

    def __init__(self, side: Side, pieceType: PieceType, position: Position):
        self.position = position
        self.side = side
        self.pieceType = pieceType
