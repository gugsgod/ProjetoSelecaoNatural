import pygame
from pygame.locals import *
import sys

class ButtonMenu:
    def __init__(self, posx, posy):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.button_menu_1 = pygame.image.load('img.button_menu_1.png').convert_alpha()
        self.button_menu_2 = pygame.image.load('img.button_menu_2.png').convert_alpha()
        self.posx = posx
        self.posy = posy
        self.buttom_size = [293, 112]
        self.rect_button = pygame.Rect(self.posx, posy, self.buttom_size[0], self.buttom_size[1])
        self.mouse = pygame.mouse.get_pos()

    def show(self):
        self.screen.blit(self.button_menu_1, (self.posx, self.posy))
        if self.rect_button.collidepoint(self.mouse):
            self.screen.blit(self.button_menu_2, (self.posx, self.posy))

    def click_enter(self):
        if self.rect_button.collidepoint(self.mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                self.click_action