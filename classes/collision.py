import pygame
from pygame.locals import *


class Collision:
    def __init__(self,):
        self.screen = pygame.display.set_mode((1920, 1080))
    def surface(self, posx, posy , sizex, sizey):
        pygame.Rect(posx, posy, sizex, sizey)