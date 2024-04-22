import pygame
from pygame.locals import *
import random
from animal import Animal

class Butterfly(Animal):
    def __init__(self, img, pos):
        super().__init__(img, pos)
    
    def show(self):
        super().show()

    def movement(self):
        super().movement()
        
    def collision_screen(self):
        super().collision_screen()