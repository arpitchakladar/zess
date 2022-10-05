from typing import Callable, Optional
from board.position import Position
from board.player import Player
from board.piece import Piece, PieceType
from board.move import Move

class Board:
    board: list[list[Optional[Piece]]]
    turn: Player
    move_history: list[Move]
    king_moved: tuple[bool, bool]

    def __init__(self) -> None:
        self.board = []
        self.turn = Player.WHITE
        self.move_history = []
        self.king_moved = (False, False)

    def get_pawn_moves(self, piece: Piece) -> list[Move]:
        moves: list[Move] = []
        increment = 1 - 2 * piece.player.value
        row = piece.position.row
        column = piece.position.column
        if 0 < row < 7:
            next_row = row + increment
            # En passant
            if increment * (row - piece.player.value * 7) == 4:
                last_move = self.move_history[len(self.move_history) - 1]
                if increment * (last_move.to_position.row - last_move.from_position.row) == 2:
                    diagonal_piece: Optional[Piece] = None
                    if column < 7:
                        diagonal_piece = self.board[column + 1][row]
                        if last_move.piece == diagonal_piece:
                            moves.append(Move(piece, Position(column + 1, row + increment), diagonal_piece))
                        else:
                            diagonal_piece = None
                    if diagonal_piece == None and column > 0:
                        diagonal_piece = self.board[column - 1][row]
                        if last_move.piece == diagonal_piece:
                            moves.append(Move(piece, Position(column - 1, row + increment), diagonal_piece))
            # Move to next square (or 2 squares)
            if self.board[column][next_row] == None:
                moves.append(Move(piece, Position(column, next_row)))
                if row == (piece.player.value * 7 + increment) and self.board[column][next_row + increment] == None:
                    moves.append(Move(piece, Position(column, next_row + increment)))
            # Diagonal capture right for white (and vise-versa)
            if column < 7:
                diagonal_piece = self.board[column + 1][next_row]
                if diagonal_piece != None:
                    assert diagonal_piece is not None
                    moves.append(Move(piece, diagonal_piece.position, diagonal_piece))
            # Diagonal capture left for white (and vise-versa)
            if column > 0:
                diagonal_piece = self.board[column - 1][next_row]
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
            self.board.append(row)

    def for_each_square(self, func: Callable[[Position, Optional[Piece]], bool]) -> None:
        result = True # if func returns False, then stop
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece == None:
                    result = func(Position(i, j), None)
                else:
                    assert piece is not None
                    result = func(piece.position, piece)
                if not result:
                    break
            if not result:
                break
