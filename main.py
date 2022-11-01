import pygame
import random

from constans import WHITE
from constans import SCREEN_SIZE

from food import Food
from bubble import Bubble

pygame.init()

game = True

surface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Introducción a la programación.')

clock = pygame.time.Clock()

player = Bubble(100, 100)

sprites = pygame.sprite.Group()
for _ in range(0, 20):
    sprites.add(Food(random.randint(0, 600), random.randint(0, 600) ))


while game:
    clock.tick(60)

    key_pressed = pygame.key.get_pressed()
    
    if key_pressed[pygame.K_RIGHT]:
        player.right()
        
    if key_pressed[pygame.K_LEFT]:
        player.left()
        
    if key_pressed[pygame.K_UP]:
        player.up()
        
    if key_pressed[pygame.K_DOWN]:
        player.down()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    
    player.move()
    
    surface.fill(WHITE)
    
    sprites.draw(surface)
    sprites.update()
    
    for point in sprites:
        if pygame.sprite.collide_mask(player, point) and not point.checked: # colide_rect # collide_circle
            point.eaten()
            player.eaten()
            
            sprites.remove(point)

    player.draw(surface)
    pygame.display.flip()
