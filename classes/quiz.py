import pygame
from pygame.locals import *
from text import Text
import random

class Quiz:
    def __init__(self, question_1, question_2, alt1, alt2, alt3, alt4):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.quiz_bg = pygame.image.load('quiz_bg').convert_alpha()
        self.question_1 = question_1
        self.question_2 = question_2
        self.alt1 = alt1
        self.alt2 = alt2
        self.alt3 = alt3
        self.alt4 = alt4
        self.pos_question_1 = [160, 130]
        self.pos_question_2 = [self.pos_question_1[0], self.pos_question_1[0] + 48]
        self.pos_alt1_1 = [292, 435]
        self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 25]
        self.pos_alt1_3 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 50]
        self.pos_alt1_4 = [self.pos_alt1_1[0], self.pos_alt1_1[1] + 75]
        self.pos_alt2_1 = [292, 780]
        self.pos_alt2_2 = [self.pos_alt2_2[0], self.pos_alt2_2[1] + 25]
        self.pos_alt2_3 = [self.pos_alt2_2[0], self.pos_alt2_2[1] + 50]
        self.pos_alt2_4 = [self.pos_alt2_2[0], self.pos_alt2_2[1] + 75]
        self.pos_alt3_1 = [1027, 435]
        self.pos_alt3_2 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 25]
        self.pos_alt3_3 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 50]
        self.pos_alt3_4 = [self.pos_alt3_1[0], self.pos_alt3_1[1] + 75]
        self.pos_alt4_1 = [1027, 780]
        self.pos_alt4_2 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 25]
        self.pos_alt4_3 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 50]
        self.pos_alt4_4 = [self.pos_alt4_1[0], self.pos_alt4_1[1] + 75]
        self.alternatives = [self.alt1, self.alt2, self.alt3, self.alt4]
        self.font_question = pygame.font.Font('fonts/upheavtt.ttf', 48)
        self.font_alt = pygame.font.Font('fonts/upheavtt.ttf', 25)
        self.text_question_1 = Text(self.question_1, self.font_question, 'BLACK', self.pos_question_1[0], self.pos_question_2[1])
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
    
    def shuffle(self):
        random.shuffle(self.alternatives)

    def rect_alternatives(self):
        self.alt_rect1 = pygame.Rect(254, 370, 676, 294)
        self.alt_rect2 = pygame.Rect(254, 724, 676, 294)
        self.alt_rect3 = pygame.Rect(990, 370, 676, 294)
        self.alt_rect4 = pygame.Rect(990, 724, 676, 294)

    def discover_alt_correct(self):
        if self.alt1 == self.alternatives[0]:
                self.alt_correct = self.alt_rect1
                self.alt_wrong_1 = self.alt_rect2
                self.alt_wrong_2 = self.alt_rect3
                self.alt_wrong_3 = self.alt_rect4
        elif self.alt1 == self.alternatives[1]:
                self.correct = self.alt_rect2
                self.wrong_1 = self.alt_rect1
                self.wrong_2 = self.alt_rect3
                self.wrong_3 = self.alt_rect4
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
                self.pos_alt1_2 = [self.pos_alt1_1[0], self.pos_alt1[1] + 25]
                self.pos_alt1_3 = [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4 = [292, self.pos_alt1[1] + 75]
            elif self.pergunta_1r[0][3] == '':
                self.pos_alt1[1] = 475
                self.pos_alt1_2=  [292, self.pos_alt1[1] + 25]
                self.pos_alt1_3=  [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4=  [292, self.pos_alt1[1] + 75]
            else:
                self.pos_alt1[1] = 470
                self.pos_alt1_2 = [292, self.pos_alt1[1] + 25]
                self.pos_alt1_3 = [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4 = [292, self.pos_alt1[1] + 75]
            if self.pergunta_1r[1][2] == '':
                self.pos_alt2[1] = 825
                self.pos_alt2_2 = [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3 = [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4 = [292, self.pos_alt2[1] + 75]
            elif self.pergunta_1r[1][3] == '':
                self.pos_alt2[1] = 820
                self.pos_alt2_2=  [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3=  [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4=  [292, self.pos_alt2[1] + 75]
            else:
                self.pos_alt2[1] = 815
                self.pos_alt2_2 = [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3 = [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4 = [292, self.pos_alt2[1] + 75]
            if self.pergunta_1r[2][2] == '':
                self.pos_alt3[1] = 480
                self.pos_alt3_2=  [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3=  [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4=  [1027, self.pos_alt3[1] + 75]
            elif self.pergunta_1r[2][3] == '':
                self.pos_alt3[1] = 475
                self.pos_alt3_2=  [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3=  [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4=  [1027, self.pos_alt3[1] + 75]
            else:
                self.pos_alt3[1] = 470
                self.pos_alt3_2 = [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3 = [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4 = [1027, self.pos_alt3[1] + 75]
            if self.pergunta_1r[3][2] == '':
                self.pos_alt4[1] = 825
                self.pos_alt4_2 = [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3 = [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4 = [1027, self.pos_alt4[1] + 75]
            elif self.pergunta_1r[3][3] == '':
                self.pos_alt4[1] = 820
                self.pos_alt4_2=  [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3=  [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4=  [1027, self.pos_alt4[1] + 75]
            else:
                self.pos_alt4[1] = 815
                self.pos_alt4_2 = [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3 = [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4 = [1027, self.pos_alt4[1] + 75]
        
    def pergunta_quiz(self, pergunta_linha1, pos_pergunta_linha1, pergunta_linha2, pos_pergunta_linha2, alternativa_1, alternativa_1_2, alternativa_1_3, alternativa_1_4, alternativa_2, alternativa_2_2, alternativa_2_3, alternativa_2_4,
                      alternativa_3, alternativa_3_2, alternativa_3_3,alternativa_3_4, alternativa_4, alternativa_4_2, alternativa_4_3, alternativa_4_4):
        
            self.screen.blit(self.quiz_bg, (0, 0))
            mouse = pygame.mouse.get_pos()
            
            #CENTRALIZAR TEXTO EIXO Y
            
            if self.pergunta_1r[0][2] == '':
                self.pos_alt1[1] = 480
                self.pos_alt1_2 = [292, self.pos_alt1[1] + 25]
                self.pos_alt1_3 = [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4 = [292, self.pos_alt1[1] + 75]
            elif self.pergunta_1r[0][3] == '':
                self.pos_alt1[1] = 475
                self.pos_alt1_2=  [292, self.pos_alt1[1] + 25]
                self.pos_alt1_3=  [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4=  [292, self.pos_alt1[1] + 75]
            else:
                self.pos_alt1[1] = 470
                self.pos_alt1_2 = [292, self.pos_alt1[1] + 25]
                self.pos_alt1_3 = [292, self.pos_alt1[1] + 50]
                self.pos_alt1_4 = [292, self.pos_alt1[1] + 75]
            if self.pergunta_1r[1][2] == '':
                self.pos_alt2[1] = 825
                self.pos_alt2_2 = [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3 = [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4 = [292, self.pos_alt2[1] + 75]
            elif self.pergunta_1r[1][3] == '':
                self.pos_alt2[1] = 820
                self.pos_alt2_2=  [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3=  [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4=  [292, self.pos_alt2[1] + 75]
            else:
                self.pos_alt2[1] = 815
                self.pos_alt2_2 = [292, self.pos_alt2[1] + 25]
                self.pos_alt2_3 = [292, self.pos_alt2[1] + 50]
                self.pos_alt2_4 = [292, self.pos_alt2[1] + 75]
            if self.pergunta_1r[2][2] == '':
                self.pos_alt3[1] = 480
                self.pos_alt3_2=  [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3=  [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4=  [1027, self.pos_alt3[1] + 75]
            elif self.pergunta_1r[2][3] == '':
                self.pos_alt3[1] = 475
                self.pos_alt3_2=  [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3=  [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4=  [1027, self.pos_alt3[1] + 75]
            else:
                self.pos_alt3[1] = 470
                self.pos_alt3_2 = [1027, self.pos_alt3[1] + 25]
                self.pos_alt3_3 = [1027, self.pos_alt3[1] + 50]
                self.pos_alt3_4 = [1027, self.pos_alt3[1] + 75]
            if self.pergunta_1r[3][2] == '':
                self.pos_alt4[1] = 825
                self.pos_alt4_2 = [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3 = [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4 = [1027, self.pos_alt4[1] + 75]
            elif self.pergunta_1r[3][3] == '':
                self.pos_alt4[1] = 820
                self.pos_alt4_2=  [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3=  [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4=  [1027, self.pos_alt4[1] + 75]
            else:
                self.pos_alt4[1] = 815
                self.pos_alt4_2 = [1027, self.pos_alt4[1] + 25]
                self.pos_alt4_3 = [1027, self.pos_alt4[1] + 50]
                self.pos_alt4_4 = [1027, self.pos_alt4[1] + 75]
            
            collision_alternativa_1 = pygame.Rect(254, 370, 676, 294)
            collision_alternativa_2 = pygame.Rect(254, 724, 676, 294)
            collision_alternativa_3 = pygame.Rect(990, 370, 676, 294)
            collision_alternativa_4 = pygame.Rect(990, 724, 676, 294)
    
            
                           
            
            if x.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.clicked_1 = False
            if y.collidepoint(mouse) or z.collidepoint(mouse) or g.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.clicked_2 = False
            if self.clicked_1 == False:
                self.screen.blit(self.bg_acerto_certo, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.clicked_1 = True
                        self.clicked_quiz1 = False
                        self.shuffle_on = True
                        self.fade_alpha = 255
            if self.clicked_2 == False:
                self.screen.blit(self.bg_acerto_errado, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        self.clicked_2 = True
                        self.clicked_quiz1 = False
                        self.shuffle_on = True
                        self.fade_alpha = 255