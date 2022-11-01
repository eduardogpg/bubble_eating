import sys
import pygame
 
game = True

pygame.init()
screen = pygame.display.set_mode((400, 300))

WHITE = (0, 0, 0)
SPEED = 2

pos_x, pos_y = 0, 0
clock = pygame.time.Clock()

while game:
    
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x -= 1
            
            if event.key == pygame.K_RIGHT:
                pos_x += 1

    screen.fill(WHITE)
    pygame.draw.circle(screen, (13, 234, 144), [pos_x, 150], 30, 0)

    pygame.display.update()
    
pygame.quit()