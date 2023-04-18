import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        Sprite.__init__(self)
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.mask = pygame.mask.from_surface(self.image[self.type])
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed, obstacle):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle.pop()
    
    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))