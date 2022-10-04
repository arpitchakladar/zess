from enum import Enum
from board.position import Position
from board.player import Player

piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]

class PieceType(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

    def __str__(self) -> str:
        return piece_names[self.value]

class Piece:
    position: Position
    piece_type: PieceType
    player: Player

    def __init__(self, player: Player, piece_type: PieceType, position: Position) -> None:
        self.position = position
        self.player = player
        self.piece_type = piece_type
