from enum import Enum
from position import Position
from board.side import Side

piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]

class PieceType(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

    def __str__(self):
        return piece_names[self.value]

class Piece:
    position: Position
    piece_type: PieceType
    side: Side

    def __init__(self, side: Side, piece_type: PieceType, position: Position):
        self.position = position
        self.side = side
        self.piece_type = piece_type
