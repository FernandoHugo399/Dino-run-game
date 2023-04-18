import pygame

from random import randint
from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.piterodactyl import Piterodactyl 
from dino_runner.utils.constants import DEATH_SOUND

cactus = Cactus()
piterodactyl = Piterodactyl()
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound = DEATH_SOUND
        self.obstacles_group = pygame.sprite.Group()
        self.obstacles_group.add(cactus)
        self.obstacles_group.add(piterodactyl)
    
    def update(self, game):
        Obstacle_type = [ 
            cactus,
            piterodactyl
        ]
        print(self.obstacles)
        if len(self.obstacles) == 0:
            print('ok')
            self.obstacles.append(Obstacle_type[randint(0, 1)]) 
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            collide = pygame.sprite.spritecollide(game.player, self.obstacles_group, True, pygame.sprite.collide_mask) # type: ignore
            if len(collide) != 0:
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