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
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [0, 50], 0)

        #Objetos Carangueijo
        self.crab_1 = Crab('images/animals/crab.png', [500, 100])
        self.crab_2 = Crab('images/animals/crab.png', [500, 100])
        self.crab_3 = Crab('images/animals/crab.png', [500, 100])

        #Atributos Placa
        self.plate9_pos = (260, 100)
        self.plate10_pos = (170, 460)
        self.plate11_pos = (650, 360)
        self.plate12_pos = (560, 850)
        self.plate13_pos = (1030, 750)
        self.plate14_pos = (940 , 540)
        self.plate15_pos = (1450 , 620)
        self.plate16_pos = (1360 , 220)
        self.plate17_pos = (1360 , 220)
        self.plate18_pos = (1360 , 220)
        
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