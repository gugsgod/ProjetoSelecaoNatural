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
        self.alternatives = [self.alt1, self.alt2, self.alt3, self.alt4]
        self.pos_question_1 = [160, 130]
        self.font_question = pygame.font.Font('fonts/upheavtt.ttf', 48)
        self.font_alt = pygame.font.Font('fonts/upheavtt.ttf', 25)
        self.text_question_1 = Text(self.question_1, self.font_question, 'BLACK', self.pos_question_1[0], self.pos_question_1[1])
        
        #Criação dos objeto da classe BotaoShow
        
        textBotao = BotaoShow()
        
        #Criação das superfícies dos botões
        self.altRect1 = pygame.Rect(254, 370, 676, 294)
        self.altRect2 = pygame.Rect(254, 724, 676, 294)
        self.altRect3 = pygame.Rect(990, 370, 676, 294)
        self.altRect4 = pygame.Rect(990, 724, 676, 294)

    def show(self):
        self.screen.blit(self.quiz_bg, (0, 0))
        self.text_question_1.show()
        Text.showBotao(self.alt1, self.altRect1)
        Text.showBotao(self.alt2, self.altRect2)
        Text.showBotao(self.alt3, self.altRect3)
        Text.showBotao(self.alt4, self.altRect4)
        
    
    def shuffle_alt(self):
        random.shuffle(self.alternatives)

    def discover_alt_correct(self):
        if self.alt1 == self.alternatives[0]:
            self.alt_correct = self.alt_rect1
            self.alt_wrong_1 = self.alt_rect2
            self.alt_wrong_2 = self.alt_rect3
            self.alt_wrong_3 = self.alt_rect4
        elif self.alt1 == self.alternatives[1]:
            self.alt_correct = self.alt_rect2
            self.alt_wrong_1 = self.alt_rect1
            self.alt_wrong_2 = self.alt_rect3
            self.alt_wrong_3 = self.alt_rect4
        elif self.alt1 == self.alternatives[2]:
            self.alt_correct = self.alt_rect3
            self.alt_wrong_1 = self.alt_rect2
            self.alt_wrong_1 = self.alt_rect1
            self.alt_wrong_1 = self.alt_rect4
        elif self.alt1 == self.alternatives[3]:
            self.alt_correct = self.alt_rect4
            self.alt_wrong_1 = self.alt_rect2
            self.alt_wrong_2 = self.alt_rect3
            self.alt_wrong_3 = self.alt_rect1
    
    def click(self):         
        clicked_1 = False 
        clicked_2 = False


        mouse = pygame.mouse.get_pos()
        if clicked_1 == False and clicked_2 == False:
            if self.alt_correct.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    clicked_1 = True
                    return 'clicked'
            if self.alt_wrong_1.collidepoint(mouse) or self.alt_wrong_2.collidepoint(mouse) or self.alt_wrong_3.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    clicked_2 = True
                    return 'clicked'
            
        if clicked_1 == True:
            self.screen.blit(self.bg_acerto_certo, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'level1'
              
        if clicked_2 == True:
            self.screen.blit(self.bg_acerto_errado, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'level1'