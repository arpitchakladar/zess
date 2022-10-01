from typing import NoReturn
import pygame

class Game:
    is_running: bool
    window: pygame.Surface

    def __init__(self):
        run = False
        window = pygame.display.set_mode((640, 640))

    def run(self) -> NoReturn:
        is_running = True
        pygame.display.set_caption("Zess")
        icon = pygame.image.load("resources/images/zess-logo.png")
        pygame.display.set_icon(icon)
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    break

        pygame.quit()
