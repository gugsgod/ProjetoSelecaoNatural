import pygame
from pygame.locals import *
from character import Character
from fade_in import FadeIn
from crab import Crab
from quiz import Quiz
from text_format import *
from database import Database
from login import Login
import mysql.connector

class Level2:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        #Background level 2
        self.bg_level2 = pygame.image.load('images/backgrounds/bg_level2.png').convert_alpha()

        #Banco de dados
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "gustavoimt123")
        
        self.db = Database()
        
        p9 = self.db.get_questions(self.mydb, 9)
        p10 = self.db.get_questions(self.mydb, 10)
        p11 = self.db.get_questions(self.mydb, 11)
        p12 = self.db.get_questions(self.mydb, 12)
        p13 = self.db.get_questions(self.mydb, 13)
        p14 = self.db.get_questions(self.mydb, 14)
        p15 = self.db.get_questions(self.mydb, 15)
        p16 = self.db.get_questions(self.mydb, 16)
        p17 = self.db.get_questions(self.mydb, 17)
        p18 = self.db.get_questions(self.mydb, 18)
        
        
        self.login = Login()
        self.user = self.login.get_user()
        
        self.score = 0

        #Objeto Character
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [0, 270], 0)

        #Objetos Carangueijo
        self.crab_1 = Crab('images/animals/crab.png', [80, 140])
        self.crab_2 = Crab('images/animals/crab.png', [200, 50])
        self.crab_3 = Crab('images/animals/crab.png', [1360, 830])

        #Atributos Placa
        self.plate9_pos = (525, 310)
        self.plate10_pos = (430, 5)
        self.plate11_pos = (840, 80)
        self.plate12_pos = (735, 685)
        self.plate13_pos = (70, 585)
        self.plate14_pos = (170, 950)
        self.plate15_pos = (1160, 850)
        self.plate16_pos = (1060, 90)
        self.plate17_pos = (1680, 180)
        self.plate18_pos = (1575, 915)
        self.plate_end_pos = (1810, 815)
        
        #Placas LOAD
        self.plate9 = pygame.image.load("images/plates/plate_9.png")
        self.plate10 = pygame.image.load("images/plates/plate_10.png")
        self.plate11 = pygame.image.load("images/plates/plate_11.png")
        self.plate12 = pygame.image.load("images/plates/plate_12.png")
        self.plate13 = pygame.image.load("images/plates/plate_13.png")
        self.plate14 = pygame.image.load("images/plates/plate_14.png")
        self.plate15 = pygame.image.load("images/plates/plate_15.png")
        self.plate16 = pygame.image.load("images/plates/plate_16.png")
        self.plate17 = pygame.image.load("images/plates/plate_17.png")
        self.plate18 = pygame.image.load("images/plates/plate_18.png")
        self.plate_end = pygame.image.load("images/plates/plate_end.png")

        self.plate_right = pygame.image.load("images/plates/plate_right.png")
        self.plate_wrong = pygame.image.load("images/plates/plate_wrong.png")

        #Pergunta e alternativas q9
        self.pergunta9 = TextFormat.format_question(p9[1])
        self.q9_alt1 = TextFormat.format_text(p9[2])
        self.q9_alt2 = TextFormat.format_text(p9[3])
        self.q9_alt3 = TextFormat.format_text(p9[4])
        self.q9_alt4 = TextFormat.format_text(p9[5])
        
        #Pergunta e alternativas q10
        self.pergunta10 = TextFormat.format_question(p10[1])
        self.q10_alt1 = TextFormat.format_text(p10[2])
        self.q10_alt2 = TextFormat.format_text(p10[3])
        self.q10_alt3 = TextFormat.format_text(p10[4])
        self.q10_alt4 = TextFormat.format_text(p10[5])
        
        #Pergunta e alternativas q11
        self.pergunta11 = TextFormat.format_question(p11[1])
        self.q11_alt1 = TextFormat.format_text(p11[2])
        self.q11_alt2 = TextFormat.format_text(p11[3])
        self.q11_alt3 = TextFormat.format_text(p11[4])
        self.q11_alt4 = TextFormat.format_text(p11[5])
        
        #Pegunta e alternativas q12
        self.pergunta12 = TextFormat.format_question(p12[1])
        self.q12_alt1 = TextFormat.format_text(p12[2])
        self.q12_alt2 = TextFormat.format_text(p12[3])
        self.q12_alt3 = TextFormat.format_text(p12[4])
        self.q12_alt4 = TextFormat.format_text(p12[5])
        
        #Pegunta e alternativas q13
        self.pergunta13 = TextFormat.format_question(p13[1])
        self.q13_alt1 = TextFormat.format_text(p13[2])
        self.q13_alt2 = TextFormat.format_text(p13[3])
        self.q13_alt3 = TextFormat.format_text(p13[4])
        self.q13_alt4 = TextFormat.format_text(p13[5])
        
        #Pegunta e alternativas q14
        self.pergunta14 = TextFormat.format_question(p14[1])
        self.q14_alt1 = TextFormat.format_text(p14[2])
        self.q14_alt2 = TextFormat.format_text(p14[3])
        self.q14_alt3 = TextFormat.format_text(p14[4])
        self.q14_alt4 = TextFormat.format_text(p14[5])
        
        #Pegunta e alternativas q15
        self.pergunta15 = TextFormat.format_question(p15[1])
        self.q15_alt1 = TextFormat.format_text(p15[2])
        self.q15_alt2 = TextFormat.format_text(p15[3])
        self.q15_alt3 = TextFormat.format_text(p15[4])
        self.q15_alt4 = TextFormat.format_text(p15[5])
        
        #Pegunta e alternativas q16
        self.pergunta16 = TextFormat.format_question(p16[1])
        self.q16_alt1 = TextFormat.format_text(p16[2])
        self.q16_alt2 = TextFormat.format_text(p16[3])
        self.q16_alt3 = TextFormat.format_text(p16[4])
        self.q16_alt4 = TextFormat.format_text(p16[5])

        #Pegunta e alternativas q17
        self.pergunta17 = TextFormat.format_question(p17[1])
        self.q17_alt1 = TextFormat.format_text(p17[2])
        self.q17_alt2 = TextFormat.format_text(p17[3])
        self.q17_alt3 = TextFormat.format_text(p17[4])
        self.q17_alt4 = TextFormat.format_text(p17[5])

        #Pegunta e alternativas q18
        self.pergunta18 = TextFormat.format_question(p18[1])
        self.q18_alt1 = TextFormat.format_text(p18[2])
        self.q18_alt2 = TextFormat.format_text(p18[3])
        self.q18_alt3 = TextFormat.format_text(p18[4])
        self.q18_alt4 = TextFormat.format_text(p18[5])

        #Objeto Quiz 9
        self.quiz_9 = Quiz(self.pergunta9, self.q9_alt1, self.q9_alt2, self.q9_alt3, self.q9_alt4)
        
        #Objeto Quiz 10
        self.quiz_10 = Quiz(self.pergunta10, self.q10_alt1, self.q10_alt2, self.q10_alt3, self.q10_alt4)
        
        #Objeto Quiz 11
        self.quiz_11 = Quiz(self.pergunta11, self.q11_alt1, self.q11_alt2, self.q11_alt3, self.q11_alt4)
        
        #Objeto Quiz 12
        self.quiz_12 = Quiz(self.pergunta12, self.q12_alt1, self.q12_alt2, self.q12_alt3, self.q12_alt4)
        
        #Objeto Quiz 13
        self.quiz_13 = Quiz(self.pergunta13, self.q13_alt1, self.q13_alt2, self.q13_alt3, self.q13_alt4)
        
        #Objeto Quiz 14
        self.quiz_14 = Quiz(self.pergunta14, self.q14_alt1, self.q14_alt2, self.q14_alt3, self.q14_alt4)
        
        #Objeto Quiz 15
        self.quiz_15 = Quiz(self.pergunta15, self.q15_alt1, self.q15_alt2, self.q15_alt3, self.q15_alt4)    

        #Objeto Quiz 16
        self.quiz_16 = Quiz(self.pergunta16, self.q16_alt1, self.q16_alt2, self.q16_alt3, self.q16_alt4)
        
        #Objeto Quiz 17
        self.quiz_17 = Quiz(self.pergunta17, self.q17_alt1, self.q17_alt2, self.q17_alt3, self.q17_alt4)

        #Objeto Quiz 18
        self.quiz_18 = Quiz(self.pergunta18, self.q18_alt1, self.q18_alt2, self.q18_alt3, self.q18_alt4)
    
        #Fase atual
        self.status = 'level2'

        #Status de resposta da questão
        self.status_quiz9 = None
        self.status_quiz10 = None
        self.status_quiz11 = None
        self.status_quiz12 = None
        self.status_quiz13 = None
        self.status_quiz14 = None
        self.status_quiz15 = None
        self.status_quiz16 = None
        self.status_quiz17 = None
        self.status_quiz18 = None

        #Bloqueio das plates com base na conclusão dos quizes
        self.quiz9_complete = False
        self.quiz10_complete = False
        self.quiz11_complete = False
        self.quiz12_complete = False
        self.quiz13_complete = False
        self.quiz14_complete = False
        self.quiz15_complete = False
        self.quiz16_complete = False
        self.quiz17_complete = False
        self.quiz18_complete = False

    def run(self):
        self.clock.tick(14)
        
        if self.status == 'level2':
            self.screen.blit(self.bg_level2, (0,0))
           
            
            #Funções do Carangueijo 1
            self.crab_1.show()
            self.crab_1.movement(10)
            self.crab_1.collision_screen()

            #Funções do Carangueijo 2
            self.crab_2.show()
            self.crab_2.movement(9)
            self.crab_2.collision_screen()

            #Funções do Carangueijo 3
            self.crab_3.show()
            self.crab_3.movement(11)
            self.crab_3.collision_screen()

            #Blit placas
            self.screen.blit(self.plate9, self.plate9_pos)
            self.screen.blit(self.plate10, self.plate10_pos)
            self.screen.blit(self.plate11, self.plate11_pos)
            self.screen.blit(self.plate12, self.plate12_pos)
            self.screen.blit(self.plate13, self.plate13_pos)
            self.screen.blit(self.plate14, self.plate14_pos)
            self.screen.blit(self.plate15, self.plate15_pos)
            self.screen.blit(self.plate16, self.plate16_pos)
            self.screen.blit(self.plate17, self.plate17_pos)
            self.screen.blit(self.plate18, self.plate18_pos)
            self.screen.blit(self.plate_end, self.plate_end_pos)
           
            #If's para mudar placas
            if self.status_quiz9 == True:
                self.plate9 = self.plate_right
            elif self.status_quiz9 == False:
                self.plate9 = self.plate_wrong
            
            if self.status_quiz10 == True:
                self.plate10 = self.plate_right
            elif self.status_quiz10 == False:
                self.plate10 = self.plate_wrong
                
            if self.status_quiz11 == True:
                self.plate11 = self.plate_right
            elif self.status_quiz11 == False:
                self.plate11 = self.plate_wrong
                
            if self.status_quiz12 == True:
                self.plate12 = self.plate_right
            elif self.status_quiz12 == False:
                self.plate12 = self.plate_wrong
                
            if self.status_quiz13 == True:
                self.plate13 = self.plate_right
            elif self.status_quiz13 == False:
                self.plate13 = self.plate_wrong
                
            if self.status_quiz14 == True:
                self.plate14 = self.plate_right
            elif self.status_quiz14 == False:
                self.plate14 = self.plate_wrong
            
            if self.status_quiz15 == True:
                self.plate15 = self.plate_right
            elif self.status_quiz15 == False:
                self.plate15 = self.plate_wrong

            if self.status_quiz16 == True:
                self.plate16 = self.plate_right
            elif self.status_quiz16 == False:
                self.plate16 = self.plate_wrong
            
            if self.status_quiz17 == True:
                self.plate17 = self.plate_right
            elif self.status_quiz17 == False:
                self.plate17 = self.plate_wrong

            if self.status_quiz18 == True:
                self.plate18 = self.plate_right
            elif self.status_quiz18 == False:
                self.plate18 = self.plate_wrong
           
            #Funções do Personagem
            self.character.show()
            self.character.skin()
            self.character.animation()
            self.character.movement()
            self.character.collision_screen()

            if self.character.collision_plate('quiz_9', self.plate9_pos) == 'quiz_9':
                if self.quiz9_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([400, 270])
                    self.status = 'quiz_9'
        
            if self.character.collision_plate('quiz_10', self.plate10_pos) == 'quiz_10':
                if self.quiz10_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([400, 60])
                    self.status = 'quiz_10'
                    
            if self.character.collision_plate('quiz_11', self.plate11_pos) == 'quiz_11':
                if self.quiz11_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([720, 55])
                    self.status = 'quiz_11'
        
            if self.character.collision_plate('quiz_12', self.plate12_pos) == 'quiz_12':
                if self.quiz12_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([720, 555])
                    self.status = 'quiz_12'

            if self.character.collision_plate('quiz_13', self.plate13_pos) == 'quiz_13':
                if self.quiz13_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([150, 555])
                    self.status = 'quiz_13'

            if self.character.collision_plate('quiz_14', self.plate14_pos) == 'quiz_14':
                if self.quiz14_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([155, 800])
                    self.status = 'quiz_14'
                
            if self.character.collision_plate('quiz_15', self.plate15_pos) == 'quiz_15':
                if self.quiz15_complete == False:
                     #Onde o player sai depois do quiz
                    self.character.pos([1040, 800])
                    self.status = 'quiz_15'
            
            if self.character.collision_plate('quiz_16', self.plate16_pos) == 'quiz_16':
                if self.quiz16_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([1040, 140])
                    self.status = 'quiz_16'

            if self.character.collision_plate('quiz_17', self.plate17_pos) == 'quiz_17':
                if self.quiz17_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([1550, 140])
                    self.status = 'quiz_17'

            if self.character.collision_plate('quiz_18', self.plate18_pos) == 'quiz_18':
                if self.quiz18_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([1550, 765])
                    self.status = 'quiz_18'

            if self.quiz9_complete and self.quiz10_complete and self.quiz11_complete and self.quiz12_complete and self.quiz13_complete and self.quiz14_complete and self.quiz15_complete and self.quiz16_complete and self.quiz17_complete and self.quiz18_complete == True:
                if self.character.collision_plate('end', self.plate_end_pos) == 'end':
                    return 'score'
            
        if self.status == 'quiz_9':
            if self.status_quiz9 == None:
                self.quiz_9.show()
                self.quiz_9.discover_alt_correct()
                self.status_quiz9 = self.quiz_9.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz9 == True:
                self.quiz_9.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz9 = True
                        self.quiz9_complete = True
            if self.status_quiz9 == False:
                self.quiz_9.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz9 = False
                        self.quiz9_complete = True
        
        if self.status == 'quiz_10':
            if self.status_quiz10 == None:
                self.quiz_10.show()
                self.quiz_10.discover_alt_correct()
                self.status_quiz10 = self.quiz_10.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz10 == True:
                self.quiz_10.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz10 = True
                        self.quiz10_complete = True
            if self.status_quiz10 == False:
                self.quiz_10.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz10 = False
                        self.quiz10_complete = True
        
        if self.status == 'quiz_11':
            if self.status_quiz11 == None:
                self.quiz_11.show()
                self.quiz_11.discover_alt_correct()
                self.status_quiz11 = self.quiz_11.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz11 == True:
                self.quiz_11.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz11 = True
                        self.quiz11_complete = True
            if self.status_quiz11 == False:
                self.quiz_11.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz11 = False
                        self.quiz11_complete = True
        
        if self.status == 'quiz_12':
            if self.status_quiz12 == None:
                self.quiz_12.show()
                self.quiz_12.discover_alt_correct()
                self.status_quiz12 = self.quiz_12.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz12 == True:
                self.quiz_12.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz12 = True
                        self.quiz12_complete = True
            if self.status_quiz12 == False:
                self.quiz_12.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz12 = False
                        self.quiz12_complete = True
        
        if self.status == 'quiz_13':
            if self.status_quiz13 == None:
                self.quiz_13.show()
                self.quiz_13.discover_alt_correct()
                self.status_quiz13 = self.quiz_13.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz13 == True:
                self.quiz_13.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz13 = True
                        self.quiz13_complete = True
            if self.status_quiz13 == False:
                self.quiz_13.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz13 = False
                        self.quiz13_complete = True
        
        if self.status == 'quiz_14':
            if self.status_quiz14 == None:
                self.quiz_14.show()
                self.quiz_14.discover_alt_correct()
                self.status_quiz14 = self.quiz_14.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz14 == True:
                self.quiz_14.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz14 = True
                        self.quiz14_complete = True
            if self.status_quiz14 == False:
                self.quiz_14.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz14 = False
                        self.quiz14_complete = True
        
        if self.status == 'quiz_15':
            if self.status_quiz15 == None:
                self.quiz_15.show()
                self.quiz_15.discover_alt_correct()
                self.status_quiz15 = self.quiz_15.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz15 == True:
                self.quiz_15.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz15 = True
                        self.quiz15_complete = True
            if self.status_quiz15 == False:
                self.quiz_15.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz15 = False
                        self.quiz15_complete = True
        
        if self.status == 'quiz_16':
            if self.status_quiz16 == None:
                self.quiz_16.show()
                self.quiz_16.discover_alt_correct()
                self.status_quiz16 = self.quiz_16.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz16 == True:
                self.quiz_16.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz16 = True
                        self.quiz16_complete = True
            if self.status_quiz16 == False:
                self.quiz_16.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz16 = False
                        self.quiz16_complete = True
        
        if self.status == 'quiz_17':
            if self.status_quiz17 == None:
                self.quiz_17.show()
                self.quiz_17.discover_alt_correct()
                self.status_quiz17 = self.quiz_17.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz17 == True:
                self.quiz_17.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz17 = True
                        self.quiz17_complete = True
            if self.status_quiz17 == False:
                self.quiz_17.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz17 = False
                        self.quiz17_complete = True
        if self.status == 'quiz_18':
            if self.status_quiz18 == None:
                self.quiz_18.show()
                self.quiz_18.discover_alt_correct()
                self.status_quiz18 = self.quiz_18.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
            if self.status_quiz18 == True:
                self.quiz_18.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.score += 1
                        self.status_quiz18 = True
                        self.quiz18_complete = True
            if self.status_quiz18 == False:
                self.quiz_18.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level2'
                        self.status_quiz18 = False
                        self.quiz18_complete = True
        
    def get_score(self):
        return self.score