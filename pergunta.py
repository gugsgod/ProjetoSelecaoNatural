import pygame
from pygame.locals import *
from text import Text

class Pergunta:
    def __init__(self):
        self.p11= ['  Essa semelhança é resultado de mutações', 'aleatórias que foram selecionadas ao longo', '   do tempo devido à pressão seletiva dos', '                         predadores']
        self.p12= [' Os insetos desenvolveram essa semelhança', '  para atrair mais facilmente suas presas', '', '']
        self.p13= [' Os insetos adotam essa camuflagem para se', '     protegerem das mudanças climáticas', '', '']
        self.p14= ['  A semelhança com folhas e ramos permite', '    que os insetos se comuniquem de forma', '                   eficiente entre si', '']
        self.pos_alt1 = [292, 435]
        self.pos_alt1_2 = [292, self.pos_alt1[1] + 25]
        self.pos_alt1_3 = [292, self.pos_alt1[1] + 50]
        self.pos_alt1_4 = [292, self.pos_alt1[1] + 75]
        self.pos_alt2 = [292, 780]
        self.pos_alt2_2 = [292, self.pos_alt2[1] + 25]
        self.pos_alt2_3 = [292, self.pos_alt2[1] + 50]
        self.pos_alt2_4 = [292, self.pos_alt2[1] + 75]
        self.pos_alt3 = [1027, 435]
        self.pos_alt3_2=  [1027, self.pos_alt3[1] + 25]
        self.pos_alt3_3=  [1027, self.pos_alt3[1] + 50]
        self.pos_alt3_4=  [1027, self.pos_alt3[1] + 75]
        self.pos_alt4 = [1027, 780]
        self.pos_alt4_2 = [1027, self.pos_alt4[1] + 25]
        self.pos_alt4_3 = [1027, self.pos_alt4[1] + 50]
        self.pos_alt4_4 = [1027, self.pos_alt4[1] + 75]
        self.pergunta_1r = [self.p11 , self.p12, self.p13, self.p14]
        self.shuffle_on = True
    
    def pergunta_quiz(self, pergunta_linha1, pos_pergunta_linha1, pergunta_linha2, pos_pergunta_linha2, alternativa_1, alternativa_1_2, alternativa_1_3, alternativa_1_4, alternativa_2, alternativa_2_2, alternativa_2_3, alternativa_2_4,
                      alternativa_3, alternativa_3_2, alternativa_3_3,alternativa_3_4, alternativa_4, alternativa_4_2, alternativa_4_3, alternativa_4_4):
        if self.clicked_1 == True and self.clicked_2 == True:
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
            Text.draw_text(self, pergunta_linha1, self.font_pergunta, 'BLACK', pos_pergunta_linha1[0], pos_pergunta_linha1[1])
            Text.draw_text(self, pergunta_linha2, self.font_pergunta, 'BLACK', pos_pergunta_linha2[0], pos_pergunta_linha2[1])
            Text.draw_text(self, alternativa_1, self.font_alternativa, 'BLACK', self.pos_alt1[0], self.pos_alt1[1])
            Text.draw_text(self, alternativa_1_2, self.font_alternativa, 'BLACK', self.pos_alt1_2[0], self.pos_alt1_2[1])
            Text.draw_text(self, alternativa_1_3, self.font_alternativa, 'BLACK', self.pos_alt1_3[0], self.pos_alt1_3[1])
            Text.draw_text(self, alternativa_1_4, self.font_alternativa, 'BLACK', self.pos_alt1_4[0], self.pos_alt1_4[1])
            Text.draw_text(self, alternativa_2, self.font_alternativa, 'BLACK', self.pos_alt2[0], self.pos_alt2[1])
            Text.draw_text(self, alternativa_2_2, self.font_alternativa, 'BLACK', self.pos_alt2_2[0], self.pos_alt2_2[1])
            Text.draw_text(self, alternativa_2_3, self.font_alternativa, 'BLACK', self.pos_alt2_3[0], self.pos_alt2_3[1])
            Text.draw_text(self, alternativa_2_4, self.font_alternativa, 'BLACK', self.pos_alt2_4[0], self.pos_alt2_4[1])
            Text.draw_text(self, alternativa_3, self.font_alternativa, 'BLACK', self.pos_alt3[0], self.pos_alt3[1])
            Text.draw_text(self, alternativa_3_2, self.font_alternativa, 'BLACK', self.pos_alt3_2[0], self.pos_alt3_2[1])
            Text.draw_text(self, alternativa_3_3, self.font_alternativa, 'BLACK', self.pos_alt3_3[0], self.pos_alt3_3[1])
            Text.draw_text(self, alternativa_3_4, self.font_alternativa, 'BLACK', self.pos_alt3_4[0], self.pos_alt3_4[1])
            Text.draw_text(self, alternativa_4, self.font_alternativa, 'BLACK', self.pos_alt4[0], self.pos_alt4[1])
            Text.draw_text(self, alternativa_4_2, self.font_alternativa, 'BLACK', self.pos_alt4_2[0], self.pos_alt4_2[1])
            Text.draw_text(self, alternativa_4_3, self.font_alternativa, 'BLACK', self.pos_alt4_3[0], self.pos_alt4_3[1])
            Text.draw_text(self, alternativa_4_4, self.font_alternativa, 'BLACK', self.pos_alt4_4[0], self.pos_alt4_4[1])
            
            if self.p11 == self.pergunta_1r[0]:
                x = collision_alternativa_1
                y = collision_alternativa_2
                z = collision_alternativa_3
                g = collision_alternativa_4
            elif self.p11 == self.pergunta_1r[1]:
                x = collision_alternativa_2
                y = collision_alternativa_1
                z = collision_alternativa_3
                g = collision_alternativa_4
            elif self.p11 == self.pergunta_1r[2]:
                x = collision_alternativa_3
                y = collision_alternativa_2
                z = collision_alternativa_1
                g = collision_alternativa_4
            elif self.p11 == self.pergunta_1r[3]:
                x = collision_alternativa_4
                y = collision_alternativa_2
                z = collision_alternativa_3
                g = collision_alternativa_1                
            
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