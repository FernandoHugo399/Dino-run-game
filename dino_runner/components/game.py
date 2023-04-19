from token import AMPEREQUAL
import pygame
pygame.init()
pygame.mixer.init()

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_SPEED, X_POSITION_BACKGROUND, Y_POSITION_BACKGROUND, SCORE_SOUND, SCORE_TXT
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component


class Game:
    def __init__(self): 
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.game_speed = GAME_SPEED
        self.x_pos_bg = X_POSITION_BACKGROUND
        self.y_pos_bg = Y_POSITION_BACKGROUND
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.death_count = 0
        self.sound_score = SCORE_SOUND
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
    
    def execute(self): 
        self.running = True
        while self.running:
            if not self.playing: # Vai mostrar o menu antes do jogo começar e quando o jogador perde
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self) 
        self.update_score()
    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0: 
            if self.game_speed < 60:
                self.game_speed += 5
            if self.score % 100 == 0:
                self.score += 1
            self.sound_score.set_volume(0.5)
            self.sound_score.play()
            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((200, 200, 200))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_score(self):
        draw_message_component(
            f"score: {self.score} ",
            self.screen,
            pos_x_center = 1200,
            pos_y_center = 50
        )
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((220, 220, 220))  
        if self.death_count == 0:
            draw_message_component("Press any key to start.", self.screen)
        else:
            draw_message_component("Press any key to play again.", self.screen, pos_y_center = self.half_screen_height - 40)
            draw_message_component(f"Your score: {self.score}", self.screen, pos_y_center = self.half_screen_height - 80) 
            draw_message_component(f"Death count: {self.death_count}", self.screen, pos_y_center=self.half_screen_height )
            draw_message_component("Better results:", self.screen, pos_y_center=self.half_screen_height + 80)
            self.best_scores()
            
            

        pygame.display.update()
        self.handle_events_on_menu()
        
    def best_scores(self):
        with open(f'{SCORE_TXT}', 'r') as archive:
            all_values = []
            for valor in archive:
                all_values.append(int(valor.replace("\n", '')))
                all_values.sort(reverse=True)
                if len(all_values) > 5:
                    all_values.pop()
            
            count = 0
            while count < len(all_values):
                draw_message_component(f"{count + 1}° - {all_values[count]}", self.screen, pos_y_center=self.half_screen_height + 80 + ((count+1) * 35))
                count += 1
            