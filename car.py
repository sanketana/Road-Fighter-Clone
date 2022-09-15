import pygame
from settings import *

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        self.image = pygame.image.load('images/red_car.png')
        self.rect = self.image.get_rect(midbottom = (width/2, height - car_offset))
        self.speed = 0
        self.lives = 3

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x