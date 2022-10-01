from typing import NoReturn
import pygame

WIDTH, HEIGHT = 640, 640

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main() -> NoReturn:
    pygame.display.set_caption("Zess")
    icon = pygame.image.load("resources/images/zess-logo.png")
    pygame.display.set_icon(icon)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()
