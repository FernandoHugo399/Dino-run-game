import pygame

from random import randint
from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.piterodactyl import Piterodactyl 
from dino_runner.utils.constants import DEATH_SOUND


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound = DEATH_SOUND
    
    def update(self, game):
        Obstacle_type = [ 
            Cactus(),
            Piterodactyl()
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(Obstacle_type[randint(0, 1)]) 
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                self.death_sound.set_volume(1)
                self.death_sound.play()
                pygame.time.delay(1000)
                game.playing = False
                game.death_count += 1
    
    def reset_obstacles(self):
        self.obstacles = [] 
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)