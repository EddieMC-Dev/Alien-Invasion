import pygame
from pygame.sprite import Sprite


class CreateShip(Sprite):
    def __init__(self, settings, window):
        super().__init__()
        self.settings = settings
        self.window = window
        self.window_rect = window.get_rect()
        
        # Coleta o valor rect e inicializa a posição inicial da nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.reset()    
        
        # Flags de movimento para esquerda e direita
        self.move_left = False
        self.move_right = False
             
    def reset(self):
        self.rect.center = self.window_rect.center
        self.rect.bottom = self.window_rect.bottom
        self.x = float(self.rect.x)
        
    def insert_ship(self):
        self.window.blit(self.image, self.rect)

    def move_ship(self):
        """Responsável por mover a nave caso o jogador ative uma flag."""
        if self.move_right and self.rect.right < self.window_rect.width:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x
    