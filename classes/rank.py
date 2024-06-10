import pygame
from pygame.locals import *
import mysql.connector
from input_box import InputBox
from text import Text
from database import Database

class Rank:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()

        #Rank Background
        self.rank_bg = pygame.image.load('images/backgrounds/digital-art-horizon-mountains-forest-pinkish.jpg')

        self.edge_user = pygame.image.load('images/buttons/edge_user.png')
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 80)
        self.pos_text_user = [425, 70]
        self.pos_rank = [600, 225]
        self.user_inputbox = InputBox(425, 150, 1070, 50)
        self.text_rank = Text('TOP 5 PONTUAÇÕES:', self.font, 'BLACK', self.pos_rank[0], self.pos_rank[1])
        self.text_user = Text('Digite o nome do usuário:', self.font, 'BLACK', self.pos_text_user[0], self.pos_text_user[1])
        
        #Database
        self.mydb = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "gustavoimt123")
        self.db = Database()
        self.score = []
        self.user_exist = False
        self.status_score = False
        self.user = ''
        self.nome = Text('', self.font, 'BLACK', 1920/2 - self.font.size(self.user)[0]/2, 300)
        self.top1 = Text('', self.font, 'BLACK', 880, 400)
        self.top2 = Text('', self.font, 'BLACK', 880, 500)
        self.top3 = Text('', self.font, 'BLACK', 880, 600)
        self.top4 = Text('', self.font, 'BLACK', 880, 700)
        self.top5 = Text('', self.font, 'BLACK', 880, 800)
        
        size_user_not_exist = self.font.size('Esse usuário não existe')
        self.error = Text('', self.font, 'BLACK', 1920/2 - size_user_not_exist[0]/2, 500)
    
    def run(self):
        self.clock.tick(30)
        self.screen.blit(self.rank_bg, (0,0))
        self.screen.blit(self.edge_user, (415, 140))
        
        for event in pygame.event.get():
            user = self.user_inputbox.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
            if event.type == pygame.KEYDOWN and event.key == K_RETURN:
                self.id = self.db.get_id(self.mydb, user)
                self.score = self.db.get_top_5(self.mydb, self.id)
                self.user = user
                if self.id == None:
                    self.user_exist = True
                else:
                    self.user_exist = False
        
        if self.user_exist == True:
            self.error.show_rank('Esse usuário não existe', '')
            
        if len(self.score) > 0:
            self.nome.show_nome(self.user)
            self.top1.show_rank(str(self.score[0][0]),'1 °. ')
            self.top2.show_rank(str(self.score[1][0]),'2°. ')
            self.top3.show_rank(str(self.score[2][0]),'3°. ')
            self.top4.show_rank(str(self.score[3][0]),'4°. ')
            self.top5.show_rank(str(self.score[4][0]),'5°. ')

        
        self.user_inputbox.draw(self.screen)
        self.text_user.show()
        self.text_rank.show()