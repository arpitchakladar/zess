from typing import NoReturn, Callable, Union
from position import Position
from board.side import Side
from board.piece import Piece, PieceType

class Board:
    pieces: list[list[Union[Piece, None]]]

    def __init__(self):
        self.pieces = []

    def arrange_pieces(self) -> NoReturn:
        for i in range(8):
            row = [None for i in range(8)]
            piece_type = PieceType.KING
            if i == 0 or i == 7:
                piece_type = PieceType.ROOK
            elif i == 1 or i == 6:
                piece_type = PieceType.KNIGHT
            elif i == 2 or i == 5:
                piece_type = PieceType.BISHOP
            elif i == 3:
                piece_type = PieceType.QUEEN
            row[0] = Piece(Side.WHITE, piece_type, Position(i, 0))
            row[7] = Piece(Side.BLACK, piece_type, Position(i, 7))
            row[1] = Piece(Side.WHITE, PieceType.PAWN, Position(i, 1))
            row[6] = Piece(Side.BLACK, PieceType.PAWN, Position(i, 6))
            self.pieces.append(row)

    def for_each_square(self, func: Callable[[Position, Union[Piece, None]], NoReturn]) -> NoReturn:
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if piece == None:
                    func(Position(i, j), None)
                else:
                    func(piece.position, piece)
