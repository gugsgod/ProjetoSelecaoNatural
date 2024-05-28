import pygame
from pygame.locals import *
import sys
import random
from character import Character
from fade_in import FadeIn
from frog import Frog
from butterfly import Butterfly
from quiz import Quiz
from text_format import *

class Level1:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        #Atributos Placa
        self.plate1_pos = (260, 100)
        self.plate2_pos = (170, 460)
        self.plate3_pos = (650, 360)
        self.plate4_pos = (560, 850)
        self.plate5_pos = (1030, 750)
        self.plate6_pos = (940 , 540)
        self.plate7_pos = (1450 , 620)
        self.plate8_pos = (1360 , 220)
        
        #Objeto Character
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [0, 50], 0)
        
        #Objetos Sapo
        self.frog_1 = Frog('images/animals/frog.png', [500, 100])
        self.frog_2 = Frog('images/animals/frog.png', [100, 700])
        self.frog_3 = Frog('images/animals/frog.png', [800, 300])
        self.frog_4 = Frog('images/animals/frog.png', [1400, 200])
        self.frog_5 = Frog('images/animals/frog.png', [1700, 900])
        
        #Objetos Borboleta
        self.butterfly1 = Butterfly('images/animals/butterfly.png', [600, 200])
        self.butterfly2 = Butterfly('images/animals/butterfly.png', [640, 200])
        self.butterfly3 = Butterfly('images/animals/butterfly.png', [600, 240])
        
        #Placas LOAD
        self.placa1 = pygame.image.load("images/plates/placa_1.png")
        self.placa2 = pygame.image.load("images/plates/placa_2.png")
        self.placa3 = pygame.image.load("images/plates/placa_3.png")
        self.placa4 = pygame.image.load("images/plates/placa_4.png")
        self.placa5 = pygame.image.load("images/plates/placa_5.png")
        self.placa6 = pygame.image.load("images/plates/placa_6.png")
        self.placa7 = pygame.image.load("images/plates/placa_7.png")
        self.placa8 = pygame.image.load("images/plates/placa_8.png")
        self.placa9 = pygame.image.load("images/plates/placa_9.png")
        #self.placa10 = pygame.image.load()
        
        self.placacorreto = pygame.image.load("images/plates/placa_certo.png")
        self.placaerrado = pygame.image.load("images/plates/placa_errada.png")
        
        #Pergunta e alternativas q1
        self.pergunta1 = TextFormat.format_question('Por que alguns insetos parecem folhas ou ramos de plantas? E como isso os ajuda a escapar dos seus predadores?')
        self.q1_alt1 = TextFormat.format_text('Essa semelhança é resultado de mutações aleatórias que foram selecionadas ao longo do tempo devido à pressão seletiva dos predadores')
        self.q1_alt2 = TextFormat.format_text('Os insetos desenvolveram essa semelhança para atrair mais facilmente suas presas')
        self.q1_alt3 = TextFormat.format_text('Os insetos adotam essa camuflagem para se protegerem das mudanças climáticas')
        self.q1_alt4 = TextFormat.format_text('A semelhança com folhas e ramos permite que os insetos se comuniquem de forma eficiente entre si')
        
        #Pergunta e alternativas q2
        
        self.pergunta2 = TextFormat.format_question("Porque os tentilhões possuem diferentes formas de bico aqui nas ilhas de Galápagos?")
        self.q2_alt1 = TextFormat.format_text("Sob pressões seletivas diferentes, as condições ambientais nas ilhas levaram à seleção de diferentes características nos tentilhões.")
        self.q2_alt2 = TextFormat.format_text("Os tentilhões fizeram cirurgias plásticas em seus bicos para se adaptarem.")
        self.q2_alt3 = TextFormat.format_text("Os tentilhões começaram a frequentar restaurantes diferentes na ilha, resultando em uma variedade de bicos.")
        self.q2_alt4 = TextFormat.format_text("Para evitar brigas por comida, os tentilhões desenvolveram bicos especializados em tipos diferentes de alimento.")
        
        #Pergunta e alternativas q3
        self.pergunta3 = None
        self.q3_alt1 = None
        self.q3_alt2 = None
        self.q3_alt3 = None
        self.q3_alt4 = None
        
        #Pegunta e alternativas q4
        self.pergunta4 = None
        self.q4_alt1 = None
        self.q4_alt2 = None
        self.q4_alt3 = None
        self.q4_alt4 = None
        
        #Pegunta e alternativas q5
        self.pergunta5 = None
        self.q5_alt1 = None
        self.q5_alt2 = None
        self.q5_alt3 = None
        self.q5_alt4 = None
        
        #Pegunta e alternativas q6
        self.pergunta6 = None
        self.q6_alt1 = None
        self.q6_alt2 = None
        self.q6_alt3 = None
        self.q6_alt4 = None
        
        #Pegunta e alternativas q7
        self.pergunta7 = None
        self.q7_alt1 = None
        self.q7_alt2 = None
        self.q7_alt3 = None
        self.q7_alt4 = None
        
        #Pegunta e alternativas q8
        self.pergunta8 = None
        self.q8_alt1 = None
        self.q8_alt2 = None
        self.q8_alt3 = None
        self.q8_alt4 = None
        
        #Pegunta e alternativas q9
        self.pergunta9 = None
        self.q9_alt1 = None
        self.q9_alt2 = None
        self.q9_alt3 = None
        self.q9_alt4 = None
        
        #Pegunta e alternativas q10
        self.pergunta10 = None
        self.q10_alt1 = None
        self.q10_alt2 = None
        self.q10_alt3 = None
        self.q10_alt4 = None
        
        #Objeto Quiz 1
        self.quiz_1 = Quiz(self.pergunta1, self.q1_alt1, self.q1_alt2, self.q1_alt3, self.q1_alt4)
        
        #Objeto Quiz 2
        self.quiz_2 = Quiz(self.pergunta2, self.q2_alt1, self.q2_alt2, self.q2_alt3, self.q2_alt4)
        
        #Objeto Quiz 3
        self.quiz_3 = Quiz(self.pergunta3, self.q3_alt1, self.q3_alt2, self.q3_alt3, self.q3_alt4)
        
        #Objeto Quiz 4
        self.quiz_4 = Quiz(self.pergunta4, self.q4_alt1, self.q4_alt2, self.q4_alt3, self.q4_alt4)
        
        #Objeto Quiz 5
        
        self.quiz_5 = Quiz(self.pergunta5, self.q5_alt1, self.q5_alt2, self.q5_alt3, self.q5_alt4)
        
        #Objeto Quiz 6
        
        self.quiz_6 = Quiz(self.pergunta6, self.q6_alt1, self.q6_alt2, self.q6_alt3, self.q6_alt4)
        
        #Objeto Quiz 7
        
        self.quiz_7 = Quiz(self.pergunta7, self.q7_alt1, self.q7_alt2, self.q7_alt3, self.q7_alt4)    

        #Objeto Quiz 8
        
        self.quiz_8 = Quiz(self.pergunta8, self.q8_alt1, self.q8_alt2, self.q8_alt3, self.q8_alt4)
        
        #Objeto Quiz 9
        
        self.quiz_9 = Quiz(self.pergunta9, self.q9_alt1, self.q9_alt2, self.q9_alt3, self.q9_alt4)
        
        #Objeto Quiz 10
        
        self.quiz_10 = Quiz(self.pergunta10, self.q10_alt1, self.q10_alt2, self.q10_alt3, self.q10_alt4)
        
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
            
            #Funções do Sapo 1
            self.frog_1.show()
            self.frog_1.movement(10)
            self.frog_1.collision_screen()
            
            #Funções do Sapo 2    
            self.frog_2.show()
            self.frog_2.movement(12)
            self.frog_2.collision_screen()
            
            #Funções do Sapo 3
            self.frog_3.show()
            self.frog_3.movement(8)
            self.frog_3.collision_screen()

            #Funções do Sapo 4
            self.frog_4.show()
            self.frog_4.movement(9)
            self.frog_4.collision_screen()

            #Funções do Sapo 5
            self.frog_5.show()
            self.frog_5.movement(13)
            self.frog_5.collision_screen()
            
            #Funções da Butterfly 1
            
            self.butterfly1.show()
            self.butterfly1.movement(100, 2)
            self.butterfly1.collision_screen()

            #Funções da Butterfly 2
            
            self.butterfly2.show()
            self.butterfly2.movement(90, 2)
            self.butterfly2.collision_screen()

            #Funções da Butterfly 3
            
            self.butterfly3.show()
            self.butterfly3.movement(100, 2)
            self.butterfly3.collision_screen()
            
            #Blit placas
            
            self.screen.blit(self.placa1, self.plate1_pos)
            self.screen.blit(self.placa2, self.plate2_pos)
            self.screen.blit(self.placa3, self.plate3_pos)
            self.screen.blit(self.placa4, self.plate4_pos)
            self.screen.blit(self.placa5, self.plate5_pos)
            self.screen.blit(self.placa6, self.plate6_pos)
            self.screen.blit(self.placa7, self.plate7_pos)
            self.screen.blit(self.placa8, self.plate8_pos)
            
            #If's para mudar placa
    
            if self.status_quiz1 == True:
                self.placa1 = self.placacorreto
            elif self.status_quiz1 == False:
                self.placa1 = self.placaerrado
            
            if self.status_quiz2 == True:
                self.placa2 = self.placacorreto
            elif self.status_quiz2 == False:
                self.placa2 = self.placaerrado
                
            if self.status_quiz3 == True:
                self.placa3 = self.placacorreto
            elif self.status_quiz3 == False:
                self.placa3 = self.placaerrado
                
            if self.status_quiz4 == True:
                self.placa4 = self.placacorreto
            elif self.status_quiz4 == False:
                self.placa4 = self.placaerrado
                
            if self.status_quiz5 == True:
                self.placa5 = self.placacorreto
            elif self.status_quiz5 == False:
                self.placa5 = self.placaerrado
                
            if self.status_quiz6 == True:
                self.placa6 = self.placacorreto
            elif self.status_quiz6 == False:
                self.placa6 = self.placaerrado
            
            #Funções do Personagem
            
            self.character.show()
            self.character.skin()
            self.character.animation()
            self.character.movement()
            self.character.collision_screen()
            
            if self.character.collision_plate('quiz_1', self.plate1_pos) == 'quiz_1':
                if self.quiz1_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([150, 60])
                    self.status = 'quiz_1'
            # else:       
            #     pygame.draw.rect(self.screen, (0, 50, 155), pygame.Rect(270, 105, 44, 50))
            if self.character.collision_plate('quiz_2', self.plate2_pos) == 'quiz_2':
                if self.quiz2_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([150, 330])
                    self.status = 'quiz_2'
                    
            if self.character.collision_plate('quiz_3', self.plate3_pos) == 'quiz_3':
                if self.quiz3_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([450, 330])
                    self.status = 'quiz_3'
        
            if self.character.collision_plate('quiz_4', self.plate4_pos) == 'quiz_4':
                    if self.quiz4_complete == False:
                        #Onde o player sai depois do quiz
                        self.character.pos([560, 800])
                        self.status = 'quiz_4'

            if self.character.collision_plate('quiz_5', self.plate5_pos) == 'quiz_5':
                    if self.quiz5_complete == False:
                        #Onde o player sai depois do quiz
                        self.character.pos([450, 330])
                        self.status = 'quiz_5'

            if self.character.collision_plate('quiz_6', self.plate6_pos) == 'quiz_6':
                    if self.quiz6_complete == False:
                        #Onde o player sai depois do quiz
                        self.character.pos([450, 330])
                        self.status = 'quiz_6'

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
                        self.status_quiz1 = True
                        self.quiz1_complete = True
            if self.status_quiz1 == False:
                self.quiz_1.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz1 = False
                        self.quiz1_complete = True
                        
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
                        self.status_quiz2 = True
                        self.quiz2_complete = True
            if self.status_quiz2 == False:
                self.quiz_2.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz2 = False
                        self.quiz2_complete = True
                        
        if self.status == 'quiz_3':
            if self.status_quiz3 == None:
                self.quiz_3.show()
                self.quiz_3.discover_alt_correct()
                self.status_quiz3 = self.quiz_3.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz3 == True:
                self.quiz_3.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz3 = True
                        self.quiz3_complete = True
            if self.status_quiz3 == False:
                self.quiz_3.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz3 = False
                        self.quiz3_complete = True
                        
        if self.status == 'quiz_4':
            if self.status_quiz4 == None:
                self.quiz_4.show()
                self.quiz_4.discover_alt_correct()
                self.status_quiz4 = self.quiz_4.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz4 == True:
                self.quiz_4.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz4 = True
                        self.quiz4_complete = True
            if self.status_quiz4 == False:
                self.quiz_4.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz4 = False
                        self.quiz4_complete = False
                        
        if self.status == 'quiz_5':
            if self.status_quiz5 == None:
                self.quiz_5.show()
                self.quiz_5.discover_alt_correct()
                self.status_quiz5 = self.quiz_5.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz5 == True:
                self.quiz_5.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz5 = True
                        self.quiz5_complete = True
            if self.status_quiz5 == False:
                self.quiz_5.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz5 = False
                        self.quiz5_complete = False
                        
        if self.status == 'quiz_6':
            if self.status_quiz6 == None:
                self.quiz_6.show()
                self.quiz_6.discover_alt_correct()
                self.status_quiz6 = self.quiz_6.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz6 == True:
                self.quiz_6.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz6 = True
                        self.quiz6_complete = True
            if self.status_quiz6 == False:
                self.quiz_6.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz6 = False
                        self.quiz6_complete = False