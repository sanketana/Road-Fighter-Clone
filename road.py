import pygame
from settings import *

class Road:
    def __init__(self):
        self.length = 50
        self.gap = 50
        self.width = 5
        self.color = (255, 255, 255)
        self.offset = 0

    def draw(self, screen, speed):
        self.offset = 0

        while (self.offset + self.length) < height:
            x = (width/2) - (self.width/2)
            rect = pygame.Rect(x, self.offset, self.width, self.length)
            pygame.draw.rect(screen, self.color, rect)
            
            self.offset += self.length + self.gap

