import pygame

class ShowButton:
<<<<<<< HEAD
=======
    
>>>>>>> fb15168f0d9f257134fe84ddd4ebaee975414cef
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