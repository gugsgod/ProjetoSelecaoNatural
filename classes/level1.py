import pygame
from pygame.locals import *
import sys
import random
from character import Character
from fade_in import FadeIn
from frog import Frog


class Level1:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.character = Character('images/Scientists.png', 0, 0, [50, 40], [10,110], 0)
        self.frog_1 = Frog('images/frog.png', [500, 100])
        self.frog_2 = Frog('images/frog.png', [100, 700])
        self.frog_3 = Frog('images/frog.png', [800, 300])
        self.frog_4 = Frog('images/frog.png', [1400, 200])
        self.frog_5 = Frog('images/frog.png', [1700, 900])
        self.bg_play = pygame.image.load('images/bg_game.png').convert_alpha()
    
    
    def run(self):
        self.clock.tick(10)
        self.screen.blit(self.bg_play, (0,0))
               
        self.frog_1.show()
        self.frog_1.movement()
        self.frog_1.collision_screen()
               
        self.frog_2.show()
        self.frog_2.movement()
        self.frog_2.collision_screen()
        
        self.frog_3.show()
        self.frog_3.movement()
        self.frog_3.collision_screen()

        self.frog_4.show()
        self.frog_4.movement()
        self.frog_4.collision_screen()

        self.frog_5.show()
        self.frog_5.movement()
        self.frog_5.collision_screen()
                
        self.character.show()
        self.character.skin()
        self.character.animation()
        self.character.movement()
    

        if self.character.collision_plate('quiz', [270, 105], [44, 50]) == 'quiz':
            return 'quiz'
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                return 'menu'
                