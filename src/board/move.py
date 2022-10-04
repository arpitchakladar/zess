from typing import Optional
from board.piece import Piece
from board.position import Position

class Move:
    piece: Piece
    position: Position
    capture: Optional[Piece]

    def __init__(self, piece: Piece, position: Position, capture: Optional[Piece] = None) -> None:
        self.piece = piece
        self.position = position
        self.capture = capture
