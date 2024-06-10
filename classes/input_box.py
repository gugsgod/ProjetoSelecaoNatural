import pygame
import sys

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 50)
        self.active = False
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)
        self.color = self.GRAY

    # Função para criar a input box
    def draw_text(self, surface, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        self.len_text = len(self.text)
        if self.len_text < 56:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.WHITE if self.active else self.GRAY
            if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            return self.text
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
        else:
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
    
    def update(self):
        width = max(1070, self.font.size(self.text)[0]+10)
        self.rect.w = width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_text(surface, self.text, self.font, self.BLACK, self.rect.x+5, self.rect.y+5)