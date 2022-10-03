from typing import NoReturn
import pygame

class Game:
    is_running: bool
    window: pygame.Surface
    display_size: int

    def __init__(self, display_size: int = 640):
        self.is_running = False
        self.window = pygame.display.set_mode((display_size, display_size))
        self.display_size = display_size

    def draw_board(self):
        cell_size = self.display_size / 8
        dark_color = (125, 206, 160)
        light_color = (232, 248, 245)
        for i in range(8):
            for j in range(8):
                color = dark_color
                if (i + j) % 2 == 0:
                    color = light_color
                pygame.draw.rect(self.window, color, pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size))

    def run(self) -> NoReturn:
        self.is_running = True
        pygame.init()
        pygame.display.set_caption("Zess")
        icon = pygame.image.load("resources/images/zess-logo.png")
        pygame.display.set_icon(icon)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    break
                self.draw_board()
                pygame.display.update()

        pygame.quit()
