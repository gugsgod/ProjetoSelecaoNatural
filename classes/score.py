import pygame
from pygame.locals import *
from character import Character
from text import Text
from text_format import *
from database import Database
from login import Login
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

        
        #Objetos text
        self.score_text = Text('', self.font, 'BLACK', 1920/2 - 4/2, 300)
        self.pontuation_text = Text('Sua Pontuação É:', self.font, 'BLACK', 800, 220)
        
        #Database
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "gustavoimt123")
        self.db = Database()
        self.score_total = 0
        
        #Objeto Login
        self.login = Login()
    
    def run(self, score_level1, score_level2, user):
        score = score_level1 + score_level2
        self.screen.blit(self.bg_score, (0,0))
        self.score_text.show_update(str(score))
        self.pontuation_text.show()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                self.db.insert_points(self.mydb, score, user)
                return 'menu'