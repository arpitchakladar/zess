from typing import NoReturn
import pygame

class Game:
    is_running: bool
    window: pygame.Surface
    display_size: int
    font: pygame.font.Font
    white_playing: bool

    def __init__(self, side: str = "white", display_size: int = 640):
        pygame.init()
        pygame.font.init()
        self.is_running = False
        self.display_size = display_size
        self.font = pygame.font.SysFont("arial", 25)
        self.white_playing = side.lower().strip() != "black"

    def draw_board(self) -> NoReturn:
        # Flipping the board if white is playing
        a = 1
        b = 7
        c = -1
        if self.white_playing:
            a = 0
            b = 0
            c = 1

        cell_size = self.display_size / 8
        dark_color = (125, 206, 160)
        light_color = (232, 248, 245)
        for i in range(8):
            for j in range(8):
                color = light_color if (i + j + a) % 2 == 0 else dark_color
                pygame.draw.rect(self.window, color, pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size))

        for i in range(8):
            color = light_color if (i + a) % 2 == 0 else dark_color
            column_index = self.font.render(chr(b + 97), False, color)
            row_index = self.font.render(chr(b + 49), False, color)
            self.window.blit(column_index, (cell_size * (i + 1) - 11, self.display_size - 20))
            self.window.blit(row_index, (2, cell_size * (7 - i) + 2))
            b += c

    def run(self) -> NoReturn:
        self.is_running = True
        self.window = pygame.display.set_mode((self.display_size, self.display_size))
        pygame.display.set_caption("Zess")
        icon = pygame.image.load("resources/images/zess-logo.png")
        pygame.display.set_icon(icon)
        timer = pygame.USEREVENT + 1
        pygame.time.set_timer(timer, 5000)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    break
                if event.type == timer: # alternating between black side and white side every 5 seconds
                    self.white_playing =  not self.white_playing
                self.draw_board()
                pygame.display.update()

        pygame.quit()
