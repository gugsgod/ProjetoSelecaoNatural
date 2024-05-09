import pygame
from pygame.locals import *
import sys
import random
from character import Character
from fade_in import FadeIn
from frog import Frog
from quiz import Quiz
from classes.transform_text import *

class Level1:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        self.bg_acerto_certo = pygame.image.load('images/backgrounds/bg_acerto_certo.png').convert_alpha()
        self.bg_acerto_errado = pygame.image.load('images/backgrounds/bg_acerto_errado.png').convert_alpha()
        #Objeto Character
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [10,110], 0)
        
        #Objetos Sapo
        self.frog_1 = Frog('images/animals/frog.png', [500, 100])
        self.frog_2 = Frog('images/animals/frog.png', [100, 700])
        self.frog_3 = Frog('images/animals/frog.png', [800, 300])
        self.frog_4 = Frog('images/animals/frog.png', [1400, 200])
        self.frog_5 = Frog('images/animals/frog.png', [1700, 900])
        
        #Alternativas
        self.alt1 = TextFormat.FormatText('Essa semelhança é resultado de mutações aleatórias que foram selecionadas ao longo do tempo devido à pressão seletiva dos predadores')
        self.alt2 = TextFormat.FormatText('Os insetos desenvolveram essa semelhança para atrair mais facilmente suas presas')
        self.alt3 = TextFormat.FormatText('Os insetos adotam essa camuflagem para se protegerem das mudanças climáticas')
        self.alt4 = TextFormat.FormatText('A semelhança com folhas e ramos permite que os insetos se comuniquem de forma eficiente entre si')
        #Objeto Quiz
        self.quiz_1 = Quiz('Por que alguns insetos parecem folhas ou ramos de plantas? E como isso os ajuda a escapar dos seus predadores?',
                           self.alt1,
                           self.alt2,
                           self.alt3,
                           self.alt4
                           )
        
        self.bg_play = pygame.image.load('images/backgrounds/bg_game.png').convert_alpha()
        self.status = 'level1'
    
    def run(self):
        self.clock.tick(14)
        
        if self.status == 'level1':
            self.screen.blit(self.bg_play, (0,0))
            
            #Sapo Spawn 1
            self.frog_1.show()
            self.frog_1.movement()
            self.frog_1.collision_screen()
            
            #Sapo Spawn 2    
            self.frog_2.show()
            self.frog_2.movement()
            self.frog_2.collision_screen()
            
            #Sapo Spawn 3
            self.frog_3.show()
            self.frog_3.movement()
            self.frog_3.collision_screen()

            #Sapo Spawn 4
            self.frog_4.show()
            self.frog_4.movement()
            self.frog_4.collision_screen()

            #Sapo Spawn 5
            self.frog_5.show()
            self.frog_5.movement()
            self.frog_5.collision_screen()
                    
            #Character Módulos
            self.character.show()
            self.character.skin()
            self.character.animation()
            self.character.movement()
            self.character.collision_screen()
            
            if self.character.collision_plate('quiz_1', [270, 105], [44, 50]) == 'quiz_1':
                self.character.pos([150, 125])
                self.status = 'quiz_1'
            else:       
                pygame.draw.rect(self.screen, (0, 50, 155), pygame.Rect(270, 105, 44, 50))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
            

        if self.status == 'quiz_1':
            self.quiz_1.show()
            self.quiz_1.discover_alt_correct()
            run = self.quiz_1.click()
            if run == True:
                self.quiz_1.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            elif run == False:
                self.quiz_1.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
