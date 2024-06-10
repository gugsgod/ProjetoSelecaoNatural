import pygame
from pygame.locals import *
import sys
from input_box import InputBox
from text import Text

class Rank:
    def __init__(self):
        #Padrão
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.rank_bg = pygame.image.load('images/backgrounds/digital-art-horizon-mountains-forest-pinkish.jpg')
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 80)
        self.pos_text_user = [425, 70]
        self.pos_rank = [800, 225]
        self.user_inputbox = InputBox(425, 150, 400, 50)
        self.text_rank = Text('RANK:', self.font, 'BLACK', self.pos_rank[0], self.pos_rank[1])
        self.text_user = Text('Digite o nome do usuário:', self.font, 'BLACK', self.pos_text_user[0], self.pos_text_user[1])
    
    def run(self):
        self.clock.tick(30)
        self.screen.blit(self.rank_bg, (0,0))
        for event in pygame.event.get():
            self.user_inputbox.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    return 'menu'
        self.user_inputbox.update()
        self.user_inputbox.draw(self.screen)
        self.text_user.show()
        self.text_rank.show()