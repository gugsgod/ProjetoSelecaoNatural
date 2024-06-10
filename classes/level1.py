import pygame
from pygame.locals import *
from character import Character
from fade_in import FadeIn
from frog import Frog
from butterfly import Butterfly
from quiz import Quiz
from text_format import *
from database import Database
from login import Login
import mysql.connector

class Level1:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        #Background level 1
        self.bg_level1 = pygame.image.load('images/backgrounds/bg_level1.png').convert_alpha()
        
        #Banco de dados
        self.mydb = mysql.connector.connect(host = "localhost", user = "root", password = "imtdb")
        
        self.db = Database()
        
        p1 = self.db.get_questions(self.mydb, 1)
        p2 = self.db.get_questions(self.mydb, 2)
        p3 = self.db.get_questions(self.mydb, 3)
        p4 = self.db.get_questions(self.mydb, 4)
        p5 = self.db.get_questions(self.mydb, 5)
        p6 = self.db.get_questions(self.mydb, 6)
        p7 = self.db.get_questions(self.mydb, 7)
        p8 = self.db.get_questions(self.mydb, 8)
        
        self.login = Login()
        self.user = self.login.get_user()
        
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
        self.butterfly4 = Butterfly('images/animals/butterfly.png', [900, 900])
        
        #Atributos placas
        self.plate1_pos = (260, 100)
        self.plate2_pos = (170, 460)
        self.plate3_pos = (650, 360)
        self.plate4_pos = (560, 850)
        self.plate5_pos = (1030, 750)
        self.plate6_pos = (940, 540)
        self.plate7_pos = (1450, 620)
        self.plate8_pos = (1360, 220)

        #Placas LOAD
        self.plate1 = pygame.image.load("images/plates/plate_1.png")
        self.plate2 = pygame.image.load("images/plates/plate_2.png")
        self.plate3 = pygame.image.load("images/plates/plate_3.png")
        self.plate4 = pygame.image.load("images/plates/plate_4.png")
        self.plate5 = pygame.image.load("images/plates/plate_5.png")
        self.plate6 = pygame.image.load("images/plates/plate_6.png")
        self.plate7 = pygame.image.load("images/plates/plate_7.png")
        self.plate8 = pygame.image.load("images/plates/plate_8.png")

        
        self.plate_right = pygame.image.load("images/plates/plate_right.png")
        self.plate_wrong = pygame.image.load("images/plates/plate_wrong.png")
        
        #Pergunta e alternativas q1
        self.pergunta1 = TextFormat.format_question(p1[1])
        self.q1_alt1 = TextFormat.format_text(p1[2])
        self.q1_alt2 = TextFormat.format_text(p1[3])
        self.q1_alt3 = TextFormat.format_text(p1[4])
        self.q1_alt4 = TextFormat.format_text(p1[5])
        
        #Pergunta e alternativas q2
        
        self.pergunta2 = TextFormat.format_question(p2[1])
        self.q2_alt1 = TextFormat.format_text(p2[2])
        self.q2_alt2 = TextFormat.format_text(p2[3])
        self.q2_alt3 = TextFormat.format_text(p2[4])
        self.q2_alt4 = TextFormat.format_text(p2[5])
        
        #Pergunta e alternativas q3
        self.pergunta3 = TextFormat.format_question(p3[1])
        self.q3_alt1 = TextFormat.format_text(p3[2])
        self.q3_alt2 = TextFormat.format_text(p3[3])
        self.q3_alt3 = TextFormat.format_text(p3[4])
        self.q3_alt4 = TextFormat.format_text(p3[5])
        
        #Pegunta e alternativas q4
        self.pergunta4 = TextFormat.format_question(p4[1])
        self.q4_alt1 = TextFormat.format_text(p4[2])
        self.q4_alt2 = TextFormat.format_text(p4[3])
        self.q4_alt3 = TextFormat.format_text(p4[4])
        self.q4_alt4 = TextFormat.format_text(p4[5])
        
        #Pegunta e alternativas q5
        self.pergunta5 = TextFormat.format_question(p5[1])
        self.q5_alt1 = TextFormat.format_text(p5[2])
        self.q5_alt2 = TextFormat.format_text(p5[3])
        self.q5_alt3 = TextFormat.format_text(p5[4])
        self.q5_alt4 = TextFormat.format_text(p5[5])
        
        #Pegunta e alternativas q6
        self.pergunta6 = TextFormat.format_question(p6[1])
        self.q6_alt1 = TextFormat.format_text(p6[2])
        self.q6_alt2 = TextFormat.format_text(p6[3])
        self.q6_alt3 = TextFormat.format_text(p6[4])
        self.q6_alt4 = TextFormat.format_text(p6[5])
        
        #Pegunta e alternativas q7
        self.pergunta7 = TextFormat.format_question(p7[1])
        self.q7_alt1 = TextFormat.format_text(p7[2])
        self.q7_alt2 = TextFormat.format_text(p7[3])
        self.q7_alt3 = TextFormat.format_text(p7[4])
        self.q7_alt4 = TextFormat.format_text(p7[5])
        
        #Pegunta e alternativas q8
        self.pergunta8 = TextFormat.format_question(p8[1])
        self.q8_alt1 = TextFormat.format_text(p8[2])
        self.q8_alt2 = TextFormat.format_text(p8[3])
        self.q8_alt3 = TextFormat.format_text(p8[4])
        self.q8_alt4 = TextFormat.format_text(p8[5])
        
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
        
        #Pontuação
        self.score = 0
        
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
        
        #Bloqueio das plates com base na conclusão dos quizes
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
            self.screen.blit(self.bg_level1, (0,0))
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

            #Funções da Butterfly 4
            self.butterfly4.show()
            self.butterfly4.movement(100, 2)
            self.butterfly4.collision_screen()
            
            #Blit placas
            self.screen.blit(self.plate1, self.plate1_pos)
            self.screen.blit(self.plate2, self.plate2_pos)
            self.screen.blit(self.plate3, self.plate3_pos)
            self.screen.blit(self.plate4, self.plate4_pos)
            self.screen.blit(self.plate5, self.plate5_pos)
            self.screen.blit(self.plate6, self.plate6_pos)
            self.screen.blit(self.plate7, self.plate7_pos)
            self.screen.blit(self.plate8, self.plate8_pos)
            
            #If's para mudar placas
            if self.status_quiz1 == True:
                self.plate1 = self.plate_right
            elif self.status_quiz1 == False:
                self.plate1 = self.plate_wrong
            
            if self.status_quiz2 == True:
                self.plate2 = self.plate_right
            elif self.status_quiz2 == False:
                self.plate2 = self.plate_wrong
                
            if self.status_quiz3 == True:
                self.plate3 = self.plate_right
            elif self.status_quiz3 == False:
                self.plate3 = self.plate_wrong
                
            if self.status_quiz4 == True:
                self.plate4 = self.plate_right
            elif self.status_quiz4 == False:
                self.plate4 = self.plate_wrong
                
            if self.status_quiz5 == True:
                self.plate5 = self.plate_right
            elif self.status_quiz5 == False:
                self.plate5 = self.plate_wrong
                
            if self.status_quiz6 == True:
                self.plate6 = self.plate_right
            elif self.status_quiz6 == False:
                self.plate6 = self.plate_wrong
            
            if self.status_quiz7 == True:
                self.plate7 = self.plate_right
            elif self.status_quiz7 == False:
                self.plate7 = self.plate_wrong

            if self.status_quiz8 == True:
                self.plate8 = self.plate_right
            elif self.status_quiz8 == False:
                self.plate8 = self.plate_wrong

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
                    self.character.pos([520, 330])
                    self.status = 'quiz_3'
        
            if self.character.collision_plate('quiz_4', self.plate4_pos) == 'quiz_4':
                if self.quiz4_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([530, 700])
                    self.status = 'quiz_4'

            if self.character.collision_plate('quiz_5', self.plate5_pos) == 'quiz_5':
                if self.quiz5_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([910, 700])
                    self.status = 'quiz_5'

            if self.character.collision_plate('quiz_6', self.plate6_pos) == 'quiz_6':
                if self.quiz6_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([910, 570])
                    self.status = 'quiz_6'
                
            if self.character.collision_plate('quiz_7', self.plate7_pos) == 'quiz_7':
                if self.quiz7_complete == False:
                     #Onde o player sai depois do quiz
                    self.character.pos([1330, 570])
                    self.status = 'quiz_7'
            
            if self.character.collision_plate('quiz_8', self.plate8_pos) == 'quiz_8':
                if self.quiz8_complete == False:
                    #Onde o player sai depois do quiz
                    self.character.pos([1340, 260])
                    self.status = 'quiz_8'

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
            
            if self.quiz1_complete == True and self.quiz2_complete == True and self.quiz3_complete == True and self.quiz4_complete == True and self.quiz5_complete == True and self.quiz6_complete == True and self.quiz7_complete == True and self.quiz8_complete == True:
                if self.character.collision_portal('level2', [1890, 270]) == 'level2':
                    return 'level2'

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
                        self.score += 1
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
                        self.score += 1
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
                        self.score += 1
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
                        self.score += 1
                        self.status_quiz4 = True
                        self.quiz4_complete = True
            if self.status_quiz4 == False:
                self.quiz_4.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz4 = False
                        self.quiz4_complete = True
                        
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
                        self.score += 1
                        self.status_quiz5 = True
                        self.quiz5_complete = True
            if self.status_quiz5 == False:
                self.quiz_5.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz5 = False
                        self.quiz5_complete = True
                        
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
                        self.score += 1
                        self.status_quiz6 = True
                        self.quiz6_complete = True
            if self.status_quiz6 == False:
                self.quiz_6.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz6 = False
                        self.quiz6_complete = True

        if self.status == 'quiz_7':
            if self.status_quiz7 == None:
                self.quiz_7.show()
                self.quiz_7.discover_alt_correct()
                self.status_quiz7 = self.quiz_7.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz7 == True:
                self.quiz_7.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.score += 1
                        self.status_quiz7 = True
                        self.quiz7_complete = True
            if self.status_quiz7 == False:
                self.quiz_7.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz7 = False
                        self.quiz7_complete = True
        
        if self.status == 'quiz_8':
            if self.status_quiz8 == None:
                self.quiz_8.show()
                self.quiz_8.discover_alt_correct()
                self.status_quiz8 = self.quiz_8.click()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
            if self.status_quiz8 == True:
                self.quiz_8.clicked_true()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.score += 1
                        self.status_quiz8 = True
                        self.quiz8_complete = True
            if self.status_quiz8 == False:
                self.quiz_8.clicked_false()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.status = 'level1'
                        self.status_quiz8 = False
                        self.quiz8_complete = True
    
    def get_score(self):
        return self.score
