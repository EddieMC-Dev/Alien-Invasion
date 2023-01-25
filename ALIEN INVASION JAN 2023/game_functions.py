import sys
from time import sleep

import pygame
from pygame import mixer_music

from bullet import CreateBullet
from alien import CreateAlien


def check_keydown(event, settings, window, ship, bullets):
    """Verifica eventos de pressionamentos de tecla."""
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_SPACE:
        if settings.shot_limit > len(bullets):
            new_bullet = CreateBullet(settings, window, ship)
            bullets.add(new_bullet)
            play_bullet_sound()

def check_keyup(event, ship):
    """Verifica eventos de solturas de tecla."""
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False    

def check_mousebuttondown(settings, window, 
                          aliens, ship, bullets, new_game_button, 
                          high_score_button, quit_button, back_menu_button):
    """Verifica eventos de pressionamentos do mouse."""
    if not settings.game_active:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if not settings.menu_high_score:   
            check_new_game(settings, window, aliens, ship, bullets, 
                        new_game_button, mouse_x, mouse_y)     
            check_high_score(settings, high_score_button, mouse_x, mouse_y)       
            check_quit_game(quit_button, mouse_x, mouse_y)   
        else:
            check_back_menu(settings, back_menu_button, mouse_x, mouse_y)        
          
def check_events(settings, window, ship, bullets, 
                 aliens, new_game_button, high_score_button, 
                 quit_button, back_menu_button):
    """Verifica eventos de teclas e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mousebuttondown(settings, window, 
                                  aliens, ship, bullets, new_game_button,
                                  high_score_button, quit_button, 
                                  back_menu_button) 
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, window, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def check_new_game(settings, window, aliens, ship, bullets, 
                   new_game_button, mouse_x, mouse_y):
    """Verifica se um novo jogo foi requisitado e responde adequadamente."""
    if new_game_button.second_rect.collidepoint((mouse_x, mouse_y)):
        pygame.mouse.set_visible(False)
        settings.game_active = True
        reset_sprites(settings, window, aliens, ship, bullets)     
    
def check_high_score(settings, high_score_button, mouse_x, mouse_y):
    """Verifica se o botão High Score foi acionado para exibir a pontuação
    máxima do jogador.""" 
    if high_score_button.second_rect.collidepoint((mouse_x, mouse_y)):
        settings.menu_high_score = True   

def check_back_menu(settings, back_menu_button, mouse_x, mouse_y):
    """Verifica se o usuário acionou pra retornar ao menu principal."""
    if back_menu_button.second_rect.collidepoint((mouse_x, mouse_y)): 
        settings.menu_high_score = False      

def high_score_place(settings, window, back_menu_button, sb):
    """Abre uma nova tela dentro do menu, para mostra a pontuação máxima."""
    sb.prep_menu_high_score()
    window.fill(settings.bg_color)
    window.blit(sb.title_img, sb.title_rect)
    window.blit(sb.numbers_img, sb.numbers_rect)
    back_menu_button.draw_button()
    pygame.display.flip()

def check_quit_game(quit_button, mouse_x, mouse_y):
    """Verifica se o jogo foi fechado."""
    if quit_button.second_rect.collidepoint((mouse_x, mouse_y)):
        sys.exit()
    
def reset_sprites(settings, window, aliens, ship, bullets):
    """Reinicia todos os sprites existentes."""
    sleep(0.25)
    ship.reset()
    bullets.empty()
    aliens.empty()
    create_aliens_fleet(settings, window, ship, aliens)

def check_game_over(settings, sb):  
    """Verifica se o jogador perdeu todas as vidas e 
    ativa o restart do jogo."""      
    if settings.player_lifes == 0:
        sb.prep_high_score()
        pygame.mouse.set_visible(True)
        settings.game_reset()
 
def update_menu(settings, window, new_game_button, 
                high_score_button, quit_button):
    """Atualiza as operações realizadas no menu quando o jogo está inativo."""
    window.fill(settings.bg_color)
    
    
    alien_image = pygame.image.load("images/menu.png")
    alien_image = pygame.transform.smoothscale(alien_image, (900, 600))
    alien_image_rect = alien_image.get_rect()
    window_rect = window.get_rect()
    
    alien_image_rect.center = window_rect.center
    

    window.blit(alien_image, alien_image_rect)  
        
    new_game_button.draw_button()
    high_score_button.draw_button()
    quit_button.draw_button() 
    
    pygame.display.flip()  
  
def play_bullet_sound():
    """Toca o som do disparo da bala."""
    mixer_music.load('audios/laser.mp3')
    mixer_music.set_volume(0.25)
    mixer_music.play()

def clear_missing_bullets(bullets):
    """Limpa os projéteis que sumiram da janela."""
    for bullet in bullets.copy():
        if bullet.y < 0:
            bullets.remove(bullet)

def check_if_shoot(bullets):
    """Verifica se um projétil foi disparado."""
    if bullets.sprites():
        for bullet in bullets.sprites():
            bullet.shoot_bullet()
            
def update_bullets(bullets):
    """Atualiza os projéteis em caso de disparo ou desaparecimento."""
    check_if_shoot(bullets)
    clear_missing_bullets(bullets)

def check_zero_aliens(settings, window, ship, bullets, aliens):
    """Verifica a ausência de aliens e responde apropriadamente."""
    if len(aliens) == 0:
        bullets.empty()
        create_aliens_fleet(settings, window, ship, aliens)
        settings.increase_difficulty()

def play_dead_ship_sound():
    """Toca o som de morte da espaçonave após uma colisão."""
    mixer_music.load('audios/ship_died.mp3')
    mixer_music.set_volume(0.5)
    mixer_music.play()
    sleep(0.75)

def check_ship_hit(settings, window, aliens, ship, bullets):
    """Responde caso haja colisão entre a espaçonave e um dos aliens."""
    for alien in aliens.sprites():
        if pygame.sprite.spritecollideany(ship, aliens):
            settings.player_lifes -= 1
            play_dead_ship_sound()
            reset_sprites(settings, window, aliens, ship, bullets)
            break

def check_alien_hit(settings, aliens, bullets, sb):
    """Verifica se deve tocar o som de morte do alien."""
    for alien in aliens.sprites():     
        if pygame.sprite.spritecollide(alien, bullets, True):
            aliens.remove(alien)
            sb.score += settings.alien_point
            sb.prep_score()
            if sb.high_score < sb.score:
                sb.high_score = sb.score 
                sb.prep_high_score()
            mixer_music.load('audios/alien_died.mp3')
            mixer_music.set_volume(0.15)
            mixer_music.play()

def aliens_drop(settings, aliens):
    """Faz com que a frota de aliens desça."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop 

