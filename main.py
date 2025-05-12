import pygame
from pygame.locals import *
import ctypes
import tetris
import slither
import Rithomgame

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

current_selection = 0
is_space_pressed = False

screen = pygame.display.set_mode(screensize, FULLSCREEN)

font = pygame.font.Font('font/a시월구일1.ttf',52)

Tetris = pygame.image.load('image/tetris.png')
Slither = pygame.image.load('image/slither.png')
Music = pygame.image.load('image/music.png')

btn_width = Tetris.get_width()
btn_height = Tetris.get_height()

button_spacing = 100
button_x = (screensize[0] // 2) - (((btn_width * 3) + button_spacing * 2) // 2)
button_y = (screensize[1] // 2) + 100
tetris_rect = pygame.Rect(button_x, button_y, btn_width, btn_height)
slither_rect = pygame.Rect(button_x + btn_width + button_spacing, button_y, btn_width, btn_height)
music_rect = pygame.Rect(button_x + (btn_width + button_spacing) * 2, button_y, btn_width, btn_height)


tetris_active = False
slither_active = False
galaga_active = False

def main_menu():
    global current_selection, is_space_pressed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif event.key == K_SPACE:
                    is_space_pressed = True
                elif event.key == K_RIGHT:
                    current_selection = (current_selection + 1) % 3
                elif event.key == K_LEFT:
                    current_selection = (current_selection - 1) % 3

                if is_space_pressed:
                    if current_selection == 0:
                        print('Tetris button clicked!')
                        App = tetris.App()
                        App.run()
                        main_menu()
                    elif current_selection == 1:
                        print('Slither button clicked!')
                        App = slither.App()
                        App.run()
                        main_menu()
                    elif current_selection == 2:
                        print('Music button clicked!')
                        App = Rithomgame.Rithomgame_run()
                        App.run()
                        main_menu()

                elif event.type == KEYUP:
                    if event.key == K_SPACE:
                        is_space_pressed = False

            elif event.type == QUIT:
                running = False
                
        render()

def render():
    screen.fill(BLACK)

    if current_selection == 0:
        screen.blit(pygame.transform.scale(Tetris, (btn_width + 10, btn_height + 10)),
                    (tetris_rect.x - 5, tetris_rect.y - 5))
        pygame.draw.rect(screen, (255, 0, 0), tetris_rect.inflate(10, 10), 5)
    else:
        screen.blit(Tetris, tetris_rect)

    if current_selection == 1:
        screen.blit(pygame.transform.scale(Slither, (btn_width + 10, btn_height + 10)),
                    (slither_rect.x - 5, slither_rect.y - 5))
        pygame.draw.rect(screen, (255, 0, 0), slither_rect.inflate(10, 10), 5)
    else:
        screen.blit(Slither, slither_rect)

    if current_selection == 2:
        screen.blit(pygame.transform.scale(Music, (btn_width + 10, btn_height + 10)),
                    (music_rect.x - 5, music_rect.y - 5))
        pygame.draw.rect(screen, (255, 0, 0), music_rect.inflate(10, 10), 5)
    else:
        screen.blit(Music, music_rect)

    text_surface = font.render('게임을 고르세요!', True, WHITE)

    text_rect = text_surface.get_rect()
    text_rect.center = screen.get_rect().center

    screen.blit(text_surface, text_rect)

    pygame.display.flip()

main_menu()
