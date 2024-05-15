import pygame


class ShowButton:
    def __init__(self, font, text_col):
        self.font = font
        self.text_col = text_col

    def ShowButton(self, lista, botao):
        tamanho = len(lista)
        standard_y = 125
        for i in range(tamanho):
            img = self.font.render(lista[i], True, self.text_col)
            if i == 0 and tamanho == 1:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 11.5))
                break
            elif i == 0 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y - 1.5))
            elif i == 1 and tamanho == 2:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 24.5))
                break
            elif i == 0 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y - 14.5))
            elif i == 1 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 11.5))
            elif i == 2 and tamanho == 3:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 37.5))
                break
            elif i == 0 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y - 27.5))
            elif i == 1 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y - 1.5))
            elif i == 2 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 24.5))
            elif i == 3 and tamanho == 4:
                tamanhoFont = self.font.size(lista[i])
                botao.blit(img, (338 - tamanhoFont[0]/2, standard_y + 50.5))
                break
            
    def show_question(self, lista):
        tamanho = len(list)
        y_padrao = 140
        jorge = pygame.font.Font('fonts/upheavtt.ttf', 48)
        font_size = jorge.size(lista[i])
        lista
        for i in range(tamanho):
            if i == 0 and tamanho == 1:
                lista.append((1920/2 - font_size[0]/2 , y_padrao))
            if i == 0 and tamanho == 2:
                lista.append((1920/2 - font_size[1]/2 , y_padrao - 12.5))
            if i == 1 and tamanho == 2:
                lista.append((1920/2 - font_size[1]/2 , y_padrao +12.5))