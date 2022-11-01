import pygame
from constans import FOOD_BACKGROUND, FOOD_SIZE

class Food(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.color = FOOD_BACKGROUND
        
        self.image = pygame.Surface(FOOD_SIZE)
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        self.checked = False
    
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    
    def eaten(self):
        self.color = (0, 0, 0)
        self.image.fill(self.color)
        
        self.checked = True