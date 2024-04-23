import pygame
from pygame.locals import *
from text import Text
import random

class Quiz:
    def __init__(self, question_1, question_2, alt1, alt2, alt3, alt4):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.quiz_bg = pygame.image.load('images/quiz_bg.png').convert_alpha()
        self.bg_acerto_certo = pygame.image.load('images/bg_acerto_certo.png').convert_alpha()
        self.bg_acerto_errado = pygame.image.load('images/bg_acerto_errado.png').convert_alpha()
        self.question_1 = question_1
        self.question_2 = question_2
        self.alt1 = alt1
        self.alt2 = alt2
        self.alt3 = alt3
        self.alt4 = alt4
        self.alternatives = [self.alt1, self.alt2, self.alt3, self.alt4]
        self.pos_question_1 = [160, 130]
        self.pos_question_2 = [self.pos_question_1[0], self.pos_question_1[0] + 38]
        self.pos_alt1_1 = [292, 435]
        self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 25]
        self.pos_alt1_3 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 50]
        self.pos_alt1_4 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 75]
        self.pos_alt2_1 = [292, 780]
        self.pos_alt2_2 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 25]
        self.pos_alt2_3 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 50]
        self.pos_alt2_4 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 75]
        self.pos_alt3_1 = [1027, 435]
        self.pos_alt3_2 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 25]
        self.pos_alt3_3 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 50]
        self.pos_alt3_4 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 75]
        self.pos_alt4_1 = [1027, 780]
        self.pos_alt4_2 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 25]
        self.pos_alt4_3 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 50]
        self.pos_alt4_4 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 75]
        self.font_question = pygame.font.Font('fonts/upheavtt.ttf', 48)
        self.font_alt = pygame.font.Font('fonts/upheavtt.ttf', 25)
        self.text_question_1 = Text(self.question_1, self.font_question, 'BLACK', self.pos_question_1[0], self.pos_question_1[1])
        self.text_question_2 = Text(self.question_2, self.font_question, 'BLACK', self.pos_question_2[0], self.pos_question_2[1])
        self.text_alt1_1 = Text(self.alternatives[0][0], self.font_alt, 'BLACK', self.pos_alt1_1[0], self.pos_alt1_1[1])
        self.text_alt1_2 = Text(self.alternatives[0][1], self.font_alt, 'BLACK', self.pos_alt1_2[0], self.pos_alt1_2[1])
        self.text_alt1_3 = Text(self.alternatives[0][2], self.font_alt, 'BLACK', self.pos_alt1_3[0], self.pos_alt1_3[1])
        self.text_alt1_4 = Text(self.alternatives[0][3], self.font_alt, 'BLACK', self.pos_alt1_4[0], self.pos_alt1_4[1])
        self.text_alt2_1 = Text(self.alternatives[1][0], self.font_alt, 'BLACK', self.pos_alt2_1[0], self.pos_alt2_1[1])
        self.text_alt2_2 = Text(self.alternatives[1][1], self.font_alt, 'BLACK', self.pos_alt2_2[0], self.pos_alt2_2[1])
        self.text_alt2_3 = Text(self.alternatives[1][2], self.font_alt, 'BLACK', self.pos_alt2_3[0], self.pos_alt2_3[1])
        self.text_alt2_4 = Text(self.alternatives[1][3], self.font_alt, 'BLACK', self.pos_alt2_4[0], self.pos_alt2_4[1])
        self.text_alt3_1 = Text(self.alternatives[2][0], self.font_alt, 'BLACK', self.pos_alt3_1[0], self.pos_alt3_1[1])
        self.text_alt3_2 = Text(self.alternatives[2][1], self.font_alt, 'BLACK', self.pos_alt3_2[0], self.pos_alt3_2[1])
        self.text_alt3_3 = Text(self.alternatives[2][2], self.font_alt, 'BLACK', self.pos_alt3_3[0], self.pos_alt3_3[1])
        self.text_alt3_4 = Text(self.alternatives[2][3], self.font_alt, 'BLACK', self.pos_alt3_4[0], self.pos_alt3_4[1])
        self.text_alt4_1 = Text(self.alternatives[3][0], self.font_alt, 'BLACK', self.pos_alt4_1[0], self.pos_alt4_1[1])
        self.text_alt4_2 = Text(self.alternatives[3][1], self.font_alt, 'BLACK', self.pos_alt4_2[0], self.pos_alt4_2[1])
        self.text_alt4_3 = Text(self.alternatives[3][2], self.font_alt, 'BLACK', self.pos_alt4_3[0], self.pos_alt4_3[1])
        self.text_alt4_4 = Text(self.alternatives[3][3], self.font_alt, 'BLACK', self.pos_alt4_4[0], self.pos_alt4_4[1])
        self.alt_rect1 = pygame.Rect(254, 370, 676, 294)
        self.alt_rect2 = pygame.Rect(254, 724, 676, 294)
        self.alt_rect3 = pygame.Rect(990, 370, 676, 294)
        self.alt_rect4 = pygame.Rect(990, 724, 676, 294)

    def show(self):
        self.screen.blit(self.quiz_bg, (0, 0))
        self.text_question_1.show()
        self.text_question_2.show()
        self.text_alt1_1.show()
        self.text_alt1_2.show()
        self.text_alt1_3.show()
        self.text_alt1_4.show()
        self.text_alt2_1.show()
        self.text_alt2_2.show()
        self.text_alt2_3.show()
        self.text_alt2_4.show()
        self.text_alt3_1.show()
        self.text_alt3_2.show()
        self.text_alt3_3.show()
        self.text_alt3_4.show()
        self.text_alt4_1.show()
        self.text_alt4_2.show()
        self.text_alt4_3.show()
        self.text_alt4_4.show()
    
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
    
    def centralize_y(self):
         
        if self.alternatives[0][2] == '':
            self.pos_alt1_1[1] = 480
            self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 25]
            self.pos_alt1_3 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 50]
            self.pos_alt1_4 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 75]
        elif self.alternatives[0][3] == '':
            self.pos_alt1_1[1] = 475
            self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 25]
            self.pos_alt1_3 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 50]
            self.pos_alt1_4 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 75]
        else:
            self.pos_alt1_1[1] = 470
            self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 25]
            self.pos_alt1_3 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 50]
            self.pos_alt1_4 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 75]
        if self.alternatives[1][2] == '':
            self.pos_alt2_1[1] = 825
            self.pos_alt2_2 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 25]
            self.pos_alt2_3 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 50]
            self.pos_alt2_4 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 75]
        elif self.alternatives[1][3] == '':
            self.pos_alt2_1[1] = 820
            self.pos_alt2_2 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 25]
            self.pos_alt2_3 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 50]
            self.pos_alt2_4 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 75]
        else:
            self.pos_alt2_1[1] = 815
            self.pos_alt2_2 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 25]
            self.pos_alt2_3 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 50]
            self.pos_alt2_4 = [self.pos_alt2_1[0], self.pos_alt2_1[1] + 75]
        if self.alternatives[2][2] == '':
            self.pos_alt3_1[1] = 480
            self.pos_alt3_2 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 25]
            self.pos_alt3_3 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 50]
            self.pos_alt3_4 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 75]
        elif self.alternatives[2][3] == '':
            self.pos_alt3_1[1] = 475
            self.pos_alt3_2 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 25]
            self.pos_alt3_3 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 50]
            self.pos_alt3_4 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 75]
        else:
            self.pos_alt3_1[1] = 470
            self.pos_alt3_2 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 25]
            self.pos_alt3_3 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 50]
            self.pos_alt3_4 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 75]
        if self.alternatives[3][2] == '':
            self.pos_alt4_1[1] = 825
            self.pos_alt4_2 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 25]
            self.pos_alt4_3 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 50]
            self.pos_alt4_4 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 75]
        elif self.alternatives[3][3] == '':
            self.pos_alt4_1[1] = 820
            self.pos_alt4_2 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 25]
            self.pos_alt4_3 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 50]
            self.pos_alt4_4 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 75]
        else:
            self.pos_alt4_1[1] = 815
            self.pos_alt4_2 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 25]
            self.pos_alt4_3 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 50]
            self.pos_alt4_4 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 75]

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