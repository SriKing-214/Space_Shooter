import pygame
import random
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Space Shooter")
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100

# imports
player_surf = pygame.image.load(join('images', 'spaceship.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGTH / 2))
player_direction = 1


star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGTH)) for i in range(20)]

astroid_surf = pygame.image.load(join('images', 'astroid.png')).convert_alpha()
astroid_rect = astroid_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGTH / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGTH - 20))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # this draws the game
    screen.fill('darkgray')
    for position in star_positions:
        screen.blit(star_surf, position)
    
    screen.blit(astroid_surf, astroid_rect)
    screen.blit(laser_surf, laser_rect)
    
    # player movement
    player_rect.x += player_direction * 0.4
    if player_rect.right >= WINDOW_WIDTH:
        player_rect.right = WINDOW_WIDTH
        player_direction *= -1
    if player_rect.left <= 0:
        player_rect.left = 0
        player_direction *= -1
        
    screen.blit(player_surf, player_rect)
    pygame.display.update()



pygame.quit()       