import pygame


class CentralizeText:
    def __init__(self, font, text_col,screen = None):
        self.font = font
        self.text_col = text_col
        self.screen = screen

    def centralize_alternative(self, list, button):
        size = len(list)
        standard_y = 125
        for i in range(size):
            img = self.font.render(list[i], True, self.text_col)
            if i == 0 and size == 1:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 11.5))
                break
            elif i == 0 and size == 2:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y - 1.5))
            elif i == 1 and size == 2:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 24.5))
                break
            elif i == 0 and size == 3:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y - 14.5))
            elif i == 1 and size == 3:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 11.5))
            elif i == 2 and size == 3:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 37.5))
                break
            elif i == 0 and size == 4:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y - 27.5))
            elif i == 1 and size == 4:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y - 1.5))
            elif i == 2 and size == 4:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 24.5))
            elif i == 3 and size == 4:
                sizeFont = self.font.size(list[i])
                button.blit(img, (338 - sizeFont[0]/2, standard_y + 50.5))
                break
            
    def centralize_question(self, list):
        size = len(list)
        y_standard = 140
        for i in range(size):
            img = self.font.render(list[i], True, self.text_col)
            if i == 0 and size == 1:
                font_size = self.font.size(list[i])
                self.screen.blit(img, (1920/2 + font_size[0]/2 , y_standard))
                break
            if i == 0 and size == 2:
                font_size = self.font.size(list[i])
                self.screen.blit(img, (1920/2 - font_size[0]/2 , y_standard - 12.5))
            if i == 1 and size == 2:
                font_size = self.font.size(list[i])
                self.screen.blit(img, (1920/2 - font_size[0]/2 , y_standard + 25))
                break