import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_SPEED, X_POSITION_BACKGROUND, Y_POSITION_BACKGROUND, BIRD, RUNNING
from sys import exit


class Game: # Cria a classe para iniciar o jogo
    def __init__(self): 
        pygame.init() # Inicia a aplicação com o pygame
        pygame.display.set_caption(TITLE) # Renomeia o nome do jogo
        pygame.display.set_icon(ICON) # Altera o ícone do jogo
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Define o tamanho da tela apresentada para o usuário
        self.clock = pygame.time.Clock()
        self.playing = False # Se o jogo vai executar ou não
        self.game_speed = GAME_SPEED # Define a velocidade do jogo
        self.x_pos_bg = X_POSITION_BACKGROUND # Posição eixo x background
        self.y_pos_bg = Y_POSITION_BACKGROUND # Posição eixo y background
        
        self.player = Dinosaur() # Adiciona o dinossauro ao jogo

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit() # Termina a execução do pygame
        exit() # Força a aplicação a parar de forma brusca

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Caso o evento seja de sair do jogo, ele encerra a aplicação
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed() # Pega a tecla pressionada pelo usuário
        self.player.update(user_input) # Passa a tecla pressionada para o tratamento dela

    def draw(self):
        self.clock.tick(FPS) # Define a quantidade de frames por segundo que a aplicação irá ter
        self.screen.fill((200, 200, 200)) # Define o fundo da aplicação
        self.draw_background() # Mostra o background - Caminho no qual o dinossauro irá passar
        
        self.player.draw(self.screen) # Desenha o dinossauro na tela 
        
        pygame.display.update() # Atualiza uma porção da tela de exibição - Caso não seja passado parâmetros, atualiza tudo
        pygame.display.flip() # Atualiza o conteúdo de toda a tela de exibição
        

    def draw_background(self): # Mostra o background - Caminho no qual o dinossauro irá passar
        image_width = BG.get_width() # Retorna a largura da tela
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) # Mostra o background de acordo com a posição do eixo y e eixo x
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) # Vai mostrar outro background exatamente após o fim da primeira imagem
        if self.x_pos_bg <= -image_width: # Caso o eixo x já tenha mostrado todo o background
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) # Vai impedir que tenha falhas no meio do caminho
            self.x_pos_bg = 0 # faz com que a imagem do fundo fique em looping
        self.x_pos_bg -= self.game_speed # Quantidade de pixeis que irão diminuir de acordo com os frames que forem contados