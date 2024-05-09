import pygame
from pygame.locals import *
import sys
import random
from character import Character
from fade_in import FadeIn
from frog import Frog
from quiz import Quiz
from transform_text import *

class Level1:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        #Objeto Character
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [10,110], 0)
        
        #Objetos Sapo
        self.frog_1 = Frog('images/animals/frog.png', [500, 100])
        self.frog_2 = Frog('images/animals/frog.png', [100, 700])
        self.frog_3 = Frog('images/animals/frog.png', [800, 300])
        self.frog_4 = Frog('images/animals/frog.png', [1400, 200])
        self.frog_5 = Frog('images/animals/frog.png', [1700, 900])
        
        #Placas LOAD
        self.placa1 = pygame.image.load("images/placas/placa_1.png")
        self.placa2 = pygame.image.load("images/placas/placa_2.png")
        self.placa3 = pygame.image.load("images/placas/placa_3.png")
        self.placa4 = pygame.image.load("images/placas/placa_4.png")
        self.placa5 = pygame.image.load("images/placas/placa_5.png")
        self.placa6 = pygame.image.load("images/placas/placa_6.png")
        self.placa7 = pygame.image.load("images/placas/placa_7.png")
        self.placa8 = pygame.image.load("images/placas/placa_8.png")
        self.placa9 = pygame.image.load("images/placas/placa_9.png")
        #self.placa10 = pygame.image.load()
        
        #Pergunta e alternativas Q1
        self.pergunta1 = 'Por que alguns insetos parecem folhas ou ramos de plantas? E como isso os ajuda a escapar dos seus predadores?'
        self.Q1_alt1 = TextFormat.FormatText('Essa semelhança é resultado de mutações aleatórias que foram selecionadas ao longo do tempo devido à pressão seletiva dos predadores')
        self.Q1_alt2 = TextFormat.FormatText('Os insetos desenvolveram essa semelhança para atrair mais facilmente suas presas')
        self.Q1_alt3 = TextFormat.FormatText('Os insetos adotam essa camuflagem para se protegerem das mudanças climáticas')
        self.Q1_alt4 = TextFormat.FormatText('A semelhança com folhas e ramos permite que os insetos se comuniquem de forma eficiente entre si')
        
        #Pergunta e alternativas Q2
        self.pergunta2 = None
        self.Q2_alt1 = None
        self.Q2_alt2 = None
        self.Q2_alt3 = None
        self.Q2_alt4 = None
        
        #Pergunta e alternativas Q3
        self.pergunta3 = None
        self.Q3_alt1 = None
        self.Q3_alt2 = None
        self.Q3_alt3 = None
        self.Q3_alt4 = None
        
        #Pegunta e alternativas Q4
        self.pergunta4 = None
        self.Q4_alt1 = None
        self.Q4_alt2 = None
        self.Q4_alt3 = None
        self.Q4_alt4 = None
        
        #Pegunta e alternativas Q5
        self.pergunta5 = None
        self.Q5_alt1 = None
        self.Q5_alt2 = None
        self.Q5_alt3 = None
        self.Q5_alt4 = None
        
        #Pegunta e alternativas Q6
        self.pergunta6 = None
        self.Q6_alt1 = None
        self.Q6_alt2 = None
        self.Q6_alt3 = None
        self.Q6_alt4 = None
        
        #Pegunta e alternativas Q7
        self.pergunta7 = None
        self.Q7_alt1 = None
        self.Q7_alt2 = None
        self.Q7_alt3 = None
        self.Q7_alt4 = None
        
        #Pegunta e alternativas Q8
        self.pergunta8 = None
        self.Q8_alt1 = None
        self.Q8_alt2 = None
        self.Q8_alt3 = None
        self.Q8_alt4 = None
        
        #Pegunta e alternativas Q9
        self.pergunta9 = None
        self.Q9_alt1 = None
        self.Q9_alt2 = None
        self.Q9_alt3 = None
        self.Q9_alt4 = None
        
        #Pegunta e alternativas Q10
        self.pergunta10 = None
        self.Q10_alt1 = None
        self.Q10_alt2 = None
        self.Q10_alt3 = None
        self.Q10_alt4 = None
        
        #Objeto Quiz 1
        self.quiz_1 = Quiz(self.pergunta1, self.Q1_alt1, self.Q1_alt2, self.Q1_alt3, self.Q1_alt4)
        
        #Objeto Quiz 2
        self.quiz_2 = Quiz(self.pergunta2, self.Q2_alt1, self.Q2_alt2, self.Q2_alt3, self.Q2_alt4)
        
        #Objeto Quiz 3
        self.quiz_3 = Quiz(self.pergunta3, self.Q3_alt1, self.Q3_alt2, self.Q3_alt3, self.Q3_alt4)
        
        #Objeto Quiz 4
        self.quiz_4 = Quiz(self.pergunta4, self.Q4_alt1, self.Q4_alt2, self.Q4_alt3, self.Q4_alt4)
        
        #Objeto Quiz 5
        
        self.quiz_5 = Quiz(self.pergunta5, self.Q5_alt1, self.Q5_alt2, self.Q5_alt3, self.Q5_alt4)
        
        #Objeto Quiz 6
        
        self.quiz_6 = Quiz(self.pergunta6, self.Q6_alt1, self.Q6_alt2, self.Q6_alt3, self.Q6_alt4)
        
        #Objeto Quiz 7
        
        self.quiz_7 = Quiz(self.pergunta7, self.Q7_alt1, self.Q7_alt2, self.Q7_alt3, self.Q7_alt4)    

        #Objeto Quiz 8
        
        self.quiz_8 = Quiz(self.pergunta8, self.Q8_alt1, self.Q8_alt2, self.Q8_alt3, self.Q8_alt4)
        
        #Objeto Quiz 9
        
        self.quiz_9 = Quiz(self.pergunta9, self.Q9_alt1, self.Q9_alt2, self.Q9_alt3, self.Q9_alt4)
        
        #Objeto Quiz 10
        
        self.quiz_10 = Quiz(self.pergunta10, self.Q10_alt1, self.Q10_alt2, self.Q10_alt3, self.Q10_alt4)
        
        #Backgroun level 1
        self.bg_play = pygame.image.load('images/backgrounds/bg_game.png').convert_alpha()
        
        #Fase atual
        self.status = 'level1'
        
        #Status de resposta da questão
        self.status_quiz1 = None
        self.status_quiz2 = None
        self.status_quiz3 = None
        self.status_quiz4 = None
        self.status_quiz5 = None
        self.status_quiz6 = None
        self.status_quiz7 = None
        self.status_quiz8 = None
        self.status_quiz9 = None
        self.status_quiz10 = None
        
        #Bloqueio das placas com base na conclusão dos quizes
        self.quiz1_complete = False
        self.quiz2_complete = False
        self.quiz3_complete = False
        self.quiz4_complete = False
        self.quiz5_complete = False
        self.quiz6_complete = False
        self.quiz7_complete = False
        self.quiz8_complete = False
        self.quiz9_complete = False
        self.quiz10_complete = False


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
                    
            #Blit placas
            self.screen.blit(self.placa1, (270,105))
            self.screen.blit(self.placa2, (180,470))
            
            
            #Character Módulos
            self.character.show()
            self.character.skin()
            self.character.animation()
            self.character.movement()
            self.character.collision_screen()
            
            if self.character.collision_plate('quiz_1', [270, 105], [44, 50]) == 'quiz_1':
                if self.quiz1_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([150, 60])
                    self.status = 'quiz_1'
            # else:       
            #     pygame.draw.rect(self.screen, (0, 50, 155), pygame.Rect(270, 105, 44, 50))
                

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
            

        if self.status == 'quiz_1':
            if self.status_quiz1 == None:
                self.quiz_1.show()
                self.quiz_1.discover_alt_correct()
                self.status_quiz1 = self.quiz_1.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz1 == True:
                self.quiz_1.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.quiz1_complete = True
            if self.status_quiz1 == False:
                self.quiz_1.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz1 = None
                        self.quiz1_complete = False
                        
        if self.status == 'quiz_2':
            if self.status_quiz2 == None:
                self.quiz_2.show()
                self.quiz_2.discover_alt_correct()
                self.status_quiz2 = self.quiz_2.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz2 == True:
                self.quiz_2.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.quiz2_complete = True
            if self.status_quiz2 == False:
                self.quiz_2.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz2 = None
                        self.quiz2_complete = False