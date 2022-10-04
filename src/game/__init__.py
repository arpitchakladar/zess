from typing import Optional
import pygame
from position import Position
from board import Board
from board.side import Side
from board.piece import Piece, PieceType

class Game:
    is_running: bool
    window: Optional[pygame.surface.Surface]
    display_size: int
    square_size: int
    font: pygame.font.Font
    side: Side
    board: Board
    selected_piece: Optional[Piece]
    piece_images: list[pygame.surface.Surface]

    def __init__(self, side: Side = Side.WHITE, display_size: int = 640) -> None:
        pygame.init()
        pygame.font.init()
        self.is_running = False
        self.display_size = display_size
        self.font = pygame.font.SysFont("arial", 25) # using arial as it is supported in virtually all platforms
        self.side = side
        self.board = Board()
        self.window = None
        self.selected_piece = None
        self.board.arrange_pieces()
        self.piece_images = []
        self.square_size = int(self.display_size / 8)
        piece_size = self.square_size * 0.8
        # The PieceType enum values will correspond to their indexes
        # Each PieceType will occupy 2 elements, the first being white and second being black
        for piece_type in PieceType:
            piece_image = pygame.image.load(f"res/images/pieces/w_{piece_type}.png")
            piece_image = pygame.transform.scale(piece_image, (piece_size, piece_size))
            self.piece_images.append(piece_image)
            piece_image = pygame.image.load(f"res/images/pieces/b_{piece_type}.png")
            piece_image = pygame.transform.scale(piece_image, (piece_size, piece_size))
            self.piece_images.append(piece_image)

    def draw_board(self) -> None:
        assert self.window is not None
        window: pygame.surface.Surface = self.window
        self.square_size: int = int(self.display_size / 8)
        dark_color: tuple[int, int, int] = (125, 206, 160)
        light_color: tuple[int, int, int] = (232, 248, 245)
        def draw_square(position: Position, piece: Optional[Piece]) -> bool:
            i, j = position.column, position.row
            if self.side == Side.WHITE:
                j = 7 - j
            color = dark_color
            is_selected = False
            if self.selected_piece != None:
                assert self.selected_piece is not None
                if self.selected_piece.position == position:
                    color = (214, 219, 223)
                    is_selected = True
            if not is_selected and (i + j + self.side.value) % 2 == 0:
                color = light_color
            x = i * self.square_size
            y = j * self.square_size
            pygame.draw.rect(window, color, pygame.Rect(x, y, self.square_size, self.square_size))
            if piece != None:
                assert piece is not None
                offset = self.square_size * 0.1
                window.blit(self.piece_images[2 * piece.piece_type.value + piece.side.value], (x + offset, y + offset))
            return True

        self.board.for_each_square(draw_square)
        b, c = self.side.value * 7, 1 - 2 * self.side.value

        for i in range(8):
            color = light_color if (i + self.side.value) % 2 == 0 else dark_color
            column_index = self.font.render(chr(b + 97), False, color)
            row_index = self.font.render(chr(b + 49), False, color)
            window.blit(column_index, (self.square_size * (i + 1) - 11, self.display_size - 20))
            window.blit(row_index, (2, self.square_size * (7 - i) + 2))
            b += c

    def get_clicked(self, position: tuple[int, int]) -> Optional[Piece]:
        x: int = position[0]
        y: int = position[1]
        self.selected_piece = None
        def check_clicked(position: Position, piece: Optional[Piece]) -> bool:
            if piece != None:
                piece_x = position.column * self.square_size
                piece_y = position.row
                if self.side == Side.WHITE:
                    piece_y = 7 - piece_y
                piece_y *= self.square_size
                if piece_x < x < (piece_x + self.square_size) and piece_y < y < (piece_y + self.square_size):
                    self.selected_piece = piece
                    return False
            return True
        self.board.for_each_square(check_clicked)

    def run(self) -> None:
        self.is_running = True
        self.window = pygame.display.set_mode((self.display_size, self.display_size))
        self.selected_piece = None
        pygame.display.set_caption("Zess")
        icon = pygame.image.load("res/images/zess-logo.png")
        pygame.display.set_icon(icon)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    break
                elif event.type == pygame.MOUSEBUTTONUP:
                    position = pygame.mouse.get_pos()
                    self.get_clicked(position)
                self.draw_board()
                pygame.display.update()

        pygame.quit()
