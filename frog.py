import pygame
from pygame.locals import *
import random

class Frog:
    def __init__(self,  frog_img, frog_pos):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.frog_img = frog_img
        self.frog_pos = frog_pos
        self.frog_random = [1, 2, 3, 4]
        self.time_frog = 0
    
    def show(self):
        self.screen.blit(self.frog_img, (self.frog_pos[0], self.frog_pos[1]))

    def movement(self):
        
        self.time_frog += 4
        if self.time_frog >100:
            self.time_frog = 0
        
        if self.time_frog == 100:
            random.shuffle(self.frog_random)
            if self.frog_random[0] == 1:
                self.frog_pos[0] += 10
            if self.frog_random[0] == 2:
                self.frog_pos[0] -= 10
            if self.frog_random[0] == 3:
                self.frog_pos[1] -= 10
            if self.frog_random[0] == 4:
                self.frog_pos[1] += 10
                
    
    def frog_collision_screen(self):
        if self.frog_pos[0] < 0:
            self.frog_pos[0] += 10
        if self.frog_pos[0] > 1890:
            self.frog_pos[0] -= 10
        if self.frog_pos[1] < 0:
            self.frog_pos[1] += 10
        if self.frog_pos[1] > 1070:
            self.frog_pos[1] -= 10