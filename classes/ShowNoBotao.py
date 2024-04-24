import pygame

class BotaoShow:
    
    def __init__(self, font, text_col):
        self.font = font
        self.text_col = text_col

    def showBotao(self, lista, botao):
        tamanho = len(lista)
        for i in range(tamanho):
            img = self.font.render(lista[i], True, self.text_col)
            if i == 0 and tamanho == 1:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 159.5))
                break
            elif i == 0 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 120.5))
            elif i == 1 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 173.5))
                break
            elif i == 0 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 131.5))
            elif i == 1 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 159.5))
            elif i == 2 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 187.5))
                break
            elif i == 0 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 92.5))
            elif i == 1 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 120.5))
            elif i == 2 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 173.5))
            elif i == 3 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, 201.5))
                break