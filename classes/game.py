import pygame
from pygame.locals import *
import sys
import random
from text import Text

from button_menu import ButtonMenu
from character import Character
from fade_in import FadeIn
from frog import Frog
from level1 import Level1
from menu import Menu

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('SN GAME')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.level1 = Level1()
        self.screen_status = 'menu'
    
    def run(self):
        while True:
            pygame.mixer.music.set_volume(0.2)
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.load("SoundEffects/musica/ordinary-loop-minimal-piano-182046.mp3")
                pygame.mixer.music.play()
            if self.screen_status == 'menu':
                if self.menu.run() == 'level1':
                    self.screen_status = 'level1'
            
            if self.screen_status == 'level1':
                match self.level1.run():
                    case 'menu':
                       self.screen_status = 'menu'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    
                    sys.exit()
    
            pygame.display.update()

Game().run()