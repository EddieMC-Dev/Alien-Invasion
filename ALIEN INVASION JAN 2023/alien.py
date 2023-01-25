import pygame
from pygame.sprite import Sprite


class CreateAlien(Sprite):
    """Cria um objeto como alien para a frota."""
    def __init__(self, settings, window):
        super().__init__()
        self.settings = settings
        self.window = window
        self.window_rect = window.get_rect()
        
        # Coleta o valor rect da figura do alien e a posiciona
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        self.x = self.rect.x
        
    def insert_alien(self):
        self.window.blit(self.image, self.rect)
        
    def update(self):
        self.x += self.settings.alien_speed * self.settings.move_direction
        self.rect.x = self.x
        
    def check_edges(self):
        if self.rect.x <= self.window_rect.x:
            return True
        elif self.rect.right >= self.window_rect.right:
            return True
        