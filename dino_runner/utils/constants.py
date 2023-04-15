import pygame
import os

# Global Constants
TITLE = "Dino Runner" # Título da aplicação
SCREEN_HEIGHT = 600 # Altura da tela de exibição
SCREEN_WIDTH = 1100 # Largura da tela de exibição
FPS = 30 # Frames por segundo
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets") # Diretório das imagens
GAME_SPEED = 20 # Define a velocidade do jogo

X_POSITION_BACKGROUND = 0 # Posição eixo x background
Y_POSITION_BACKGROUND = 380 # Posição eixo y background
X_POSITION_DINO = 80 # Posição eixo x do dinossauro
Y_POSITION_DINO = 310 # Posição eixo y do dionossauro

JUMP_VELOCITY = 8.5 # Velocidade do pulo do dinossauro

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png")) # Carrega o favicon do dinossauro

RUNNING = [ # Carrega as imagens dinossauro enquanto corre
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [ # Carrega as imagens dinossauro enquanto corre e com o escudo ativo
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [ # Carrega as imagens dinossauro enquant corre e com o martelo ativo
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png")) # Efetua a ação de pular
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png")) # Efetua a ação de pular com o escudo
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png")) # Efetua a ação de pular com o martelo

DUCKING = [ # Carrega as imagens dinossauro enquanto corre abaixado
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [ # Carrega as imagens dinossauro enquanto corre abaixado com o escudo
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [ # Carrega as imagens dinossauro enquanto corre abaixado com o martelo
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [ # Carrega as imagenss pequenos cactos
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [ # Carrega as imagenss grandes cactos
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [ # Carrega as imagenss pequenos cactos
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')) # Carrega a imagem da núvem
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')) # Carrega a imagem do escudo
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')) # Carrega a imagem do martelo

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png')) # Carrega o caminho que o dinossauro percorre durante o jogo

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png')) # Carrega uma imagem mostrando a vida do dinossauro

DEFAULT_TYPE = "default"
