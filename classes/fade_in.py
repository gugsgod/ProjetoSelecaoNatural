import pygame
from pygame.locals import *

class FadeIn:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.fade_img = pygame.Surface((1920, 1080)).convert_alpha()
        self.fade_alpha =  255
        self.fade_rect = ((0, 0, 1920, 1080))


    def show(self):
        self.fade_img.fill('BLACK')
        self.screen.blit(self.fade_img, self.fade_rect)
            
        if self.fade_alpha > 0:
            self.fade_alpha -= 30
            self.fade_img.set_alpha(self.fade_alpha)
    
    def reset(self):
        self.fade_alpha = 255