import pygame
from pygame.sprite import Group

import game_functions as gf
from game_settings import GameSettings
from scoreboard import Scoreboard 
from buttons import CreateButton
from ship import CreateShip


def run_game():
    """Inicializa os pacotes do pygame, as configurações, a janela, 
    os conjuntos de sprites e todas as funcionalidades do jogo."""
    pygame.init()
    
    settings = GameSettings()
    window = pygame.display.set_mode((settings.window_width, 
                                      settings.window_height))
    pygame.display.set_caption(settings.game_title) 
    pygame.display.set_icon(settings.icon)
    settings.window = window
    
    ship = CreateShip(settings, window)
    bullets = Group()
    aliens = Group()
    
    sb = Scoreboard(settings, window)
       
    # Define botões pro menu
    new_game_button = CreateButton(window, "New Game")
    high_score_button = CreateButton(window, "High Score")
    high_score_button.configure_high_score()
    back_menu_button = CreateButton(window, "Back to Menu")
    quit_button = CreateButton(window, "Quit Game")
    quit_button.configure_quit()
    
    gf.create_aliens_fleet(settings, window, ship, aliens)
    
    while True:
        gf.check_events(settings, window, ship, 
                        bullets,aliens, new_game_button, high_score_button, 
                        quit_button, back_menu_button)
        if settings.game_active:         
            ship.move_ship()
            gf.update_bullets(bullets)
            gf.update_aliens(settings,window, aliens, ship, bullets, sb)
            gf.update_window(settings, window, ship, bullets, aliens, sb)
            
        elif settings.menu_high_score:
            gf.high_score_place(settings, window, back_menu_button, sb)
            
        else:
            gf.update_menu(settings, window,
                           new_game_button, high_score_button, quit_button)
            
    
run_game()    
