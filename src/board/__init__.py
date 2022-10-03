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
            pieceType = PieceType.KING
            if i == 0 or i == 7:
                pieceType = PieceType.ROOK
            elif i == 1 or i == 6:
                pieceType = PieceType.KNIGHT
            elif i == 2 or i == 5:
                pieceType = PieceType.BISHOP
            elif i == 3:
                pieceType = PieceType.QUEEN
            row[0] = Piece(Side.WHITE, pieceType, Position(i, 0))
            row[7] = Piece(Side.BLACK, pieceType, Position(i, 7))
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
