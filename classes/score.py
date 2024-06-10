import pygame
from pygame.locals import *
from character import Character
from text import Text
from text_format import *
from database import Database
from login import Login
from level1 import Level1
from level2 import Level2
import mysql.connector

class Score:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        
        #Background score
        self.bg_score = pygame.image.load('images/backgrounds/bg_score.png').convert_alpha()
        
        #Fonte
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 80)

        #Objetos levels
        self.level1 = Level1()
        self.level2 = Level2()

        #Objetos text
        self.score_text = Text('', self.font, 'BLACK', 1920/2 - 4/2, 300)
        
        #Database
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "gustavoimt123")
        self.db = Database()
        
        #Objeto Login
        self.login = Login()

    def run(self):
        self.screen.blit(self.bg_score, (0,0))
        score_total = self.level1.get_score() + self.level2.get_score()
        self.score_text.show_update(str(score_total))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                self.db.insert_points(self.mydb, self.score_total, self.db.get_id(self.mydb, self.login.get_user()))
                return 'menu'

