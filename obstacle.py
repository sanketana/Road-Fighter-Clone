import pygame
from settings import *
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        self.image = pygame.image.load('images/blue_car.png')
        self.gap = 50
        self.x = random.randint(self.gap, width-self.gap)
        self.y = 20
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.speed = 7

    def update(self):
        self.rect.y += self.speed