import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, font, text_col, x, y):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.text = text
        self.font = font
        self.text_col = text_col
        self.x = x
        self.y = y
           
    def show(self):
        img = self.font.render(self.text, True, self.text_col)
        self.screen.blit(img, (self.x, self.y))
        
    def showBotao(self, lista, botao):
        tamanho = len(lista)
        for i in range(tamanho):
            img = self.font.render(lista[i], True, self.text_col)
            if i == 0 and tamanho == 1:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 159.5))
            elif i == 0 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 173.5))
            elif i == 1 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 120.5))
            elif i == 0 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 187.5))
            elif i == 1 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 159.5))
            elif i == 2 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 131.5))
            elif i == 0 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 201.5))
            elif i == 1 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 173.5))
            elif i == 2 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 120.5))
            elif i == 3 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 92.5))
                