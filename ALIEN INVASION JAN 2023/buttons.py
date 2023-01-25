import pygame

class CreateButton():
    """Cria um button personalizado para o jogador. """
    def __init__(self, window, msg):
        self.window = window
        self.window_rect = window.get_rect()
        
        self.configure()
         
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.second_bg_color) 
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.second_rect.center
        
    def draw_button(self):
        # Desenha as bordas do botão
        pygame.draw.rect(self.window, self.first_bg_color, self.first_rect)
        
        # Desenha o botão
        pygame.draw.rect(self.window, self.second_bg_color, self.second_rect)
        
        # Insere o texto do botão na tela
        self.window.blit(self.msg_image, self.msg_image_rect)
    
    def configure(self):
        """Por padrão, configura um botão personalizado no meio da janela."""
        self.width, self.height = 200, 50
        
        # Criando as bordas do botão
        self.first_bg_color = (255, 255, 255)
        self.first_rect = pygame.Rect(0, 0, self.width, self.height)
        self.first_rect.center = self.window_rect.center
        
        # Criando o botão
        self.second_bg_color = (0, 0, 0)
        self.second_rect = pygame.Rect(0, 0, self.width - 5, self.height - 5)
        self.second_rect.center = self.first_rect.center
    
    def configure_quit(self):
        """Configura um botão de saida do jogo."""
        self.first_rect.top = self.first_rect.bottom + 70
        self.second_rect.center = self.first_rect.center
        self.msg_image_rect.center = self.second_rect.center
    
    def configure_high_score(self):
        """Configura um botão de acesso a última pontuação mais alta."""
        self.first_rect.top = self.first_rect.bottom + 10
        self.second_rect.center = self.first_rect.center
        self.msg_image_rect.center = self.second_rect.center
    