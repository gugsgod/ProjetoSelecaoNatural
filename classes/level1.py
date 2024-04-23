import pygame
from pygame.locals import *
import sys
import random
from character import Character
from fade_in import FadeIn
from frog import Frog
from quiz import Quiz

class Level1:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.character = Character('images/Scientists.png', 0, 0, [75, 60], [10,110], 0)
        self.frog_1 = Frog('images/frog.png', [500, 100])
        self.frog_2 = Frog('images/frog.png', [100, 700])
        self.frog_3 = Frog('images/frog.png', [800, 300])
        self.frog_4 = Frog('images/frog.png', [1400, 200])
        self.frog_5 = Frog('images/frog.png', [1700, 900])
        self.quiz_1 = Quiz(' Por que alguns insetos parecem folhas ou ramos de plantas?', '       E como isso os ajuda a escapar dos seus predadores?',
                           ['  Essa semelhança é resultado de mutações', 'aleatórias que foram selecionadas ao longo', '   do tempo devido à pressão seletiva dos',  '                         predadores'],
                           [' Os insetos desenvolveram essa semelhança', '  para atrair mais facilmente suas presas', '', ''],
                           [' Os insetos adotam essa camuflagem para se', '     protegerem das mudanças climáticas', '', ''],
                           ['  A semelhança com folhas e ramos permite', '    que os insetos se comuniquem de forma', '                   eficiente entre si', ''])
        self.bg_play = pygame.image.load('images/bg_game.png').convert_alpha()
        self.status = 'level1'
    
    def run(self):
        self.clock.tick(14)
        
        if self.status == 'level1':
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
            self.character.collision_screen()
            
            self.quiz_1.shuffle_alt()
            
            if self.character.collision_plate('quiz_1', [270, 105], [44, 50]) == 'quiz_1':
                self.character.pos([150, 125])
                self.status = 'quiz_1'
            else:       
                pygame.draw.rect(self.screen, (0, 50, 155), pygame.Rect(270, 105, 44, 50))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
            
        if self.status == 'quiz_1':
            self.quiz_1.centralize_y()
            self.quiz_1.show()
            self.quiz_1.discover_alt_correct()
            if self.quiz_1.click() == 'level1':
                self.status = 'level1'


                
        