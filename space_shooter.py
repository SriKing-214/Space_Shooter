import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False