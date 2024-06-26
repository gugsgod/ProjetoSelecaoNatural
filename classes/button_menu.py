import pygame
from pygame.locals import *
import sys

class ButtonMenu:
    def __init__(self, posx, posy, click_action = ''):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.button_menu_1 = pygame.image.load('images/buttons/img.button_menu_1.png').convert_alpha()
        self.button_menu_2 = pygame.image.load('images/buttons/img.button_menu_2.png').convert_alpha()
        self.posx = posx
        self.posy = posy
        self.button_size = [293, 112]
        self.rect_button = pygame.Rect(self.posx, self.posy, self.button_size[0], self.button_size[1])
        self.click_action = click_action

    def show(self):
        
        mouse = pygame.mouse.get_pos()
        self.screen.blit(self.button_menu_1, (self.posx, self.posy))
        if self.rect_button.collidepoint(mouse):
            self.screen.blit(self.button_menu_2, (self.posx -3, self.posy -3))
    
    def click(self):
        
        mouse = pygame.mouse.get_pos()
        if self.rect_button.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.click_action == 'level1':
                    return 'level1'    
                if self.click_action == 'rank':
                    return 'rank'
                if self.click_action == 'quit':
                    pygame.quit()
                    sys.exit()
                if self.click_action == 'login':
                    return 'login'
                if self.click_action == 'register':
                    return 'register'