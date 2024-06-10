import pygame
from pygame.locals import *
import mysql.connector
from input_box import InputBox
from text import Text
from database import Database

class Login:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.login_bg = pygame.image.load('images/backgrounds/digital-art-horizon-mountains-forest-pinkish.jpg')
        self.email = ''
        self.senha = ''

    def run(self):
        self.clock.tick(30)
        self.screen.blit(self.login_bg, (0,0))
    
    def get_email(self):
        return self.email