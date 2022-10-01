import pygame

WIDTH, HEIGHT = 900, 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    pygame.display.set_caption("Zess");
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()
