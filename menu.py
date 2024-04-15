import pygame
from pygame.locals import *
from button_menu import ButtonMenu
from text import Text
def __init__(self):
    self.button_play = ButtonMenu(813.5, 300)
    self.button_rank = ButtonMenu(813.5, 525)
    self.button_quit = ButtonMenu(813.5, 750)
    self.text_play = self.Text(self, 'SN GAME', self.font, 'BLACK', self.pos_button_play[0] - 10, 100)

def run(self):
    
    self.text_play.draw_text(self, 'SN GAME', self.font, 'BLACK', self.pos_button_play[0] - 10, 100)
    self.button_play.show()
    self.button_play.show()
    self.button_rank.show()
    self.button_quit.show()