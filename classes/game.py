import pygame
from pygame.locals import *
import sys
from login import Login
from menu import Menu
from rank import Rank
from level1 import Level1
from level2 import Level2
from score import Score

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('SN GAME')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.login = Login()
        self.menu = Menu()
        self.rank = Rank()
        self.level1 = Level1()
        self.level2 = Level2()
        self.score = Score()
        self.screen_status = 'login'
        
    def run(self):
        while True:
            pygame.mixer.music.set_volume(0.2)
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.load("SoundEffects/musica/ordinary-loop-minimal-piano-182046.mp3")
                pygame.mixer.music.play()
            if self.screen_status == 'login':
                match self.login.run():
                    case 'menu':
                        self.screen_status = 'menu'
            if self.screen_status == 'menu':
                match self.menu.run():
                    case 'level1':
                        self.screen_status = 'level1'
                    case 'rank':
                        self.screen_status = 'rank'
            
            if self.screen_status == 'rank':
                match self.rank.run():
                    case 'menu':
                        self.screen_status = 'menu'

            if self.screen_status == 'level1':
                match self.level1.run():
                    case 'menu':
                       self.screen_status = 'menu'
                    case 'level2':
                        self.screen_status = 'level2'
                    case 'save_score':
                        self.status_score = True

            if self.screen_status == 'level2':
                match self.level2.run():
                    case 'menu':
                        self.screen_status = 'menu'
                    case 'score':
                        self.screen_status = 'score'
            
            if self.screen_status == 'score':
                match self.score.run(self.level1.get_score(), self.level2.get_score(), self.login.get_user()):
                    case 'menu':
                        self.screen_status = 'menu'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

Game().run()