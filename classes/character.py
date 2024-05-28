import pygame
from pygame.locals import *

class Character:
    def __init__(self, character_img, sprite_charactery, sprite_characterx, character_size, character_pos, skiny):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.character_img = pygame.image.load(character_img).convert_alpha()
        self.character_img = pygame.transform.scale(self.character_img, (736 * 3, 512 * 3))
        self.sprite_charactery = sprite_charactery
        self.sprite_characterx = sprite_characterx
        self.character_size = character_size
        self.character_pos = character_pos
        self.skin_y = skiny
        
    
    def show(self):
        self.screen.blit(self.character_img, self.character_pos, (self.sprite_characterx* 96, self.sprite_charactery, 96, 96))
    
    def pos(self, character_pos):
        self.character_pos = character_pos
    
    def skin(self):
        key = pygame.key.get_pressed()
        if key[K_1]:
            self.skin_y = 0
        if key[K_2]:
            self.skin_y = 4
        if key[K_3]:
            self.skin_y = 8
        if key[K_4]:
            self.skin_y = 12
        
        self.sprite_charactery = 96 * self.skin_y 
    
    def movement(self):
        key = pygame.key.get_pressed() 
        if key[K_w]:
            self.character_pos[1] -= 14
            self.sprite_charactery = 96 * (self.skin_y + 1)
        if key[K_s]:
            self.character_pos[1] += 14
            self.sprite_charactery = 96 * (self.skin_y + 1)
        if key[K_d]:
            self.character_pos[0] += 14
            self.sprite_charactery = 96 * (self.skin_y + 1)
        if key[K_a]:
            self.character_pos[0] -= 14
            self.sprite_charactery = 96 * (self.skin_y + 1)
         
    def animation(self):
        self.sprite_characterx += 1
        if self.sprite_characterx > 3:
            self.sprite_characterx = 0
    
    def collision_screen(self):
        if self.character_pos[0] < -20:
            self.character_pos[0] += 14
        if self.character_pos[0] > 1850:
            self.character_pos[0] -= 14
        if self.character_pos[1] < -20:
            self.character_pos[1] += 14
        if self.character_pos[1] > 990:
            self.character_pos[1] -= 14

    def collision_tree(self, pos):
        tree_size = [0, 0]
        character_surface = pygame.Rect(self.character_pos[0], self.character_pos[1]+20, self.character_size[0], self.character_size[1])
        tree_surface_top = pygame.Rect(pos[0], pos[1], tree_size[0], 1)

    def collision_plate(self, action, pos):
        plate_size = [44, 50]
        character_surface = pygame.Rect(self.character_pos[0], self.character_pos[1]+20, self.character_size[0], self.character_size[1])
        plate_surface = pygame.Rect(pos[0], pos[1], plate_size[0], plate_size[1])
        if character_surface.colliderect(plate_surface):
            return action