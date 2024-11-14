import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x,y = 0, 0

        while running:
            screen.fill("light pink")
            for i in range (1, 640//32):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))
            for j in range (1, 512//32):
                pygame.draw.line(screen, "black", (0, j*32), (640, j*32))
            screen.blit(mole_image, mole_image.get_rect(topleft = (x,y)))
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    a = a//32*32
                    b = b//32*32
                    if (a, b) == (x, y):
                        (x, y) = (random.randrange(0,20)*32, random.randrange(0,16)*32)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
