import pygame
import os

from pygame.locals import K_UP, K_DOWN, K_SPACE
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, DUCKING_HAMMER, HAMMER_TYPE, JUMPING_HAMMER, RUNNING, JUMPING, JUMP_VELOCITY, RUNNING_HAMMER, X_POSITION_DINO, Y_POSITION_DINO, Y_POSITION_DUCK, DEFAULT_TYPE, JUMP_SOUND, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD


DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite):
    def __init__(self) -> None:
        Sprite.__init__(self).__init__()
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = X_POSITION_DINO 
        self.rect.y = Y_POSITION_DINO
        self.mask = pygame.mask.from_surface(self.image)
        self.step_index = 0
        self.dino_run = True
        self.dino_down = False
        self.dino_jump = False
        self.jump_vel = JUMP_VELOCITY
        self.jump_sound = JUMP_SOUND
        self.jump_sound_is_played = False
        self.setup_state()
    
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
        
    def update(self, user_input):        
        if self.dino_run:
            self.run()
            
        if self.dino_jump:
            self.jump()
            
        if self.dino_down:
            self.down()
              
        if (user_input[K_UP] and not self.dino_jump and not user_input[K_DOWN]) or (user_input[K_SPACE] and not self.dino_jump and not user_input[K_DOWN]):
            self.dino_run = False
            self.dino_jump = True  
            if not self.jump_sound_is_played:
                self.jump_sound.set_volume(1)
                self.jump_sound.play()
                self.jump_sound_is_played = True
        elif user_input[K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_down = True
            if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_SPACE]:
                self.dino_down = False
                self.dino_jump = True  
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_down = False
            self.dino_jump = False
        
        
        if self.step_index >= 10:
            self.step_index = 0
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = X_POSITION_DINO
        self.rect.y = Y_POSITION_DINO
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.mask = pygame.mask.from_surface(self.image)
        self.jump_sound_is_played = False
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4 #type: ignore
            if pygame.key.get_pressed()[K_DOWN]:
                self.jump_vel -= 1.6
            else:
                self.jump_vel -= 0.8

        if self.rect.y >= Y_POSITION_DINO:
            self.rect.y = Y_POSITION_DINO
            self.dino_jump = False
            self.jump_vel = JUMP_VELOCITY
            
    def down(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = X_POSITION_DINO
        self.rect.y = Y_POSITION_DUCK
        self.step_index += 1