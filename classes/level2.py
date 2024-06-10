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
        
        
        self.login = Login()
        self.user = self.login.get_user()
        
        self.score = 0

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
        
        #Objeto Character
        self.character = Character('images/player/Scientists.png', 0, 0, [75, 60], [0, 50], 0)
    
    def run(self):
        self.clock.tick(14)
        
        if self.status == 'level2':
            self.screen.blit(self.bg_level2, (0,0))
           
            #Funções do Carangueijo 1
            self.crab_1.show()
            self.crab_1.movement(10)
            self.crab_1.collision_screen()