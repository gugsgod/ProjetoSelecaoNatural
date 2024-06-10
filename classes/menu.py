import pygame
from pygame.locals import *
import sys
from button_menu import ButtonMenu
from text import Text
from fade_in import FadeIn

class Menu:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.menu_bg = pygame.image.load('images/backgrounds/digital-art-horizon-mountains-forest-pinkish.jpg')
        self.pos_name = [803.5, 100]
        self.pos_button_play = [813.5, 300]
        self.pos_button_rank = [813.5, 525]
        self.pos_button_quit = [813.5, 750]
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 80)
        self.text_name = Text('SN GAME', self.font, 'BLACK', self.pos_name[0], self.pos_name[1])
        self.text_play = Text('Play', self.font, 'BLACK', self.pos_button_play[0] + 51, self.pos_button_play[1] + 15)
        self.text_rank = Text('Rank', self.font, 'BLACK', self.pos_button_rank[0] + 50, self.pos_button_rank[1] + 15)
        self.text_quit = Text('Quit', self.font, 'BLACK', self.pos_button_quit[0] + 60, self.pos_button_quit[1] + 15)
        self.button_level1 = ButtonMenu(self.pos_button_play[0],  self.pos_button_play[1], 'level1')
        self.button_rank = ButtonMenu(self.pos_button_rank[0], self.pos_button_rank[1], 'rank')
        self.button_quit = ButtonMenu(self.pos_button_quit[0],  self.pos_button_quit[1], 'quit')
        self.fade_in = FadeIn()
    
    def run(self):
        
        self.clock.tick(30)
        self.screen.blit(self.menu_bg, (0,0))
        self.button_level1.show()
        if self.button_level1.click() == 'level1':
            return 'level1'
        self.button_rank.show()
        if self.button_rank.click() == 'rank':
            return 'rank'
        self.button_quit.show()
        self.button_quit.click()
        self.text_name.show()
        self.text_play.show()
        self.text_rank.show()
        self.text_quit.show()
        self.fade_in.show()

        