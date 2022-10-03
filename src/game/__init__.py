from typing import NoReturn, Union
import pygame
from position import Position
from board import Board
from board.side import Side
from board.piece import Piece

class Game:
    is_running: bool
    window: pygame.Surface
    display_size: int
    font: pygame.font.Font
    side: Side
    board: Board

    def __init__(self, side: Side = Side.WHITE, display_size: int = 640):
        pygame.init()
        pygame.font.init()
        self.is_running = False
        self.display_size = display_size
        self.font = pygame.font.SysFont("arial", 25) # using arial as it is supported in virtually all platforms
        self.side = side
        self.board = Board()
        self.board.arrange_pieces()

    def draw_board(self) -> NoReturn:
        # Flipping the board if white is playing
        a, b, c = 0, 7, -1
        if self.side == Side.WHITE:
            a, b, c = 1, 0, 1

        square_size = self.display_size / 8
        dark_color = (125, 206, 160)
        light_color = (232, 248, 245)
        def draw_square(position: Position, piece: Union[Piece, None]) -> NoReturn:
            i, j = position.column, (7 - position.row) # Pygame uses top left as the origin but in chess the bottom left square is the origin
            color = light_color if (i + j + a) % 2 == 0 else dark_color
            pygame.draw.rect(self.window, color, pygame.Rect(i * square_size, j * square_size, square_size, square_size))

        self.board.for_each_square(draw_square)

        for i in range(8):
            color = light_color if (i + a) % 2 == 0 else dark_color
            column_index = self.font.render(chr(b + 97), False, color)
            row_index = self.font.render(chr(b + 49), False, color)
            self.window.blit(column_index, (square_size * (i + 1) - 11, self.display_size - 20))
            self.window.blit(row_index, (2, square_size * (7 - i) + 2))
            b += c

    def run(self) -> NoReturn:
        self.is_running = True
        self.window = pygame.display.set_mode((self.display_size, self.display_size))
        pygame.display.set_caption("Zess")
        icon = pygame.image.load("res/images/zess-logo.png")
        pygame.display.set_icon(icon)
        timer = pygame.USEREVENT + 1
        pygame.time.set_timer(timer, 5000)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    break
                if event.type == timer: # alternating between black side and white side every 5 seconds
                    self.side = Side((self.side.value + 1) % 2)
                self.draw_board()
                pygame.display.update()

        pygame.quit()
