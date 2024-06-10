import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, font, text_col, x, y):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.text = text
        self.font = font
        self.text_col = text_col
        self.x = x
        self.y = y
           
    def show(self):
        img = self.font.render(self.text, True, self.text_col)
        self.screen.blit(img, (self.x, self.y))
    
    def show_update(self, text):
        img = self.font.render(text, True, self.text_col)
        self.screen.blit(img, (self.x, self.y))

    def show_rank(self, text = '', n = ''):
        img = self.font.render(n + text, True, self.text_col)
        self.screen.blit(img, (self.x, self.y))
        