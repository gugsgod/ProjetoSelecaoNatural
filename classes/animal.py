import pygame
from pygame.locals import *
import random

class Animal:
    def __init__(self, img, pos):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.img = pygame.image.load(img).convert_alpha()
        self.pos = pos
        self.movement_random = [1, 2, 3, 4]
        self.movement_time = 0
    
    def show(self):
        self.screen.blit(self.img, (self.pos[0], self.pos[1]))

    def movement(self, time, dis):
        
        self.movement_time += time
        if self.movement_time >= 100:
            random.shuffle(self.movement_random)
            if self.movement_random[0] == 1:
                self.pos[0] += dis
            if self.movement_random[0] == 2:
                self.pos[0] -= dis
            if self.movement_random[0] == 3:
                self.pos[1] -= dis
            if self.movement_random[0] == 4:
                self.pos[1] += dis
        
        if self.movement_time >= 100:
            self.movement_time = 0
                
    
    def collision_screen(self):
        if self.pos[0] < 0:
            self.pos[0] += 10
        if self.pos[0] > 1890:
            self.pos[0] -= 10
        if self.pos[1] < 0:
            self.pos[1] += 10
        if self.pos[1] > 1070:
            self.pos[1] -= 10