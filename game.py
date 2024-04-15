import pygame
from pygame.locals import *
import sys
import random
from text import Text
from pergunta import Pergunta
from button_menu import ButtonMenu
from characater import Character
from fade_in import FadeIn
from frog import Frog
from play import Play
class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('SN GAME')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.play = Play()
        self.bg_play = pygame.image.load('bg_game.png').convert_alpha()
        self.clicked_menu = True
        self.clicked_quiz1 = False
        self.clicked_1 = True
        self.clicked_2 = True
        self.fade = FadeIn(pygame.Surface((1920, 1080)).convert_alpha(), 255, (0, 0, 1920, 1080))
        self.tree = pygame.image.load('trees.png').convert_alpha()
        self.quiz_bg = pygame.image.load('quiz_bg.png').convert_alpha()
        self.bg_acerto_certo = pygame.image.load('bg_acerto_certo.png').convert_alpha()
        self.bg_acerto_errado = pygame.image.load('bg_acerto_errado.png').convert_alpha()
        self.button_menu_1 = pygame.image.load('img.button_menu_1.png').convert_alpha()
        self.button_menu_2 = pygame.image.load('img.button_menu_2.png').convert_alpha()
        self.tamanho_button_menu = [293, 112]
        self.pos_button_rank = [813.5, 525]
        self.pos_button_quit = [813.5, 750]
        self.tree_pos = [320, 30, 200, 260]
        self.player_pos = [10, 110]
        self.player_tamanho = [50, 110]
        self.menu_bg = pygame.image.load('menu_bg.png')
        self.font = pygame.font.Font('upheavtt.ttf', 80)
        self.font_pergunta = pygame.font.Font('upheavtt.ttf', 48)
        self.font_alternativa = pygame.font.Font('upheavtt.ttf', 25)
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
  
    
    
    def run(self):
        while True:

            #MENU
                 
            if self.clicked_menu == True:
                
                self.clock.tick(30)
                self.screen.blit(self.menu_bg, (0,0))

                mouse = pygame.mouse.get_pos()
            
                collision_rank = pygame.Rect(self.pos_button_rank[0], self.pos_button_rank[1], self.tamanho_button_menu[0], self.tamanho_button_menu[1])
                collision_quit = pygame.Rect(self.pos_button_quit[0], self.pos_button_quit[1], self.tamanho_button_menu[0], self.tamanho_button_menu[1])
                
                Text.draw_text(self, 'SN GAME', self.font, 'BLACK', self.pos_button_play[0] - 10, 100)
                self.button_play.show()
                self.button_play.show()
                self.button_rank.show()
                self.button_quit.show()
                
                Text.draw_text(self, 'PLAY', self.font, 'BLACK', self.pos_button_play[0] + 51, self.pos_button_play[1] + 15)
                Text.draw_text(self, 'RANK', self.font, 'BLACK', self.pos_button_rank[0] + 50, self.pos_button_rank[1] + 15)
                Text.draw_text(self, 'QUIT', self.font, 'BLACK', self.pos_button_quit[0] + 60, self.pos_button_quit[1] + 15)
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if collision_play.collidepoint(mouse):
                    self.screen.blit(self.button_menu_2, (self.pos_button_play[0] -3, self.pos_button_play[1] -3))
                    Text.draw_text(self, 'PLAY', self.font, 'BLACK', self.pos_button_play[0] + 51, self.pos_button_play[1] + 15)
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.clicked_menu = False
                        self.fade.reset()
                if collision_rank.collidepoint(mouse):
                    self.screen.blit(self.button_menu_2, (self.pos_button_rank[0] -3, self.pos_button_rank[1] -3))
                    Text.draw_text(self, 'RANK', self.font, 'BLACK', self.pos_button_rank[0] + 50, self.pos_button_rank[1] + 15)
                if collision_quit.collidepoint(mouse):
                    self.screen.blit(self.button_menu_2, (self.pos_button_quit[0] -3, self.pos_button_quit[1] -3))
                    Text.draw_text(self, 'QUIT', self.font, 'BLACK',  self.pos_button_quit[0] + 60, self.pos_button_quit[1] + 15)
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.quit()
                        sys.exit()
                
                self.fade.show()
            

            
                

            #PLAY

            self.play.run()
            
            #QUIZ
                    
            if self.clicked_quiz1 == True:
                
                self.clock.tick(100)
                Pergunta.pergunta_quiz(self, ' Por que alguns insetos parecem folhas ou ramos de plantas?', [160, 130],
                                    ' E como isso os ajuda a escapar dos seus predadores?', [220, 178],
                                    self.pergunta_1r[0][0], self.pergunta_1r[0][1], self.pergunta_1r[0][2], self.pergunta_1r[0][3],
                                    self.pergunta_1r[1][0], self.pergunta_1r[1][1], self.pergunta_1r[1][2], self.pergunta_1r[1][3],
                                    self.pergunta_1r[2][0], self.pergunta_1r[2][1], self.pergunta_1r[2][2], self.pergunta_1r[2][3],
                                    self.pergunta_1r[3][0], self.pergunta_1r[3][1], self.pergunta_1r[3][2], self.pergunta_1r[3][3],)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    
                    sys.exit()
    
            pygame.display.update()

Game().run()