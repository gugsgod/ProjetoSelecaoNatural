import pygame
from pygame.locals import *

class FadeIn:
    def __init__(self, fade_img, fade_alpha, fade_rect):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.fade_img = fade_img
        self.fade_alpha = fade_alpha
        self.fade_rect = fade_rect


    def show(self):
        
        self.fade_img.fill('BLACK')
        self.screen.blit(self.fade_img, self.fade_rect)
            
        if self.fade_alpha > 0:
            self.fade_alpha -= 30
            self.fade_img.set_alpha(self.fade_alpha)
    
    def reset(self):
        self.fade_alpha = 255