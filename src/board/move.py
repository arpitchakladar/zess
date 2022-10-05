from typing import Optional
from board.piece import Piece
from board.position import Position

class Move:
    piece: Piece
    from_position: Position
    to_position: Position
    capture: Optional[Piece]

    def __init__(self, piece: Piece, to_position: Position, capture: Optional[Piece] = None) -> None:
        self.piece = piece
        self.to_position = to_position
        self.from_position = piece.position
        self.capture = capture
