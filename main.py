import pygame
import random
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Space Shooter")
running = True


surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100


player_surf = pygame.image.load(join('images', 'spaceship.png')).convert_alpha()
astroid_surf = pygame.image.load(join('images', 'astroid.png')).convert_alpha()
astroid_postions = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGTH)) for i in range(20)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("darkgray")
    for position in astroid_postions:
        screen.blit(astroid_surf, position)
    
    x += 0.1
    screen.blit(player_surf, (x,150))
 
    pygame.display.update()
    


pygame.quit()       