import pygame
from pygame.locals import *
from text import Text
from ShowNoBotao import BotaoShow
import random

class Quiz:
    def __init__(self, question_1, alt1, alt2, alt3, alt4):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.quiz_bg = pygame.image.load('images/quiz_bg.png').convert_alpha()
        self.bg_acerto_certo = pygame.image.load('images/bg_acerto_certo.png').convert_alpha()
        self.bg_acerto_errado = pygame.image.load('images/bg_acerto_errado.png').convert_alpha()
        self.question_1 = question_1
        self.alt1 = alt1
        self.alt2 = alt2
        self.alt3 = alt3
        self.alt4 = alt4
        self.pos_question_1 = [160, 130]
        self.font_question = pygame.font.Font('fonts/upheavtt.ttf', 48)
        self.font_alt = pygame.font.Font('fonts/upheavtt.ttf', 25)
        self.text_question_1 = Text(self.question_1, self.font_question, 'BLACK', self.pos_question_1[0], self.pos_question_1[1])
        self.list_alternatives_random = [self.alt1, self.alt2, self.alt3, self.alt4]
        self.index_correct = None
        random.shuffle(self.list_alternatives_random)
        self.index_correct = self.list_alternatives_random.index(self.alt1)
                
        #Criação dos objeto da classe BotaoShow
        
        self.textBotao = BotaoShow(self.font_alt, 'BLACK')
        
        #Criação dos retângulos dos botões
        self.alt_rect1 = pygame.Rect(254, 370, 676, 294)
        self.alt_rect2 = pygame.Rect(254, 724, 676, 294)
        self.alt_rect3 = pygame.Rect(990, 370, 676, 294)
        self.alt_rect4 = pygame.Rect(990, 724, 676, 294)
        
        #Criação das superficies dos retângulos dos botões
        self.sup_bot1 = pygame.Surface((676, 294))
        self.sup_bot2 = pygame.Surface((676, 294))
        self.sup_bot3 = pygame.Surface((676, 294))
        self.sup_bot4 = pygame.Surface((676, 294))
        #Fill para checar posicionamento
        self.sup_bot1.fill('aqua')
        self.sup_bot2.fill('aqua')
        self.sup_bot3.fill('aqua')
        self.sup_bot4.fill('aqua')
        #Colorkey para deixar trasparente o fundo
        self.sup_bot1.set_colorkey('aqua')
        self.sup_bot2.set_colorkey('aqua')
        self.sup_bot3.set_colorkey('aqua')
        self.sup_bot4.set_colorkey('aqua')
        

    def show(self):
        self.screen.blit(self.quiz_bg, (0, 0))
        self.text_question_1.show()
        #Colocando a surface em cima do botão
        self.screen.blit(self.sup_bot1, (254, 370))
        self.screen.blit(self.sup_bot2, (254, 724))
        self.screen.blit(self.sup_bot3, (990, 370))
        self.screen.blit(self.sup_bot4, (990, 724))
        self.textBotao.showBotao(self.list_alternatives_random[0], self.sup_bot1)
        self.textBotao.showBotao(self.list_alternatives_random[1], self.sup_bot2)
        self.textBotao.showBotao(self.list_alternatives_random[2], self.sup_bot3)
        self.textBotao.showBotao(self.list_alternatives_random[3], self.sup_bot4)
        
        return self.index_correct

    def discover_alt_correct(self):
        if self.alt1 == self.list_alternatives_random[0]:
            self.alt_correct = self.alt_rect1
            self.alt_wrong = self.alt_rect2
            self.alt_wrong_1 = self.alt_rect3
            self.alt_wrong_2 = self.alt_rect4
        elif self.alt1 == self.list_alternatives_random[1]:
            self.alt_correct = self.alt_rect2
            self.alt_wrong = self.alt_rect1
            self.alt_wrong_1 = self.alt_rect3
            self.alt_wrong_2 = self.alt_rect4
        elif self.alt1 == self.list_alternatives_random[2]:
            self.alt_correct = self.alt_rect3
            self.alt_wrong = self.alt_rect2
            self.alt_wrong_1 = self.alt_rect1
            self.alt_wrong_2 = self.alt_rect4
        elif self.alt1 == self.list_alternatives_random[3]:
            self.alt_correct = self.alt_rect4
            self.alt_wrong = self.alt_rect2
            self.alt_wrong_1 = self.alt_rect3
            self.alt_wrong_2 = self.alt_rect1
    
    def click(self, i):       
        mouse = pygame.mouse.get_pos()
        if self.alt_correct.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                i = 1
                return True, i
        if self.alt_wrong.collidepoint(mouse) or self.alt_wrong_1.collidepoint(mouse) or self.alt_wrong_2.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                i = 2
                return True, i
        
    def clicked_true(self):
        self.screen.blit(self.bg_acerto_certo, (0, 0))
        
    def clicked_false(self):
        self.screen.blit(self.bg_acerto_errado, (0, 0))