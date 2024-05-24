import pygame
from pygame.locals import *
import random
from animal import Animal

class Frog(Animal):
    def __init__(self, img, pos):
        super().__init__(img, pos)
    
    def show(self):
        super().show()

    def movement(self, time):
        super().movement(time, 10)
        
    def collision_screen(self):
        super().collision_screen()