def check_alien_edge(settings, window, aliens, ship, bullets):
    """Responde caso um alien toque em qualquer borda da janela"""
    for alien in aliens.sprites():
        if alien.check_edges():
            settings.move_direction *= -1
            aliens_drop(settings, aliens)
            break
        
    for alien in aliens.sprites():
        if alien.rect.bottom >= settings.window_height:
            reset_sprites(settings, window, aliens, ship, bullets)

def update_aliens(settings, window, aliens, ship, bullets, sb):
    """Atualiza as posições da frota de aliens e detecta eventos de colisão."""
    aliens.update()
    check_ship_hit(settings, window, aliens, ship, bullets)
    check_game_over(settings, sb)
    check_alien_hit(settings, aliens, bullets, sb)
    check_zero_aliens(settings, window, ship, bullets, aliens)
    check_alien_edge(settings, window, aliens, ship, bullets)

def get_aliens_by_row(settings, alien_width):
    """Calcula quantos aliens cabem em uma linha"""
    available_space_x = settings.window_width - 2 * alien_width
    aliens_number_x = int(available_space_x / (2 * alien_width))
    return aliens_number_x

def get_rows_number(settings, alien_height, ship_height):
    """Calcula quantas linhas com aliens cabem na janela."""
    space_removed = 3 * alien_height + 2 * ship_height
    available_space_y = (settings.window_height - space_removed)
    rows_number = int(available_space_y / (2 * alien_height))
    return rows_number

def create_alien(settings, window, aliens, 
                 alien_width, alien_height, alien_number, row_number):
    """Cria um alien para a frota."""
    alien = CreateAlien(settings, window)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)

def create_aliens_fleet(settings, window, ship, aliens):
    """Realiza os cálculos e constrói a frota de aliens."""
    alien = CreateAlien(settings, window)
    alien_width, alien_height = alien.rect.width, alien.rect.height
    aliens_by_row = get_aliens_by_row(settings, alien_width)
    rows_number = get_rows_number(settings, alien_height, ship.rect.height)
    
    for row_number in range(rows_number):
        for alien_number in range(aliens_by_row):
            create_alien(settings, window, aliens, alien_width, alien_height, 
                        alien_number, row_number)
            
def update_window(settings, window, ship, bullets, aliens, sb):
    """Atualiza todos os elementos na janela."""
    window.fill(settings.bg_color)
    
    sb.show_score()
    settings.show_lifes()
    settings.show_level()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    for alien in aliens.sprites():
        alien.insert_alien()
            
    ship.insert_ship()
       
    pygame.display.flip()
    
