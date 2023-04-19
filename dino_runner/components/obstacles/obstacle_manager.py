import pygame

from random import randint
from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.piterodactyl import Piterodactyl 
from dino_runner.utils.constants import DEATH_SOUND, GAME_OVER, DINO_DEAD



class ObstacleManager:
    def __init__(self):
        self.cactus = Cactus()
        self.piterodactyl = Piterodactyl()
        self.obstacles = []
        self.death_sound = DEATH_SOUND
        self.obstacles_group = pygame.sprite.Group()
        
    def update(self, game):
        Obstacle_type = [ 
            self.cactus,
            self.piterodactyl
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(Obstacle_type[randint(0, 1)]) 
            self.obstacles_group.add(self.cactus)
            self.obstacles_group.add(self.piterodactyl)
        self.verify_collide(game)
        
    def verify_collide(self, game):
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            collide = pygame.sprite.spritecollide(game.player, self.obstacles_group, True, pygame.sprite.collide_mask) # type: ignore
            if len(collide) != 0:
                if not game.player.has_power_up:
                    game.player.image = DINO_DEAD
                    game.draw()
                    self.death_sound.set_volume(1)
                    self.death_sound.play()
                    pygame.time.delay(1000)
                    obstacle.restart_position()
                    game.playing = False
                    game.death_count += 1
                    game.update_list_score(game.score)
                else: 
                    self.reset_obstacles()
                    self.cactus = Cactus()
                    self.piterodactyl = Piterodactyl()
        
    def reset_obstacles(self):
        self.obstacles = [] 
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)