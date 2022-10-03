from typing import NoReturn, Callable
from position import Position

class Board:
    pieces: list[list[None]]

    def __init__(self):
        self.pieces = [[None for _ in range(8)] for _ in range(8)]

    def for_each_cell(self, func: Callable[[Position, None], NoReturn]) -> NoReturn:
        for i in range(8):
            for j in range(8):
                func(Position(i, j), self.pieces[i][j])
