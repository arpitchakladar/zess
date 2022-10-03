from typing import NoReturn, Optional
import pygame
from position import Position
from board import Board
from board.side import Side
from board.piece import Piece, PieceType

class Game:
    is_running: bool
    window: pygame.surface.Surface
    display_size: int
    font: pygame.font.Font
    side: Side
    board: Board
    piece_images: list[pygame.Surface]

    def __init__(self, side: Side = Side.WHITE, display_size: int = 640) -> None:
        pygame.init()
        pygame.font.init()
        self.is_running = False
        self.window = pygame.display.set_mode((self.display_size, self.display_size))
        self.display_size = display_size
        self.font = pygame.font.SysFont("arial", 25) # using arial as it is supported in virtually all platforms
        self.side = side
        self.board = Board()
        self.board.arrange_pieces()
        self.piece_images = []
        square_size = self.display_size / 8
        piece_size = square_size * 0.8
        # The PieceType enum values will correspond to their indexes
        # Each PieceType will occupy 2 elements, the first being white and second being black
        for piece_type in PieceType:
            piece_image = pygame.image.load(f"res/images/pieces/w_{piece_type}.png")
            piece_image = pygame.transform.scale(piece_image, (piece_size, piece_size))
            self.piece_images.append(piece_image)
            piece_image = pygame.image.load(f"res/images/pieces/b_{piece_type}.png")
            piece_image = pygame.transform.scale(piece_image, (piece_size, piece_size))
            self.piece_images.append(piece_image)

    def draw_board(self) -> NoReturn:
        square_size: int = int(self.display_size / 8)
        dark_color: tuple[int, int, int] = (125, 206, 160)
        light_color: tuple[int, int, int] = (232, 248, 245)
        def draw_square(position: Position, piece: Optional[Piece]) -> NoReturn:
            i, j = position.column, position.row
            if self.side == Side.BLACK:
                i = 7 - i
            else:
                j = 7 - j
            color = light_color if (i + j + self.side.value) % 2 == 0 else dark_color
            x = i * square_size
            y = j * square_size
            pygame.draw.rect(self.window, color, pygame.Rect(x, y, square_size, square_size))
            if piece != None:
                assert piece is not None
                offset = square_size * 0.1
                self.window.blit(self.piece_images[2 * piece.piece_type.value + piece.side.value], (x + offset, y + offset))

        self.board.for_each_square(draw_square)
        b, c = self.side.value * 7, 1 - 2 * self.side.value

        for i in range(8):
            color = light_color if (i + self.side.value) % 2 == 0 else dark_color
            column_index = self.font.render(chr(b + 97), False, color)
            row_index = self.font.render(chr(b + 49), False, color)
            self.window.blit(column_index, (square_size * (i + 1) - 11, self.display_size - 20))
            self.window.blit(row_index, (2, square_size * (7 - i) + 2))
            b += c

    def run(self) -> NoReturn:
        self.is_running = True
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
