import json

import pygame


class Scoreboard():
    """Classe que gerencia as pontuações do jogador."""
    def __init__(self, settings, window):
        self.settings = settings
        self.window = window 
        self.window_rect = window.get_rect()

        self.text_color = (190, 190, 190)
        self.font = pygame.font.SysFont(None, 54)
        
        self.score = 0
        self.load_high_score()
        self.prep_score()
        self.prep_high_score()
        self.prep_menu_high_score()
    
    def load_high_score(self):
        """Extrai a pontuação máxima do jogador."""
        try:
            with open("high_score.json") as file_object:
                self.high_score = json.load(file_object)
        except:
            self.high_score = 0
            self.save_high_score()
                
    def save_high_score(self):
        """Salva a pontuação máxima do jogador."""
        with open("high_score.json", "w") as file_object:
            json.dump(self.high_score, file_object)
        
    def prep_score(self):
        """Preparando a imagem renderizada para a pontuação."""
        self.score = round(int(self.score), -1)
        self.score_text = f"Score: {self.score:,}"
        self.score_img = self.font.render(self.score_text, True, 
                                          self.text_color, 
                                          self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.settings.window_width - 10
        self.score_rect.top = 10
     
    def prep_high_score(self):
        """Preparando a imagem renderizada para a pontuação máxima."""
        self.high_score_text = f"High score: {self.high_score:,}"
        self.high_score_img = self.font.render(self.high_score_text, True, 
                                               self.text_color,
                                               self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.center = self.window_rect.center
        self.high_score_rect.top = self.score_rect.top

        self.save_high_score()
     
    def prep_menu_high_score(self):
        """Preparando a imagem renderizada para a pontuação máxima no menu."""
        self.color = (0, 255, 0)
        
        self.title = "HIGH SCORE"    
        self.title_img = self.font.render(self.title, True, self.text_color)
        self.title_rect = self.title_img.get_rect()
        self.title_rect.centerx = self.window_rect.centerx
        self.title_rect.top = self.window_rect.top
        
        self.load_high_score()
        self.numbers = f"{self.high_score:,}"
        self.numbers_img = self.font.render(self.numbers, True, self.color)
        self.numbers_rect = self.numbers_img.get_rect()
        self.numbers_rect.center = self.title_rect.center
        self.numbers_rect.top = self.title_rect.bottom + 140
        
    def show_score(self):
        """Exibe a pontuação normal e a pontuação máxima na tela."""
        self.window.blit(self.score_img, self.score_rect)
        self.window.blit(self.high_score_img, self.high_score_rect)
        
    