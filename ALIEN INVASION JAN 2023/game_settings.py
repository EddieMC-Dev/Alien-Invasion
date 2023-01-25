import pygame

class GameSettings():
    def __init__(self):
        self.window = None
        self.game_reset()
        
        # Window
        self.game_title = 'Alien Invasion'
        self.icon = pygame.image.load('images/alien.bmp')
        self.window_width = 1200
        self.window_height = 800
        self.bg_color = (0, 0, 50)
        self.menu_high_score = False
        
        # Bullets
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
              
        # Ship 
        self.shot_limit = 3 
        
        # Aliens    
        self.fleet_drop = 10
        
        # Taxa de aumento da dificuldade do jogo
        self.difficulty_increase_rate = 1.1
        
        # Taxa de crescimento da pontuação
        self.increase_score = 1.5
    
    def increase_difficulty(self):
        """Aumenta a dificuldade do jogo."""
        self.ship_speed *= self.difficulty_increase_rate
        self.alien_speed *= self.difficulty_increase_rate
        self.bullet_speed *= self.difficulty_increase_rate
        self.alien_point = self.alien_point * self.increase_score
        self.level += 1
        
    def game_reset(self):
        """Recupera as configurações padrões do jogo após um game over."""
        self.game_active = False
        self.player_lifes = 3   
        
        self.bullet_speed = 1
        self.ship_speed = 1.5
        
        self.alien_point = 50
        self.alien_speed = 1
        self.move_direction = 1  # 1 = right: -1 = left 
        
        self.level = 1
        
    def show_lifes(self):
        """Mostra as vidas do jogador na tela."""
        self.window_rect = self.window.get_rect()
        
        self.life_img = pygame.image.load("images/ship.bmp")
        self.life_img = pygame.transform.smoothscale(self.life_img, (30, 30))
        self.life_rect = self.life_img.get_rect() 
        self.life_rect.x = 0
        self.life_rect.top = self.window_rect.top
        
        for life in range(self.player_lifes):
            self.life_rect.x = self.life_rect.width * life
            self.window.blit(self.life_img, self.life_rect)     
            
    def show_level(self):
        """Exibe o level atual do jogo."""
        self.font = pygame.font.SysFont(None, 48)    
        self.level_color = (190, 190, 190) 
        self.level_str = f"Level {self.level}"
        self.level_img = self.font.render(self.level_str, True, 
                                          self.level_color)
        
        self.level_rect = self.level_img.get_rect()
        self.level_rect.left = 100
        self.level_rect.top = 0
        self.window.blit(self.level_img, self.level_rect)
        