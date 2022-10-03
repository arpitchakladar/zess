class Position:
    column: int
    row: int

    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row

    def __str__(self) -> str:
        return f"{chr(self.column + 97)}{self.row + 1}"
