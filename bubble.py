import pygame
from constans import PLAYER_BACKGROUND

class Bubble(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = 40
        self.height = 40
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 3
        self.direction = 0
        
        self.recalculate_rect_size()
       
    
    def draw(self, surface):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        surface.blit(self.image, self.rect)
    

    def up(self):
        self.direction = 0
        
    def right(self):
        self.direction = 1
        
        
    def down(self):
        self.direction = 2
        
    
    def left(self):
        self.direction = 3
        
    
    def move(self):
        if self.direction == 0:
            self.pos_y -= self.speed
        
        elif self.direction == 1:
            self.pos_x += self.speed
        
        elif self.direction == 2:
            self.pos_y += self.speed
        
        elif self.direction == 3:
            self.pos_x -=  self.speed


    def eaten(self):
        self.add_speed()
        self.increment_size()
        
        self.recalculate_rect_size()
        

    def recalculate_rect_size(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        
        pygame.draw.circle(self.image, PLAYER_BACKGROUND, self.rect.center, self.width // 2 )
        

    def add_speed(self):
        self.speed = self.speed
        
    
    def increment_size(self):
        self.width += 10
        self.height += 10