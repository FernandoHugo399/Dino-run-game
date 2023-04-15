import pygame
import os

from pygame.locals import K_UP, K_DOWN
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNNING, JUMPING, JUMP_VELOCITY, X_POSITION_DINO, Y_POSITION_DINO, DEFAULT_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING}
DUCK_IMG = {DEFAULT_TYPE: DUCKING}

class Dinosaur(Sprite):
    def __init__(self) -> None:
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POSITION_DINO 
        self.dino_rect.y = Y_POSITION_DINO
        self.step_index = 0
        self.dino_run = True
        self.dino_down = False
        self.dino_jump = False
        self.jump_vel = JUMP_VELOCITY
        
    def update(self, user_input):        
        if self.dino_run:
            self.run()
            
        if self.dino_jump:
            self.jump()
            
        if self.dino_down:
            self.down()
        
        if user_input[K_UP] and not self.dino_jump and not user_input[K_DOWN]:
            self.dino_run = False
            self.dino_jump = True  
        elif user_input[K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_down = True
            if pygame.key.get_pressed()[K_UP]:
                self.dino_down = False
                self.dino_jump = True  
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_down = False
            self.dino_jump = False
        
        if self.step_index >= 10:
            self.step_index = 0
            
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POSITION_DINO
        self.dino_rect.y = Y_POSITION_DINO
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #type: ignore
            if pygame.key.get_pressed()[K_DOWN]:
                self.jump_vel -= 1.6
            else:
                self.jump_vel -= 0.8
                
        if self.dino_rect.y >= Y_POSITION_DINO:
            self.dino_rect.y = Y_POSITION_DINO
            self.dino_jump = False
            self.jump_vel = JUMP_VELOCITY
            
    def down(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POSITION_DINO
        self.dino_rect.y = Y_POSITION_DINO + 34
        self.step_index += 1