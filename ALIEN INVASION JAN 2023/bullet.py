import pygame
from pygame.sprite import Sprite


class CreateBullet(Sprite):
    """Cria um projétil para ser disparado."""
    def __init__(self, settings, window, ship):
        super().__init__()
        self.settings = settings
        self.window = window
        
        # Constrói o projétil e o posiciona dentro da nave
        self.rect = pygame.Rect(0, 0, settings.bullet_width, 
                                settings.bullet_height)
        self.rect.center = ship.rect.center
        self.rect.top = ship.rect.top
    
        # Define uma posição float
        self.y = float(self.rect.y)
        
    def draw_bullet(self):
        pygame.draw.rect(self.window, self.settings.bullet_color, self.rect)
      
    def shoot_bullet(self):
        """Simula o disparo do projétil."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y  
        