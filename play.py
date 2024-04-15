import pygame
from pygame.locals import *
import random
from characater import Character
from fade_in import FadeIn
from frog import Frog

class Play:
    def __init__(self):
        self.character = Character('Scientists.png', 0, 0, [50, 40], [10,110], 0)
        self.frog_1 = Frog(pygame.image.load('frog.png').convert_alpha(), [500, 100])
        self.frog_2 = Frog(pygame.image.load('frog.png').convert_alpha(), [100, 700])
    def run(self):
        
        random.shuffle(self.pergunta_1r)
                
        self.clock.tick(10)

        self.screen.blit(self.bg_play,  (0,0))
               
        self.frog_1.show()
        self.frog_1.movement()
        self.frog_1.frog_collision_screen()
               
        self.frog_2.show()
        self.frog_2.movement()
        self.frog_2.movement()
                
        self.character.show()
        self.character.skin()
        self.character.movement()
        self.character.animation()
        self.character.character_collision_screen()
                
                
                
    

        #COLISSION
                    
        colission_placa_1 = pygame.Rect(270, 105, 44, 50)
        player_area = pygame.Rect(self.player_pos[0], self.player_pos[1], self.player_tamanho[0], self.player_tamanho[1])

        '''if player_area.colliderect(colission_placa_1):
                
            self.clicked_quiz1 = True
            self.player_pos[0] = 150
            self.player_pos[1] = 125
            self.shuffle_on = False'''
        '''else:       
                pygame.draw.rect(self.screen, (0, 50, 155), self.colission_area)'''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE: