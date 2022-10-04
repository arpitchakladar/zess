from typing import Callable, Optional
from board.position import Position
from board.player import Player
from board.piece import Piece, PieceType
from board.move import Move

class Board:
    pieces: list[list[Optional[Piece]]]

    def __init__(self) -> None:
        self.pieces = []

    def get_pawn_moves(self, piece: Piece) -> list[Move]:
        moves: list[Move] = []
        a = 1 - 2 * piece.player.value
        if 0 < piece.position.row < 7:
            next_row = piece.position.row + a
            if self.pieces[piece.position.column][next_row] == None:
                moves.append(Move(piece, Position(piece.position.column, next_row)))
                if piece.position.row == (piece.player.value * 7 + a) and self.pieces[piece.position.column][next_row + a]:
                    moves.append(Move(piece, Position(piece.position.column, next_row + a)))
            if piece.position.column < 7:
                diagonal_piece = self.pieces[piece.position.column + 1][next_row]
                if diagonal_piece != None:
                    assert diagonal_piece is not None
                    moves.append(Move(piece, diagonal_piece.position, diagonal_piece))
            if piece.position.column > 0:
                diagonal_piece = self.pieces[piece.position.column - 1][next_row]
                if diagonal_piece != None:
                    assert diagonal_piece is not None
                    moves.append(Move(piece, diagonal_piece.position, diagonal_piece))
        return moves

    # TODO: Add logic to compute the possible legal moves for a piece
    # def get_legal_moves(self, piece: Piece) -> list[Move]:
    #    pass

    def arrange_pieces(self) -> None:
        for i in range(8):
            row: list[Optional[Piece]] = [None for i in range(8)]
            piece_type = PieceType.KING
            if i == 0 or i == 7:
                piece_type = PieceType.ROOK
            elif i == 1 or i == 6:
                piece_type = PieceType.KNIGHT
            elif i == 2 or i == 5:
                piece_type = PieceType.BISHOP
            elif i == 3:
                piece_type = PieceType.QUEEN
            row[0] = Piece(Player.WHITE, piece_type, Position(i, 0))
            row[7] = Piece(Player.BLACK, piece_type, Position(i, 7))
            row[1] = Piece(Player.WHITE, PieceType.PAWN, Position(i, 1))
            row[6] = Piece(Player.BLACK, PieceType.PAWN, Position(i, 6))
            self.pieces.append(row)

    def for_each_square(self, func: Callable[[Position, Optional[Piece]], bool]) -> None:
        result = True # if func returns False, then stop
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if piece == None:
                    result = func(Position(i, j), None)
                else:
                    assert piece is not None
                    result = func(piece.position, piece)
                if not result:
                    break
            if not result:
                break
