import pygame
from pygame.locals import *
import mysql.connector
from input_box import InputBox
from text import Text
from database import Database
from button_menu import ButtonMenu

class Login:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.login_bg = pygame.image.load('images/backgrounds/digital-art-horizon-mountains-forest-pinkish.jpg')
        self.login_pop_up = pygame.image.load('images/backgrounds/login_pop_up.png')
        self.edge_user = pygame.image.load('images/buttons/edge_user.png')
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 80)
        self.user_inputbox = InputBox(425, 240, 1070, 50)
        self.password_inputbox = InputBox(425, 500, 1070, 50)
        
        self.pos_user_text = [425, 160]
        self.pos_password_text = [425, 420]
        
        self.pos_button_quit = [1163.5, 750]
        self.pos_button_login = [463.5, 750]
        self.pos_button_register = [813.5, 750]
        
        self.user_text = Text('Usuário:', self.font, 'BLACK', self.pos_user_text[0], self.pos_user_text[1])
        self.password_text = Text('Senha:', self.font, 'BLACK', self.pos_password_text[0], self.pos_password_text[1])
        
        self.text_quit = Text('Quit', self.font, 'BLACK', self.pos_button_quit[0] + 60, self.pos_button_quit[1] + 15)
        self.text_login = Text('Login', self.font, 'BLACK', self.pos_button_login[0] + 30, self.pos_button_login[1]+ 15)
        self.text_register = Text('Criar',self.font, 'BLACK', self.pos_button_register[0] + 30, self.pos_button_register[1]+ 15)
        
        self.button_quit = ButtonMenu(self.pos_button_quit[0],  self.pos_button_quit[1], 'quit')
        self.button_login = ButtonMenu(self.pos_button_login[0], self.pos_button_login[1], 'login')
        self.button_register = ButtonMenu(self.pos_button_register[0], self.pos_button_register[1], 'register')
        
        self.user = ''
        self.senha = ''
        
        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "gustavoimt123"
        )
        self.db = Database()

    def run(self):
        self.clock.tick(30)
        self.screen.blit(self.login_bg, (0,0))
        self.screen.blit(self.login_pop_up, (360, 135))
        self.screen.blit(self.edge_user, (415, 230))
        self.screen.blit(self.edge_user, (415, 490))
        for event in pygame.event.get():
            self.user = self.user_inputbox.handle_event_user(event)
            self.password = self.password_inputbox.handle_event(event)
        
        self.button_quit.show()
        self.button_quit.click()
        self.text_quit.show() 
        
        self.button_login.show()
        if self.button_login.click() == 'login':
            self.db.login(self.mydb, self.user, self.password)
        self.text_login.show()
        
        self.button_register.show()
        self.button_register.click()
        self.text_register.show()
        
        self.user_text.show()
        self.password_text.show()
        self.password_inputbox.draw_password(self.screen)
        self.user_inputbox.draw(self.screen)
        
    def get_user(self):
        return self.user
