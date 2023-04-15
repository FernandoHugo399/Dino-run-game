import pygame
import os

from pygame.locals import K_UP, K_DOWN
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNNING, JUMPING, JUMP_VELOCITY, X_POSITION_DINO, Y_POSITION_DINO, DEFAULT_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING} # Recebe as imagens para animação de corrida
JUMP_IMG = {DEFAULT_TYPE: JUMPING} # Recebe as imagens para animação de pulo
DUCK_IMG = {DEFAULT_TYPE: DUCKING}

class Dinosaur(Sprite): # São objetos - Objetos da pasta assets
    def __init__(self) -> None:
        self.type = DEFAULT_TYPE # Define o tipo padrão da imagem
        self.image = RUN_IMG[self.type][0] # Está pegando a primeira imagem nas constante RUNNING
        self.dino_rect = self.image.get_rect() # Recebe as medidas do retângulo do dinossauro
        #print(self.dino_rect.top)
        #print(self.dino_rect.right)
        #print(self.dino_rect.bottom)
        #print(self.dino_rect.left)
        self.dino_rect.x = X_POSITION_DINO # Posição x do Dino
        self.dino_rect.y = Y_POSITION_DINO # Posição y do Dino
        self.step_index = 0 # Índice de passos
        self.dino_run = True # Variável que define se o Dino está correndo
        self.dino_down = False # Variável que define se o Dino está abaixado
        self.dino_jump = False # Variável que define se o Dino está pulando
        self.jump_vel = JUMP_VELOCITY # Define a velocidade de pulo do dinossauro
        
    def update(self, user_input):        
        if self.dino_run: # Caso o Dino esteja correndo
            self.run()
            
        if self.dino_jump: # Caso o Dino pule
            self.jump()
            
        if self.dino_down: # Caso o Dino esteja abaixado
            self.down()
        
        if user_input[K_UP] and not self.dino_jump and not user_input[K_DOWN]: # Caso a key_up seja clicada
            self.dino_run = False
            self.dino_jump = True  
        elif user_input[K_DOWN] and not self.dino_jump: # Caso a key_down seja clicada
            self.dino_run = False
            self.dino_down = True
            if pygame.key.get_pressed()[K_UP]:
                self.dino_down = False
                self.dino_jump = True  
        elif not self.dino_jump: # Caso não esteja pulando
            self.dino_run = True
            self.dino_down = False
            self.dino_jump = False
        
        if self.step_index >= 10: # Caso o contador de passo chegue a 10
            self.step_index = 0
            
    def draw(self, screen): # Desenha a imagem do dinossauro na tela
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
    def run(self): # Método responsável pela animação de corrida
        self.image = RUN_IMG[self.type][self.step_index // 5] # Responsável por alternar as imagens
        self.dino_rect = self.image.get_rect() # Recebe as medidas do retângulo do dinossauro
        self.dino_rect.x = X_POSITION_DINO # Atribui a posição X do Dino
        self.dino_rect.y = Y_POSITION_DINO # Atribui a posição Y do Dino
        self.step_index += 1 # Aumenta o contador dos passos
        

    def jump(self): # Método responsável pela animação de pulo
        self.image = JUMP_IMG[self.type] # Recebe a imagem do pulo
        if self.dino_jump: # Caso o dino esteja pulando
            self.dino_rect.y -= self.jump_vel * 4 # A imagem do dino vai mudar o eixo Y  # type: ignore
            if pygame.key.get_pressed()[K_DOWN]: # Desce mais rápido caso seja clicado a key_down
                self.jump_vel -= 1.6 # Diminui a velocidade do pulo
            else:
                self.jump_vel -= 0.8 # Diminui a velocidade do pulo
                
        if self.dino_rect.y >= Y_POSITION_DINO: # Verifica se já tocou o solo
            self.dino_rect.y = Y_POSITION_DINO # Volta a posição original do pulo
            self.dino_jump = False # Desativa o pulo
            self.jump_vel = JUMP_VELOCITY # Deixa a velocidade pulo padrão
            
    def down(self): # Método responsável pela animação de abaixar
        self.image = DUCK_IMG[self.type][self.step_index // 5] # Responsável por alternar as imagens
        self.dino_rect = self.image.get_rect() # Recebe as medidas do retângulo do dinossauro
        self.dino_rect.x = X_POSITION_DINO # Atribui a posição X do Dino
        self.dino_rect.y = Y_POSITION_DINO + 34 # Atribui a posição Y do Dino
        self.step_index += 1 # Aumenta o contador dos passos