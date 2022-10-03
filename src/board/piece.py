from enum import Enum
from position import Position
from board.side import Side

class PieceType(Enum):
    PAWN = "pawn"
    KNIGHT = "knight"
    BISHOP = "bishop"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"

class Piece:
    position: Position
    pieceType: PieceType
    side: Side

    def __init__(self, side: Side, pieceType: PieceType, position: Position):
        self.position = position
        self.side = side
        self.pieceType = pieceType
